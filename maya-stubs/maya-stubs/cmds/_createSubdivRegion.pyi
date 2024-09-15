from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def createSubdivRegion(*args: Any) -> bool:
    """Creates a subdivision surface region based on the selection list. Once
    a selection region is created, only the components in the selection list
    or converted from the selection list will be displayed and selectible
    through the UI.subdivision, surface, select, region
    Returns:
        bool: Command result

    Example:
    """

