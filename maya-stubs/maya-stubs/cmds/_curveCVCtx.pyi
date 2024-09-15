from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def curveCVCtx(*args: Any, edit: bool = ..., query: bool = ..., bezier: bool = ..., degree: Queryable[int] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., multEndKnots: bool = ..., name: str = ..., preserveShape: bool = ..., rational: bool = ..., refit: bool = ..., symmetry: bool = ..., uniform: bool = ...) -> Union[str, bool, int]:
    """The curveCVCtx command creates a new context for creating curves
    by placing control vertices (CVs).
    Args:
        bezier (bool?):   
                Properties: create, query, edit
        degree (Queryable[int]?): Curve degree  
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
        multEndKnots (bool?): Specify if multiple end knots are to be created.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        preserveShape (bool?): Set this flag to make the operation preserve the shape  
                Properties: create, query, edit
        rational (bool?): Should the curve be rational?  
                Properties: create, query, edit
        refit (bool?): Set this flag to refit the curve  
                Properties: create, query, edit
        symmetry (bool?): Specify if symmetry is to be used  
                Properties: create, query, edit
        uniform (bool?): Should the curve use uniform parameterization?  
                Properties: create, query, edit

    Returns:
        str: (name of the new context)

    Example:
    """

