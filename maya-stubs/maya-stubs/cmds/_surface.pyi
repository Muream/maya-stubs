from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def surface(*args: str, degreeU: int = ..., degreeV: int = ..., formU: str = ..., formV: str = ..., knotU: Multiuse[float] = ..., knotV: Multiuse[float] = ..., name: str = ..., objectSpace: bool = ..., point: Multiuse[Tuple[float, float, float]] = ..., pointWeight: Multiuse[Tuple[float, float, float, float]] = ..., worldSpace: bool = ...) -> str:
    """The cmd creates a NURBS spline surface (rational or non rational).
    The surface is created by specifying control vertices (CV's) and
    knot sequences in the U and V direction.  You cannot query
    the properties of the surface using this command.  See examples
    below.
    Args:
        degreeU (int?): Degree in surface U direction.  Default is degree 3.  
                Properties: create
        degreeV (int?): Degree in surface V direction.  Default is degree 3.  
                Properties: create
        formU (str?): The string for open is "open" , for closed is "closed"  or  
                for periodic is "periodic" in U.  
                Properties: create
        formV (str?): The string for open is "open" , for closed is "closed"  or  
                for periodic is "periodic" in V.  
                Properties: create
        knotU (Multiuse[float]?): Knot value(s) in U direction.  One flag per knot value. There must  
                be (numberOfPointsInU + degreeInU - 1) knots and the knot  
                vector must be non-decreasing.  
                Properties: create, multiuse
        knotV (Multiuse[float]?): Knot value(s) in V direction.  One flag per knot value. There must  
                be (numberOfPointsInV + degreeInV - 1) knots and the knot  
                vector must be non-decreasing.  
                Properties: create, multiuse
        name (str?): Name to use for new transforms.  
                Properties: create
        objectSpace (bool?): Should the operation happen in objectSpace?  
                Properties: create
        point (Multiuse[Tuple[float, float, float]]?): To specify non rational CV with (x, y, z) values.  "linear" means  
                that this flag can take values with units.  Note that you  
                must specify (degree+1) surface points in any direction to create  
                a visible surface span.  eg.  if the surface is degree 3 in the U  
                direction, you must specify 4 CVs in the U direction.  
                Points are specified in rows of U and columns of V.  If you  
                want to incorporate units, add the unit name to the value, eg.  
                "-p 3.3in 5.5ft 6.6yd"  
                Properties: create, multiuse
        pointWeight (Multiuse[Tuple[float, float, float, float]]?): To specify rational CV with (x, y, z, w) values.  "linear" means  
                that this flag can take values with units.  Note that you  
                must specify (degree+1) surface points in any direction to create  
                a visible surface span.  eg.  if the surface is degree 3 in the U  
                direction, you must specify 4 CVs in the U direction.  
                Points are specified in rows of U and columns of V.  
                Properties: create, multiuse
        worldSpace (bool?): Should the operation happen in worldSpace?  
                Properties: create

    Returns:
        str: The path to the new surface

    Example:
    """

