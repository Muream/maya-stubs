from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showHidden(*args: str, above: bool = ..., allObjects: bool = ..., below: bool = ..., lastHidden: bool = ...) -> bool:
    """Thecommand is used to make invisible
    objects visible.  If no flags are specified, only the objects
    given to the command will be made visible. If a parent of an object
    is invisible, the object will still be invisible. Invisibility
    is inherited. To ensure the object becomes visible, use the
    -a/above flag. This forces all invisible ancestors of the object(s)
    to be visible. If the -b/below flag is used, any invisible objects
    below the object will be made visible.  To make all objects visible,
    use the -all/allObjects flag.hide
    Args:
        above (bool?): Make objects and all their invisible ancestors visible.  
                Properties: create
        allObjects (bool?): Make all invisible objects visible.  
                Properties: create
        below (bool?): Make objects and all their invisible descendants visible.  
                Properties: create
        lastHidden (bool?): Show everything that was hidden with the last hide command.  
                Properties: create

    Returns:
        bool:

    Example:
    """

