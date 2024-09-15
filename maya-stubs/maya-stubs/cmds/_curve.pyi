from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def curve(*args: str, append: bool = ..., bezier: bool = ..., degree: float = ..., editPoint: Multiuse[Tuple[float, float, float]] = ..., knot: Multiuse[float] = ..., name: str = ..., objectSpace: bool = ..., periodic: bool = ..., point: Multiuse[Tuple[float, float, float]] = ..., pointWeight: Multiuse[Tuple[float, float, float, float]] = ..., replace: bool = ..., worldSpace: bool = ...) -> str:
    """The curve command creates a new curve from a list of control vertices
    (CVs).  A string is returned containing the pathname to the newly
    created curve.  You can create a curve from points either in world
    space or object (local) space, either with weights or without.
    You can replace an existing curve by using the "-r/replace"
    flag.  You can append a point to an existing curve by using the
    "-a/append" flag.To create a curve-on-surface, use the curveOnSurface command.To change the degree of a curve, use the rebuildCurve command.To change the of parameter range curve, use the rebuildCurve command.
    Args:
        append (bool?): Appends point(s) to the end of an existing curve.  
                If you use this flag, you must specify the name of the  
                curve to append to, at the end of the command.  (See examples below.)  
                Properties: create
        bezier (bool?): The created curve will be a bezier curve.  
                Properties: create
        degree (float?): The degree of the new curve.  Default is 3.  Note that you need  
                (degree+1) curve points to create a visible curve span.  eg. you  
                must place 4 points for a degree 3 curve.  
                Properties: create
        editPoint (Multiuse[Tuple[float, float, float]]?): The x, y, z position of an edit point.  "linear" means that this flag  
                can take values with units.  This flag can not be used with  
                the -point or the -pointWeight flags.  
                Properties: create, multiuse
        knot (Multiuse[float]?): A knot value in a knot vector.  One flag per knot value.  
                There must be (numberOfPoints + degree - 1) knots and the knot  
                vector must be non-decreasing.  
                Properties: create, multiuse
        name (str?): Name of the curve  
                Properties: create
        objectSpace (bool?): Points are in object, or "local" space.  This is the default.  
                You cannot specify both "-os" and "-ws" in the same command.  
                Properties: create
        periodic (bool?): If on, creates a curve that is periodic.  Default is off.  
                Properties: create
        point (Multiuse[Tuple[float, float, float]]?): The x, y, z position of a point.  "linear" means that this flag  
                can take values with units.  
                Properties: create, multiuse
        pointWeight (Multiuse[Tuple[float, float, float, float]]?): The x,y,z and w values of a point, where the w is a weight value.  
                A rational curve will be created if this flag is used.  
                "linear" means that this flag can take values with units.  
                Properties: create, multiuse
        replace (bool?): Replaces an entire existing curve.  
                If you use this flag, you must specify the name of the curve to  
                replace, at the end of the command.  (See examples below.)  
                Properties: create
        worldSpace (bool?): Points are in world space.  The default is "-os".  
                You cannot specify both "-os" and "-ws" in the same command.  
                Properties: create

    Returns:
        str: The path to the new curve or the replaced curve

    Example:
    """

