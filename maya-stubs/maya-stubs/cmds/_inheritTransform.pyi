from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def inheritTransform(*args: str, query: bool = ..., off: bool = ..., on: bool = ..., preserve: bool = ..., toggle: bool = ...) -> bool:
    """This command toggles the inherit state of an object. If this
    flag is off the object will not inherit transformations from
    its parent. In other words transformations applied to the
    parent node will not affect the object and it will act as
    though it is under the world.If the -p flag is specified then the object's transformation will
    be modified to compensate when changing the inherit flag so the
    object will not change its world-space location.
    Args:
        off (bool?): turn off inherit state for the given object(s)  
                Properties: create, query
        on (bool?): turn on inherit state for the given object(s)  
                Properties: create, query
        preserve (bool?): preserve the objects world-space position  
                by modifying the object(s) transformation  
                matrix.  
                Properties: create, query
        toggle (bool?): toggle the inherit state for the given object(s)  
                (default if no flags are given)  
                -on  
                turn on inherit state for the given object(s)  
                -off  
                turn off inherit state for the given object(s)  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

