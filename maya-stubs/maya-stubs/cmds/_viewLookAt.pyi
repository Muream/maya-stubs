from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewLookAt(arg0: str = ..., /, *, position: Tuple[float, float, float] = ...) -> bool:
    """The viewLookAt command positions the specified camera so it is
    looking at the centroid of all selected objects. If no objects are
    specified the camera will look at the ground plane.
    Args:
        position (Tuple[float, float, float]?): Position in world space to make the camera look at.  
                Properties: create

    Returns:
        bool:

    Example:
    """

