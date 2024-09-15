from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def instanceable(*args: str, query: bool = ..., allow: bool = ..., recursive: bool = ..., shape: bool = ...) -> Union[None, List[bool], bool]:
    """Flags one or more DAG nodes so that they can (or cannot) be instanced.
    This command sets an internal state on the specified DAG nodes which is
    checked whenever Maya attempts an instancing operation.
    If no node names are provided on the command line then the current selection list is used.Sets are automatically expanded to their constituent objects. Nodes which are already
    instanced (or have children which are already instanced) cannot be marked as non-instancable.node, dependency, graph, instancing
    Args:
        allow (bool?): Specifies the new instanceable state for the node. Specify true to allow the node  
                to be instanceable, and false to prevent it from being instanced. The default is true  
                (i.e. nodes can be instanced by default).  
                Properties: create, query
        recursive (bool?): Can be specified with the -allow flag in create or edit mode to recursively apply the  
                -allow setting to all non-shape children of the selected node(s). To also affect  
                shapes, also specify the -shape flag along with -recursive.  
                Properties: create
        shape (bool?): Can be specified with the -allow flag in create or edit mode to apply the  
                -allow setting to all shape children of the selected node(s). This flag can be  
                specified in conjunction with the -recursive flag.  
                Properties: create

    Returns:
        None: For regular command execution.
        List[bool]: For query execution.

    Example:
    """

