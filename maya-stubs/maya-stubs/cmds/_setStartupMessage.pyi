from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setStartupMessage(arg0: str = ..., /) -> bool:
    """Update the startup window message.  Also know as the 'Splash Screen',
    this is the window that appears while the application is starting up.
    Returns:
        bool:

    Example:
    """

