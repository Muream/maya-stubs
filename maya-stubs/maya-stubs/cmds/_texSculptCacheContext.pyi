from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texSculptCacheContext(*args: Any, edit: bool = ..., query: bool = ..., adjustSize: bool = ..., adjustStrength: bool = ..., direction: Queryable[int] = ..., falloffType: Queryable[int] = ..., floodPin: float = ..., grabTwist: bool = ..., inverted: bool = ..., mode: Queryable[str] = ..., sculptFalloffCurve: Queryable[str] = ..., showBrushRingDuringStroke: bool = ..., size: Queryable[float] = ..., strength: Queryable[float] = ...) -> Union[bool, int, str, float]:
    """This is a tool context command for uv cache sculpting tool.
    Args:
        adjustSize (bool?): If true, puts the tool into the mode where dragging the mouse will edit the brush size.  
                If false, puts the tool back into the previous sculpt mode.  
                Properties: edit
        adjustStrength (bool?): If true, puts the tool into the mode where dragging the mouse will edit the brush strength.  
                If false, puts the tool back into the previous sculpt mode.  
                Properties: edit
        direction (Queryable[int]?): Specifies how the brush determines where the uvs go.  
                Properties: query, edit
        falloffType (Queryable[int]?): Specifies how the brush determines which uvs to affect.  
                Properties: query, edit
        floodPin (float?): Sets the pin value for each UV to the given value  
                Properties: create, edit
        grabTwist (bool?): If true, the grab brush twists the UVs  
                Properties: create, query, edit
        inverted (bool?): If true, inverts the effect of the brush.  
                Properties: create, query, edit
        mode (Queryable[str]?): Specifies the type of sculpting effect the brush will perform.  
                Properties: query, edit
        sculptFalloffCurve (Queryable[str]?): Specifies the falloff curve that affects the brush.  
                Properties: query, edit
        showBrushRingDuringStroke (bool?): Specifies whether or not to show the brush ring during stroke.  
                Properties: query, edit
        size (Queryable[float]?): Specifies the world-space size of the current brush.  
                Properties: query, edit
        strength (Queryable[float]?): Specifies the world-space strength of the current brush.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

