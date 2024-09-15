from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def pointLight(*args: str, edit: bool = ..., query: bool = ..., decayRate: Queryable[int] = ..., discRadius: Queryable[float] = ..., exclusive: bool = ..., intensity: Queryable[float] = ..., name: Queryable[str] = ..., position: Queryable[Tuple[float, float, float]] = ..., rgb: Queryable[Tuple[float, float, float]] = ..., rotation: Queryable[Tuple[float, float, float]] = ..., shadowColor: Queryable[Tuple[float, float, float]] = ..., shadowDither: Queryable[float] = ..., shadowSamples: Queryable[int] = ..., softShadow: bool = ..., useRayTraceShadows: bool = ...) -> Union[str, int, float, bool, Tuple[float, float, float]]:
    """The pointLight command is used to edit the parameters of
    existing pointLights, or to create new ones. The default
    behaviour is to create a new pointlight.
    Args:
        decayRate (Queryable[int]?): decay rate of the light (0. no decay, 1. slow, 2. realistic, 3. fast)  
                Properties: create, query, edit
        discRadius (Queryable[float]?): radius of the disc around the light  
                Properties: create, query, edit
        exclusive (bool?): This flag is obsolete.  
                Properties: create, query, edit
        intensity (Queryable[float]?): intensity of the light (expressed as a percentage)  
                Properties: create, query, edit
        name (Queryable[str]?): specify the name of the light  
                Properties: create, query, edit
        position (Queryable[Tuple[float, float, float]]?): This flag is obsolete.  
                Properties: create, query, edit
        rgb (Queryable[Tuple[float, float, float]]?): color of the light (0. 1)  
                Properties: create, query, edit
        rotation (Queryable[Tuple[float, float, float]]?): This flag is obsolete.  
                Properties: create, query, edit
        shadowColor (Queryable[Tuple[float, float, float]]?): the shadow color  
                Properties: create, query, edit
        shadowDither (Queryable[float]?): dither the shadow  
                Properties: create, query, edit
        shadowSamples (Queryable[int]?): number of shadow samples.  
                Properties: create, query, edit
        softShadow (bool?): soft shadow  
                Properties: create, query, edit
        useRayTraceShadows (bool?): ray trace shadows  
                Properties: create, query, edit

    Returns:
        str: Light shape name

    Example:
    """

