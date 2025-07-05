from typing_derive.impl import typeddict_from_func


def f(x: int, y: int = 5) -> None: ...


TD = typeddict_from_func('TD', f)

x: TD = {'x': 1}

f(**x)
