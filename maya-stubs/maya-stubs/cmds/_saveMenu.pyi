from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def saveMenu(arg0: str = ..., arg1: str = ..., /) -> str:
    """This command is used for saving the contents of a menu, so that
    another instance of the menu may be recreated later. The command
    writes out a file which, when run as a script, will rebuild the
    menuItems contained in the original menu. Note that the fileName
    is relative to the user's marking menu preference directory.Note that this command is used solely by the Marking Menu Editor
    and is not intended to be used for general purposes.Note that this command doesn't work well with controls that have
    mixed mel and python command callbacks.  Also, because it saves the menu
    state to a mel file, it does not work with callbacks that are python
    callable objects.The first argument is the name of the manu to save, the second one is
    the name of the file.
    Returns:
        str: The name of the saved file.

    Example:
    """

