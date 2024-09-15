from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def connectJoint(arg0: str = ..., arg1: str = ..., /, *, connectMode: bool = ..., parentMode: bool = ...) -> bool:
    """This command will connect two skeletons based on the two selected joints.
    The first selected joint can be made a child of the parent of the second
    selected joint or a child of the second selected joint, depending on
    the flags used.Note1: The first selected joint must be the root of a skeleton.
    The second selected joint must have a parent.Note2: If a joint name is specified in the command line, it is used as the
    child and the first selected joint will be the parent. If no joint
    name is given at the command line, two joints must be selected.
    Args:
        connectMode (bool?): The first selected joint will be parented under the parent of the  
                second selected joint.  
                Properties: create
        parentMode (bool?): The first selected joint will be parented under the second selected  
                joint. Both joints will be in the active list(selection list).  
                Properties: create

    Returns:
        bool:

    Example:
    """

