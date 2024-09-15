from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def collision(*args: str, edit: bool = ..., query: bool = ..., friction: Queryable[float] = ..., name: Queryable[str] = ..., offset: Queryable[float] = ..., resilience: Queryable[float] = ...) -> Union[List[str], float, str]:
    """For each listed object, the command creates a new field.
    The field has a shape which lives in the DAG and it has an associated
    dependency node. The field is added to the list of fields owned
    by the object. Use connectDynamic to cause the field to affect a dynamic
    object. Note that if more than one object is listed, a separate field is
    created for each object.If fields are created, this command returns the names of each
    owning shape and of the field shapes themselves. If a field was queried,
    the results of the query are returned. If a field was edited, the field
    name is returned.If no object names are provided but the active selection list is non-empty,
    the command creates a field for every object in the list. If the
    list is empty, the command defaults to -pos 0 0 0.
    The collision command causes particles to collide with geometry.
    It also allows you to specify values for the surface properties
    (friction and resilience) of the collision.  These values are stored
    in the geoConnector node for the geometry object.  Unlike earlier versions
    of Maya, there is no separate "collision node."If a soft object is in the selection list, the collision command assumes
    that you want to make it a collider.  In order to make the soft object
    collide with something use, use connectDynamic -c.  The collision menu
    option sorts this out using the lead object rule and issues the necessary
    commands.
    On creation, this command returns aof the geometry names that were setup for particle collision.When the command is used to query information, there are several possible return types.
    These include:
    Args:
        friction (Queryable[float]?): Friction of the surface.  This is the amount of the colliding particle's  
                velocity parallel to the surface which is removed when the particle collides.  
                A value of 0 will mean that no tangential velocity is lost, while a value  
                of 1 will cause the particle to reflect straight along the normal of  
                the surface.  
                Properties: query, edit
        name (Queryable[str]?): name of field  
                Properties: query, edit
        offset (Queryable[float]?): Offset value for the connector.  
                Properties: query, edit
        resilience (Queryable[float]?): Resilience of the surface.  This is the amount of the colliding particle's  
                velocity reflected along the normal of the surface.  A value of 1 will  
                give perfect reflection, while a value of 0 will have no reflection along  
                the normal of the surface.  
                Properties: query, edit

    Returns:
        List[str]: Geometry names that were setup for particle collision.

    Example:
    """

