from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def extendFluid(*args: str, edit: bool = ..., query: bool = ..., endD: int = ..., endH: int = ..., endW: int = ..., startD: int = ..., startH: int = ..., startW: int = ...) -> None: ...
