from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def insertJointCtx(*args: Any, edit: bool = ..., query: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ...) -> str:
    """The command will create an insert joint context. The insert joint tool
    inserts joints into an existing chain of joints.
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
        str: The name of the context.

    Example:
    """

