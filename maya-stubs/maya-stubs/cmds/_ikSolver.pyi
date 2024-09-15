from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikSolver(*args: str, edit: bool = ..., query: bool = ..., epsilon: Queryable[float] = ..., maxIterations: Queryable[int] = ..., name: Queryable[str] = ..., solverType: Queryable[str] = ...) -> Union[str, float, int]:
    """The ikSolver command is used to set the attributes for an IK Solver
    or create a new one. The standard edit (-e) and query (-q) flags are
    used for edit and query functions.
    Args:
        epsilon (Queryable[float]?): max error  
                Properties: create, query, edit
        maxIterations (Queryable[int]?): Sets the max iterations for a solution  
                Properties: create, query, edit
        name (Queryable[str]?): Name of solver  
                Properties: create, query, edit
        solverType (Queryable[str]?): valid solverType (only ikSystem knows what is valid) for  
                creation of a new solver (required)  
                Properties: create, query, edit

    Returns:
        str: Command result

    Example:
    """

