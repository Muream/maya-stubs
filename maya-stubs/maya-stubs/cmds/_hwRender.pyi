from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hwRender(*args: str, query: bool = ..., acceleratedMultiSampleSupport: bool = ..., activeTextureCount: bool = ..., camera: Queryable[str] = ..., currentFrame: bool = ..., currentView: bool = ..., edgeAntiAliasing: Queryable[Tuple[int, int]] = ..., fixFileNameNumberPattern: bool = ..., frame: float = ..., fullRenderSupport: bool = ..., height: Queryable[int] = ..., imageFileName: bool = ..., layer: Queryable[str] = ..., limitedRenderSupport: bool = ..., lowQualityLighting: bool = ..., noRenderView: bool = ..., notWriteToFile: bool = ..., printGeometry: bool = ..., renderHardwareName: bool = ..., renderRegion: Queryable[Tuple[int, int, int, int]] = ..., renderSelected: bool = ..., textureResolution: Queryable[int] = ..., width: Queryable[int] = ..., writeAlpha: bool = ..., writeDepth: bool = ...) -> Union[bool, str, Tuple[int, int], int, Tuple[int, int, int, int]]:
    """Renders an image or a sequence using the hardware rendering enginehardware, rendering
    Args:
        acceleratedMultiSampleSupport (bool?): This flag when used with query will return whether the graphics supports  
                    hardware accelerated multi-sampling.  
                Properties: query
        activeTextureCount (bool?): This flag when used with query will return the number of textures that  
                    have been bound to the graphics by the hardware renderer.  
                Properties: query
        camera (Queryable[str]?): Specify the camera to use.  Use the first available camera if the camera  
                        given is not found.  
                Properties: create, query
        currentFrame (bool?): Render the current frame.  
                Properties: create, query
        currentView (bool?): When turned on, only the current view will be rendered.  
                Properties: create, query
        edgeAntiAliasing (Queryable[Tuple[int, int]]?): Enables multipass rendering. Controls for the number of exposures rendered  
                per frame are provided in the form of two associated flag arguments. The first  
                specifies the sampling algorithm:  
              
                0. Uniform Weighted Grid Sampling  
                1. Rotated Grid Super Sampling (RGSS)  
                2. Gaussian Weighted Sampling  
              
                 Use of a sampling method other than the others listed above, will result in  
                use of the default sample method of Uniform Weighted Grid Sampling. The second  
                argument specifies a number of samples to use. For each sampling algorithm  
                there is a fixed set of sample counts available:  
              
                0. Uniform Weighted Grid Sampling  
                1 Sample  
                3 Samples  
                4 Samples  
                5 Samples  
                7 Samples  
                9 Samples  
                16 Samples  
                25 Samples  
                36 Samples  
                1. Rotated Grid Super Sampling (RGSS)  
                1 Sample  
                4 Samples  
                5 Samples  
                2. Gaussian Weighted Sampling  
                1 Sample  
                3 Samples  
                4 Samples  
                5 Samples  
                7 Samples  
                9 Samples  
                16 Samples  
                25 Samples  
                36 Samples  
              
                 Using a sampling count other than the allowable options for the given  
                sampling method will result in using the default sample count of 5. The values  
                passed via the command will override settings stored in the  
                hardwareRenderGlobals node.  
                Properties: create, query
        fixFileNameNumberPattern (bool?): This flag allows the user to take the hardwareRenderGlobals  
                    filename as the initial filename pattern,  
                    fix the frame number pattern in the filename in a unique way,  
                    returns the new filename pattern.  This does not change the  
                    hardwareRenderGlobals's filename.  
                Properties: create, query
        frame (float?): Specify the frame to render.  
                Properties: create
        fullRenderSupport (bool?): This flag may be used in the create or query context.  
                    In the create context, it will force the renderer to abort and not  
                    render any frames if the hardware is not fully supported.  
                        In the query context, it will return whether full quality rendering  
                    is supported on the current graphics system. Please see the graphics  
                    card qualification charts for an explanation of limited support.  
                Properties: create, query
        height (Queryable[int]?): Height. If not used, the height is taken from the render globals settings.  
                Properties: create, query
        imageFileName (bool?): This flag let people query the image name for a specified frame.  
                    The frame can be specified using the "-frame" flag.  
                    When no "-frame" is used, the  
                    current frame number is used.  
                Properties: create, query
        layer (Queryable[str]?): Render the specified render layer.  
                        Only this render layer will be rendered,  
                        regardless of the renderable attribute value of the render layer.  
                        The layer name will be appended to the output image file name.  
                        The specified render layer becomes the current render layer before rendering,  
                        and remains as current render layer after the rendering.  
                Properties: create, query
        limitedRenderSupport (bool?): This flag when used with query will return whether limited rendering is supported  
                        on the current graphics system. Please see the graphics card qualification  
                        charts for the current definition of limited support.  
                Properties: query
        lowQualityLighting (bool?): Disable lighting evaluation per pixel (fragment).  
                        Note: The values passed via the command will override settings stored in  
                    the hardware render globals node.  
                Properties: create, query
        noRenderView (bool?): When turned on, the render view is not updated after image computation  
                Properties: create, query
        notWriteToFile (bool?): This flag is set to true if the user does not want to write  
                    the image to a file.  It is set to false, otherwise.  
                    The default value of the flag is "false".  
                Properties: create, query
        printGeometry (bool?): Print the geomety objects as they get translated.  
                Properties: create, query
        renderHardwareName (bool?): This flag will create a graphics context and return the name of the  
                    graphics hardware being used. The graphics hardware is determined by  
                    creating an off screen buffer and querying the GL_RENDERER string  
                    from OpenGL. If the off screen buffer cannot be created an empty  
                    string is returned.  
                Properties: query
        renderRegion (Queryable[Tuple[int, int, int, int]]?): Render region. The parameters are 4 integers, indicating  
                            left right bottom top  
                    of the region.  
                Properties: create, query
        renderSelected (bool?): Only renders the selected objects.  
                Properties: create, query
        textureResolution (Queryable[int]?): Specify the desired resolution of baked textures.  
                Properties: create, query
        width (Queryable[int]?): Width. If not used, the width is taken from the render globals settings.  
                Properties: create, query
        writeAlpha (bool?): Read the alpha channel of color buffer and return as tif file.  
                Properties: create, query
        writeDepth (bool?): Read the depth buffer and return as tif file.  
                Properties: create, query

    Returns:
        bool: Command result

    Example:
    """

