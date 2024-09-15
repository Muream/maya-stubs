from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ctxAbort() -> bool:
    """This command tells the current context to reset itself, losing
    what has been done so far.  If a escape context has been set
    it then makes that context current.
    Returns:
        bool:

    Example:
    """

