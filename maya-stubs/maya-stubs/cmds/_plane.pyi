from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def plane(*, length: float = ..., name: str = ..., position: Tuple[float, float, float] = ..., rotation: Tuple[float, float, float] = ..., size: float = ..., width: float = ...) -> str:
    """The command creates a sketch plane (also known as a "construction plane")
    in space.  To create an object (such as a NURBS curve, joint chain or
    polygon) on a construction plane, you need to first make the plane live.
    See also the makeLive command.
    Args:
        length (float?): The length of plane.  
                "linear" means that this flag can handle values with units.  
                Properties: create
        name (str?): Name the resulting object.  
                Properties: create
        position (Tuple[float, float, float]?): 3D position where the centre of the plane is positioned.  
                "linear" means that this flag can handle values with units.  
                Properties: create
        rotation (Tuple[float, float, float]?): The rotation of plane.  
                "angle" means that this flag can handle values with units.  
                Properties: create
        size (float?): The combined size (size x size) of plane.  
                "linear" means that this flag can handle values with units.  
                Properties: create
        width (float?): The width of plane.  
                "linear" means that this flag can handle values with units.  
                Properties: create

    Returns:
        str: (name of the new plane)

    Example:
    """

