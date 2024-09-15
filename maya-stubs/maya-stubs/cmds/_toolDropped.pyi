from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toolDropped(arg0: str = ..., /) -> bool:
    """This command builds and executes the commands necessary to recreate the
    specified tool button.  It is invoked when a tool is dropped on the shelf.
    Returns:
        bool:

    Example:
    """

