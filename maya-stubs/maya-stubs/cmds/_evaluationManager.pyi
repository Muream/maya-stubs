from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def evaluationManager(*args: str, query: bool = ..., cycleCluster: Queryable[str] = ..., disableInfo: Queryable[str] = ..., empty: bool = ..., enabled: bool = ..., fallbackTriggered: bool = ..., idleAction: Queryable[int] = ..., idleBuild: bool = ..., invalidate: bool = ..., manipulation: bool = ..., manipulationPrevalidation: bool = ..., manipulationReady: bool = ..., mode: Queryable[str] = ..., downstreamFrom: str = ..., nodeTypeGloballySerialize: bool = ..., nodeTypeParallel: bool = ..., nodeTypeSerialize: bool = ..., nodeTypeUntrusted: bool = ..., upstreamFrom: str = ..., reduceGraphRebuild: bool = ..., safeMode: bool = ...) -> Union[List[str], bool, int, List[bool], str]:
    """Handles turning on and off the evaluation manager method of evaluating the DG.
    Query the 'mode' flag to see all available evaluation modes. The special mode
    'off' disables the evaluation manager.
    The scheduling override flags 'nodeTypeXXX' force certain node types to use
    specific scheduling types, even though the node descriptions might indicate
    otherwise. Use with caution; certain nodes may not react well to
    alternative scheduling types.
    Only one scheduling type override will be in force at a time, the most
    restrictive one. In order, they are untrusted, globally serialized, locally
    serialized, and parallel. The node types will however remember all overrides.
    For example, if you set a node type override to be untrusted, then to be
    parallel it will continue to use the untrusted override. If you then turn off
    the untrusted override, the scheduling will advance to the parallel one.
    The actual node scheduling type is always superceded by the overrides. For example, a
    serial node will still be considered as parallel if the node type has the
    parallel override set, even though 'serial' is a more restrictive scheduling type.
    See the 'dbpeek' command 'graph' operation with arguments 'evaluationGraph' and
    'scheduling' to see what scheduling type any particular node will end up using
    after the hierarchy of overrides and native scheduling types is applied.evaluation, manager, DG, runtime
    Args:
        cycleCluster (Queryable[str]?): Returns a list of nodes that are stored together with the given one in  
                a cycle cluster. The list will be empty when the evaluation mode is not  
                active or the node is not in a cycle.  
                Properties: create, query
        disableInfo (Queryable[str]?): Returns a list of strings that contain the reasons that the evaluation manager has  
                been disabled (as distinct from it being deliberately turned off, e.g. because an  
                unsupported node type or attribute value was encountered).  
                If the list is empty then the evaluation manager is operating normally.  
                Properties: query
        empty (bool?): Valid in query mode only. Checks to see if the evaluation graph has any nodes in it.  
                This is independent of the current mode.  
                Properties: query
        enabled (bool?): Valid in query mode only. Checks to see if the evaluation manager is currently enabled.  
                This is independent of the current mode.  
                Properties: query
        fallbackTriggered (bool?): Valid in query mode only. Checks to see if fallback serial evaluation has been triggered.  
                Will be true if errors during parallel execution have forced a fallback to serial mode.  
                Will reset to false if the mode is changed again after the fallback was triggered.  
                Properties: query
        idleAction (Queryable[int]?): This flag sets the actions EM will perform on idle. It accepts the following values:  
              
                0. No action  
                1. Graph Rebuild  
                2. EM Manipulation Preparation  
                3. Graph Rebuild and EM Manipulation Preparation  
              
              
                Where:  
              
                Graph Rebuild will rebuild the evaluation graph on an idle event as soon  
                as it is able to do so.  
                EM ManipulationPreparation will get the evaluation manager to perform all  
                the steps necessary for EM manipulation to be available after the next idle event.  
              
              
                Note: These idle actions only apply to the graph attached to the normal context.  
                All other graphs will be built according to their own rules.  
              
                The disadvantage of enabling idle actions is that for some workflows that are  
                changing the graph frequently, or very large graphs, the graph build and  
                manipulation preparation time may impact the workflow. If workflows are impacted  
                it is suggested to turn idle actions off by passing this flag a value of 0.  
                Properties: create, query
        idleBuild (bool?): This flag is obsolete. Please use the -idleAction flag with a value of 1  
                in order to activate evaluation graph rebuild on idle.  
                Properties: create, query
        invalidate (bool?): This flag invalidates the graph. Value is used to control auto rebuilding on idle (false) or forced (true).  
                This command should be used as a last resort.  
                In query mode it checks to see if the graph is valid.  
                Properties: create, query
        manipulation (bool?): This flag is used to activate evaluation manager manipulation support.  
                Properties: create, query
        manipulationPrevalidation (bool?): This flag is used to activate evaluation manager manipulation prevalidation.  
                Prevalidation checks for known patterns in manipulation.  In case of a  
                successful prevalidation, there is no need to use dirty propagation in the  
                first frame of manipulation to validate that EM manipulation can safely be used,  
                and fast manipulation can start right away.  
                Properties: create, query
        manipulationReady (bool?): Valid in query mode only. Checks to see if the evaluation manager manipulation is currently ready/allowed.  
                This is independent of the current mode.  
                Properties: query
        mode (Queryable[str]?): Changes the current evaluation mode in the evaluation manager. Supported values are  
                "off", "serial" and "parallel".  
                Properties: create, query
        downstreamFrom (str?): Find the DG nodes that are immediately downstream of the named one in  
                the evaluation graph. Note that the connectivity is via evaluation mode  
                connections, not DG connections.  
                In query mode the graph is walked and any nodes downstream of the named  
                one are returned. The return type is alternating pairs of values that  
                represent the graph level and the node name, e.g. if you walk downstream  
                from A in the graph A -> B -> C then the return will be the array of  
                strings ("0","A","1","B","2","C"). Scripts can deconstruct this  
                information into something more visually recognizable. Note that cycles  
                are likely to be present so any such scripts would have to handle them.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        nodeTypeGloballySerialize (bool?): This flag is used only when the evaluation manager is in "parallel" mode  
                but can be set at anytime. It activates or deactivates the override to force  
                global serial scheduling for the class name argument(s) in the evaluation manager.  
                Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".  
                When queried without specified nodes, it returns the list of nodes with the  
                global serial scheduling override active.  
                Scheduling overrides take precedence over all of the node and node type  
                scheduling rules. Use with caution; certain nodes may not react well to  
                alternative scheduling types.  
                Properties: create, query
        nodeTypeParallel (bool?): This flag is used only when the evaluation manager is in "parallel" mode  
                but can be set at anytime. It activates or deactivates the override to force  
                parallel scheduling for the class name argument(s) in the evaluation manager.  
                Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".  
                When queried without specified nodes, it returns the list of nodes with the  
                parallel scheduling override active.  
                Scheduling overrides take precedence over all of the node and node type  
                scheduling rules. Use with caution; certain nodes may not react well to  
                alternative scheduling types.  
                Properties: create, query
        nodeTypeSerialize (bool?): This flag is used only when the evaluation manager is in "parallel" mode  
                but can be set at anytime. It activates or deactivates the override to force  
                local serial scheduling for the class name argument(s) in the evaluation manager.  
                Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".  
                When queried without specified nodes, it returns the list of nodes with the  
                local serial scheduling override active.  
                Scheduling overrides take precedence over all of the node and node type  
                scheduling rules. Use with caution; certain nodes may not react well to  
                alternative scheduling types.  
                Properties: create, query
        nodeTypeUntrusted (bool?): This flag is used only when the evaluation manager is in "parallel" mode  
                but can be set at anytime. It activates or deactivates the override to force  
                untrusted scheduling for the class name argument(s) in the evaluation manager.  
                Legal object values are class type names: e.g. "transform", "skinCluster", "mesh".  
                When queried without specified nodes, it returns the list of nodes with the  
                untrusted scheduling override active.  
                Scheduling overrides take precedence over all of the node and node type  
                scheduling rules. Use with caution; certain nodes may not react well to  
                alternative scheduling types.  
                Untrusted scheduling will allow nodes to be evaluated in a critical section,  
                separately from any other node evaluation. It should be used only as a last resort  
                since the lost parallelism caused by untrusted nodes can greatly reduce performance.  
                Properties: create, query
        upstreamFrom (str?): Find the DG nodes that are immediately upstream of the named one in  
                the evaluation graph. Note that the connectivity is via evaluation mode  
                connections, not DG connections.  
                In query mode the graph is walked and any nodes upstream of the named  
                one are returned. The return type is alternating pairs of values that  
                represent the graph level and the node name, e.g. if you walk upstream  
                from C in the graph A -> B -> C then the return will be the array of  
                strings ("0","C","1","B","2","A"). Scripts can deconstruct this  
                information into something more visually recognizable. Note that cycles  
                are likely to be present so any such scripts would have to handle them.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        reduceGraphRebuild (bool?): This flag is used to activate evaluation manager mode to minimize rebuild when animated node are connected to EM prepopulated plug.  
                Properties: create, query
        safeMode (bool?): This flag activates/deactivates parallel evaluation safe mode. When  
                enabled, parallel execution will fall back to serial when evaluation  
                graph is missing dependencies. Detection is happening on scheduling  
                of parallel evaluation, which means potential fallback will happen at  
                the next evaluation.  
                WARNING: This mode should be disabled with extreme caution. It will  
                prevent parallel mode from falling back to serial mode when an invalid  
                evaluation is detected. Sometimes the evaluation will still work  
                correctly in those situations and use of this flag will keep the peak  
                parallel performance running. However since the safe mode is used to  
                catch invalid evaluation disabling it may also cause problems with  
                evaluation, anything from invalid values, missing evaluation, or even  
                crashes.  
                Properties: create, query

    Returns:
        List[str]: The names of all evaluation manager modes (querying without flags)
        List[str]: The names of all nodes involved in a cycle cluster with the selected one.
        bool: The success of activating of deactivating manipulation (with the 'manipulation' flag)
        bool: The manipulation active or inactive state (querying the 'manipulation' flag)
        bool: The manipulation prevalidation active or inactive state (querying the 'manipulationPrevalidation' flag)
        bool: The manipulation allowed or disallowed state (querying the 'manipulationReady' flag)
        bool: The success of setting the evaluation manager mode (with the 'mode' flag)
        bool: The success of setting the evaluation manager idle action (with the 'idleAction' flag)
        bool: False if there are any nodes in the evaluation graph (with the 'empty' flag)
        int: The Evaluation Manager idle action (querying with the 'idleAction' flag)
        bool: Is the evaluation graph currently valid? (querying with the 'invalidate' flag)
        bool: The success of setting the node type parallel scheduling mode (with the 'nodeTypeParallel' flag)
        List[bool]: The parallel scheduling states of specified node types (querying the 'nodeTypeParallel' flag with object(s))
        List[str]: The names of all node types in parallel scheduling mode (querying the 'nodeTypeParallel' flag alone)
        bool: The success of setting the node type serialized mode (with the 'nodeTypeSerialize' flag)
        List[bool]: The serialized states of specified node types (querying the 'nodeTypeSerialize' flag with object(s))
        List[str]: The names of all node types in serial scheduling mode (querying the 'nodeTypeSerialize' flag alone)
        bool: The success of setting the node type globally serialized mode (with the 'nodeTypeGloballySerialize' flag)
        List[bool]: The globally serialized states of specified node types (querying the 'nodeTypeGloballySerialize' flag with object(s))
        List[str]: The names of all node types in globally serialized scheduling mode (querying the 'nodeTypeGloballySerialize' flag alone)
        bool: The success of setting the node type untrusted mode (with the 'nodeTypeUntrusted' flag)
        List[bool]: The untrusted of specified node types (querying the 'nodeTypeUntrusted' flag with object(s))
        List[str]: The names of all node types in untrusted scheduling mode (querying the 'nodeTypeUntrusted' flag alone)
        str: The evaluation manager mode (querying with the 'mode' flag)
        List[str]: The names of all nodes immediately downstream/upstream of the named one(s) (with the 'upstreamFrom' or 'downstreamFrom' flags)
        List[str]: The list of reasons the evaluation manager has been disabled (querying the 'disableInfo' flag)
        bool: The state of fallback serial evaluation (querying the 'fallbackTriggered' flag)
        bool: The state of reduceGraphRebuild Support (querying the 'reduceGraphRebuild ' flag)

    Example:
    """

