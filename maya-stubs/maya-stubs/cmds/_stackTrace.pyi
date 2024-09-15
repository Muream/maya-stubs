from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def stackTrace(*, query: bool = ..., dump: bool = ..., parameterCount: int = ..., parameterType: Tuple[int, int] = ..., parameterValue: Tuple[int, int] = ..., state: bool = ...) -> None: ...
