from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorEditor(*, query: bool = ..., alpha: Queryable[float] = ..., hsvValue: Queryable[Tuple[float, float, float]] = ..., mini: bool = ..., parent: str = ..., position: Tuple[int, int] = ..., result: bool = ..., rgbValue: Queryable[Tuple[float, float, float]] = ...) -> Union[str, float, Tuple[float, float, float], bool]:
    """Thecommand displays a modal dialog that may be used
    to specify colors in RGB or HSV. The default behaviour
    when no arguments are specified is to provide an initial color of
    black (rgb 0.0 0.0 0.0).The command will return the user's color component values along with a
    boolean to indicate whether the dialog was dismissed by pressing
    the "OK" button.  As an alternative to responding to
    thecommand's return string you can now query
    the, andflags to get the same information.
    Args:
        alpha (Queryable[float]?): Float values corresponding to the alpha transparency component,  
                , which ranges from 0.0 to 1.0.  Use this flag to specify the  
                initial alpha value of the Color Editor, or query  
                this flag to determine the alpha value set in the editor.  
                Properties: create, query
        hsvValue (Queryable[Tuple[float, float, float]]?): Three float values corresponding to the hue, saturation, and  
                value color components, where the hue value ranges from 0.0 to 360.0  
                and the saturation and value components range from 0.0 to 1.0.  Use  
                this flag to specify the initial color of the Color Editor, or query  
                this flag to determine the color set in the editor.  
                Properties: create, query
        mini (bool?): Enable the mini color editor mode.  
                Properties: create
        parent (str?): Specify the parent window for the dialog.  The dialog will  
                be centered on this window and raise and lower with it's parent.  
                By default, the dialog is not parented to a particular window and  
                is simply centered on the screen.  
                Properties: create
        position (Tuple[int, int]?): Specify the window position for the dialog.  
                Properties: create
        result (bool?): This query only flag returns true if the dialog's "OK" button  
                was pressed, false otherwise.  If you query this flag immediately  
                after showing the Color Editor then it will return the same value  
                as the boolean value returned in the colorEditor command's  
                return string.  
                Properties: query
        rgbValue (Queryable[Tuple[float, float, float]]?): Three float values corresponding to the red, green, and blue  
                color components, all of which range from 0.0 to 1.0.  Use this  
                flag to specify the initial color of the Color Editor, or query  
                this flag to determine the color set in the editor.  
                Properties: create, query

    Returns:
        str: The string format is "float float float boolean". The first three
            float values correspond to the color components.
            
            The final argument is 1 if the dialog's "OK" button was pressed,
            and 0 if the "Cancel" button was pressed.

    Example:
    """

