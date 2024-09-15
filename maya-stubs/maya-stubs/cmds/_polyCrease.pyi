from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def polyCrease(*args: str, edit: bool = ..., query: bool = ..., createHistory: bool = ..., operation: Queryable[int] = ..., relativeValue: Queryable[float] = ..., value: Queryable[Multiuse[float]] = ..., vertexValue: Queryable[Multiuse[float]] = ...) -> Union[bool, int, float, Multiuse[float]]:
    """Command to set the crease values on the edges or vertices
    of a poly.  The crease values are used by the smoothing
    algorithm.poly, crease, smooth, subdiv
    Args:
        createHistory (bool?): For objects that have no construction history, this flag can be used  
                to force the creation of construction history for creasing.  By default,  
                history is not created if the object has no history.  Regardless of this  
                flag, history is always created if the object already has history.  
                Properties: create, query, edit
        operation (Queryable[int]?): Operation to perform.  Valid values are:  
                0. Crease the specified components.  
                1. Remove the crease values for the specified components.  
                2. Remove all crease values from the mesh.  
                Default is 0.  
                Properties: create, query, edit
        relativeValue (Queryable[float]?): Specifies a new relative value for all selected vertex and edge components.  
                This flag can not be used at the same time as either the value or vertexValue  
                flags.  
                Properties: create, query, edit
        value (Queryable[Multiuse[float]]?): Specifies the crease value for the selected edge components.  
                When specified multiple times, the values are assigned respectively to  
                the specified edges.  
                Properties: create, query, edit, multiuse
        vertexValue (Queryable[Multiuse[float]]?): Specifies the crease value for the selected vertex components.  
                When specified multiple times, the values are assigned respectively to  
                the specified vertices.  
                Properties: create, query, edit, multiuse

    Returns:
        bool: Success or Failure.

    Example:
    """

