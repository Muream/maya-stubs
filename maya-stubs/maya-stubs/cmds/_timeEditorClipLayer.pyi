from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorClipLayer(*args: Any, edit: bool = ..., query: bool = ..., addAttribute: str = ..., addLayer: str = ..., addObject: str = ..., allLayers: bool = ..., attribute: Multiuse[str] = ..., attributeKeyable: Queryable[str] = ..., clipId: int = ..., index: int = ..., keySiblings: bool = ..., layerId: int = ..., layerName: Queryable[str] = ..., mode: int = ..., mute: bool = ..., name: bool = ..., path: str = ..., removeAttribute: str = ..., removeLayer: bool = ..., removeObject: str = ..., resetSolo: bool = ..., setKeyframe: bool = ..., solo: bool = ..., zeroKeying: bool = ...) -> Union[str, bool]:
    """Time Editor clip layers commandstimeEditor, nle, layer
    Args:
        addAttribute (str?): Add given plug to a layer with a supplied layerId.  
                Properties: edit
        addLayer (str?): Add a new layer with a given name.  
                Properties: edit
        addObject (str?): Add given object with all its attributes in the clip to a layer with a supplied layerId.  
                Properties: edit
        allLayers (bool?): Return all layers given clip ID.  
                Properties: query
        attribute (Multiuse[str]?): The attribute path to key.  
                Properties: edit, multiuse
        attributeKeyable (Queryable[str]?): Return whether specified attribute is keyable.  
                Properties: query
        clipId (int?): ID of the clip this layer command operates on.  
                			In query mode, this flag can accept a value.  
                Properties: edit
        index (int?): Layer index, used when adding new layer at specific location in the stack.  
                Properties: edit
        keySiblings (bool?): If set to true, additional attributes might be keyed while keying to achieve desired result.  
                Properties: edit
        layerId (int?): Layer ID used in conjunction with other edit flags.  
                			In query mode, this flag can accept a value.  
                Properties: edit
        layerName (Queryable[str]?): Edit layer name.  
                In query mode, return the layer name given its layer ID and clip ID.  
                Properties: query, edit
        mode (int?): To control the playback speed of the clip by animation curve:  
              
                0. additive  
                1. additive override  
                2. override  
                3. override passthrough  
                Properties: edit
        mute (bool?): Mute/unmute a layer given its layer ID and clip ID.  
                Properties: edit
        name (bool?): Query the attribute name of a layer given its layer ID and clip ID.  
                Properties: query
        path (str?): Full path of a layer or a clip on which to operate. For example: composition1|track1|clip1|layer1; composition1|track1|group|track1|clip1.  
                			In query mode, this flag can accept a value.  
                Properties: edit
        removeAttribute (str?): Remove given plug from a layer with a supplied layerId.  
                Properties: edit
        removeLayer (bool?): Remove layer with an ID.  
                Properties: edit
        removeObject (str?): Remove given object with all its attributes in the clip to a layer with a supplied layerId.  
                Properties: edit
        resetSolo (bool?): Unsolo all soloed layers in a given clip ID.  
                Properties: edit
        setKeyframe (bool?): Set keyframe on specified attributes on specified layer of a clip.  
                Use -clipId to indicate the specified clip.  
                Use -layerId to indicate the specified layer of the clip.  
                Use -attribute to indicate the specified attributes (if no attribute flag is used, all attribute will be keyed).  
                Use -zeroKeying to indicate that zero offset from original animation should be keyed.  
                Properties: edit
        solo (bool?): Solo/unsolo a layer given its layers ID and clip ID.  
                Properties: edit
        zeroKeying (bool?): Indicate if the key to set should be zero offset from original animation.  
                Properties: edit

    Returns:
        str: Command result

    Example:
    """

