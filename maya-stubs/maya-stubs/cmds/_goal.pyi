from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def goal(*args: str, query: bool = ..., goal: Queryable[Multiuse[str]] = ..., index: bool = ..., useTransformAsGoal: bool = ..., weight: float = ...) -> Union[str, Multiuse[str], bool]:
    """Specifies the given objects as being goals for the given particle
    object.  If the goal objects are geometry, each particle in the particle
    object will each try to follow or match its position to that of a certain
    vertex/CV/lattice point of the goal.  If the goal object is another
    particle object, each particle will try to follow a paricle of the goal.
    In any other case, all the particles will try to follow the current location
    of the goal object's transform.  You can get this latter behavior for
    a geometry or particle object too by using -utr true.The goal weight can be keyframed.  It lives on the particle object to
    which the goal was added and is a multi-attribute.
    Args:
        goal (Queryable[Multiuse[str]]?): This flag specifies string to be a goal of the particle object on  
                the command line or the currently selected particle object.  This flag  
                can be used multiple times to specify multiple goals for a particle  
                object.  Query is for use by the attribute editor.  
                Properties: create, query, multiuse
        index (bool?): Returns array of multi-attribute indices for the goals.  
                Intended for use by the Attribute Editor.  
                Properties: query
        useTransformAsGoal (bool?): Use transform of specified object instead of the shape.  
                Meaningful only for particle and geometry objects.  Can only be  
                passed once, applies to all objects passed with -g.  
                Properties: create
        weight (float?): This specifies the goal weight as a value from 0 to 1.  A value of 0  
                means that the goal's position will have no effect on the particle  
                object, while a weight of 1 will make the particle object try to follow  
                the goal object exactly.  This flag can only be passed once and sets  
                the weight for every goal passed with the -g/-goal flag.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

