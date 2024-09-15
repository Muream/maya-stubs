from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def track(arg0: str = ..., /, *, down: float = ..., left: float = ..., right: float = ..., upDistance01: float = ..., upDistance02: float = ...) -> bool:
    """The track command translates a camera horizontally or vertically
    in the world space. The viewing-direction and up-direction of the
    camera are not altered. There is no translation in the viewing
    direction.The track command can be applied to either a perspective or an
    orthographic camera.When no camera name is supplied, this command is applied to the
    camera in the active view.
    Args:
        down (float?): Set the amount of down translation in unit distance.  
                Properties: create
        left (float?): Set the amount of left translation in unit distance.  
                Properties: create
        right (float?): Set the amount of right translation in unit distance.  
                Properties: create
        upDistance01 (float?): Set the amount of up translation in unit distance. This is equivalent  
                to using up/upDistance02 flag.  
                Properties: create
        upDistance02 (float?): Set the amount of up translation in unit distance. This is equivalent  
                to using u/upDistance01 flag.  
                Properties: create

    Returns:
        bool:

    Example:
    """

