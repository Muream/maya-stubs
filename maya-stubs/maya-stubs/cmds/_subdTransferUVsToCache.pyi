from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def subdTransferUVsToCache(*args: str) -> bool:
    """The subdivision surface finer level uvs will get copied to the polygonToSubd
    node sent in as argument.The command takes a single subdivision surface and a single polygonToSubd
    node as input. Additional inputs will be ignored.
    Please note that this command is an internal command and is to be used
    with care, directly by the usersubdivision, surface, hierarchy, blind, data
    Returns:
        bool: Command result

    Example:
    """

