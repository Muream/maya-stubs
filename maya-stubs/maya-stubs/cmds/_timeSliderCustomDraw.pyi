from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeSliderCustomDraw(arg0: int = ..., /, *, edit: bool = ..., query: bool = ..., color: Tuple[float, float, float, float] = ..., clearPrimitives: bool = ..., deregister: int = ..., height: int = ..., layer: int = ..., location: int = ..., priority: int = ..., registerAbove: str = ..., registerBelow: str = ..., registerOn: Tuple[str, int] = ..., setPrimitives: Tuple[str, float, float] = ..., visible: bool = ...) -> None: ...
