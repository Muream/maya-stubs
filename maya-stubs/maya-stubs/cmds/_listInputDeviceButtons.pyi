from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listInputDeviceButtons(*args: Any) -> List[str]:
    """This command lists all of the buttons of the specified
    input device specified as an argument.
    Returns:
        List[str]: Command result

    Example:
    """

