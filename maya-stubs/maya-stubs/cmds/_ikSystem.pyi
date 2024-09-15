from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikSystem(*, edit: bool = ..., query: bool = ..., allowRotation: bool = ..., autoPriority: bool = ..., autoPriorityMC: bool = ..., autoPrioritySC: bool = ..., list: Queryable[Tuple[int, int]] = ..., snap: bool = ..., solve: bool = ..., solverTypes: bool = ...) -> Union[str, bool, Tuple[int, int]]:
    """The ikSystem command is used to set the global snapping flag for handles
    and set the global solve flag for solvers.  The standard edit (-e) and
    query (-q) flags are used for edit and query functions.
    Args:
        allowRotation (bool?): Set true to allow rotation of an ik handle with keys set on  
                translation.  
                Properties: query, edit
        autoPriority (bool?): set autoPriority for all ikHandles  
                Properties: edit
        autoPriorityMC (bool?): set autoPriority for all multiChain handles  
                Properties: edit
        autoPrioritySC (bool?): set autoPriority for all singleChain handles  
                Properties: edit
        list (Queryable[Tuple[int, int]]?): returns the solver execution order when in query  
                mode(list of strings) changes execution order when in edit mode  
                (int old position, int new position)  
                Properties: query, edit
        snap (bool?): Set global snapping  
                Properties: query, edit
        solve (bool?): Set global solve  
                Properties: query, edit
        solverTypes (bool?): returns a list of valid solverTypes ( query only )  
                Properties: query

    Returns:
        str: Command result

    Example:
    """

