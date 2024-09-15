from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def loadFluid(*args: str, edit: bool = ..., query: bool = ..., currentTime: bool = ..., frame: Queryable[float] = ..., initialConditions: bool = ...) -> Union[bool, float]:
    """A command to set builtin fluid attributes such as Density, Velocity, etc
    for all cells in the grid from the initial state cachefluid
    Args:
        currentTime (bool?): This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.  
                Properties: create, query, edit
        frame (Queryable[float]?): This flag is now obsolete. Move the cache clip in the Trax editor to view different frames of the playback cache.  
                Properties: create, query, edit
        initialConditions (bool?): load initial conditions cache  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

