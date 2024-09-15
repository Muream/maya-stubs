from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def promptDialog(*, query: bool = ..., backgroundColor: Tuple[float, float, float] = ..., button: Multiuse[str] = ..., cancelButton: str = ..., defaultButton: str = ..., dismissString: str = ..., message: str = ..., messageAlign: str = ..., parent: str = ..., scrollableField: bool = ..., style: str = ..., text: Queryable[str] = ..., title: str = ...) -> str:
    """The promptDialog command creates a modal dialog with a message to the
    user, a text field in which the user may enter a response, and a
    variable number of buttons to dismiss the dialog.  The dialog is
    dismissed when the user presses any button or chooses the
    close item from the window menu.  In the case where a button is
    pressed then the name of the button selected is returned.  If the
    dialog is dismissed via the close item then the string returned is
    specified by theflag.The default behaviour when no arguments are specified is to create an
    empty single button dialog.To obtain the text entered by the user simply query
    theflag.
    Args:
        backgroundColor (Tuple[float, float, float]?): The background color of the dialog. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0. (Windows only flag)  
                Properties: create
        button (Multiuse[str]?): Create a button with the given string as it's text.  
                Properties: create, multiuse
        cancelButton (str?): The cancel button is activated by pressing the escape key.  
                Note that this flag does not create a button, it simply indicates  
                which button created via the -b/button flag shall respond  
                to the escape key.  
                Properties: create
        defaultButton (str?): The default button is activated by pressing the enter key.  
                Note that this flag does not create a button, it simply indicates  
                which button created via the -b/button flag shall respond  
                to the enter key.  
                Properties: create
        dismissString (str?): The string returned when the user selects the 'Close' item  
                from the Window Manager menu.  If this flag is not set then the  
                string "dismiss" is returned.  
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
        scrollableField (bool?): By default a single line text field is used in the dialog.  
                Specify true for a multi-line scroll field.  
                Properties: create
        style (str?): Specify the type of input expected in the input field.  
                Vaid input types are "integer" "float" "text".  
                If this flag is not specified, we assume the input type is "text".  
                Properties: create
        text (Queryable[str]?): The field text.  
                Properties: create, query
        title (str?): The dialog title.  
                Properties: create

    Returns:
        str: Indicates how the dialog was dismissed. If a button is
            pressed then the label of the button is returned. If the dialog is
            closed then the value for the flag ds/dismissString is
            returned.

    Example:
    """

