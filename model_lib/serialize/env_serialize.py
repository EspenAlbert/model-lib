from __future__ import annotations

from io import StringIO

from dotenv import dotenv_values


def parse_env_str(data: str) -> dict:
    return dict(dotenv_values(stream=StringIO(data)))


def dump_env_str(data: object) -> str:
    if not isinstance(data, dict):
        raise TypeError(f"env format only supports flat dicts, got {type(data)}")
    return "\n".join(f"{k}={v}" for k, v in data.items())
