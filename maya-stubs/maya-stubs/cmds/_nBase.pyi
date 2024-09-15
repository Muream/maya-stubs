from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nBase(*args: str, edit: bool = ..., query: bool = ..., clearCachedTextureMap: str = ..., clearStart: bool = ..., stuffStart: bool = ..., textureToVertex: str = ...) -> bool:
    """Edits one or more nBase objects. Note that nBase objects include nCloth, nRigid
    and nParticle objects, but the options on this command do not currently apply
    to nParticle objects.nBase
    Args:
        clearCachedTextureMap (str?): Clear the cached texture map for the specified attribute from  
                the nBase.  
                Properties: create, edit
        clearStart (bool?): Indicates that start state should be cleared  
                Properties: create, edit
        stuffStart (bool?): Indicates that current state should be stuffed into the start state  
                Properties: create, edit
        textureToVertex (str?): Transfer the texture map data for the specified attribute into  
                the related per-vertex attribute.  
                Properties: create, edit

    Returns:
        bool: Command result

    Example:
    """

