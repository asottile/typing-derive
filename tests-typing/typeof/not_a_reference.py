from typing_derive.impl import typeof


V = typeof('V', 1)  # type: ignore[misc]  # not a RefExpr

x = 5
A1 = typeof('A1', x)
A2 = typeof('A2', A1)  # type: ignore[misc]  # not a Var / FuncBase
