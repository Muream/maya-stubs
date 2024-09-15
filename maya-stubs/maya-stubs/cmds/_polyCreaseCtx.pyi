from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCreaseCtx(*args: Any, edit: bool = ..., query: bool = ..., createSet: str = ..., exists: bool = ..., extendSelection: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., relative: bool = ...) -> Union[bool, str]:
    """Create a new context to crease components on polygonal objects
    Args:
        createSet (str?): Creates a set for the selected components.  
                Properties: edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        extendSelection (bool?): Enable/disable extending selection to all connected creased components.  
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
        relative (bool?): Enable/disable applying value relative to existing crease value.  
                If disabled, absolute value is applied.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

