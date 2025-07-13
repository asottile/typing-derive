from typing_derive.impl import typeof


def f(): pass  # type: ignore[no-untyped-def]


F = typeof('F', f)  # type: ignore[misc]
