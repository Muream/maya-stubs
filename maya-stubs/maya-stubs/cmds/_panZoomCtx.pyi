from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def panZoomCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., alternateContext: bool = ..., buttonDown: bool = ..., buttonUp: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., panMode: bool = ..., toolName: Queryable[str] = ..., zoomMode: bool = ..., zoomScale: Queryable[float] = ...) -> Union[str, bool, float]:
    """This command can be used to create camera 2D pan/zoom context.
    Args:
        alternateContext (bool?): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.  
                Properties: create, query
        buttonDown (bool?): Perform the button down operation  
                Properties: create
        buttonUp (bool?): Perform the button up operation  
                Properties: create
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
        panMode (bool?): Specify to create a camera 2D pan context, which is the default.  
                Properties: create
        toolName (Queryable[str]?): Name of the specific tool to which this command refers.  
                Properties: create, query
        zoomMode (bool?): Specify to create a camera 2D zoom context.  
                Properties: create
        zoomScale (Queryable[float]?): Scale the zoom. The smaller the scale the slower the drag.  
                Properties: create, query, edit

    Returns:
        str: The name of the context

    Example:
    """

