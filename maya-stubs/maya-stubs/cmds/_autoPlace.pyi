from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def autoPlace(*, useMouse: bool = ...) -> List[float]:
    """This command takes a point in the centre of the current
    modeling pane and projects it onto the live surface.
    This produces a point in 3 space which is returned.
    If theflag is set the current mouse position
    is used rather than the centre of the modeling pane.
    Args:
        useMouse (bool?): Use the current mouse position rather than the centre of the  
                active view.  
                Properties: create

    Returns:
        List[float]: Placement location in 3D space

    Example:
    """

