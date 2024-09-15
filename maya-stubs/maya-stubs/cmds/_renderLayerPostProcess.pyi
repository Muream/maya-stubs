from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderLayerPostProcess(*, query: bool = ..., keepImages: bool = ..., sceneName: Queryable[str] = ...) -> Union[bool, str]:
    """Post process the results when rendering is done with. Presently this
    generates a layered PSD file using individual iff files.renderlayers, psd, photoshop
    Args:
        keepImages (bool?): When set to on, the original iff images are kept after the conversion to PSD.  
                Default is to remove them.  
                Properties: create, query
        sceneName (Queryable[str]?): Specifies the scene name for interactive batch rendering.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

