from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toggleDisplacement(*args: str) -> bool:
    """This command toggles the displacement preview of the polygon.
    This command is NOT un-doable.
    Returns:
        bool:

    Example:
    """

