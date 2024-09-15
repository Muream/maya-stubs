from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pointConstraint(*args: str, edit: bool = ..., query: bool = ..., layer: str = ..., maintainOffset: bool = ..., name: Queryable[str] = ..., offset: Queryable[Tuple[float, float, float]] = ..., remove: bool = ..., skip: Multiuse[str] = ..., targetList: bool = ..., weight: Queryable[float] = ..., weightAliasList: bool = ...) -> Union[List[str], str, Tuple[float, float, float], bool, float]:
    """Constrain an object's position to the position of the target object or
    to the average position of a number of targets.A pointConstraint takes as input one or more "target" DAG transform
    nodes at which to position the single "constraint object" DAG
    transform node.  The pointConstraint positions the constrained object
    at the weighted average of the world space position target
    objects.
    Args:
        layer (str?): Specify the name of the animation layer where the constraint should be added.  
                Properties: create, edit
        maintainOffset (bool?): The offset necessary to preserve the constrained  
                object's initial position will be calculated and used as the  
                offset.  
                Properties: create
        name (Queryable[str]?): Sets the name of the constraint node to the specified  
                name.  Default name is constrainedObjectName_constraintType  
                Properties: create, query, edit
        offset (Queryable[Tuple[float, float, float]]?): Sets or queries the value of the offset. Default is 0,0,0.  
                Properties: create, query, edit
        remove (bool?): removes the listed target(s) from the constraint.  
                Properties: edit
        skip (Multiuse[str]?): Specify the axis to be skipped. Valid values are "x", "y", "z" and "none". During creation, "none" is the default. This flag is multi-use.  
                Properties: create, edit, multiuse
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
        List[str]: Name of the created constraint node

    Example:
    """

