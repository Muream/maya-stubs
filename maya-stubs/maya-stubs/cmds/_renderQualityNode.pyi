from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderQualityNode(arg0: str = ..., /, *, name: str = ..., parent: str = ..., shared: bool = ..., skipSelect: bool = ...) -> str:
    """This command creates a new node in the dependency graph of the
    specified type.The renderQualityNode creates a render quality node
    and registers it with the model.  The createNode
    command will not register nodes of this type correctly.
    Args:
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace doesn't exist, we  
                will create the namespace.  
                Properties: create
        parent (str?): Specifies the parent in the DAG under which the new node belongs.  
                Properties: create
        shared (bool?): This node is shared across multiple files, so only create it if  
                it does not already exist.  
                Properties: create
        skipSelect (bool?): This node is not to be selected after creation, the original selection  
                will be preserved.  
                Properties: create

    Returns:
        str: The name of the new node.
        str: The Name of the render quality node

    Example:
    """

