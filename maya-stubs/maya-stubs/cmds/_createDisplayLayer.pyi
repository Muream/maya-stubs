from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def createDisplayLayer(*args: str, empty: bool = ..., makeCurrent: bool = ..., name: str = ..., noRecurse: bool = ..., number: int = ...) -> str:
    """Create a new display layer.  The display layer number will be assigned
    based on the first unassigned number not less than the base index number
    found in the display layer global parameters.  Normally all objects and
    their descendants will be added to the new display layer but if the '-nr'
    flag is specified then only the objects themselves will be added.displayLayer, display, layer, color, playback, render
    Args:
        empty (bool?): If set then create an empty display layer.  ie. Do not add the selected  
                items to the new display layer.  
                Properties: create
        makeCurrent (bool?): If set then make the new display layer the current one.  
                Properties: create
        name (str?): Name of the new display layer being created.  
                Properties: create
        noRecurse (bool?): If set then only add selected objects to the display layer.  Otherwise all  
                descendants of the selected objects will also be added.  
                Properties: create
        number (int?): Number for the new display layer being created.  
                Properties: create

    Returns:
        str: Name of display layer node that was created

    Example:
    """

