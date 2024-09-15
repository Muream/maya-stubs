from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shadingGeometryRelCtx(*args: Any, edit: bool = ..., query: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., offCommand: Queryable[str] = ..., onCommand: Queryable[str] = ..., shadingCentric: bool = ...) -> Union[str, bool]:
    """This command creates a context that can be used for associating geometry
    to shading groups.  You can put the context into shading-centric mode
    by using the -shadingCentric flag and specifying true.  This means that the
    shading group is selected first then geometry associated with the shading
    group are highlighted.  Subsequent selections result in assignments.Specifying -shadingCentric false means that the geometry is to be selected
    first.  The shading group associated with the geometry will then be selected
    and subsequent selections will result in assignments being made.
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
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        offCommand (Queryable[str]?): command to be issued when context is turned on  
                Properties: create, query, edit
        onCommand (Queryable[str]?): command to be issued when context is turned on  
                Properties: create, query, edit
        shadingCentric (bool?): shading-centric mode.  
                Properties: create, query, edit

    Returns:
        str: Name of the context created.

    Example:
    """

