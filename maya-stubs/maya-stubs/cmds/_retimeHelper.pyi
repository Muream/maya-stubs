from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def retimeHelper(*, edit: bool = ..., query: bool = ..., deleteFrame: int = ..., frame: float = ..., lockBar: Tuple[int, int] = ..., locks: int = ..., moveFrame: Tuple[int, float] = ..., mouseOver: bool = ...) -> None: ...
