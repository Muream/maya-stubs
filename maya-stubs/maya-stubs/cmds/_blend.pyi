from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def blend(*args: str, edit: bool = ..., query: bool = ..., autoDirection: bool = ..., caching: bool = ..., crvsInFirstRail: int = ..., constructionHistory: bool = ..., flipLeft: bool = ..., flipRight: bool = ..., frozen: bool = ..., leftParameter: float = ..., multipleKnots: bool = ..., name: str = ..., nodeState: int = ..., object: bool = ..., polygon: int = ..., positionTolerance: float = ..., rightParameter: float = ..., tangentTolerance: float = ...) -> None: ...
