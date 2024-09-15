from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def emitter(*args: str, edit: bool = ..., query: bool = ..., alongAxis: Queryable[float] = ..., aroundAxis: Queryable[float] = ..., awayFromAxis: Queryable[float] = ..., awayFromCenter: Queryable[float] = ..., cycleEmission: Queryable[str] = ..., cycleInterval: Queryable[int] = ..., directionX: Queryable[float] = ..., directionY: Queryable[float] = ..., directionZ: Queryable[float] = ..., directionalSpeed: Queryable[float] = ..., maxDistance: Queryable[float] = ..., minDistance: Queryable[float] = ..., name: Queryable[str] = ..., needParentUV: bool = ..., normalSpeed: Queryable[float] = ..., position: Queryable[Multiuse[Tuple[float, float, float]]] = ..., randomDirection: Queryable[float] = ..., rate: Queryable[float] = ..., scaleRateByObjectSize: bool = ..., scaleSpeedBySize: bool = ..., speed: Queryable[float] = ..., speedRandom: Queryable[float] = ..., spread: Queryable[float] = ..., tangentSpeed: Queryable[float] = ..., torusSectionRadius: Queryable[float] = ..., type: Queryable[str] = ..., volumeOffset: Queryable[Tuple[float, float, float]] = ..., volumeShape: Queryable[str] = ..., volumeSweep: Queryable[float] = ...) -> Union[str, float, int, bool, Multiuse[Tuple[float, float, float]], Tuple[float, float, float]]:
    """Creates, edits or queries an auxiliary dynamics object
    (for example, a field or emitter).
    Creates an emitter object. If object names are provided or if objects are
    selected, applies the emitter to the named/selected object(s)in the
    scene.  Particles will then be emitted from each. If no objects are
    named or selected, or if the -pos option is specified, creates a
    positional emitter.If an emitter was created, the command returns the name of the object
    owning the emitter, and the name of emitter shape. If an emitter was
    queried, the command returns the results of the query.Keyframeable attributes of the emitter node: rate, directionX,
    directionY, directionZ, minDistance, maxDistance, spread.
    Args:
        alongAxis (Queryable[float]?): Initial velocity multiplier in the direction along  
                the central axis of the volume.  See the diagrams in  
                the documentation.  Applies only to volume emitters.  
                Properties: query, edit
        aroundAxis (Queryable[float]?): Initial velocity multiplier in the direction around  
                the central axis of the volume.  See the diagrams  
                in the documentation.  Applies only to volume emitters.  
                Properties: query, edit
        awayFromAxis (Queryable[float]?): Initial velocity multiplier in the direction away  
                from the central axis of the volume.  See the diagrams  
                in the documentation.  Used only with the cylinder, cone,  
                and torus volume emitters.  
                Properties: query, edit
        awayFromCenter (Queryable[float]?): Initial velocity multiplier in the direction away from  
                the center point of a cube or sphere volume emitter. Used only with  
                the cube and sphere volume emitters.  
                Properties: query, edit
        cycleEmission (Queryable[str]?): Possible values are "none" and "frame."  
                Cycling emission restarts the random number stream after  
                a specified interval.  This can either be a number of frames  
                or a number of emitted particles.  In each case the number  
                is specified by the cycleInterval attribute. Setting cycleEmission to  
                "frame" and cycleInterval to 1 will then re-start the random stream every  
                frame. Setting cycleInterval to values greater than 1 can be used  
                to generate cycles for games work.  
                Properties: query, edit
        cycleInterval (Queryable[int]?): Specifies the number of frames or particles between restarts of  
                the random number stream.  See cycleEmission.  Has no effect if  
                cycleEmission is set to None.  
                Properties: query, edit
        directionX (Queryable[float]?): x-component of emission direction.  
                Used for directional emitters, and for volume emitters with  
                directionalSpeed.  
                Properties: query, edit
        directionY (Queryable[float]?): y-component of emission direction.  
                Used for directional emitters, and for volume emitters with  
                directionalSpeed.  
                Properties: query, edit
        directionZ (Queryable[float]?): z-component of emission direction.  
                Used for directional emitters, and for volume emitters with  
                directionalSpeed.  
                Properties: query, edit
        directionalSpeed (Queryable[float]?): For volume emitters only, adds a component of speed in the  
                direction specified by the directionX, Y, and Z attributes.  
                Applies only to volume emitters. Does not apply to other types  
                of emitters.  
                Properties: query, edit
        maxDistance (Queryable[float]?): Maximum distance at which emission ends.  
                Properties: query, edit
        minDistance (Queryable[float]?): Minimum distance at which emission starts.  
                Properties: query, edit
        name (Queryable[str]?): Object name  
                Properties: create, query, edit
        needParentUV (bool?): If aNeedParentUV is true, compute parentUV value from  
                each triangle or each line segment, then send out to the  
                target particle object. You also need to add parentU and  
                parentV attributes to the particle object to store these values.  
                Properties: query, edit
        normalSpeed (Queryable[float]?): Normal speed multiple for point emission. For each emitted  
                particle, multiplies the component of the velocity normal  
                to the surface or curve by this amount. Surface and curve  
                emitters only.  
                Properties: query, edit
        position (Queryable[Multiuse[Tuple[float, float, float]]]?): world-space position  
                Properties: create, query, edit, multiuse
        randomDirection (Queryable[float]?): Magnitude of a random component of the speed  
                from volume emission.  
                Properties: query, edit
        rate (Queryable[float]?): Rate at which particles emitted (can be non-integer).  
                For point emission this is rate per point per unit time.  
                For surface emission it is rate per square unit of area per unit time.  
                Properties: query, edit
        scaleRateByObjectSize (bool?): Applies to curve and surface emitters, only.  
                If true, number of particles is determined by object size  
                (area or length) times rate value.  If false, object size  
                is ignored and the rate value is used without modification.  
                The former is the way Maya behaved prior to version 3.0.  
                Properties: query, edit
        scaleSpeedBySize (bool?): Indicates whether the scale of a volume emitter  
                affects its velocity.  
                Properties: query, edit
        speed (Queryable[float]?): Speed multiple.  Multiplies the velocity of the  
                emitted particles by this amount. Does not apply to volume  
                emitters.  For that emitter type, use directionalSpeed.  
                Properties: query, edit
        speedRandom (Queryable[float]?): Identifies a range of random variation for the speed of  
                each generated particle.  If set to a non-zero value, speed  
                becomes the mean value of the generated particles, whose speeds  
                vary by a random amount up to plus or minus speedRandom/2.  
                For example, speed 5 and speedRandom 2 will make the speeds  
                vary between 4 and 6.  
                Properties: query, edit
        spread (Queryable[float]?): Random spread (0. 1), as a fraction of 90 degrees,  
                along specified direction.   Directional emitters only.  
                Properties: query, edit
        tangentSpeed (Queryable[float]?): Tangent speed multiple for point emission.  
                For each emitted particle, multiplies the component of the velocity  
                tangent to the surface  or curve by this amount.  
                Surface and curve emitters only.  
                Properties: query, edit
        torusSectionRadius (Queryable[float]?): Section radius for a torus volume.  Applies only to torus.  
                Similar to the section radius in the torus modelling primitive.  
                Properties: query, edit
        type (Queryable[str]?): Type of emitter. The choices are omni | dir | direction | surf |  
                surface | curve | curv. The default is omni.  
                The full definition of these types are: omnidirectional point emitter,  
                directional point emitter, surface emitter, or curve emitter.  
                Properties: query, edit
        volumeOffset (Queryable[Tuple[float, float, float]]?): Volume offset of the emitter.  Volume offset translates  
                the emission volume by the specified amount from the actual  
                emitter location.  This is in the emitter's local space.  
                Properties: query, edit
        volumeShape (Queryable[str]?): Volume shape of the emitter.  Sets/edits/queries the  
                field's volume shape attribute.  If set to any value other  
                than "none", determines a 3. D volume within which  
                particles are generated.  
                Values are: "cube," "sphere," "cylinder," "cone," "torus."  
                Properties: query, edit
        volumeSweep (Queryable[float]?): Volume sweep of the emitter.  Applies only to sphere, cone,  
                cylinder, and torus.  Similar effect to the sweep attribute  
                in modelling.  
                Properties: query, edit

    Returns:
        str: Command result

    Example:
    """

