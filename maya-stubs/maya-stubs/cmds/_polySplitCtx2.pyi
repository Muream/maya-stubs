from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySplitCtx2(*args: Any, edit: bool = ..., query: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., adjustEdgeFlow: Queryable[float] = ..., constrainToEdges: bool = ..., edgeMagnets: Queryable[int] = ..., insertWithEdgeFlow: bool = ..., snapTolerance: Queryable[float] = ..., snappedToEdgeColor: Queryable[Tuple[float, float, float]] = ..., snappedToFaceColor: Queryable[Tuple[float, float, float]] = ..., snappedToMagnetColor: Queryable[Tuple[float, float, float]] = ..., snappedToVertexColor: Queryable[Tuple[float, float, float]] = ...) -> Union[bool, str, float, int, Tuple[float, float, float]]:
    """Create a new context to split facets on polygonal objects
    Args:
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
        adjustEdgeFlow (Queryable[float]?): The weight value of the edge vertices to be positioned.  
                Properties: create, query, edit
        constrainToEdges (bool?): Enable/disable snapping to edge. If enabled any click in the  
                current face will snap to the closest valid edge. If there  
                is no valid edge, the click will be ignored.  
                NOTE: This is different from magnet snapping, which causes  
                the click to snap to certain points along the edge.  
                Properties: create, query, edit
        edgeMagnets (Queryable[int]?): number of extra magnets to snap onto, regularly spaced along the edge  
                Properties: create, query, edit
        insertWithEdgeFlow (bool?): True to enable edge flow. Otherwise, the edge flow is disabled.  
                Properties: create, query, edit
        snapTolerance (Queryable[float]?): precision for custom magnet snapping. Range[0,1]. Value 1  
                means any click on an edge will snap to either  
                extremities or magnets.  
                Properties: create, query, edit
        snappedToEdgeColor (Queryable[Tuple[float, float, float]]?): Color for edge snapping.  
                Properties: create, query, edit
        snappedToFaceColor (Queryable[Tuple[float, float, float]]?): Color for face snapping.  
                Properties: create, query, edit
        snappedToMagnetColor (Queryable[Tuple[float, float, float]]?): Color for magnet snapping.  
                Properties: create, query, edit
        snappedToVertexColor (Queryable[Tuple[float, float, float]]?): Color for vertex snapping.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

