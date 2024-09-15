from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeCode(*, edit: bool = ..., query: bool = ..., mayaStartFrame: Queryable[float] = ..., productionStartFrame: Queryable[float] = ..., productionStartHour: Queryable[float] = ..., productionStartMinute: Queryable[float] = ..., productionStartSecond: Queryable[float] = ...) -> Union[int, float]:
    """Use this command to query and set the time code information in the filetimecode, time
    Args:
        mayaStartFrame (Queryable[float]?): Sets the Maya start time of the time code, in frames.  
                In query mode, returns the Maya start frame of the time code.  
                Properties: create, query, edit
        productionStartFrame (Queryable[float]?): Sets the production start time of the time code, in terms of frames.  
                In query mode, returns the sub-second frame of production start time.  
                Properties: create, query, edit
        productionStartHour (Queryable[float]?): Sets the production start time of the time code, in terms of hours.  
                In query mode, returns the hour of production start time.  
                Properties: create, query, edit
        productionStartMinute (Queryable[float]?): Sets the production start time of the time code, in terms of minutes.  
                In query mode, returns the minute of production start time.  
                Properties: create, query, edit
        productionStartSecond (Queryable[float]?): Sets the production start time of the time code, in terms of seconds.  
                In query mode, returns the second of production start time.  
                Properties: create, query, edit

    Returns:
        int: values

    Example:
    """

