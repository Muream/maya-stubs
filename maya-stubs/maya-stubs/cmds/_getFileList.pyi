from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getFileList(*, filespec: str = ..., folder: str = ...) -> List[str]:
    """Returns a list of files matching an optional wildcard pattern.
    Note that this command works directly on raw system files and does not go through standard Maya file path resolution.
    Args:
        filespec (str?): wildcard specifier for search.  
                Properties: create
        folder (str?): return a directory listing  
                Properties: create

    Returns:
        List[str]: an array of file names

    Example:
    """

