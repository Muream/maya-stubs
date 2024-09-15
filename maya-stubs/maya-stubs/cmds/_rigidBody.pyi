from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rigidBody(*args: str, edit: bool = ..., query: bool = ..., active: bool = ..., angularVelocity: bool = ..., applyForceAt: Queryable[str] = ..., bounciness: Queryable[float] = ..., cache: bool = ..., centerOfMass: Queryable[Tuple[float, float, float]] = ..., collisions: bool = ..., contactCount: bool = ..., contactName: bool = ..., contactPosition: bool = ..., damping: Queryable[float] = ..., deleteCache: bool = ..., dynamicFriction: Queryable[float] = ..., force: bool = ..., ignore: bool = ..., impulse: Tuple[float, float, float] = ..., impulsePosition: Tuple[float, float, float] = ..., initialAngularVelocity: Queryable[Tuple[float, float, float]] = ..., initialVelocity: Queryable[Tuple[float, float, float]] = ..., layer: Queryable[int] = ..., lockCenterOfMass: bool = ..., mass: Queryable[float] = ..., name: Queryable[str] = ..., orientation: Queryable[Tuple[float, float, float]] = ..., particleCollision: bool = ..., passive: bool = ..., position: Queryable[Tuple[float, float, float]] = ..., removeShape: Queryable[str] = ..., solver: Queryable[str] = ..., spinImpulse: Tuple[float, float, float] = ..., standInObject: Queryable[str] = ..., staticFriction: Queryable[float] = ..., tesselationFactor: Queryable[int] = ..., velocity: bool = ...) -> Union[str, bool, float, Tuple[float, float, float], int]:
    """This command creates a rigid body from a polygonal or nurbs surface.
    Args:
        active (bool?): Creates a rigid body that is active.  An active rigid body accepts and  
                causes collisions and is effected by dynamic fields.  This is the  
                default.  
                Properties: create, query, edit
        angularVelocity (bool?): Current angular velocity of rigid body.  
                Properties: query
        applyForceAt (Queryable[str]?): Determines how forces are applied to the rigid body.  
                The choices are centerOfMass | boundingBox | verticesOrCVs.  
                Default: boundingBox  
                Properties: create, query, edit
        bounciness (Queryable[float]?): Sets the restitution (or bounciness) of the rigid body.  
                Range:   0.0. 2.0  
                Default: 0.6  
                Properties: create, query, edit
        cache (bool?): Turns caching on (1) or off (0) for the rigid body.  
                Default: off  
                Properties: create, query, edit
        centerOfMass (Queryable[Tuple[float, float, float]]?): Sets the center of mass (x,y,z) of the rigid body.  
                Default: actual center of mass.  
                Properties: create, query, edit
        collisions (bool?): Truns collisions on/off for the rigid body.  If the collisions  
                are turned of the rigid body will not collide with any other rigid body.  
                Default: on.  
                Properties: create, query, edit
        contactCount (bool?): returns the current contact count for the rigid body.  
                Properties: query
        contactName (bool?): returns all the rigid body names which are in contact with this shape.  One name  
                for each contact will be returned.  
                Properties: query
        contactPosition (bool?): returns all the contact position.  One position for each contact  
                will be returned.  
                Properties: query
        damping (Queryable[float]?): Sets the damping value of the rigid body.  
                Range:   -2.0. 2.0  
                Default: 0.0  
                Properties: create, query, edit
        deleteCache (bool?): Deletes the cache (if one exists) of the rigid body.  
                Properties: edit
        dynamicFriction (Queryable[float]?): Sets the dynamic friction for the rigid body.  
                Range:   0.0. 1.0  
                Default: 0.2  
                Properties: create, query, edit
        force (bool?): Current force on the rigid body.  
                Properties: query
        ignore (bool?): Causes the rigid body to be ignored in the rigid solver.  
                Default: off  
                Properties: create, query, edit
        impulse (Tuple[float, float, float]?): Applies an impulse (instantaneous) force on a rigid body.  
                Default: 0.0 0.0 0.0  
                Properties: create, edit
        impulsePosition (Tuple[float, float, float]?): The position at which the impulse is applied.  
                Default: the bodies center of mass.  
                Properties: create, edit
        initialAngularVelocity (Queryable[Tuple[float, float, float]]?): Sets the initial angular velocity of the rigid body.  
                Default: 0.0 0.0 0.0  
                Properties: create, query, edit
        initialVelocity (Queryable[Tuple[float, float, float]]?): Sets the initial velocity of the rigid body.  
                Default: 0.0 0.0 0.0  
                Properties: create, query, edit
        layer (Queryable[int]?): Sets the collision layer of the rigid body.  Only rigid bodies in the  
                same collision layer can collide with each other.  
                Range:   >= 0  
                Default: 0.  
                Properties: create, query, edit
        lockCenterOfMass (bool?): Locks the center of mass for the rigid body.  
                Default: off  
                Properties: create, query, edit
        mass (Queryable[float]?): Sets the mass of the rigid body.  
                Range:   > 0  
                Default: 1.0  
                Properties: create, query, edit
        name (Queryable[str]?): Assigns the rigid body the given name.  
                Properties: create, query, edit
        orientation (Queryable[Tuple[float, float, float]]?): Sets the initial orientation (x,y,z) of the rigid body.  
                Default: current orientation.  
                Properties: create, query, edit
        particleCollision (bool?): Turns the ability for a rigid body to collide with particles  
                on and off.  The particles will exert a force on the rigid body.  
                Default: off  
                Properties: create, query, edit
        passive (bool?): Creates a rigid body that is passive.  A passive rigid body does not  
                react to collisions but active rigid bodies can collide with it.  
                Dynamic Fields will not effect a passive rigid body.  Only passive  
                rigid bodies can be keyframed.  
                Properties: create, query, edit
        position (Queryable[Tuple[float, float, float]]?): Sets the initial position (x,y,z) of the rigid body.  
                Default: current position.  
                Properties: create, query, edit
        removeShape (Queryable[str]?): Remove the named shape.  
                Properties: create, query, edit
        solver (Queryable[str]?): The name of the solver which this rigid node is to resided.  If the  
                solver does not exists then the rigid body will not be created.  If the  
                edit flag is thrown add the solver exists, the rigid body will be moved  
                to that solver.  
                Properties: create, query, edit
        spinImpulse (Tuple[float, float, float]?): Applies an spin impulse (instantaneous rotational) force on a rigid body.  
                Default: 0.0 0.0 0.0  
                Properties: create, edit
        standInObject (Queryable[str]?): Causes the simulator to use a stand in object for the simulation.  
                The choices are none | cube | sphere. The default is none.  
                Default: none  
                Properties: create, query, edit
        staticFriction (Queryable[float]?): Sets the static friction for the rigid body.  
                Range:   0.0. 1.0  
                Default: 0.2  
                Properties: create, query, edit
        tesselationFactor (Queryable[int]?): Sets the tesselation factor for a rigid body surface.  
                Range:   >= 10  
                Default: 200.  
                Properties: create, query
        velocity (bool?): Current velocity of rigid body.  
                Properties: query

    Returns:
        str: New rigid body name.

    Example:
    """

