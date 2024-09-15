from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def displayString(arg0: str = ..., arg1: str = ..., arg2: str = ..., arg3: str = ..., /, *, query: bool = ..., delete: bool = ..., exists: bool = ..., keys: bool = ..., replace: bool = ..., value: Queryable[str] = ...) -> Union[bool, str]:
    """Assign a string value to a string identifier. Allows you define a string in
    one location and then refer to it by its identifier in many other locations.
    Formatted strings are also supported (NOTE however, this functionality is now
    provided in a more general fashion by the format command, use of format
    is recommended). You may embed up to 3 special character sequences
    ^1s, ^2s, and ^3s to perform automatic string replacement. The
    embedded characters will be replaced with the extra command arguments. See
    example section for more detail. Note the extra command arguments do not need
    to be display string identifiers.display, string
    Args:
        delete (bool?): This flag is used to remove an identifer string.  
                The command will fail if the identifier does not exist.  
                Properties: create
        exists (bool?): Returns true or false depending upon whether the specified identifier exists.  
                Properties: create
        keys (bool?): List all displayString keys that match the identifier string.  
                The identifier string may be a whole or partial key string.  
                The command will return a list of all identifier keys that contain this  
                identifier string as a substring.  
                Properties: create, query
        replace (bool?): Since a displayString command will fail if it tries to assign a new value  
                to an existing identifer, this flag is required to allow updates  
                to the value of an already-existing identifier.  If the identifier does  
                not already exist, a new identifier is added as if the -replace flag were  
                not present.  
                Properties: create, query
        value (Queryable[str]?): The display string\\'s value. If you do not specify this flag when  
                creating a display string then the value will be the same as the  
                identifier.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

