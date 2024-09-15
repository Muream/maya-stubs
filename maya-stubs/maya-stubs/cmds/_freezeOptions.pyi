from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def freezeOptions(*, query: bool = ..., displayLayers: bool = ..., downstream: Queryable[str] = ..., explicitPropagation: bool = ..., invisible: bool = ..., referencedNodes: bool = ..., runtimePropagation: bool = ..., upstream: Queryable[str] = ...) -> Union[str, bool]:
    """This command provides access to the options used by the evaluation manager to
    handle propagation and recognition of when a node is in a frozen state.
    See the individual flags for the different options available.
    These values are all stored as user preferences and persist across sessions.evaluation, manager, DG, runtime, freeze
    Args:
        displayLayers (bool?): If this option is enabled then any nodes that are in an enabled, invisible display  
                layer will be considered to be frozen, and the frozen state will propagate accordingly.  
                Properties: create, query
        downstream (Queryable[str]?): Controls how frozen state is propagated downstream from currently frozen nodes.  
                Valid values are "none" for no propagation, "safe" for propagation downstream  
                only when all upstream nodes are frozen, and "force" for propagation downstream  
                when any upstream node is frozen.  
                Properties: create, query
        explicitPropagation (bool?): When turned on this will perform an extra pass when the evaluation graph is  
                constructed to perform intelligent propagation of the frozen state to related  
                nodes as specified by the currently enabled options of the evaluation graph.  
                See also "runtimePropagation".  
                This option performs more thorough propagation of the frozen state, but requires  
                extra time for recalculating the evaluation graph.  
                Properties: create, query
        invisible (bool?): If this option is enabled then any nodes that are invisible, either directly or  
                via an invisible parent node, will be considered to be frozen, and the frozen state  
                will propagate accordingly.  
                Properties: create, query
        referencedNodes (bool?): If this option is enabled then any nodes that are referenced in from a frozen referenced node  
                will also be considered to be frozen, and the frozen state will propagate accordingly.  
                Properties: create, query
        runtimePropagation (bool?): When turned on this will allow the frozen state to propagate during execution  
                of the evaluation graph. See also "explicitPropagation".  
                This option allows frozen nodes to be scheduled for evaluation, but once it  
                discovers a node that is frozen it will prune the evaluation based on the  
                current set of enabled options. It only works in the downstream direction.  
                Properties: create, query
        upstream (Queryable[str]?): Controls how frozen state is propagated upstream from currently frozen nodes.  
                Valid values are "none" for no propagation, "safe" for propagation upstream  
                only when all downstream nodes are frozen, and "force" for propagation upstream  
                when any downstream node is frozen.  
                Properties: create, query

    Returns:
        str: Current value of the option if querying the downstream or upstream flags
        bool: Current value of the option if querying the displayLayers, invisible, referencedNodes, explicitPropagation, or runtimePropagaton flags
        bool: In creation mode returns true if all options were successfully set

    Example:
    """

