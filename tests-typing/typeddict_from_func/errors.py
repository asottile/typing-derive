from typing_derive.impl import typeddict_from_func

x = 'hi'

TD = typeddict_from_func()  # type: ignore[call-arg,misc]
TD = typeddict_from_func('TD')  # type: ignore[call-arg,misc]
TD = typeddict_from_func('TD', 'wat')  # type: ignore[arg-type,misc]
TD = typeddict_from_func('TD', lambda: None)  # type: ignore[misc]
TD = typeddict_from_func('TD', x)  # type: ignore[arg-type,misc]


def f(*a: object) -> None: ...
def g(**k: object) -> None: ...
def h(x: object, /) -> None: ...


TD = typeddict_from_func('TD', f)  # type: ignore[misc]
TD = typeddict_from_func('TD', g)  # type: ignore[misc]
TD = typeddict_from_func('TD', h)  # type: ignore[misc]
