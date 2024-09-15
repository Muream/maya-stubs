from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def confirmDialog(*, annotation: Multiuse[str] = ..., backgroundColor: Tuple[float, float, float] = ..., button: Multiuse[str] = ..., cancelButton: str = ..., defaultButton: str = ..., dismissString: str = ..., icon: str = ..., message: str = ..., messageAlign: str = ..., parent: str = ..., title: str = ...) -> str:
    """The confirmDialog command creates a modal dialog with a message to the
    user and a variable number of buttons to dismiss the dialog.  The
    dialog is dismissed when the user presses any button or chooses the
    close item from the window menu.  In the case where a button is
    pressed then the name of the button selected is returned.  If the
    dialog is dismissed via the close item then the string returned is
    specified by theflag.The default behaviour when no arguments are specified is to create an
    empty single button dialog.
    Args:
        annotation (Multiuse[str]?): set the annotation for the buttons  
                Properties: create, multiuse
        backgroundColor (Tuple[float, float, float]?): The background color of the dialog. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0. (Windows only flag)  
                Properties: create
        button (Multiuse[str]?): Create a button with the given string as it's text.  
                Properties: create, multiuse
        cancelButton (str?): The cancel button is activated by pressing the escape key.  
                Note that this flag does not create a button, it simply indicates  
                which button created via the button flag shall respond  
                to the escape key.  
                Properties: create
        defaultButton (str?): The default button is activated by pressing the enter key.  
                Note that this flag does not create a button, it simply indicates  
                which button created via the button flag shall respond  
                to the enter key.  
                Properties: create
        dismissString (str?): The string returned when the user selects the 'Close' item  
                from the Window Manager menu.  If this flag is not set then the  
                string "dismiss" is returned.  
                Properties: create
        icon (str?): The user can specify one of the four standard icons -- "question", "information", "warning" and "critical".  The question icon indicates that the messsage is asking a question.  The information icon indicates that the message is nothing out of the ordinary.  The warning icon indicates that the message is a warning, but can be dealt with.  The critical icon indicates that the message represents a critical problem.  
                When no icon flag is present, we assume the user does not want to  
                include any icon in the confirm dialog.  
                Properties: create
        message (str?): The message text appearing in the dialog.  
                Properties: create
        messageAlign (str?): Align the message left, center, or right.  
                Properties: create
        parent (str?): Specify the parent window for the dialog.  The dialog will  
                be centered on this window and raise and lower with it's parent.  
                By default, the dialog is not parented to a particular window and  
                is simply centered on the screen.  
                Properties: create
        title (str?): The dialog title.  
                Properties: create

    Returns:
        str: Indicates how the dialog was dismissed. If a button is
            pressed then the label of the button is returned. If the dialog is
            closed then the value for the flag dismissString is
            returned.

    Example:
    """

