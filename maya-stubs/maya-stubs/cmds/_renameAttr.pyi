from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renameAttr(*args: str) -> str:
    """Renames the given user-defined attribute to the name given in the
    string argument. If the new name conflicts with an existing name then
    this command will fail.
    Note that it is not legal to rename an attribute to the empty string.node, connection, rename, attribute, dynamic
    Returns:
        str: The new name. When undone returns the original name.

    Example:
    """

