from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def directionalLight(*args: str, edit: bool = ..., query: bool = ..., decayRate: int = ..., discRadius: Queryable[float] = ..., exclusive: bool = ..., intensity: Queryable[float] = ..., name: Queryable[str] = ..., position: Queryable[Tuple[float, float, float]] = ..., rgb: Queryable[Tuple[float, float, float]] = ..., rotation: Queryable[Tuple[float, float, float]] = ..., shadowColor: Queryable[Tuple[float, float, float]] = ..., shadowDither: Queryable[float] = ..., shadowSamples: Queryable[int] = ..., softShadow: bool = ..., useRayTraceShadows: bool = ...) -> Union[List[float], int, str, float, bool, Tuple[float, float, float]]:
    """TlightCmd is the base class for other light commands.
    TnonAmbientLightCmd is a class that looks like a command but
    is not.  It is a base class for the extended/nonExtended
    lights.
    TnonExtendedLightCmd is a base class and not a real command. It is inherited by several
    lights: TpointLight, TdirectionalLight, TspotLight etc.
    The directionalLight command is used to edit the parameters
    of existing directionalLights, or to create new ones. The
    default behaviour is to create a new directionallight.This is the commmand that instantiates an directionalLight
    or edits the parameters of an existing one.
    TdirectionalLightCmd inherits from TnonExtendedLightCmd
    which defines softShadow flags.
    See TlightCmd for a global picture of the light commands.TdirectionalLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly
    different behaviour is that it calls up to
    TnonExtendedLightCmd to complete the functionality of
    the command.
    Args:
        decayRate (int?): Decay rate of the light (0. no decay, 1. slow, 2. realistic, 3. fast)  
                Properties: create
        discRadius (Queryable[float]?): Radius of shadow disc.  
                Properties: create, query
        exclusive (bool?): True if the light is exclusively assigned  
                Properties: create, query
        intensity (Queryable[float]?): Intensity of the light  
                Properties: create, query
        name (Queryable[str]?): Name of the light  
                Properties: create, query
        position (Queryable[Tuple[float, float, float]]?): Position of the light  
                Properties: create, query
        rgb (Queryable[Tuple[float, float, float]]?): RGB colour of the light  
                Properties: create, query
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
        useRayTraceShadows (bool?): True if ray trace shadows are to be used  
                Properties: create, query

    Returns:
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
        str: Light shape name

    Example:
    """

