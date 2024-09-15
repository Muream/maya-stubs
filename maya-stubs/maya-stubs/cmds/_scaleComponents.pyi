from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scaleComponents(arg0: float = ..., arg1: float = ..., arg2: float = ..., /, *args: str, pivot: Tuple[float, float, float] = ..., rotation: Tuple[float, float, float] = ...) -> bool:
    """This is a limited version of the scale command.  First, it
    only works on selected components. You provide a pivot in
    world space, and you can provide a rotation.  This rotation
    affects the scaling, so that rather than scaling in X, Y, Z,
    this is scaling in X, Y, and Z after they have been rotated
    by the given rotation.This allows selected components to be scaled in any arbitrary
    space, not just object or world space as the regular scale
    allows.Scale values are always relative, not absolute.
    Args:
        pivot (Tuple[float, float, float]?): The pivot position in world space (default is origin)  
                Properties: create
        rotation (Tuple[float, float, float]?): The rotational offset for the scaling (default is none)  
                Properties: create

    Returns:
        bool:

    Example:
    """

