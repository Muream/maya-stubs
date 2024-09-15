from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgInfo(*args: str, allNodes: bool = ..., connections: bool = ..., dirty: bool = ..., nodes: bool = ..., nonDeletable: bool = ..., outputFile: str = ..., propagation: bool = ..., short: bool = ..., size: bool = ..., subgraph: bool = ..., type: str = ...) -> bool:
    """This command prints information about the DG in plain text.
    The scope of the information printed is the entire graph
    if theflag is used, the nodes/plugs on the command line if
    they were specified, and the selection list, in that order.
    Each plug on a connection will have two pieces of state information
    displayed together at the end of the line on which they are printed.
    There are two possible values for each of the two states displayed.
    The values are updated when the DG pulls data across them, usually
    through evaluation, or pushes a dirty message through them. There
    are some subtleties in how the data is pulled through the connection
    but for simplicity it will be referred to as "evaluation".
    The values displayed will be CLEAN or DIRTY followed by PROP or BLOCK.
    The first keyword has these meanings:Note: the data on the node has its own dirty state that depends
    on other factors so having a clean connection doesn't necessarily
    mean the plug's data is clean, and vice versa.
    The second keyword has these meanings:The combinationshould never be seen in a valid DG.
    This indicates that while the plug connection has been evaluated since
    the last dirty message it will not propagate any new dirty messages
    coming in to it. That in turn means downstream nodes will not be
    notified that the graph is changing and they will not evaluate properly.
    Recovering from this invalid state requires entering the commandto mark everything dirty and restart proper evaluation.
    Think of this command as the reset/reboot of the DG world.
    Both state types behave differently depending on your connection type.There are some other exceptions to these rules:debug, dependency, graph, node, output, connection
    Args:
        allNodes (bool?): Use the entire graph as the context  
                Properties: create
        connections (bool?): Print the connection information  
                Properties: create
        dirty (bool?): Only print dirty/clean nodes/plugs/connections.  Default is both  
                Properties: create
        nodes (bool?): Print the specified nodes (or the entire graph if -all is used)  
                Properties: create
        nonDeletable (bool?): Include non-deletable nodes as well (normally not of interest)  
                Properties: create
        outputFile (str?): Send the output to the file FILE instead of STDERR  
                Properties: create
        propagation (bool?): Only print propagating/not propagating nodes/plugs/connections.  
                Default is both.  
                Properties: create
        short (bool?): Print using short format instead of long  
                Properties: create
        size (bool?): Show datablock sizes for all specified nodes. Return value is tuple of  
                all selected nodes (NumberOfNodes, NumberOfDatablocks, TotalDatablockMemory)  
                Properties: create
        subgraph (bool?): Print the subgraph affected by the node or plugs (or all nodes  
                in the graph grouped in subgraphs if -all is used)  
                Properties: create
        type (str?): Filter output to only show nodes of type NODETYPE  
                Properties: create

    Returns:
        bool:

    Example:
    """

