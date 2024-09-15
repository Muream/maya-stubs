from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyToCurve(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addUnderTransform: bool = ..., caching: bool = ..., constructionHistory: bool = ..., degree: int = ..., displaySmoothMesh: int = ..., form: int = ..., frozen: bool = ..., name: str = ..., nodeState: int = ..., object: bool = ..., conformToSmoothMeshPreview: bool = ...) -> None: ...
