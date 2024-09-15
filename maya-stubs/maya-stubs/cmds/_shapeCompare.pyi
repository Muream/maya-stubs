from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shapeCompare(*args: str) -> int:
    """Compares two shapes.
    If no shapes are specified in the command line, then the
    shapes from the active list are used.
    Returns:
        int: 0 if successful, 1 if both shapes are not determined to be equal
            based on requested flags.

    Example:
    """

