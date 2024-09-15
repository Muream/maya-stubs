from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def paramLocator(*args: str, edit: bool = ..., query: bool = ..., position: bool = ...) -> str:
    """The command creates a locator in the underworld of a NURBS curve or
    NURBS surface at the specified parameter value.  If no object is
    specified, then a locator will be created on the first valid selected item
    (either a curve point or a surface point).
    Args:
        position (bool?): Whether to set the locator position in normalized space.  
                Properties: create

    Returns:
        str: Name for the new locator in the underworld of NURBS shape.

    Example:
    """

