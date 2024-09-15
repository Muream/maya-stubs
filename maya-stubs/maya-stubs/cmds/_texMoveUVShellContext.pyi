from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texMoveUVShellContext(*args: Any, edit: bool = ..., query: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., iterations: Queryable[int] = ..., mask: bool = ..., position: bool = ..., shellBorder: Queryable[float] = ...) -> Union[str, int, bool, float]:
    """This command can be used to create, edit, or query a texture editor
    move manip context.
    Note that the above flags control the global behaviour of all texture
    editor move manip contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flags, will
    change all existing texture editor move manip contexts.
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
        iterations (Queryable[int]?): Sets or queries the number of iterations to perform.  
                Properties: query, edit
        mask (bool?): Sets or queries masking on the shell.  
                Properties: query, edit
        position (bool?): Returns the current position of the manipulator  
                Properties: query
        shellBorder (Queryable[float]?): Sets or queries the size of the shell border.  
                Properties: query, edit

    Returns:
        str: (the name of the new context)

    Example:
    """

