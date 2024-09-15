from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def uvSnapshot(*args: str, antiAliased: bool = ..., blueColor: int = ..., entireUVRange: bool = ..., fileFormat: str = ..., greenColor: int = ..., name: str = ..., overwrite: bool = ..., redColor: int = ..., uMax: float = ..., uMin: float = ..., uvSetName: str = ..., vMax: float = ..., vMin: float = ..., xResolution: int = ..., yResolution: int = ...) -> bool:
    """Builds an image containg the UVs of the selected objects.texture, uv, image
    Args:
        antiAliased (bool?): When this flag is set, lines are antialiased.  
                Properties: create
        blueColor (int?): Blue component of line drawing. Default is 255.  
                Properties: create
        entireUVRange (bool?): When this flag is set, the generated image will contain the entire uv range. Default is UV in 0. 1 range.  
                Properties: create
        fileFormat (str?): Output file format. Any of those keyword:  
                                                "iff", "sgi", "pic", "tif", "als", "gif", "rla", "jpg"  
                        Default is iff.  
                Properties: create
        greenColor (int?): Green component of line drawing. Default is 255.  
                Properties: create
        name (str?): Name of the file to be created.  
                Properties: create
        overwrite (bool?): When this flag is set, existing file can be ovewritten.  
                Properties: create
        redColor (int?): Red component of line drawing. Default is 255.  
                Properties: create
        uMax (float?): Optional User Specified Max value for U. Default value is 1. This will take precedence over the "entire range" -euv flag.  
                Properties: create
        uMin (float?): Optional User Specified Min value for U. Default value is 0. This will take precedence over the "entire range" -euv flag.  
                Properties: create
        uvSetName (str?): Name of the uv set to use. Default is the current one.  
                Properties: create
        vMax (float?): Optional User Specified Max value for V. Default value is 1. This will take precedence over the "entire range" -euv flag.  
                Properties: create
        vMin (float?): Optional User Specified Min value for V. Default value is 0. This will take precedence over the "entire range" -euv flag.  
                Properties: create
        xResolution (int?): Horizontal size of the image. Default is 512.  
                Properties: create
        yResolution (int?): Vertical size of the image. Default is 512.  
                Properties: create

    Returns:
        bool:

    Example:
    """

