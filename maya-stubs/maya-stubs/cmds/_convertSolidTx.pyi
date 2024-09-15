from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def convertSolidTx(*args: str, edit: bool = ..., query: bool = ..., alpha: bool = ..., antiAlias: bool = ..., backgroundColor: Tuple[int, int, int] = ..., backgroundMode: str = ..., camera: str = ..., componentRange: bool = ..., doubleSided: bool = ..., fileFormat: str = ..., fileImageName: str = ..., fillTextureSeams: bool = ..., force: bool = ..., fullUvRange: bool = ..., name: str = ..., pixelFormat: str = ..., resolutionX: int = ..., resolutionY: int = ..., reuseDepthMap: bool = ..., samplePlane: bool = ..., samplePlaneRange: Tuple[float, float, float, float] = ..., shadows: bool = ..., uvBBoxIntersect: bool = ..., uvRange: Tuple[float, float, float, float] = ..., uvSetName: str = ...) -> List[str]:
    """Command to convert a texture on a surface to a file texture. The first
    argument is a rendering node or attribute. If only the node is
    specified, the outColor attribute will be sampled. If the node does
    not have an outColor attribute, the first attribute on the node which
    is: readable, not writable, not hidden, connectable, and not a multi
    is used. If lighting is to be baked, a shading group must be specified
    as the texture.The current selection will be used if a texture and surface are not
    specified.An image file will be generated for each object and stored in your
    image segment of your project. The filename will be formatted using
    the texture and surface names as follows:However, if force is off and there is a name collision a version
    number will be determined and the filename will be formatted as
    follows:If uv/uvsetName option is specified the filename will include
    {surface}-{uvname} instead of {surface}.
    Args:
        alpha (bool?): Specify whether to compute the transparency when baking  
                lighting. The conversion will sample both the color and  
                transparency of the shading network; the alpha channel of the  
                file texture will be set to correspond to the result from sampling  
                the transparency. By default transparency is not computed.  
                Properties: create
        antiAlias (bool?): Perform anti-aliasing on the resulting image. Convert solid  
                texture will generally take four times longer than without  
                anti-aliasing. By default this flag is off.  
                Properties: create
        backgroundColor (Tuple[int, int, int]?): Set the background color to a specific value. Default is to  
                use the shader default color to fill the background. Valid  
                values range from 0 to 255 if the pixel format is 8 bits per channel,  
                or 0 to 65535 if the pixel format is 16 bits per channel.  
                This flag automatically sets -backgroundMode to "color".  
                Default is black: 0 0 0.  
                Properties: create
        backgroundMode (str?): Defines how the background of the texture should be  
                filled. Three modes are available:  
                "shader" or 1. uses the default shader color.  
                "color" or 2. uses the color given by  
                -backgroundColor flag.  
                "extend" or 3. extends outwards the color along the  
                seam edges.  
                Default is "shader".  
                Properties: create
        camera (str?): Specify a camera to use in baking lighting. If a camera is not  
                specified the camera in the active view will be used.  
                Properties: create
        componentRange (bool?): If one or more components have been selected to use, then  
                if this flag is set, then the uv range of the components  
                is used to fit into the texture map resolution. By default this  
                flag is set to false.  
                Properties: create
        doubleSided (bool?): Specify whether the sampler should flip the surface normal if the  
                sample point faces away from the camera. Note: flipping the normal  
                will make the result dependent on the camera (ie. one camera may  
                flip normals where different camera wouldn't). It's not recommended  
                that doubleSided be used in combination with shadows. By default  
                this flag is false.  
                Properties: create
        fileFormat (str?): File format to be used for output. IFF is the default if  
                unspecified. Other valid formats are:  
                als: Alias PIX  
                cin: Cineon  
                eps: EPS  
                gif: GIF  
                iff: Maya IFF  
                jpg: JPEG  
                yuv: Quantel  
                rla: Wavefront RLA  
                sgi: SGI  
                si: SoftImage (.pic)  
                tga: Targa  
                tif: TIFF  
                bmp: Windows Bitmap  
                Properties: create
        fileImageName (str?): Specify the output path and name of file texture image. If the  
                file name doesn't contain a directory separator, the image  
                will be written to source images of the current project. The  
                file will not be versioned if it already exists.  
                Properties: create
        fillTextureSeams (bool?): Specify whether or not to overscan the polygon beyond its outer  
                edges, when creating the file texture, in order to fill the texture  
                seams.  
                Default is true.  
                Properties: create
        force (bool?): If the output image already exists overwrite it. By default  
                this flag is off.  
                Properties: create
        fullUvRange (bool?): Sample using the full uv range of the surface. This flag  
                cannot be used with the -uvr flag. A 2D texture placement node  
                will be created and connected to the file texture. The placement's  
                translate and coverage will be set according to the full UV range of  
                the surface.  
                Properties: create
        name (str?): Set the name of the file texture node. Name conflict  
                resolution will be used to determine valid names when multiple  
                objects are specified.  
                Properties: create
        pixelFormat (str?): Specifies the pixel format of the image.  
                Note that not all file formats support all pixel formats.  
                Available options:  
                "8": 8 bits per channel, unsigned (0. 255)  
                "16": 16 bits per channel, unsigned (0. 65535)  
                Default is "8".  
                Properties: create
        resolutionX (int?): Set the horizontal image resolution. If this flag  
                is not specified, the resolution will be set to 256.  
                Properties: create
        resolutionY (int?): Set the vertical image resolution. If this flag  
                is not specified, the resolution will be set to 256.  
                Properties: create
        reuseDepthMap (bool?): Specify whether or not to reuse all the generated dmaps.  
                Default is false.  
                Properties: create
        samplePlane (bool?): Specify whether to sample using a virtual plane. This virtual plane  
                has texture coordinates in the rectangle defined by the  
                -samplePlaneRange flag. If the -samplePlaneRange flag is not set then  
                the virtual plane defaults to having texture coordinates in the  
                (0,0) to (1,1) square. If this option is set than all surface based  
                arguments will be ignored.  
                Properties: create
        samplePlaneRange (Tuple[float, float, float, float]?): Specify the uv range of the texture coordinates used to sample if  
                the -samplePlane option is set. There are four arguments corresponding  
                to uMin, uMax, vMin and vMax. By default the virtual plane is from  
                uMin 0 to uMax 1, and vMin 0 to vMax 1.  
                Properties: create
        shadows (bool?): Specify whether to compute shadows when baking lighting. Disk based  
                shadow maps will be used. Only lights with depth map shadows enabled  
                will contribute to the shading. By default shadows are not computed.  
                Properties: create
        uvBBoxIntersect (bool?): This flag is obsolete.  
                Properties: create
        uvRange (Tuple[float, float, float, float]?): Specify the uv range in which samples will be computed. There are  
                four arguments corresponding to uMin, uMax, vMin and vMax. Each  
                value should be specified based on the surface's uv space. A 2D  
                texture placement node will be created and connected to the file  
                texture. The placement's frame translate and coverage will be set  
                according to the uv range specified. By default the entire uv range  
                of the surface will be used.  
                Properties: create
        uvSetName (str?): Specify which uv set has to be used as the driving parametrization  
                for convert solid.  
                Properties: create

    Returns:
        List[str]: File texture nodes

    Example:
    """

