from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timerX(*, startTime: float = ...) -> float:
    """Used to calculate elapsed time. This command returns
    sub-second accurate time values. It is useful from scripts
    for timing the length of operations. Call this command
    before and after the operation you wish to time. On the
    first call, do not use any flags. It will return the start
    time. Save this value. After the operation, call this
    command a second time, and pass the saved start time using
    the -st flag. The elapsed time will be returned.
    Args:
        startTime (float?): When this flag is used, the command returns the elapsed time since the specified start time.  
                Properties: create

    Returns:
        float: This command returns a different value depending on
            the flag used. If no flag is used, then the start time
            is returned. If the "-st" flag is used, then it returns
            the elapsed time since the start time.

    Example:
    """

