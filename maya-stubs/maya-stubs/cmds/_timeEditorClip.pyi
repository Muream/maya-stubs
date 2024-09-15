from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorClip(*args: Any, edit: bool = ..., query: bool = ..., absolute: bool = ..., addAttribute: Multiuse[str] = ..., allowShrinking: bool = ..., animSource: Queryable[str] = ..., audio: str = ..., blendMode: Queryable[int] = ..., children: Queryable[int] = ..., clipAfter: bool = ..., clipBefore: bool = ..., clipDataType: bool = ..., clipId: Multiuse[int] = ..., clipIdFromNodeName: Queryable[int] = ..., clipIdFromPath: bool = ..., clipNode: bool = ..., clipPath: bool = ..., copyClip: bool = ..., crossfadeMode: Queryable[int] = ..., crossfadePlug: bool = ..., curveTime: Queryable[int] = ..., defaultGhostRoot: bool = ..., drivenAttributes: bool = ..., drivenClipsBySource: Queryable[str] = ..., drivenObjects: bool = ..., drivenRootObjects: bool = ..., drivingSources: Queryable[str] = ..., duplicateClip: bool = ..., duration: Queryable[int] = ..., emptySource: bool = ..., endTime: Queryable[int] = ..., existingOnly: bool = ..., exists: bool = ..., explode: int = ..., exportAllClips: bool = ..., exportFbx: str = ..., extend: bool = ..., extendParent: bool = ..., ghost: bool = ..., ghostRootAdd: Multiuse[str] = ..., ghostRootRemove: Multiuse[str] = ..., group: bool = ..., holdEnd: Queryable[int] = ..., holdStart: Queryable[int] = ..., importTakeDestination: int = ..., isContainer: bool = ..., listUserGhostRoot: bool = ..., loopEnd: Queryable[int] = ..., loopStart: Queryable[int] = ..., minClipDuration: bool = ..., modifyAnimSource: bool = ..., moveClip: int = ..., mute: bool = ..., name: Queryable[str] = ..., parent: int = ..., parentClipId: Queryable[int] = ..., parentGroupId: bool = ..., pasteClip: int = ..., path: Multiuse[str] = ..., preserveAnimationTiming: bool = ..., razorClip: int = ..., remap: Tuple[str, str] = ..., remapNamespace: Multiuse[Tuple[str, str]] = ..., remapSource: Tuple[str, str] = ..., remappedSourceAttrs: bool = ..., remappedTargetAttrs: bool = ..., removeAttribute: Multiuse[str] = ..., removeClip: bool = ..., removeCrossfade: bool = ..., removeWeightCurve: bool = ..., resetTiming: bool = ..., resetTransition: bool = ..., ripple: bool = ..., rootClipId: int = ..., rootPath: str = ..., scaleEnd: int = ..., scalePivot: int = ..., scaleStart: int = ..., setKeyframe: Multiuse[str] = ..., speedRamping: Queryable[int] = ..., startTime: Queryable[int] = ..., timeWarp: bool = ..., timeWarpCurve: bool = ..., timeWarpType: Queryable[int] = ..., track: Queryable[str] = ..., tracksNode: bool = ..., transition: bool = ..., trimEnd: int = ..., trimStart: int = ..., truncated: bool = ..., uniqueAnimSource: bool = ..., userGhostRoot: bool = ..., weightCurve: bool = ..., zeroKeying: bool = ..., addObjects: Queryable[str] = ..., addRelatedKG: bool = ..., addSelectedObjects: bool = ..., attribute: Multiuse[str] = ..., exclusive: bool = ..., importAllFbxTakes: bool = ..., importFbx: str = ..., importFbxTakes: str = ..., importMayaFile: str = ..., importOption: str = ..., importPopulateOption: str = ..., importedContainerNames: str = ..., includeRoot: bool = ..., populateImportedAnimSources: str = ..., poseClip: bool = ..., recursively: bool = ..., removeSceneAnimation: bool = ..., showAnimSourceRemapping: bool = ..., takeList: str = ..., takesToImport: str = ..., type: Queryable[Multiuse[str]] = ...) -> Union[str, bool, int, Multiuse[str]]:
    """This command edits/queries Time Editor clips.timeEditor, nle
    Args:
        absolute (bool?): This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc.  
                to query (global) absolute time.  
                Properties: query
        addAttribute (Multiuse[str]?): Add new attribute to the clip.  
                Properties: edit, multiuse
        allowShrinking (bool?): When extending clip, allow shrinking.  
                Properties: edit
        animSource (Queryable[str]?): Populate based on animation source.  
                Properties: create, query, edit
        audio (str?): Create a clip with audio inside.  
                Properties: create
        blendMode (Queryable[int]?): Set the blending mode for the clips specified with the -clipId flags:  
              
                0. normal          - absolute blend  
                1. additive        - relative blend  
                Properties: query, edit
        children (Queryable[int]?): Get children clip IDs.  
                Properties: query
        clipAfter (bool?): Get the clip ID of the next clip.  
                Properties: query
        clipBefore (bool?): Get the clip ID of the previous clip.  
                Properties: query
        clipDataType (bool?): Query the type of data being driven by the given clip ID.  
                Return values are:  
              
                0. Animation       - Clip drives animation curves  
                1. Audio           - Clip drives audio  
                3. Group           - Clip is a group  
                Properties: query
        clipId (Multiuse[int]?): ID of the clip to be edited.  
                Properties: create, edit, multiuse
        clipIdFromNodeName (Queryable[int]?): Get clip ID from clip node name.  
                Properties: query
        clipIdFromPath (bool?): Flag for querying the clip ID given the path. Clip path is a vertical-bar-delimited string to indicate  
                a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented.  
                For example: composition1|track1|clip1  
                Note: To specify the path, this flag must appear before -query flag.  
                Properties: query
        clipNode (bool?): Flag for querying the name of the clip node.  
                Properties: query
        clipPath (bool?): Flag for querying the path given the clip ID. Clip path is a vertical bar delimited string to indicate  
                a hierarchical structure of a clip. Please refer to the hierarchical path in outliner to see how it is represented.  
                For example: composition1|track1|clip1.  
                Note: If the clip is not connected to any track, it will return empty string.  
                Properties: query
        copyClip (bool?): Get the selected clip IDs and store them in a list that could be used for pasting.  
                Properties: edit
        crossfadeMode (Queryable[int]?): Set the crossfading mode between two clips that lie on the same track, and that are specified with the -clipId flags:  
              
                0. linear          - Two clips are blended with a constant ratio  
                1. step            - Left clip keeps its value until the middle of the crossfading region and then right clip's value is used  
                2. hold left       - Use only left clip's value  
                3. hold right      - Use only right clip's value  
                4. custom          - User defined crossfade curve  
                5. custom (spline) - User defined crossfade curve with spline preset  
                Properties: query, edit
        crossfadePlug (bool?): Get plug path for a custom crossfade curve between 2 clips.  
                Properties: query
        curveTime (Queryable[int]?): Query the curve local time in relation to the given clip.  
                Properties: query
        defaultGhostRoot (bool?): Edit or query default ghost root variable.  
                Determine whether to use the default ghost root (object driven by clip).  
                Properties: query, edit
        drivenAttributes (bool?): Return a list of attributes driven by a clip.  
                Properties: query
        drivenClipsBySource (Queryable[str]?): Returns the clips driven by the given source. Can filter the return result by the specified type, like animCurve, expression, constraint, etc.  
                This flag must come before the -query flag.  
                Properties: query
        drivenObjects (bool?): Return an array of strings consisting of the names of all objects driven by the current clip and its children clips.  
                Properties: query
        drivenRootObjects (bool?): Return an array of strings consisting of the names of all root objects driven by this clip and its children clips.  
                Properties: query
        drivingSources (Queryable[str]?): Return all sources driving the given clip. Can filter the return result by the specified type, like animCurve, expression, constraint, etc.  
                If used after the -query flag (without an argument), the command returns all sources driving the given clip.  
                To specify the type, this flag must appear before the -query flag.  
                			In query mode, this flag can accept a value.  
                Properties: query
        duplicateClip (bool?): Duplicate clip into two clips with the same timing info.  
                Properties: edit
        duration (Queryable[int]?): Relative duration of the new clip.  
                Properties: create, query
        emptySource (bool?): Create a clip with an empty source.  
                Properties: create
        endTime (Queryable[int]?): Query the relative end time of the clip.  
                Properties: query
        existingOnly (bool?): This flag can only be used in edit mode, in conjunction with the animSource flag. Retain the animSource flag functionality but  
                only bind attributes that are already part of the clip. It does not attempt to populate unbound  
                source attributes to their default destination.  
                Properties: edit
        exists (bool?): Return true if the specified clip exists.  
                Properties: query
        explode (int?): Reparent all tracks and their clips within a group out to its parent track node and remove the group.  
                Properties: edit
        exportAllClips (bool?): When used with the ef/exportFbx flag, export all clips.  
                Properties: edit
        exportFbx (str?): Export currently selected clips to FBX files.  
                Properties: edit
        extend (bool?): Extend the clip to encompass all children.  
                Properties: edit
        extendParent (bool?): Extend parent to fit this clip.  
                Properties: edit
        ghost (bool?): Enable/disable ghosting for the specified clip.  
                Properties: query, edit
        ghostRootAdd (Multiuse[str]?): Add path to specified node as a custom ghost root.  
                Properties: edit, multiuse
        ghostRootRemove (Multiuse[str]?): Remove path to specified node as a custom ghost root.  
                Properties: edit, multiuse
        group (bool?): Specify if the new container should be created as a group, containing other specified clips.  
                Properties: create
        holdEnd (Queryable[int]?): Hold clip's end to time.  
                Properties: query, edit
        holdStart (Queryable[int]?): Hold clip's start to time.  
                Properties: query, edit
        importTakeDestination (int?): Specify how to organize imported FBX takes:  
                0. Import takes into a group (default)  
                1. Import takes into multiple compositions  
                2. Import takes as a sequence of clips  
                Properties: create
        isContainer (bool?): Indicate if given clip ID is a container.  
                Properties: query
        listUserGhostRoot (bool?): Get user defined ghost root object for indicated clips.  
                Properties: query
        loopEnd (Queryable[int]?): Loop clip's end to time.  
                Properties: query, edit
        loopStart (Queryable[int]?): Loop clip's start to time.  
                Properties: query, edit
        minClipDuration (bool?): Returns the minimum allowed clip duration.  
                Properties: query
        modifyAnimSource (bool?): When populating, automatically modify Anim Source without asking the user.  
                Properties: create, edit
        moveClip (int?): Move clip by adding delta to its start time.  
                Properties: edit
        mute (bool?): Mute/Unmute the clip given a clip ID. In query mode, return the muted state of the clip. Clips muted by soloing are not affected by this flag.  
                Properties: query, edit
        name (Queryable[str]?): Name of the clip. A clip will never have an empty name.  
                If an empty string is provided, it will be replaced with "_".  
                Properties: query, edit
        parent (int?): Specify group/object parent ID.  
                Properties: edit
        parentClipId (Queryable[int]?): Specify the parent clip ID of a clip to be created.  
                Properties: create, query
        parentGroupId (bool?): Return the parent group ID of the given clip.  
                Properties: query
        pasteClip (int?): Paste clip to the given time and track. Destination track is required to be specified through the track flag in the format "tracksNode:trackIndex".  
                A trackIndex of -1 indicates that a new track will be created.  
                Properties: edit
        path (Multiuse[str]?): Full path of the clip to be edited. For example: composition1|track1|clip1.  
                			In query mode, this flag can accept a value.  
                Properties: edit, multiuse
        preserveAnimationTiming (bool?): When used with the population command, it ensures the animation is offset within a clip in such way that it matches its original scene timing, regardless of the new clip's position.  
                Properties: create
        razorClip (int?): Razor clip into two clips at the specified time.  
                Properties: edit
        remap (Tuple[str, str]?): Change animation source for a given clip item to a new one, specified by the target path.  
                This removes all clips for the roster item and creates new clips from the Anim Source for the new target path.  
                Properties: edit
        remapNamespace (Multiuse[Tuple[str, str]]?): Remap namespace(s). Can only be used in create mode, in conjunction with the  
                -importFbx/fbx, -importMayaFile/mf, or -attribute/at flags.  
                This flag will replace any occurrences of a given namespace to  
                an alternate specified namespace.  It takes in two string arguments. The  
                first argument specifies the namespace to replace. The second argument  
                specifies the replacement namespace. This flag cannot be used in conjunction  
                with the -sar/showAnimSourceRemapping flag.  
                Note that a track must be specified, and  must exist prior to invoking the  
                timeEditorClip command with the -remapNamespace flag.  
                Properties: create, multiuse
        remapSource (Tuple[str, str]?): Set animation source to be remapped for a given clip item to new one, specified by the target path.  
                Properties: edit
        remappedSourceAttrs (bool?): Return an array of attribute indices and names of the source attributes of a remapped clip.  
                Properties: query
        remappedTargetAttrs (bool?): Return an array of attribute indices and names of the target attributes of a remapped clip.  
                Properties: query
        removeAttribute (Multiuse[str]?): Remove attribute from the clip.  
                Properties: edit, multiuse
        removeClip (bool?): Remove clip of specified ID.  
                Properties: edit
        removeCrossfade (bool?): Remove custom crossfade between two clips specified by -clipId flags.  
                Properties: edit
        removeWeightCurve (bool?): Remove the weight curve connected to the clip.  
                Properties: create, query, edit
        resetTiming (bool?): Reset start and duration of a clip with the given clip ID to the values stored in its Anim Source.  
                Properties: edit
        resetTransition (bool?): Reset transition intervals between specified clips.  
                Properties: edit
        ripple (bool?): Apply rippling to a clip operation.  
                Properties: edit
        rootClipId (int?): ID of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip.  
                For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.  
                Properties: edit
        rootPath (str?): Path of the root clip. It is used together with various clip editing flags. When used, the effect of clip editing and its parameters will be affected by the given root clip.  
                For example, moving a clip under the group root (usually in group tab view) will be performed in the local time space of the group root.  
                Properties: edit
        scaleEnd (int?): Scale the end time of the clip to the given time.  
                Properties: edit
        scalePivot (int?): Scale the time of the clip based on the pivot. This should be used together with -scs/scaleStart or -sce/scaleEnd.  
                Properties: edit
        scaleStart (int?): Scale the start time of the clip to the given time.  
                Properties: edit
        setKeyframe (Multiuse[str]?): Set keyframe on a specific clip for a specified attribute.  
                Properties: edit, multiuse
        speedRamping (Queryable[int]?): To control the playback speed of the clip by animation curve:  
              
                1. create - Attach a speed curve and a time warp curve to the clip to control the playback speed  
                2. edit - Open the Graph editor to edit the speed curve  
                3. enable - Create a time warp curve from current speed curve and attach to clip  
                4. disable - Remove the time warp curve from clip  
                5. delete - Delete the attached speed curve and time warp curve  
                6. reset - Reset the speed curve back to the default  
                7. convert to speed curve from time warp  
                8. convert to time warp from speed curve  
              
                In query mode, return true if a speed curve is attached to the clip.  
                Properties: query, edit
        startTime (Queryable[int]?): Relative start time of the new clip.  
                Properties: create, query
        timeWarp (bool?): Return true if the clip is being warped by the speed curve. If no speed curve is attached to the clip, it will always return false.  
                Properties: query
        timeWarpCurve (bool?): Returns the name of the time warp curve connected to the clip.  
                Properties: query
        timeWarpType (Queryable[int]?): Time warp mode:  
              
                0. remapping - Connected time warp curve performs frame by frame remapping  
                1. speed curve - Connected time warp curve acts as a speed curve  
              
                In query mode, return time warp mode of a clip.  
                Properties: query, edit
        track (Queryable[str]?): The new clip container will be created on the track in the format "trackNode:trackNumber", or on a track path, for example "composition1|track1".  
                In query mode, return a string containing the track number and tracks node of the given clip ID.  
                In create mode, if the track number is '-1' or not given at all, then a new track will be created. For example: "trackNode:-1"; "composition1|".  
                Properties: create, query, edit
        tracksNode (bool?): Get tracks node if specified clip is a group clip.  
                Properties: query
        transition (bool?): Create transition intervals between specified clips.  
                Properties: edit
        trimEnd (int?): Trim the end time of the clip to the given time.  
                Properties: edit
        trimStart (int?): Trim the start time of the clip to the given time.  
                Properties: edit
        truncated (bool?): This flag is used in conjunction with other timing flags like -s/start, -d/duration, -ed/end, etc.  
                to query (global) truncated time.  
                Properties: query
        uniqueAnimSource (bool?): If a given clip is sharing its Anim Source node with another clip, make the Anim Source of this clip unique.  
                Properties: edit
        userGhostRoot (bool?): Edit or query custom ghost root variable.  
                Determine whether to use user defined ghost root.  
                Properties: query, edit
        weightCurve (bool?): In edit mode, create a weight curve and connect it to the clip.  
                In query mode, return the name of the weight curve connected to the clip.  
                Properties: create, query, edit
        zeroKeying (bool?): A toggle flag to use in conjunction with k/setKeyframe, set the value of the key frame(s) to be keyed to zero.  
                Properties: edit
        addObjects (Queryable[str]?): Populate the given object(s) and their attributes to anim source to Time Editor. For multiple object, pass each name separated by semicolon.  
                In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames for the given object(s).  
                Similar to -addSelectedObjects flag but acts on given object(s) instead.  
                This flag will override the flag -addSelectedObjects.  
                Properties: create, query, edit
        addRelatedKG (bool?): During population, determine if associated keying groups should be populated  
                or not. Normally used for populating HIK. By default the value is false.  
                Properties: create, query, edit
        addSelectedObjects (bool?): Populate the currently selected objects and their attributes to anim source or Time Editor.  
                In query mode, return the number of attributes that will be populated given the flags, along with the animation's first and last frames.  
                Properties: create, query, edit
        attribute (Multiuse[str]?): Populate a specific attribute on a object.  
                Properties: create, edit, multiuse
        exclusive (bool?): Populate all types of animation sources which are not listed by "type" Flag.  
                Properties: create, edit
        importAllFbxTakes (bool?): Import all FBX takes into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).  
                Properties: create
        importFbx (str?): Import an animation from FBX file into the new anim source (for timeEditorAnimSource command) or new container (for timeEditorClip command).  
                Properties: create
        importFbxTakes (str?): Import multiple FBX takes (separated by semicolons) into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).  
                Properties: create
        importMayaFile (str?): Import an animation from Maya file into the new anim sources (for timeEditorAnimSource command) or new containers (for timeEditorClip command).  
                Properties: create
        importOption (str?): Option for importing animation source. Specify either 'connect' or 'generate'.  
                connect:  Only connect with nodes already existing in the scene.  
                                  Importing an animation source that does not match with any element  
                                  of the current scene will not create any clip.  
                                  (connect is the default mode).  
                generate: Import everything and generate new nodes for items not existing in the scene.  
                Properties: edit
        importPopulateOption (str?): Option for population when importing.  
                Properties: edit
        importedContainerNames (str?): Internal use only. To be used along with populateImportedAnimSources to specify names for the created containers.  
                Properties: create
        includeRoot (bool?): Populate transform (Translate, Rotate, Scale) of hierarchy root nodes.  
                Properties: create, edit
        populateImportedAnimSources (str?): Internal use only. Populate the Time Editor with clips using the Animation Sources specified (use ; as a delimiter for multiple anim sources).  
                Properties: create
        poseClip (bool?): Populate as pose clip with current attribute values.  
                Properties: create
        recursively (bool?): Populate selection recursively, adding all the children.  
                Properties: create, edit
        removeSceneAnimation (bool?): If true, remove animation from scene when creating clips or anim sources. Only Time Editor will drive the removed scene animation.  
                Properties: create, edit
        showAnimSourceRemapping (bool?): Show a remapping dialog when the imported anim source attributes do not match the scene attributes.  
                Properties: create
        takeList (str?): Internal use only. To be used along with populateImportedAnimSources to specify the imported take names.  
                Properties: create
        takesToImport (str?): Internal use only. To be used along with populateImportedAnimSources to specify the imported take indices.  
                Properties: create
        type (Queryable[Multiuse[str]]?): Only populate the specified type of animation source.  
                Properties: create, query, edit, multiuse

    Returns:
        str: Return created clip's name.

    Example:
    """

