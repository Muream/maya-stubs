from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def makeLive(*args: str, edit: bool = ..., query: bool = ..., addObjects: bool = ..., none: bool = ..., registry: Queryable[int] = ..., registryCount: bool = ..., registryReset: bool = ..., registrySize: Queryable[int] = ..., removeObjects: bool = ...) -> Union[bool, int]:
    """This commmand makes one or several objects live.  A live object defines the
    surface on which to create objects and to move objects relative to.
    Only construction planes, nurbs surfaces and polygon meshes can be made live.The makeLive command expects one of these types of objects as an explicit
    argument.  If no argument is explicitly specified, then there are a number
    of default behaviours based on what is currently active.  The command will
    fail if the active object(s) is/are not one of the valid types of objects.
    If there is nothing active, the current live object(s) will become dormant.
    Otherwise, the active object(s) will become the live object(s).The command allows for a limited number of objects collections to be saved
    in a registry entry. These collections can be queried and/or made live.
    Args:
        addObjects (bool?): Add the listed object(s) to the current live list.  
                If an object is already in the live list, it is ignored.  
                Properties: edit
        none (bool?): If the -n/none flag, the live object(s) will become dormant.  
                Use of this flag causes any arguments to be ignored.  
                Properties: create
        registry (Queryable[int]?): Make live the objects defined in the specified registry entry.  
                In Query mode, return the list of objects defined in the specified registry entry.  
                Properties: create, query
        registryCount (bool?): Return the actual number of registry entries.  
                This number ranges from 0 to 'registrySize' - 1.  
                Properties: query
        registryReset (bool?): Reset the maximum number of registry entries to the default value and clear all stored data.  
                Properties: create
        registrySize (Queryable[int]?): Defines the maximum number of registry entries that are remembered by the command.  
                In Query mode, returns the maximum number currently set.  
                Properties: create, query
        removeObjects (bool?): Remove the listed object(s) from the current live list.  
                If an object is not in the list, it is ignored.  
                Properties: edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

