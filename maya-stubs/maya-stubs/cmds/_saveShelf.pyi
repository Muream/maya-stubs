from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def saveShelf(arg0: str = ..., arg1: str = ..., /) -> bool:
    """This command saves the specified shelf (first argument) to the
    specified file (second argument).Note that this command doesn't work well with controls that have
    mixed mel and python command callbacks.  Also, because it saves the
    state to a mel file, it does not work with callbacks that are python
    callable objects.
    Returns:
        bool: True if successful.

    Example:
    """

