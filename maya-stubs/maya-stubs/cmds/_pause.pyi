from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pause(*, seconds: int = ...) -> bool:
    """Pause for a specified number of seconds for canned demos or
    for test scripts to allow user to view results.
    Args:
        seconds (int?): Pause for the specified number of seconds.  
                Properties: create

    Returns:
        bool:

    Example:
    """

