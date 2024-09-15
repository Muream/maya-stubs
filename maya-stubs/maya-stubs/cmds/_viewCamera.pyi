from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewCamera(arg0: str = ..., /, *, move: str = ..., sideView: bool = ..., topView: bool = ...) -> bool:
    """The viewCamera command is used to position a camera to look
    directly at the side or top of another camera. This is primarily
    useful for the user when he or she is setting depth-of-field and
    clipping planes, if they are being used.The default behaviour: If no other flags are specified, the camera
    in the active panel is moved and the -t is presumed. If there is a
    camera selected, it is used as the target camera.
    Args:
        move (str?): Specifies which camera needs to move.  
                Properties: create
        sideView (bool?): Position camera to look at the side of the target camera.  
                Properties: create
        topView (bool?): Position camera to look at the top of the target camera  
                (default).  
                Properties: create

    Returns:
        bool:

    Example:
    """

