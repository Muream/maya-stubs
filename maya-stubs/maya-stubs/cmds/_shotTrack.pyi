from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shotTrack(*args: str, edit: bool = ..., query: bool = ..., insertTrack: int = ..., lock: bool = ..., mute: bool = ..., numTracks: Queryable[int] = ..., removeEmptyTracks: bool = ..., removeTrack: int = ..., selfmute: bool = ..., solo: bool = ..., swapTracks: Tuple[int, int] = ..., title: Queryable[str] = ..., track: int = ..., unsolo: bool = ...) -> Union[bool, int, str]:
    """This command is used for inserting and removing tracks related to the shots displayed in the Sequencer. It can also be used to modify the track state, for example, to lock or mute a track.shot, sequencer, track
    Args:
        insertTrack (int?): This flag is used to insert a new empty track at the track index specified.  
                Properties: create
        lock (bool?): This flag specifies whether shots on a track are to be locked or not.  
                Properties: create, query, edit
        mute (bool?): This flag specifies whether shots on a track are to be muted or not.  
                Properties: create, query, edit
        numTracks (Queryable[int]?): To query the number of tracks  
                Properties: query
        removeEmptyTracks (bool?): This flag is used to remove all tracks that have no clips.  
                Properties: create
        removeTrack (int?): This flag is used to remove the track with the specified index.  The  
                track must have no clips on it before it can be removed.  
                Properties: create
        selfmute (bool?): This flag specifies whether shots on a track are to be muted or not (unlike mute, this disregards soloing).  
                Properties: create, query, edit
        solo (bool?): This flag specifies whether shots on a track are to be soloed or not.  
                Properties: create, query, edit
        swapTracks (Tuple[int, int]?): This flag is used to swap the contents of two specified tracks.  
                Properties: create
        title (Queryable[str]?): This flag specifies the title for the track.  
                Properties: create, query, edit
        track (int?): Specify the track on which to operate by using the track's trackNumber.  
                			In query mode, this flag needs a value.  
                Properties: create, query, edit
        unsolo (bool?): This flag specifies whether shots on a track are to be unsoloed or not.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

