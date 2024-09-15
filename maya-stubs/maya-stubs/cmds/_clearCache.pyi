from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def clearCache(*args: str, allNodes: bool = ..., computed: bool = ..., dirty: bool = ...) -> int:
    """Even though dependency graph values are computed or dirty they may still
    occupy space temporarily within the nodes.  This command goes in to all of
    the data that can be regenerated if required and removes it from the caches (datablocks), thus clearing up space in memory.dependency, graph, cache, optimize, performance, memory
    Args:
        allNodes (bool?): If toggled then all nodes in the graph are cleared.  Otherwise only those  
                nodes that are selected are cleared.  
                Properties: create
        computed (bool?): If toggled then remove all data that is computable.  (Warning: If the data  
                is requested for redraw then the recompute will immediately fill the data  
                back in.)  
                Properties: create
        dirty (bool?): If toggled then remove all heavy data that is dirty.  
                Properties: create

    Returns:
        int: Number of items removed from caches

    Example:
    """

