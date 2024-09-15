from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def grabColor(*, alpha: bool = ..., hsvValue: bool = ..., rgbValue: bool = ...) -> float:
    """This command changes the cursor and enters a modal state which will be
    exited by pressing a mouse button.  The color component values of the
    pixel below the cursor at the time of the button press are returned.
    Args:
        alpha (bool?): Appends the alpha value to the results  
                Properties: create
        hsvValue (bool?): The 3 returned float values will specify the hue, saturation and  
                value color components.  
                Properties: create
        rgbValue (bool?): Default : the 3 returned float values will specify the red, green and blue  
                color components.  
                Properties: create

    Returns:
        float: []
            
            Three float values representing the color components of the pixel below
            the cursor.  If no flags are specified then the default is to return
            the red, green and blue color components.

    Example:
    """

