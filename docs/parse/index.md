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
<a id="parse_dict_def"></a>

### function: `parse_dict`
- [source](../../model_lib/serialize/parse.py#L130)
> **Since:** 0.100.0

```python
def parse_dict(
    payload: ~RegisteredPayloadT | str | bytes | Path | dict | list, format: FileFormat | str = "json"
) -> dict: ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext parse_dict_def === -->
<!-- === DO_NOT_EDIT: pkg-ext parse_list_def === -->
<a id="parse_list_def"></a>

### function: `parse_list`
- [source](../../model_lib/serialize/parse.py#L123)
> **Since:** 0.100.0

```python
def parse_list(
    payload: ~RegisteredPayloadT | str | bytes | Path | dict | list, format: FileFormat | str = "json"
) -> list: ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext parse_list_def === -->
<!-- === DO_NOT_EDIT: pkg-ext parse_model_def === -->
<a id="parse_model_def"></a>

### function: `parse_model`
- [source](../../model_lib/serialize/parse.py#L54)
> **Since:** 0.100.0

```python
def parse_model(
    payload: ~RegisteredPayloadT | str | bytes | Path | dict | list,
    t: type[~T] | None = None,
    format: FileFormat | str = "json",
    extra_kwargs: Mapping[str, Any] | None = None,
) -> ~T: ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext parse_model_def === -->
<!-- === DO_NOT_EDIT: pkg-ext parse_payload_def === -->
<a id="parse_payload_def"></a>

### function: `parse_payload`
- [source](../../model_lib/serialize/parse.py#L137)
> **Since:** 0.100.0

```python
def parse_payload(payload: object, format="json") -> dict | list: ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext parse_payload_def === -->