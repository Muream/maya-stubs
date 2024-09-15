from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showSelectionInTitle(arg0: str = ..., /) -> bool:
    """This command causes the title of the window specified as an argument
    to be linked to the current file and selection. When selection
    changes, the window title will change to show the current file name
    and the name of the last selected object.
    Returns:
        bool:

    Example:
    """

