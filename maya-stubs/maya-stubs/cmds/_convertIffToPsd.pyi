from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def convertIffToPsd(*, query: bool = ..., iffFileName: Queryable[str] = ..., psdFileName: Queryable[str] = ..., xResolution: Queryable[int] = ..., yResolution: Queryable[int] = ...) -> Union[bool, str, int]:
    """Converts iff file to PSD file of given sizerenderlayers, psd, photoshop
    Args:
        iffFileName (Queryable[str]?): Input iff file name  
                Properties: create, query
        psdFileName (Queryable[str]?): Output file name  
                Properties: create, query
        xResolution (Queryable[int]?): X resolution of the image  
                Properties: create, query
        yResolution (Queryable[int]?): Y resolution of the image  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

