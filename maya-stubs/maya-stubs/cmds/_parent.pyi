from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def parent(*args: str, absolute: bool = ..., addObject: bool = ..., noConnections: bool = ..., noInvScale: bool = ..., relative: bool = ..., removeObject: bool = ..., shape: bool = ..., world: bool = ...) -> List[str]:
    """This command parents (moves) objects under a new group, removes
    objects from an existing group, or adds/removes parents.If the -w flag is specified all the selected or specified objects
    are parented to the world (unparented first).If the -rm flag is specified then all the selected or specified
    instances are removed.If there are more than two objects specified all the objects are
    parented to the last object specified.If the -add flag is specified, the objects are not reparented but
    also become children of the last object specified.If there is only a single object specified then the selected objects
    are parented to that object.If an object is parented under a different group and there is
    an object in that group with the same name then this command
    will rename the parented object.
    Args:
        absolute (bool?): preserve existing world object transformations  
                (overall object transformation is preserved  
                by modifying the objects local transformation)  
                If the object to parent is a joint, it will  
                alter the translation and joint orientation of  
                the joint to preserve the world object  
                transformation if this suffices. Otherwise, a  
                transform will be inserted between the joint  
                and the parent for this purpose. In this case,  
                the transformation inside the joint is not  
                altered.  
                [default]  
                Properties: create
        addObject (bool?): preserve existing local object transformations  
                but don't reparent, just add the object(s) under  
                the parent. Use -world to add the world as  
                a parent of the given objects.  
                Properties: create
        noConnections (bool?): The parent command will normally generate  
                new instanced set connections when adding instances.  
                (ie. make a connection to the shading engine for  
                new instances) This flag suppresses this behaviour  
                and is primarily used by the file format.  
                Properties: create
        noInvScale (bool?): The parent command will normally connect  
                inverseScale to its parent scale on joints.  
                This is used to compensate scale on joint.  
                The connection of inverseScale will occur if both child and parent are joints and no connection is present on child's inverseScale.  
                In case of a reparenting, the old inverseScale will only get broken if the old parent is a joint. Otherwise connection will remain intact.  
                This flag suppresses this behaviour.  
                Properties: create
        relative (bool?): preserve existing local object transformations  
                (relative to the parent node)  
                Properties: create
        removeObject (bool?): Remove the immediate parent of every object specified. To remove only  
                a single instance of a shape from a parent, the path to the shape  
                should be specified.  
                Note: if there is a single parent then the object is effectively deleted from  
                the scene. Use -world to remove the world as a parent of the given object.  
                Properties: create
        shape (bool?): The parent command usually only operates on  
                transforms.  Using this flags allows a shape  
                that is specified to be directly parented under  
                the given transform.  This is used to instance  
                a shape node. (ie. "parent -add -shape"    is  
                equivalent to the "instance" command).  
                This flag is primarily used by the file format.  
                Properties: create
        world (bool?): unparent given object(s) (parent to world)  
                Properties: create

    Returns:
        List[str]: Names of the objects parented (possibly renamed)

    Example:
    """

