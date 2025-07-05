from typing_derive.impl import typeddict_from_func


def f(x: 'R') -> None:
    """forward ref triggers a deferral"""


TD = typeddict_from_func('TD', f)


class R:
    ...
