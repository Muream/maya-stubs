from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def constrain(*args: str, edit: bool = ..., query: bool = ..., barrier: bool = ..., damping: Queryable[float] = ..., directionalHinge: bool = ..., hinge: bool = ..., interpenetrate: bool = ..., nail: bool = ..., name: Queryable[str] = ..., orientation: Queryable[Tuple[float, float, float]] = ..., pinConstraint: bool = ..., position: Queryable[Tuple[float, float, float]] = ..., restLength: Queryable[float] = ..., spring: bool = ..., stiffness: Queryable[float] = ...) -> Union[bool, float, str, Tuple[float, float, float]]:
    """This command constrains rigid bodies to the world or other rigid bodies.
    Args:
        barrier (bool?): Creates a barrier constraint.  This command requires one rigid bodies.  
                Properties: create, query
        damping (Queryable[float]?): Sets the damping constant.  
                Default value: 0.1  
                Range: -1000.0 to 1000.0  
                Properties: create, query, edit
        directionalHinge (bool?): Creates a directional hinge constraint.  This command requires two rigid bodies.  
                The directional hinge always maintains the initial direction of its axis.  
                Properties: create, query
        hinge (bool?): Creates a hinge constraint.  This command requires one or two rigid bodies.  
                Properties: create, query
        interpenetrate (bool?): Allows (or disallows) the rigid bodies defined in the constrain to ipenetrate.  
                Properties: create, query, edit
        nail (bool?): Creates a nail constraint.  This command requires one rigid body.  
                Properties: create, query
        name (Queryable[str]?): Names the rigid constraint.  
                Properties: create, query, edit
        orientation (Queryable[Tuple[float, float, float]]?): Set initial orientation of the constraint in world space.  This  
                command is only valid with hinge and barrier constraints  
                Default value: 0.0 0.0 0.0  
                Properties: create, query, edit
        pinConstraint (bool?): Creates a pin constraint.  This command requires two rigid bodies.  
                Properties: create, query
        position (Queryable[Tuple[float, float, float]]?): Set initial position of the constraint in world space.  
                Default value: 0.0 0.0 0.0 for uni-constraints, midpoint of bodies for deul constraint.  
                Properties: create, query, edit
        restLength (Queryable[float]?): Sets the rest length.  
                Default value: 1.0  
                Properties: create, query, edit
        spring (bool?): Creates a spring constraint.  This command requires one or two rigidies.  
                Properties: create, query
        stiffness (Queryable[float]?): Sets the springs stiffness constant.  
                Default value: 5.0  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

