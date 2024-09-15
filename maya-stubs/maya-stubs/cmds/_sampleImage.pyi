from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sampleImage(*args: Any, fastSample: bool = ..., resolution: Tuple[int, str] = ...) -> bool:
    """The sampleImage command is used to control parameters of
    sample images, such as swatches in the multilister.
    The fast option turns on or off some rendering cheats which speed up the
    render but may cause edges to look ragged.
    The resolution option specifies the width in pixels of the image which will
    be rendered for the specified node. Note that the width of the image
    is also the height of the image since sample images are square.
    Args:
        fastSample (bool?): If fast but rough rendering for sampleImage is to be used  
                Properties: create
        resolution (Tuple[int, str]?): The first argument to this flag specifies a resolution in pixels.  
                The second argument specifies a dependency node. The effect of this  
                flag is that further sample image renderings for the specified node  
                will be made at the specified resolution.  
                Properties: create

    Returns:
        bool:

    Example:
    """

