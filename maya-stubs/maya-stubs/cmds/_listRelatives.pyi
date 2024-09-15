from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listRelatives(*args: str, allDescendents: bool = ..., allParents: bool = ..., children: bool = ..., fullPath: bool = ..., noIntermediate: bool = ..., parent: bool = ..., path: bool = ..., shapes: bool = ..., type: Multiuse[str] = ...) -> List[str]:
    """This command lists parents and children of DAG objects. The flags
    -c/children, -ad/allDescendents, -s/shapes, -p/parent and -ap/allParents
    are mutually exclusive. Only one can be used in a command.Unlike ls, this command does not return a unique path but simply returns
    the object's name by default. To get a unique path the -path flag must
    be used.When listing parents of objects directly under the world, the command
    will return an empty parent list. Listing parents of objects directly
    under a shape (underworld objects) will return their containing shape
    node in the list of parents. Listing parents of components of objects
    will return the object.When listing children, shape nodes will return their underworld
    objects in the list of children. Listing children of components of
    objects returns nothing.The -ni/noIntermediate flag works with the -s/shapes flag.
    It causes any intermediate shapes among the descendents to be ignored.
    Args:
        allDescendents (bool?): Returns all the children, grand-children etc. of  
                this dag node.  If a descendent is instanced,  
                it will appear only once on the list returned.  
                Note that it lists grand-children before children.  
                Properties: create
        allParents (bool?): Returns all the parents of this dag node. Normally, this  
                command only returns the parent corresponding to the first  
                instance of the object  
                Properties: create
        children (bool?): List all the children of this dag node (default).  
                Properties: create
        fullPath (bool?): Return full pathnames instead of object names.  
                Properties: create
        noIntermediate (bool?): No intermediate objects  
                Properties: create
        parent (bool?): Returns the parent of this dag node  
                Properties: create
        path (bool?): Return a proper object name that can be passed to other commands.  
                Properties: create
        shapes (bool?): List all the children of this dag node that are  
                shapes (ie, not transforms)  
                Properties: create
        type (Multiuse[str]?): List all relatives of the specified type.  
                Properties: create, multiuse

    Returns:
        List[str]: Command result

    Example:
    """

