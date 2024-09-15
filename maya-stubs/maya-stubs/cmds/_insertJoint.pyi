from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def insertJoint(arg0: str = ..., /) -> str:
    """This command will insert a new joint under the given or selected joint. If
    the given joint has child joints, they will be reparented under the new
    inserted joint.The given joint(or selected joint) should not have skin attached.
    The command works on the selected joint. No options or flags are necessary.
    Returns:
        str: The name of the new inserted joint

    Example:
    """

