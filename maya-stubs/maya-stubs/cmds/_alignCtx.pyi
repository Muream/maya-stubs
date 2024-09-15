from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def alignCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., align: bool = ..., anchorFirstObject: bool = ..., distribute: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., showAlignTouch: bool = ...) -> Union[str, bool]:
    """The alignCtx command creates a tool for aligning and
    distributing objects.
    Args:
        align (bool?): Align objects  
                Properties: create, query, edit
        anchorFirstObject (bool?): Anchor first or last selected object. Default false.  
                Only applicable when aligning objects.  
                Properties: create, query, edit
        distribute (bool?): Distribute objects  
                Properties: create, query, edit
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
        showAlignTouch (bool?): Show or hide align touching handles. Default true.  
                Only applicable when aligning objects.  
                Properties: create, query, edit

    Returns:
        str: (name of the new context)

    Example:
    """

