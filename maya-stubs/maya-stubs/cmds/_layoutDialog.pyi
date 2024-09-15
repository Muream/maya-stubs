from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def layoutDialog(*, backgroundColor: Tuple[float, float, float] = ..., dismiss: str = ..., parent: str = ..., title: str = ..., uiScript: Callable[..., Any] = ...) -> str:
    """The layoutDialog command creates a modal dialog containing a formLayout
    with 100 divisions. The formLayout can be populated with arbitrary UI
    elements through use of the '-ui/-uiScript' flag.NOTE:A layoutDialog is not a window and certain UI elements will not function
    properly within it. In particular menuBars and panels containing menuBars
    should not be used with the layoutDialog.
    Args:
        backgroundColor (Tuple[float, float, float]?): The background color of the dialog. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0. (Windows only flag)  
                Properties: create
        dismiss (str?): Dismiss the current layoutDialog. The specified string will  
                be set as the result of the initial layoutDialog command.  
                Properties: create
        parent (str?): Specify the parent window for the dialog.  The dialog will  
                be centered on this window and raise and lower with it's parent.  
                By default, the dialog is not parented to a particular window and  
                is simply centered on the screen.  
                Properties: create
        title (str?): The dialog title.  
                Properties: create
        uiScript (Callable[..., Any]?): The specified MEL procedure name will be invoked to build the  
                UI of the layoutDialog. This flag is required when creating  
                a layoutDialog.  
                The top-level control of a layoutDialog is a formLayout with  
                100 divisions. It can be accessed by calling 'setParent -q' at  
                the beginning of the specified MEL procedure.  
                Properties: create

    Returns:
        str: The string specified by the -dismiss flag, or "dismiss" if the dialog
            was closed.

    Example:
    """

