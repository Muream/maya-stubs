from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shotRipple(arg0: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., deleted: bool = ..., endDelta: Queryable[int] = ..., endTime: Queryable[int] = ..., startDelta: Queryable[int] = ..., startTime: Queryable[int] = ...) -> Union[bool, int]:
    """When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated
    are moved in sequence time to either make way or close up gaps corresponding to that
    node's editing.
    Given some parameters about the shot edit that just took place, this command
    will choose which other shots to move, and move them the appropriate amounts
    If no shot name is provided, the command will attempt to use the first selected shot.reference, sequencer, node, shot, ripple
    Args:
        deleted (bool?): Specify whether this ripple edit is due to a shot deletion  
                Properties: create, query, edit
        endDelta (Queryable[int]?): Specify the change in the end time in frames  
                Properties: create, query, edit
        endTime (Queryable[int]?): Specify the initial shot end time in the sequence timeline.  
                Properties: create, query, edit
        startDelta (Queryable[int]?): Specify the change in the start time in frames  
                Properties: create, query, edit
        startTime (Queryable[int]?): Specify the initial shot start time in the sequence timeline.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

