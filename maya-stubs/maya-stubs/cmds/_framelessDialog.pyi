from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def framelessDialog(*, button: Multiuse[str] = ..., message: str = ..., parent: str = ..., path: str = ..., primary: Multiuse[str] = ..., title: str = ...) -> str:
    """The framelessDialog command creates a modal dialog with a message to the
    user and a variable number of buttons to dismiss the dialog.  The
    dialog is dismissed when the user presses any button or chooses the
    close item from the window menu.  In the case where a button is
    pressed then the name of the button selected is returned.
    Args:
        button (Multiuse[str]?): Create a button with the given string as it's text.  
                Properties: create, multiuse
        message (str?): The message text appearing in the dialog.  
                Properties: create
        parent (str?): Specify the parent window for the dialog.  The dialog will  
                be centered on this window and raise and lower with it's parent.  
                By default, the dialog is not parented to a particular window and  
                is simply centered on the screen.  
                Properties: create
        path (str?): An optional path appearing after the message.  
                Properties: create
        primary (Multiuse[str]?): Set given buttons as primary.  
                Properties: create, multiuse
        title (str?): The dialog title.  
                Properties: create

    Returns:
        str: Indicates how the dialog was dismissed. If a button is
            pressed then the label of the button is returned.

    Example:
    """

