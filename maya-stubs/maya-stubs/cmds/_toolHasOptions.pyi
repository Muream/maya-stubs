from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toolHasOptions(arg0: str = ..., /) -> bool:
    """This command queries a tool to see if it has options. If it does,
    it returns true. Otherwise it returns false.
    Returns:
        bool: True if the queried tool has options, otherwise false.

    Example:
    """

