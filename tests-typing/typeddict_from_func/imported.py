from .required_args import f
from typing_derive.impl import typeddict_from_func

TD = typeddict_from_func('TD', f)

x: TD = {'x': 1, 'y': '2'}
f(**x)
