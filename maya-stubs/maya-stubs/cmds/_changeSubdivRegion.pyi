from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def changeSubdivRegion(*args: Any, action: int = ..., level: int = ...) -> bool:
    """Changes a subdivision surface region based on the command parameters.
    The command operates on the selected subdivision surfaces.subdivision, surface, select, region
    Args:
        action (int?): Specifies the action to the selection region  
                     1 = delete selection region  
                     2 = enlarge selection region  
                Properties: create
        level (int?): Specify the level of the subdivision surface to perform the operation  
                Properties: create

    Returns:
        bool: Command result

    Example:
    """

