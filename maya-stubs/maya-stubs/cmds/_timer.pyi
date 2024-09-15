from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timer(*, endTimer: bool = ..., lapTime: bool = ..., name: str = ..., startTimer: bool = ...) -> bool:
    """Allow simple timing of scripts and commands. The resolution of this timer
    is at the level of your OS'sfunction.This command does not handle stacked calls. For
    example, this code below will give an incorrect answer on the
    secondcall.To do this use named timers:debug, timer
    Args:
        endTimer (bool?): Stop the timer and return the time elapsed since the timer was  
                started (in seconds). Once a timer is turned off it no longer exists,  
                though it can be recreated with a new start  
                Properties: create
        lapTime (bool?): Get the lap time of the timer (time elapsed since start in seconds).  
                Unlike the end flag this keeps the timer running.  
                Properties: create
        name (str?): Use a named timer for the operation. If this is omitted then the default  
                timer is assumed.  
                Properties: create
        startTimer (bool?): Start the timer.  
                Properties: create

    Returns:
        bool:

    Example:
    """

