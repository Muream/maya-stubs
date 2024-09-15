from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCollapseTweaks(arg0: str = ..., /, *, query: bool = ..., hasVertexTweaks: bool = ...) -> bool:
    """A command that updates a mesh's vertex tweaks by applying its tweak data
    (stored on the mesh node) onto its respective vertex data.This command is only useful in cases where no construction history is associated
    with the shape node.If a mesh name is not specified as input, a singly selected mesh (if any) will
    have its tweaked vertices baked.
    Args:
        hasVertexTweaks (bool?): Determines whether an individual mesh has vertex tweaks.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

