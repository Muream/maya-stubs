from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def particleExists(*args: str) -> bool:
    """This command is used to query if a particle or soft object with
    the given name exists. Either the transform or shape name can be used
    as well as the name of the soft object.
    Returns:
        bool: True if there is a particle object or soft object by the given
            name, false otherwise.

    Example:
    """

