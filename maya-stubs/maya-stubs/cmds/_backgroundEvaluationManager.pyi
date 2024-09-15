from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def backgroundEvaluationManager(*args: str, query: bool = ..., interrupt: bool = ..., mode: Queryable[str] = ..., pause: bool = ..., resume: bool = ...) -> Union[bool, str]:
    """Allows user to pause and restart background evaluations.async, background, time, evaluation, manager, DG, runtime
    Args:
        interrupt (bool?): Enable or disable fast interrupt of background execution during interactive workflow.  
                Properties: create, query
        mode (Queryable[str]?): Changes the current evaluation mode in the evaluation manager. Supported values are  
                "serial" and "parallel".  
                Properties: create, query
        pause (bool?): Pause background evaluation. Will block till background evaluation is fully stopped.  
                Can be queried to get the current state.  
                Properties: create, query
        resume (bool?): Resume background evaluation. Will start suspended evaluations unless someones else requested it.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

