from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getModulePath(*, moduleName: str = ...) -> str:
    """Returns the module path for a given module name.module
    Args:
        moduleName (str?): The name of the module whose path you want to retrieve.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

