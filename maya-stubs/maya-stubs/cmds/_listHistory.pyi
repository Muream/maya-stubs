from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listHistory(*args: str, query: bool = ..., allConnections: bool = ..., allFuture: bool = ..., allGraphs: bool = ..., breadthFirst: bool = ..., fastIteration: bool = ..., fullNodeName: bool = ..., future: bool = ..., futureLocalAttr: bool = ..., futureWorldAttr: bool = ..., groupLevels: bool = ..., historyAttr: bool = ..., interestLevel: int = ..., leaf: bool = ..., levels: int = ..., pruneDagObjects: bool = ...) -> Union[List[str], bool]:
    """This command traverses backwards or forwards in the graph from
    the specified node and returns all of the nodes whose construction
    history it passes through. The construction history consists of
    connections to specific attributes of a node defined as the
    creators and results of the node's main data, eg. the curve for
    a Nurbs Curve node.For information on history connections through specific plugs use
    the "listConnections" command first to find where the history begins
    then use this command on the resulting node.
    Args:
        allConnections (bool?): If specified, the traversal that searches for the history or future will  
                not restrict its traversal across nodes to only dependent plugs.  
                Thus it will reach all upstream nodes (or all downstream nodes for f/future).  
                Properties: create
        allFuture (bool?): If listing the future, list all of it. Otherwise if a shape has  
                an attribute that represents its output geometry data, and that plug  
                is connected, only list the future history downstream from that  
                connection.  
                Properties: create
        allGraphs (bool?): This flag is obsolete and has no effect.  
                Properties: create
        breadthFirst (bool?): The breadth first traversal will return the closest nodes in the  
                traversal first. The depth first traversal will follow a complete  
                path away from the node, then return to any other paths from the  
                node. Default is depth first.  
                Properties: create
        fastIteration (bool?): This flag enables a faster iteration mode that offers more scalable performance,  
                especially when traversing nodes with numerous connections.  However, the results can  
                be slightly different, especially in cases with transitive dependencies between  
                attributes (attribute A is affected by B which is affected by C, but A is not  
                directly affected by C).  
                Properties: create
        fullNodeName (bool?): Return full node name in result.  
                Properties: create
        future (bool?): List the future instead of the history.  
                Properties: create
        futureLocalAttr (bool?): This flag allows querying of the local-space future-related attribute(s) on shape nodes.  
                Properties: query
        futureWorldAttr (bool?): This flag allows querying of the world-space future-related attribute(s) on shape nodes.  
                Properties: query
        groupLevels (bool?): The node names are grouped depending on the level.  > 1 is  
                the lead, the rest are grouped with it.  
                Properties: create
        historyAttr (bool?): This flag allows querying of the attribute where history connects on shape nodes.  
                Properties: query
        interestLevel (int?): If this flag is set, only nodes whose historicallyInteresting  
                attribute value is not less than the value will be listed.  
                The historicallyInteresting attribute is 0 on nodes which are  
                not of interest to non-programmers.  1 for the TDs, 2 for the users.  
                Properties: create
        leaf (bool?): If transform is selected, show history for its leaf  
                shape. Default is true.  
                Properties: create
        levels (int?): Levels deep to traverse. Setting the number of levels to  
                0 means do all levels. All levels is the default.  
                Properties: create
        pruneDagObjects (bool?): If this flag is set, prune at dag objects.  
                Properties: create

    Returns:
        List[str]: List of history nodes

    Example:
    """

