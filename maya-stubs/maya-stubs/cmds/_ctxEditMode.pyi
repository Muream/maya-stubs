from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ctxEditMode(*, buttonDown: bool = ..., buttonUp: bool = ...) -> bool:
    """This command tells the current context to switch edit modes.It acts as a toggle.
    Args:
        buttonDown (bool?): Edit mode is being invoked from a hotkey press event.  
                Properties: create
        buttonUp (bool?): Edit mode is being invoked from a hotkey release event.  
                Properties: create

    Returns:
        bool:

    Example:
    """

