from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def inViewMessage(*, alpha: float = ..., assistMessage: str = ..., backColor: int = ..., clear: str = ..., clickKill: bool = ..., dragKill: bool = ..., fade: bool = ..., fadeInTime: int = ..., fadeOutTime: int = ..., fadeStayTime: int = ..., font: str = ..., fontSize: int = ..., frameOffset: int = ..., hide: bool = ..., message: str = ..., minimize: bool = ..., position: str = ..., restore: bool = ..., show: bool = ..., statusMessage: str = ..., textAlpha: float = ..., textOffset: int = ..., uvEditor: bool = ...) -> bool:
    """Used for displaying in-view messages.Note: On Linux, theandflags for inViewMessage are
    only supported when running a window manager that supports compositing (transparency
    and opacity).  Otherwise, they are ignored.  In addition, the flags for message
    fading:are supported,
    but the message will display without a fade effect if the window manager
    doesn't support compositing.
    Args:
        alpha (float?): Sets the maximum alpha transparency for the message box.  
                Properties: create
        assistMessage (str?): The user assistance message to be displayed, can be html format.  
                Properties: create
        backColor (int?): Sets the background color for the message using the format 0xAARRGGBB, alpha is not taken into account.  
                Properties: create
        clear (str?): Use this flag to clear the message at a specified position.  
                The supported positions are the same as for the -pos/position flag.  
                Properties: create
        clickKill (bool?): Use this flag if the message needs to be deleted on mouse click.  
                Properties: create
        dragKill (bool?): Use this flag if the message needs to be deleted on mouse drag.  
                Properties: create
        fade (bool?): Whether the message will fade after a time interval or not.  
                Properties: create
        fadeInTime (int?): Sets how long it takes for the image to fade in (milliseconds).  
                Properties: create
        fadeOutTime (int?): Sets how long it takes for the image to fade out (milliseconds).  
                Properties: create
        fadeStayTime (int?): Sets how long the image stays at max opacity  (milliseconds).  
                Properties: create
        font (str?): Sets the message to a font (eg. "Arial").  
                Properties: create
        fontSize (int?): Sets the message font size.  
                Properties: create
        frameOffset (int?): Sets how far the message appears from the edge of the viewport in pixels.  
                Properties: create
        hide (bool?): Hides all messages.  
                Properties: create
        message (str?): The message to be displayed, can be html format.  
                General message, inherited by -amg/assistMessage and -smg/statusMessage.  
                Properties: create
        minimize (bool?): Minimize all messages.  
                Properties: create
        position (str?): The position that the message will appear at relative to the active viewport.  
                The supported positions are:  
              
                "topLeft"  
                "topCenter"  
                "topRight"  
                "midLeft"  
                "midCenter"  
                "midCenterTop"  
                "midCenterBot"  
                "midRight"  
                "botLeft"  
                "botCenter"  
                "botRight"  
                Properties: create
        restore (bool?): Restore all messages.  
                Properties: create
        show (bool?): Shows all messages.  
                Properties: create
        statusMessage (str?): The status info message to be displayed, can be html format.  
                Properties: create
        textAlpha (float?): Sets the maximum alpha transparency for the message text.  
                Properties: create
        textOffset (int?): Sets how far the text appears from the edge of the message box in pixels.  
                Properties: create
        uvEditor (bool?): Show the message in the active UV editor view.  
                Properties: create

    Returns:
        bool:

    Example:
    """

