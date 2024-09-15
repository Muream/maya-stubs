from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hilite(*args: str, replace: bool = ..., toggle: bool = ..., unHilite: bool = ...) -> bool:
    """Hilites/Unhilites the specified object(s).  Hiliting an object makes
    it possible to select the components of the object.  If no objects
    are specified then the selection list is used.
    Args:
        replace (bool?): Hilite the specified objects.  Any objects previously  
                hilited will no longer be hilited.  
                Properties: create
        toggle (bool?): Toggle the hilite state of the specified objects.  
                Properties: create
        unHilite (bool?): Remove the specified objects from the hilite list.  
                Properties: create

    Returns:
        bool:

    Example:
    """

