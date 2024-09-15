from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toggleWindowVisibility(arg0: str = ..., /) -> bool:
    """Toggle the visibility of a window. If no window is specified then
    the current window (most recently created) is used. See also
    thecommand'sflag.
    Returns:
        bool:

    Example:
    """

