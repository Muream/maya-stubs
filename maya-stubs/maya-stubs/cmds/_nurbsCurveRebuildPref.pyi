from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsCurveRebuildPref(*, query: bool = ..., degree: int = ..., endKnots: int = ..., fitRebuild: int = ..., keepControlPoints: bool = ..., keepEndPoints: bool = ..., keepRange: int = ..., keepTangents: bool = ..., rebuildType: int = ..., spans: int = ..., smartSurfaceCurve: bool = ..., tolerance: float = ...) -> None: ...
