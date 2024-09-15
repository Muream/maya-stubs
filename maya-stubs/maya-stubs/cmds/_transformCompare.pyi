from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def transformCompare(*args: str, root: bool = ...) -> int:
    """Compares two transforms passed as arguments. If they are the same,
    returns 0. If they are different, returns 1. If no transforms are
    specified in the command line, then the transforms from the active
    list are used.
    Args:
        root (bool?): Compare the root only, rather than the entire hierarchy below the roots.  
                Properties: create

    Returns:
        int: 0 if successful, 1 if transform1 and transform2 are not determined to be equal.

    Example:
    """

