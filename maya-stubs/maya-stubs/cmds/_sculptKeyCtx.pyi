from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sculptKeyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeMode: Queryable[int] = ..., affectsTime: bool = ..., affectsTimeAll: Queryable[str] = ..., brushScaling: Queryable[int] = ..., editingRadius: bool = ..., editingStrength: bool = ..., exists: bool = ..., falloffCurve: Queryable[str] = ..., falloffCurveAll: Queryable[str] = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., minRadius: Queryable[float] = ..., minStrength: Queryable[float] = ..., minStrengthAll: Queryable[str] = ..., mode: Queryable[int] = ..., modeMinStrength: Multiuse[Tuple[int, float]] = ..., modeStrength: Multiuse[Tuple[int, float]] = ..., name: str = ..., radius: Queryable[float] = ..., reset: bool = ..., strength: Queryable[float] = ..., strengthAll: Queryable[str] = ...) -> Union[str, int, bool, float]:
    """This command creates a context which may be used to
    deform key frames with a sculpt brush. This context
    only works in the graph editor.
    Args:
        activeMode (Queryable[int]?): Used to query the current active sculpt mode. This can differ from the base  
                mode if the user is holding down the shift hotkey to temporarily switch to  
                smooth mode.  
                Properties: query
        affectsTime (bool?): Specifies whether or not the sculpt tools affect the time as well as the value of the keys.  
                Properties: create, query, edit
        affectsTimeAll (Queryable[str]?): Specifies whether or not the sculpt tools affect the time as well as the value of the keys  
                for all modes.  
                Properties: create, query, edit
        brushScaling (Queryable[int]?): Specifies how the sculpt brush scales relative to the Graph Editor.  
                1 = no scaling,  
                2 = scaling based on time,  
                3 = scaling based on value  
                Properties: create, query, edit
        editingRadius (bool?): Enables or disables interactive radius scaling.  
                Properties: create, edit
        editingStrength (bool?): Enables or disables interactive strength scaling.  
                Properties: create, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        falloffCurve (Queryable[str]?): Specifies the falloff curve of the sculpting effect.  
                Properties: create, query, edit
        falloffCurveAll (Queryable[str]?): Internal flag used to save/restore falloff curves for all modes.  
                Properties: create, query, edit
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
        minRadius (Queryable[float]?): Specifies the minumum radius the sculpt brush will take due to stylus pressure.  
                Cannot be more than the base brush radius.  
                Properties: create, query, edit
        minStrength (Queryable[float]?): Specifies the minumum strength of sculpting due to stylus pressure.  
                Cannot be more than the base strength.  
                Properties: create, query, edit
        minStrengthAll (Queryable[str]?): Internal flag used to save/restore min strength for all modes.  
                Properties: create, query, edit
        mode (Queryable[int]?): Specifies the base sculpt mode.  
                0 = grab,  
                1 = smooth  
                2 = smear  
                Properties: create, query, edit
        modeMinStrength (Multiuse[Tuple[int, float]]?): Specifies the min strength for the specified mode.  
                Properties: create, edit, multiuse
        modeStrength (Multiuse[Tuple[int, float]]?): Specifies the strength for the specified mode.  
                Properties: create, edit, multiuse
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        radius (Queryable[float]?): Specifies the radius of the sculpt brush.  
                Properties: create, query, edit
        reset (bool?): Internal flag used to reset current tool mode settings.  
                Properties: query, edit
        strength (Queryable[float]?): Specifies the strength of the sculpting effect for the current mode.  
                Each mode can have a different strength.  
                Properties: create, query, edit
        strengthAll (Queryable[str]?): Internal flag used to save/restore strength for all modes.  
                Properties: create, query, edit

    Returns:
        str: Context name

    Example:
    """

