import inspect
import sys
from collections.abc import Callable
from typing import Any
from typing import NotRequired
from typing import TypedDict


def _caller() -> str:
    return sys._getframemodulename(2) or '__main__'  # type: ignore[attr-defined]  # noqa: E501


def typeddict_from_func(
        name: str,
        func: Callable[..., Any],
) -> type[dict[Any, Any]]:
    params = {}
    for param in inspect.signature(func).parameters.values():
        if param.kind not in {
                inspect.Parameter.KEYWORD_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
        }:
            raise AssertionError(
                f'param ({param}) has unsupported kind ({param.kind})',
            )
        elif param.annotation is inspect.Parameter.empty:
            raise AssertionError(f'param ({param}) is missing annotation')

        if param.default is inspect.Parameter.empty:
            params[param.name] = param.annotation
        else:
            params[param.name] = NotRequired[param.annotation]

    ret = TypedDict(name, params)  # type: ignore[misc]
    ret.__module__ = _caller()
    return ret  # type: ignore[return-value]


def typeof(name: str, o: object) -> type[Any]:
    return Any  # can't really do better?
