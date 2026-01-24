# Changelog

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
