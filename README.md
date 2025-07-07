[![build status](https://github.com/asottile/typing-derive/actions/workflows/main.yml/badge.svg)](https://github.com/asottile/typing-derive/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/asottile/typing-derive/main.svg)](https://results.pre-commit.ci/latest/github/asottile/typing-derive/main)

typing-derive
=============

derive types from other types to make it easier to type code!

## Installation

```bash
pip install typing-derive
```

## usage

add as a mypy plugin

```ini
[mypy]
plugins = typing_derive.plugin
```

### `typing_derive.impl.typeddict_from_func`

create a usable `TypedDict` from some callable.  useful if you need to
dynamically build up `**kwargs` to call a function

```python
from typing_derive.impl import typeddict_from_func

def f(x: int, y: str) -> None: ...

TD = typeddict_from_func('TD', f)

x: TD = {
    'x': 1,
    'y': 'hello hello',
}

f(**x)
```
