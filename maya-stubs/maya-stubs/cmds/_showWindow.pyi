from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showWindow(arg0: str = ..., /) -> bool:
    """Make a window visible. If no window is specified then the current
    window (most recently created) is used. See also thecommand'sflag.If the specified window is iconified, it will be opened.
    Returns:
        bool:

    Example:
    """

