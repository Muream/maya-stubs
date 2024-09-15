from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def volumeBind(*, edit: bool = ..., query: bool = ..., influence: Queryable[str] = ..., name: str = ...) -> Union[List[str], str]:
    """Command for creating and editing volume binding nodes.
    The node is use for storing volume data to define skin weighting data.
    Args:
        influence (Queryable[str]?): Edit or Query the list of influences connected to the skin cluster.  
                Properties: query, edit
        name (str?): Used to specify the name of the node being created.  
                Properties: create

    Returns:
        List[str]: List of queried influences

    Example:
    """

