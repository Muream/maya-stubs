from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def condition(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., delete: bool = ..., dependency: Multiuse[str] = ..., initialize: bool = ..., script: str = ..., state: bool = ...) -> bool:
    """This command creates a new named condition object whose true/false
    value is calculated by running a mel script. This new condition can
    then be used for dimming, or controlling other scripts, or whatever.
    Args:
        delete (bool?): Deletes the condition.  
                Properties: create
        dependency (Multiuse[str]?): Each -dependency flag specifies another condition that the  
                new condition will be dependent on.  When any of these conditions  
                change, the new-state-script will run, and the state of this  
                condition will be set accordingly.  It is possible to define infinite loops,  
                but they will be caught and handled correctly at run-time.  
                Properties: create, multiuse
        initialize (bool?): Initializes the condition, by forcing it to run its script  
                as soon as it is created.  If this flag is not specified, the  
                script will not run until one of the dependencies is triggered.  
                Properties: create
        script (str?): The script that determines the new state of  
                the condition.  
                Properties: create
        state (bool?): Sets the state of the condition. This can be used to create  
                a manually triggered condition: you could create a condition  
                without any dependencies and without a new-state-script. This  
                condition would only change state in response to the -st/state flag.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

