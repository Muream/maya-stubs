from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sculptMeshCacheCtx(*args: Any, edit: bool = ..., query: bool = ..., adjustSize: bool = ..., adjustStrength: bool = ..., affectAllLayers: bool = ..., brushDirection: Queryable[int] = ..., brushSize: Queryable[float] = ..., brushStrength: Queryable[float] = ..., buildUpRate: Queryable[float] = ..., cloneHideSource: bool = ..., cloneMethod: Queryable[int] = ..., cloneShapeSource: Queryable[str] = ..., cloneTargetSource: Queryable[str] = ..., constrainToSurface: bool = ..., direction: Queryable[int] = ..., displayFrozen: bool = ..., displayMask: bool = ..., displayWireframe: bool = ..., falloffType: Queryable[int] = ..., flood: float = ..., floodFreeze: float = ..., frame: bool = ..., freezeSelection: bool = ..., grabFollowPath: bool = ..., grabSilhouette: bool = ..., grabTwist: bool = ..., inverted: bool = ..., lastMode: Queryable[str] = ..., lockShellBorder: bool = ..., makeStroke: Multiuse[Tuple[int, int, int, float, float]] = ..., minSize: Queryable[float] = ..., minStrength: Queryable[float] = ..., mirror: Queryable[int] = ..., mode: Queryable[str] = ..., orientToSurface: bool = ..., recordStroke: bool = ..., sculptFalloffCurve: Queryable[str] = ..., size: Queryable[float] = ..., stampDistance: Queryable[float] = ..., stampFile: Queryable[str] = ..., stampFlipX: bool = ..., stampFlipY: bool = ..., stampOrientToStroke: bool = ..., stampPlacement: Queryable[int] = ..., stampRandomization: bool = ..., stampRandomizationSeed: int = ..., stampRandomizeFlipX: bool = ..., stampRandomizeFlipY: bool = ..., stampRandomizePosX: Queryable[float] = ..., stampRandomizePosY: Queryable[float] = ..., stampRandomizeRotation: Queryable[float] = ..., stampRandomizeScale: Queryable[float] = ..., stampRandomizeStrength: Queryable[float] = ..., stampRotation: Queryable[float] = ..., steadyStrokeDistance: Queryable[float] = ..., strength: Queryable[float] = ..., updatePlane: bool = ..., useGlobalSize: bool = ..., useScreenSpace: bool = ..., useStampDistance: bool = ..., useStampImage: bool = ..., useSteadyStroke: bool = ..., wholeStroke: bool = ..., wireframeAlpha: Queryable[float] = ..., wireframeColor: Queryable[Tuple[float, float, float]] = ...) -> Union[bool, int, float, str, Tuple[float, float, float]]:
    """This is a tool context command for mesh cache sculpting tool.
    Args:
        adjustSize (bool?): If true, puts the tool into the mode where dragging the mouse will edit the brush size.  
                If false, puts the tool back into the previous sculpt mode.  
                Properties: edit
        adjustStrength (bool?): If true, puts the tool into the mode where dragging the mouse will edit the brush strength.  
                If false, puts the tool back into the previous sculpt mode.  
                Properties: edit
        affectAllLayers (bool?): If true, the brush affects all layers at once.  
                Properties: create, query, edit
        brushDirection (Queryable[int]?): Specifies the direction of the named brush.  
                Properties: query, edit
        brushSize (Queryable[float]?): Specifies the world-space size of the named brush.  
                Properties: query, edit
        brushStrength (Queryable[float]?): Specifies the world-space strength of the named brush.  
                Properties: query, edit
        buildUpRate (Queryable[float]?): Specifies the brush strength increasing along the stroke.  
                Properties: query, edit
        cloneHideSource (bool?): True if the cloned source should be hidden.  
                Properties: create, query, edit
        cloneMethod (Queryable[int]?): Controls how the source delta vectors should change the target. 0=copy 1=add  
                Properties: create, query, edit
        cloneShapeSource (Queryable[str]?): Name of the shape source to clone.  
                Properties: create, query, edit
        cloneTargetSource (Queryable[str]?): Name of the target source of the clone.  
                Properties: create, query, edit
        constrainToSurface (bool?): If true, the modification keeps the surface curvature.  
                Properties: create, query, edit
        direction (Queryable[int]?): Specifies the direction in which the vertices are moved.  
                Properties: query, edit
        displayFrozen (bool?): If false, turns off the display of frozen area on the object.  
                Properties: create, query, edit
        displayMask (bool?): If false, turns off the display of masked area on the object.  
                Properties: create, query, edit
        displayWireframe (bool?): If false, turns off the wireframe display of the object.  
                Properties: create, query, edit
        falloffType (Queryable[int]?): Specifies how the brush determines which vertices to affect.  
                Properties: query, edit
        flood (float?): Sets the brush effect for each vertex to the given value.  
                Properties: create, edit
        floodFreeze (float?): Sets the freeze value for each vertex to the given value.  
                Properties: create, edit
        frame (bool?): Frames on the sculpted area.  
                Properties: create, edit
        freezeSelection (bool?): Freezes selected components.  
                Properties: create, edit
        grabFollowPath (bool?): If true, the grab brush effect follows mouse movement.  
                Properties: create, query, edit
        grabSilhouette (bool?): If true, the grab brush uses paint-through mode.  
                Properties: create, query, edit
        grabTwist (bool?): If true, the grab brush twists the vertices.  
                Properties: create, query, edit
        inverted (bool?): If true, inverts the effect of the brush.  
                Properties: create, query, edit
        lastMode (Queryable[str]?): Specifies the type of the last active sculpting brush.  
                Properties: query, edit
        lockShellBorder (bool?): Lock the shell borders so that they won't be moved by a UV texture brush.  
                Properties: create, query, edit
        makeStroke (Multiuse[Tuple[int, int, int, float, float]]?): Specify a surface point patch for a brush stroke. Multiple patches can be specified to form a brush stroke.  
                The first argument is the mesh index.  
                The second argument is the side index. use 0 for the original side, and 1 for the mirrored side  
                The third argument is the face index within the specified mesh.  
                The fourth and fifth arguments are the face coordinates within the specified face.  
                Properties: edit, multiuse
        minSize (Queryable[float]?): Specifies the minimum size percentage of the current brush.  
                Properties: query, edit
        minStrength (Queryable[float]?): Specifies the minimum strength percentage of the current brush.  
                Properties: query, edit
        mirror (Queryable[int]?): Specifies the mirror mode of the brush.  
                Properties: query, edit
        mode (Queryable[str]?): Specifies the type of sculpting effect the brush will perform.  
                Properties: query, edit
        orientToSurface (bool?): If true, aligns the brush display to the surface of the mesh.  
                Properties: create, query, edit
        recordStroke (bool?): Set this flag to true to enable stroke recording that can be later played back with the makeStroke flag.  
                Properties: query, edit
        sculptFalloffCurve (Queryable[str]?): Specifies the falloff curve of sculpting effect the brush will perform.  
                Properties: query, edit
        size (Queryable[float]?): Specifies the world-space size of the current brush.  
                Properties: query, edit
        stampDistance (Queryable[float]?): Specifies the stamping distance of the brush.  
                Properties: query, edit
        stampFile (Queryable[str]?): Specifies an image file to use as stamp.  
                Properties: query, edit
        stampFlipX (bool?): Specifies if the brush stamp is flipped on the X axis.  
                Properties: create, query, edit
        stampFlipY (bool?): Specifies if the brush stamp is flipped on the Y axis.  
                Properties: create, query, edit
        stampOrientToStroke (bool?): Specifies if the brush stamp is aligned to the stroke direction.  
                Properties: create, query, edit
        stampPlacement (Queryable[int]?): Specifies the placement mode of the stamp image.  
                Properties: query, edit
        stampRandomization (bool?): Specifies if the brush stamp is randomized.  
                Properties: create, query, edit
        stampRandomizationSeed (int?): Specifies the stamp randomization seed value. Use a value of 0 to generate a random seed value.  
                Properties: edit
        stampRandomizeFlipX (bool?): Specifies if the brush stamp flipping is randomized on the X axis.  
                Properties: create, query, edit
        stampRandomizeFlipY (bool?): Specifies if the brush stamp flipping is randomized on the Y axis.  
                Properties: create, query, edit
        stampRandomizePosX (Queryable[float]?): Specifies the stamp X position value is randomized.  
                Properties: query, edit
        stampRandomizePosY (Queryable[float]?): Specifies the stamp Y position value is randomized.  
                Properties: query, edit
        stampRandomizeRotation (Queryable[float]?): Specifies the stamp rotation value is randomized.  
                Properties: query, edit
        stampRandomizeScale (Queryable[float]?): Specifies the stamp scale value is randomized.  
                Properties: query, edit
        stampRandomizeStrength (Queryable[float]?): Specifies the stamp strength value is randomized.  
                Properties: query, edit
        stampRotation (Queryable[float]?): Specifies the rotation value of the stamp image.  
                Properties: query, edit
        steadyStrokeDistance (Queryable[float]?): Specifies the distance for the steady stroke.  
                Properties: query, edit
        strength (Queryable[float]?): Specifies the world-space strength of the current brush.  
                Properties: query, edit
        updatePlane (bool?): Recalculates the underlying tool plane for each stamp in a stroke.  
                Properties: create, query, edit
        useGlobalSize (bool?): If true, all the brushes have a shared size property; otherwise size is local.  
                Properties: create, query, edit
        useScreenSpace (bool?): If true, the brush size is in screen space pixels.  
                Properties: create, query, edit
        useStampDistance (bool?): Force the stamps to be spread out along the stroke, rather than building up continually.  
                Properties: create, query, edit
        useStampImage (bool?): Specifies if the brush uses a stamp image.  
                Properties: create, query, edit
        useSteadyStroke (bool?): Turns using steady stroke on/off.  
                Properties: create, query, edit
        wholeStroke (bool?): Continuously recalculates the underlying tool plane from all the vertices affected during the stroke.  
                Properties: create, query, edit
        wireframeAlpha (Queryable[float]?): Sets the alpha value of the wireframe for the object that is being sculpted.  
                Properties: create, query, edit
        wireframeColor (Queryable[Tuple[float, float, float]]?): Sets the color of the wireframe for the object that is being sculpted.  
                Values should be 0. 1 RGB.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

