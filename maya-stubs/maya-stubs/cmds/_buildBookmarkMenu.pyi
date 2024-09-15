from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def buildBookmarkMenu(arg0: str = ..., /, *, editor: str = ..., type: str = ...) -> bool:
    """This command handles building the "dynamic" Bookmark
    menu, to show all bookmarks ("sets") of a specified
    type ("sets -text")menuName is the string returned by the "menu" command.
    Args:
        editor (str?): Name of the editor which this menu belongs to  
                Properties: create
        type (str?): Type of bookmark (sets -text) to display  
                Properties: create

    Returns:
        bool:

    Example:
    """

