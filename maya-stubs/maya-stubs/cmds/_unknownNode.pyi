from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def unknownNode(arg0: str = ..., /, *, query: bool = ..., plugin: bool = ..., realClassName: bool = ..., realClassTag: bool = ...) -> Union[List[str], bool]:
    """Allows querying of the data stored for unknown nodes
    (nodes that are defined by a plug-in that Maya could not
    load when loading a scene file).
    Args:
        plugin (bool?): In query mode return the name of the plug-in from which the unknown node originated.  
                If no plug-in then the empty string is returned.  
                Properties: query
        realClassName (bool?): Return the real class name of the node.  
                Properties: query
        realClassTag (bool?): Return the real class IFF tag of the node.  
                Properties: query

    Returns:
        List[str]: in query mode

    Example:
    """

