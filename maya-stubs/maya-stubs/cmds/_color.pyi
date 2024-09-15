from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def color(*args: str, rgbColor: Tuple[float, float, float] = ..., userDefined: int = ...) -> bool:
    """This command sets the dormant wireframe color of the specified
    objects to be their class color or if the -ud/userDefined flag is
    specified, one of the user defined colors. The -rgb/rgbColor flags
    can be specified if the user requires floating point RGB colors.
    Args:
        rgbColor (Tuple[float, float, float]?): Specifies and rgb color to set the selected object to.  
                Properties: create
        userDefined (int?): Specifies the user defined color index to set selected  
                object to. The valid range of numbers is [1. 8].  
                Properties: create

    Returns:
        bool:

    Example:
    """

