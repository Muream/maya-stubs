from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def frameBufferName(*, autoTruncate: bool = ..., camera: str = ..., renderLayer: str = ..., renderPass: str = ...) -> str:
    """Returns the frame buffer name for a given renderPass renderLayer and
    camera combination. Optionally, this command can apply a name truncation
    algorithm so that the frameBuffer name will respect the maximum length
    imposed by the destination file format, if applicable.render, pass
    Args:
        autoTruncate (bool?): use this flag to apply a name truncation algorithm so that the frameBuffer  
                name will respect the maximum length imposed by the destination file format,  
                if applicable.  
                Properties: create
        camera (str?): Specify a camera  
                Properties: create
        renderLayer (str?): Specify a renderer layer  
                Properties: create
        renderPass (str?): Specify a renderer pass  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

