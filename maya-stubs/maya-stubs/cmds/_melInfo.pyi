from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def melInfo() -> List[str]:
    """This command returns the names of all global MEL procedures that are currently
    defined as a string array. The user can query the definition of each MEL
    procedure using the "whatIs" command.mel
    Returns:
        List[str]: procedure names

    Example:
    """

