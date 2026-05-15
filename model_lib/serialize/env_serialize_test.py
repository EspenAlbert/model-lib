from pathlib import Path
from typing import cast

import pytest

from model_lib.constants import FileFormat
from model_lib.serialize.dump import dump_as_str
from model_lib.serialize.env_serialize import dump_env_str, parse_env_str
from model_lib.serialize.parse import parse_payload

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
