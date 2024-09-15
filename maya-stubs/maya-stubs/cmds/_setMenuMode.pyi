from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setMenuMode(arg0: str = ..., /) -> str:
    """Optionally sets a new Menu Mode for the menu bar in the main Maya window.
    Returns the current Menu Mode, and if a new one is specified, then the previous
    Menu Mode is returned.
    Note that due to recent changes to the menu set architecture (8.0+), this function now
    takes a menu set as a parameter instead of a label.menu, menus, menubar
    Returns:
        str: The current Menu Mode for the menu bar in the main Maya window.

    Example:
    """

