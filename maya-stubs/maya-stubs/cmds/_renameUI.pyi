from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renameUI(arg0: str = ..., arg1: str = ..., /) -> str:
    """This command renames the UI object passed as first arument to the new
    name specified as second argument. If the
    new name is a duplicate, or not valid, then re-naming fails and the
    old name is returned.This command does not update other objects or commands that reference
    this object by name, so use this command at your own risk.
    Returns:
        str: The new name, or the old name if re-naming fails.

    Example:
    """

