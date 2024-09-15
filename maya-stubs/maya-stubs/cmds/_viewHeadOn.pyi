from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewHeadOn(arg0: str = ..., /) -> bool:
    """The viewHeadOn command positions the specified camera so it is
    looking "down" the normal of the live object, and fitted to the
    live object. If the live object is a surface, an arbitrary normal
    is chosen.
    Returns:
        bool:

    Example:
    """

