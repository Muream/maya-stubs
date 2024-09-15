from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdiv(*args: Any, query: bool = ..., currentLevel: bool = ..., currentSubdLevel: bool = ..., deepestLevel: Queryable[int] = ..., displayLoad: bool = ..., edgeStats: bool = ..., faceStats: bool = ..., maxPossibleLevel: Queryable[int] = ..., proxyMode: Queryable[int] = ..., smallOffsets: bool = ...) -> Union[bool, int]:
    """Provides useful information about the selected subdiv or components, such
    as the deepest subdivided level, the children or parents of the currently
    selected components, etc.subdivision, surface, query, level
    Args:
        currentLevel (bool?): When queried, this flag returns an integer representing  
                the level of the currently selected subdiv surface component(s).  
                Returns -1, if there are more than one level of CVs are selected,  
                (even if they are from different objects)  
                Returns -2, if there are no input subdiv CVs to process.  
                Properties: create, query
        currentSubdLevel (bool?): When queried, this flag returns an integer representing  
                the level of the currently selected subdiv surface, regardless  
                of whether components are selected or not.  
                Returns -2, if there are no input subdiv CVs to process.  
                Properties: create, query
        deepestLevel (Queryable[int]?): When queried, this flag returns an integer representing the  
                deepest level to which the queried subdiv surface has  
                been subdivided.  
                Properties: create, query
        displayLoad (bool?): When queried, this flag prints the display load of selected subdiv  
                Properties: create, query
        edgeStats (bool?): When queried, this flag prints stats on the current subd.  
                Properties: create, query
        faceStats (bool?): When queried, this flag prints stats on the current subd.  
                Properties: create, query
        maxPossibleLevel (Queryable[int]?): When queried, this flag returns an integer representing  
                the maximum possible level to which the queried subdiv surface can  
                been subdivided.  
                Properties: create, query
        proxyMode (Queryable[int]?): When queried, this flag returns an integer representing  
                whether or not the subdivision surface is in "polygon proxy" mode.  
                "Proxy" mode allows the base mesh of a subdivision surface  
                without construction history to be edited using the polygonal  
                editing tools.  
                Returns 1, if the subdivision surface is in "polygon proxy" mode.  
                Returns 0, if the surface is not currently in "proxy" mode, but could  
                be put into "proxy" mode since it has no construction history.  (This state  
                is also known as "standard" mode.)  
                Returns 2, if the surface is not in "proxy" mode and cannot be put  
                into proxy mode, as it has construction history.  
                Properties: create, query
        smallOffsets (bool?): When queried, this flag prints the number of subdiv vertices in the  
                hierarchy that have a small enough offset so that the vertex is not required  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

