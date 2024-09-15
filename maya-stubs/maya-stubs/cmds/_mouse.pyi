from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def mouse(*, enableScrollWheel: bool = ..., mouseButtonTracking: int = ..., mouseButtonTrackingStatus: bool = ..., scrollWheelStatus: bool = ...) -> int:
    """This command allows to configure mouse.
    Args:
        enableScrollWheel (bool?): Enable or disable scroll wheel support.  
                Properties: create
        mouseButtonTracking (int?): Set the number (1, 2 or 3) of mouse buttons to track.  
                Note: this is only supported on Macintosh  
                Properties: create
        mouseButtonTrackingStatus (bool?): returns the current number of mouse buttons being tracked.  
                Properties: create
        scrollWheelStatus (bool?): returns the current status of scroll wheel support.  
                Properties: create

    Returns:
        int: When -scrollWheelStatus flag is used, will return 1 if scroll wheel support enabled, otherwise 0.
            When -mouseButtonTrackingStatus flag is used, will return the number of mouse buttons being tracked.

    Example:
    """

