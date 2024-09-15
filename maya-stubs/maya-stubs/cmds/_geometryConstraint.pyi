from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def geometryConstraint(*args: str, edit: bool = ..., query: bool = ..., layer: str = ..., name: Queryable[str] = ..., remove: bool = ..., targetList: bool = ..., weight: Queryable[float] = ..., weightAliasList: bool = ...) -> Union[List[str], str, bool, float]:
    """Constrain an object's position based on the shape of the target
    surface(s) at the closest point(s) to the object.A geometryConstraint takes as input one or more surface shapes (the
    targets) and a DAG transform node (the object).  The
    geometryConstraint position constrained object such object lies on
    the surface of the target with the greatest weight value.  If two
    targets have the same weight value then the one with the lowest index
    is chosen.
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
        List[str]: Name of the created constraint node

    Example:
    """

