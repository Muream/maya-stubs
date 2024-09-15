from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setDefaultShadingGroup(arg0: str = ..., /) -> bool:
    """The setDefaultShadingGroup command is used to change which shading
    group is considered the current default shading group. Subsequently
    created objects will be assigned to the new default group.
    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

