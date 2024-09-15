from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySpinEdge(*args: str, edit: bool = ..., query: bool = ..., caching: bool = ..., constructionHistory: bool = ..., frozen: bool = ..., name: str = ..., nodeState: int = ..., offset: int = ..., reverse: bool = ...) -> None: ...
