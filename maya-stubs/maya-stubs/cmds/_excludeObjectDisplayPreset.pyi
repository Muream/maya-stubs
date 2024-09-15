from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def excludeObjectDisplayPreset() -> str:
    """This commands creates named presets of objects that can be used
    with the modelEditor command to exclude objects from beind displayed
    in a viewport.
    Returns:
        str: array

    Example:
    """

