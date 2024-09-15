from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def curveEditorCtx(*args: Any, edit: bool = ..., query: bool = ..., direction: Queryable[int] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., relativeTangentSize: Queryable[float] = ..., title: Queryable[str] = ...) -> Union[str, int, float]:
    """The curveEditorCtx command creates a new NURBS editor context, which
    is used to edit a NURBS curve or surface.
    Args:
        direction (Queryable[int]?): Query the current direction of the tangent control.  Always  
                zero for the curve case.  In the surface case, its 0 for the normal  
                direction, 1 for U direction and 2 for V direction.  
                Properties: query
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
        relativeTangentSize (Queryable[float]?): Relative size of the tangent manipulator handle.  Helps  
                to adjust as the surface parameterization controls the size of the  
                tangent, even if the shape of the surface remains the same.  
                The default is 4.  
                Properties: create, query, edit
        title (Queryable[str]?): The title for the tool.  
                Properties: query, edit

    Returns:
        str: (name of the new context)

    Example:
    """

