from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def convertUnit(*args: str, fromUnit: str = ..., toUnit: str = ...) -> float:
    """This command converts values between different units of measure.  The
    command takes a string, because a string can incorporate unit
    names as well as values (see examples).
    Args:
        fromUnit (str?): The unit to convert from.  If not supplied, it is assumed to be the  
                system default.  The from unit may also be supplied as part of the  
                value e.g. 11.2m (11.2 meters).  
                Properties: create
        toUnit (str?): The unit to convert to.  If not supplied, it is assumed to be the  
                system default  
                Properties: create

    Returns:
        float: or string

    Example:
    """

