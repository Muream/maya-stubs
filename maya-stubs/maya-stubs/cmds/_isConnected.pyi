from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def isConnected(arg0: str = ..., arg1: str = ..., /, *, ignoreUnitConversion: bool = ...) -> bool:
    """Thecommand is used to check if two plugs are
    connected in the dependency graph. The return value isif they are not andif they are.The first string specifies the source plug to check for connection.The second one specifies the destination plug to check for connection.
    Args:
        ignoreUnitConversion (bool?): In looking for connections, skip past unit conversion nodes.  
                Properties: create

    Returns:
        bool: Are the two plugs connected?

    Example:
    """

