from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cacheFileTrack(*args: str, edit: bool = ..., query: bool = ..., insertTrack: int = ..., lock: bool = ..., mute: bool = ..., removeEmptyTracks: bool = ..., removeTrack: int = ..., solo: bool = ..., track: Queryable[int] = ...) -> Union[bool, int]:
    """This command is used for inserting and removing tracks related to the caches displayed in the trax editor. It can also be used to modify the track state, for example, to lock or mute a track.cache, file, disk, blend, trax, track
    Args:
        insertTrack (int?): This flag is used to insert a new empty track at the track index  
                specified.  
                Properties: create
        lock (bool?): This flag specifies whether clips on a track are to be locked or not.  
                Properties: create, query, edit
        mute (bool?): This flag specifies whether clips on a track are to be muted or not.  
                Properties: create, query, edit
        removeEmptyTracks (bool?): This flag is used to remove all tracks that have no clips.  
                Properties: create
        removeTrack (int?): This flag is used to remove the track with the specified index.  The  
                track must have no clips on it before it can be removed.  
                Properties: create
        solo (bool?): This flag specifies whether clips on a track are to be soloed or not.  
                Properties: create, query, edit
        track (Queryable[int]?): Used to specify a new track index for a cache to be displayed. Track-indices are 1. based.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

