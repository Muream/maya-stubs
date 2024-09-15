from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def reloadImage(arg0: str = ..., arg1: str = ..., /) -> bool:
    """This command reloads an xpm image from disk. This can be used when the
    file has changed on disk and needs to be reloaded.The first string argument is the file name of the .xpm file. The
    second string argument is the name of a control using the specified
    pixmap.
    Returns:
        bool: True if image is successfully loaded, false otherwise.

    Example:
    """

