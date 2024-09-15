from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def align(*args: str, alignToLead: bool = ..., coordinateSystem: str = ..., xAxis: str = ..., yAxis: str = ..., zAxis: str = ...) -> bool:
    """Align or spread objects along X Y and Z axis.objects, move, align
    Args:
        alignToLead (bool?): When set, the min, center or max values are computed from the  
                lead object. Otherwise, the values are averaged for all objects.  
                Default is false  
                Properties: create
        coordinateSystem (str?): Defines the X, Y, and Z coordinates. Default is the world coordinates  
                Properties: create
        xAxis (str?): Any of none, min, mid, max, dist, stack.  
                This defines the kind of alignment to perfom, default is none.  
                Properties: create
        yAxis (str?): Any of none, min, mid, max, dist, stack.  
                This defines the kind of alignment to perfom, default is none.  
                Properties: create
        zAxis (str?): Any of none, min, mid, max, dist, stack.  
                This defines the kind of alignment to perfom, default is none.  
                Properties: create

    Returns:
        bool: true/false

    Example:
    """

