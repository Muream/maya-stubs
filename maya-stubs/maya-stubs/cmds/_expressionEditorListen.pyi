from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def expressionEditorListen(*, listenFile: str = ..., listenForAttr: str = ..., listenForExpression: str = ..., listenForName: str = ..., stopListenForAttr: str = ..., stopListenForExpression: str = ..., stopListenForName: str = ...) -> bool:
    """Listens for messages for the Expression Editor, at its request, and
    communicates them to it.  This action is for internal use only and
    should not be called by users.  This action should be called only
    by the Expression Editor.
    Args:
        listenFile (str?): Listen for changes to the file argument.  
                Properties: create
        listenForAttr (str?): Listen for changes to the attributes of the node argument.  
                Properties: create
        listenForExpression (str?): Listen for changes to the named expression  
                Properties: create
        listenForName (str?): Listen for name changes for the node argument.  
                Properties: create
        stopListenForAttr (str?): Stop listening for changes to the attributes of the  
                node argument.  
                Properties: create
        stopListenForExpression (str?): Stop listening for changes to the named expression  
                Properties: create
        stopListenForName (str?): Stop listening for name changes for the node argument.  
                Properties: create

    Returns:
        bool:

    Example:
    """

