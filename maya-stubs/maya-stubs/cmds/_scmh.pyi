from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scmh(arg0: float = ..., arg1: float = ..., arg2: float = ..., arg3: float = ..., arg4: float = ..., arg5: float = ..., /, *args: str, absolute: bool = ..., ignore: Multiuse[int] = ..., quiet: bool = ..., relative: bool = ...) -> bool:
    """Set the current manipulator handle value(s).  In UI units (where
    applicable), though the syntax is set to handle the unit type
    of the current manipulator handle (if available).
    Args:
        absolute (bool?): The values are absolute  
                Properties: create
        ignore (Multiuse[int]?): This is a multiuse flag which specifies that the index-th (1. based)  
                entry is to be ignored  
                Properties: create, multiuse
        quiet (bool?): This flag suppresses all error messages  
                Properties: create
        relative (bool?): The values are relative  
                Properties: create

    Returns:
        bool:

    Example:
    """

