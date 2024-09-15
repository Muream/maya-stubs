from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def encodeString(*args: str) -> str:
    """This action will take a string and encode any character that
    would need to be escaped before being sent to some other
    command. Such characters include:
    Returns:
        str: Command result

    Example:
    """

