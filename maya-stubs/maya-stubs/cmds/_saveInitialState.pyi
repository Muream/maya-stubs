from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def saveInitialState(*args: str, attribute: Multiuse[str] = ..., saveall: bool = ...) -> str:
    """saveInitialState saves the current state of dynamics objects as
    the initial state.  A dynamic object is a particle shape, rigid body, rigid
    constraint or rigid solver.  If no objects are specified, it saves the
    initial state for any selected objects.
    It returns the names of the objects for which initial state was saved.
    Args:
        attribute (Multiuse[str]?): Save the initial state of the specified attribute only.  
                This is a multi-use flag.  
                Properties: create, multiuse
        saveall (bool?): Save the initial state for all dynamics objects in the scene.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

