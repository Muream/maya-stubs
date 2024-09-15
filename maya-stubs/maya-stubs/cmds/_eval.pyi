from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def eval(arg0: str = ..., /) -> Any:
    """This function takes a string which contains MEL code and evaluates it
    using the MEL interpreter. The result is converted into a Python data type
    and is returned. If an error occurs during the execution of the MEL
    script, a Python exception is raised with the appropriate error message.
    Returns:
        Any: depending on input.

    Example:
    """

