<!-- === DO_NOT_EDIT: pkg-ext header === -->
# dump

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`IgnoreFalsy`](#ignorefalsy_def)
- [`dump_as_dict`](#dump_as_dict_def)
- [`dump_as_list`](#dump_as_list_def)
- [`dump_as_str`](#dump_as_str_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext ignorefalsy_def === -->
<a id="ignorefalsy_def"></a>

### class: `IgnoreFalsy`
- [source](../../model_lib/dump_functions.py#L17)
> **Since:** 0.100.0

```python
class IgnoreFalsy(BaseModel):
    ...
```
<!-- === OK_EDIT: pkg-ext ignorefalsy_def === -->
<!-- === DO_NOT_EDIT: pkg-ext dump_as_dict_def === -->
<a id="dump_as_dict_def"></a>

### function: `dump_as_dict`
- [source](../../model_lib/serialize/dump.py#L67)
> **Since:** 0.100.0

```python
def dump_as_dict(instance: object) -> dict:
    ...
```
<!-- === OK_EDIT: pkg-ext dump_as_dict_def === -->
<!-- === DO_NOT_EDIT: pkg-ext dump_as_list_def === -->
<a id="dump_as_list_def"></a>

### function: `dump_as_list`
- [source](../../model_lib/serialize/dump.py#L72)
> **Since:** 0.100.0

```python
def dump_as_list(instance: Iterable[~ModelT]) -> list:
    ...
```
<!-- === OK_EDIT: pkg-ext dump_as_list_def === -->
<!-- === DO_NOT_EDIT: pkg-ext dump_as_str_def === -->
<a id="dump_as_str_def"></a>

### function: `dump_as_str`
- [source](../../model_lib/serialize/dump.py#L55)
> **Since:** 0.100.0

```python
def dump_as_str(instance: object, format: FileFormat | str) -> str:
    ...
```

>>> dump_as_str('', "json")
''
<!-- === OK_EDIT: pkg-ext dump_as_str_def === -->