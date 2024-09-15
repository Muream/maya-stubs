from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listNodeTypes(arg0: str = ..., /, *, exclude: str = ...) -> List[str]:
    """Lists dependency node types satisfying a specified classification string.See the 'getClassification' command for a list of the standard classification
    strings.
    Args:
        exclude (str?): Nodes that satisfies this exclude classification will be filtered out.  
                Properties: create

    Returns:
        List[str]: The type names of all node types in the system that satisfy the
            given classification string.

    Example:
    """

