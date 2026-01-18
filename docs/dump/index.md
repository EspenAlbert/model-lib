<!-- === DO_NOT_EDIT: pkg-ext header === -->
# dump

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`IgnoreFalsy`](#ignorefalsy_def)
- [`dump`](#dump_def)
- [`dump_as_dict`](#dump_as_dict_def)
- [`dump_as_list`](#dump_as_list_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext ignorefalsy_def === -->
### class: `IgnoreFalsy`
- [source](../../model_lib/dump_functions.py#L17)
> **Since:** 0.100.0

```python
class IgnoreFalsy(BaseModel):
    ...
```
<!-- === OK_EDIT: pkg-ext ignorefalsy_def === -->
<!-- === DO_NOT_EDIT: pkg-ext dump_def === -->
### function: `dump`
- [source](../../model_lib/serialize/json_serialize.py#L19)

```python
def dump(instance: Any) -> str:
    ...
```
<!-- === OK_EDIT: pkg-ext dump_def === -->
<!-- === DO_NOT_EDIT: pkg-ext dump_as_dict_def === -->
### function: `dump_as_dict`
- [source](../../model_lib/serialize/dump.py#L73)
> **Since:** 0.100.0

```python
def dump_as_dict(instance: object) -> dict:
    ...
```
<!-- === OK_EDIT: pkg-ext dump_as_dict_def === -->
<!-- === DO_NOT_EDIT: pkg-ext dump_as_list_def === -->
### function: `dump_as_list`
- [source](../../model_lib/serialize/dump.py#L78)
> **Since:** 0.100.0

```python
def dump_as_list(instance: Iterable[~ModelT]) -> list:
    ...
```
<!-- === OK_EDIT: pkg-ext dump_as_list_def === -->