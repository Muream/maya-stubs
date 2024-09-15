from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCacheMonitor(*, cacheValue: bool = ..., nodeName: str = ...) -> bool:
    """When the cacheInput attribute has a positive value the midModifier node caches the output mesh
    improving performance in computations of downstream nodes.
    When the counter has a zero value the midModifier releases the cached data.poly, cache
    Args:
        cacheValue (bool?): Flag to indicate whether the node's cache counter should be incremented or decremented.  
                True increments the counter, false decrements the counter.  
                Properties: create
        nodeName (str?): Name of the node whose cache counter needs to be changed.  
                Properties: create

    Returns:
        bool:

    Example:
    """

