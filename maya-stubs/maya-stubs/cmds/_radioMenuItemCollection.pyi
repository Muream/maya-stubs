from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def radioMenuItemCollection(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., defineTemplate: str = ..., exists: bool = ..., gl: bool = ..., parent: str = ..., useTemplate: str = ...) -> Union[str, bool]:
    """This command creates a radioMenuItemCollection.  Attach radio menu
    items to radio menu item collection objects to get radio button
    behaviour.  Radio menu item collections will be parented to the
    current menu if no parent is specified with theflag. As children of the menu they will be deleted when the menu is
    deleted. Collections may also span more than one menu if
    theflag is used. In this case the collection has no
    parent menu and must be explicitly deleted with thecommand when it is no longer wanted.
    Args:
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        gl (bool?): Set the collection to have no parent menu.  Global  
                collections must be explicitly deleted.  
                Properties: create, query
        parent (str?): The parent of the collection.  The collection will be deleted  
                along with the parent.  
                Properties: create
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: Full path name to the collection.

    Example:
    """

