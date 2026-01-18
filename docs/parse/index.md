<!-- === DO_NOT_EDIT: pkg-ext header === -->
# parse

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`parse_dict`](#parse_dict_def)
- [`parse_list`](#parse_list_def)
- [`parse_model`](#parse_model_def)
- [`parse_payload`](#parse_payload_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext parse_dict_def === -->
### function: `parse_dict`
- [source](../../model_lib/serialize/parse.py#L132)
> **Since:** 0.100.0

```python
def parse_dict(payload: ~RegisteredPayloadT | str | bytes | Path | dict | list, format: FileFormat | str = 'json') -> dict:
    ...
```
<!-- === OK_EDIT: pkg-ext parse_dict_def === -->
<!-- === DO_NOT_EDIT: pkg-ext parse_list_def === -->
### function: `parse_list`
- [source](../../model_lib/serialize/parse.py#L125)
> **Since:** 0.100.0

```python
def parse_list(payload: ~RegisteredPayloadT | str | bytes | Path | dict | list, format: FileFormat | str = 'json') -> list:
    ...
```
<!-- === OK_EDIT: pkg-ext parse_list_def === -->
<!-- === DO_NOT_EDIT: pkg-ext parse_model_def === -->
### function: `parse_model`
- [source](../../model_lib/serialize/parse.py#L50)
> **Since:** 0.100.0

```python
def parse_model(payload: ~RegisteredPayloadT | str | bytes | Path | dict | list, t: type[~T] | None = None, format: FileFormat | str = 'json', extra_kwargs: Mapping[str, Any] | None = None) -> ~T:
    ...
```
<!-- === OK_EDIT: pkg-ext parse_model_def === -->
<!-- === DO_NOT_EDIT: pkg-ext parse_payload_def === -->
### function: `parse_payload`
- [source](../../model_lib/serialize/parse.py#L139)
> **Since:** 0.100.0

```python
def parse_payload(payload: object, format = 'json') -> dict | list:
    ...
```
<!-- === OK_EDIT: pkg-ext parse_payload_def === -->