from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def connectAttr(arg0: str = ..., arg1: str = ..., /, *, force: bool = ..., lock: bool = ..., nextAvailable: bool = ..., referenceDest: str = ...) -> str:
    """Connect the attributes of two dependency nodes and return the
    names of the two connected attributes. The connected
    attributes must be be of compatible types. First argument is the
    source attribute, second one is the destination.Refer to dependency node documentation.
    Args:
        force (bool?): Forces the connection.  If the destination is already  
                connected, the old connection is broken and the new one  
                made.  
                Properties: create
        lock (bool?): If the argument is true, the destination attribute  
                is locked after making the connection. If the argument is false,  
                the connection is unlocked before making the connection.  
                Properties: create
        nextAvailable (bool?): If the destination multi-attribute has set the indexMatters  
                to be false with this flag specified, a connection is made to  
                the next available index. No index need be specified.  
                Properties: create
        referenceDest (str?): This flag is used for file io only. The flag indicates that  
                the connection replaces a connection made in a  
                referenced file, and the flag argument indicates the original  
                destination from the referenced file. This  
                flag is used so that if the reference file is modified, maya  
                can still attempt to make the appropriate connections in the  
                main scene to the referenced object.  
                Properties: create

    Returns:
        str: A phrase containing the names of the connected attributes.

    Example:
    """

