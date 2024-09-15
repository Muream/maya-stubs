from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def evalDeferred(arg0: Callable[..., Any] = ..., /, *, evaluateNext: bool = ..., list: bool = ..., lowPriority: bool = ..., lowestPriority: bool = ...) -> List[str]:
    """This command takes the string it is given and evaluates it
    during the next available idle time.  It is useful for attaching
    commands to controls that can change or delete the control.
    Args:
        evaluateNext (bool?): Specified that the command to be executed should be ran with the  
                highest priority, ideally queued up next.  
                Properties: create
        list (bool?): Return a list of the command strings that are currently pending on  
                the idle queue. By default, it will return the list of commands for all  
                priorities. The -lowestPriority and -lowPriority can be used to  
                restrict the list of commands to a given priority level.  
                Properties: create
        lowPriority (bool?): Specified that the command to be executed should be deferred with the  
                low priority. That is, it will be executed whenever Maya is idle.  
                Properties: create
        lowestPriority (bool?): Specified that the command to be executed should be deferred with the  
                lowest priority. That is, it will be executed when no other idle  
                events are scheduled.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

