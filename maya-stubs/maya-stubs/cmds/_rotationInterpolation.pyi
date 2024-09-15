from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rotationInterpolation(*args: str, query: bool = ..., convert: Queryable[str] = ...) -> Union[bool, str]:
    """The rotationInterpolation command converts the rotation curves to the
            desired rotation interpolation representation. For example, an
            Euler-angled representation can be converted to Quaternion.curve, rotation, interpolation, quaternion, euler
    Args:
        convert (Queryable[str]?): Specifies the rotation interpolation mode for the curves after converting.  
                Possible choices are "none" (unsynchronized Euler-angled curves which are  
                compatible with pre-4.0 Maya curves), "euler" (Euler-angled curves with  
                keyframes kept synchronized), "quaternion" (quaternion curves with  
                keyframes kept synchronized, but the exact interpolation depends on  
                individual tangents),  "quaternionSlerp" (applies quaternion slerp interpolation  
                to the curve, ignoring tangent settings), "quaternionSquad" (applied cubic interpolation  
                to the curve in quaternion space, ignoring tangent settings)  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

