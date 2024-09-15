from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fluidEmitter(*args: str, edit: bool = ..., query: bool = ..., cycleEmission: Queryable[str] = ..., cycleInterval: Queryable[int] = ..., densityEmissionRate: Queryable[float] = ..., fluidDropoff: Queryable[float] = ..., fuelEmissionRate: Queryable[float] = ..., heatEmissionRate: Queryable[float] = ..., maxDistance: Queryable[float] = ..., minDistance: Queryable[float] = ..., name: Queryable[str] = ..., position: Queryable[Multiuse[Tuple[float, float, float]]] = ..., rate: Queryable[float] = ..., torusSectionRadius: Queryable[float] = ..., type: Queryable[str] = ..., volumeOffset: Queryable[Tuple[float, float, float]] = ..., volumeShape: Queryable[str] = ..., volumeSweep: Queryable[float] = ...) -> Union[str, int, float, Multiuse[Tuple[float, float, float]], Tuple[float, float, float]]:
    """Creates, edits or queries an auxiliary dynamics object
    (for example, a field or emitter).
    Creates an emitter object. If object names are provided or if objects are
    selected, applies the emitter to the named/selected object(s)in the
    scene.  Fluid will then be emitted from each. If no objects are
    named or selected, or if the -pos option is specified, creates a
    positional emitter.If an emitter was created, the command returns the name of the object
    owning the emitter, and the name of emitter shape. If an emitter was
    queried, the command returns the results of the query.
    Args:
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
        densityEmissionRate (Queryable[float]?): Rate at which density is emitted.  
                Properties: query, edit
        fluidDropoff (Queryable[float]?): Fluid Emission Dropoff in volume  
                Properties: query, edit
        fuelEmissionRate (Queryable[float]?): Rate at which  is emitted.  
                Properties: query, edit
        heatEmissionRate (Queryable[float]?): Rate at which density is emitted.  
                Properties: query, edit
        maxDistance (Queryable[float]?): Maximum distance at which emission ends.  
                Properties: query, edit
        minDistance (Queryable[float]?): Minimum distance at which emission starts.  
                Properties: query, edit
        name (Queryable[str]?): Object name  
                Properties: create, query, edit
        position (Queryable[Multiuse[Tuple[float, float, float]]]?): world-space position  
                Properties: create, query, edit, multiuse
        rate (Queryable[float]?): Rate at which particles emitted (can be non-integer).  
                For point emission this is rate per point per unit time.  
                For surface emission it is rate per square unit of area per unit time.  
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

