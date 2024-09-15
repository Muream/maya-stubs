from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyHole(*args: str, edit: bool = ..., query: bool = ..., assignHole: bool = ..., createHistory: bool = ...) -> bool:
    """Command to set and clear holes on given faces.poly, hole, smooth, subdiv
    Args:
        assignHole (bool?): Assign the selected faces to be hole or unassign the hole faces to be non-hole. By default, the command will  
                assign faces to be hole.  
                Properties: create, query, edit
        createHistory (bool?): For objects that have no construction history, this flag can be used  
                to force the creation of construction history for hole.  By default,  
                history is not created if the object has no history.  Regardless of this  
                flag, history is always created if the object already has history.  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

