<!-- === DO_NOT_EDIT: pkg-ext header === -->
# fields

<!-- === OK_EDIT: pkg-ext header === -->

<!-- === DO_NOT_EDIT: pkg-ext symbols === -->
- [`BaseModelT`](#basemodelt_def)
- [`copy_and_validate`](#copy_and_validate_def)
- [`env_var_name`](#env_var_name_def)
- [`env_var_names`](#env_var_names_def)
- [`field_names`](#field_names_def)
<!-- === OK_EDIT: pkg-ext symbols === -->

<!-- === DO_NOT_EDIT: pkg-ext symbol_details_header === -->
## Symbol Details
<!-- === OK_EDIT: pkg-ext symbol_details_header === -->

<!-- === DO_NOT_EDIT: pkg-ext basemodelt_def === -->
### type_alias: `BaseModelT`
- [source](../../model_lib/pydantic_utils.py)
> **Since:** 0.100.0

```python
BaseModelT = ~BaseModelT
```

Type variable.

The preferred way to construct a type variable is via the dedicated
syntax for generic functions, classes, and type aliases::

    class Sequence[T]:  # T is a TypeVar
        ...

This syntax can also be used to create bound and constrained type
variables::

    # S is a TypeVar bound to str
    class StrSequence[S: str]:
        ...

    # A is a TypeVar constrained to str or bytes
    class StrOrBytesSequence[A: (str, bytes)]:
        ...

Type variables can also have defaults:

    class IntDefault[T = int]:
        ...

However, if desired, reusable type variables can also be constructed
manually, like so::

   T = TypeVar('T')  # Can be anything
   S = TypeVar('S', bound=str)  # Can be any subtype of str
   A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
   D = TypeVar('D', default=int)  # Defaults to int

Type variables exist primarily for the benefit of static type
checkers.  They serve as the parameters for generic types as well
as for generic function and type alias definitions.

The variance of type variables is inferred by type checkers when they
are created through the type parameter syntax and when
``infer_variance=True`` is passed. Manually created type variables may
be explicitly marked covariant or contravariant by passing
``covariant=True`` or ``contravariant=True``. By default, manually
created type variables are invariant. See PEP 484 and PEP 695 for more
details.
<!-- === OK_EDIT: pkg-ext basemodelt_def === -->
<!-- === DO_NOT_EDIT: pkg-ext copy_and_validate_def === -->
### function: `copy_and_validate`
- [source](../../model_lib/pydantic_utils.py#L103)
> **Since:** 0.100.0

```python
def copy_and_validate(model: ~BaseModelT, **updates) -> ~BaseModelT:
    ...
```
<!-- === OK_EDIT: pkg-ext copy_and_validate_def === -->
<!-- === DO_NOT_EDIT: pkg-ext env_var_name_def === -->
### function: `env_var_name`
- [source](../../model_lib/pydantic_utils.py#L13)
> **Since:** 0.100.0

```python
def env_var_name(settings: BaseSettings | type[BaseSettings], field_name: str) -> str:
    ...
```
<!-- === OK_EDIT: pkg-ext env_var_name_def === -->
<!-- === DO_NOT_EDIT: pkg-ext env_var_names_def === -->
### function: `env_var_names`
- [source](../../model_lib/pydantic_utils.py#L31)
> **Since:** 0.100.0

```python
def env_var_names(settings: BaseSettings | type[BaseSettings]) -> list[str]:
    ...
```
<!-- === OK_EDIT: pkg-ext env_var_names_def === -->
<!-- === DO_NOT_EDIT: pkg-ext field_names_def === -->
### function: `field_names`
- [source](../../model_lib/pydantic_utils.py#L128)
> **Since:** 0.100.0

```python
def field_names(model_type: type[BaseModel] | BaseModel) -> list[str]:
    ...
```
<!-- === OK_EDIT: pkg-ext field_names_def === -->