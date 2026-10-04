from pathlib import Path
from typing import cast

import pytest
from pydantic import ConfigDict, Field, ValidationError

from model_lib import Event
from model_lib.constants import FileFormat
from model_lib.errors import PayloadError
from model_lib.serialize.dump import dump_as_str
from model_lib.serialize.env_serialize import dump_env_str, parse_env_str
from model_lib.serialize.parse import parse_model, parse_payload

_ENV_CONTENT = """\
DB_HOST=localhost
DB_PORT=5432
APP_SECRET=s3cr3t
# a comment
EMPTY_VAR=
"""


def test_dump_env_str():
    data = {"KEY": "value", "OTHER": "123"}
    result = dump_env_str(data)
    assert result == "KEY=value\nOTHER=123"


def test_dump_as_str_env():
    data = {"HOST": "localhost", "PORT": "5432"}
    result = dump_as_str(data, FileFormat.env)
    assert "HOST=localhost" in result
    assert "PORT=5432" in result


def test_parse_env_str():
    result = parse_env_str(_ENV_CONTENT)
    assert result == {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "APP_SECRET": "s3cr3t",
        "EMPTY_VAR": "",
    }


def test_parse_payload_str():
    result = cast(dict, parse_payload(_ENV_CONTENT, "env"))
    assert result["DB_HOST"] == "localhost"
    assert result["DB_PORT"] == "5432"


def test_parse_payload_path(tmp_path: Path):
    env_file = tmp_path / ".env"
    env_file.write_text(_ENV_CONTENT)
    result = cast(dict, parse_payload(env_file))
    assert result["DB_HOST"] == "localhost"
    assert result["APP_SECRET"] == "s3cr3t"


def test_dump_env_str_non_dict_raises():
    with pytest.raises(TypeError, match="env format only supports flat dicts"):
        dump_env_str(["KEY=value"])


class _EnvCredentials(Event):
    cred_path: str = Field(alias="GSHEET_CRED_PATH")
    spreadsheet_id: str = Field(alias="GSHEET_SPREADSHEET_ID")


def test_parse_model_env_ignores_undeclared_keys(tmp_path: Path):
    env_file = tmp_path / ".env"
    env_file.write_text("GSHEET_CRED_PATH=/tmp/cred.json\nGSHEET_SPREADSHEET_ID=abc\nSECRET_TOKEN=leak-me\n")
    creds = parse_model(env_file, t=_EnvCredentials)
    assert creds.cred_path == "/tmp/cred.json"
    assert creds.spreadsheet_id == "abc"
    assert not hasattr(creds, "SECRET_TOKEN")


def test_parse_model_env_error_hides_undeclared_keys(tmp_path: Path):
    env_file = tmp_path / ".env"
    env_file.write_text("GSHEET_SPREADSHEET_ID=abc\nSECRET_TOKEN=leak-me\n")
    with pytest.raises(ValidationError) as excinfo:
        parse_model(env_file, t=_EnvCredentials)
    message = str(excinfo.value)
    assert "GSHEET_CRED_PATH" in message
    assert "SECRET_TOKEN" not in message
    assert "leak-me" not in message


def test_parse_model_env_accepts_field_names(tmp_path: Path):
    env_file = tmp_path / ".env"
    env_file.write_text("cred_path=/tmp/cred.json\nspreadsheet_id=abc\n")
    creds = parse_model(env_file, t=_EnvCredentials)
    assert creds.cred_path == "/tmp/cred.json"


def test_parse_model_env_forbid_rejects_extra_keys(tmp_path: Path):
    class _Strict(Event):
        model_config = ConfigDict(extra="forbid")
        name: str

    env_file = tmp_path / ".env"
    env_file.write_text("name=espen\nextra=leak-me\n")
    with pytest.raises(PayloadError, match="unexpected env keys"):
        parse_model(env_file, t=_Strict)
