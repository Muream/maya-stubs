from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pixelMove(arg0: int = ..., arg1: int = ..., /) -> bool:
    """The pixelMove command moves objects by what appears as pixel units
    based on the current view. It takes two integer arguments which
    specify the direction in screen space an object should appear to
    move. The vector between the center pixel of the view and the
    specified offset is mapped to some world space vector which defines
    the relative amount to move the selected objects. The mapping is
    dependent upon the view.
    Returns:
        bool:

    Example:
    """

