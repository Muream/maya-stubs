from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bezierAnchorState(*, even: bool = ..., smooth: bool = ...) -> int:
    """The bezierAnchorState command provides an easy interface to modify anchor states:- Smooth/Broken anchor tangents
    - Even/Uneven weighted anchor tangents
    Args:
        even (bool?): Sets selected anchors (or attached tangent handles) to even weighting when true, uneven otherwise.  
                Properties: create
        smooth (bool?): Sets selected anchors (or attached tangent handles) to smooth when true, broken otherwise.  
                Properties: create

    Returns:
        int: (number of modified anchors)

    Example:
    """

