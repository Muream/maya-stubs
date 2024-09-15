from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def checkDefaultRenderGlobals(arg0: str = ..., /) -> bool:
    """To query whether or not the defaultRenderGlobals node has been modified since the last file save, use `ls -modified`. To force the scene to be dirty/clean use `file -modified`checkDefaultRenderGlobals, registration
    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

