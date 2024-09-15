from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def tumbleCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., alternateContext: bool = ..., autoOrthoConstrain: bool = ..., autoSetPivot: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., localTumble: Queryable[int] = ..., name: str = ..., objectTumble: bool = ..., orthoLock: bool = ..., orthoStep: Queryable[float] = ..., toolName: Queryable[str] = ..., tumbleScale: Queryable[float] = ...) -> Union[str, bool, int, float]:
    """This command can be used to create, edit, or query a tumble
    context.
    Args:
        alternateContext (bool?): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.  
                Properties: create, query
        autoOrthoConstrain (bool?): Automatically constrain horizontal and vertical rotations when  
                the camera is orthographic. The shift key can be used to  
                unconstrain the rotation.  
                Properties: create, query, edit
        autoSetPivot (bool?): Automatically set the camera pivot to the selection or tool effect region  
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
        localTumble (Queryable[int]?): Describes what point the camera will tumble around:  
              
                0 for the camera's tumble pivot  
                1 for the camera's center of interest  
                2 for the camera's local axis, offset by its tumble pivot  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        objectTumble (bool?): Make the camera tumble around the selected object, if true.  
                Properties: create, query, edit
        orthoLock (bool?): Orthographic cameras cannot be tumbled while orthoLock is on.  
                Properties: create, query, edit
        orthoStep (Queryable[float]?): Specify the angular step in degrees for orthographic  
                rotation. If camera is orthographic and autoOrthoConstrain is  
                toggled on the rotation will be stepped by this amount.  
                Properties: create, query, edit
        toolName (Queryable[str]?): Name of the specific tool to which this command refers.  
                Properties: create, query
        tumbleScale (Queryable[float]?): Set the rotation speed. A tumble scale of 1.0 will result in  
                in 40 degrees of rotation per 100 pixels of cursor drag.  
                Properties: create, query, edit

    Returns:
        str: The name of the context

    Example:
    """

