from typing_derive.impl import typeof


def f(x: int, y: str) -> None: ...


F = typeof('F', f)

x: F = f


def g(x: int, y: str) -> None: ...


y: F = g
