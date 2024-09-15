from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynGlobals(*args: str, edit: bool = ..., query: bool = ..., active: bool = ..., listAll: bool = ..., overSampling: Queryable[int] = ...) -> Union[str, int, bool]:
    """This node edits and queries the attributes of the active dynGlobals
    node in the scene. There can be only one active node of this type.
    The active dynGlobals node is the first one that was created, either
    with a "createNode" command or by accessing/editing any of the
    attributes on the node through this command.
    Args:
        active (bool?): This flag returns the name of the active dynGlobals node in the  
                the scene.  Only one dynGlobals node is active. It is the first on  
                created.  Any additional dynGlobals nodes will be ignored.  
                Properties: query
        listAll (bool?): This flag will list all of the dynGlobals nodes in the scene.  
                Properties: query
        overSampling (Queryable[int]?): This flag will set the current overSampling value for all of  
                the particle in the scene.  
                Properties: query, edit

    Returns:
        str: For edit commands
        int: or string
            For query commands, depending on the flag queried.

    Example:
    """

