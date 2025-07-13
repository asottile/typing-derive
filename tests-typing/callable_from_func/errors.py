from typing_derive.impl import callable_from_func


def f(x: int) -> int:
    return x


F = callable_from_func('F', f)


def takes_func(func: F) -> int:
    return func(x=1)


def wrong_arg_type(x: str) -> int:
    return int(x)


takes_func(wrong_arg_type)  # type: ignore[arg-type]


def wrong_return_type(x: int) -> str:
    return str(x)


takes_func(wrong_return_type)  # type: ignore[arg-type]


def wrong_arg_name(x1: int) -> int:
    return x1


takes_func(wrong_arg_name)  # type: ignore[arg-type]
