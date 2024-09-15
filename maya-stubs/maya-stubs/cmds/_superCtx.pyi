from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def superCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., attach: Multiuse[str] = ..., exists: bool = ..., image1: str = ..., image2: str = ..., image3: str = ...) -> None: ...
