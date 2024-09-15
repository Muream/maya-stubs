from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def iprEngine(*args: Any, edit: bool = ..., query: bool = ..., copy: str = ..., defineTemplate: str = ..., diagnostics: bool = ..., estimatedMemory: bool = ..., exists: bool = ..., iprImage: Queryable[str] = ..., motionVectorFile: bool = ..., object: Queryable[str] = ..., region: Queryable[Tuple[int, int, int, int]] = ..., relatedFiles: bool = ..., releaseIprImage: bool = ..., resolution: bool = ..., scanlineIncrement: Queryable[str] = ..., showProgressBar: bool = ..., startTuning: bool = ..., stopTuning: bool = ..., underPixel: Tuple[int, int] = ..., update: bool = ..., updateDepthOfField: bool = ..., updateLightGlow: bool = ..., updateMotionBlur: bool = ..., updatePort: Queryable[str] = ..., updateShaderGlow: bool = ..., updateShading: bool = ..., updateShadowMaps: bool = ..., useTemplate: str = ...) -> Union[str, bool, Tuple[int, int, int, int]]:
    """Command to create or edit an iprEngine.  A iprEngine
    is an object that watches for changes to shading
    networks and automatically reshades to generate an
    up-to-date image.
    Args:
        copy (str?): Copies the deep raster file, as well as its related files, to the  
                new location.  
                Properties: edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        diagnostics (bool?): The diagnostics should be shown  
                Properties: edit
        estimatedMemory (bool?): Displays the estimated memory being used by IPR.  
                Properties: query
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        iprImage (Queryable[str]?): Specify the ipr image to use.  
                Properties: create, query, edit
        motionVectorFile (bool?): Returns the name of the motion vector file used by IPR.  
                Properties: query
        object (Queryable[str]?): The objects to be tuned.  
                Properties: create, query, edit
        region (Queryable[Tuple[int, int, int, int]]?): The coordinates of the region to be tuned.  
                The integers are in the sequence left bottom right top  
                or x1,y2  x2,y2  
                Properties: create, query, edit
        relatedFiles (bool?): Returns the names for the related files, e.g, the non-glow-non-blur image,  
                the motion vector file, and the depth-map files.  
                Properties: query
        releaseIprImage (bool?): The ipr image should be released and  
                memory should    be freed.  
                Properties: edit
        resolution (bool?): The width and height of the ipr file.  
                Properties: query
        scanlineIncrement (Queryable[str]?): Set the scanline increment percentage.  If the height of  
                the region being update is 240 pixels, and the scanlineIncrement  
                is 10% then the image will refresh blocks of 24 scanlines.  
                Properties: create, query, edit
        showProgressBar (bool?): Show progress bar during tuning.  
                Properties: create, query, edit
        startTuning (bool?): An ipr image has been specified and now changes  
                to shading    networks should force an image to be  
                produced.  
                Properties: create, query, edit
        stopTuning (bool?): Tuning should cease but ipr image should not be closed.  
                Properties: create, query, edit
        underPixel (Tuple[int, int]?): Get list of objects under the pixel sprcified.  
                Properties: edit
        update (bool?): Force an update.  
                Properties: create, edit
        updateDepthOfField (bool?): Force a refresh of depth-of-field.  
                Properties: create, edit
        updateLightGlow (bool?): Automatically update when light glow changes.  
                Properties: create, query, edit
        updateMotionBlur (bool?): Automatically update when 2.5D motion blur changes.  
                Properties: create, query, edit
        updatePort (Queryable[str]?): The name of the port that is to be updated when  
                pixel values are recomputed.  (not currently supported)  
                Properties: create, query, edit
        updateShaderGlow (bool?): Automatically update when shader glow changes.  
                Properties: create, query, edit
        updateShading (bool?): Automatically update shading.  
                Properties: create, query, edit
        updateShadowMaps (bool?): Force the shadow maps to be generated and an update to occur.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: - the name of the ipr engine created or modified

    Example:
    """

