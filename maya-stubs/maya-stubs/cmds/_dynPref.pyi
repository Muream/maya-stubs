from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynPref(*, query: bool = ..., autoCreate: bool = ..., echoCollision: bool = ..., runupFrom: Queryable[int] = ..., runupToCurrentTime: bool = ..., saveOnQuit: bool = ..., saveRuntimeState: bool = ...) -> Union[bool, int]:
    """This action modifies and queries the current state of "autoCreate
    rigid bodies", "run up to current time", and  "run up from"
    (previous time or start time).
    Args:
        autoCreate (bool?): If on, autoCreate rigid bodies.  
                Properties: create, query
        echoCollision (bool?): If on, will cause particle systems to echo to the Script Editor the  
                command that they are running for each particle collision event.  
                If off, only the output of the command will be echoed.  
                Properties: create, query
        runupFrom (Queryable[int]?): If on, run up from previous time; if 2, run up from start time  
                Properties: create, query
        runupToCurrentTime (bool?): If on, run up the scene to current time  
                Properties: create, query
        saveOnQuit (bool?): If on, save the current values of preferences to userPrefs file.  
                Properties: create, query
        saveRuntimeState (bool?): If on, runtime state as well as initial state of all particle objects  
                will be saved to file. If off, only initial state will be saved.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

