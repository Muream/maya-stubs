from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showShadingGroupAttrEditor(*args: Any) -> bool:
    """The showShadingGroupAttrEditor command opens up the attribute
    editor for the current object's shading-group information.
    Returns:
        bool: true if a shading group is displayed, otherwise false.

    Example:
    """

