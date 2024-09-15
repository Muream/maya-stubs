from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def upAxis(*args: str, query: bool = ..., axis: Queryable[str] = ..., rotateView: bool = ...) -> Union[bool, str]:
    """The upAxis command changes the world up direction.
    Current implementation provides only two choices of axis (the Y-axis
    or the Z-axis) as the world up direction.By default, the ground plane in Maya is on the XY plane.
    Hence, the default up-direction is the direction of the positive Z-axis.The -ax flag is mandatory. In conjunction with the -ax flag,
    when the -rv flag is specified, the camera of currently active view is
    revolved about the X-axis such that the position of the groundplane in
    the view will remain the same as before the the up direction is changed.The screen update is applied to all cameras of all views.
    Args:
        axis (Queryable[str]?): This flag specifies the axis as the world up direction.  
                The valid axis are either "y" or "z".  
                When queried, it returns a string.  
                Properties: query
        rotateView (bool?): This flag specifies to rotate the view as well.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

