from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def disconnectAttr(arg0: str = ..., arg1: str = ..., /, *, nextAvailable: bool = ...) -> str:
    """Disconnects two connected attributes. First argument is the source
    attribute, second is the destination.
    Args:
        nextAvailable (bool?): If the destination multi-attribute has set the indexMatters  
                to be false, the command will disconnect the first matching  
                connection.  No index needs to be specified.  
                Properties: create

    Returns:
        str: A phrase containing the names of the disconnected attributes.

    Example:
    """

