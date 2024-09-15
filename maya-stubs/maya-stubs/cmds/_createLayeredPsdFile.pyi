from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def createLayeredPsdFile(*args: Any, imageFileName: Multiuse[Tuple[str, str, str]] = ..., psdFileName: str = ..., xResolution: int = ..., yResolution: int = ...) -> bool:
    """Creates a  layered PSD file with image names as input to individual layers
    Args:
        imageFileName (Multiuse[Tuple[str, str, str]]?): Layer name, blend mode, Image file name  The image in the file will be  
                transferred to layer specified. The image file specified can be in any  
                of the formats supported by maya (ex. iff, jpg, gif, tif etc.). The blend  
                mode options are : "Normal", "Dissolve", "Dark", "Multiply", "Color Burn",  
                "Linear Burn", "Lighten", "Screen", "Color Dodge", "Linear Dogde", "Overlay",  
                "Soft Light", "Hard Light", "Dissolve", "Vivid Light", "Linear Light", "Pin Light",  
                "Hard Mix", "Difference", "Exclusion", "Hue", "Saturation", "Color",  "Luminosity"  
                Properties: create, multiuse
        psdFileName (str?): PSD file name.  
                Properties: create
        xResolution (int?): X - resolution of the image.  
                Properties: create
        yResolution (int?): Y - resolution of the image.  
                Properties: create

    Returns:
        bool:

    Example:
    """

