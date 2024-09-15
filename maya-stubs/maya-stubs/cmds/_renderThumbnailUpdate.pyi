from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderThumbnailUpdate(*args: Any, query: bool = ..., forceUpdate: str = ...) -> bool:
    """Toggle the updating of object thumbnails. These are visible in tools
    like the Attribute Editor and Hypershade. All thumbnails everywhere
    will not update to reflect changes to the object until this command is
    used to toggle to true unless a specific thumbnail is forced to render
    using the -forceUpdate flag.
    Args:
        forceUpdate (str?): Force the thumbnail to update.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

