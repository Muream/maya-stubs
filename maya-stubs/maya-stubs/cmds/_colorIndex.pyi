from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorIndex(arg0: int = ..., arg1: float = ..., arg2: float = ..., arg3: float = ..., /, *, query: bool = ..., active: bool = ..., dormant: bool = ..., hueSaturationValue: bool = ..., resetToFactory: bool = ..., resetToSaved: bool = ..., userColor: bool = ...) -> Union[int, bool]:
    """The index specifies a color index in the color palette.
    The r, g, and b values (between 0-1) specify the RGB values
    (or the HSV values if the -hsv flag is used) for the color.
    Args:
        active (bool?): Combined with query mode, with given index, query the active color palette.  
                Properties: create
        dormant (bool?): Combined with query mode, with given index, query the dormant color palette.  
                Properties: create
        hueSaturationValue (bool?): Indicates that rgb values are really hsv values.  
                Upon query, returns the HSV valuses as an array of 3 floats.  
                Properties: create, query
        resetToFactory (bool?): Resets all color index palette entries to their  
                factory defaults.  
                Properties: create
        resetToSaved (bool?): Resets all color palette entries to their saved values.  
                Properties: create
        userColor (bool?): Combined with query mode, with given index, query the user color palette.  
                Properties: create

    Returns:
        int: Returns 1 on success.

    Example:
    """

