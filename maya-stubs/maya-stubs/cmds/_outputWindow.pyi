from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def outputWindow(*, query: bool = ..., show: bool = ...) -> bool:
    """This command open the output window, if it exists.
    This window shows various diagnostic, status and progress updates.
    This command does nothing on MacOS and Linux as they don't have an output window.
    Args:
        show (bool?): Show or hide the output window.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

