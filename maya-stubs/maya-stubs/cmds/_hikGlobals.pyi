from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hikGlobals(*, edit: bool = ..., query: bool = ..., releaseAllPinning: bool = ...) -> bool:
    """Sets global HumanIK flags for the application.
    Args:
        releaseAllPinning (bool?): Sets the global release all pinning hik flag. When this flag is set,  
                all pinning states are ignored.  
                Properties: query, edit

    Returns:
        bool: Giving the state of the option

    Example:
    """

