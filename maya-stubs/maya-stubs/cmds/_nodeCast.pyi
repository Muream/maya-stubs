from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nodeCast(arg0: str = ..., arg1: str = ..., /, *, copyDynamicAttrs: bool = ..., disableAPICallbacks: bool = ..., disableScriptJobCallbacks: bool = ..., disconnectUnmatchedAttrs: bool = ..., force: bool = ..., swapNames: bool = ..., swapValues: bool = ...) -> int:
    """Given two nodes, a source node of type A and a target node of type B,
    where type A is either type B or a sub-type of B, this command will replace the
    target node with the source node. That is, all node connections, DAG hierarchy
    and attribute values on the target node will be removed from the target node
    and placed on the source node. This operation will fail if either object is
    referenced, locked or if the nodes do not share a common sub-type.
    This operation is atomic. If the given parameters fail, then the source and
    target nodes will remain in their initial state prior to execution of the
    command.
    IMPORTANT: the command will currently ignore instance connections and
    instance objects.  It will also ignore reference nodes.node, swap, cast
    Args:
        copyDynamicAttrs (bool?): If the target node contains any dynamic attributes that are not defined on the  
                source node, then create identical dynamic attricutes on the source node and copy  
                the values and connections from the target node into them.  
                Properties: create
        disableAPICallbacks (bool?): add comment  
                Properties: create
        disableScriptJobCallbacks (bool?): add comment  
                Properties: create
        disconnectUnmatchedAttrs (bool?): If the node that is being swapped out has any connections that do not exist  
                on the target node, then indicate if the connection should be disconnected.  
                By default these connections are not removed because they cannot be restored  
                if the target node is swapped back with the source node.  
                Properties: create
        force (bool?): Forces the command to do the node cast operation even if the nodes do  
                not share a common base object. When this flag is specified the command  
                will try to do the best possible attribute matching when swapping the  
                command.  It is not recommended to use the '-swapValues/sv' flag with  
                this flag.  
                Properties: create
        swapNames (bool?): Swap the names of the nodes. By default names are not swapped.  
                Properties: create
        swapValues (bool?): Indicates if the commands should exchange attributes on the common attributes  
                between the two nodes.  For example, if the nodes are the same base type  
                as a transform node, then rotate, scale, translate values would be copied  
                over.  
                Properties: create

    Returns:
        int: 0 for success, 1 for failure.

    Example:
    """

