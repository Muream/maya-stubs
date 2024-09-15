from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def lsThroughFilter(arg0: str = ..., /, *args: str, item: Multiuse[str] = ..., nodeArray: bool = ..., reverse: bool = ..., selection: bool = ..., sort: str = ...) -> List[str]:
    """List all objects in the world that pass a given filter.
    Args:
        item (Multiuse[str]?): Run the filter on specified node(s), using the fast  
                version of this command.  
                Properties: create, multiuse
        nodeArray (bool?): Fast version that runs an entire array of  
                nodes through the filter at one time.  
                Properties: create
        reverse (bool?): Only available in conjunction with nodeArray flag.  
                Reverses the order of nodes in the returned arrays if true.  
                Properties: create
        selection (bool?): Run the filter on selected nodes only, using the fast  
                version of this command.  
                Properties: create
        sort (str?): Only available in conjunction with nodeArray flag.  
                Orders the nodes in the returned array. Current options are:  
                "byName", "byType", and "byTime".  
                Properties: create

    Returns:
        List[str]: List of nodes passing the filter

    Example:
    """

