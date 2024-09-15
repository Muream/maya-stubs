from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toggleAxis(*, query: bool = ..., origin: bool = ..., view: bool = ...) -> bool:
    """Toggles the state of the display axis.Note: the display of the axis in the bottom left corner has
    been rendered obsolete by the headsUpDisplay command.
    Args:
        origin (bool?): Turns display of the axis at the origin of the ground plane  
                on or off.  
                Properties: create, query
        view (bool?): Turns display of the axis at the bottom left of each view  
                on or off. (Obsolete - refer to the headsUpDisplay command)  
                Properties: create, query

    Returns:
        bool: if in the query mode, otherwise none.

    Example:
    """

