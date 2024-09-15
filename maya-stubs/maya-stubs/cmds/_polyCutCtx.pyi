from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCutCtx(*args: Any, edit: bool = ..., query: bool = ..., deleteFaces: bool = ..., exists: bool = ..., extractFaces: bool = ..., extractOffset: Queryable[Tuple[float, float, float]] = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ...) -> Union[bool, Tuple[float, float, float], str]:
    """Create a new context to cut facets on polygonal objects
    Args:
        deleteFaces (bool?): whether to delete the one-half of the cut-faces  
                of the poly.  If true, they are deleted.  
                Default: false  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        extractFaces (bool?): whether to extract the cut-faces of the poly  
                into a separate shell.  If true, they are extracted.  
                Default: false  
                Properties: create, query, edit
        extractOffset (Queryable[Tuple[float, float, float]]?): The displacement offset of the cut faces.  
                Default: 0.5, 0.5, 0.5  
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

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

