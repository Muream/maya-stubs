from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def animView(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., endTime: int = ..., maxValue: float = ..., minValue: float = ..., nextView: bool = ..., previousView: bool = ..., startTime: int = ...) -> bool:
    """This command allows you to specify the current view range within
    an animation editor.
    Args:
        endTime (int?): End time to display within the editor
        maxValue (float?): Upper value to display within the editor
        minValue (float?): Lower value to display within the editor
        nextView (bool?): Switches to the next view.  
                Properties: edit
        previousView (bool?): Switches to the previous view.  
                Properties: edit
        startTime (int?): Start time to display within the editor

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

