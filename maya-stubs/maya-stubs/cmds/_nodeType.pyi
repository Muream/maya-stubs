from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nodeType(arg0: str = ..., /, *, apiType: bool = ..., derived: bool = ..., inherited: bool = ..., isTypeName: bool = ..., ufeRuntimeName: bool = ...) -> Union[str, List[str]]:
    """This command returns a string which identifies the given node's type.When no flags are used, the unique type name is returned.  This can be
    useful for seeing if two nodes are of the same type.When theflag is used, the MFn::Type of the node is returned.
    This can be useful for seeing if a plug-in node belongs to a given
    class. Theflag cannot be used in conjunction with any other
    flags.When theflag is used, the command returns a string array
    containing the names of all the currently known node types which derive
    from the node type of the given object.When theflag is used, the command returns a string array
    containing the names of all the base node types inherited by the
    the given node.If theflag is present then the argument provided to the
    command is taken to be the name of a node type rather than the name of a
    specific node. This makes it possible to query the hierarchy of node types
    without needing to have instances of each node type.
    Args:
        apiType (bool?): Return the MFn::Type value (as a string) corresponding  
                to the given node.  This is particularly useful when  
                the given node is defined by a plug-in, since in this  
                case, the MFn::Type value corresponds to the  
                underlying proxy class.  
              
                This flag cannot be used in combination with any of the other flags.  
                Properties: create
        derived (bool?): Return a string array containing the names of all the currently known node  
                types which derive from the type of the specified node.  
                Properties: create
        inherited (bool?): Return a string array containing the names of all the  
                base node types inherited by the specified node.  
                Properties: create
        isTypeName (bool?): If this flag is present, then the argument provided to the command  
                is the name of a node type rather than the name of a specific node.  
                Properties: create
        ufeRuntimeName (bool?): Return the UFE Runtime name corresponding to the given node.  
                This is particularly useful to filter between native Maya objects  
                and non-native objects exposed to Maya through the UFE interface.  
                Properties: create

    Returns:
        str: Single command result
        List[str]: Multiple command result

    Example:
    """

