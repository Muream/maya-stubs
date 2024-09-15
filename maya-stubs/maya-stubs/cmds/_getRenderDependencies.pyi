from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getRenderDependencies(arg0: str = ..., /) -> str:
    """Command to return dependencies of an image source.  Image sources (such
    as render targets) can depend on other upstream image sources that result
    from renderings of 3D scene, or renderings of 2D compositing graphs.
    This command returns these dependencies, so that they can be analyzed and
    rendered.image, source, dependencies
    Returns:
        str: Dependencies for argument image source

    Example:
    """

