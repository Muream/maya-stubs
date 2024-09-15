from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shadingConnection(arg0: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., connectionState: bool = ...) -> bool:
    """Sets the connection state of a connection between nodes that are used
    in shading. Specify the destination attribute of the connection.
    Args:
        connectionState (bool?): Specifies the state of the connection.  
                On/True/1 means the connection is still active.  
                Off/False/0 means the connection is inactive.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

