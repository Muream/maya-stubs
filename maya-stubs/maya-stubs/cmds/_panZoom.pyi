from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def panZoom(arg0: str = ..., /, *, absolute: bool = ..., downDistance: float = ..., leftDistance: float = ..., relative: bool = ..., rightDistance: float = ..., upDistance: float = ..., zoomRatio: float = ...) -> bool:
    """The panZoom command pans/zooms the 2D film.The panZoom command can be applied to either a perspective or an
    orthographic camera.When no camera name is supplied, this command is applied to the
    camera in the active view.
    Args:
        absolute (bool?): This flag modifies the behavior of the distance and zoomRatio  
                flags. If specified, the distance and zoomRatio value will be applied  
                directly.  
                Properties: create
        downDistance (float?): Set the amount of down pan distance in inches  
                Properties: create
        leftDistance (float?): Set the amount of left pan distance in inches  
                Properties: create
        relative (bool?): This flag modifies the behavior of the distance and zoomRatio  
                flags. If specified, the distance or zoomRatio value is used multiply  
                the camera's existing value. By default the relative flag is always on.  
                Properties: create
        rightDistance (float?): Set the amount of right pan distance in inches  
                Properties: create
        upDistance (float?): Set the amount of up pan distance in inches  
                Properties: create
        zoomRatio (float?): Set the amount of zoom ratio  
                Properties: create

    Returns:
        bool:

    Example:
    """

