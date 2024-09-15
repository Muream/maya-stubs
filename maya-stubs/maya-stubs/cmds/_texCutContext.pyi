from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def texCutContext(*args: Any, edit: bool = ..., query: bool = ..., adjustSize: bool = ..., displayShellBorders: bool = ..., edgeSelectSensitive: Queryable[float] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., mode: Queryable[str] = ..., moveRatio: Queryable[float] = ..., name: str = ..., size: Queryable[float] = ..., steadyStroke: bool = ..., steadyStrokeDistance: Queryable[float] = ..., touchToSew: bool = ...) -> Union[float, bool, str]:
    """This command creates a context for cut uv tool.  This
    context only works in the UV editor.
    Args:
        adjustSize (bool?): If true, puts the tool into the mode where dragging the mouse will edit the brush size.  
                If false, puts the tool back into the previous mode.  
                Properties: edit
        displayShellBorders (bool?): Toggle the display of shell borders.  
                Properties: query, edit
        edgeSelectSensitive (Queryable[float]?): Set the value of the edge selection sensitivity.  
                Properties: query, edit
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
        mode (Queryable[str]?): Specifies the type of effect the brush will perform, Cut or Sew.  
                Properties: query, edit
        moveRatio (Queryable[float]?): The cut open ratio relative to edge length.  
                Properties: query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        size (Queryable[float]?): Brush size value of the brush ring.  
                Properties: query, edit
        steadyStroke (bool?): Turn on steady stroke or not.  
                Properties: query, edit
        steadyStrokeDistance (Queryable[float]?): The distance for steady stroke.  
                Properties: query, edit
        touchToSew (bool?): Toggle the touch to sew mode.  
                Properties: query, edit

    Returns:
        float: Size of the brush rung, when querying brushSize
        float: The value of the edge selection sensitivity, when querying the edgeSelectSensitive flag.
        bool: Whether steady stroke is on or not, when querying the steadyStroke flag.
        float: The distance for a steady stroke, when querying the steadyStrokeDistance flag.
        float: The cut open ratio relative to edge length, when querying the moveRatio flag.
        str: The type of effect the brush will perform, when querying the mode flag.
        bool: Whether shell borders are displayed, when querying the displayShellBorders flag.
        bool: Current touch-to-sew mode, when querying the touchToSew flag.

    Example:
    """

