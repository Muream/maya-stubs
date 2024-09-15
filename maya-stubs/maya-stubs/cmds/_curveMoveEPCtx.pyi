from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def curveMoveEPCtx(*args: Any, edit: bool = ..., query: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ...) -> str:
    """The curveMoveEPCtx command creates a new context for moving
    curve edit points using a manipulator.  Edit points can only be
    moved one at a time.
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

    Returns:
        str: (name of the new context)

    Example:
    """

