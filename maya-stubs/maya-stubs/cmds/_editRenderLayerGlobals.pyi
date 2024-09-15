from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editRenderLayerGlobals(*, query: bool = ..., baseId: Queryable[int] = ..., currentRenderLayer: Queryable[str] = ..., enableAutoAdjustments: bool = ..., mergeType: Queryable[int] = ..., useCurrent: bool = ...) -> Union[bool, str, int]:
    """Edit the parameter values common to all render layers.  Some of these
    paremeters, eg. baseId and mergeType, are stored as preferences and
    some, eg. currentRenderLayer, are stored in the file.renderLayer, render, layer, globals, current, merge
    Args:
        baseId (Queryable[int]?): Set base layer ID.  This is the number at which new layers start searching  
                for a unique ID.  
                Properties: create, query
        currentRenderLayer (Queryable[str]?): Set current render layer. This will will update the renderLayerManger and  
                all DAG objects to identify them as members of the render layer. This  
                flag may also be used in conjunction with "useCurrent" to automatically  
                add new DAG objects to the active layer. The "isCurrentRenderLayerChanging"  
                condition can be used to determine when the current layer is being changed  
                and adjustments are being applied to the scene.  
                Properties: create, query
        enableAutoAdjustments (bool?): Set whether or not to enable automatic creation of adjustments when  
                certain attributes (ie. surface render stats, shading group assignment,  
                or render settings) are changed.  
                Properties: create, query
        mergeType (Queryable[int]?): Set file import merge type.  Valid values are 0, none, 1, by number, and  
                2, by name.  
                Properties: create, query
        useCurrent (bool?): Set whether or not to enable usage of the current render layer as the  
                destination for all new nodes.  
                Properties: create, query

    Returns:
        bool: Command success
        str: Current render layer name, when querying
        int: Merge type, when querying
        int: Base ID, when querying

    Example:
    """

