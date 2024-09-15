from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def disconnectJoint(arg0: str = ..., /, *, attachHandleMode: bool = ..., deleteHandleMode: bool = ...) -> str:
    """This command will break a skeleton at the selected joint and delete
    any associated handles.
    Args:
        attachHandleMode (bool?): This flag is obsolete and no longer supported.  
                Properties: create
        deleteHandleMode (bool?): Delete the handle on the associated joint.  
                Properties: create

    Returns:
        str: After the joint is disconnected, a new joint will be created. The return value is the name of the newly created joint and its ancestor.

    Example:
    """

