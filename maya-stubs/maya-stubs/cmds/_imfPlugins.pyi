from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def imfPlugins(arg0: str = ..., /, *, query: bool = ..., extension: Queryable[str] = ..., keyword: Queryable[str] = ..., multiFrameSupport: Queryable[str] = ..., pluginName: Queryable[str] = ..., readSupport: Queryable[str] = ..., writeSupport: Queryable[str] = ...) -> Union[List[str], str]:
    """This command queries all the available imf plugins for its
    name, keyword or image file extension.
    Only one of the attributes (name, keyword or extension) can be queried at a time.
    If no flags are specified, this command returns a list of all available plugin
    names.imf
    Args:
        extension (Queryable[str]?): image file extension  
                Properties: create, query
        keyword (Queryable[str]?): imf keyword  
                Properties: create, query
        multiFrameSupport (Queryable[str]?): multi frame IO is supported  
                Properties: create, query
        pluginName (Queryable[str]?): imf plugin name  
                Properties: create, query
        readSupport (Queryable[str]?): read operation is supported  
                Properties: create, query
        writeSupport (Queryable[str]?): write operation is supported  
                Properties: create, query

    Returns:
        List[str]: Command result

    Example:
    """

