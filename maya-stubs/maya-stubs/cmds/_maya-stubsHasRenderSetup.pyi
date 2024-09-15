from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def mayaHasRenderSetup(*, edit: bool = ..., query: bool = ..., enableCurrentSession: bool = ..., enableDuringTests: bool = ...) -> bool:
    """This command controls and queries render setup states.render, setup
    Args:
        enableCurrentSession (bool?): Enables or disables render setup for this Maya session only.  
                This flag should only be called during Maya intialization. This flag is for internal use only, may change at any time and is unsupported.  
                Properties: query, edit
        enableDuringTests (bool?): Switches render setup for this Maya session only, as legacy render layer mode is assumed during testing.  
                This flag is for internal use only, may change at any time and is unsupported.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

