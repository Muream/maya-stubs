from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editDisplayLayerMembers(*args: str, query: bool = ..., clear: bool = ..., fullNames: bool = ..., noRecurse: bool = ..., ufeObjects: bool = ...) -> Union[int, List[str], bool]:
    """This command is used to query and edit membership of display layers.  No
    equivalent 'remove' command is necessary since all objects must be in exactly
    one display layer.  Removing an object from a layer can be accomplished by
    adding it to a different layer.displayLayer, display, layer, member, relationship
    Args:
        clear (bool?): Remove all the objects contained in the layer by moving them to the default layer.  
                Properties: create
        fullNames (bool?): (Query only.) If set then return the full DAG paths of the objects in the  
                layer.  Otherwise return just the name of the object.  
                Properties: query
        noRecurse (bool?): If set then only add selected objects to the display layer.  Otherwise all  
                descendants of the selected objects will also be added.  
                Properties: create, query
        ufeObjects (bool?): (Query only.) If set will return objects that are  
                defined through the UFE interface as well as native Maya objects.  
                Properties: query

    Returns:
        int: Number of objects added to the layer
        List[str]: Query: List of objects in layer

    Example:
    """

