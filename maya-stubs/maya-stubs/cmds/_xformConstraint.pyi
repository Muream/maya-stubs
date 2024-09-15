from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def xformConstraint(*, edit: bool = ..., query: bool = ..., alongNormal: Queryable[int] = ..., live: bool = ..., type: Queryable[str] = ...) -> Union[bool, int, str]:
    """This command allows you to change the transform constraint used by the
    transform tools during component transforms.
    Args:
        alongNormal (Queryable[int]?): When set the transform constraint will first be applied along the  
                vertex normals of the components being transformed. When queried,  
                returns the current state of this option.  
                Properties: query, edit
        live (bool?): Query-only flag that can be used to check whether the current  
                live surface will be used as a transform constraint.  
                Properties: query
        type (Queryable[str]?): Set the type of transform constraint to use. When queried,  
                returns the current transform constraint as a string.  
              
                none - no constraint  
                surface - constrain components to their surface  
                edge - constrain components to surface edges  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

