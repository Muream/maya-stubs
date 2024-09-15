from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def projectionManip(*, query: bool = ..., fitBBox: bool = ..., projType: int = ..., switchType: bool = ...) -> bool:
    """Various commands to set the manipulator to interesting positions.
    Args:
        fitBBox (bool?): Fit the projection manipulator size and position to the shading  
                group bounding box. The orientation is not modified.  
                Properties: create
        projType (int?): Set the projection type to the given value. Projection type values are:  
              
                 1 = planar.  
                 2 = spherical.  
                 3 = cylindrical.  
                 4 = ball.  
                 5 = cubic.  
                 6 = triplanar.  
                 7 = concentric.  
                 8 = camera.  
                Properties: create
        switchType (bool?): Loop over the allowed types. If the hardware shading is on, it loops  
                over the hardware shadeable types (planar, cylindrical, spherical),  
                otherwise, it loops over all the types.  
                If there is no given value, it loops over the different projection  
                types.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

