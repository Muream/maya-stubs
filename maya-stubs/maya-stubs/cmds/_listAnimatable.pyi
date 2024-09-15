from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listAnimatable(*args: str, active: bool = ..., manip: bool = ..., manipHandle: bool = ..., shape: bool = ..., type: bool = ...) -> List[str]:
    """This command list the animatable attributes of a node.  Command flags
    allow filtering by the current manipulator, or node type.
    Args:
        active (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        manip (bool?): Return only those attributes affected by the current manip.  
                If there is no manip active and any other flags are  
                specified, output is the same as if the "-manip" flag were not present.  
                Properties: create
        manipHandle (bool?): Return only those attributes affected by the current manip handle.  
                If there is no manip handle active and any other flags are  
                specified, output is the same as if the "-manipHandle" flag were not present.  
                Properties: create
        shape (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        type (bool?): Instead of returning attributes, Return the types of nodes that  
                are currently animatable.  
                Properties: create

    Returns:
        List[str]: All animatable attributes found

    Example:
    """

