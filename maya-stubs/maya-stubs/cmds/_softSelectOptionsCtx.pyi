from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def softSelectOptionsCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., buttonDown: bool = ..., buttonUp: bool = ..., colorCurve: str = ..., condition: bool = ..., enableFalseColor: int = ..., enabled: bool = ..., exists: bool = ..., falloffCurve: str = ..., falloffMode: int = ..., image1: str = ..., image2: str = ..., image3: str = ..., size: float = ..., uvSize: float = ...) -> None: ...
