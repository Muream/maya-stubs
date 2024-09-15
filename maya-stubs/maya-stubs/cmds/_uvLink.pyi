from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def uvLink(*, query: bool = ..., b: bool = ..., isValid: bool = ..., make: bool = ..., queryObject: str = ..., texture: str = ..., uvSet: str = ...) -> str:
    """This command is used to make, break and query UV linking
    relationships between UV sets on objects and textures that use those
    UV sets.If no make, break or query flag is specified and both uvSet and
    texture flags are present, the make flag is assumed to be specified.If no make, break or query flag is specified and only one of the
    uvSet and texture flags is present, the query flag is assumed to be
    specified.The term "texture" in the context of UV linking is a bit of an
    oversimplification. In fact, UV sets can be linked to any node which
    takes UV coordinates as input. However in most cases it will be a
    texture to which you wish to link a UV set.
    Args:
        b (bool?): The presence of this flag on the command indicates that the  
                command is being invoked to break links between UV sets and  
                textures.  
                Properties: create
        isValid (bool?): This flag is used to verify whether or not a texture or UV set is  
                valid for the purposes of UV linking. It should be used in  
                conjunction with either the -texture flag or the -uvSet flag, but  
                not both at the same time.  
                Properties: create
        make (bool?): The presence of this flag on the command indicates that the  
                command is being invoked to make links between UV sets and  
                textures.  
                Properties: create
        queryObject (str?): This flag should only be used in conjunction with a query of a  
                texture. This flag is used to indicate that the results of the  
                query should be limited to UV sets of the object specified by this  
                flag.  
                Properties: create
        texture (str?): The argument to the texture flag specifies the texture to be used by  
                the command in performing the action.  
                Properties: create
        uvSet (str?): The argument to the uvSet flag specifies the UV set to be used by  
                the command in performing the action.  
                Properties: create

    Returns:
        str: or array of strings for query
            boolean for isValid

    Example:
    """

