from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def poleVectorConstraint(*args: str, edit: bool = ..., query: bool = ..., layer: str = ..., name: Queryable[str] = ..., remove: bool = ..., targetList: bool = ..., weight: Queryable[float] = ..., weightAliasList: bool = ...) -> Union[List[str], str, bool, float]:
    """Constrains the poleVector of an ikRPsolve handle to point at a
    target object or at the average position of a number of targets.An poleVectorConstraint takes as input one or more "target" DAG
    transform nodes at which to aim pole vector for an IK handle using
    the rotate plane solver.  The pole vector is adjust such that
    the in weighted average of the world space position target
    objects lies is the "rotate plane" of the handle.
    Args:
        layer (str?): Specify the name of the animation layer where the constraint should be added.  
                Properties: create, edit
        name (Queryable[str]?): Sets the name of the constraint node to the specified  
                name.  Default name is constrainedObjectName_constraintType  
                Properties: create, query, edit
        remove (bool?): removes the listed target(s) from the constraint.  
                Properties: edit
        targetList (bool?): Return the list of target objects.  
                Properties: query
        weight (Queryable[float]?): Sets the weight value for the specified target(s).  
                If not given at creation time, the default value of 1.0 is used.  
                Properties: create, query, edit
        weightAliasList (bool?): Returns the names of the attributes that control the weight  
                of the target objects. Aliases are returned in the same order  
                as the targets are returned by the targetList flag  
                Properties: query

    Returns:
        List[str]: name of the created constraint node

    Example:
    """

