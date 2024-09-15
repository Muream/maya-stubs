from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def currentTime(arg0: int = ..., /, *, edit: bool = ..., query: bool = ..., update: bool = ...) -> int:
    """When given a time argument (with or without the -edit flag) this
    command sets the current global time.  The model updates and
    displays at the new time, unless "-update off" is present on the
    command line.
    Args:
        update (bool?): change the current time, but do not update the world.  
                Default value is true.  
                Properties: create

    Returns:
        int: Command result

    Example:
    """

