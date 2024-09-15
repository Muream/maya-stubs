from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def orbit(arg0: str = ..., /, *, horizontalAngle: float = ..., pivotPoint: Tuple[float, float, float] = ..., rotationAngles: Tuple[float, float] = ..., verticalAngle: float = ...) -> bool:
    """The orbit command revolves the camera(s) horizontally and/or
    vertically in the perspective window. The rotation axis is with
    respect to the camera.To revolve horizontally: the rotation axis is the camera up
    direction vector. To revolve vertically: the rotation axis is the
    camera left direction vector.When both the horizontal and the vertical angles are supplied on
    the command line, the camera is firstly revolved horizontally,
    then revolved vertically.This command may be applied to more than one camera; objects that
    are not cameras are ignored. When no camera name supplied, this command
    is applied to all currently active cameras.
    Args:
        horizontalAngle (float?): Angle to revolve horizontally.  
                Properties: create
        pivotPoint (Tuple[float, float, float]?): Used as the pivot point in the world space.  
                Properties: create
        rotationAngles (Tuple[float, float]?): Angle to revolve horizontally and vertically.  
                Properties: create
        verticalAngle (float?): Angle to revolve vertically.  
                Properties: create

    Returns:
        bool:

    Example:
    """

