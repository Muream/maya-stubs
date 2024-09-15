from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rigidSolver(*args: str, edit: bool = ..., query: bool = ..., autoTolerances: bool = ..., bounciness: bool = ..., cacheData: bool = ..., collide: bool = ..., collisionTolerance: Queryable[float] = ..., contactData: bool = ..., create: bool = ..., current: bool = ..., deleteCache: bool = ..., displayCenterOfMass: bool = ..., displayConstraint: bool = ..., displayVelocity: bool = ..., dynamics: bool = ..., friction: bool = ..., interpenetrate: bool = ..., interpenetrationCheck: bool = ..., name: Queryable[str] = ..., rigidBodies: bool = ..., rigidBodyCount: bool = ..., showCollision: bool = ..., showInterpenetration: bool = ..., solverMethod: Queryable[int] = ..., startTime: Queryable[float] = ..., state: bool = ..., statistics: bool = ..., stepSize: Queryable[float] = ..., velocityVectorScale: Queryable[float] = ...) -> Union[bool, float, str, int]:
    """This command sets the attributes for the rigid solver
    Args:
        autoTolerances (bool?): Turns the auto tolerance calculation on and off.  The auto tolerances  
                calculation will override the default or user defined values of the  
                step size and collision tolerance value that is calculated based  
                on the objects in the scene.  
                Default: 0 (off)  
                Properties: query, edit
        bounciness (bool?): Turns bounciness on and off for the an the objects in the  
                simulation.  
                Default value: on  
                Properties: query, edit
        cacheData (bool?): Turns the cache on fall all rigid bodies in the system.  
                Default value: off  
                Properties: query, edit
        collide (bool?): Disallows the interpenetration of the two rigid bodies listed.  
                Default: Collide is on for all bodies.  
                Properties: query, edit
        collisionTolerance (Queryable[float]?): Sets the collision tolerance.  This is the error at which two objects  
                are considered to have collided.  
                Range:   0.0005. 1.000  
                Default: 0.02  
                Properties: query, edit
        contactData (bool?): Turns the contact data information on/off for all rigid bodies.  
                Default value: off  
                Properties: query, edit
        create (bool?): Creates a new rigid solver.  
                Properties: create
        current (bool?): Sets rigid solver as the current solver.  
                Properties: create
        deleteCache (bool?): Deletes the cache for all rigid bodies in the system.  
                Properties: query, edit
        displayCenterOfMass (bool?): Displays the center of mass icon.  
                Default value: on  
                Properties: query, edit
        displayConstraint (bool?): Displays the constraint vectors.  
                Default value: on  
                Properties: query, edit
        displayVelocity (bool?): Displays the velocity vectors.  
                Default value: off  
                Properties: query, edit
        dynamics (bool?): Turns dynamics on and off for the an the objects in the simulation.  
                Default value: on  
                Properties: query, edit
        friction (bool?): Turns friction on and off for the an the objects in the simulation.  
                Default value: on  
                Properties: query, edit
        interpenetrate (bool?): Allows the two rigid bodies listed to interpenetrate.  
                Default: interpenetration is off for all bodies.  
                Properties: query, edit
        interpenetrationCheck (bool?): Checks for interpenetrating rigid bodies in the scene.  
                Properties: edit
        name (Queryable[str]?): Name of the new object  
                Properties: create, query, edit
        rigidBodies (bool?): Returns a list of rigid bodies in the solver.  
                Properties: query
        rigidBodyCount (bool?): Returns the number of rigid bodies in the solver.  
                Properties: query
        showCollision (bool?): Displays the colliding objects in a different color.  
                Properties: query, edit
        showInterpenetration (bool?): Displays the interpenetrating objects in a different color.  
                Properties: query, edit
        solverMethod (Queryable[int]?): Sets the solver method.  The choices are 0 | 1 | 2.  
                0 = Euler (fastest/least acurate),  
                1 = Runge-Kutta ( slower/more acurate),  
                2 = adaptive Runge-Kutta  
                (slowest/most acurate).  
                The default is 2 (adaptive Runge-Kutta)  
                Properties: query, edit
        startTime (Queryable[float]?): Sets the start time for the solver.  
                Properties: create, query, edit
        state (bool?): Turns the rigid solver on or off.  
                Properties: query, edit
        statistics (bool?): Turns the statistic information on/off for all rigid bodies.  
                Default value: off  
                Properties: query, edit
        stepSize (Queryable[float]?): Sets the solvers step size.  This is the maximum size of a single step  
                the  
                solver will take at one time.  
                Range:   0.0004. 0.100  
                Default: 0.0333  
                Properties: query, edit
        velocityVectorScale (Queryable[float]?): scales the velocity vector display.  
                Default value: 1.0  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

