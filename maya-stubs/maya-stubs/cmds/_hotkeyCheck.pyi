from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hotkeyCheck(*, altModifier: bool = ..., commandModifier: bool = ..., ctrlModifier: bool = ..., isRepeatable: bool = ..., keyString: str = ..., keyUp: bool = ..., optionModifier: bool = ...) -> str:
    """This command checks if the given hotkey is mapped to a nameCommand
    object.  If so, the annotation of the nameCommand object is returned.
    Otherwise an empty string is returned.
    Args:
        altModifier (bool?): Specifies if the Alt key is pressed.  
                Properties: create
        commandModifier (bool?): Specifies if the command key is pressed.  
                Properties: create
        ctrlModifier (bool?): Specifies if the Ctrl key is pressed.  
                Properties: create
        isRepeatable (bool?): Specify this flag if the hotkey is repeatable.  
                Properties: create
        keyString (str?): The key to check.  
                Properties: create
        keyUp (bool?): Specifies if the hotkey is on keyup or keydown  
                (i.e. Release or Press).  
                Properties: create
        optionModifier (bool?): Specifies if the option key is pressed.  
                Properties: create

    Returns:
        str: Contains all clients name, each followed by the annotation of the corresponding nameCommand object, or
            an empty string.

    Example:
    """

