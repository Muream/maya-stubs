from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def changeSubdivComponentDisplayLevel(*args: Any, query: bool = ..., level: Queryable[int] = ..., relative: bool = ...) -> Union[int, bool]:
    """Explicitly forces the subdivision surface to display components at a
    particular level of refinement.subdivision, surface, display, level, fine, coarse, level
    Args:
        level (Queryable[int]?): Specifies the display level of components.  
                Properties: create, query
        relative (bool?): If set, level refers to the relative display level  
                Properties: create, query

    Returns:
        int: Command result

    Example:
    """

