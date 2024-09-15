from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def controller(*args: str, edit: bool = ..., query: bool = ..., allControllers: bool = ..., children: bool = ..., group: bool = ..., index: Queryable[int] = ..., isController: Queryable[str] = ..., parent: bool = ..., pickWalkDown: bool = ..., pickWalkLeft: bool = ..., pickWalkRight: bool = ..., pickWalkUp: bool = ..., unparent: bool = ...) -> Union[str, bool, int]:
    """Commands for managing animation sourcescontroller
    Args:
        allControllers (bool?): When this flag is queried, returns all dependNode attached to a controller in the scene.  
                Properties: create, query
        children (bool?): Return true if the specified dependNode is a controller.  
                Properties: query
        group (bool?): Create a controller that is not associated with any object. This new controller will be the parent of all the selected objects.  
                Properties: create, query
        index (Queryable[int]?): In query mode, returns the index of the controller in the parent controller's list of children.  
                In edit mode, reorder the parent controller's children connections so that the current controller is assigned the given index.  
                Properties: query, edit
        isController (Queryable[str]?): Returns true if the specified dependNode is a controller.  
                Properties: create, query
        parent (bool?): Set or query the parent controller of the selected controller node.  
                Properties: create, query, edit
        pickWalkDown (bool?): Return the first child.  
                Properties: query
        pickWalkLeft (bool?): Return the previous sibling.  
                Properties: query
        pickWalkRight (bool?): Return the next sibling.  
                Properties: query
        pickWalkUp (bool?): Return the parent.  
                Properties: query
        unparent (bool?): Unparent all selected controller objects from their respective parent.  
                Properties: edit

    Returns:
        str: Command result

    Example:
    """

