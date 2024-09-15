from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cycleCheck(*args: str, query: bool = ..., all: bool = ..., children: bool = ..., dag: bool = ..., evaluation: bool = ..., firstCycleOnly: bool = ..., firstPlugPerNode: bool = ..., lastPlugPerNode: bool = ..., list: bool = ..., listSeparator: str = ..., parents: bool = ..., secondary: bool = ..., timeLimit: int = ...) -> Union[bool, List[str]]:
    """This command searches for plug cycles in the dependency graph. If
    a plug or node is selected then it searches for cycles that
    that plug or node is involved with. Plugs or nodes can also be passed
    as arguments. If the -all flag is used then the entire graph is searched.Normally the return value is a boolean indicating whether or not the
    given items were involved in a cycle.  If the -list flag is used then
    the return value is the list of all plugs in cycles (involving the
    selected plug or node if any).Note that it is possible for evaluation cycles to occur even where
    no DG connections exist. Here are some examples:1) Nodes with evaluation-time dependent connections: An example is
    expression nodes, because we cannot tell what an expression
    node is actually referring to until it is evaluated, and such
    evaluation-time dependent nodes may behave differently based on
    the context (e.g. time) they are evaluated at. If you suspect a
    cycle due to such a connection, the best way to detect the
    cycle is through manual inspection.2) Cycles due to DAG hierarchy: noting that DAG nodes are implicitely
    connected through parenting, if a child DAG node connects an output into
    the input of a parent node, a cycle will exist if the plugs involved
    also affect each other. In order to enable detection of cycles
    involving the DAG, add the -dag flag to the command line.Note also that this command may incorrectly report a cycle on
    an instanced skeleton where some of the instances use IK.
    You will have to examine the reported cycle yourself to determine
    if it is truly a cycle or not.
    The evaluation time cycle checking will not report false cycles.
    Args:
        all (bool?): search the entire graph for cycles instead of the selection list.  
                (Note: if nothing is selected, -all is assumed).  
                Properties: create
        children (bool?): Do not consider cycles on the children, only the specified plugs  
                Properties: create
        dag (bool?): Also look for cycles due to relationships in the DAG. For each DAG node,  
                the parenting connection on its children is also considered when searching  
                for cycles.  
                Properties: create
        evaluation (bool?): Turn on and off cycle detection during graph evaluation  
                Properties: create, query
        firstCycleOnly (bool?): When -list is used to return a plug list, the list may contain  
                multiple cycles or partial cycles. When -firstCycleOnly is specified  
                only the first such cycle (which will be a full cycle) is returned.  
                Properties: create
        firstPlugPerNode (bool?): When -list is used to return a plug list, the list will typically contain  
                multiple plugs per node (e.g. ... A.output B.input B.output C.input ...),  
                reflecting internal "affects" relationships rather than external DG connections.  
                When -firstPlugPerNode is specified, only the first plug in the list for each  
                node is returned (B.input in the example).  
                Properties: create
        lastPlugPerNode (bool?): When -list is used to return a plug list, the list will typically contain  
                multiple plugs per node (e.g. ... A.output B.input B.output C.input ...),  
                reflecting internal "affects" relationships rather than external DG connections.  
                When -lastPlugPerNode is specified, only the last plug in the list for each  
                node is returned (B.output in the example).  
                Properties: create
        list (bool?): Return all plugs involved in one or more cycles.  If not  
                specified, returns a boolean indicating whether a cycle exists.  
                Properties: create
        listSeparator (str?): When -list is used to return a plug list, the list may contain  
                multiple cycles or partial cycles. Use -listSeparator to specify  
                a string that will be inserted into the returned string array  
                to separate the cycles.  
                Properties: create
        parents (bool?): Do not consider cycles on the parents, only the specified plugs  
                Properties: create
        secondary (bool?): Look for cycles on related plugs as well as the specified plugs  
                Default is "on" for the "-all" case and "off" for others  
                Properties: create
        timeLimit (int?): Limit the search to the given amount of time  
                Properties: create

    Returns:
        bool: in the general case.
        List[str]: When the list flag is used.

    Example:
    """

