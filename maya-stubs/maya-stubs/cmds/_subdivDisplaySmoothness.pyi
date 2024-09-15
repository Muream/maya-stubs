from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdivDisplaySmoothness(*args: Any, query: bool = ..., all: bool = ..., smoothness: Queryable[int] = ...) -> Union[bool, int]:
    """Sets or querys the display smoothness of subdivision surfaces on the selection list or of all subdivision surfaces if the -all option is set.  Smoothness options are; rough, medium, or fine.  Rough is the default.subdivision, surface, display, smoothness
    Args:
        all (bool?): If set, change smoothness for all subdivision surfaces  
                Properties: create, query
        smoothness (Queryable[int]?): Smoothness - 1 rough, 2 medium, 3 fine  
                Properties: create, query

    Returns:
        bool: Command result

    Example:
    """

