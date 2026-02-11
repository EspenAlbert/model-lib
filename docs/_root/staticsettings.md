# StaticSettings

<!-- === DO_NOT_EDIT: pkg-ext staticsettings_def === -->
## class: StaticSettings
- [source](../../model_lib/static_settings.py#L11)
> **Since:** 0.100.0

```python
class StaticSettings(BaseSettings):
    STATIC_DIR: Path | None = None
    CACHE_DIR: Path | None = None
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
| 0.102.1 | field 'STATIC_DIR' default added: None |
| 0.102.1 | field 'CACHE_DIR' default added: None |
| 0.102.1 | added base class 'BaseSettings' |
| 0.102.0 | field 'STATIC_DIR' default removed (was: PydanticUndefined) |
| 0.102.0 | field 'STATIC_DIR' type: Path -> Path | None |
| 0.102.0 | field 'CACHE_DIR' default removed (was: PydanticUndefined) |
| 0.102.0 | field 'CACHE_DIR' type: Path -> Path | None |
| 0.100.0 | Made public |
<!-- === OK_EDIT: pkg-ext staticsettings_changes === -->