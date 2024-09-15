from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listCameras(*, orthographic: bool = ..., perspective: bool = ...) -> List[str]:
    """Command to list all cameras. If no flags are given, both
    perspective and orthographic cameras will be displayed. This
    command returns an array of camera names. When the transform name
    uniquely identifies the camera it is used, otherwise the shape
    name will be returned.
    Args:
        orthographic (bool?): Display all orthographic cameras.  
                Properties: create
        perspective (bool?): Display all perspective cameras.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

