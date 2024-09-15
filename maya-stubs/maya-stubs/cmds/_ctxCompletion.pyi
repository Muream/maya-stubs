from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ctxCompletion() -> bool:
    """This command tells the current context to finish what it is
    doing and create any objects that is is working on.
    Returns:
        bool:

    Example:
    """

