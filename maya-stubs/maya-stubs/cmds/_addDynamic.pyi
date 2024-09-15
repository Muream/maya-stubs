from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def addDynamic(*args: str) -> str:
    """Makes the "object" specified as second argument the source of an
    existing field or emitter specified as the first argument. In
    practical terms, what this means is that a field will emanate its
    force from its owner object, and an emitter will emit from its owner
    object.addDynamic makes the specified field or emitter a child of
    the owner's transform (adding it to the model if it was not already
    there), and makes the necessary attribute connections.If either of the arguments is omitted, addDynamic searches the
    selection list for objects to use instead. If more than one possible
    owner or field/emitter is selected, addDynamic will do
    nothing.If the specified field/emitter already has a source, addDynamic will
    remove the current source and replace it with the newly specified
    source.If a subset of the owner object's cvs/particles/vertices is selected,
    addDynamic will add the field/emitter to that subset only.
    Returns:
        str: The name of the source object and the field or emitter which was
            attached to it.

    Example:
    """

