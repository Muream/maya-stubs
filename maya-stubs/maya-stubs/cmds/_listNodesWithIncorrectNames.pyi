from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listNodesWithIncorrectNames() -> bool:
    """List all nodes with incorrect names in the Script Editor.
    Returns:
        bool:

    Example:
    """

