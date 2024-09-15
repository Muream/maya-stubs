from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cameraSet(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., active: bool = ..., appendTo: bool = ..., camera: Queryable[str] = ..., clearDepth: bool = ..., deleteAll: bool = ..., deleteLayer: bool = ..., insertAt: bool = ..., layer: Queryable[int] = ..., name: Queryable[str] = ..., numLayers: bool = ..., objectSet: Queryable[str] = ..., order: Queryable[int] = ...) -> Union[str, bool, int]:
    """This command manages camera set nodes. Camera sets allow the users to
    break a single camera shot into layers. Instead of drawing all objects
    with a single camera, you can isolate the camera to only focus on
    certain objects and layer another camera into the viewport that draws
    the other objects. The situation to use camera sets primarily occurs
    when building stereoscopic scenes.For example, a set of stereo parameters may make the background
    objects divergent beyond the tolerable range of the human perceptual
    system. However, you like the settings because the main focus is in
    the foreground and the depth is important to the visual look of the
    scene.  You can use camera sets to break apart the shot into a
    foreground stereo camera and background stereo camera. The foreground
    stereo camera will retain the original parameters; however, it will
    only focus on the foreground elements.  The background stereo camera
    will have a different set of stereo parameters and will only draw the
    background element.Camera sets can be viewed using the stereo viewer and are currently only
    designed to work with stereo camera rigs.
    Args:
        active (bool?): Gets / sets the active camera layer.  
                Properties: create, query, edit
        appendTo (bool?): Append a new camera and/or object set to then end of the cameraSet layer  
                list. This flag cannot be used in conjunction with insert flag. Additionally,  
                it requires the camera and/or objectSet flag to be used.  
                Properties: create, edit
        camera (Queryable[str]?): Set/get the camera for a particular layer. When in query mode, You  
                must specify the layer with the layer flag.  
                Properties: create, query, edit
        clearDepth (bool?): Specifies if the drawing buffer should be cleared before beginning the draw  
                for that layer.  
                Properties: create, query, edit
        deleteAll (bool?): Delete all camera layers  
                Properties: create, edit
        deleteLayer (bool?): Delete a layer from the camera set. You must specify the layer using the  
                layer flag.  
                Properties: create, edit
        insertAt (bool?): Inserts the specified camera and/or object set at the specified layer.  
                This flag cannot be used in conjunction with the append flag. Additionally,  
                this flag requires layer and camera (or objectSet) flag to be used.  
                Properties: create, edit
        layer (Queryable[int]?): Specifies the layer index to be used when accessing layer information  
                Properties: create, query, edit
        name (Queryable[str]?): Gets or sets the name for the created camera set.  
                Properties: create, query
        numLayers (bool?): Returns the number of layers defined in the specified cameraSet  
                Properties: create, query
        objectSet (Queryable[str]?): Set/get the objectSet for a particular layer. When in query mode, you must  
                specify the layer with the layer flag.  
                Properties: create, query, edit
        order (Queryable[int]?): Set the order in which a particular layer is processed. This flag must be  
                used in conjunction with the layer flag.  
                Properties: create, query, edit

    Returns:
        str: The new cameraSet node (when in create mode)

    Example:
    """

