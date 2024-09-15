from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texSmudgeUVContext(*args: Any, edit: bool = ..., query: bool = ..., dragSlider: Queryable[str] = ..., effectType: Queryable[str] = ..., exists: bool = ..., functionType: Queryable[str] = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., pressure: Queryable[float] = ..., radius: Queryable[float] = ..., smudgeIsMiddle: bool = ...) -> Union[str, float, bool]:
    """This command creates a context for smudge UV tool.  This
    context only works in the texture UV editor.
    Args:
        dragSlider (Queryable[str]?): radius | none  
                Enables the drag slider mode. This is to support brush  
                resizing while holding the 'b' or 'B' button.  
                Properties: query, edit
        effectType (Queryable[str]?): fixed | smudge  
                Specifies the effect of the tool. In fixed mode, the UVs  
                move as if they are attached by a rubber band. In smudge mode the  
                UVs are moved as the cursor is dragged over the UVs.  
                Properties: query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        functionType (Queryable[str]?): exponential | linear | constant.  
                Specifies how UVs fall off from the center of influence.  
                Properties: query, edit
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
        pressure (Queryable[float]?): Pressure value when effect type is set to smudge.  
                Properties: query, edit
        radius (Queryable[float]?): Radius of the smudge tool. All UVs within this radius are  
                affected by the tool  
                Properties: query, edit
        smudgeIsMiddle (bool?): By default, the left mouse button initiates the smudge.  
                However, this conflicts with selection. When smudgeIsMiddle is  
                on, smudge mode is activated by the middle mouse button  
                instead of the left mouse button.  
                Properties: query, edit

    Returns:
        str: Name of the effect type created.

    Example:
    """

