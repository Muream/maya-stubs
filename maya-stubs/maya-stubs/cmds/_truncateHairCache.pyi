from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def truncateHairCache(*args: str) -> bool:
    """This command sets the end time of a hair cache to the current time.
    If the current time is less than the end time of the cache,
    the cache is truncated so that only the portion of the cache up
    to and including the current time is preserved.truncate, hair, cache
    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

