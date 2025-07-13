from typing_derive.impl import typeof


def f(x: 'R') -> None: ...


F = typeof('F', f)

x: F = f


class R:
    ...
