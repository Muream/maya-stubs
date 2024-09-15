from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def commandEcho(*, query: bool = ..., addFilter: List[str] = ..., filter: Queryable[List[str]] = ..., lineNumbers: bool = ..., state: bool = ...) -> Union[bool, List[str]]:
    """This command controls what is echoed to the command window.
    Args:
        addFilter (List[str]?): This flag allows you to append filters to the current list of filtered commands when echo all commands is enabled.  
                Just like the filter flag, you can provide a partial command name, so all commands that start with a substring specified in the addFilter entry will be filtered out.  
                Properties: create
        filter (Queryable[List[str]]?): This flag allows you to filter out unwanted commands when echo all commands is enabled.  
                You can provide a partial command name, so all commands that start with a substring specified in filter entry will be filtered out.  
                If filter is empty, all commands are echoed to the command window.  
                Properties: create, query
        lineNumbers (bool?): If true then file name and line number information is provided in  
                error and warning messages.  
                If false then no file name and line number information is provided  
                in error and warning messages.  
                Properties: create, query
        state (bool?): If true then all commands are echoed to the command window.  
                If false then only relevant commands are echoed.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

