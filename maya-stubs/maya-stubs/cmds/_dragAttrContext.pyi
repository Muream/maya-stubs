from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dragAttrContext(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., connectTo: Queryable[Multiuse[str]] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., reset: bool = ...) -> Union[str, Multiuse[str]]:
    """The dragAttrContext allows a user to manipulate the attributes of an object by using
    a virtual slider within the viewport.  The virtual slider is used by dragging in a
    viewport with the middle mouse button.  The speed at which the attributes are changed
    can be controlled by holding down the Ctrl key to slow it down and the Shift key to
    speed it up.
    Args:
        connectTo (Queryable[Multiuse[str]]?): Specifies an attribute to which to connect the context. This is a multi-use  
                flag, but all attributes used must be from one object.  
                Properties: create, query, edit, multiuse
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
        reset (bool?): Resets the list of attributes to which the context is connected.  
                Properties: create, edit

    Returns:
        str: The name of the context created

    Example:
    """

