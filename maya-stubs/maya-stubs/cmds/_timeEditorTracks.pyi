from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorTracks(*args: Any, edit: bool = ..., query: bool = ..., activeClipWeight: Queryable[int] = ..., activeClipWeightId: Queryable[int] = ..., addTrack: int = ..., allClips: bool = ..., allTracks: bool = ..., allTracksRecursive: bool = ..., composition: bool = ..., path: str = ..., plugIndex: Queryable[int] = ..., removeTrack: Multiuse[int] = ..., removeTrackByPath: Multiuse[str] = ..., reorderTrack: Tuple[int, int] = ..., resetMute: bool = ..., resetSolo: bool = ..., selectedTracks: bool = ..., trackGhost: bool = ..., trackIndex: Queryable[int] = ..., trackMuted: bool = ..., trackName: Queryable[str] = ..., trackSolo: bool = ..., trackType: Queryable[int] = ...) -> Union[int, bool, str]:
    """Time Editor tracks commandstimeEditor, nle
    Args:
        activeClipWeight (Queryable[int]?): Get the clip weight at the specified time.  
                Properties: query
        activeClipWeightId (Queryable[int]?): Get the clip ID carrying the active clip weight at the specified time.  
                Properties: query
        addTrack (int?): Add new track at the track index specified. Indices are 0. based.  
                Specify -1 to add the track at the end.  
                Properties: edit
        allClips (bool?): Return a list of clip IDs under the specified track.  
                Properties: query
        allTracks (bool?): Return a list of strings for all the immediate tracks for the given tracks node in the format "tracksNode:trackIndex".  
                Properties: query
        allTracksRecursive (bool?): Return a list of strings for all the tracks for the given tracks node, or  
                return a list of strings for all tracks of all tracks nodes in the format "tracksNode:trackIndex".  
                If the given root tracks node is from a composition, this command returns the tracks under that composition, including the tracks within groups that is under the same composition.  
                Properties: query
        composition (bool?): Return the composition the specified track belongs to.  
                Properties: query
        path (str?): Full path of a track node or a track on which to operate. For example: composition1|track1|group; composition1|track1.  
                			In query mode, this flag can accept a value.  
                Properties: edit
        plugIndex (Queryable[int]?): Get the plug index of the specified track.  
                Properties: query, edit
        removeTrack (Multiuse[int]?): Remove track at given index. It is a multi-use flag.  
                Properties: edit, multiuse
        removeTrackByPath (Multiuse[str]?): Remove track at given path. It is a multi-use flag. For example: composition1|track1|group|track1;  
                Properties: edit, multiuse
        reorderTrack (Tuple[int, int]?): Move the track relative to other tracks. The first argument is the track index (0. based). The second argument can be a positive or negative number  
                to indicate the steps to move. Positive numbers move forward and negative numbers move backward.  
                Properties: edit
        resetMute (bool?): Reset all the muted tracks in the active composition.  
                Properties: create
        resetSolo (bool?): Reset the soloing of all tracks on the active composition.  
                Properties: create
        selectedTracks (bool?): Return a list of the indices for all the selected tracks for the given tracks node, or  
                return a list of strings for all selected tracks of all tracks nodes in the format "tracksNode:trackIndex".  
                Properties: query
        trackGhost (bool?): Ghost all clips under track.  
                Properties: query, edit
        trackIndex (Queryable[int]?): Specify the track index. This flag is used in conjunction with the other flags.  
                			In query mode, this flag can accept a value.  
                Properties: query, edit
        trackMuted (bool?): Return whether the track is muted.  
                Properties: query, edit
        trackName (Queryable[str]?): Display name of the track.  
                Properties: query, edit
        trackSolo (bool?): Return whether the track is soloed.  
                Properties: query, edit
        trackType (Queryable[int]?): Specify the track type. Can only be used together with -at/addTrack. Does not work by itself.  
                In query mode, return the integer corresponding to the track type.  
              
                 0. Animation Track (Default)  
                 1. Audio Track  
                Properties: query, edit

    Returns:
        int: In edit mode, return the newly created Track index.

    Example:
    """

