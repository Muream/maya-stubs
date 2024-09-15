from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def boxZoomCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., zoomScale: Queryable[float] = ...) -> Union[str, float]:
    """This command can be used to create, edit, or query a box zoom
    context. If this context is used on a perspective camera, the
    field of view and view direction are changed. If the camera is
    orthographic, the orthographic width and eye point are
    changed. The left and middle mouse interactively zoom the
    view. The control key can be used to enable box zoom. A box
    starting from left to right will zoom in, and a box starting from
    right to left will zoom out.
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
        zoomScale (Queryable[float]?): Scale the zoom.  
                Properties: create, query, edit

    Returns:
        str: The name of the context

    Example:
    """

