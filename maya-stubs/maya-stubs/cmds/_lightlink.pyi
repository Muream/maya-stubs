from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def lightlink(*args: str, query: bool = ..., b: bool = ..., hierarchy: bool = ..., light: Multiuse[str] = ..., make: bool = ..., object: Multiuse[str] = ..., sets: bool = ..., shadow: bool = ..., shapes: bool = ..., transforms: bool = ..., useActiveLights: bool = ..., useActiveObjects: bool = ...) -> Union[str, List[str]]:
    """This command is used to make, break and query light linking
    relationships between lights/sets of lights and objects/sets of
    objects.If no make, break or query flag is specified and both lights and
    objects flags are present, the make flag is assumed to be specified.If no make, break or query flag is specified and only one of the
    lights and objects flags is present, the query flag is assumed to be
    specified.You can specify as many lights and objects as you like, using the
    multiuse -light and -object flags.A better way to perform light linking is to make sets of lights and
    sets of geometry. If you create a set which contains lights (such as
    the ceiling lights in your scene) and a set which contains geometry
    (such as the geometry of your character), you can then link thecontaining lights with thecontaining geometry
    in order to get those lights to illuminate those pieces of geometry.
    In addition, you can add and remove lights and geometry from their
    respective sets without having to make and break light links.
    Args:
        b (bool?): The presence of this flag on the command indicates that the  
                command is being invoked to break links between lights and  
                renderable objects.  
                Properties: create
        hierarchy (bool?): When querying, specifies whether the result should include the  
                hierarchy of transforms above shapes linked to the queried  
                light/object. The transforms considered part of the hierarchy do  
                not include the transform immediately above the shape. Default  
                is true.  
                Properties: create
        light (Multiuse[str]?): The argument to the light flag specifies a node to be used by  
                the command in performing the action as if the node is a light.  
                This is a multiuse flag -- many light nodes can be specified in  
                a single invocation of the lightlink command.  
                Properties: create, multiuse
        make (bool?): The presence of this flag on the command indicates that the  
                command is being invoked to make links between lights and  
                renderable objects.  
                Properties: create
        object (Multiuse[str]?): The argument to the object flag specifies a node to be used by  
                the command in performing the action as if the node is an object.  
                This is a multiuse flag -- many object nodes can be specified in  
                a single invocation of the lightlink command.  
                Properties: create, multiuse
        sets (bool?): When querying, specifies whether the result should include sets  
                linked to the queried light/object. Default is true.  
                Properties: create
        shadow (bool?): Specify that shadows are to be linked.  
                Properties: create
        shapes (bool?): When querying, specifies whether the result should include shapes  
                linked to the queried light/object. Default is true.  
                Properties: create
        transforms (bool?): When querying, specifies whether the result should include  
                transforms immediately above shapes linked to the queried  
                light/object. Default is true.  
                Properties: create
        useActiveLights (bool?): Specify that active lights are to be used.  
                Properties: create
        useActiveObjects (bool?): Specify that active objects are to be used.  
                Properties: create

    Returns:
        str: Single element command result
        List[str]: Multi element command result

    Example:
    """

