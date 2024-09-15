from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setFocus(arg0: str = ..., /) -> bool:
    """Give keyboard focus to a specific control or panel, passed
    as an argument.
    Returns:
        bool:

    Example:
    """

