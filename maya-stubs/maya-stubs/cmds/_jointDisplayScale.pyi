from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def jointDisplayScale(arg0: float = ..., /, *, edit: bool = ..., query: bool = ..., absolute: bool = ..., ikfk: Queryable[float] = ...) -> Union[float, bool]:
    """This action modifies and queries the current display size of
    skeleton joints. The joint display size is controlled by a
    scale factor; a scale factor of 1 sets the display size to its
    default, which is 1 in diameter.
    With the plain format, the float argument is the factor with
    respect to the default size. When -a/absolute is used, the
    float argument refers to the diameter of the joint
    display size.
    Args:
        absolute (bool?): Interpret the float argument as the display size as  
                opposed to the scale factor.  
                Properties: create, query, edit
        ikfk (Queryable[float]?): Set the display size of ik/fk skeleton joints.  
                Properties: create, query, edit

    Returns:
        float: Returns current display size of skeleton joints.

    Example:
    """

