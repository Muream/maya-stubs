from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynamicLoad(*args: str) -> bool:
    """Dynamically load the DLL passed as argument.
    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

