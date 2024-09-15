from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def canCreateManip(*args: str) -> bool:
    """This command returns true if there can be a manipulator made for
    the specified selection, false otherwise.
    Returns:
        bool: Command result

    Example:
    """

