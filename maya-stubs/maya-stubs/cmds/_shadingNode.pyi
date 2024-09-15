from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shadingNode(*args: Any, asLight: bool = ..., asPostProcess: bool = ..., asRendering: bool = ..., asShader: bool = ..., asTexture: bool = ..., asUtility: bool = ..., isColorManaged: bool = ..., name: str = ..., parent: str = ..., shared: bool = ..., skipSelect: bool = ...) -> str:
    """This command creates a new node in the dependency graph of the
    specified type.The shadingNode command classifies any DG node as a shader, texture
    light, post process, or utility so that it can be properly organized
    in the multi-lister.  Recall that any DG node can be used a part of a
    a shader, texture or light - regardless of how it is classified by this.
    command. These classifications are provided for convenience in the UI.
    Args:
        asLight (bool?): classify the current DG node as a light  
                Properties: create
        asPostProcess (bool?): classify the current DG node as a post process  
                Properties: create
        asRendering (bool?): classify the current DG node as a rendering node  
                Properties: create
        asShader (bool?): classify the current DG node as a shader  
                Properties: create
        asTexture (bool?): classify the current DG node as a texture  
                Properties: create
        asUtility (bool?): classify the current DG node as a utility  
                Properties: create
        isColorManaged (bool?): classify the current DG node as being color managed  
                Properties: create
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
        str: (the name of the new node)

    Example:
    """

