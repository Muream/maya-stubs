from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def headsUpMessage(*args: Any, horizontalOffset: int = ..., object: str = ..., selection: bool = ..., time: float = ..., uvTextureEditor: bool = ..., verticalOffset: int = ..., viewport: bool = ...) -> bool:
    """This command draws a message in the 3d view.  The message
    is automatically erased at the next screen refresh.
    Args:
        horizontalOffset (int?): If this flag is specified, the message will appear  
                the specified distance (in pixels) to the right of  
                the point.  Otherwise, a default horizontal offset of 0  
                pixels is used.  
                Properties: create
        object (str?): If an object is specified, then the message is drawn  
                just above the object's bounding-box centre point.  
                If this flag is not specified, or the object is not  
                found, then the message is centred in the current view.  
                Properties: create
        selection (bool?): If this flag is specified, the message will be  
                centred among the currently selected objects.  This  
                flag does nothing if the object flag is also specified.  
                Properties: create
        time (float?): If this flag is specified, the message will be  
                displayed for a minimum of the given amount of time  
                (in seconds).  Otherwise a default time of 1.0 seconds  
                is used.  
                Properties: create
        uvTextureEditor (bool?): Should the HUD be shown in the UV Texture Editor?  
                Properties: create
        verticalOffset (int?): If this flag is specified, the message will appear  
                the specified distance (in pixels) above the point.  
                Otherwise, a default vertical offset of 0 pixels is used.  
                Properties: create
        viewport (bool?): Should the HUD be shown in the viewport?  
                Properties: create

    Returns:
        bool:

    Example:
    """

