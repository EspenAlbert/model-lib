# flake8: noqa
from __future__ import annotations

import logging
from contextlib import suppress
from functools import singledispatch
from pathlib import Path
from typing import Any, Callable, Dict, Mapping, Optional, Tuple, Type, TypeVar, cast

from model_lib.constants import (
    FileFormat,
    FileFormatT,
    ModelRawT,
    PayloadParser,
    PayloadT,
    RegisteredPayloadT,
)
from model_lib.errors import (
    PayloadError,
    PayloadParserAlreadyExistError,
    PayloadParserNotFoundError,
    UnknownModelError,
)
from model_lib.model_base import model_name_to_t
from pydantic import AliasChoices, AliasPath, BaseModel
from zero_3rdparty.object_name import as_name

from .env_serialize import parse_env_str
from .json_serialize import parse as parse_json
from .toml_serialize import parse_toml_str
from .yaml_serialize import parse_yaml_str

logger = logging.getLogger(__name__)
_registered_parsers: Dict[Type, PayloadParser] = {}
T = TypeVar("T")


_format_parsers: Dict[FileFormat, Callable[[str], ModelRawT]] = {
    FileFormat.json: parse_json,
    FileFormat.yaml: parse_yaml_str,
    FileFormat.yml: parse_yaml_str,
    FileFormat.toml: parse_toml_str,
    FileFormat.toml_compact: parse_toml_str,
    FileFormat.env: parse_env_str,
}
_file_format_to_raw_format: Dict[str, FileFormat] = {
    ".json": FileFormat.json,
    ".yaml": FileFormat.yaml,
    ".yml": FileFormat.yaml,
    ".toml": FileFormat.toml,
    ".env": FileFormat.env,
}


def parse_model(
    payload: PayloadT,
    t: Optional[Type[T]] = None,
    format: FileFormat | str = FileFormat.json,
    extra_kwargs: Mapping[str, Any] | None = None,
) -> T:
    model, _ = parse_model_metadata(payload, t=t, format=format, extra_kwargs=extra_kwargs)
    return model


def create_model(cls: Type[T], model_args: dict | Any, extra_kwargs: Mapping[str, Any]) -> T:
    """Raises ValidationError."""
    model_kwargs = isinstance(model_args, dict)
    if extra_kwargs:
        return (
            cls(**(model_args | extra_kwargs))  # type: ignore
            if model_kwargs
            else cls(model_args, **extra_kwargs)  # type: ignore
        )
    return cls(**model_args) if model_kwargs else cls(model_args)  # type: ignore


def _lookup_safe(model_name: str) -> Type | None:
    with suppress(UnknownModelError):
        return model_name_to_t(model_name)
    return None


def _is_env_format(payload: PayloadT, format: FileFormat | str) -> bool:
    if isinstance(payload, Path):
        file_format = payload.suffix or payload.name
        format = _file_format_to_raw_format.get(file_format, format)
    return format == FileFormat.env


def _alias_input_keys(alias: Any) -> set[str]:
    """Top-level env keys Pydantic reads a field from for the given alias."""
    if isinstance(alias, str):
        return {alias}
    if isinstance(alias, AliasPath):
        # env payloads are flat, so only a single-segment path can resolve
        first = alias.path[0] if alias.path else None
        return {first} if len(alias.path) == 1 and isinstance(first, str) else set()
    if isinstance(alias, AliasChoices):
        keys: set[str] = set()
        for choice in alias.choices:
            keys.update(_alias_input_keys(choice))
        return keys
    return set()


def _accepted_model_keys(model_type: type[BaseModel]) -> set[str]:
    config = model_type.model_config
    validate_by_alias = bool(config.get("validate_by_alias", True))
    validate_by_name = bool(config.get("validate_by_name") or config.get("populate_by_name"))
    keys: set[str] = set()
    for name, field in model_type.model_fields.items():
        if validate_by_name or not validate_by_alias:
            keys.add(name)
        if not validate_by_alias:
            continue
        alias = field.validation_alias if field.validation_alias is not None else field.alias
        if alias is None:
            keys.add(name)
        else:
            keys.update(_alias_input_keys(alias))
    return keys


