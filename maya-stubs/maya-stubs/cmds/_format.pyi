from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def format(arg0: str = ..., /, *, stringArg: Multiuse[str] = ...) -> str:
    """This command takes a format string, where the format string contains
    format specifiers.  The format specifiers have a number associated
    with them relating to which parameter they represent to allow for
    alternate ordering of the passed-in values for other
    languages by merely changing the format stringformat, string
    Args:
        stringArg (Multiuse[str]?): Specify the arguments for the format string.  
                Properties: create, multiuse

    Returns:
        str: Command result

    Example:
    """

