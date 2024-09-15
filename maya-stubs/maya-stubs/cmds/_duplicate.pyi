from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def duplicate(*args: str, fullPath: bool = ..., inputConnections: bool = ..., instanceLeaf: bool = ..., name: str = ..., parentOnly: bool = ..., renameChildren: bool = ..., returnRootsOnly: bool = ..., smartTransform: bool = ..., transformsOnly: bool = ..., upstreamNodes: bool = ...) -> List[str]:
    """This command duplicates the given objects. If no objects are
    given, then the selected list is duplicated.The smart transform feature allows duplicate to transform
    newly duplicated objects based on previous transformations
    between duplications.Example: Duplicate an object and move it to a new
    location. Duplicate it again with the smart duplicate
    flag. It should have moved once again the distance you had
    previously moved it.Note: changing the selected list between smart duplications
    will cause the transform information to be deletedThe upstream Nodes option forces duplication of all
    upstream nodes leading upto the selected objects.. Upstream nodes
    are defined as all nodes feeding into selected nodes. During traversal
    of Dependency graph, if another dagObject is encountered, then that
    node and all it's parent transforms are also duplicated.The inputConnections option forces the duplication of input connections
    to the nodes that are to be duplicated. This is very useful especially
    in cases where two nodes that are connected to each other are
    specified as nodes to be duplicated. In that situation, the connection
    between the nodes is also duplicated.instance
    Args:
        fullPath (bool?): ADDED 2023  
                Return full pathnames instead of object names.  
                Properties: create
        inputConnections (bool?): Input connections to the node to be duplicated, are  
                also duplicated. This would result in a fan-out  
                scenario as the nodes at the input side are not  
                duplicated (unlike the -un option).  
                Properties: create
        instanceLeaf (bool?): instead of duplicating leaf DAG nodes, instance them.  
                Properties: create
        name (str?): name to give duplicated object(s)  
                Properties: create
        parentOnly (bool?): Duplicate only the specified DAG node and not any of its  
                children.  
                Properties: create
        renameChildren (bool?): rename the child nodes of the hierarchy, to make them  
                unique.  
                Properties: create
        returnRootsOnly (bool?): return only the root nodes of the new hierarchy.  
                When used with upstreamNodes flag, the upstream nodes  
                will be omitted in the result.  This flag controls only  
                what is returned in the output string[], and it does  
                NOT change the behaviour of the duplicate command.  
                Properties: create
        smartTransform (bool?): remembers last transformation and applies  
                it to duplicated object(s)  
                Properties: create
        transformsOnly (bool?): Duplicate only transform nodes and not any shapes.  
                Properties: create
        upstreamNodes (bool?): the upstream nodes leading upto the selected nodes  
                (along with their connections) are also duplicated.  
                Properties: create

    Returns:
        List[str]: : names of the objects created

    Example:
    """

