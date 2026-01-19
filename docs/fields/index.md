<!-- === DO_NOT_EDIT: pkg-ext header === -->
# fields

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`UtcDatetime`](#utcdatetime_def)
- [`UtcDatetimeMs`](#utcdatetimems_def)
- [`copy_and_validate`](#copy_and_validate_def)
- [`env_var_name`](#env_var_name_def)
- [`env_var_names`](#env_var_names_def)
- [`field_names`](#field_names_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext copy_and_validate_def === -->
<a id="copy_and_validate_def"></a>

### function: `copy_and_validate`
- [source](../../model_lib/pydantic_utils.py#L93)
> **Since:** 0.100.0

```python
def copy_and_validate(model: ~BaseModelT, **updates) -> ~BaseModelT:
    ...
```
<!-- === OK_EDIT: pkg-ext copy_and_validate_def === -->
<!-- === DO_NOT_EDIT: pkg-ext env_var_name_def === -->
<a id="env_var_name_def"></a>

### function: `env_var_name`
- [source](../../model_lib/pydantic_utils.py#L13)
> **Since:** 0.100.0

```python
def env_var_name(settings: BaseSettings | type[BaseSettings], field_name: str) -> str:
    ...
```
<!-- === OK_EDIT: pkg-ext env_var_name_def === -->
<!-- === DO_NOT_EDIT: pkg-ext env_var_names_def === -->
<a id="env_var_names_def"></a>

### function: `env_var_names`
- [source](../../model_lib/pydantic_utils.py#L29)
> **Since:** 0.100.0

```python
def env_var_names(settings: BaseSettings | type[BaseSettings]) -> list[str]:
    ...
```
<!-- === OK_EDIT: pkg-ext env_var_names_def === -->
<!-- === DO_NOT_EDIT: pkg-ext field_names_def === -->
<a id="field_names_def"></a>

### function: `field_names`
- [source](../../model_lib/pydantic_utils.py#L118)
> **Since:** 0.100.0

```python
def field_names(model_type: type[BaseModel] | BaseModel) -> list[str]:
    ...
```
<!-- === OK_EDIT: pkg-ext field_names_def === -->
<!-- === DO_NOT_EDIT: pkg-ext utcdatetime_def === -->
<a id="utcdatetime_def"></a>

### type_alias: `UtcDatetime`
- [source](../../model_lib/pydantic_utils.py)
> **Since:** 0.101.0

```python
UtcDatetime = typing.Annotated[<class 'datetime.datetime'>, AfterValidator(func=ensure_timezone)]
```
<!-- === OK_EDIT: pkg-ext utcdatetime_def === -->
<!-- === DO_NOT_EDIT: pkg-ext utcdatetimems_def === -->
<a id="utcdatetimems_def"></a>

### type_alias: `UtcDatetimeMs`
- [source](../../model_lib/pydantic_utils.py)
> **Since:** 0.101.0

```python
UtcDatetimeMs = typing.Annotated[<class 'datetime.datetime'>, AfterValidator(func=as_ms_precision_utc)]
```
<!-- === OK_EDIT: pkg-ext utcdatetimems_def === -->
