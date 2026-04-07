# Changelog

## 0.103.1 2026-04-07T09-37Z

### Other Changes
- Chore: pydantic-v1-import-drop


## 0.103.0 2026-03-25T14-35Z

### Parse
- fix(parse): add support for .yml file format in parse.py [0a98e8](https://github.com/EspenAlbert/model-lib/commit/0a98e8)

### Yaml
- New class `allow_duplicate_anchors`


## 0.102.2 2026-02-18T06-43Z

### __Root__
- fix: refurb fixes [d86236](https://github.com/EspenAlbert/model-lib/commit/d86236)


## 0.102.1 2026-02-11T07-33Z

### __Root__
- `__ROOT__.Event`: added base class '_Model'
- `__ROOT__.Entity`: added base class '_Model'
- `__ROOT__.StaticSettings`: added base class 'BaseSettings'
- `__ROOT__.StaticSettings`: field 'CACHE_DIR' default added: None
- `__ROOT__.StaticSettings`: field 'STATIC_DIR' default added: None

### Dump
- `dump.IgnoreFalsy`: added base class 'BaseModel'


## 0.102.0 2026-01-24T18-45Z

### __Root__
- BREAKING `__ROOT__.StaticSettings`: field 'CACHE_DIR' type: Path -> Path | None
- BREAKING `__ROOT__.StaticSettings`: field 'CACHE_DIR' default removed (was: PydanticUndefined)
- BREAKING `__ROOT__.StaticSettings`: field 'STATIC_DIR' type: Path -> Path | None
- BREAKING `__ROOT__.StaticSettings`: field 'STATIC_DIR' default removed (was: PydanticUndefined)


## 0.101.0 2026-01-19T06-30Z

### Fields
- Removed `fields.BaseModelT`
- New type_alias `UtcDatetime`
- New type_alias `UtcDatetimeMs`


## 0.100.0 2026-01-18T20-08Z

### __Root__
- New class StaticSettings
- New class Event
- New class Entity

### Dump
- New function dump_as_dict
- New function dump_as_list
- New class IgnoreFalsy
- New function dump_as_str

### Fields
- New function env_var_name
- New function env_var_names
- New function copy_and_validate
- New function field_names
- New type_alias BaseModelT

### Parse
- New function parse_model
- New function parse_list
- New function parse_dict
- New function parse_payload

### Yaml
- New class edit_yaml
- New class edit_helm_template
- New class multiline_pipe_style
- New class no_yaml_anchors
