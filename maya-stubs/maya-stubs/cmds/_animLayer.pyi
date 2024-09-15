from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def animLayer(arg0: str = ..., arg1: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., addRelatedKG: bool = ..., addSelectedObjects: bool = ..., affectedLayers: bool = ..., animCurves: bool = ..., attribute: Queryable[Multiuse[str]] = ..., baseAnimCurves: bool = ..., bestAnimLayer: bool = ..., bestLayer: bool = ..., blendNodes: bool = ..., children: Queryable[str] = ..., collapse: bool = ..., copy: str = ..., copyAnimation: str = ..., copyNoAnimation: str = ..., excludeBoolean: bool = ..., excludeDynamic: bool = ..., excludeEnum: bool = ..., excludeProxy: bool = ..., excludeRotate: bool = ..., excludeScale: bool = ..., excludeTranslate: bool = ..., excludeVisibility: bool = ..., exists: bool = ..., extractAnimation: str = ..., findCurveForPlug: str = ..., forceUIRebuild: bool = ..., forceUIRefresh: bool = ..., layeredPlug: str = ..., lock: bool = ..., maxLayers: bool = ..., moveLayerAfter: str = ..., moveLayerBefore: str = ..., mute: bool = ..., override: bool = ..., parent: Queryable[str] = ..., passthrough: bool = ..., preferred: bool = ..., removeAllAttributes: bool = ..., removeAttribute: Multiuse[str] = ..., removeSelectedObjects: bool = ..., root: Queryable[str] = ..., selected: bool = ..., solo: bool = ..., weight: Queryable[float] = ..., writeBlendnodeDestinations: bool = ...) -> Union[str, bool, Multiuse[str], float]:
    """This command creates and edits animation layers.layer, animation, additive, override
    Args:
        addRelatedKG (bool?): When adding or removing selected object(s) from the layer, adds associated keying group(s)  
                to the object(s).  
                Properties: create, query, edit
        addSelectedObjects (bool?): Adds selected object(s) to the layer.  
                Properties: create, query, edit
        affectedLayers (bool?): Return the layers that the currently selected object(s) are members of  
                Properties: query
        animCurves (bool?): In query mode returns the anim curves associated with this layer  
                Properties: create, query, edit
        attribute (Queryable[Multiuse[str]]?): Adds a specific attribute on a object to the layer.  
                Properties: create, query, edit, multiuse
        baseAnimCurves (bool?): In query mode returns the base layer anim curves associated with this layer, if any.  
                Properties: create, query, edit
        bestAnimLayer (bool?): In query mode returns the best anim layers for keying for the selected  
                objects. If used in conjunction with -at, will return the best anim layers  
                for keying for the specific plugs (attributes) specified.  
                Properties: create, query, edit
        bestLayer (bool?): Return the layer that will be keyed for specified attribute.  
                Properties: query
        blendNodes (bool?): In query mode returns the blend nodes associated with this layer  
                Properties: create, query, edit
        children (Queryable[str]?): Get the list of children layers. Return value is a string array.  
                Properties: query
        collapse (bool?): Determine if a layer is collapse in the layer editor.  
                Properties: create, query, edit
        copy (str?): Copy from the layer.  
                Properties: edit
        copyAnimation (str?): Copy animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.  
                Properties: create, edit
        copyNoAnimation (str?): Copy from layer without the animation curves.  
                Properties: edit
        excludeBoolean (bool?): When adding or removing selected object(s) from the layer, excludes any boolean attributes.  
                Properties: create, query, edit
        excludeDynamic (bool?): When adding or removing selected object(s) from the layer, excludes any dynamic attributes.  
                Properties: create, query, edit
        excludeEnum (bool?): When adding or removing selected object(s) from the layer, excludes any enum attributes.  
                Properties: create, query, edit
        excludeProxy (bool?): When adding or removing selected object(s) from the layer, excludes any proxy attributes.  
                Properties: create, query, edit
        excludeRotate (bool?): When adding or removing selected object(s) from the layer, excludes the rotate attribute.  
                Properties: create, query, edit
        excludeScale (bool?): When adding or removing selected object(s) from the layer, excludes the scale attribute.  
                Properties: create, query, edit
        excludeTranslate (bool?): When adding or removing selected object(s) from the layer, excludes the translate attribute.  
                Properties: create, query, edit
        excludeVisibility (bool?): When adding or removing selected object(s) from the layer, excludes the visibility attribute.  
                Properties: create, query, edit
        exists (bool?): Determine if a layer exists.  
                Properties: query
        extractAnimation (str?): Transfer animation from specified layer to destination layer, only animation that are on attribute layered by both layer that are concerned.  
                Properties: create, edit
        findCurveForPlug (str?): Finds the parameter curve containing the animation data for the specified plug on the given layer.  
                			In query mode, this flag needs a value.  
                Properties: query, edit
        forceUIRebuild (bool?): Rebuilds the animation layers user interface.  
                Properties: create
        forceUIRefresh (bool?): Refreshes the animation layers user interface.  
                Properties: create
        layeredPlug (str?): Returns the plug on the blend node corresponding to the specified layer  
                			In query mode, this flag needs a value.  
                Properties: query
        lock (bool?): Set the lock state of the specified layer. A locked layer cannot receive key. Default is false.  
                Properties: create, query, edit
        maxLayers (bool?): Returns the maximum number of anim layers supported by this product.  
                Properties: query
        moveLayerAfter (str?): Move layer after the specified layer  
                Properties: edit
        moveLayerBefore (str?): Move layer before the specified layer  
                Properties: edit
        mute (bool?): Set the mute state of the specified layer. Default is false.  
                Properties: create, query, edit
        override (bool?): Set the overide state of the specified layer. Default is false.  
                Properties: create, query, edit
        parent (Queryable[str]?): Set the parent of the specified layer. Default is the animation layer root.  
                Properties: create, query, edit
        passthrough (bool?): Set the passthrough state of the specified layer. Default is true.  
                Properties: create, query, edit
        preferred (bool?): Determine if a layer is a preferred layer, the best layer algorithm will try to set keyframe in preferred layer first.  
                Properties: create, query, edit
        removeAllAttributes (bool?): Remove all objects from the layer.  
                Properties: edit
        removeAttribute (Multiuse[str]?): Remove object from the layer.  
                Properties: edit, multiuse
        removeSelectedObjects (bool?): Removes selected object(s) from the layer.  
                Properties: edit
        root (Queryable[str]?): Return the base layer if it exist  
                Properties: query
        selected (bool?): Determine if a layer is selected, a selected layer will be show in the timecontrol, graph editor.  
                Properties: create, query, edit
        solo (bool?): Set the solo state of the specified layer. Default is false.  
                Properties: create, query, edit
        weight (Queryable[float]?): Set the weight of the specified layer between 0.0 and 1.0. Default is 1.  
                Properties: create, query, edit
        writeBlendnodeDestinations (bool?): In edit mode writes the destination plugs of the blend nodes that belong to the layer  
                into the blend node. This is used for layer import/export purposes and is not for  
                general use.  
                Properties: edit

    Returns:
        str: Return values currently not documented.

    Example:
    """

