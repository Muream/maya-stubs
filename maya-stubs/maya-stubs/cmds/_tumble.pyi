from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def tumble(arg0: str = ..., /, *, azimuthAngle: float = ..., elevationAngle: float = ..., localTumble: int = ..., pivotPoint: Tuple[float, float, float] = ..., rotationAngles: Tuple[float, float] = ...) -> bool:
    """The tumble command revolves the camera(s) by varying the azimuth
    and elevation angles in the perspective window. When both the
    azimuth and the elevation angles are supplied on the command line,
    the camera is firstly tumbled for the azimuth angle, then tumbled
    for the elevation angle.When no camera name is supplied, this command is applied to the
    camera in the active view.The camera's rotate pivot will override a specified pivot point if
    the rotate pivot is not at the camera's eye point.
    Args:
        azimuthAngle (float?): Degrees to change the azimuth angle.  
                Properties: create
        elevationAngle (float?): Degrees to change the elevation angle.  
                Properties: create
        localTumble (int?): Describes what point the camera will tumble around:  
                0 for the camera's tumble pivot,  
                1 for the camera's center of interest, and  
                2 for the camera's local axis, offset by its tumble pivot.  
                Properties: create
        pivotPoint (Tuple[float, float, float]?): Three dimensional point used as the pivot point in the world  
                space.  
                Properties: create
        rotationAngles (Tuple[float, float]?): Two values in degrees to change the azimuth and elevation  
                angles.  
                Properties: create

    Returns:
        bool:

    Example:
    """

