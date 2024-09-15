from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texMoveContext(*args: Any, edit: bool = ..., query: bool = ..., editPivotMode: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., position: bool = ..., snap: bool = ..., snapComponentsRelative: bool = ..., snapPixelMode: Queryable[int] = ..., snapValue: Queryable[float] = ..., tweakMode: bool = ...) -> Union[str, bool, int, float]:
    """This command can be used to create, edit, or query a texture editor
    move manip context.
    Note that the above flags control the global behaviour of all texture
    editor move manip contexts.  Changing one context independently is not
    allowed.  Changing a context's behaviour using the above flags, will
    change all existing texture editor move manip contexts.
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
        position (bool?): Returns the current position of the manipulator  
                Properties: query
        snap (bool?): Sets or queries whether snapping is to be used.  
                Properties: query, edit
        snapComponentsRelative (bool?): Value can be : true or false.  
                If true, while snapping a group of UVs, the  
                relative spacing between them will be preserved.  
                If false, all the UVs will be snapped to the  
                target point  
                Properties: query, edit
        snapPixelMode (Queryable[int]?): Sets the snapping mode to be the pixel center or upper  
                left corner.  
                Properties: query, edit
        snapValue (Queryable[float]?): Sets or queries the size of the snapping increment.  
                Properties: query, edit
        tweakMode (bool?): When true, the manipulator is hidden and highlighted components can be selected  
                and moved in one step using a click-drag interaction.  
                Properties: query, edit

    Returns:
        str: (the name of the new context)

    Example:
    """

