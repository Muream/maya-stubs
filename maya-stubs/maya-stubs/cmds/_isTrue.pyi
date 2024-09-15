from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def isTrue(arg0: str = ..., /) -> bool:
    """This commmand returns the state of the named condition. If the
    condition is true, it returns 1.  Otherwise it returns 0.
    Returns:
        bool:

    Example:
    """

