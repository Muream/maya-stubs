from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def snapTogetherCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., clearSelection: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., setOrientation: bool = ..., snapPolygonFace: bool = ...) -> Union[str, bool]:
    """The snapTogetherCtx command creates a tool for snapping surfaces
    together.
    Args:
        clearSelection (bool?): Sets whether the tool should clear the selection  
                on entry to the tool. Default true.  
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
        setOrientation (bool?): Sets whether the tool should orient as well as moving  
                an item. Default true.  
                Properties: create, query, edit
        snapPolygonFace (bool?): Sets whether the tool should snap the cursor to  
                polygon face centers. Default false.  
                Properties: create, query, edit

    Returns:
        str: (name of the new context)

    Example:
    """

