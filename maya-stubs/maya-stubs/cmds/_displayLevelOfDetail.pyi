from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayLevelOfDetail(*, query: bool = ..., levelOfDetail: bool = ...) -> bool:
    """This command is responsible for setting the display level-of-detail
    for edit refreshes.  If enabled, objects will draw with lower detail
    based on their distance from the camera. When disabled objects will
    display at full resolution at all times.  This is not an undoable
    command
    Args:
        levelOfDetail (bool?): Enable/disable level of detail.

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

