from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def saveToolSettings() -> bool:
    """This command causes all the tools not on the
    shelf to save their settings as optionVars.  This
    is called automatically by the system when Maya exits.
    Returns:
        bool:

    Example:
    """

