from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def objectCenter(arg0: str = ..., /, *, gl: bool = ..., local: bool = ..., x: bool = ..., y: bool = ..., z: bool = ...) -> Union[List[float], float]:
    """This command returns the coordinates of the center of the bounding box
    of the specified object. If one coordinate only is specified, it will
    be returned as a float. If no coordinates are specified, an array of
    floats is returned, containing x, y, and z. If you specify multiple
    coordinates, only one will be returned.
    Args:
        gl (bool?): Return positional values in global coordinates (default).  
                Properties: create
        local (bool?): Return positional values in local coordinates.  
                Properties: create
        x (bool?): Return X value only  
                Properties: create
        y (bool?): Return Y value only  
                Properties: create
        z (bool?): Return Z value only  
                Properties: create

    Returns:
        List[float]: When the asking for the center (default).
        float: When asking for one coordinate only.

    Example:
    """

