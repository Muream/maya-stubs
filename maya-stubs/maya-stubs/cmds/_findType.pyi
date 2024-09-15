from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def findType(*args: str, deep: bool = ..., exact: bool = ..., forward: bool = ..., type: str = ...) -> List[str]:
    """Thecommand is used to search through a dependency
    subgraph on a certain node to find all nodes of the given type.
    The search can go either upstream (input connections) or downstream (output
    connections). The plug/attribute dependencies are not taken into account
    when searching for matching nodes, only the connections.debug, node, type, search
    Args:
        deep (bool?): Find all nodes of the given type instead of just the first.  
                Properties: create
        exact (bool?): Match node types exactly instead of any in a node hierarchy.  
                Properties: create
        forward (bool?): Look forwards (downstream) through the graph rather than backwards  
                (upstream) for matching nodes.  
                Properties: create
        type (str?): Type of node to look for (e.g. "transform"). This flag is mandatory.  
                Properties: create

    Returns:
        List[str]: The list of node(s) of the requested type connected to the given node(s)

    Example:
    """

