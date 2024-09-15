from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shot(arg0: str = ..., arg1: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., audio: Queryable[str] = ..., clip: Queryable[str] = ..., clipDuration: Queryable[int] = ..., clipOpacity: Queryable[float] = ..., clipSyncState: bool = ..., clipZeroOffset: Queryable[int] = ..., copy: bool = ..., createCustomAnim: bool = ..., currentCamera: Queryable[str] = ..., customAnim: bool = ..., deleteCustomAnim: bool = ..., determineTrack: bool = ..., endTime: Queryable[int] = ..., favorite: bool = ..., flag1: bool = ..., flag10: bool = ..., flag11: bool = ..., flag12: bool = ..., flag2: bool = ..., flag3: bool = ..., flag4: bool = ..., flag5: bool = ..., flag6: bool = ..., flag7: bool = ..., flag8: bool = ..., flag9: bool = ..., hasCameraSet: bool = ..., hasStereoCamera: bool = ..., imagePlaneVisibility: bool = ..., linkAudio: Queryable[str] = ..., lock: bool = ..., mute: bool = ..., paste: bool = ..., pasteInstance: bool = ..., postHoldTime: Queryable[int] = ..., preHoldTime: Queryable[int] = ..., scale: Queryable[float] = ..., selfmute: bool = ..., sequenceDuration: Queryable[int] = ..., sequenceEndTime: Queryable[int] = ..., sequenceStartTime: Queryable[int] = ..., shotName: Queryable[str] = ..., sourceDuration: Queryable[int] = ..., startTime: Queryable[int] = ..., track: Queryable[int] = ..., transitionInLength: Queryable[int] = ..., transitionInType: Queryable[int] = ..., transitionOutLength: Queryable[int] = ..., transitionOutType: Queryable[int] = ..., unlinkAudio: bool = ...) -> Union[str, int, float, bool]:
    """Use this command to create a shot node or manipulate that node.reference, sequencer, node
    Args:
        audio (Queryable[str]?): Specify the audio clip for this shot. Audio can be linked to a shot to allow playback of specific sounds when that shot is being displayed in the Sequencer. Refer to the shot node's documentation for details on how audio is used by shots and the Sequencer.  
                Properties: create, query, edit
        clip (Queryable[str]?): The clip associated with this shot. This clip will be posted to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.  
                Properties: create, query, edit
        clipDuration (Queryable[int]?): Length of clip. This is used for the display of the clip indicator bar in the Sequencer.  
                Properties: create, query, edit
        clipOpacity (Queryable[float]?): Opacity for the shot's clip, this value is assigned to the currentCamera's imagePlane. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.  
                Properties: create, query, edit
        clipSyncState (bool?): The viewport synchronization status of the clip associated with this shot.  
                Return values are,  
                0 = no clip associated with this shot  
                1 = clip is fully in sync with viewport, and frames are 1. 1 with sequencer  
                2 = clip is partially in sync with viewport, movie may be scaled to match sequencer  
                3 = clip not in sync with viewport (i.e. could have scale/time/camera differences)  
                Properties: create, query, edit
        clipZeroOffset (Queryable[int]?): Specify which time of the clip corresponds to the beginning of the shot. This is used to properly align splitted clips.  
                Properties: create, query, edit
        copy (bool?): This flag is used to copy a shot to the clipboard. In query mode, this flag allows you to query what, if anything, has been copied into the shot clipboard.  
                Properties: create, query, edit
        createCustomAnim (bool?): Creates an animation layer and links the shot node's customAnim attr to the weight  
                attr of the animation layer  
                Properties: edit
        currentCamera (Queryable[str]?): The camera associated with this shot. Refer to the shot node's documentation for details on how cameras are used by shots and the Sequencer.  
                Properties: create, query, edit
        customAnim (bool?): Returns the name of the animation layer node linked to this shot node's customAnim attr  
                Properties: query
        deleteCustomAnim (bool?): Disconnects the animation layer from this shot's customAnim attr and deletes the  
                animation layer node  
                Properties: edit
        determineTrack (bool?): Determines an available track for the shot. Returns a new track number or the  
                existing track number if the current track is available.  
                Properties: query, edit
        endTime (Queryable[int]?): The shot end time in the Maya timeline. Changing the startTime will extend the duration of a shot.  
                Properties: create, query, edit
        favorite (bool?): Make the shot a favorite. This is a UI indicator only to streamline navigation in the Sequencer panel  
                Properties: create, query, edit
        flag1 (bool?): User specified state flag 1/12 for this shot  
                Properties: create, query, edit
        flag10 (bool?): User specified state flag 10/12 for this shot  
                Properties: create, query, edit
        flag11 (bool?): User specified state flag 11/12 for this shot  
                Properties: create, query, edit
        flag12 (bool?): User specified state flag 12/12 for this shot  
                Properties: create, query, edit
        flag2 (bool?): User specified state flag 2/12 for this shot  
                Properties: create, query, edit
        flag3 (bool?): User specified state flag 3/12 for this shot  
                Properties: create, query, edit
        flag4 (bool?): User specified state flag 4/12 for this shot  
                Properties: create, query, edit
        flag5 (bool?): User specified state flag 5/12 for this shot  
                Properties: create, query, edit
        flag6 (bool?): User specified state flag 6/12 for this shot  
                Properties: create, query, edit
        flag7 (bool?): User specified state flag 7/12 for this shot  
                Properties: create, query, edit
        flag8 (bool?): User specified state flag 8/12 for this shot  
                Properties: create, query, edit
        flag9 (bool?): User specified state flag 9/12 for this shot  
                Properties: create, query, edit
        hasCameraSet (bool?): Returns true if the camera associated with this shot is a camera set.  
                Properties: create, query, edit
        hasStereoCamera (bool?): Returns true if the camera associated with this shot is a stereo camera.  
                Properties: create, query, edit
        imagePlaneVisibility (bool?): Visibility of the shot imageplane, this value is assigned to the currentCamera's imagePlane.  
                Properties: create, query, edit
        linkAudio (Queryable[str]?): Specify an audio clip to link to this shot. Any currently linked audio will be unlinked.  
                Properties: create, query, edit
        lock (bool?): Lock a specific shot. This is different than locking an entire track, which is done via the shotTrack command  
                Properties: create, query, edit
        mute (bool?): Mute a specific shot. This is different than muting an entire track, which is done via the shotTrack command. Querying this attribute will return true if the shot is muted due to its own mute, its shot being muted, or its shot being unsoloed. See flag "selfmute" to query only the shot's own state.  
                Properties: create, query, edit
        paste (bool?): This flag is used to paste a shot or shots from the clipboard to the sequence timeline. Shots are added to the clipboard using the c/copy flag.  
                Properties: create, query, edit
        pasteInstance (bool?): This flag is used to paste an instance of a shot or shots from the clipboard to the sequence timeline. Unlike the p/paste flag, which duplicates the camera and image plane from the original source shot, the pi/pasteInstance flag shares the camera and image plane from the source shot. The audio node is duplicated.  
                Properties: create, query, edit
        postHoldTime (Queryable[int]?): Specify the time length to append to the shot in the sequence timeline. This repeats the last frame of the shot, in sequence time, over the specified duration.  
                Properties: create, query, edit
        preHoldTime (Queryable[int]?): Specify the time length to prepend to the shot in the sequence timeline. This repeats the first frame of the shot, in sequence time, over the specified duration.  
                Properties: create, query, edit
        scale (Queryable[float]?): Specify an amount to scale the Maya frame range of the shot. This will affect the sequenceEndFrame, leaving the sequenceStartFrame unchanged.  
                Properties: create, query, edit
        selfmute (bool?): Query if this individual shot's own mute state is set. This is different from the flag "mute", which will return true if this shot is muted due to the track being muted or another track being soloed. Editing this flag will set this shot's own mute status (identical behavior as the flag "mute").  
                Properties: create, query, edit
        sequenceDuration (Queryable[int]?): Return the sequence duration of the shot, which will include the holds and scale. This flag can only be queried.  
                Properties: query, edit
        sequenceEndTime (Queryable[int]?): The shot end in the sequence timeline. Changing the endTime of a shot will scale it in sequence time.  
                Properties: create, query, edit
        sequenceStartTime (Queryable[int]?): The shot start in the sequence timeline. Changing the startTime of a shot will shift it in sequence time.  
                Properties: create, query, edit
        shotName (Queryable[str]?): Specify a user-defined name for this shot. This allows the assignment of names that are not valid as node names within Maya. Whenever the shotName attribute is defined its value is used in the UI.  
                Properties: create, query, edit
        sourceDuration (Queryable[int]?): Return the number of source frames in the shot. This flag can only be queried.  
                Properties: query, edit
        startTime (Queryable[int]?): The shot start time in the Maya timeline. Changing the startTime will extend the duration of a shot.  
                Properties: create, query, edit
        track (Queryable[int]?): Specify the track in which this shot resides.  
                Properties: query, edit
        transitionInLength (Queryable[int]?): Length of the transtion into the shot.  
                Properties: create, query, edit
        transitionInType (Queryable[int]?): Specify the the type of transition for the transition into the shot.  
                0 = Fade  
                1 = Dissolve  
                Properties: query, edit
        transitionOutLength (Queryable[int]?): Length of the transtion out of the shot.  
                Properties: create, query, edit
        transitionOutType (Queryable[int]?): Specify the the type of transition for the transition out of the shot.  
                0 = Fade  
                1 = Dissolve  
                Properties: query, edit
        unlinkAudio (bool?): COMMENT  
                Unlinks any currently linked audio.  
                Properties: query, edit

    Returns:
        str: Shot name

    Example:
    """

