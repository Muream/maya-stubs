from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgeval(*args: str, src: bool = ..., verbose: bool = ...) -> bool:
    """Thecommand is used to force a dependency graph
    evaluate of a node or plug.  Used for debugging to find
    propagation problems.Normally the selection list is used to determine which objects to
    evaluate, but you can add to the selection list by specifying which
    objects you want on the command line.
    Args:
        src (bool?): This flag is obsolete. Do not use.  
                Properties: create
        verbose (bool?): If this flag is used then the results of the evaluation(s) is/are  
                printed on stdout.  
                Properties: create

    Returns:
        bool:

    Example:
    """

