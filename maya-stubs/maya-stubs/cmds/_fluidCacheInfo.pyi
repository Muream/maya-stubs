from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fluidCacheInfo(*args: str, edit: bool = ..., query: bool = ..., attribute: Queryable[str] = ..., cacheTime: Queryable[int] = ..., endFrame: bool = ..., hasCache: bool = ..., hasData: bool = ..., initialConditions: bool = ..., playback: bool = ..., resolution: bool = ..., startFrame: bool = ...) -> Union[bool, str, int]:
    """A command to get information about the fluids cache.
    Get the startFrame and resolution for InitialConditions.
    Get the endFrame as well for a playback cache.
    Note that for the playback cache, it will look at the current time
    (or last frame if the current time is past end of cache)fluid
    Args:
        attribute (Queryable[str]?): Modifier to the "hasData" flag, used to query whether a  
                cache has data (at the current time)  
                for a specific fluid attribute.  Valid attribute  
                values are "density", "velocity", "temperature", "fuel", "color",  
                "coordinates" (for texture coordinates), "falloff".  
                Properties: create, query, edit
        cacheTime (Queryable[int]?): Only valid with the -hasData flag.  The time the -hasData flag  
                uses when it queries the cache to see if there is data.  
                Properties: create, query, edit
        endFrame (bool?): Returns end time of cache as float.  
                Properties: create, query, edit
        hasCache (bool?): Returns true if fluid has specified cache, false if not.  
                Properties: create, query, edit
        hasData (bool?): Queries whether a given cache has data in it at the time specified  
                by the -time flag.  (If not -time flag is present, -hasData assumes  
                the current time.)  
                When used with  
                the "attribute" flag, indicates if data for the specified attribute  
                exists in the cache.  When used without the "attribute" flag, "hasData"  
                indicates whether there is data in the cache for any of the valid  
                fluid attributes.  
                Properties: create, query, edit
        initialConditions (bool?): Specifies the cache to be queried is the "Initial Conditions" cache.  
                Properties: create, query, edit
        playback (bool?): Specifies the cache to be queried is the "Playback" cache.  
                Properties: create, query, edit
        resolution (bool?): Returns cache resolution as float[].  
                Properties: create, query, edit
        startFrame (bool?): Returns start time for cache as float.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

