from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectKeyframe(*args: str, animation: str = ..., attribute: Multiuse[str] = ..., controlPoints: bool = ..., float: Multiuse[Range[float]] = ..., hierarchy: str = ..., index: Multiuse[int] = ..., includeUpperBound: bool = ..., shape: bool = ..., selectionWindow: Tuple[float, float, float, float] = ..., time: Multiuse[NullableRange[float]] = ...) -> None: ...
