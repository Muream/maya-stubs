from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def doBlur(*, colorFile: str = ..., length: float = ..., memCapSize: float = ..., sharpness: float = ..., smooth: float = ..., smoothColor: bool = ..., vectorFile: str = ...) -> str:
    """The doBlur command  will invoke the blur2d, which is a Maya
    stand-alone application to do 2.5 motion blur given the color image
    and the motion vector file.  For a given input colorFile name, e.g.
    "xxx.iff", the output blurred image will be "xxx_blur.iff" in the
    same directory as the input colorFile.  There is currently no control
    over the name of the output blurred image.
    Args:
        colorFile (str?): Name of the input color image to be blurred.  
                Properties: create
        length (float?): Scale applied on the motion vector. Ranges from 0 to infinity.  
                Properties: create
        memCapSize (float?): Size of the memory cap, in bytes  
                Properties: create
        sharpness (float?): Determines  the shape of the blur filter. The higher the value,  
                the narrower the filter, the sharper the blur. The lower the value,  
                the wider the filter, the more spread out the blur.  
                Ranges from 0 to infinity.  
                Properties: create
        smooth (float?): Filter size to smooth the blurred image. The higher the value,  
                the more anti-aliased the alpha channel. Ranges from 1.0 to 5.0.  
                Properties: create
        smoothColor (bool?): Whether to smooth the color or not.  
                Properties: create
        vectorFile (str?): Name of the input motion vector file.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

