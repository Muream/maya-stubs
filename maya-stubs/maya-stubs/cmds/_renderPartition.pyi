from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderPartition(arg0: str = ..., /) -> str:
    """Set or query the model's current partition. When flagis
    not used, a partion name must be passed as an argument. In this
    case the current partition is set to that name.
    Returns:
        str: The render partition

    Example:
    """

