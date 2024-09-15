from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def glRender(*, edit: bool = ..., query: bool = ..., accumBufferPasses: Queryable[int] = ..., alphaSource: Queryable[str] = ..., antiAliasMethod: Queryable[str] = ..., cameraIcons: bool = ..., clearClr: Queryable[Tuple[float, float, float]] = ..., collisionIcons: bool = ..., crossingEffect: bool = ..., currentFrame: bool = ..., drawStyle: Queryable[str] = ..., edgeSmoothness: Queryable[float] = ..., emitterIcons: bool = ..., fieldIcons: bool = ..., flipbookCallback: Queryable[str] = ..., frameEnd: Queryable[int] = ..., frameIncrement: Queryable[int] = ..., frameStart: Queryable[int] = ..., fullResolution: bool = ..., grid: bool = ..., imageDirectory: Queryable[str] = ..., imageName: Queryable[str] = ..., imageSize: Queryable[Tuple[int, int, float]] = ..., lightIcons: bool = ..., lightingMode: Queryable[str] = ..., lineSmoothing: bool = ..., offScreen: bool = ..., renderFrame: Queryable[str] = ..., renderSequence: Queryable[str] = ..., sharpness: Queryable[float] = ..., shutterAngle: Queryable[float] = ..., textureDisplay: bool = ..., transformIcons: bool = ..., useAccumBuffer: bool = ..., viewport: Queryable[Tuple[int, int, float]] = ..., writeDepthMap: bool = ...) -> Union[bool, int, str, Tuple[float, float, float], float, Tuple[int, int, float]]:
    """This command provides access to the Hardware Render Manager (HRM). There
    is one-and-only-one HRM in maya. The HRM controls the rendering performed
    in the hardware render buffer window. This command allows shell scripts,
    to modify the render state, and to initiate a render request.
    Args:
        accumBufferPasses (Queryable[int]?): Set the number of accum buffer render passes.  
                Properties: query, edit
        alphaSource (Queryable[str]?): Control the alpha source when writing image files. Valid values  
                include: off, alpha, red, green, blue, luminance, clamp, invClamp.  
                Properties: query, edit
        antiAliasMethod (Queryable[str]?): Set the method used for anti-aliasing polygons: off,  
                uniform, gaussian.  
                Properties: query, edit
        cameraIcons (bool?): Set display status of camera icons.  
                Properties: query, edit
        clearClr (Queryable[Tuple[float, float, float]]?): Set the viewport clear color (0. 1).  
                Properties: query, edit
        collisionIcons (bool?): Set display status of collison model icons.  
                Properties: query, edit
        crossingEffect (bool?): Enable/disable image filtering with a convolution filter.  
                Properties: query, edit
        currentFrame (bool?): Returns the current frame being rendered.  
                Properties: query
        drawStyle (Queryable[str]?): Set the object drawing style: boundingBox, points, wireframe,  
                flatShaded, smoothShaded.  
                Properties: query, edit
        edgeSmoothness (Queryable[float]?): Controls the amount of edge smoothing. A value of 0.0 gives no  
                smoothing, 1.0 gives default smoothing, and any other value scales  
                the amount of default smoothing. Must enable the accumulation buffer.  
                Properties: query, edit
        emitterIcons (bool?): Set display status of emitter icons.  
                Properties: query, edit
        fieldIcons (bool?): Set display status of field icons.  
                Properties: query, edit
        flipbookCallback (Queryable[str]?): Register a procedure to be called after the render sequence has  
                completed. Used to build the flipbook pulldown menu. See the  
                example section for more details about how to build this procedure.  
                Properties: query, edit
        frameEnd (Queryable[int]?): Set the last frame to be rendered.  
                Properties: query, edit
        frameIncrement (Queryable[int]?): Set the frame increment during rendering.  
                Properties: query, edit
        frameStart (Queryable[int]?): Set the first frame to be rendered.  
                Properties: query, edit
        fullResolution (bool?): Enable/disable rendering to full image output resolution.  
                Must set a valid image output resolution (-is).  
                Properties: query, edit
        grid (bool?): Set display status of the grid.  
                Properties: query, edit
        imageDirectory (Queryable[str]?): Set the directory for the image files.  
                Properties: query, edit
        imageName (Queryable[str]?): Set the base name of the image files.  
                Properties: query, edit
        imageSize (Queryable[Tuple[int, int, float]]?): Set the image output size. Takes width, height and aspect ratio.  
                Pass 0,0,0 to use current port size. The image size must be equal to  
                or greater then the viewport size. Large images will be tiled if full  
                resolution rendering has been enabled (-fr/fullResolution).  
                Properties: query, edit
        lightIcons (bool?): Set display status of light icons.  
                Properties: query, edit
        lightingMode (Queryable[str]?): Set the lighting mode used for rendering: all, selected, default.  
                Properties: query, edit
        lineSmoothing (bool?): Enable/disable anti-aliased lines.  
                Properties: query, edit
        offScreen (bool?): When set, this toggle allow HRM to use an offscreen buffer  
                to render the view. This allows HRM to work when the application  
                is iconified, or obscured  
                Properties: query, edit
        renderFrame (Queryable[str]?): Render the current frame. Requires the name of the view in  
                which to render.  
                Properties: query, edit
        renderSequence (Queryable[str]?): Render the current frame sequence. Requires the name of the  
                view in which to render.  
                Properties: query, edit
        sharpness (Queryable[float]?): Control the sharpness level of the convolution filter.  
                Properties: query, edit
        shutterAngle (Queryable[float]?): Set the shutter angle used for motion blur (0. 1). A value  
                of 0.0 gives no blurring, 0.5 gives correct blurring, and 1.0  
                gives continuous blurring. Must enable the accumulation buffer.  
                Properties: query, edit
        textureDisplay (bool?): Enable/disable texture map display.  
                Properties: query, edit
        transformIcons (bool?): Set display status of transform icons.  
                Properties: query, edit
        useAccumBuffer (bool?): Enable/disable the accumulation buffer.  
                Properties: query, edit
        viewport (Queryable[Tuple[int, int, float]]?): Set the viewport size. Pass in the width, height and aspect ratio.  
                This size will be used for all test rendering and image output size  
                unless full resolution (-fr) has been set and a valid image output  
                size (-is) has been set.  
                Properties: query, edit
        writeDepthMap (bool?): Enable/disable writing of zdepth to image files.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

