from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdToNurbs(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., applyMatrixToResult: bool = ..., addUnderTransform: bool = ..., caching: bool = ..., constructionHistory: bool = ..., frozen: bool = ..., name: str = ..., nodeState: int = ..., object: bool = ..., outputType: int = ...) -> None: ...
