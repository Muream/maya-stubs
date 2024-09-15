from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def instance(*args: str, leaf: bool = ..., name: str = ..., smartTransform: bool = ...) -> str:
    """Instancing is a way of making the same object appear twice in the
    scene. This is accomplished by creation of a new transform node
    that points to an exisiting object. Changes to the transform
    are independent but changes to the "instanced" object affect
    all instances since the node is shared.If no objects are given, then the selected list is instanced.
    When an object is instanced a  new transform node is created
    that points to the selected object.The smart transform feature allows instance to transform newly
    instanced objects based on previous transformations between instances.Example: Instance an object and move it to a new location.  Instance
    it again with the smart transform flag.  It should have moved once
    again the distance you had previously moved it.Note: changing the selected list between smart instances will cause
    the transform information to be deleted.It returns a list of the new objects created by the instance operation.duplicate
    Args:
        leaf (bool?): Instances leaf-level objects. Acts like duplicate  
                except leaf-level objects are instanced.  
                Properties: create
        name (str?): Name to give new instance  
                Properties: create
        smartTransform (bool?): Transforms instances item based on movements between  
                transforms  
                Properties: create

    Returns:
        str: - the name of the new transform node is returned.

    Example:
    """

