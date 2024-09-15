from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def surfaceSampler(*args: str, camera: str = ..., fileFormat: Multiuse[str] = ..., filename: Multiuse[str] = ..., filterSize: float = ..., filterType: int = ..., flipU: bool = ..., flipV: bool = ..., ignoreMirroredFaces: bool = ..., ignoreTransforms: bool = ..., mapHeight: Multiuse[int] = ..., mapMaterials: Multiuse[bool] = ..., mapOutput: Multiuse[str] = ..., mapSpace: Multiuse[str] = ..., mapWidth: Multiuse[int] = ..., maxSearchDistance: Multiuse[float] = ..., maximumValue: Multiuse[float] = ..., overscan: int = ..., searchCage: Multiuse[str] = ..., searchMethod: int = ..., searchOffset: Multiuse[float] = ..., shadows: Multiuse[bool] = ..., source: Multiuse[str] = ..., sourceUVSpace: Multiuse[str] = ..., superSampling: int = ..., target: Multiuse[str] = ..., targetUVSpace: Multiuse[str] = ..., useGeometryNormals: bool = ..., uvSet: Multiuse[str] = ...) -> bool:
    """Maps surface detail from a source surface to a new texture map on a target
    surface. Both objects must be selected when the command is invoked, with
    the source surface selected first, and the target last.
    Args:
        camera (str?): Specify the camera to use for camera specific lighting calculations such as  
                specular highlights or reflections.  
                Properties: create
        fileFormat (Multiuse[str]?): The image format as a file extension (e.g. "dds").  
                This must be included once for every output map specified.  
                Properties: create, multiuse
        filename (Multiuse[str]?): The filename to use when creating the map.  
                This must be included once for every output map specified.  
                Properties: create, multiuse
        filterSize (float?): The filter size to use in pixels. Larger values (e.g. over 2.0) will produce smoother/softer  
                results, while values closer to 1.0 will produce sharper results.  
                Properties: create
        filterType (int?): The filter type to use. 0 is a Guassian filter, 1 is a triangular filter, 2 is a box filter.  
                Properties: create
        flipU (bool?): Flip the U coordinate of the generated image.  
                Properties: create
        flipV (bool?): Flip the V coordinate of the generated image.  
                Properties: create
        ignoreMirroredFaces (bool?): Stops reverse wound (i.e. mirrored) faces from contributing to the map  
                generation.  
                Properties: create
        ignoreTransforms (bool?): Controls whether transforms are used (meaning the search is performed in worldspace),  
                or not (meaning the search is performed in object space).  
                Properties: create
        mapHeight (Multiuse[int]?): Pixel width of the generated map.  
                This must be included once for every output map specified.  
                Properties: create, multiuse
        mapMaterials (Multiuse[bool]?): Where appropriate (e.g. normal maps), this controls whether the material  
                should be included when sampling the map attribute.  
                This must be included once for every output map specified.  
                Properties: create, multiuse
        mapOutput (Multiuse[str]?): Specifies a new output map to create. One of "normal", "displacement"  
                "diffuseRGB", "litAndShadedRGB", or "alpha"  
                Properties: create, multiuse
        mapSpace (Multiuse[str]?): The space to generate the map in. Valid keyword is "object". Default  
                is tangent space.  
                This must be included once for every output map specified.  
                Properties: create, multiuse
        mapWidth (Multiuse[int]?): Pixel width of the generated map. Some output image formats require even or power of 2.  
                This must be included once for every output map specified.  
                Properties: create, multiuse
        maxSearchDistance (Multiuse[float]?): Controls the maximum distance away from a target surface that will  
                be searched for source surfaces. A value of 0 indicates no limit.  
                When generated maps include artifacts from the "other side" of an  
                object, try setting this value to a distance approximately equal to  
                the radius of the object.  
                If this flag is included, it must be included once for every target.  
                Properties: create, multiuse
        maximumValue (Multiuse[float]?): The maximum value to include in the map. This allows control of how floating  
                point values (like displacement) are quantised into integer image formats.  
                Properties: create, multiuse
        overscan (int?): The number of additional pixels to render around UV borders.  
                This will help to minimise texel filtering artifacts on  
                UV seams. When mipmaps are going to be generated for the texture  
                a higher value may be necessary (in addition to a filterSize  
                greater than 1).  
                Properties: create
        searchCage (Multiuse[str]?): Specifies a search envelope surface to use as a search guide  
                when looking for source surfaces.  
                If this flag is included, it must be included once for every target.  
                Properties: create, multiuse
        searchMethod (int?): Controls the search method used to match sample points on a target surface  
                to points on the sources. 0 is closest to envelope, 1 is prefer any intersection  
                inside envelope to intersections outside it, and 2 is only use intersections  
                inside envelope.  
                Properties: create
        searchOffset (Multiuse[float]?): Specifies a fixed offset from a target surface to use as the  
                starting point when looking for source surfaces. This value is  
                only used when no search cage is specified for a given target.  
                If this flag is included, it must be included once for every target.  
                Properties: create, multiuse
        shadows (Multiuse[bool]?): Where appropriate (e.g. lit and shaded), this controls whether  
                shadows are included in the calculation. Currently only depth  
                map shadows are supported.  
                Properties: create, multiuse
        source (Multiuse[str]?): Specifies a surface to use as a sampling source  
                Properties: create, multiuse
        sourceUVSpace (Multiuse[str]?): Specifies that the transfer of data between the surfaces should be  
                done in UV space and specifies the name of the UV set on the source  
                surface(s) that should be used as the transfer space.  
                Properties: create, multiuse
        superSampling (int?): Controls the number of sampling points calculated for each output value. The algorithm will  
                use 2 ^ n squared samples for each point (so a value of 0 will use a single sample, while a value  
                of 3 will calculate 64 samples for each point).  
                Properties: create
        target (Multiuse[str]?): Specified a surface to sample output information for.  
                Properties: create, multiuse
        targetUVSpace (Multiuse[str]?): Specifies that the transfer of data between the surfaces should be  
                done in UV space and specifies the name of the UV set on the target  
                surface(s) that should be used as the transfer space.  
                Properties: create, multiuse
        useGeometryNormals (bool?): Controls whether geometry or surface normals are used for surface searching.  
                Using geometry normals will ensure a smooth mapping but can introduce distorted  
                mappings where there are large distances between the source and target surfaces.  
                Surface normals can introduce overlapping or discontinuous mappings, but does  
                allow map distortion to be influenced by surface normal direction.  
                Properties: create
        uvSet (Multiuse[str]?): The name of the UV set to use when creating output maps.  
                If this flag is included, it must be included once for every target.  
                Properties: create, multiuse

    Returns:
        bool:

    Example:
    """

