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

### `typing_derive.impl.typeof`

create a type alias for the type of a function / variable.

one use might be to pass functions of matching signatures as objects

```python
def f(x: int, y: str) -> None: ...

F = typeof('F', f)

def g(func: F) -> None:
    func(x=1, y='two')

def h(x: int, y: str) -> None: ...
def j(x: str, y: str) -> None: ...
def k(x1: int, y: str) -> None: ...

g(f)  # ok
g(h)  # ok
g(j)  # error: `x` is `str` not `int`
g(k)  # error: `x1` mismatches `x`
```

it also just works on normal variables too -- though I haven't come up with a
use for this yet

```python
x = 5

X = typeof('X', x)  # effectively `type X = int`

y: X = 6  # ok
z: X = 'no'  # not ok!
```
