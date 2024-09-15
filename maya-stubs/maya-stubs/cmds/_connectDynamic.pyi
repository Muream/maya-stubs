from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def connectDynamic(*args: str, addScriptHandler: Callable[..., Any] = ..., collisions: Multiuse[str] = ..., delete: bool = ..., emitters: Multiuse[str] = ..., fields: Multiuse[str] = ..., removeScriptHandler: int = ...) -> str:
    """Dynamic connection specifies that the force fields, emitters, or collisions
    of an object affect another dynamic object. The dynamic object that is
    connected to a field, emitter, or collision object is influenced by those
    fields, emitters and collision objects.Connections are made to individual fields, emitters, collisions.  So, if
    an object owns several fields, if the user wants some of the fields to
    affect an object, s/he can specify each field with a "-f" flag; but if
    the user wants to connect all the fields owned by an object, s/he can
    specify the object name with the "-f" flag. The same is true for
    emitters and collisions.
    Different connection types (i.e., for fields vs. emitters)
    between the same pair of objects are logically
    independent. In other words, an
    object can be influenced by another object's fields without being
    influenced by its emitters or collisions.Each connected object must be a dynamic object. The object connected to
    can be any object that
    owns fields, emitters, etc.; it need not be dynamic. Objects that can
    own influences are particles, geometry objects (nurbs and polys) and
    lattices.  You can specify either the shape name or the transform name of
    the object to be influenced.
    Args:
        addScriptHandler (Callable[..., Any]?): Registers a script that will be given a chance to handle calls to the  
                dynamicConnect command. This flag allows other dynamics systems to  
                override the behaviour of the connectDynamic command. You must pass a Python  
                function as the argument for this flag, and that function must take the  
                following keyword arguments: fields, emitters, collisionObjects and objects.  
                The python function must return True if it has handled the call to  
                connectDynamic. In the case that the script returns true, the connectDynamic  
                command will not do anything as it assumes that the work was handled by the  
                script. If all of the callbacks return false, the connectDynamic command will  
                proceed as normal.  
              
                The addScriptHandler flag may not be used with any other flags. When the  
                flag is used, the command will return a numerical id that can be used to  
                deregister the callback later (see the removeScriptHandler flag)  
                Properties: create
        collisions (Multiuse[str]?): Connects each object to the collision models of the given object.  
                Properties: create, multiuse
        delete (bool?): Deletes existing connections.  
                Properties: create
        emitters (Multiuse[str]?): Connects each object to the emitters of the given object.  
                Properties: create, multiuse
        fields (Multiuse[str]?): Connects each object to the fields of the given object.  
                Properties: create, multiuse
        removeScriptHandler (int?): This flag is used to remove a callback that was previously registered  
                with the addScriptHandler flag. The argument to this flag is the numerical  
                id returned by dynamicConnect when the addScriptHandler flag was used.  
                If this flag is called with an invalid id, then the command will do  
                nothing.  
              
                This flag may not be used with any other flag.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

