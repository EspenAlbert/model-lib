<!-- === DO_NOT_EDIT: pkg-ext header === -->
# yaml

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`allow_duplicate_anchors`](#allow_duplicate_anchors_def)
- [`edit_helm_template`](#edit_helm_template_def)
- [`edit_yaml`](#edit_yaml_def)
- [`multiline_pipe_style`](#multiline_pipe_style_def)
- [`no_yaml_anchors`](#no_yaml_anchors_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext edit_helm_template_def === -->
<a id="edit_helm_template_def"></a>

### class: `edit_helm_template`
- [source](../../model_lib/serialize/yaml_serialize.py#L103)
> **Since:** 0.100.0

```python
class edit_helm_template:
    ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext edit_helm_template_def === -->
<!-- === DO_NOT_EDIT: pkg-ext edit_yaml_def === -->
<a id="edit_yaml_def"></a>

### class: `edit_yaml`
- [source](../../model_lib/serialize/yaml_serialize.py#L66)
> **Since:** 0.100.0

```python
class edit_yaml:
    ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext edit_yaml_def === -->
<!-- === DO_NOT_EDIT: pkg-ext multiline_pipe_style_def === -->
<a id="multiline_pipe_style_def"></a>

### class: `multiline_pipe_style`
- [source](../../model_lib/serialize/yaml_serialize.py#L182)
> **Since:** 0.100.0

```python
class multiline_pipe_style:
    ...
```

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext multiline_pipe_style_def === -->
<!-- === DO_NOT_EDIT: pkg-ext no_yaml_anchors_def === -->
<a id="no_yaml_anchors_def"></a>

### class: `no_yaml_anchors`
- [source](../../model_lib/serialize/yaml_serialize.py#L201)
> **Since:** 0.100.0

```python
class no_yaml_anchors:
    ...
```

Context manager to disable YAML anchors/aliases during serialization.

This prevents duplicate objects from being represented as anchors (*id001)
and aliases (&id001), which can happen with datetime objects or other
repeated values in the data structure.

Usage:
    with no_yaml_anchors():
        yaml_str = dump(data, "yaml")

### Changes

| Version | Change |
|---------|--------|
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext no_yaml_anchors_def === -->
<!-- === DO_NOT_EDIT: pkg-ext allow_duplicate_anchors_def === -->
<a id="allow_duplicate_anchors_def"></a>

### class: `allow_duplicate_anchors`
- [source](../../model_lib/serialize/yaml_serialize.py#L241)
> **Since:** unreleased

```python
class allow_duplicate_anchors:
    ...
```

Context manager to allow duplicate YAML anchors during parsing.

Some YAML files (e.g. codegen configs) reuse anchor names across sections.
PyYAML raises ComposerError for these. This temporarily swaps in a loader
that drops old anchors before re-registering.

Usage:
    with allow_duplicate_anchors():
        data = parse_payload(path)

### Changes

| Version | Change |
|---------|--------|
| unreleased | Made public |
<!-- === OK_EDIT: pkg-ext allow_duplicate_anchors_def === -->