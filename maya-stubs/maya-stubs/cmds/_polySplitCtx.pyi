from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySplitCtx(*args: Any, edit: bool = ..., query: bool = ..., enablesnap: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., magnetsnap: Queryable[int] = ..., precsnap: Queryable[float] = ..., smoothingangle: Queryable[float] = ..., snaptoedge: bool = ..., subdivision: Queryable[int] = ...) -> Union[bool, str, int, float]:
    """Create a new context to split facets on polygonal objects
    Args:
        enablesnap (bool?): Enable/disable custom magnet snapping to start/middle/end of edge  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        magnetsnap (Queryable[int]?): number of extra magnets to snap onto, regularly spaced along the edge  
                Properties: create, query, edit
        precsnap (Queryable[float]?): precision for custom magnet snapping. Range[0,100]. Value 100  
                means any click on an edge will snap to either  
                extremities or magnets.  
                Properties: create, query, edit
        smoothingangle (Queryable[float]?): the threshold that controls whether newly created edges are hard or soft  
                Properties: create, query, edit
        snaptoedge (bool?): Enable/disable snapping to edge. If enabled any click in the  
                current face will snap to the closest valid edge. If there  
                is no valid edge, the click will be ignored.  
                NOTE: This is different from magnet snapping, which causes  
                the click to snap to certain points along the edge.  
                Properties: create, query, edit
        subdivision (Queryable[int]?): number of sub-edges to add between 2 consecutive edge  
                points. Default is 1.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

