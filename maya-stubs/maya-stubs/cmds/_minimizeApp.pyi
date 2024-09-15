from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def minimizeApp() -> bool:
    """This command minimizes (iconifies) all of the application's windows
    into a single desktop icon.  To restore the application click on the
    desktop icon.
    Returns:
        bool:

    Example:
    """

