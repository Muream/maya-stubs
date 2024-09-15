from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def snapshotBeadCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., inTangent: bool = ..., name: str = ..., outTangent: bool = ...) -> Union[str, bool]:
    """Creates a context for manipulating in and/or out tangent beads on the motion trail
    Args:
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
        inTangent (bool?): Indicates that we will be showing beads for the in tangent when  
                entering the context  
                Properties: query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        outTangent (bool?): Indicates that we will be showing beads for the out tangent when  
                entering the context  
                Properties: query, edit

    Returns:
        str: (name of the new context)

    Example:
    """

