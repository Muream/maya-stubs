from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def multiTouch(*args: Any, query: bool = ..., gestures: bool = ..., trackpad: Queryable[int] = ...) -> Union[bool, int]:
    """Used to interact with the Gestura (multi-touch) library.
    Args:
        gestures (bool?): Enables/Disables multi touch gestures.  
                Properties: create, query
        trackpad (Queryable[int]?): Sets the trackpad mode.  Values can be:  
              
                1. Cursor Control only  
                2. Multi-touch Gestures Only  
                3. Cursor and Multi-touch  
              
                Note: this is a "Mac" only flag.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

