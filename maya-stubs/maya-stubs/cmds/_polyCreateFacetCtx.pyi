from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCreateFacetCtx(*args: Any, edit: bool = ..., query: bool = ..., append: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., maximumNumberOfPoints: Queryable[int] = ..., planarConstraint: bool = ..., subdivision: Queryable[int] = ..., texture: Queryable[int] = ...) -> Union[bool, str, int]:
    """Create a new context to create polygonal objects
    Args:
        append (bool?): Allows to switch to polyAppendFacetCtx tool  
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
        maximumNumberOfPoints (Queryable[int]?): Allows the ability to set a upper bound on the number of  
                points in interactively place before polygon is  
                created. A value less than 2 will mean that there is no  
                upper bound.  
                Properties: create, query, edit
        planarConstraint (bool?): allows/avoid new facet to be non-planar.  
                If on, all new points will be projected onto  
                current facet plane.  
                Properties: create, query, edit
        subdivision (Queryable[int]?): Number of subdivisions for each edge.  
                Default: 1  
                Properties: create, query, edit
        texture (Queryable[int]?): What texture mechanism to be applied  
                0=No textures, 1=Normalized, Undistorted textures  
                2=Unitized textures  
                Default: 0  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

