from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getModifiers() -> int:
    """This command returns the current state of the modifier keys. The state
    of each modifier can be obtained by testing for the modifier's
    corresponding bit value in the return value. Shift is bit 1,
    Ctrl is bit 3, Alt is bit 4, and bit 5 is the 'Windows' key on Windows keyboards
    and the Command key on Mac keyboards.  See the provided
    example for more details on testing for each modifier's bit value.
    Returns:
        int: indicating which modifier keys are pressed.

    Example:
    """

