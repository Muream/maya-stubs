from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderSettings(*args: Any, camera: str = ..., customTokenString: str = ..., firstImageName: bool = ..., fullPath: bool = ..., fullPathTemp: bool = ..., genericFrameImageName: str = ..., imageGenericName: bool = ..., lastImageName: bool = ..., layer: str = ..., leaveUnmatchedTokens: bool = ...) -> List[str]:
    """Query interface to the common tab of the render settingsrender, settings
    Args:
        camera (str?): Specify a camera that you want to replace the current renderable camera  
                Properties: create
        customTokenString (str?): Specify a custom key-value string to use to replace custom tokens in  
                the file name. Use with firstImageName or lastImageName. Basic tokens  
                (Scene, Layer, RenderLayer, Camera, Version, Extension) will be  
                automatically expanded. Any other tokens must be specified here to  
                be expanded.  
                The format of the string is a space separated list of tokens-value pairs.  
                For example, if the file name string is "myFile_<myToken>_<myOtherToken>_v"  
                then the argument to this flag string should take the form  
                "myToken=myTokenValue myOtherToken=myOtherTokenValue".  
                Properties: create
        firstImageName (bool?): Returns the first image name  
                Properties: create
        fullPath (bool?): Returns the full path for the image using the current project. Use with  
                firstImageName, lastImageName, or genericFrameImageName.  
                Properties: create
        fullPathTemp (bool?): Returns the full path for the preview render of the image using the current  
                project. Use with firstImageName, lastImageName, or genericFrameImageName.  
                Properties: create
        genericFrameImageName (str?): Returns the generic frame image name with the custom specified frame  
                index token  
                Properties: create
        imageGenericName (bool?): Returns the image generic name  
                Properties: create
        lastImageName (bool?): Returns the last image name  
                Properties: create
        layer (str?): Specify a render layer name that you want to replace the current render layer  
                Properties: create
        leaveUnmatchedTokens (bool?): Do not remove unmatched tokens from the name string. Use with  
                firstImageName or lastImageName.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

