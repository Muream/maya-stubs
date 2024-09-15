from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def targetWeldCtx(*args: Any, edit: bool = ..., query: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., mergeToCenter: bool = ..., preserveUV: bool = ...) -> Union[bool, str]:
    """Create a new context to weld vertices together on a poly object.
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
        mergeToCenter (bool?): If mergeToCenter is set to true then the source and target vertices's  
                will be moved to the center before doing the merge.  If set to false  
                the source vertex will be moved to the target vertex before doing the  
                merge.  
                Properties: create, query, edit
        preserveUV (bool?): When false, UVs are not changed when welding components.  
                When true, the UVs are modified to stop texture swimming  
                when welding components. Default is true.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

