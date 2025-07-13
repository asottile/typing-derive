from typing_derive.impl import callable_from_func


def f(x: int, y: str) -> None: ...


F = callable_from_func('F', f)

x: F = f


def g(x: int, y: str) -> None: ...


y: F = g
