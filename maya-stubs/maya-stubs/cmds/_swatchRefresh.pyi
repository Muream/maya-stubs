from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def swatchRefresh(*args: str) -> bool:
    """Thecommand causes image source node swatches to be
    refreshed on screen.  The purpose of this command is to provide a mechanism
    to trigger a swatch refresh in cases that are not subject to dirty propagation
    in the dependency graph.  This command only works with imageSource-derived
    node types. Invoking this command with no arguments will cause all imageSource
    swatches to be refreshed.swatch, renderPass, renderLayer, renderTarget
    Returns:
        bool: true if all arguments are valid image source nodes and the operation succeded.

    Example:
    """

