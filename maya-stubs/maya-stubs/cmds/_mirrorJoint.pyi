from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def mirrorJoint(arg0: str = ..., /, *, mirrorBehavior: bool = ..., mirrorXY: bool = ..., mirrorXZ: bool = ..., mirrorYZ: bool = ..., searchReplace: Tuple[str, str] = ...) -> List[str]:
    """This command will duplicate a branch of the skeleton from the selected
    joint symmetrically about a plane in world space.
    There are three mirroring modes(xy-, yz-, xz-plane).
    Args:
        mirrorBehavior (bool?): The mirrorBehavior flag is used to specify that when performing the  
                mirror, the joint orientation axes should be mirrored such that equal  
                rotations on the original and mirrored joints will place the skeleton  
                in a mirrored position (symmetric across the mirroring plane). Thus,  
                animation curves from the original joints can be copied to the mirrored  
                side to produce a similar (but symmetric) behavior. When mirrorBehavior  
                is not specified, the joint orientation on the mirrored side will be identical  
                to the source side.  
                Properties: create
        mirrorXY (bool?): mirror skeleton from the selected joint about xy-plane in world space.  
                Properties: create
        mirrorXZ (bool?): mirror skeleton from the selected joint about xz-plane in world space.  
                Properties: create
        mirrorYZ (bool?): mirror skeleton from the selected joint about yz-plane in world space.  
                Properties: create
        searchReplace (Tuple[str, str]?): After performing the mirror, rename the new joints by searching the name for the  
                first specified string and replacing it with the second specified string.  
                Properties: create

    Returns:
        List[str]: Names of the mirrored joints

    Example:
    """

