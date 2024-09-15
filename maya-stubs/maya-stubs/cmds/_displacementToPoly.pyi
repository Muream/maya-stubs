from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displacementToPoly(*args: str, edit: bool = ..., query: bool = ..., findBboxOnly: bool = ...) -> bool:
    """Command bakes geometry with displacement mapping into a polygonal object.displacement, to, polygon
    Args:
        findBboxOnly (bool?): When used, only the bounding box scale for the displaced object is found.  
                Properties: create, query, edit

    Returns:
        bool: Success or Failure.

    Example:
    """

