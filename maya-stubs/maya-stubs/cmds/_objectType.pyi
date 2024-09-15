from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def objectType(arg0: str = ..., /, *, isAType: str = ..., isType: str = ..., tagFromType: str = ..., typeFromTag: int = ..., typeTag: bool = ...) -> Union[str, bool]:
    """This command returns the type of elements. Warning: This command is
    incomplete and may not be supported by all object types.
    Args:
        isAType (str?): Returns true if the object is the specified type or derives  
                from an object that is of the specified type. This flag will  
                only work with dependency nodes.  
                Properties: create
        isType (str?): Returns true if the object is exactly of the specified type.  
                False otherwise.  
                Properties: create
        tagFromType (str?): Returns the type tag given a type name.  
                Properties: create
        typeFromTag (int?): Returns the type name given an integer type tag.  
                Properties: create
        typeTag (bool?): Returns an integer tag that is unique for that object type.  Not all  
                object types will have tags.  This is the unique 4. byte value that is  
                used to identify nodes of a given type in the binary file format.  
                Properties: create

    Returns:
        str: The type of the specified object
        bool: For "isType": was the object of the specified type?

    Example:
    """

