from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editRenderLayerAdjustment(*args: str, query: bool = ..., attributeLog: bool = ..., layer: Queryable[str] = ..., nodeLog: bool = ..., remove: bool = ...) -> Union[int, List[str], bool, str]:
    """This command is used to create, edit, and query adjustments to render
    layers. An adjustment allows different attribute values or connections
    to be used depending on the active render layer.renderLayer
    Args:
        attributeLog (bool?): Output all adjustments for the specified layer sorted by attribute name.  
                Properties: query
        layer (Queryable[str]?): Specified layer in which the adjustments will be modified. If not specified  
                the active render layer will be used.  
                Properties: create, query
        nodeLog (bool?): Output all adjustments for the specified layer sorted by node name.  
                Properties: query
        remove (bool?): Remove the specified adjustments from the render layer. If an adjustment  
                is removed from the current layer, the specified plug will revert back to  
                it's master value determined by the default render layer.  
                Properties: create

    Returns:
        int: Number of adjustments applied
        List[str]: Query: List of plugs adjustments to layer

    Example:
    """

