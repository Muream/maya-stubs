from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texRotateContext(*args: Any, edit: bool = ..., query: bool = ..., editPivotMode: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., position: bool = ..., snap: bool = ..., snapRelative: bool = ..., snapValue: Queryable[float] = ..., tweakMode: bool = ...) -> Union[str, bool, float]:
    """This command can be used to create, edit, or query a
    rotate context for the UV Editor.
    Note that the above flag controls the global behaviour of all texture
    editor rotate contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flag, will
    change all existing texture editor rotate contexts.
    Args:
        editPivotMode (bool?): Returns true when the manipulator is in edit pivot mode.  
                Properties: query
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
        position (bool?): Returns the current position of the manipulator.  
                Properties: query
        snap (bool?): Sets or queries whether snapping is to be used.  
                Properties: query, edit
        snapRelative (bool?): Sets or queries whether snapping is relative.  
                Properties: query, edit
        snapValue (Queryable[float]?): Sets or queries the size of the snapping increment.  
                Properties: query, edit
        tweakMode (bool?): When true, the manipulator is hidden and highlighted components can be selected  
                and rotated in one step using a click-drag interaction.  
                Properties: query, edit

    Returns:
        str: : name of the context created

    Example:
    """

