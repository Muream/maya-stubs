from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def buildKeyframeMenu(arg0: str = ..., /) -> bool:
    """This command handles building the "dynamic" Keyframe
    menu, to show attributes of currently selected objects,
    filtered by the current manipulator.menuName is the string returned by the "menu" command.
    The target menu will entries appended to it (and deleted from it) to always
    show what's currently keyframable.
    Returns:
        bool:

    Example:
    """

