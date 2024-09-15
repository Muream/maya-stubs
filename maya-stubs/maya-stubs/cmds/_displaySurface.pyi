from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displaySurface(*args: str, query: bool = ..., flipNormals: bool = ..., twoSidedLighting: bool = ..., xRay: bool = ...) -> bool:
    """This command toggles display options on the specified or active
    surfaces. Typically this command applies to NURBS or poly mesh
    surfaces and ignores other type of objects.
    Args:
        flipNormals (bool?): flip normal direction on the surface  
                Properties: query
        twoSidedLighting (bool?): toggle if the surface should be considered  
                two-sided.  If it's single-sided, drawing and rendering  
                may use single sided lighting and back face cull  
                to improve performance.  
                Properties: query
        xRay (bool?): toggle X ray mode (make surface transparent)  
                Properties: query

    Returns:
        bool: when in the query mode.

    Example:
    """

