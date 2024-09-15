from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def render(arg0: str = ..., /, *args: str, abortMissingTexture: bool = ..., batch: bool = ..., keepPreImage: bool = ..., layer: str = ..., nglowpass: bool = ..., nshadows: bool = ..., replace: bool = ..., xresolution: int = ..., yresolution: int = ...) -> str:
    """The render command is used to start off a MayaSoftware rendering
    session of the currently active camera. If a rendering is already
    in progress, then this command stops the rendering. This command is
    not undoable.
    Args:
        abortMissingTexture (bool?): Abort renderer when encountered missing texture. Only  
                available when -batch is set  
                Properties: create
        batch (bool?): Run in batch mode. Compute the images for all renderable  
                cameras. This is the mel equivalent of running maya in batch  
                mode with the -render flag set. All other flags are ignored  
                when -batch is used.  
                Properties: create
        keepPreImage (bool?): Keep the renderings prior to post-process around. Only  
                available when -batch is set  
                Properties: create
        layer (str?): Render the specified render layer.  
                Only this render layer will be rendered,  
                regardless of the renderable attribute value of the render layer.  
                The layer name will be appended to the output image file name.  
                The specified render layer becomes the current render layer before rendering,  
                and remains as current render layer after the rendering.  
                Properties: create
        nglowpass (bool?): Overwrite glow pass capabilities (can turn off glow pass globally  
                by setting this value to false)  
                Properties: create
        nshadows (bool?): Shadowing capabilities (can turn off shadow globally  
                by setting this value to false)  
                Properties: create
        replace (bool?): Replace the rendered image if it already exists. Only  
                available when -batch is set  
                Properties: create
        xresolution (int?): Overwrite x resolution  
                Properties: create
        yresolution (int?): Overwrite y resolution  
                Properties: create

    Returns:
        str: The name of the rendered image.

    Example:
    """

