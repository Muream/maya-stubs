from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def clipSchedule(*args: str, edit: bool = ..., query: bool = ..., allAbsolute: bool = ..., allRelative: bool = ..., blend: Queryable[Tuple[int, int]] = ..., blendNode: Queryable[Tuple[int, int]] = ..., blendUsingNode: str = ..., character: bool = ..., clipIndex: Queryable[int] = ..., cycle: Queryable[float] = ..., defaultAbsolute: bool = ..., enable: bool = ..., group: bool = ..., groupIndex: Multiuse[int] = ..., groupName: Queryable[str] = ..., hold: Queryable[int] = ..., insertTrack: int = ..., instance: str = ..., listCurves: bool = ..., listPairs: bool = ..., lock: bool = ..., mute: bool = ..., name: Queryable[str] = ..., postCycle: Queryable[float] = ..., preCycle: Queryable[float] = ..., remove: bool = ..., removeBlend: Tuple[int, int] = ..., removeEmptyTracks: bool = ..., removeTrack: int = ..., rotationsAbsolute: bool = ..., scale: Queryable[float] = ..., shift: int = ..., shiftIndex: Multiuse[int] = ..., solo: bool = ..., sourceClipName: bool = ..., sourceEnd: Queryable[int] = ..., sourceStart: Queryable[int] = ..., start: Queryable[int] = ..., track: Queryable[int] = ..., weight: Queryable[float] = ..., weightStyle: Queryable[int] = ...) -> Union[str, bool, Tuple[int, int], int, float]:
    """This command is used to create, edit and query clips and blends in the Trax editor. It operates on the clipScheduler node attached to the character. In query mode, if no flags are specified, returns an array of strings in this form:
     (clipName,clipIndex,clipStart,clipSourceStart,clipSourceEnd,clipScale,clipPreCycle,clipPostCycle,clipHold)character, clip, animation
    Args:
        allAbsolute (bool?): Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.  
                Properties: query, edit
        allRelative (bool?): Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.  
                Properties: query, edit
        blend (Queryable[Tuple[int, int]]?): This flag is used to blend two clips, whose indices are provided as flag arguments.  
                Properties: create, query
        blendNode (Queryable[Tuple[int, int]]?): This query only flag list all of the blend nodes associated with the blend defined by the two clip indices. This flag returns a string array.  
                			In query mode, this flag can accept a value.  
                Properties: query
        blendUsingNode (str?): This flag is used to blend using an existing blend node. It is used in conjunction with the blend flag. The blend flag specifies the clip indices for the blend. The name of an existing animBlend node should be supplied supplied as an argument for the blendUsingNode flag.  
                Properties: create
        character (bool?): This flag is used to query which characters this scheduler controls. It returns an array of strings.  
                Properties: query
        clipIndex (Queryable[int]?): Specify the index of the clip to schedule. In query mode, returns  
                an array of strings in this form:  
                (clipName,index,start,sourceStart,sourceEnd,scale,preCycle,postCycle)  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        cycle (Queryable[float]?): This flag is now obsolete. Use the postCycle flag instead.  
                Properties: create, query
        defaultAbsolute (bool?): Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.  
                Properties: query, edit
        enable (bool?): This flag is used to enable or disable a clip. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be enabled or disabled.  
                Properties: create, query
        group (bool?): This flag is used to add (true) or remove (false) a list of clips (specified with groupIndex) into a group.  
                Properties: create
        groupIndex (Multiuse[int]?): This flag specifies a multiple number of clips to be added or removed from a group.  
                Properties: create, multiuse
        groupName (Queryable[str]?): This flag is used to specify the group that should be added to.  If no group  
                by that name exists and new group is created with that name.  By default if  
                this is not specified a new group will be created.  
                Properties: create, query
        hold (Queryable[int]?): Specify how long to hold the last value of the clip after its normal or cycled end.  
                Properties: create, query
        insertTrack (int?): This flag is used to insert a new empty track at the track index  
                specified.  
                Properties: create
        instance (str?): Create an instanced copy of the named clip. An instanced clip is one that is linked to an original clip. Thus, changes to the animation curve of the original curve will also modify all instanced clips. The name of the instanced clip is returned  
                as a string.  
                Properties: create
        listCurves (bool?): This flag is used to list the animation curves associated with a clip. It should be used in conjunction with the clipIndex flag, which specifies the clip of interest.  
                Properties: create, query
        listPairs (bool?): This query only flag returns a string array containing the channels  
                in a character that are used by a clip and the names of the animation  
                curves that drive the channels. Each string in the string array consists  
                of the name of a channel, a space, and the name of the animation curve  
                animating that channel. This flag must be used with the ci/clipIndex flag.  
                Properties: query
        lock (bool?): This flag specifies whether clips on a track are to be locked or not.  
                Must be used in conjuction with the track flag.  
                Properties: query, edit
        mute (bool?): This flag specifies whether clips on a track are to be muted or not.  
                Must be used in conjuction with the track flag.  
                Properties: query, edit
        name (Queryable[str]?): This flag is used to query the name of the clip node associated with the specified clip index, or to specify the name of the instanced clip during instancing.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        postCycle (Queryable[float]?): Specify the number of times to repeat the clip after its normal end.  
                Properties: create, query
        preCycle (Queryable[float]?): Specify the number of times to repeat the clip before its normal start.  
                Properties: create, query
        remove (bool?): This flag is used to remove a clip from the timeline. It must be used in conjunction with the ci/clipIndex flag. The specified clip will be removed from the timeline, but will still exist in the library and any instanced clips will remain in the timeline. To permanently remove a clip from the scene, the clip command should be used instead.  
                Properties: create
        removeBlend (Tuple[int, int]?): This flag is used to remove an existing blend between two clips, whose indices are provided as flag arguments.  
                Properties: create
        removeEmptyTracks (bool?): This flag is used to remove all tracks that have no clips.  
                Properties: create
        removeTrack (int?): This flag is used to remove the track with the specified index.  The  
                track must have no clips on it before it can be removed.  
                Properties: create
        rotationsAbsolute (bool?): Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.  
                Properties: query, edit
        scale (Queryable[float]?): Specify the amount to scale the clip. Values must be greater than 0.  
                Properties: create, query
        shift (int?): This flag allows multiple clips to be shifted by a certain number of tracks  
                and works in conjunction with the shiftIndex flag.  The flag specifies the  
                number of tracks to shift the associated clips.  Positive values shift the  
                clips down an negative values shift the clips up.  
                Properties: create
        shiftIndex (Multiuse[int]?): This flag allows multiple clips to be shifted by a certain number of tracks  
                and works in conjunction with the shiftAmount flag.  The flag specifies the  
                index of the clip to shift.  This flag can be used multiple times on the command  
                line to specify a number of clips to shift.  
                Properties: create, multiuse
        solo (bool?): This flag specifies whether clips on a track are to be soloed or not.  
                Must be used in conjuction with the track flag.  
                Properties: query, edit
        sourceClipName (bool?): This flag is used to query the name of the source clip node associated with the specified clip index.  
                Properties: create, query
        sourceEnd (Queryable[int]?): Specify where to end in the source clip's animation curves  
                Properties: create, query
        sourceStart (Queryable[int]?): Specify where to start in the source clip's animation curves  
                Properties: create, query
        start (Queryable[int]?): Specify the placement of the start of the clip  
                Properties: create, query
        track (Queryable[int]?): Specify the track to operate on. For example, which track to place  
                a clip on, which track to mute/lock/solo.  In query mode, it may be used  
                in conjuction with the clipIndex flag to return the track number of a clip,  
                where track 1 is the first track of the character.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        weight (Queryable[float]?): This flag is used in to set or query the weight of the clip associated with the specified clip index.  
                Properties: create, query
        weightStyle (Queryable[int]?): This flag is used to set or query the weightStyle attribute of the clip associated with the specified clip index.  
                Properties: create, query

    Returns:
        str: Clip name

    Example:
    """

