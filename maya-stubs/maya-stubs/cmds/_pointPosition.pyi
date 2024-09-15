from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pointPosition(arg0: str = ..., /, *, local: bool = ..., world: bool = ...) -> List[float]:
    """This command returns the world or local space position for any type of
    point object. Valid selection items are:
    - curve and surface CVs
    - poly vertices
    - lattice points
    - particles
    - curve and surface edit points
    - curve and surface parameter points
    - poly uvs
    - rotate/scale/joint pivots
    - selection handles
    - locators, param locators and arc length locatorsIt works on the selected object or you can specify the object in
    the command. By default, if no flag is specified then the world
    position is returned.
    Args:
        local (bool?): Return the point in local space coordinates.  
                Properties: create
        world (bool?): Return the point in world space coordinates.  
                Properties: create

    Returns:
        List[float]: Command result

    Example:
    """

