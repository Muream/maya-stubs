from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def querySubdiv(*args: Any, action: int = ..., level: int = ..., relative: bool = ...) -> bool:
    """Queries a subdivision surface based on a set of query parameters and updates the selection list with the results.subdivision, surface, query
    Args:
        action (int?): Specifies the query parameter:  
                        1 = find all tweaked verticies at level  
                        2 = find all sharpened vertices at level  
                        3 = find all sharpened edges at level  
                        4 = find all faces at level  
                If the attribute "level" is not specified then the query is applied to  
                the current component display level. If the attribute level is  
                specified then the query is applied to that level, either absolute or  
                relative to the current level based on the "relative" flag state.  
                Properties: create
        level (int?): Specify the level of the subdivision surface on which to perform the operation.  
                Properties: create
        relative (bool?): If set, level flag refers to the level relative to the current component display level.  
                Properties: create

    Returns:
        bool: Command result

    Example:
    """

