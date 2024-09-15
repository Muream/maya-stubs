from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def coarsenSubdivSelectionList(*args: Any) -> bool:
    """Coarsens a subdivision surface set of components based on the selection list. The
    selected components are selected at a coarser level.subdivision, surface, select, region, coarsen, level, coarse, fine
    Returns:
        bool: Command result

    Example:
    """

