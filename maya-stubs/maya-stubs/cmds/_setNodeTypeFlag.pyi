from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setNodeTypeFlag(arg0: str = ..., /, *, query: bool = ..., display: bool = ..., threadSafe: bool = ...) -> bool:
    """This command sets static data on the specified node type. This will affect the
    class of node type as a whole.  The argument passed may be the name of the node
    type or the node type tag.  Node type tags may be found using the objectType
    command.
    Args:
        display (bool?): Sets whether the node type will appear in the UI or not.  Setting  
                display to false will cause the node type to not appear in the UI.  
                Query mode to obtain the value of the display flag.  
                Properties: create, query
        threadSafe (bool?): This flag is obsolete.  Has no effect.  
                Properties: create, query

    Returns:
        bool: Did the command succeed?

    Example:
    """

