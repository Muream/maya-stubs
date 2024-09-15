from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def connectionInfo(arg0: str = ..., /, *, destinationFromSource: bool = ..., getExactDestination: bool = ..., getExactSource: bool = ..., getLockedAncestor: bool = ..., isDestination: bool = ..., isExactDestination: bool = ..., isExactSource: bool = ..., isLocked: bool = ..., isSource: bool = ..., sourceFromDestination: bool = ...) -> Union[bool, str, List[str]]:
    """Thecommand is used to get information about
    connection sources and destinations.  Unlike the isConnected command,
    this command needs only one end of the connection.
    Args:
        destinationFromSource (bool?): If the specified plug (or its ancestor) is a source, this flag returns  
                the list of destinations connected from the source. (array of strings,  
                empty array if none)  
                Properties: create
        getExactDestination (bool?): If the plug or its ancestor is connection destination, this returns the  
                name of the plug that is the exact destination. (empty string if there  
                is no such connection).  
                Properties: create
        getExactSource (bool?): If the plug or its ancestor is a connection source, this returns the  
                name of the plug that is the exact source. (empty string if there is  
                no such connection).  
                Properties: create
        getLockedAncestor (bool?): If the specified plug is locked, its name is returned.  If an  
                ancestor of the plug is locked, its name is returned.  If more  
                than one ancestor is locked, only the name of the closest one  
                is returned.  If neither this plug nor any ancestors are locked,  
                an empty string is returned.  
                Properties: create
        isDestination (bool?): Returns true if the plug (or its ancestor) is the destination  
                of a connection, false otherwise.  
                Properties: create
        isExactDestination (bool?): Returns true if the plug is the exact destination of a connection,  
                false otherwise.  
                Properties: create
        isExactSource (bool?): Returns true if the plug is the exact source of a connection,  
                false otherwise.  
                Properties: create
        isLocked (bool?): Returns true if this plug (or its ancestor) is locked  
                Properties: create
        isSource (bool?): Returns true if the plug (or its ancestor) is the source of a  
                connection, false otherwise.  
                Properties: create
        sourceFromDestination (bool?): If the specified plug (or its ancestor) is a destination, this flag returns  
                the source of the connection. (string, empty if none)  
                Properties: create

    Returns:
        bool: When asking for a property, depending on the flags used.
        str: When asking for a plug name.
        List[str]: When asking for a list of plugs.

    Example:
    """

