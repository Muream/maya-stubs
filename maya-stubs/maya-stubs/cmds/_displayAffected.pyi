from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayAffected(arg0: bool = ..., /) -> int:
    """Turns on/off the special coloring of objects that are affected by the
    objects that are currently in the selection list.If one of the curves in a loft were selected and this feature were
    turned on, then the lofted surface would be highlighted because it
    is affected by the loft curve.
    Returns:
        int: Affected display count

    Example:
    """

