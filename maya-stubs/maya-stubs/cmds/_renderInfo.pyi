from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderInfo(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., castShadows: bool = ..., chordHeight: float = ..., chordHeightRatio: float = ..., doubleSided: bool = ..., edgeSwap: bool = ..., minScreen: float = ..., name: str = ..., opposite: bool = ..., smoothShading: bool = ..., unum: int = ..., useChordHeight: bool = ..., useChordHeightRatio: bool = ..., useDefaultLights: bool = ..., useMinScreen: bool = ..., utype: int = ..., vnum: int = ..., vtype: int = ...) -> bool:
    """The renderInfo commands sets geometric properties of surfaces
    of the selected object.
    Args:
        castShadows (bool?): Determines if object casts shadow or not.  
                Properties: create
        chordHeight (float?): Tessellation subdivision criteria.  
                Properties: create
        chordHeightRatio (float?): Tessellation subdivision criteria.  
                Properties: create
        doubleSided (bool?): Determines if object double or single sided.  
                Properties: create
        edgeSwap (bool?): Tessellation subdivision criteria.  
                Properties: create
        minScreen (float?): Tessellation subdivision criteria.  
                Properties: create
        name (str?): Namespace to use.  
                Properties: create
        opposite (bool?): Determines if the normals of the object is to be reversed.  
                Properties: create
        smoothShading (bool?): Determines if smooth shaded, or flat shaded - applies only to polysets.  
                Properties: create
        unum (int?): Tessellation subdivision criteria.  
                Properties: create
        useChordHeight (bool?): Tessellation subdivision criteria.  
                Properties: create
        useChordHeightRatio (bool?): Tessellation subdivision criteria.  
                Properties: create
        useDefaultLights (bool?): Obsolete flag.  
                Properties: create
        useMinScreen (bool?): Tessellation subdivision criteria.  
                Properties: create
        utype (int?): Tessellation subdivision criteria.  
                Properties: create
        vnum (int?): Tessellation subdivision criteria.  
                Properties: create
        vtype (int?): Tessellation subdivision criteria.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

