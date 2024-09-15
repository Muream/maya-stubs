from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def exactWorldBoundingBox(*args: str, calculateExactly: bool = ..., ignoreInvisible: bool = ...) -> List[float]:
    """This command figures out an exact-fit bounding box for the
    specified objects (or selected objects if none are specified)
    This bounding box is always in world space.
    Args:
        calculateExactly (bool?): Should the bounding box calculation be exact?  
                Properties: create
        ignoreInvisible (bool?): Should the bounding box calculation include or exclude  
                invisible objects?  
                Properties: create

    Returns:
        List[float]: xmin, ymin, zmin, xmax, ymax, zmax.

    Example:
    """

