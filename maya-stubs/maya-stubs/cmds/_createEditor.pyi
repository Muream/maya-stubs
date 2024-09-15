from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def createEditor(arg0: str = ..., arg1: str = ..., /, *, noCloseOnDelete: bool = ..., queueForDelete: bool = ...) -> bool:
    """This command creates a property sheet for any dependency node. The
    second argument is the name of the node, and the first is the name of
    a layout into which the property sheet controls should be placed.The property sheets created by this command can by user-customized
    using thecommand.
    Args:
        noCloseOnDelete (bool?): If this flag is set then don't close the editor when the data is deleted  
                Properties: create
        queueForDelete (bool?): The specified layout is put on a queue.  When the queue  
                is full, layouts past the end of the queue are automatically  
                deleted.  If the layout is already on the queue, it is  
                moved to the front.  This allows us to dispose of editors  
                when they are no longer being used.  This flag should only be  
                used by the showEditor.mel script.  
                Properties: create

    Returns:
        bool:

    Example:
    """

