from typing_derive.impl import typeof

x = 5

X = typeof('X', x)

y: X = 5

z: X = 'no'  # type: ignore[assignment]
