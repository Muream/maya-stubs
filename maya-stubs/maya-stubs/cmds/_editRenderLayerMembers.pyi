from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editRenderLayerMembers(*args: str, query: bool = ..., fullNames: bool = ..., noRecurse: bool = ..., remove: bool = ...) -> Union[int, List[str], bool]:
    """This command is used to query and edit memberships to render layers. Only
    transform and geometry nodes may be members. At render time, all
    descendants of the members of a render layer will also be included in the
    render layer.renderLayer, render, layer, member, relationship
    Args:
        fullNames (bool?): (Query only.) If set then return the full DAG paths of the objects in the  
                layer.  Otherwise return just the name of the object.  
                Properties: query
        noRecurse (bool?): If set then only add selected objects to the render layer.  Otherwise all  
                descendants of the selected objects will also be added. This flag may be  
                applied to adding or removing objects from the layer.  
                Properties: create
        remove (bool?): Remove the specified objects from the render layer.  
                Properties: create

    Returns:
        int: Number of objects added to the layer
        List[str]: Query: List of objects in layer

    Example:
    """

