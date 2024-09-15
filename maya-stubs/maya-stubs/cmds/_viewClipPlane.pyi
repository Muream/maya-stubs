from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewClipPlane(arg0: str = ..., /, *, query: bool = ..., autoClipPlane: bool = ..., farClipPlane: Queryable[float] = ..., nearClipPlane: Queryable[float] = ..., surfacesOnly: bool = ...) -> Union[bool, float]:
    """The viewClipPlane command can be used to query or set a camera's
    clip planes. If a camera is not specified, the camera in the
    active view will be used. The near and far clip plane flags may be
    used in conjunction with the auto clip plane flag.
    Args:
        autoClipPlane (bool?): Compute the clip planes such that all object's in the camera's  
                viewing frustum will be visible.  
                Properties: create, query
        farClipPlane (Queryable[float]?): Set or query the far clip plane.  
                Properties: create, query
        nearClipPlane (Queryable[float]?): Set or query the near clip plane.  
                Properties: create, query
        surfacesOnly (bool?): This flag is to be used in conjunction with the auto clip  
                plane flag. Only the bounding boxes of surfaces will be used  
                to compute the camera's clipping planes.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

