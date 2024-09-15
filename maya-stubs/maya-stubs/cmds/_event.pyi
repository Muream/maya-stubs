from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def event(*args: str, edit: bool = ..., query: bool = ..., count: Queryable[int] = ..., delete: bool = ..., dieAtCollision: bool = ..., emit: Queryable[int] = ..., list: bool = ..., name: Queryable[str] = ..., proc: Queryable[Callable[..., Any]] = ..., random: bool = ..., rename: Queryable[str] = ..., select: bool = ..., split: Queryable[int] = ..., spread: Queryable[float] = ..., target: Queryable[str] = ...) -> Union[str, int, bool, Callable[..., Any], float]:
    """The event command assigns collision events to a particle object.
    Collision events are stored in multi-attributes in the particle shape.
    The event command returns the event name.
    Args:
        count (Queryable[int]?): Collision number (for each particle) to which this event  
                applies. Zero (the default) indicates that it applies to all  
                collisions.  
                Properties: query, edit
        delete (bool?): Delete the specified event.  
                Properties: create
        dieAtCollision (bool?): Particle dies at the collision specified by "count."  
                If no count value is given, die at first collision.  
                Properties: query, edit
        emit (Queryable[int]?): Emit n additional particles into the assigned target object.  
                The original (colliding) particle survives as well, and remains  
                in its original object.  The new particles have age zero and mass  
                equal to the emitting particle. They use the velocity inheritance  
                parameter of the target object.  
                Properties: query, edit
        list (bool?): List all events for the chosen shape, like this:  
                event1Name event2Name ...  
                If no shape identified, list all events for all shapes, like this:  
                shape1Name event1Name shape2Name event2Name...  
                Returns a string array.  
                Properties: create
        name (Queryable[str]?): Assign a name to an event you are creating, or identify an  
                event you wish to edit, query, or delete. See examples.  
                Properties: create, query, edit
        proc (Queryable[Callable[..., Any]]?): Specify a MEL proc to be called each time the event occurs.  
                This must be a global proc with arguments as follows:  
                global proc procName( string obj, int id, string objHit );  
                Arguments passed in are the name of the particle object, the  
                id of the particle which collided, and the name of the object  
                collided with.  You can use particle -id -q to get values of  
                the particle's attributes.  
                Properties: create, query, edit
        random (bool?): Used with -split and -emit flags.  If -random is set true  
                and -split or -emit is set to n, then a random number of particles  
                uniformly distributed between 1 and n will be created at the event.  
                Properties: query, edit
        rename (Queryable[str]?): Assign a new name to an event you are editing. See examples.  
                Properties: query
        select (bool?): This flag is obsolete.  See the -name flag.
        split (Queryable[int]?): Colliding particle splits into specified number of  
                new particles. These new particles become part of the assigned  
                target object. If no target has been assigned, they become part of  
                the same object.  The new particles inherit the current age of  
                the particle that split.  They use the velocity inheritance  
                parameter of the target object.  If you set both emit and split,  
                the event will do both: first emit new particles, then split  
                the original one. This is a change from earlier versions where emit  
                and split were mutually exclusive.  
                Properties: query, edit
        spread (Queryable[float]?): Particles created at collision will spread out a random amount  
                from the rebound direction of the colliding particle.  The spread is  
                specified as a fraction (0. 1) of 90 degrees.  If spread is set at 0  
                (the default) all the new particles created may coincide.  
                Properties: query, edit
        target (Queryable[str]?): Target object for emitting or split particles. New particles  
                created through the -emit or -split flags join this object.  
                Properties: query, edit

    Returns:
        str: for creation; string array for list.

    Example:
    """

