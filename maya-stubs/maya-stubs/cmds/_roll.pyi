from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def roll(arg0: str = ..., /, *, absolute: bool = ..., degree: float = ..., relative: bool = ...) -> bool:
    """The roll command rotates a camera about its viewing direction, a
    positive angle produces clockwise camera rotation, while a
    negative angle produces counter-clockwise camera rotation.The default mode is relative and the rotation is applied with
    respect to the current orientation of the camera. When mode is set
    to absolute, the rotation is applied with respect to the plane
    constructed from the following three vectors in the world space:
    the world up vector, the camera view vector, and the camera up
    vector.The rotation angle is specified in degrees.The roll command can be applied to either a perspective or an
    orthographic camera.This command may be applied to more than one camera; objects that
    are not cameras are ignored. When no camera name supplied, this command
    is applied to all currently active cameras.
    Args:
        absolute (bool?): Set to absolute mode.  
                Properties: create
        degree (float?): Set the amount of the rotation angle.  
                Properties: create
        relative (bool?): Set to relative mode.  
                Properties: create

    Returns:
        bool:

    Example:
    """

