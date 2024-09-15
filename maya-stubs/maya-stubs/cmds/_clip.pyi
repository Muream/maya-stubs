from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def clip(*args: str, edit: bool = ..., query: bool = ..., absolute: bool = ..., absoluteRotations: bool = ..., active: Queryable[str] = ..., addTrack: bool = ..., allAbsolute: bool = ..., allClips: bool = ..., allRelative: bool = ..., allSourceClips: bool = ..., animCurveRange: bool = ..., character: bool = ..., constraint: bool = ..., copy: bool = ..., defaultAbsolute: bool = ..., duplicate: bool = ..., endTime: Queryable[int] = ..., expression: bool = ..., ignoreSubcharacters: bool = ..., isolate: bool = ..., leaveOriginal: bool = ..., mapMethod: str = ..., name: Queryable[Multiuse[str]] = ..., newName: str = ..., paste: bool = ..., pasteInstance: bool = ..., remove: bool = ..., removeTrack: bool = ..., rotationOffset: Queryable[Tuple[float, float, float]] = ..., rotationsAbsolute: bool = ..., scheduleClip: bool = ..., sourceClipName: bool = ..., split: int = ..., startTime: Queryable[int] = ..., translationOffset: Queryable[Tuple[float, float, float]] = ..., useChannel: Multiuse[str] = ...) -> Union[List[str], str, bool, int, Multiuse[str], Tuple[float, float, float]]:
    """This command is used to create, edit and query character clips.character, clip, animation
    Args:
        absolute (bool?): This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead.  This flag controls whether the clip follows its keyframe values or whether they are offset by a value to maintain a smooth path. Default is true.  
                Properties: create
        absoluteRotations (bool?): This flag is now deprecated.  Use aa/allAbsolute, ar/allRelative, ra/rotationsAbsolute, or da/defaultAbsolute instead. If true, this overrides the -absolute flag so that rotation channels are always calculated with absolute offsets. This allows you to have absolute offsets on rotations and relative offsets on all other channels.  
                Properties: create
        active (Queryable[str]?): Query or edit the active clip. This flag is not valid in create mode. Making a  
                clip active causes its animCurves to be hooked directly to the character attributes in addition to being attached to the clip library node. This makes it easier to access the animCurves if you want to edit, delete or add additional animCruves to the clip.  
                Properties: query, edit
        addTrack (bool?): This flag is now obsolete. Use the insertTrack flag on the clipSchedule command instead.
        allAbsolute (bool?): Set all channels to be calculated with absolute offsets.  This flag cannot be used in conjunction with the ar/allRelative, ra/rotationsAbsolute or da/defaultAbsolute flags.  
                Properties: create
        allClips (bool?): This flag is used to query all the clips in the scene. Nodes of type "animClip" that are storing poses, are not returned by this command.  
                Properties: query
        allRelative (bool?): Set all channels to be calculated with relative offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ra/rotationsAbsolute or da/defaultAbsolute flags.  
                Properties: create
        allSourceClips (bool?): This flag is used to query all the source clips in the scene. Nodes of type "animClip" that are storing poses or clip instances, are not returned by this command.  
                Properties: query
        animCurveRange (bool?): This flag can be used at the time you create the clip instead of the startTime and endTime flags. It specifies that you want the range of the clip to span the range of keys in the clips associated animCurves.  
                Properties: create
        character (bool?): This is a query only flag which operates on the specified clip. It returns the names of any characters that a clip is associated with.  
                Properties: query
        constraint (bool?): This creates a clip out of any constraints on the character. The constraint will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.  
                Properties: create
        copy (bool?): This flag is used to copy a clip or clips to the clipboard. It should be used in conjunction with the name flag to copy the named clips on the specified character and its subcharacters. In query mode, this flag allows you to query what, if anything, has been copied into the clip clipboard.  
                Properties: create, query
        defaultAbsolute (bool?): Sets all top-level channels except rotations in the clip to relative, and the remaining channels to absolute. This is the default during clip creation if no offset flag is specified.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative, or ra/rotationsAbsolute flags.  
                Properties: create
        duplicate (bool?): Duplicate the clip specified by the name flag. The start time of the new clip should be specified with the startTime flag.  
                Properties: query
        endTime (Queryable[int]?): Specify the clip end  
                Properties: create, query, edit
        expression (bool?): This creates a clip out of any expressions on the character. The expression will be moved off of the character and into the clip, so that it is only active for the duration of the clip, and its value can be scaled/offset/cycled according to the clip attributes.  
                Properties: create
        ignoreSubcharacters (bool?): During clip creation, duplication and isolation, subcharacters are included by default. If you want to create a clip on the top level character only, or you want to duplicate the clip on the top level character without including subCharacters, use the ignoreSubcharacters flag.  
                Properties: create
        isolate (bool?): This flag should be used in conjunction with the name flag to specify that a clip or clips should be copied to a new clip library. The most common use of this flag is for export, when you want to only export certain clips from the character, without exporting all of the clips.  
                Properties: create
        leaveOriginal (bool?): This flag is used when creating a clip to specify that the animation curves should be copied to the clip library, and left on the character.  
                Properties: create
        mapMethod (str?): This is is valid with the paste and pasteInstance flags only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", "byCharacterMap", "byAttrOrder", "byMapOrAttrName" and "byMapOrNodeName". "byAttrName" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence, "byCharacterMap" uses the existing characterMap node to do the mapping. "byMapOrAttrName" uses a character map if one exists, otherwise uses the attribute name. "byMapOrNodeName" uses a character map if one exists, otherwise uses the attribute name.  
                Properties: create
        name (Queryable[Multiuse[str]]?): In create mode, specify the clip name. In query mode, return a list of all the clips. In duplicate mode, specify the clip to be duplicated. In copy mode, specify the clip to be copied. This flag is multi-use, but multiple use is only supported with the copy flag. For use during create and with all other flags, only the first instance of the name flag will be utilized.  
                			In query mode, this flag can accept a value.  
                Properties: create, query, multiuse
        newName (str?): Rename a clip. Must be used in conjunction with the clip name flag, which is used to specify the clip to be renamed.  
                Properties: create
        paste (bool?): This flag is used to paste a clip or clips from the clipboard to a character. Clips are added to the clipboard using the c/copy flag.  
                Properties: create
        pasteInstance (bool?): This flag is used to paste an instance of a clip or clips from the clipboard to a character. Unlike the p/paste flag, which duplicates the animCurves from the original source clip, the pi/pasteInstance flag shares the animCurves from the source clip.  
                Properties: create
        remove (bool?): Remove the clip specified by the name flag. The clip will be  
                permanently removed from the library and deleted from any times  
                where it has been scheduled.  
                Properties: query
        removeTrack (bool?): This flag is now obsolete. Use removeTrack flag on the clipSchedule command instead.  
                Properties: create
        rotationOffset (Queryable[Tuple[float, float, float]]?): Return the channel offsets used to modify the clip's rotation.  
                Properties: create, query
        rotationsAbsolute (bool?): Set all channels except rotations to be calculated with relative offsets.  Rotation channels will be calculated with absolute offsets.  This flag cannot be used in conjunction with the aa/allAbsolute, ar/allRelative or da/defaultAbsolute flags.  
                Properties: create
        scheduleClip (bool?): This flag is used when creating a clip to specify whether or not the clip should immediately be scheduled at the current time. If the clip is not scheduled, the clip will be placed in the library for future use, but will not be placed on the timeline. This flag is for use only when creating a new clip or duplicating an existing. The default is true.  
                Properties: create
        sourceClipName (bool?): This flag is for query only. It returns the name of the source clip that controls an instanced clip.  
                Properties: query
        split (int?): Split an existing clip into two clips. The split occurs around the specified time.  
                Properties: create, edit
        startTime (Queryable[int]?): Specify the clip start  
                Properties: create, query, edit
        translationOffset (Queryable[Tuple[float, float, float]]?): Return the channel offsets used to modify the clip's translation.  
                Properties: create, query
        useChannel (Multiuse[str]?): Specify which channels should be acted on. This flag is valid only in  
                conjunction with clip creation, and the isolate flag. The specified channels  
                must be members of the character.  
                Properties: create, multiuse

    Returns:
        List[str]: clip names

    Example:
    """

