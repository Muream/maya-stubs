from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikHandleDisplayScale(*args: Any) -> float:
    """This action modifies and queries the current display size of ikHandle.
    The default display scale is 1.0.
    Returns:
        float: Returns current display size of ikHandle.

    Example:
    """

