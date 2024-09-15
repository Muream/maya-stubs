from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def unknownPlugin(arg0: str = ..., /, *, query: bool = ..., dataTypes: bool = ..., list: bool = ..., nodeTypes: bool = ..., remove: bool = ..., version: bool = ...) -> Union[List[str], bool]:
    """Allows querying of the unknown plug-ins used by the scene,
    and provides a means to remove them.
    Args:
        dataTypes (bool?): Returns the data types associated with the given unknown plug-in.  
                This will always be empty for pre-Maya 2014 files.  
                Properties: query
        list (bool?): Lists the unknown plug-ins in the scene.  
                Properties: query
        nodeTypes (bool?): Returns the node types associated with the given unknown plug-in.  
                This will always be empty for pre-Maya 2014 files.  
                Properties: query
        remove (bool?): Removes the given unknown plug-in from the scene.  
                For Maya 2014 files and onwards, this will fail if node  
                or data types defined by the plug-in are still in use.  
                Properties: create
        version (bool?): Returns the version string of the given unknown plug-in.  
                Properties: query

    Returns:
        List[str]: in query mode

    Example:
    """

