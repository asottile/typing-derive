from collections.abc import Callable

from mypy.nodes import ArgKind
from mypy.nodes import FuncDef
from mypy.nodes import GDEF
from mypy.nodes import PlaceholderNode
from mypy.nodes import RefExpr
from mypy.nodes import SymbolTableNode
from mypy.nodes import TypeAlias
from mypy.plugin import DynamicClassDefContext
from mypy.plugin import Plugin
from mypy.types import CallableType
from mypy.types import TypedDictType


def _defer(ctx: DynamicClassDefContext) -> None:
    if not ctx.api.final_iteration:  # pragma: no branch
        # XXX: hack for python/mypy#17402
        ph = PlaceholderNode(
            ctx.api.qualified_name(ctx.name),
            ctx.call,
            ctx.call.line,
            becomes_typeinfo=True,
        )
        ctx.api.add_symbol_table_node(ctx.name, SymbolTableNode(GDEF, ph))
        ctx.api.defer()


def _get_arg1_func(ctx: DynamicClassDefContext) -> CallableType | None:
    if len(ctx.call.args) != 2:
        return ctx.api.fail('expected 2 args', ctx.call)

    _, func_arg = ctx.call.args
    if not isinstance(func_arg, RefExpr):
        return ctx.api.fail('expected arg 1 to be func', ctx.call)

    if func_arg.node is None:
        return _defer(ctx)  # type: ignore[func-returns-value] # python/mypy#19433  # noqa: E501

    if (
        not isinstance(func_arg.node, FuncDef) or
        not isinstance(func_arg.node.type, CallableType)
    ):
        return ctx.api.fail('expected arg 1 to be func', ctx.call)

    analyzed = ctx.api.anal_type(func_arg.node.type)
    if analyzed is None:
        return _defer(ctx)  # type: ignore[func-returns-value] # python/mypy#19433  # noqa: E501

    assert isinstance(analyzed, CallableType), analyzed
    return analyzed


def _typeddict_from_func(ctx: DynamicClassDefContext) -> None:
    func_tp = _get_arg1_func(ctx)
    if func_tp is None:
        return None

    items = {}
    required_keys = set()

    c = func_tp
    for kind, name, tp in zip(c.arg_kinds, c.arg_names, c.arg_types):
        if name is None:
            return ctx.api.fail('func has pos-only argument', ctx.call)
        elif kind is ArgKind.ARG_STAR or kind is ArgKind.ARG_STAR2:
            return ctx.api.fail('func has star argument', ctx.call)

        if kind is not ArgKind.ARG_OPT and kind is not ArgKind.ARG_NAMED_OPT:
            required_keys.add(name)

        items[name] = tp

    fallback = ctx.api.named_type('typing._TypedDict')
    td = TypedDictType(items, required_keys, set(), fallback)
    info = ctx.api.basic_new_typeinfo(ctx.name, fallback, ctx.call.line)
    info.update_typeddict_type(td)

    st = SymbolTableNode(GDEF, info, plugin_generated=True)
    ctx.api.add_symbol_table_node(ctx.name, st)


def _callable_from_func(ctx: DynamicClassDefContext) -> None:
    func_tp = _get_arg1_func(ctx)
    if func_tp is None:
        return None

    alias = TypeAlias(
        func_tp,
        ctx.name,
        line=ctx.call.line,
        column=ctx.call.column,
    )
    st = SymbolTableNode(GDEF, alias, plugin_generated=True)
    ctx.api.add_symbol_table_node(ctx.name, st)


class _Plugin(Plugin):
    def get_dynamic_class_hook(
        self, fullname: str,
    ) -> Callable[[DynamicClassDefContext], None] | None:
        if fullname == 'typing_derive.impl.typeddict_from_func':
            return _typeddict_from_func
        elif fullname == 'typing_derive.impl.callable_from_func':
            return _callable_from_func
        else:
            return None


def plugin(version: str) -> type[Plugin]:
    return _Plugin
