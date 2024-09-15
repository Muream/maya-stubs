from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ambientLight(*args: str, edit: bool = ..., query: bool = ..., ambientShade: Queryable[float] = ..., discRadius: Queryable[float] = ..., exclusive: bool = ..., intensity: Queryable[float] = ..., name: Queryable[str] = ..., position: Queryable[Tuple[float, float, float]] = ..., rgb: Queryable[Tuple[float, float, float]] = ..., rotation: Queryable[Tuple[float, float, float]] = ..., shadowColor: Queryable[Tuple[float, float, float]] = ..., shadowDither: Queryable[float] = ..., shadowSamples: Queryable[int] = ..., softShadow: bool = ..., useRayTraceShadows: bool = ...) -> Union[List[float], str, float, bool, Tuple[float, float, float], int]:
    """TlightCmd is the base class for other light commands.
    The ambientLight command is used to edit the parameters of
    existing ambientLights, or to create new ones. The default
    behaviour is to create a new ambientlight.This is the commmand that instantiates an ambientLight
    or edits the parameters of an existing one.
    TambientLightCmd inherits from TlightCmd which defines
    common flags like intensity, colour etc.
    See TlightCmd for a global picture of the light commands.
    Note that the flag fAmbientLightUsed indicates whether
    the command uses any ambient specific flags.
    That is, if a command doesn't use flags
    defined here, the boolean fAmbientLightUsed is set to
    false and thus the undo/redo information is not saved
    at this level.TambientLightCmd behaves like any other command, it
    has flags, saves undo information etc. the only slightly
    different behaviour is that it calls up to TlightCmd to
    complete the functionality of the command.
    Example	parseArgs:  TambientLightCmd defines
    ambientLight specific parameters like -ambientShade
    however, several other parameters are available in
    TlightCmd such as -intensity etc.  So when parsing
    the arguments, a call is made to TlightCmd::parseArgs
    to parse common parameters (like Intensity).
    Args:
        ambientShade (Queryable[float]?): ambientShade  
                Properties: create, query, edit
        discRadius (Queryable[float]?): radius of the disc around the light  
                Properties: create, query, edit
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
        shadowDither (Queryable[float]?): dither the shadow  
                Properties: create, query, edit
        shadowSamples (Queryable[int]?): number of shadow samples.  
                Properties: create, query, edit
        softShadow (bool?): soft shadow  
                Properties: create, query, edit
        useRayTraceShadows (bool?): True if ray trace shadows are to be used  
                Properties: create, query

    Returns:
        List[float]: when querying the rgb or shadowColor flags
            double when querying the intensity flag
            boolean when querying the useRayTraceShadows or exclusive flags
            linear[] when querying the position flag
            angle[] when querying the rotation flag
            string when querying the name flag
        str: Light shape name

    Example:
    """

