from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listSets(*, allSets: bool = ..., extendToShape: bool = ..., object: str = ..., type: int = ...) -> List[str]:
    """The listSets command is used to get a list of all the sets an
    object belongs to. To get sets of a specific type for an object
    use the type flag as well.To get a list of all sets in the scene then don't use an object
    in the command line but use one of the flags instead.
    Args:
        allSets (bool?): Returns all sets in the scene.  
                Properties: create
        extendToShape (bool?): When requesting a transform's sets also walk down to the shape  
                immediately below it for its sets.  
                Properties: create
        object (str?): Returns all sets which this object is a member of.  
                Properties: create
        type (int?): Returns all sets in the scene of the given type:  
              
                1. all rendering sets  
                2. all deformer sets  
                Properties: create

    Returns:
        List[str]: (string array of all sets the object belongs to)

    Example:
    """

