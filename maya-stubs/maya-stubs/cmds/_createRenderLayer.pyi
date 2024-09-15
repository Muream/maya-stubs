from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def createRenderLayer(*args: str, empty: bool = ..., g: bool = ..., makeCurrent: bool = ..., name: str = ..., noRecurse: bool = ..., number: int = ...) -> str:
    """Create a new render layer.  The render layer number will be assigned
    based on the first unassigned number not less than the base index number
    found in the render layer global parameters.  Normally all objects and
    their descendants will be added to the new render layer but if '-noRecurse'
    is specified then only the objects themselves will be added. Only transforms
    and geometry will be added to the new render layer.renderLayer, 2d3d, layer, color, playback, render
    Args:
        empty (bool?): If set then create an empty render layer. The global flag or specified  
                member list will take precidence over  use of this flag.  
                Properties: create
        g (bool?): If set then create a layer that contains all DAG objects in the scene. Any  
                future objects created will also automatically become members of this layer.  
                The global flag will take precidence over use of the empty flag or specified  
                member list.  
                Properties: create
        makeCurrent (bool?): If set then make the new render layer the current one.  
                Properties: create
        name (str?): Name of the new render layer being created.  
                Properties: create
        noRecurse (bool?): If set then only add specified objects to the render layer.  Otherwise all  
                descendants will also be added.  
                Properties: create
        number (int?): Number for the new render layer being created.  
                Properties: create

    Returns:
        str: Name of render layer node that was created

    Example:
    """

