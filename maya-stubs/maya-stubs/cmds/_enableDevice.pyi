from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def enableDevice(*args: Any, query: bool = ..., apply: bool = ..., device: Queryable[str] = ..., enable: bool = ..., monitor: bool = ..., record: bool = ...) -> Union[bool, str]:
    """Sets (or queries) the device enable state for actions involving the device.Disabling a channel for applyTake cause applyTake to ignore
    the enable state of all "child" channels -- treating them as disabled.
    Args:
        apply (bool?): enable/disable "applyTake" for the specified channel(s)  
                Properties: create, query
        device (Queryable[str]?): specifies the device to change  
                Properties: create, query
        enable (bool?): enable (or disable) monitor/record/apply  
                Properties: create, query
        monitor (bool?): enables/disables visible update for the device (default)  
                Properties: create, query
        record (bool?): enable/disable "recordDevice" device recording  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

