from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def progressWindow(*, edit: bool = ..., query: bool = ..., endProgress: bool = ..., isCancelled: bool = ..., isInterruptable: bool = ..., maxValue: Queryable[int] = ..., minValue: Queryable[int] = ..., progress: Queryable[int] = ..., status: Queryable[str] = ..., step: int = ..., title: Queryable[str] = ...) -> Union[bool, int, str]:
    """The progressWindow command creates a window
    containing a status message, a graphical progress gauge,
    and optionally a "Hit ESC to Cancel" label for interruptable operations.Only one progress window is allowed on screen at a time. While the window
    is visible, the busy cursor is shown.
    Args:
        endProgress (bool?): Terminates the progress window. No other flags can be used  
                at the same time. This is normally issued through  
                MEL in response to the -ic/isCancelled flag being set or if the progress  
                value reaches its maximum.  
                Properties: create
        isCancelled (bool?): Returns true if the user has tried to cancel the operation.  
                Returns false otherwise.  
                Properties: query
        isInterruptable (bool?): Returns true if the progress window should respond to attempts  
                to cancel the operation. The cancel button is disabled if this is set  
                to true.  
                Properties: create, query, edit
        maxValue (Queryable[int]?): The maximum or "ending" value of the progress indicator.  
                If the progress value is greater than the -max/maxValue, the  
                progress value will be set to the maximum.  
                Default value is 100.  
                Properties: create, query, edit
        minValue (Queryable[int]?): The minimum or "starting" value of the progress indicator.  
                If the progress value is less than the -min/minValue, the  
                progress value will be set to the minimum.  
                Default value is 0.  
                Properties: create, query, edit
        progress (Queryable[int]?): The amount of progress currently shown on the control.  
                The value will always be between min and max.  
                Default is equal to the minimum when the control is created.  
                Properties: create, query, edit
        status (Queryable[str]?): The status text appearing above the progress gauge.  
                Properties: create, query, edit
        step (int?): Increments the -pr/progress value by the amount specified.  
                Properties: edit
        title (Queryable[str]?): The window title.  
                Properties: create, query, edit

    Returns:
        bool: Returns true if the window was successfully
            created, and false if the window could not be created (possibly
            because one is already showing).

    Example:
    """

