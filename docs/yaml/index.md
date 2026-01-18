<!-- === DO_NOT_EDIT: pkg-ext header === -->
# yaml

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`edit_helm_template`](#edit_helm_template_def)
- [`edit_yaml`](#edit_yaml_def)
- [`multiline_pipe_style`](#multiline_pipe_style_def)
- [`no_yaml_anchors`](#no_yaml_anchors_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext edit_helm_template_def === -->
### class: `edit_helm_template`
- [source](../../model_lib/serialize/yaml_serialize.py#L115)
> **Since:** 0.100.0

```python
class edit_helm_template:
    ...
```
<!-- === OK_EDIT: pkg-ext edit_helm_template_def === -->
<!-- === DO_NOT_EDIT: pkg-ext edit_yaml_def === -->
### class: `edit_yaml`
- [source](../../model_lib/serialize/yaml_serialize.py#L76)
> **Since:** 0.100.0

```python
class edit_yaml:
    ...
```
<!-- === OK_EDIT: pkg-ext edit_yaml_def === -->
<!-- === DO_NOT_EDIT: pkg-ext multiline_pipe_style_def === -->
### class: `multiline_pipe_style`
- [source](../../model_lib/serialize/yaml_serialize.py#L196)
> **Since:** 0.100.0

```python
class multiline_pipe_style:
    ...
```
<!-- === OK_EDIT: pkg-ext multiline_pipe_style_def === -->
<!-- === DO_NOT_EDIT: pkg-ext no_yaml_anchors_def === -->
### class: `no_yaml_anchors`
- [source](../../model_lib/serialize/yaml_serialize.py#L215)
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
<!-- === OK_EDIT: pkg-ext no_yaml_anchors_def === -->