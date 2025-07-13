from typing_derive.impl import typeddict_from_func


def f(x: int) -> int:
    return x


TD = typeddict_from_func('TD', f)

x: TD = {'x': 1}

f(**x)
