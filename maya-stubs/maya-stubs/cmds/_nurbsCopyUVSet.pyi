from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nurbsCopyUVSet(*args: str) -> bool:
    """This is only a sample command for debugging purposes,
    which makes a copy of the implicit st parameterization
    on a nurbs surface to be the 1st explicit uvset.nurbs, uvSet, copyUVSet
    Returns:
        bool: Success or Failure.

    Example:
    """

