from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editDisplayLayerGlobals(*, query: bool = ..., baseId: Queryable[int] = ..., currentDisplayLayer: Queryable[str] = ..., mergeType: Queryable[int] = ..., useCurrent: bool = ...) -> Union[bool, str, int]:
    """Edit the parameter values common to all display layers.  Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and
    some, eg. currentDisplayLayer, are stored in the file.displayLayer, display, layer, globals, current, merge
    Args:
        baseId (Queryable[int]?): Set base layer ID.  This is the number at which new layers start searching  
                for a unique ID.  
                Properties: create, query
        currentDisplayLayer (Queryable[str]?): Set current display layer; ie. the one that all new objects are added to.  
                Properties: create, query
        mergeType (Queryable[int]?): Set file import merge type.  Valid values are 0, none, 1, by number, and  
                2, by name.  
                Properties: create, query
        useCurrent (bool?): Set whether or not to enable usage of the current display layer as the  
                destination for all new nodes.  
                Properties: create, query

    Returns:
        bool: Command success
        str: Current display layer name, when querying
        int: Merge type, when querying
        int: Base ID, when querying

    Example:
    """

