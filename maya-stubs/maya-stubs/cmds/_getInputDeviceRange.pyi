from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getInputDeviceRange(*args: Any, maxValue: bool = ..., minValue: bool = ...) -> List[float]:
    """This command lists the minimum and maximum values the device
    axis can return.  This value is the raw device values before
    any mapping is applied.  If you don't specify an axis the
    values for all axes of the device are returned.
    Args:
        maxValue (bool?): list only the maximum value of the axis  
                Properties: create
        minValue (bool?): list only the minimum value of the axis  
                Properties: create

    Returns:
        List[float]: Command result

    Example:
    """

