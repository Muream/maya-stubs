from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgValidateCurve(*args: str, allCurves: bool = ..., verbose: bool = ...) -> int:
    """Thecommand is used to make sure the curve internal
    status matches their actual state.
    It forces checks on curves that might not be tagged as static, even if they are.
    The DG tracks static curves in order to optimize evaluation by not
    considering them animated.  Once keys are added and modified on the
    curve, it is no longer static.  Certain operations on the curve might
    make it flat / without animation, but the DG will not treat it as
    static because it expects it to be modified again soon.
    This command allows to explicitly request checks for the static state
    of animation curves.dg, dependency, graph, dirty, static, curve
    Args:
        allCurves (bool?): Ignore the selected or specified objects and work on all curves.  
                Properties: create
        verbose (bool?): Prints out all of the curves set static or not.  
                Properties: create

    Returns:
        int: Number of curves which changed their static status.

    Example:
    """

