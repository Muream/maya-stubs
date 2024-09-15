from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def spotLight(*args: str, edit: bool = ..., query: bool = ..., barnDoors: bool = ..., bottomBarnDoorAngle: Queryable[float] = ..., coneAngle: Queryable[float] = ..., decayRate: int = ..., discRadius: Queryable[float] = ..., dropOff: Queryable[float] = ..., exclusive: bool = ..., intensity: Queryable[float] = ..., leftBarnDoorAngle: Queryable[float] = ..., name: Queryable[str] = ..., penumbra: Queryable[float] = ..., position: Queryable[Tuple[float, float, float]] = ..., rgb: Queryable[Tuple[float, float, float]] = ..., rightBarnDoorAngle: Queryable[float] = ..., rotation: Queryable[Tuple[float, float, float]] = ..., shadowColor: Queryable[Tuple[float, float, float]] = ..., shadowDither: Queryable[float] = ..., shadowSamples: Queryable[int] = ..., softShadow: bool = ..., topBarnDoorAngle: Queryable[float] = ..., useRayTraceShadows: bool = ...) -> Union[str, List[float], int, bool, float, Tuple[float, float, float]]:
    """TlightCmd is the base class for other light commands.
    TnonAmbientLightCmd is a class that looks like a command but
    is not.  It is a base class for the extended/nonExtended
    lights.
    TnonExtendedLightCmd is a base class and not a real command. It is inherited by several
    lights: TpointLight, TdirectionalLight, TspotLight etc.
    The spotLight command is used to edit the parameters of
    existing spotLights, or to create new ones. The default
    behaviour is to create a new spotlight.
    Args:
        barnDoors (bool?): Are the barn doors enabled?  
                Properties: create, query, edit
        bottomBarnDoorAngle (Queryable[float]?): Angle of the bottom of the barn door.  
                Properties: create, query, edit
        coneAngle (Queryable[float]?): angle of the spotLight  
                Properties: create, query, edit
        decayRate (int?): Decay rate of the light (0. no decay, 1. slow, 2. realistic, 3. fast)  
                Properties: create
        discRadius (Queryable[float]?): Radius of shadow disc.  
                Properties: create, query
        dropOff (Queryable[float]?): dropOff of the spotLight  
                Properties: create, query, edit
        exclusive (bool?): True if the light is exclusively assigned  
                Properties: create, query
        intensity (Queryable[float]?): Intensity of the light  
                Properties: create, query
        leftBarnDoorAngle (Queryable[float]?): Angle of the left of the barn door.  
                Properties: create, query, edit
        name (Queryable[str]?): Name of the light  
                Properties: create, query
        penumbra (Queryable[float]?): specify penumbra region  
                Properties: create, query, edit
        position (Queryable[Tuple[float, float, float]]?): Position of the light  
                Properties: create, query
        rgb (Queryable[Tuple[float, float, float]]?): RGB colour of the light  
                Properties: create, query
        rightBarnDoorAngle (Queryable[float]?): Angle of the right of the barn door.  
                Properties: create, query, edit
        rotation (Queryable[Tuple[float, float, float]]?): Rotation of the light for orientation, where applicable  
                Properties: create, query
        shadowColor (Queryable[Tuple[float, float, float]]?): Color of the light's shadow  
                Properties: create, query
        shadowDither (Queryable[float]?): Shadow dithering value.  
                Properties: create, query
        shadowSamples (Queryable[int]?): Numbr of shadow samples to use  
                Properties: create, query
        softShadow (bool?): True if soft shadowing is to be enabled  
                Properties: create, query
        topBarnDoorAngle (Queryable[float]?): Angle of the top of the barn door.  
                Properties: create, query, edit
        useRayTraceShadows (bool?): True if ray trace shadows are to be used  
                Properties: create, query

    Returns:
        str: Light shape name
            boolean Barn door enabled state
            angle Left barn door angle
            angle Right barn door angle
            angle Top barn door angle
            angle Bottom barn door angle
            angle Cone angle
            angle Penumbra angle
            float Dropoff value
        List[float]: when querying the rgb or shadowColor flags
            double when querying the intensity flag
            boolean when querying the useRayTraceShadows or exclusive flags
            linear[] when querying the position flag
            angle[] when querying the rotation flag
            string when querying the name flag
        int: rate of light decay, when querying the decayRate flag
        int: Number of shadow samples, when querying the shadowSamples flag
            boolean True if soft shadows are enabled, when querying the softShadow flag
            float Shadow dithering value, when querying the shadowDither flag
            float Disc radius value, when querying the discRadius flag

    Example:
    """

