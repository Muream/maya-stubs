from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filterInstances(*args: str, query: bool = ..., shapes: bool = ...) -> List[str]:
    """This command filters the selection list to remove duplicate instances
    that refer to the same object/components. If any such instances are
    found they will be merged with the first selected instance.Returns a string array containing all matching selection items or
    true/false if the query flag is used.
    Args:
        shapes (bool?): If this is true then the command will check for an instanced shapes  
                below the selected transform(s) and use them to decide whether the  
                parent transforms should be considered instances. Default is false.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

