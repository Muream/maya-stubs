from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def skinBindCtx(*args: Any, edit: bool = ..., query: bool = ..., about: Queryable[str] = ..., axis: Queryable[str] = ..., colorRamp: Queryable[str] = ..., currentInfluence: Queryable[str] = ..., displayInactiveMode: Queryable[int] = ..., displayNormalized: bool = ..., exists: bool = ..., falloffCurve: Queryable[str] = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., symmetry: bool = ..., tolerance: Queryable[float] = ...) -> Union[str, int, bool, float]:
    """This command creates a tool that can be used to edit volumes from an interactive bind.
    Args:
        about (Queryable[str]?): The space in which the axis should be mirrored. Valid values are: "world" and "object".  
                Properties: create, query, edit
        axis (Queryable[str]?): The mirror axis. Valid values are: "x","y", and "z".  
                Properties: create, query, edit
        colorRamp (Queryable[str]?): Set the values on the color ramp used to display the weight values.  
                Properties: create, query, edit
        currentInfluence (Queryable[str]?): Set the index of the current influence or volume to be adjusted by the manipulator.  
                Properties: create, query, edit
        displayInactiveMode (Queryable[int]?): Determines the display mode for drawing volumes that are not selected,  
                in particular which volume cages if any are displayed.  
                0. None  
                1. Nearby volumes  
                2. All volumes  
                Properties: create, query, edit
        displayNormalized (bool?): Display raw select weights (false) or finalized normalized weights (true).  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        falloffCurve (Queryable[str]?): Set the values on the falloff curve control.  
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
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        symmetry (bool?): Controls whether or not the tool operates in symmetric (mirrored) mode.  
                Properties: create, query, edit
        tolerance (Queryable[float]?): The tolerance setting for determining whether another influence is symmetric to the the current influence.  
                Properties: create, query, edit

    Returns:
        str: The name of the context created

    Example:
    """

