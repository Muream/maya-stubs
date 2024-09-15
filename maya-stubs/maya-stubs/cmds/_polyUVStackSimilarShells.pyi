from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyUVStackSimilarShells(*args: str, onlyMatch: bool = ..., tolerance: float = ...) -> List[str]:
    """Stack Similar UV Shells.
    Args:
        onlyMatch (bool?): If this flag is true, only match UV shells and return UVs of target UV shells but don't stack.  
                Properties: create
        tolerance (float?): The tolerance setting for stacking how similar UV shells.  
                Properties: create

    Returns:
        List[str]: UVs of stacked UV Shells or target UV shells.

    Example:
    """

