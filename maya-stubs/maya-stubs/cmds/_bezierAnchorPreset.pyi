from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bezierAnchorPreset(*, preset: int = ...) -> int:
    """This command provides a queryable interface for Bezier curve shapes.
    Args:
        preset (int?): Selects a preset to apply to selected Bezier anchors. Valid arguments are:  
              
                0. Bezier  
                1. Bezier Corner  
                2. Corner  
                Properties: create

    Returns:
        int: (number of modified anchors)

    Example:
    """

