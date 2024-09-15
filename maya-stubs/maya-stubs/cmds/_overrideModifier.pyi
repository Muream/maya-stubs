from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def overrideModifier(*args: Any, clear: bool = ..., press: Multiuse[str] = ..., release: Multiuse[str] = ...) -> bool:
    """This command allows you to assign modifier key behaviour to other
    parts of the system.  For example you can use a hotkey
    or input device instead of a modifer key to perform the same action.Note that the original modifier key behaviour is not altered in anyway.
    For example, if you've assigned "Ctrl" key behaviour to the "c" key
    then the "Ctrl" key will still work as you expect, all you've done is
    allowed yourself to use the "c" key as an alternative to the "Ctrl" key.
    Args:
        clear (bool?): Don't force any modifier keys.  
                Properties: create
        press (Multiuse[str]?): Force the following modifier to be pressed. Valid values are "Alt",  
                "Ctrl", "Shift".  
                Properties: create, multiuse
        release (Multiuse[str]?): Force the following modifier to be released. Valid values are "Alt",  
                "Ctrl", "Shift".  
                Properties: create, multiuse

    Returns:
        bool:

    Example:
    """

