from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def lookThru(arg0: str = ..., arg1: str = ..., /, *, query: bool = ..., farClip: float = ..., nearClip: float = ...) -> bool:
    """This command sets a particular camera to look through in a view. This
    command may also be used to view the negative z axis of lights or
    other DAG objects. The standard camera tools can then be used to place
    the object.Note: if there are multiple objects under the transform selected,
    cameras and lights take precedence.
    Args:
        farClip (float?): Used when setting clip far plane for a new look thru camera. Will  
                not affect the attributes of an existing camera.  
                Clip values must come before shape or view.  
                Properties: create
        nearClip (float?): Used when setting near clip plane for a new look thru camera. Will  
                not affect the attributes of an existing camera.  
                Clip values must come before shape or view.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

