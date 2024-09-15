from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def refineSubdivSelectionList(*args: Any) -> bool:
    """Refines a subdivision surface set of components based on the selection list. The
    selected components are subdivided. The selection list after the command is the
    newly created components at the finer subdivision level.subdivision, surface, select, region, refine, level, coarse, fine
    Returns:
        bool: Command result

    Example:
    """

