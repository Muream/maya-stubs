from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgmodified() -> List[str]:
    """Thecommand is used to find out which nodes in the
              dependency graph have been modified.  This is mostly useful for fixing
              instances where file new asks you to save when no changes have been
              made to the scene.debug, modified, nodes
    Returns:
        List[str]: list of all nodes that have been modified

    Example:
    """

