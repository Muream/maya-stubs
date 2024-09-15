from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def isolateSelect(arg0: str = ..., /, *, query: bool = ..., addDagObject: str = ..., addSelected: bool = ..., addSelectedObjects: bool = ..., loadSelected: bool = ..., removeDagObject: str = ..., removeSelected: bool = ..., state: bool = ..., update: bool = ..., viewObjects: bool = ...) -> bool:
    """This command turns on/off isolate select mode in a specified modeling
    view, specified as the argument. Isolate select mode is a display mode
    where the currently selected objects are added to a list and only
    those objects are displayed in the view. It allows for selective
    viewing of specific objects and object components.
    Args:
        addDagObject (str?): Add the specified object to the set of objects to be  
                displayed in the view.
        addSelected (bool?): Add the currently active objects to the set of  
                objects to be displayed in the view.
        addSelectedObjects (bool?): Add selected objects to the set of objects to be displayed in the view.  
                This flag differs from addSelected in that it will ignore selected components  
                and add the entire object.
        loadSelected (bool?): Replace the objects being displayed with the currently  
                active objects.
        removeDagObject (str?): Remove the specified object from the set of objects to be  
                displayed in the view.
        removeSelected (bool?): Remove the currently active objects to the set of  
                objects to be displayed in the view.
        state (bool?): Turns isolate select mode on/off.  
                Properties: query
        update (bool?): Update the view's list of objects due to a change  
                to the set of objects to be displayed.
        viewObjects (bool?): Returns the name (if any) of the objectSet which contains  
                the list of objects visible in the view if isolate select mode  
                is on. If isolate select mode is off, an empty string is  
                returned.  
                Properties: query

    Returns:
        bool: When used with query

    Example:
    """

