from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def removeJoint(*args: str) -> bool:
    """This command will remove the selected joint or the joint given at the
    command line from the skeleton.The given (or selected) joint should not be the root joint of the skeleton,
    and not have skin attached. The command works on the given (or selected)
    joint. No options or flags are necessary.
    Returns:
        bool:

    Example:
    """

