from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdivCrease(*args: Any, sharpness: bool = ...) -> bool:
    """Set the creasing on subdivision mesh edges or mesh points that are on
    the selection list.subdivision, surface, crease
    Args:
        sharpness (bool?): Specifies the sharpness value to set the crease to  
                Properties: create

    Returns:
        bool: Command result

    Example:
    """

