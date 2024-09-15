from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cacheFileMerge(*args: str, edit: bool = ..., query: bool = ..., endTime: int = ..., geometry: bool = ..., startTime: int = ...) -> Union[List[float], List[str], bool]:
    """If selected/specified caches can be successfully merged, will return the start/end frames of the new cache followed by the
    start/end frames of any gaps in the merged cache for which no data should be written to file. In query mode, will return
    the names of geometry associated with the specified cache file nodes.cache, file, merge, disk
    Args:
        endTime (int?): Specifies the end frame of the merge range. If not specified, will figure  
                out range from times of caches being merged.  
                Properties: create
        geometry (bool?): Query-only flag used to find the geometry nodes associated with the specified cache files.  
                Properties: query
        startTime (int?): Specifies the start frame of the merge range. If not specified, will figure  
                out range from the times of the caches being merged.  
                Properties: create

    Returns:
        List[float]: The start and end times of merged cache followed by start/end of any gaps
        List[str]: Names of geometry associated with specified cache in query mode.

    Example:
    """

