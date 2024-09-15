from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def psdTextureFile(*args: Any, channelRGB: Multiuse[Tuple[str, int, int, int, int]] = ..., channels: Multiuse[Tuple[str, int, bool]] = ..., imageFileName: Multiuse[Tuple[str, str, int]] = ..., psdFileName: str = ..., snapShotImageName: str = ..., uvSnapPostionTop: bool = ..., xResolution: int = ..., yResolution: int = ...) -> bool:
    """Creates a Photoshop file with UVSnap shot image and the layer set
    names as the input.
    Args:
        channelRGB (Multiuse[Tuple[str, int, int, int, int]]?): (M) Layer set names, index, red, green and blue values are given as input.  
                Using this flag, the layers created can be filled with specified  
                colors.  This is a multi use flag.  The index specifies the  
                placement order of layer sets in the created file.  
                Properties: create, multiuse
        channels (Multiuse[Tuple[str, int, bool]]?): (M) Layer set names and index are given as input. This is a multi use flag.  
                A layer set with the given name will be created.  The second argument  
                is the index which specifies the placement order of layer sets  
                in the created file. The third argument is a boolean, if "true" a layer  
                is created inside the layer set , "false" creates an  empty layer set  
                Properties: create, multiuse
        imageFileName (Multiuse[Tuple[str, str, int]]?): Image file name, Layerset name and index.  The image in the file will be  
                transferred to layer set specified.  The index specifies the  
                placement order of layer sets in the created psd file.  The image file  
                specified can be in any of the formats supported by maya  
                (ex. iff, jpg, gif, tif etc.)  
                Properties: create, multiuse
        psdFileName (str?): PSD file name.  
                Properties: create
        snapShotImageName (str?): Image file name on the disk containing UV snapshot / reference image.  
                Properties: create
        uvSnapPostionTop (bool?): Specifies the position of UV snapshot image layer  in the PSD file. "True"  
                positions this layer at the top and "False" positions the layer at the bottom  
                next to the background layer in the PSD file  
                Properties: create
        xResolution (int?): X - resolution of the image.  
                Properties: create
        yResolution (int?): Y - resolution of the image.  
                Properties: create

    Returns:
        bool:

    Example:
    """

