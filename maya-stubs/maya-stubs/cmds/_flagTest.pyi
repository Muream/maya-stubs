from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def flagTest(arg0: str = ..., arg1: float = ..., arg2: int = ..., arg3: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., floatRange: Multiuse[Range[float]] = ..., int64: int = ..., indexRange: Multiuse[int] = ..., multiUse: Multiuse[Tuple[float, int, str]] = ..., noReport: bool = ..., optionalQueryArgsFlag: Tuple[float, int, str] = ..., pythonOptionalQueryArgsFlag: Tuple[float, int, str] = ..., pythonQueryArgsFlag: Tuple[float, int, str] = ..., queryArgsFlag: Tuple[float, int, str] = ..., simpleFlag: bool = ..., stringArrayFlag: List[str] = ..., stringFlag: str = ..., tripleFloat: Tuple[float, float, float] = ..., timeRange: Multiuse[NullableRange[float]] = ...) -> None: ...
