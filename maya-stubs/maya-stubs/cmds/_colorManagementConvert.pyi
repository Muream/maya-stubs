from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorManagementConvert(*, toDisplaySpace: Tuple[float, float, float] = ...) -> bool:
    """This command can be used to convert rendering (a.k.a. working) space color values to display space
    color values. This is useful if you create custom UI with colors painted to screen, where you need
    to handle color management yourself. The current view transform set in the Color Management user
    preferences will be used.color, management
    Args:
        toDisplaySpace (Tuple[float, float, float]?): Converts the given RGB value to display space.  
                Properties: create

    Returns:
        bool:

    Example:
    """

