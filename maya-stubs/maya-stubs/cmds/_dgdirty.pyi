from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgdirty(*args: str, query: bool = ..., allPlugs: bool = ..., clean: bool = ..., implicit: bool = ..., list: Queryable[str] = ..., propagation: bool = ..., showTiming: bool = ..., verbose: bool = ...) -> Union[List[str], int, bool, str]:
    """Thecommand is used to force a dependency graph
    dirty message on a node or plug.  Used for debugging to find
    evaluation problems.  If no nodes are specified then the current
    selection list is used.
    If theflag is used it will return the list of things
    currently marked as dirty (or clean if theflag was
    also used). The returned values will be the names of plugs either
    clean/dirty themselves, at both ends of a clean/dirty connection,
    or representing the location of clean/dirty data on the node.
    Be careful using this option in conjunction with
    theflag, the list could be huge.dg, dependency, graph, dirty, plug, state
    Args:
        allPlugs (bool?): Ignore the selected or specified objects and dirty (or clean)  
                all plugs.  
                Properties: create, query
        clean (bool?): If this flag is set then the attributes are cleaned.  Otherwise  
                they are set to dirty.  
                Properties: create, query
        implicit (bool?): If this flag is set then allow the implicit or default nodes to be  
                processed as well. Otherwise they will be skipped for efficiency.  
                Properties: create, query
        list (Queryable[str]?): When this flag is specified then instead of sending out dirty/clean  
                messages the list of currently dirty/clean objects will be returned.  
                The allPlugs and clean flags are respected to narrow  
                guide the values to be returned.  
                The value of the flag tells what will be reported.  
              
                "data" or "d" = show plugs that have dirty/clean data  
                "plug" or "p" = show plugs that have dirty/clean states  
                "connection" or "c" = show plugs with connections that have dirty/clean states  
                Query this flag to find all legal values of the flag. Query this flag with  
                its value already set to get a description of what that value means.  
              
                Note that "p" and "c" modes are restricted to plugs that have connections  
                or non-standard state information. Other attributes will not have state  
                information to check, though they will have data.  
                In the case of array attributes only the children that have values  
                currently set will be considered. No attempt will be made to evaluate  
                them in order to update the available child lists.  
                e.g. if you have a DAG with transform T1 and shape S1 the instanced  
                attribute S1.wm[0] will be reported. If in a script you create a second  
                instance T2. >S1 and immediately list the plugs again before evaluation  
                you will still only see S1.wm[0]. The new S1.wm[1] won't be reported  
                until it is created through an evaluation, usually caused by refresh,  
                a specific getAttr command, or an editor update.  
                Note that the list is only for selected nodes. Unlike when dirty  
                messages are sent this does not travel downstream.  
                Properties: create, query
        propagation (bool?): If this flag is set then the ability of dirty messages to flow through  
                the graph is left enabled.  
                Properties: create, query
        showTiming (bool?): If this flag is used then show how long the dirty messages took  
                to propagate.  
                Properties: create, query
        verbose (bool?): Prints out all of the plugs being set dirty on stdout.  
                Properties: create, query

    Returns:
        List[str]: List of dirty/clean plugs in list plug mode.
        List[str]: List of plugs with dirty/clean data in list data mode.
        List[str]: Pairs of dirty/clean connected plugs in list connection mode.
        int: Number of dirty/clean messages sent out in normal mode.

    Example:
    """

