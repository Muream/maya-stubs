from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polySelectEditCtx(*args: Any, edit: bool = ..., query: bool = ..., adjustEdgeFlow: Queryable[float] = ..., divisions: Queryable[int] = ..., exists: bool = ..., fixQuads: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., insertWithEdgeFlow: bool = ..., smoothingAngle: Queryable[float] = ..., splitType: Queryable[int] = ..., useEqualMultiplier: bool = ..., absoluteOffset: bool = ..., autoComplete: bool = ..., deleteEdge: bool = ..., endVertexOffset: Queryable[float] = ..., mode: Queryable[int] = ..., startVertexOffset: Queryable[float] = ...) -> Union[str, float, int, bool]:
    """Create a new context to select and edit polygonal objects
    Args:
        adjustEdgeFlow (Queryable[float]?): The weight value of the edge vertices to be positioned.  
                Default: 1.0f  
                Properties: create, query, edit
        divisions (Queryable[int]?): Number of divisions.  
                Default: 2  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        fixQuads (bool?): Fixes splits which go across a quad face leaving a 5 and 3  
                sided faces by splitting from the middle of the new edge to  
                the vertex accross from the edge on the 5 sided face.  
                Default: false  
                Properties: create, query, edit
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        insertWithEdgeFlow (bool?): True to enable edge flow. Otherwise, the edge flow is disabled.  
                Default: false  
                Properties: create, query, edit
        smoothingAngle (Queryable[float]?): Angle below which new edges will be smoothed  
                Default: kPi  
                Properties: create, query, edit
        splitType (Queryable[int]?): Format: 0. Absolute, 1. Relative, 2. Multi  
                Default: TdnpolySplitRing::Relative  
                Properties: create, query, edit
        useEqualMultiplier (bool?): Changes how the profile curve effects the offset when doing  
                a multisplit.  If true then the verts will be offset the same distance  
                based on the shortest edge being split.  If false then each inserted  
                edge loop will be offset a distance relative to the length of the edge  
                that is being split.  
                Default: true  
                Properties: create, query, edit
        absoluteOffset (bool?): This flag is deprecated. Use splitType/stp instead.  
                This flag is deprecated. Use splitType/stp instead.  
                Properties: create, query, edit
        autoComplete (bool?): If true then use auto completion on selections  
                Properties: create
        deleteEdge (bool?): When true, the end edges are deleted so the end triangles are converted to quads.  
                Properties: create, query, edit
        endVertexOffset (Queryable[float]?): Weight value controlling the offset of the end vertex of the edgeloop.  
                Properties: create, query, edit
        mode (Queryable[int]?): which mode to work on.  Available modes are 1. loop and 2. ring  
                Properties: create, query, edit
        startVertexOffset (Queryable[float]?): Weight value controlling the offset of the start vertex of the edgeloop.  
                Properties: create, query, edit

    Returns:
        str: The context name

    Example:
    """

