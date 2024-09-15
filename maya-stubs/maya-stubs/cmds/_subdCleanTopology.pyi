from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdCleanTopology(*args: str) -> bool:
    """Command cleans topology of subdiv surfaces - at all levels. It cleans the
    geometry of vertices that satisfy the following conditions:
                    - Zero edits
                    - Default uvs (uvs obtained by subdividing parent face).
                    - No creases.subdivision, surface, refine, level, coarse, fine
    Returns:
        bool: Success or Failure.

    Example:
    """

