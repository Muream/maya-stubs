from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def curveOnSurface(*args: str, append: bool = ..., degree: float = ..., knot: Multiuse[float] = ..., name: str = ..., periodic: bool = ..., positionUV: Multiuse[Tuple[float, float]] = ..., replace: bool = ...) -> str:
    """The curve command creates a new curve from a list of control vertices
    (CVs).  A string is returned containing the pathname to the newly
    created curve.  You can create a curve from points either in world
    space or object (local) space, either with weights or without.
    You can replace an existing curve by using the "-r/replace"
    flag.  You can append a point to an existing curve by using the
    "-a/append" flag.To create a curve-on-surface, use the curveOnSurface command.To change the degree of a curve, use the rebuildCurve command.To change the of parameter range curve, use the rebuildCurve command.The curve-on-surface command creates a new curve-on-surface from a
    list of control vertices (CVs).  A string is returned containing
    the pathname to the newly created curve-on-surface.
    You can replace an existing curve by using the "-r/replace"
    flag. You can append points to an existing curve-on-surface by
    using the "-a/append" flag.
    See also the curve command, which describes how to query curve
    attributes.
    Args:
        append (bool?): Appends point(s) to the end of an existing curve.  
                If you use this flag, you must specify the name of the  
                curve to append to, at the end of the command.  (See examples below.)  
                Properties: create
        degree (float?): The degree of the new curve.  Default is 3.  Note that you need  
                (degree+1) curve points to create a visible curve span.  eg. you  
                must place 4 points for a degree 3 curve.  
                Properties: create
        knot (Multiuse[float]?): A knot value in a knot vector.  One flag per knot value.  
                There must be (numberOfPoints + degree - 1) knots and the knot  
                vector must be non-decreasing.  
                Properties: create, multiuse
        name (str?): Name of the curve  
                Properties: create
        periodic (bool?): If on, creates a curve that is periodic.  Default is off.  
                Properties: create
        positionUV (Multiuse[Tuple[float, float]]?): The uv position of a point.  
                Properties: create, multiuse
        replace (bool?): Replaces an entire existing curve.  
                If you use this flag, you must specify the name of the curve to  
                replace, at the end of the command.  (See examples below.)  
                Properties: create

    Returns:
        str: - name of new curve-on-surface
        str: The path to the new curve or the replaced curve

    Example:
    """

