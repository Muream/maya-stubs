from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def autoSave(*, query: bool = ..., destination: Queryable[int] = ..., destinationFolder: bool = ..., enable: bool = ..., folder: Queryable[str] = ..., interval: Queryable[float] = ..., limitBackups: bool = ..., maxBackups: Queryable[int] = ..., perform: bool = ..., prompt: bool = ...) -> Union[bool, int, str, float]:
    """Provides an interface to the auto-save mechanism.
    Args:
        destination (Queryable[int]?): Sets the option for where auto-save files go.  
                0. auto-saves go into the workspace autosave folder  
                1. auto-saves go into the named folder (set with the -folder flag)  
                2. auto-saves go into a folder set by an environment variable (MAYA_AUTOSAVE_FOLDER)  
                Properties: create, query
        destinationFolder (bool?): Queries the actual destination folder for auto-saves, based on the current  
                setting of the -destination flag, workspace rules and environment variables.  
                Resolves environment variables etc. and makes any relative path  
                absolute (resolved relative to the workspace root).  
                The returned string will end with a trailing separator ('/').  
                Properties: query
        enable (bool?): Enables or disables auto-saves.  
                Properties: create, query
        folder (Queryable[str]?): Sets the folder for auto-saves used if the destination option is 1.  
                Properties: create, query
        interval (Queryable[float]?): Sets the interval between auto-saves (in seconds).  
                The default interval is 600 seconds (10 minutes).  
                Properties: create, query
        limitBackups (bool?): Sets whether the number of auto-save files is limited.  
                Properties: create, query
        maxBackups (Queryable[int]?): Sets the maximum number of auto-save files, if limiting is in effect.  
                Properties: create, query
        perform (bool?): Invokes the auto-save process.  
                Properties: create
        prompt (bool?): Sets whether the auto-save prompts the user before auto-saving.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

