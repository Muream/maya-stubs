from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displaySmoothness(*args: str, query: bool = ..., all: bool = ..., boundary: bool = ..., defaultCreation: bool = ..., divisionsU: Queryable[int] = ..., divisionsV: Queryable[int] = ..., full: bool = ..., hull: bool = ..., pointsShaded: Queryable[int] = ..., pointsWire: Queryable[int] = ..., polygonObject: Queryable[int] = ..., renderTessellation: bool = ..., simplifyU: Queryable[int] = ..., simplifyV: Queryable[int] = ...) -> Union[bool, int]:
    """This command is responsible for setting the display smoothness
    of NURBS curves and surfaces to either predefined or custom values.
    It also sets display modes for smoothness such as hulls and the
    hull simplification factors.
    At present, this command is NOT un-doable.
    Args:
        all (bool?): Change smoothness for all curves and surfaces  
                Properties: create, query
        boundary (bool?): Display wireframe surfaces using only the boundaries of the surface  
                Not fully implemented yet  
                Properties: create, query
        defaultCreation (bool?): The default values at creation (applies only -du, -dv, -pw, -ps)  
                Properties: create, query
        divisionsU (Queryable[int]?): Number of isoparm divisions per span in the U direction.  
                The valid range of values is [0,64].  
                Properties: create, query
        divisionsV (Queryable[int]?): Number of isoparm divisions per span in the V direction.  
                The valid range of values is [0,64].  
                Properties: create, query
        full (bool?): Display surface at full resolution - the default.  
                Properties: create, query
        hull (bool?): Display surface using the hull (control points are drawn rather  
                than surface knot points). This mode is a useful display performance  
                improvement when modifying a surface since it doesn't require  
                evaluating points on the surface.  
                Properties: create, query
        pointsShaded (Queryable[int]?): Number of points per surface span in shaded mode. The  
                valid range of values is [1,64].  
                Properties: create, query
        pointsWire (Queryable[int]?): Number of points per surface isoparm span  
                or the number of points per curve span in wireframe mode.  
                The valid range of values is [1,128].  
                Note: This is the only flag that also applies to nurbs curves.  
                Properties: create, query
        polygonObject (Queryable[int]?): Display the polygon objects with the given resolution  
                Properties: create, query
        renderTessellation (bool?): Display using render tesselation parameters when in shaded mode.  
                Properties: create, query
        simplifyU (Queryable[int]?): Number of spans to skip in the U direction when in  
                hull display mode.  
                Properties: create, query
        simplifyV (Queryable[int]?): Number of spans to skip in the V direction when in  
                hull display mode.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

