from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayPref(*, query: bool = ..., activeObjectPivots: bool = ..., displayAffected: bool = ..., displayGradient: bool = ..., ghostFrames: Queryable[Tuple[int, int, int]] = ..., materialLoadingMode: Queryable[str] = ..., maxHardwareTextureResolution: bool = ..., maxTextureResolution: Queryable[int] = ..., purgeExistingTextures: bool = ..., regionOfEffect: bool = ..., shadeTemplates: bool = ..., textureDrawPixel: bool = ..., wireframeOnShadedActive: Queryable[str] = ...) -> Union[bool, Tuple[int, int, int], str, int]:
    """This command sets/queries the state of global display parameters.
    Args:
        activeObjectPivots (bool?): Sets the display state for drawing pivots for active objects.  
                Properties: create, query
        displayAffected (bool?): Turns on/off the special coloring of objects that are affected  
                by the objects that are currently in the selection list.  
                If one of the curves in a loft were selected and this feature were  
                turned on, then the lofted surface would be highlighted because it  
                is affected by the loft curve.  
                Properties: create, query
        displayGradient (bool?): Set whether to display the background using a colored gradient as opposed  
                to a constant background color.  
                Properties: create, query
        ghostFrames (Queryable[Tuple[int, int, int]]?): Obsolete - use the "ghosting" command to set these values.  
                Properties: create, query
        materialLoadingMode (Queryable[str]?): Sets the material loading mode when loading the scene.  Possible  
                values for the string argument are  
                "immediate", "deferred" and "parallel".  
                Properties: create, query
        maxHardwareTextureResolution (bool?): Query the maximum allowable hardware texture resolution  
                available on the current video card. This maximum can vary  
                between different video cards and different operating systems.  
                Properties: query
        maxTextureResolution (Queryable[int]?): Sets the maximum hardware texture resolution to be  
                used when creating hardware textures for display. The maximum  
                will be clamped to the maximum allowable texture determined  
                for the hardware at the time this command is invoked. Use  
                the -maxHardwareTextureResolution to retrieve this maximum value.  
                Existing hardware textures are not affected. Only newly created  
                textures will be clamped to this maximum.  
                Properties: create, query
        purgeExistingTextures (bool?): Purge any existing hardware textures. This will force  
                a re-evaluation of hardware textures used for display, and  
                thus may take some time to evaluate.  
                Properties: create
        regionOfEffect (bool?): Turns on/off the display of the region of curves/surfaces  
                that is affected by changes to selected CVs and edit points.  
                Properties: create, query
        shadeTemplates (bool?): Turns on/off the display of templated surfaces as shaded  
                in shaded display mode. If its off, templated surfaces appear  
                in wireframe.  
                Properties: create, query
        textureDrawPixel (bool?): Sets the display mode for drawing image planes. True for  
                use of gltexture calls for perspective views. This flag should  
                not normally be needed. Image Planes may display faster on  
                Windows but can result in some display artifacts.  
                Properties: create, query
        wireframeOnShadedActive (Queryable[str]?): Sets the display state for drawing the wireframe on active  
                shaded objects.  Possible values for the string argument are  
                "full", "reduced" and "none".  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

