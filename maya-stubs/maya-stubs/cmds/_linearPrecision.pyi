from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def linearPrecision(arg0: int = ..., /) -> bool:
    """This command controls the display of linear strings in the interface.
    (See the linearField command). Setting this affects any linear strings
    displayed afterwards, formatting them so they will show at most the
    specified number of digits after the decimal point. Allowed values are
    0 through 6.
    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

