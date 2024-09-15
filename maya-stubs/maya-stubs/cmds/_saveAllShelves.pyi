from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def saveAllShelves() -> bool:
    """This command writes all shelves that are immediate children of the specified
    control layout to the prefs directory.
    Returns:
        bool: True if successful, otherwise issues an error message and returns false.

    Example:
    """

