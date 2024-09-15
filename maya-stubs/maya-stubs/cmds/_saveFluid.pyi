from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def saveFluid(*args: str, edit: bool = ..., query: bool = ..., currentTime: Queryable[int] = ..., endTime: Queryable[int] = ..., startTime: Queryable[int] = ...) -> Union[bool, int]:
    """A command to save the current state of the fluid to the
    initial state cache. The grids to be saved are determined
    by the cache attributes: cacheDensity, cacheVelocity, etc.
    These attributes are normally set from the options on
    Set Initial State. The cache must be set up before
    invoking this command.fluid
    Args:
        currentTime (Queryable[int]?): cache state of fluid at current time  
                Properties: create, query, edit
        endTime (Queryable[int]?): end Time for cacheing  
                Properties: create, query, edit
        startTime (Queryable[int]?): start Time for cacheing  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

