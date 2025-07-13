from typing import NotRequired

from typing_derive.impl import callable_from_func
from typing_derive.impl import typeddict_from_func


def test_creates_runtime_typeddict():
    def f(x: int, y: str) -> None: ...

    td = typeddict_from_func('td', f)
    assert td.__annotations__ == {'x': int, 'y': str}


def test_creates_runtimed_typeddict_optional_params():
    def f(x: int, y: int | None = None) -> None: ...

    td = typeddict_from_func('td', f)
    assert td.__annotations__ == {'x': int, 'y': NotRequired[int | None]}


def test_callable_from_func():
    def f() -> None: ...

    c = callable_from_func('c', f)
    # unclear what this should actually do!
    assert c
