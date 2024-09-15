from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def renderManip(*args: str, edit: bool = ..., query: bool = ..., camera: Queryable[Tuple[bool, bool, bool, bool, bool]] = ..., light: Queryable[Tuple[bool, bool, bool]] = ..., spotLight: Queryable[Tuple[bool, bool, bool, bool, bool, bool, bool]] = ..., state: bool = ...) -> Union[bool, Tuple[bool, bool, bool, bool, bool], Tuple[bool, bool, bool], Tuple[bool, bool, bool, bool, bool, bool, bool]]:
    """This command creates manipulators for cameras or lights.
    Args:
        camera (Queryable[Tuple[bool, bool, bool, bool, bool]]?): Query or edit the visiblity status of the component camera  
                manipulators. The order of components are: cycling index,  
                center of interest, pivot, clipping planes, and unused.  
                Properties: query, edit
        light (Queryable[Tuple[bool, bool, bool]]?): Query or edit the visiblity status of the component light  
                manipulators. The order of components are: cycling index,  
                center of interest, and pivot.  
                Properties: query, edit
        spotLight (Queryable[Tuple[bool, bool, bool, bool, bool, bool, bool]]?): Query or edit the visiblity status of the component spot light  
                manipulators. The order of components are: cycling index,  
                center of interest, pivot, cone angle, penumbra, look through  
                barn doors, and decay regions.  
                Properties: query, edit
        state (bool?): Query or edit the state of manipulators on an camera, ambient  
                light, directional light, point light, or spot light. This  
                flag's default value is on.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

