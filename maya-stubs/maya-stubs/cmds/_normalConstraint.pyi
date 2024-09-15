from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def normalConstraint(*args: str, edit: bool = ..., query: bool = ..., aimVector: Queryable[Tuple[float, float, float]] = ..., layer: str = ..., name: Queryable[str] = ..., remove: bool = ..., targetList: bool = ..., upVector: Queryable[Tuple[float, float, float]] = ..., weight: Queryable[float] = ..., weightAliasList: bool = ..., worldUpObject: Queryable[str] = ..., worldUpType: Queryable[str] = ..., worldUpVector: Queryable[Tuple[float, float, float]] = ...) -> Union[List[str], Tuple[float, float, float], str, bool, float]:
    """Constrain an object's orientation based on the normal of the target
    surface(s) at the closest point(s) to the object.A normalConstraint takes as input one or more surface shapes (the
    targets) and a DAG transform node (the object).  The normalConstraint
    orients the constrained object such that the aimVector (in the
    object's local coordinate system) aligns in world space to combined
    normal vector.  The upVector (again the the object's local coordinate
    system) is aligned in world space with the worldUpVector.  The
    combined normal vector is a weighted average of the normal vector
    for each target surface at the point closest to the constrained object.
    Args:
        aimVector (Queryable[Tuple[float, float, float]]?): Set the aim vector.  This is the vector in local  
                coordinates that points at the target.  If not given at creation  
                time, the default value of (1.0, 0.0, 0.0) is used.  
                Properties: create, query, edit
        layer (str?): Specify the name of the animation layer where the constraint should be added.  
                Properties: create, edit
        name (Queryable[str]?): Sets the name of the constraint node to the specified  
                name.  Default name is constrainedObjectName_constraintType  
                Properties: create, query, edit
        remove (bool?): removes the listed target(s) from the constraint.  
                Properties: edit
        targetList (bool?): Return the list of target objects.  
                Properties: query
        upVector (Queryable[Tuple[float, float, float]]?): Set local up vector.  This is the vector in local  
                coordinates that aligns with the world up vector.  If not given  
                at creation time, the default value of (0.0, 1.0, 0.0) is used.  
                Properties: create, query, edit
        weight (Queryable[float]?): Sets the weight value for the specified target(s).  
                If not given at creation time, the default value of 1.0 is used.  
                Properties: create, query, edit
        weightAliasList (bool?): Returns the names of the attributes that control the weight  
                of the target objects. Aliases are returned in the same order  
                as the targets are returned by the targetList flag  
                Properties: query
        worldUpObject (Queryable[str]?): Set the DAG object use for worldUpType "object" and  
                "objectrotation". See worldUpType for greater detail.  
                The default value is no up object, which is interpreted  
                as world space.  
                Properties: create, query, edit
        worldUpType (Queryable[str]?): Set the type of the world up vector computation.  
                The worldUpType can have one of 5 values: "scene",  
                "object", "objectrotation", "vector", or "none".  
                If the value is "scene", the upVector is  
                aligned with the up axis of the scene and  
                worldUpVector and worldUpObject are ignored.  
                If the value is "object", the upVector is  
                aimed as closely as possible to the  
                origin of the space of the worldUpObject and  
                the worldUpVector is ignored.  
                If the value is "objectrotation" then the  
                worldUpVector is interpreted as being in  
                the coordinate space of the worldUpObject, transformed into  
                world space and the upVector is aligned as  
                closely as possible to the result.  
                If the value is "vector", the upVector  
                is aligned with worldUpVector as closely as  
                possible and worldUpMatrix is ignored.  
                Finally, if the value is "none" no twist calculation  
                is performed by the constraint, with the resulting "upVector"  
                orientation based previous orientation of the  
                constrained object, and the "great circle" rotation needed  
                to align the aim vector with its constraint.  
                The default worldUpType is "vector".  
                Properties: create, query, edit
        worldUpVector (Queryable[Tuple[float, float, float]]?): Set world up vector.  This is the vector in world  
                coordinates that up vector should align with.  
                See -wut/worldUpType (below)for greater detail.  
                If not given at creation time, the default  
                value of (0.0, 1.0, 0.0) is used.  
                Properties: create, query, edit

    Returns:
        List[str]: Name of the created constraint node

    Example:
    """

