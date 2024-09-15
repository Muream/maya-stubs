from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikfkDisplayMethod(*, query: bool = ..., display: Queryable[str] = ...) -> Union[bool, str]:
    """Thecommand is used to specify how ik/fk
          blending should be shownikfk
    Args:
        display (Queryable[str]?): Specify how ik/fk blending should be shown when the handle is selected.  
                Possible choices are "none" (do not display any blending), "ik" (only  
                show ik),"fk" (only show fk), and "ikfk" (show both ik and fk).  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

