from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def combinationShape(arg0: str = ..., /, *args: str, edit: bool = ..., query: bool = ..., addDriver: bool = ..., allDrivers: bool = ..., blendShape: str = ..., combinationTargetIndex: int = ..., combinationTargetName: str = ..., combineMethod: Queryable[int] = ..., driverTargetIndex: Multiuse[int] = ..., driverTargetName: Multiuse[str] = ..., exist: bool = ..., removeDriver: bool = ...) -> Union[int, bool]:
    """Command to create or edit drive relationship of blend shape targetscombination, target
    Args:
        addDriver (bool?): Add drivers to the combination shape
        allDrivers (bool?): All drivers of the combination shape  
                Properties: query
        blendShape (str?): Associated blend shape node of the combination shape  
                			In query mode, this flag can accept a value.  
                Properties: create
        combinationTargetIndex (int?): Driven blend shape target index of the combination shape  
                			In query mode, this flag can accept a value.  
                Properties: create
        combinationTargetName (str?): Driven blend shape target name of the combination shape  
                			In query mode, this flag can accept a value.  
                Properties: create
        combineMethod (Queryable[int]?): Combine method of the combination shape:  
              
                0. Multiplication  
                1. Lowest Weighting  
                2. Lowest Weighting (Smooth)  
                Properties: create, query, edit
        driverTargetIndex (Multiuse[int]?): Driver blend shape target index of the combination shape  
                Properties: create, multiuse
        driverTargetName (Multiuse[str]?): Driver blend shape target name of the combination shape  
                Properties: create, multiuse
        exist (bool?): If the combination shape exist  
                Properties: query
        removeDriver (bool?): Remove drivers from the combination shape

    Returns:
        int: In edit mode, return the newly created combination shape node name.

    Example:
    """

