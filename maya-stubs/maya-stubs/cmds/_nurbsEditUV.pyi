from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsEditUV(*args: str, query: bool = ..., angle: Queryable[float] = ..., pivotU: Queryable[float] = ..., pivotV: Queryable[float] = ..., relative: bool = ..., rotateRatio: Queryable[float] = ..., rotation: bool = ..., scale: bool = ..., scaleU: Queryable[float] = ..., scaleV: Queryable[float] = ..., uValue: Queryable[float] = ..., vValue: Queryable[float] = ...) -> Union[bool, float]:
    """Command Edits UVs on NURBS objects. When used with the query flag, it
    returns the UV values associated with the specified components.nurbs, editUV, tweakUV, uvEditing
    Args:
        angle (Queryable[float]?): Specifies the angle value (in degrees) by which the UV values are to be rotated.  
                Properties: create, query
        pivotU (Queryable[float]?): Specifies the pivot value, in the u direction, about which the scale or  
                rotate is to be performed.  
                Properties: create, query
        pivotV (Queryable[float]?): Specifies the pivot value, in the v direction, about which the scale or  
                rotate is to be performed.  
                Properties: create, query
        relative (bool?): Specifies whether this command is editing the values relative to the currently  
                existing values. Default is true;  
                Properties: create, query
        rotateRatio (Queryable[float]?): Specifies the ratio value by which the UV values are to be rotated.  
                Default is 1.0  
                Properties: create, query
        rotation (bool?): Specifies whether this command is editing the values with rotation values  
                Properties: create, query
        scale (bool?): Specifies whether this command is editing the values with scale values  
                Properties: create, query
        scaleU (Queryable[float]?): Specifies the scale value in the u direction.  
                Properties: create, query
        scaleV (Queryable[float]?): Specifies the scale value in the v direction.  
                Properties: create, query
        uValue (Queryable[float]?): Specifies the value, in the u direction - absolute if relative flag is false..  
                Properties: create, query
        vValue (Queryable[float]?): Specifies the value, in the v direction - absolute if relative flag is false..  
                Properties: create, query

    Returns:
        bool: Success or Failure.

    Example:
    """

