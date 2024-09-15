from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hardware(*, brdType: bool = ..., cpuType: bool = ..., graphicsType: bool = ..., megaHertz: bool = ..., numProcessors: bool = ...) -> str:
    """Return description of the hardware available in the machine.
    Args:
        brdType (bool?): Returns IP number identifying the CPU motherboard  
                Properties: create
        cpuType (bool?): Returns type of CPU  
                Properties: create
        graphicsType (bool?): Returns string identifying graphics hardware type  
                Properties: create
        megaHertz (bool?): Returns string identifying the speed of the CPU chip  
                Properties: create
        numProcessors (bool?): Returns string identifying the number of processors  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

