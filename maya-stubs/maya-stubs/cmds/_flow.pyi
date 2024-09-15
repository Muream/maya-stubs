from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def flow(*args: str, edit: bool = ..., query: bool = ..., divisions: Queryable[Tuple[int, int, int]] = ..., localCompute: bool = ..., localDivisions: Queryable[Tuple[int, int, int]] = ..., objectCentered: bool = ...) -> Union[List[str], Tuple[int, int, int], bool]:
    """The flow command creates a deformation lattice to `bend' the object
    that is animated along a curve of a motion path animation.
    The motion path animation has to have the follow option set to be on.
    Args:
        divisions (Queryable[Tuple[int, int, int]]?): This flag specifies the number of lattice slices  
                in x,y,z.  
                The default values are 2 5 2.  
                When queried, it returns the uint32_t uint32_t uint32_t  
                Properties: query
        localCompute (bool?): This flag specifies whether or not to have local  
                control over the object deformation.  
                Default value:  
                is on when the lattice is around the curve, and  
                is off when the lattice is around the object.   
                When queried, it returns a boolean  
                Properties: query
        localDivisions (Queryable[Tuple[int, int, int]]?): This flag specifies the extent of the region of effect.  
                Default values are 2 2 2.  
                When queried, it returns the uint32_t uint32_t uint32_t  
                Properties: query
        objectCentered (bool?): This flag specifies whether to create the lattice around  
                the selected object at its center, or to create the lattice  
                around the curve.  
                Default value is true.  
                When queried, it returns a boolean  
                Properties: query

    Returns:
        List[str]: The names of the created flow node and associated
            lattice nodes.

    Example:
    """