def _env_model_args(model_args: Any, model_type: Any, payload: PayloadT, format: FileFormat | str) -> Any:
    """Drop env keys the model does not declare, so unrelated secrets never reach the model or its errors."""
    if not isinstance(model_args, dict) or not _is_env_format(payload, format):
        return model_args
    if not (isinstance(model_type, type) and issubclass(model_type, BaseModel)):
        return model_args
    model_cls = cast(type[BaseModel], model_type)
    accepted = _accepted_model_keys(model_cls)
    extras = sorted(key for key in model_args if key not in accepted)
    if not extras:
        return model_args
    if model_cls.model_config.get("extra") == "forbid":
        raise PayloadError(payload="", message=f"unexpected env keys: {extras}")
    return {key: value for key, value in model_args.items() if key in accepted}


def parse_model_metadata(
    payload: PayloadT,
    format: FileFormat | str = FileFormat.json,
    t: Type[T] | None = None,
    extra_kwargs: Mapping[str, Any] | None = None,
) -> Tuple[T, dict[str, Any]]:
    """raises PayloadError or ValidationError."""
    try:
        parsed_payload = parse_payload(payload, format)
    except Exception as e:
        raise PayloadError(payload, message=f"parse error: {e!r}") from e
    # from constants
    # MODEL_DUMP_KEY = "model"
    # METADATA_DUMP_KEY = "metadata"
    # METADATA_MODEL_NAME_FIELD = "model_name"
    # METADATA_MODEL_NAME_BACKUP_FIELD = "model_name_backup"
    if not isinstance(parsed_payload, dict):
        raise PayloadError(payload=payload, message="not a dictionary")
    metadata = parsed_payload.get("metadata", {})
    model_args = parsed_payload.get("model", parsed_payload)
    if t:
        return create_model(t, _env_model_args(model_args, t, payload, format), extra_kwargs or {}), metadata
    model_name = metadata.get("model_name")
    model_name_backup = metadata.get("model_name_backup")
    model_cls: Type[T] | None = _lookup_safe(model_name) or _lookup_safe(model_name_backup)  # ty: ignore[invalid-assignment]
    if model_cls is None:
        message = f"unknown models: {model_name}, {model_name_backup}"
        raise PayloadError(parsed_payload, message, metadata)
    return create_model(
        model_cls, _env_model_args(model_args, model_cls, payload, format), extra_kwargs or {}
    ), metadata


def parse_model_name_kwargs_list(payload: Any) -> list:
    raw_events: list = cast(list, parse_payload(payload))
    parsed_events = []
    for cls_name_kwargs in raw_events:
        cls_name, kwargs = cls_name_kwargs.popitem()
        cls = model_name_to_t(cls_name)
        parsed_events.append(cls(**kwargs))
    return parsed_events


def parse_list(payload: PayloadT, format: FileFormatT = FileFormat.json) -> list:
    raw_list = parse_payload(payload, format)
    if not isinstance(raw_list, list):
        raise PayloadError(payload, message="not a list")
    return raw_list


def parse_dict(payload: PayloadT, format: FileFormatT = FileFormat.json) -> dict:
    raw_dict = parse_payload(payload, format)
    if not isinstance(raw_dict, dict):
        raise PayloadError(payload, message="not a dictionary")
    return raw_dict


@singledispatch
def parse_payload(payload: object, format=FileFormat.json) -> ModelRawT:
    raise PayloadParserNotFoundError(payload=payload, format=format)


@parse_payload.register
def _parse_str(payload: str, format=FileFormat.json):
    parser = _format_parsers[format]
    return parser(payload)


@parse_payload.register
def _parse_bytes(payload: bytes, format=FileFormat.json):
    return parse_payload(payload.decode("utf-8"), format)


@parse_payload.register
def _parse_path(payload: Path, format=FileFormat.json):
    # dotfiles like `.env` have suffix="" so fall back to checking the full name
    file_format = payload.suffix or payload.name
    if raw_format := _file_format_to_raw_format.get(file_format):
        if raw_format != format:
            format = file_format.lstrip(".")
    else:
        logger.warning(f"attempting to parse a file {payload.name} as {format}")
    return parse_payload(payload.read_text(), format)


@parse_payload.register
def _parse_dict(payload: dict, format=FileFormat.json):
    return payload


@parse_payload.register
def _parse_list(payload: list, format=FileFormat.json):
    return payload


def get_parsers() -> dict[Type, PayloadParser]:
    return _registered_parsers


def register_parser(payload_type: Type, call: PayloadParser) -> None:
    if previous := _registered_parsers.get(payload_type):
        raise PayloadParserAlreadyExistError(as_name(previous), as_name(call))
    _registered_parsers[payload_type] = call
    parser_name = as_name(call)
    logger.info(f"custom parser: {parser_name} for {payload_type}")
    parse_payload.register(call)
