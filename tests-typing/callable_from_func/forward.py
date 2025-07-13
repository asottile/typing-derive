from typing_derive.impl import callable_from_func


def f(x: 'R') -> None: ...


F = callable_from_func('F', f)

x: F = f


class R:
    ...
