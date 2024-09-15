from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def isDirty(*args: str, connection: bool = ..., datablock: bool = ...) -> bool:
    """Thecommand is used to check if a plug is dirty.  The
    return value is 0 if it is not and 1 if it is.  If more than one plug
    is specified then the result is the logical "or" of all objects
    (ie. returns 1 if *any* of the plugs are dirty).
    Args:
        connection (bool?): Check the connection of the plug (default).  
                Properties: create
        datablock (bool?): Check the datablock entry for the plug.  
                Properties: create

    Returns:
        bool: Is the plug dirty? If more than one plug is given then it returns the
            logical "and" of all dirty states.

    Example:
    """

