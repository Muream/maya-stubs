from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikSystemInfo(arg0: bool = ..., /, *, query: bool = ..., globalSnapHandle: bool = ...) -> bool:
    """This action modifies and queries the current ikSystem controls.
    Args:
        globalSnapHandle (bool?): If this flag is off, all ikHandles will not be snapped.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

