from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def reroot(arg0: str = ..., /) -> bool:
    """This command will reroot a skeleton. The selected joint or the given joint
    at the command line will be the new    root of the skeleton. All ikHandles
    passing through the selected joint or above it will be deleted.The given(or selected) joint should not have skin attached. The    command
    works on the given or selected joint. No options or flags are necessary.
    Returns:
        bool:

    Example:
    """

