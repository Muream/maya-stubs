from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def boxDollyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., alternateContext: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., toolName: Queryable[str] = ...) -> Union[str, bool]:
    """This command can be used to create, edit, or query a dolly
    context.
    Args:
        alternateContext (bool?): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.  
                Properties: create, query
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
        toolName (Queryable[str]?): Name of the specific tool to which this command refers.  
                Properties: create, query

    Returns:
        str: The name of the context

    Example:
    """

