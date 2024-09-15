from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def diskCache(*, query: bool = ..., append: bool = ..., cacheType: Queryable[str] = ..., close: Queryable[str] = ..., closeAll: bool = ..., delete: Queryable[str] = ..., deleteAll: bool = ..., empty: Queryable[str] = ..., emptyAll: bool = ..., enabledCachesOnly: bool = ..., endTime: Queryable[int] = ..., frameRangeType: Queryable[str] = ..., overSample: bool = ..., samplingRate: Queryable[int] = ..., startTime: Queryable[int] = ..., tempDir: bool = ...) -> Union[bool, str, int]:
    """Command to create, clear, or close disk cache(s).disk, cache
    Args:
        append (bool?): Append at the end and not to flush the existing cache  
                Properties: create, query
        cacheType (Queryable[str]?): Specifies the type of cache to overwrite.  "mcfp" for particle playback  
                cache, "mcfi" for particle initial cache. "mcj" for jiggle cache. This  
                option is only activated during the cache creation.  
                Properties: create, query
        close (Queryable[str]?): Close the cache given the disk cache node name.  If -eco/enabledCachesOnly  
                is "true" only enabled disk cache nodes are affected.  
                Properties: create, query
        closeAll (bool?): Close all disk cache files. If -eco/enabledCachesOnly  
                is "true" only enabled disk cache nodes are affected.  
                Properties: create, query
        delete (Queryable[str]?): Delete the cache given the disk cache node name.  If -eco/enabledCachesOnly  
                is "true" only enabled disk cache nodes are affected.  
                Properties: create, query
        deleteAll (bool?): Delete all disk cache files.  If -eco/enabledCachesOnly  
                is "true" only enabled disk cache nodes are affected.  
                Properties: create, query
        empty (Queryable[str]?): Clear the content of the disk cache with the given  
                disk cache node name.  If -eco/enabledCachesOnly  
                is "true" only enabled disk cache nodes are affected.  
                Properties: create, query
        emptyAll (bool?): Clear the content of all disk caches.  If -eco/enabledCachesOnly  
                is "true" only enabled disk cache nodes are affected.  
                Properties: create, query
        enabledCachesOnly (bool?): When present, this flag restricts the -ea/emptyAll,  
                so that only "enabled" disk caches (i.e., disk cache nodes  
                with the ".enable" attribute set to "true") are affected.  
                Properties: create, query
        endTime (Queryable[int]?): Specifies the end frame of the cache range.  
                Properties: create, query
        frameRangeType (Queryable[str]?): Specifies the type of frame range to use, namely "Render Globals",  
                "Time Slider", and "Start/End".  In the case of "Time Slider", startFrame  
                and endFrame need to be specified.  (This flag is now obsolete.  Please  
                use the -startTime and -endTime flags to specify the frame range explicitly.)  
                Properties: create, query
        overSample (bool?): Over sample if true. Otherwise, under sample.  
                Properties: create, query
        samplingRate (Queryable[int]?): Specifies how frequently to sample relative to each frame.  
                When over-sampling (-overSample has been specified),  
                this parameter determines how many times per frame the runup will be evaluated.  
                When under-sampling (the default, when -overSample has not been specified), the runup will evaluate only once per sr frames, where sr is the value specified to this flag.  
                Properties: create, query
        startTime (Queryable[int]?): Specifies the start frame of the cache range.  
                Properties: create, query
        tempDir (bool?): Query-only flag for the location of temporary diskCache files.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

