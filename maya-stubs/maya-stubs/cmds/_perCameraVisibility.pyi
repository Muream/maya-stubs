from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def perCameraVisibility(*args: str, query: bool = ..., camera: Queryable[str] = ..., exclusive: bool = ..., hide: bool = ..., remove: bool = ..., removeAll: bool = ..., removeCamera: bool = ...) -> Union[List[str], str, bool]:
    """The perCameraVisibility command creates, queries and removes
    visibility relationships between DAG objects and cameras.
    These relationships are applied in any viewport that uses the cameras
    involved. (They are not used e.g. in rendering.)
    Objects can be set to be exclusive to a camera (meaning they will only
    be displayed in viewports using that camera; they will be hidden in other
    viewports) or hidden from a camera (meaning they will be not visible
    in any viewport using the camera).viewport, visibility
    Args:
        camera (Queryable[str]?): Specify the camera for the operation.  
                Properties: create, query
        exclusive (bool?): Set objects as being exclusive to the given camera.  
                Properties: create, query
        hide (bool?): Set objects as being hidden from the given camera.  
                Properties: create, query
        remove (bool?): Used with exclusive or hide, removes the objects instead of adding them.  
                Properties: create
        removeAll (bool?): Remove all exclusivity/hidden objects for all cameras.  
                Properties: create
        removeCamera (bool?): Remove all exclusivity/hidden objects for the given camera.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

