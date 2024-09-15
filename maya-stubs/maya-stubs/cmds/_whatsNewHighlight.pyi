from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def whatsNewHighlight(*, query: bool = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., highlightOn: bool = ..., showStartupDialog: bool = ...) -> Union[bool, Tuple[float, float, float]]:
    """This command is used to toggle the What's New highlighting feature,
    and the display of the settings dialog for the feature that appears
    on startup.
    Args:
        highlightColor (Queryable[Tuple[float, float, float]]?): Set the color of the What's New highlight. The arguments correspond to  
                the red, green, and blue color components. Each color component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query
        highlightOn (bool?): Toggle the What's New highlighting feature. When turned on, menu items  
                and buttons introduced in the latest version will be highlighted.  
                Properties: create, query
        showStartupDialog (bool?): Set whether the settings dialog for this feature appears on startup.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

