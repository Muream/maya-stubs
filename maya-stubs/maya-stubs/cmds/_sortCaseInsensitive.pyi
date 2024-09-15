from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sortCaseInsensitive(*args: str) -> List[str]:
    """This command sorts all the strings of an array in a case insensitive way.sort, case, insensitive
    Returns:
        List[str]: string to sort

    Example:
    """

