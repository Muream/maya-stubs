from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def effector(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., hide: bool = ..., name: Queryable[str] = ...) -> Union[str, bool]:
    """The effector command is used to set the name or hidden
    flag for the effector.  The standard edit (-e) and query (-q) flags are
    used for edit and query functions.
    Args:
        hide (bool?): Specifies whether to hide drawing of effector  
                if attached to a handle.  
                Properties: create, query, edit
        name (Queryable[str]?): Specifies the name of the effector.  
                Properties: create, query, edit

    Returns:
        str: Command result

    Example:
    """

