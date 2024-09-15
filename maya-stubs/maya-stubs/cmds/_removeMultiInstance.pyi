from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def removeMultiInstance(arg0: str = ..., /, *, allChildren: bool = ..., b: bool = ...) -> bool:
    """Removes a particular instance of a multiElement. This is only
    useful for input attributes since outputs will get regenerated the
    next time the node gets executed. This command will remove the
    instance and optionally break all incoming and outgoing connections
    to that instance. If the connections are not broken (with the -b
    true) flag, then the command will fail if connections exist.
    Args:
        allChildren (bool?): If the argument is true, remove all children of the multi parent.  
                Properties: create
        b (bool?): If the argument is true, all connections to the attribute  
                will be broken before the element is removed. If false, then  
                the command will fail if the element is connected.  
                Properties: create

    Returns:
        bool: (true if the instance was removed, false if something went wrong,
            like the attribute is connected but -b true was not specified)

    Example:
    """

