from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCanBridgeEdge(*args: str) -> bool:
    """Returns true if the specified poly edges can be bridged using polyBridgeEdge.
    Returns:
        bool: Success or Failure.

    Example:
    """

