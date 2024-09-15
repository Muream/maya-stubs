from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyFlipEdge(*args: str) -> bool:
    """Command to flip the edges shared by 2 adjacent triangles.
    When used with the edit flag, new edges can be added to the
    same node, instead of creating a separate node in the chain.poly, flip, turn, edge
    Returns:
        bool: Success or Failure.

    Example:
    """

