from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def curveRGBColor(arg0: str = ..., arg1: float = ..., arg2: float = ..., arg3: float = ..., /, *, query: bool = ..., hueSaturationValue: bool = ..., list: bool = ..., listNames: bool = ..., remove: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> Union[List[float], bool]:
    """This command creates, changes or removes custom curve colors,
    which are used to draw the curves in the Graph Editor.
    The custom curve names may contain the wildcards
    "?", which marches a single character, and
    "*", which matches any number of characters.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.
    Args:
        hueSaturationValue (bool?): Indicates that rgb values are really hsv values.  
                Properties: create, query
        list (bool?): Writes out a list of all curve color names and their values.  
                Properties: create
        listNames (bool?): Returns an array of all curve color names.  
                Properties: create
        remove (bool?): Removes the named curve color.  
                Properties: create
        resetToFactory (bool?): Resets all the curve colors to their factory defaults.  
                Properties: create
        resetToSaved (bool?): Resets all the curve colors to their saved values.  
                Properties: create

    Returns:
        List[float]: HSV values from querying the hsv flag

    Example:
    """

