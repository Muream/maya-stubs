from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hide(*args: str, allObjects: bool = ..., clearLastHidden: bool = ..., clearSelection: bool = ..., invertComponents: bool = ..., returnHidden: bool = ..., testVisibility: bool = ...) -> bool:
    """Thecommand is used to make objects invisible. If no flags are
    used, the objects specified, or the active objects if none are specified,
    will be made invisible.
    Args:
        allObjects (bool?): Make everything invisible (top level objects).  
                Properties: create
        clearLastHidden (bool?): Clear the last hidden list.  
                Properties: create
        clearSelection (bool?): Clear selection after the operation.  
                Properties: create
        invertComponents (bool?): Hide components that are not specified.  
                Properties: create
        returnHidden (bool?): Hide objects, but also return list of hidden objects.  
                Properties: create
        testVisibility (bool?): Do not change visibility, just test it (returns 1 is invisible, 2 if visible, 3 if partially visible).  
                Properties: create

    Returns:
        bool:

    Example:
    """

