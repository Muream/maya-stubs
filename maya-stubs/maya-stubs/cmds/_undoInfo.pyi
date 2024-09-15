from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def undoInfo(*, query: bool = ..., chunkName: Queryable[str] = ..., closeChunk: bool = ..., infinity: bool = ..., length: Queryable[int] = ..., openChunk: bool = ..., printQueue: bool = ..., printRedoQueue: bool = ..., redoName: Queryable[str] = ..., redoQueueEmpty: bool = ..., state: bool = ..., stateWithoutFlush: bool = ..., undoName: Queryable[str] = ..., undoQueueEmpty: bool = ...) -> Union[str, int, bool]:
    """This command controls the undo/redo parameters.In query mode, if invoked without flags (other than the query flag), this
    command will return the number of items currently on the undo queue.
    Args:
        chunkName (Queryable[str]?): Sets the name used to identify a chunk for undo/redo  
                purposes when opening a chunk.  
                Properties: create, query
        closeChunk (bool?): Closes the chunk that was opened earlier by openChunk.  
                Once close chunk is called, all undoable operations in the chunk  
                will undo as a single undo operation.  
                Use with CAUTION!! Improper use of this command can leave the  
                undo queue in a bad state.  
                Properties: create
        infinity (bool?): Set the queue length to infinity.  
                Properties: create, query
        length (Queryable[int]?): Specifies the maximum number of items in the undo queue.  
                The infinity flag overrides this one.  
                Properties: create, query
        openChunk (bool?): Opens a chunk so that all undoable operations after this call  
                will fall into the newly opened chunk, until close chunk is called.  
                Once close chunk is called, all undoable operations in the chunk  
                will undo as a single undo operation.  
                Use with CAUTION!! Improper use of this command can leave the  
                undo queue in a bad state.  
                Properties: create
        printQueue (bool?): Prints to the Script Editor the contents of the undo queue.  
                Properties: query
        printRedoQueue (bool?): Prints to the Script Editor the contents of the redo queue.  
                Properties: query
        redoName (Queryable[str]?): Returns what will be redone (if anything)  
                Properties: query
        redoQueueEmpty (bool?): Return true if the redo queue is empty. Return false if  
                there is at least one command in the queue to be redone.  
                Properties: query
        state (bool?): Turns undo/redo on or off.  
                Properties: create, query
        stateWithoutFlush (bool?): Turns undo/redo on or off without flushing the queue. Use with CAUTION!!  
                Note that if you  perform destructive operations while stateWithoutFlush is  
                disabled, and you then enable it again, subsequent undo operations that try  
                to go past the  destructive operations may be unstable since undo will  
                not be able to properly reconstruct the former state of the scene.  
                Properties: create, query
        undoName (Queryable[str]?): Returns what will be undone (if anything)  
                Properties: query
        undoQueueEmpty (bool?): Return true if the undo queue is empty. Return false if  
                there is at least one command in the queue to be undone.  
                Properties: query

    Returns:
        str: If querying undoName or redoName
        int: If querying state, infinity, or length

    Example:
    """

