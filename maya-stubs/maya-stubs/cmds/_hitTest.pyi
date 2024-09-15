from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hitTest(arg0: str = ..., arg1: int = ..., arg2: int = ..., /) -> List[str]:
    """Thecommand hit-tests a point in the named control and returns
    a list of items underneath the point. The point is specified in pixels with
    the origin (0,0) at the top-left corner. This position is compatible
    with the coordinates provided by a drop-callback. The types of items
    that may be returned depends upon the specific control; not all
    controls currently support hit-testing.hit, hittest, drag-and-drop
    Returns:
        List[str]: items underneath the hit-point

    Example:
    """

