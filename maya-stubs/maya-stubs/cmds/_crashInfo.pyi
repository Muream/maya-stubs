from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def crashInfo(*, query: bool = ..., crashFile: bool = ..., crashLog: bool = ..., savedBeforeCrash: bool = ...) -> bool:
    """Provides an interface to the crash file information.
    Args:
        crashFile (bool?): Return the crash file full path name.  
                Properties: query
        crashLog (bool?): Return the crash log full path name.  
                Properties: query
        savedBeforeCrash (bool?): Return the saved file full path name before crash.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

