from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyWarpImage(*args: str, bilinear: bool = ..., background: Tuple[int, int, int] = ..., fileFormat: str = ..., inputName: str = ..., inputUvSetName: str = ..., noAlpha: bool = ..., overwrite: bool = ..., outputName: str = ..., outputUvSetName: str = ..., tiled: bool = ..., xResolution: int = ..., yResolution: int = ...) -> None: ...
