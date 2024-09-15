from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynCache() -> bool:
    """Cache the current state of all particle shapes at the current time.
    Returns:
        bool:

    Example:
    """

