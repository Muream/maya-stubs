from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorAnimSource(*args: Any, edit: bool = ..., query: bool = ..., addSource: str = ..., apply: bool = ..., bakeToAnimSource: str = ..., calculateTiming: bool = ..., copyAnimation: bool = ..., drivenClips: bool = ..., export: str = ..., isUnique: bool = ..., removeSource: str = ..., targetIndex: Queryable[str] = ..., targets: bool = ..., addObjects: Queryable[str] = ..., addRelatedKG: bool = ..., addSelectedObjects: bool = ..., attribute: Multiuse[str] = ..., exclusive: bool = ..., importAllFbxTakes: bool = ..., importFbx: str = ..., importFbxTakes: str = ..., importMayaFile: str = ..., importOption: str = ..., importPopulateOption: str = ..., importedContainerNames: str = ..., includeRoot: bool = ..., populateImportedAnimSources: str = ..., poseClip: bool = ..., recursively: bool = ..., removeSceneAnimation: bool = ..., showAnimSourceRemapping: bool = ..., takeList: str = ..., takesToImport: str = ..., type: Queryable[Multiuse[str]] = ...) -> Union[str, bool, Multiuse[str]]:
    """Commands for managing animation sources.timeEditor, nle
    Args:
        addSource (str?): Add single new target attribute with its animation.  
                Properties: edit
        apply (bool?): Connect anim source's animation directly to the target objects. If the Time Editor is not muted, connect to scene storage instead.  
                Properties: edit
        bakeToAnimSource (str?): Create a new anim source with the same animation as this anim source. All non-curve inputs will be baked down, whereas curve sources will be shared.  
                Properties: edit
        calculateTiming (bool?): Adjust start/duration when adding/removing sources. If query it returns the [start,duration] pair.  
                Properties: query, edit
        copyAnimation (bool?): Copy animation when adding source.  
                Properties: edit
        drivenClips (bool?): Return all clips driven by the given anim source.  
                Properties: query
        export (str?): Export given anim source and the animation curves to a specified Maya file.  
                Properties: edit
        isUnique (bool?): Return true if the anim source node is only driving a single clip.  
                Properties: query
        removeSource (str?): Remove single attribute.  
                Properties: edit
        targetIndex (Queryable[str]?): Get target index.  
                Properties: query
        targets (bool?): Get a list of all targets in this anim source.  
                Properties: query
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
        str: Command result

    Example:
    """

