from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def paintEffectsDisplay(*, query: bool = ..., meshDrawEnable: bool = ...) -> bool:
    """Command to set the global display methods for paint effects itemspaintEffects, stroke, brush, pfxGeometry, pfxHair, pfxToon
    Args:
        meshDrawEnable (bool?): Set whether mesh draw is enabled on objects  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

