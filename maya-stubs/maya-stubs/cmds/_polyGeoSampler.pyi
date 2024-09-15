from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyGeoSampler(*args: Any, edit: bool = ..., alphaBlend: str = ..., averageColor: bool = ..., clampAlphaMax: float = ..., clampAlphaMin: float = ..., clampRGBMax: Tuple[float, float, float] = ..., clampRGBMin: Tuple[float, float, float] = ..., colorBlend: str = ..., colorDisplayOption: bool = ..., computeShadows: bool = ..., displaceGeometry: bool = ..., flatShading: bool = ..., ignoreDoubleSided: bool = ..., lightingOnly: bool = ..., reuseShadows: bool = ..., sampleByFace: bool = ..., scaleFactor: float = ..., shareUV: bool = ..., useLightShadows: bool = ...) -> bool:
    """This command performs a render sampling of surface color and transparency
    for each selected vertex or face and stores the sampled data
    as either the color value, or uses the sampled data to displace
    the affected vertices or faces by a sampled data value.
    Transparency is not used for displacement, and displacement
    is performed along vertex normals.
    The sampled data value used can be pre-scaled by a user defined
    amount.
    Additionally, the normals chosen for sampling can be overridden
    using a "flat" shading option. This option basically means
    to always use the normals of the faces when computing
    sampling values. This may be a desired if the user
    wishes to override an edge smoothness factor. Basically
    with the "flat" shading option on, edges are always
    considered to be hard.
    Note that displacement sampling will result
    in the -sampleByFace option to be turned
    off, since a displacement of a vertex
    always affects the faces the vertex
    is connected to.
    Finally, it is possible to force the storage of shared
    colors per vertex, and / or force the usage of unshared
    UV values.
    The computation of the resulting color is as follows:The analogous computation is done for computing the resulting alpha
    value.
    The command requires that there be a camera selected in your scene in
    order to work properly in -batch or -prompt mode.poly, sampling, GeoSampler
    Args:
        alphaBlend (str?): When specified, indicates the type of alpha blend to  
                be applied. Options are: "none", "overwrite", "add",  
                "subtract", "multiply", "divide", "average".  
                This option only applies when colors are being  
                set. The default if this argument is not  
                specified is "overwrite".  
                The "none" options  
                to not overwrite the existing value.  
                Properties: create, edit
        averageColor (bool?): When used, will mean to force the storage of shared colors  
                for vertex level sampling. By default vertex level sampling  
                stores unshared colors.  
                Properties: create, edit
        clampAlphaMax (float?): When used, will mean to clamp the storage of alpha  
                to a maximum  
                Properties: create, edit
        clampAlphaMin (float?): When used, will mean to clamp the storage of alpha  
                to a minimum  
                Properties: create, edit
        clampRGBMax (Tuple[float, float, float]?): When used, will mean to clamp the storage of RGB  
                color to a maximum  
                Properties: create, edit
        clampRGBMin (Tuple[float, float, float]?): When used, will mean to clamp the storage of RGB  
                color to a minimum  
                Properties: create, edit
        colorBlend (str?): When specified, indicates the type of color blend to  
                be applied. Options are: "none", "overwrite", "add",  
                "subtract", "multiply", "divide", "average".  
                This option only applies when colors are being  
                set. The default if this argument is not  
                specified is "overwrite".  
                The "none" options  
                to not overwrite the existing value.  
                Properties: create, edit
        colorDisplayOption (bool?): Change the display options on the mesh to display the vertex colors.  
                Properties: create, edit
        computeShadows (bool?): When used, shadow maps will be computed, saved, and reused during the sampling  
                process.  
                Properties: create, edit
        displaceGeometry (bool?): When used, geometry will be displaced along the normals at  
                the sampling positions, as opposed to storing color values. The  
                default is to store colors.  
                Properties: create, edit
        flatShading (bool?): When used, flat shaded sampling will be computed. The default  
                is smooth shading.  
                Properties: create, edit
        ignoreDoubleSided (bool?): When specified, the double sided flag will be ignored  
                for prelighting.  
                Properties: create, edit
        lightingOnly (bool?): When used, incoming illumination will be computed as opposed to  
                surface color an tranparency  
                Properties: create, edit
        reuseShadows (bool?): When used, if shadow maps were previosly computed and saved, then  
                they will be reused during the sampling process. The computeShadows  
                option must be enabled for this option to apply.  
                Properties: create, edit
        sampleByFace (bool?): When used, sample will occur at a per face level versus a per  
                vertex level, which is the default behaviour  
                Properties: create, edit
        scaleFactor (float?): When used, will scale the sampled value by the specified amount.  
                The default scale factor is 1.0. Negative values are acceptable  
                for displacement, but not for color values.  
                Properties: create, edit
        shareUV (bool?): When used, UVs are shared at a vertex when sampled.  
                By default UVs are forced to be unshared.  
                Properties: create, edit
        useLightShadows (bool?): When used, will use each lights shadow map options. Otherwise  
                these options will be overrridden when the computeShadows, and/or  
                reusedShadows option is enabled.  
                Properties: create, edit

    Returns:
        bool: Success or Failure

    Example:
    """

