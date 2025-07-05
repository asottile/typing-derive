from __future__ import annotations

from typing import assert_type

from typing_derive.impl import typeddict_from_func


def f(x: int, y: str) -> None: ...


TD = typeddict_from_func('TD', f)

x: TD = {
    'x': 1,
    'y': 'bar',
}

assert_type(x['x'], int)
assert_type(x['y'], str)

f(**x)
