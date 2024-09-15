from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def trackCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., alternateContext: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., toolName: Queryable[str] = ..., trackGeometry: bool = ..., trackScale: Queryable[float] = ...) -> Union[str, bool, float]:
    """This command can be used to create a track context.
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
        trackGeometry (bool?): Toggle whether the drag should try to track geometry. The  
                context will compute a track plane by intersecting the initial  
                press with geometry or the live object.  
                Properties: create, query, edit
        trackScale (Queryable[float]?): Specify the distance to the track plane from the camera. The  
                smaller the scale the slower the drag.  
                Properties: create, query, edit

    Returns:
        str: The name of the context

    Example:
    """

