from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def air(*args: str, edit: bool = ..., query: bool = ..., attenuation: Queryable[float] = ..., directionX: Queryable[float] = ..., directionY: Queryable[float] = ..., directionZ: Queryable[float] = ..., enableSpread: bool = ..., fanSetup: bool = ..., inheritRotation: bool = ..., inheritVelocity: Queryable[float] = ..., magnitude: Queryable[float] = ..., maxDistance: Queryable[float] = ..., name: Queryable[str] = ..., perVertex: bool = ..., position: Queryable[Multiuse[Tuple[float, float, float]]] = ..., speed: Queryable[float] = ..., spread: Queryable[float] = ..., torusSectionRadius: Queryable[float] = ..., velocityComponentOnly: bool = ..., volumeExclusion: bool = ..., volumeOffset: Queryable[Tuple[float, float, float]] = ..., volumeShape: Queryable[str] = ..., volumeSweep: Queryable[float] = ..., wakeSetup: bool = ..., windSetup: bool = ...) -> Union[str, float, bool, Multiuse[Tuple[float, float, float]], Tuple[float, float, float]]:
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
    The air field simulates the effects of moving air. The affected objects
    will be accelerated or decelerated so that their velocities match that
    of the air.With the '-vco true' flag thrown, only accelerations are applied.
    By parenting an air field to a moving part of an object (ie. a foot of a
    character) and using '-i 1 -m 0 -s .5 -vco true' flags, one can simulate
    the movement of air around the
    foot as it moves, since the TOTAL velocity vector of the field would be
    only based on the
    movement of the foot. This can be done while the character walks through
    leaves or dust on the ground.For each listed object, the command creates a new field.
    The transform is the associated dependency node.
    Use connectDynamic to cause the field to affect a dynamic object.If fields are created,  this command returns the field names. If
    a field was queried, the results of the query are returned. If a field
    was edited, the field name is returned.If the -pos flag is specified, a field is created at the position specified.
    If not, if object names are provided or the active selection list is
    non-empty, the command creates a field for every object in the list and
    calls addDynamic to add it to the object; otherwise the command defaults
    to -pos 0 0 0.Setting the -pos flag with objects named on the command line is an error.
    Args:
        attenuation (Queryable[float]?): Attentuation rate of field  
                Properties: query, edit
        directionX (Queryable[float]?):   
                Properties: query, edit
        directionY (Queryable[float]?):   
                Properties: query, edit
        directionZ (Queryable[float]?): Direction that the air will try to match the affected  
                particles' velocity to. NOTE: This is not the velocity; this is only  
                the direction. Use the -s flag to set the speed.  
                Properties: query, edit
        enableSpread (bool?): This tells the system whether or not to use the spread  
                angle given by '-sp'. If this is 'false' then all connected objectswithin the maximum distance will  
                be affected. Also, if this is set to 'false', all affected objects are forced to match their velocities  
                along the direction vector. If this is set to 'true' and spread is used, then the direction of the force  
                is along the direction from the field to the object.  
                Properties: query, edit
        fanSetup (bool?): Similar to 'windSetup' except that the effects of a fan or  
                a person blowing air are approximated. The user can pass the same  
                flags on the command line to adjust them from the defaults. These are  
                the values that get set to approximate a 'fan':  
                inheritVelocity 1.0  
                inheritRotation true  
                componentOnly false  
                enableSpread true  
                spread .5 (45 degrees from center )  
                Properties: edit
        inheritRotation (bool?): If this is set to 'true', then the direction vector  
                described with -dx, -dy, and -dz will be considered local to the owning object. Therefore, if the  
                owning object's transform undergoes any rotation (by itself or one of its parents), the direction  
                vector of the air field will undergo that same rotation.  
                Properties: query, edit
        inheritVelocity (Queryable[float]?): Amount (from 0 to 1) of the field-owner's velocity added to the  
                vector determined by the direction and speed flags. The combination  
                of these two vectors makes  
                up the TOTAL velocity vector for the air field. This allows the air  
                to be determined directly by the motion of the owning object.  
                Properties: query, edit
        magnitude (Queryable[float]?): Strength of field.  
                Properties: query, edit
        maxDistance (Queryable[float]?): Maximum distance at which field is exerted.  
                -1 indicates that the field has no maximum distance.  
                Properties: query, edit
        name (Queryable[str]?): name of field  
                Properties: query, edit
        perVertex (bool?): Per-vertex application. If this flag is set true, then each  
                individual point (CV, particle, vertex,etc.) of the chosen object  
                exerts an identical copy of the force field. If this flag is set to  
                false, then the froce is exerted only from the geometric center of  
                the set of points.  
                Properties: query, edit
        position (Queryable[Multiuse[Tuple[float, float, float]]]?): Position in space (x,y,z) where you want to place a gravity field.  
                The gravity then emanates from this position in space rather  
                than from an object. Note that you can both use -pos  
                (creating a field at a position) and also provide object names.  
                Properties: query, edit, multiuse
        speed (Queryable[float]?): How fast the affected objects' speed reaches the speed (based on the -mag, -dx, -dy, -dz flags) of the air field.  
                This value gets clamped internally to be between 0.0 and 1.0.  A value of 0.0 will make the air field have no effect.  
                A value of 1.0 will try to match the air field's speed much quicker, but not necessarily immediately.  
                Properties: query, edit
        spread (Queryable[float]?): This represents the angle from the direction vector within which  
                objects will be affected. The values are in the range of 0 to 1.  
                A value of 0 will result in an effect only  
                exactly in front of the air field along the direction vector. A  
                value of 1 will result in any object in front of the owning object, 90  
                degrees in all direction from the direction vector.  
                Properties: query, edit
        torusSectionRadius (Queryable[float]?): Section radius for a torus volume.  Applies only to torus.  
                Similar to the section radius in the torus modelling primitive.  
                Properties: query, edit
        velocityComponentOnly (bool?): If this is 'false', the air will accelerate or decelerate  
                the affected objects so that their velocities will eventually match  
                the TOTAL velocity vector of the air field. If this is 'true',  
                only ACCELERTION is applied to the affected objects so that their  
                velocity component along the TOTAL velocity vector matches or is  
                greater in magnitude than the TOTAL velocity vector. This will not  
                slow objects down to match velocities, only speed them up  
                to match components. This is most useful when using the -iv flag  
                with a value >0.  
                Properties: query, edit
        volumeExclusion (bool?): Volume exclusion of the field.  If true, points outside the  
                volume (defined by the volume shape attribute) are affected,  If false,  
                points inside the volume are affected.  Has no effect if volumeShape  
                is set to "none."  
                Properties: query, edit
        volumeOffset (Queryable[Tuple[float, float, float]]?): Volume offset of the field.  Volume offset translates  
                the field's volume by the specified amount from the actual  
                field location. This is in the field's local space.  
                Properties: query, edit
        volumeShape (Queryable[str]?): Volume shape of the field.  Sets/edits/queries the  
                field's volume shape attribute.  If set to any value other  
                than "none", determines a 3. D volume within which the field has effect.  
                Values are: "none," "cube," "sphere," "cylinder," "cone," "torus."  
                Properties: query, edit
        volumeSweep (Queryable[float]?): Volume sweep of the field.  Applies only to sphere, cone,  
                cylinder, and torus.  Similar effect to the sweep attribute  
                in modelling.  
                Properties: query, edit
        wakeSetup (bool?): Like the 'windSetup' and 'fanSetup', 'wakeSetup'  
                sets certain values in the field to approximate the movement of air  
                near a moving object, such as  a character's foot or hand.  
                The values that are set are:  
                inheritVelocity 1.0  
                inheritRotation false  
                componentOnly true  
                enableSpread false  
                speed 0.0  
                Properties: edit
        windSetup (bool?): This will set some of the values above in a way that  
                approximates the effects of a basic wind. This allows the user to then change certain values as  
                he/she wishes on the same command line. First the preset values get set, and then any other flags  
                that were passed get taken into account. These are the values that get set to approximate 'wind':  
                inheritVelocity 0.0  
                inheritRotation true  
                componentOnly false  
                enableSpread false  
                Properties: edit

    Returns:
        str: Command result

    Example:
    """

