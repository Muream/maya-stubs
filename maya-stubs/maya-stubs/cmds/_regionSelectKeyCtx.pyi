from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def regionSelectKeyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., bottomManip: Queryable[float] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., leftManip: Queryable[float] = ..., name: str = ..., rightManip: Queryable[float] = ..., topManip: Queryable[float] = ...) -> Union[float, str]:
    """This command creates a context which may be used to scale keyframes
    within the graph editor using the region select tool.
    Args:
        bottomManip (Queryable[float]?): Get a point located inside the bottom manipulator of the region box, in screen space.  
                Properties: query
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
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
        leftManip (Queryable[float]?): Get a point located inside the left manipulator of the region box, in screen space.  
                Properties: query
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        rightManip (Queryable[float]?): Get a point located inside the right manipulator of the region box, in screen space.  
                Properties: query
        topManip (Queryable[float]?): Get a point located inside the top manipulator of the region box, in screen space.  
                Properties: query

    Returns:
        float: Manip values, when queried

    Example:
    """

