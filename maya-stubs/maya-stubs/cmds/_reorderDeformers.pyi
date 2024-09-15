from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def reorderDeformers(arg0: str = ..., arg1: str = ..., /, *args: str, name: str = ...) -> bool:
    """This command changes the order in which 2 deformation nodes affect the
    output geometry. The first string argument is the name of deformer1,
    the second is deformer2, followed by the list of objects they
    deform.It inserts deformer2 before deformer1. Currently supported deformer
    nodes include: sculpt, cluster, jointCluster, lattice, wire,
    jointLattice, boneLattice, blendShape.
    Args:
        name (str?): This flag is obsolete and is not used.  
                Properties: create

    Returns:
        bool:

    Example:
    """

