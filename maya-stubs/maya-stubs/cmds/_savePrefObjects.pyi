from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def savePrefObjects() -> bool:
    """This command saves preference dependency nodes to "userPrefObjects.ma" in
    the user preference directory.
    Returns:
        bool: True if successful.

    Example:
    """

