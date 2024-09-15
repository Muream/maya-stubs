from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def unassignInputDevice(*args: Any, query: bool = ..., clutch: str = ..., device: str = ...) -> bool:
    """This command deletes all command strings associated with this
    device.
    Args:
        clutch (str?): Only delete command attachments with this clutch.  
                Properties: create
        device (str?): Specifies the device to work on.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

