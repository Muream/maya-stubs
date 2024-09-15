from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayColor(arg0: str = ..., arg1: int = ..., /, *, query: bool = ..., active: bool = ..., create: bool = ..., dormant: bool = ..., list: bool = ..., queryIndex: int = ..., resetToFactory: bool = ..., resetToSaved: bool = ...) -> bool:
    """This command changes or queries the display color for anything
    in the application that allows the user to set its color.
    The color is defined by a color index into either the dormant
    or active color palette.
    These colors are part of the UI and not part of the saved
    data for a model.  This command is not undoable.
    Args:
        active (bool?): Specifies the color index applies to active color palette.  
                name  
                Specifies the name of color to change.  
                index  
                The color index for the color.  
                Properties: create
        create (bool?): Creates a new display color which can be queried or set.  
                If is used only when saving color preferences.  
                Properties: create
        dormant (bool?): Specifies the color index applies to dormant color palette.  
                If neither of the dormant or active flags is specified, dormant  
                is the default.  
                Properties: create
        list (bool?): Writes out a list of all color names and their value.  
                Properties: create
        queryIndex (int?): Allows you to obtain a list of color names with the given color indices.  
                Properties: create
        resetToFactory (bool?): Resets all display colors to their factory defaults.  
                Properties: create
        resetToSaved (bool?): Resets all display colors to their saved values.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

