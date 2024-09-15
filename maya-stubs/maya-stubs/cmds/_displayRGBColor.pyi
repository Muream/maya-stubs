from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayRGBColor(arg0: str = ..., arg1: float = ..., arg2: float = ..., arg3: float = ..., arg4: float = ..., /, *, query: bool = ..., alpha: bool = ..., create: bool = ..., hueSaturationValue: bool = ..., list: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> Union[str, bool]:
    """This command changes or queries the display color for anything
    in the application that allows the user to set its color.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.
    Args:
        alpha (bool?): Indicates that we want to query the alpha value of the color.  
                Upon query, returns RGBA or HSVA as an array of 4 floats.  
                Properties: query
        create (bool?): Creates a new RGB display color which can be queried or set.  
                If is used only when saving color preferences.  
                name  
                Specifies the name of color to change.  
                Properties: create
        hueSaturationValue (bool?): Indicates that rgb values are really hsv values.  
                Upon query, returns the HSV values as an array of 3 floats.  
                h s v  
                The HSV values for the color.  (Between 0. 1)  
                Properties: create, query
        list (bool?): Writes out a list of all RGB color names and their value.  
                Properties: create
        resetToFactory (bool?): Resets all the RGB display colors to their factory defaults.  
                Properties: create
        resetToSaved (bool?): Resets all the RGB display colors to their saved values.  
                Properties: create

    Returns:
        str: when the list flag is used, none otherwise

    Example:
    """

