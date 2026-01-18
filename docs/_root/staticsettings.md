# StaticSettings

<!-- === DO_NOT_EDIT: pkg-ext staticsettings_def === -->
## class: StaticSettings
- [source](../../model_lib/static_settings.py#L10)
> **Since:** unreleased

```python
class StaticSettings(BaseSettings):
    STATIC_DIR: Path = PydanticUndefined
    CACHE_DIR: Path = PydanticUndefined
    SKIP_APP_NAME: bool = False
```
<!-- === OK_EDIT: pkg-ext staticsettings_def === -->

### Environment Variables

| Variable | Field | Type | Default |
|----------|-------|------|---------|
| `static_dir` | `STATIC_DIR` | Path | PydanticUndefined |
| `cache_dir` | `CACHE_DIR` | Path | PydanticUndefined |
| `skip_app_name` | `SKIP_APP_NAME` | bool | False |

### Fields

| Field | Type | Default | Since |
|---|---|---|---|
| STATIC_DIR | `Path` | `PydanticUndefined` | unreleased |
| CACHE_DIR | `Path` | `PydanticUndefined` | unreleased |
| SKIP_APP_NAME | `bool` | `False` | unreleased |

<!-- === DO_NOT_EDIT: pkg-ext staticsettings_changes === -->
### Changes

| Version | Change |
|---------|--------|
| unreleased | Made public |
<!-- === OK_EDIT: pkg-ext staticsettings_changes === -->