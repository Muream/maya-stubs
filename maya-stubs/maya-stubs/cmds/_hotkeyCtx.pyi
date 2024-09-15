from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hotkeyCtx(*, query: bool = ..., addClient: Multiuse[str] = ..., clientArray: bool = ..., currentClient: Queryable[str] = ..., insertTypeAt: Tuple[str, str] = ..., removeAllClients: bool = ..., removeClient: Multiuse[str] = ..., removeType: str = ..., type: Queryable[str] = ..., typeArray: bool = ..., typeExists: str = ...) -> Union[bool, str]:
    """This command sets the hotkey context for the entire application.
    Args:
        addClient (Multiuse[str]?): Associates a client to the given hotkey context type.  
                This flag needs to be used with the flag "type" which specifies the context type.  
                Properties: create, multiuse
        clientArray (bool?): Returns an array of the all context clients associated to the hotkey context type.  
                This flag needs to be used with the flag "type" which specifies the context type.  
                Properties: query
        currentClient (Queryable[str]?): Current client for the given hotkey context type.  
                This flag needs to be used with the flag "type" which specifies the context type.  
                Properties: create, query
        insertTypeAt (Tuple[str, str]?): Inserts a new hotkey context type in the front of the given type.  
                The first argument specifies an existing type. If it's empty,  
                the new context type will be inserted before "Global" context type.  
                The second argument specifies the name of new context type.  
                Properties: create
        removeAllClients (bool?): Removes all the clients associated to the hotkey context type.  
                This flag needs to be used with the flag "type" which specifies the context type.  
                Properties: create
        removeClient (Multiuse[str]?): Removes a client associated to the hotkey context type.  
                This flag needs to be used with the flag "type" which specifies the context type.  
                Properties: create, multiuse
        removeType (str?): Removes the given hotkey context type.  
                Properties: create
        type (Queryable[str]?): Specifies the context type. It's used together with the other flags such as  
                "currentClient", "addClient", "removeClient" and so on.  
                Properties: create, query
        typeArray (bool?): Returns a string array containing the names of all hotkey context types,  
                ordered by priority.  
                Properties: query
        typeExists (str?): Returns true|false depending upon whether the specified hotkey context type  
                exists.  
                      In query mode, this flag needs a value.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

