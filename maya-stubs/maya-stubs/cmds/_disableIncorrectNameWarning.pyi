from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def disableIncorrectNameWarning() -> bool:
    """Disable the warning dialog which complains about incorrect node names when opening
    Maya files.
    Returns:
        bool:

    Example:
    """

