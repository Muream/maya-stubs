from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toolCollection(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., collectionItemArray: bool = ..., defineTemplate: str = ..., exists: bool = ..., gl: bool = ..., numberOfCollectionItems: bool = ..., parent: str = ..., select: Queryable[str] = ..., useTemplate: str = ...) -> Union[str, bool]:
    """This command creates a tool button collection. Collections are parented
    to the current default layout if no parent is specified with
    the -p/parent flag.  As children of the layout they will be deleted when
    the layout is deleted. Collections may also span more than one window
    if the -gl/global flag is used. In this case the collection has no parent
    and must be explicitly deleted with the 'deleteUI' command when it is no
    longer wanted.
    Args:
        collectionItemArray (bool?): Returns a string list giving the long names of all the items  
                in this collection.  
                Properties: query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        gl (bool?): Set the collection to have no parent layout.  This flag must be  
                specified when the collection is created and can not be queried  
                or edited.  Consequently, global collections must be explicitly  
                deleted.  
                Properties: create, query
        numberOfCollectionItems (bool?): Returns the number of items that are in this collection.  
                Properties: query
        parent (str?): Specify the parent to associate the collection with.  The collection  
                will be deleted along with the parent.  This flag must be specified  
                when the collection is created and can not be edited.  
                Properties: create
        select (Queryable[str]?): Select the specified collection item.  If queried will return  
                the name of the currently selected collection item.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: The name of the toolCollection created.

    Example:
    """

