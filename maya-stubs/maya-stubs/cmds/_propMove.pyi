from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def propMove(arg0: float = ..., arg1: float = ..., arg2: float = ..., /, *args: str, percent: Multiuse[float] = ..., percentX: Multiuse[float] = ..., percentY: Multiuse[float] = ..., percentZ: Multiuse[float] = ..., pivot: Tuple[float, float, float] = ..., rotate: Tuple[float, float, float] = ..., scale: Tuple[float, float, float] = ..., translate: Tuple[float, float, float] = ..., worldSpace: bool = ...) -> bool:
    """Performs a proportional translate, scale or rotate operation on any
    number of objects. The percentages to rotate, scale or translate by
    can be specified using either the -p flags or -px, -py, -pz
    flags. Each selected object must have a corresponding -p or -px, -py,
    -pz flag. The rotate, scale or translate performed is relative.
    Args:
        percent (Multiuse[float]?): The percentage effect that the specified x,y,z has on an object.  
                This flag must be specified once for each object, ie. if there  
                are 4 objects specified, there must be 4 "-p" flags, (otherwise  
                a percentage of 1.0 will be used).  This flag generally has a  
                range between 0.0 and 1.0, but can be any float value.  
                Properties: create, multiuse
        percentX (Multiuse[float]?): The percentage effect that the specified x has on an object.  
                This flag is specified one per object.  
                The value ranges between 0.0 and 1.0, but can be any float value.  
                If the -p flag has been specified, this flag usage is invalid.  
                Properties: create, multiuse
        percentY (Multiuse[float]?): The percentage effect that the specified y has on an object.  
                This flag is specified one per object.  
                The value ranges between 0.0 and 1.0, but can be any float value.  
                If the -p flag has been specified, this flag usage is invalid.  
                Properties: create, multiuse
        percentZ (Multiuse[float]?): The percentage effect that the specified z has on an object.  
                This flag is specified one per object.  
                The value ranges between 0.0 and 1.0, but can be any float value.  
                If the -p flag has been specified, this flag usage is invalid.  
                Properties: create, multiuse
        pivot (Tuple[float, float, float]?): Specify the pivot about which a rotation or scale will occur.  
                The change in pivot lasts only as long as the current 'propMove' command, and so  
                must be used in conjunction with one of the above move flags for any effect to be  
                noticeable.  
                Properties: create
        rotate (Tuple[float, float, float]?): Proportionally rotate each object by the given angles. The rotation values  
                are scaled by the percentage specified by that object's  
                corresponding "-percent" flag.  
                All angles are in degrees.  
                The rotation is about the pivot specified by the "-pivot" flag, or (0, 0, 0)  
                if the "-pivot" flag is not present.  
                Properties: create
        scale (Tuple[float, float, float]?): Proportionally scale each object by the given amounts. The scale values  
                are scaled by the percentage specified by that object's  
                corresponding "-percent" flag.  
                The position and size of each object is measured relative to the pivot  
                specified by the "-pivot" flag, and defaults to each object's individual pivot.  
                In the case of control vertices, or some other object component, the  
                default is the parent object's pivot.  
                Properties: create
        translate (Tuple[float, float, float]?): Proportionally translate each object by the given amounts. The translation  
                values are scaled by the percentage specified by that object's  
                corresponding "-percent" flag.  
                The "-pivot" flag has no effect on translation.  
                Properties: create
        worldSpace (bool?): Use worldspace for the calculations.  
                Properties: create

    Returns:
        bool:

    Example:
    """

