from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def waitCursor(*, query: bool = ..., state: bool = ...) -> bool:
    """This command sets/resets a wait cursor for the
    entire Maya application.
    This works as a stack, such that for eachcommand executed there should be a matchingcommand pending.If a script fails that has turned
    the wait cursor on, the wait cursor may be left on.
    You need to turn it off manually from the command line by entering
    and executing the command 'waitCursor -state off'.
    Args:
        state (bool?): Set or reset the wait cursor for the entire Maya application.  
                Properties: create, query

    Returns:
        bool: True if the wait cursor is on.

    Example:
    """

