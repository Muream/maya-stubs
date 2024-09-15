from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attributeInfo(*args: str, allAttributes: bool = ..., bool: bool = ..., enumerated: bool = ..., hidden: bool = ..., inherited: bool = ..., internal: bool = ..., leaf: bool = ..., logicalAnd: bool = ..., multi: bool = ..., short: bool = ..., userInterface: bool = ..., writable: bool = ..., type: str = ...) -> List[str]:
    """This command lists all of the attributes that are marked with certain
    flags.  Combinations of flags may be specified and all will be considered.
    (The method of combination depends on the state of the "logicalAnd/and" flag.)
    When the "allAttributes/all" flag is specified, attributes of all
    types will be listed.attribute
    Args:
        allAttributes (bool?): Show all attributes associated with the node regardless of type.  
                Use of this flag overrides any other attribute type flags and logical operation  
                that may be specified on the command.  
                Properties: create
        bool (bool?): Show the attributes that are of type boolean.  
                Use the 'on' state to get only boolean attributes; the 'off' state  
                to ignore boolean attributes.  
                Properties: create
        enumerated (bool?): Show the attributes that are of type enumerated.  
                Use the 'on' state to get only enumerated attributes; the 'off' state  
                to ignore enumerated attributes.  
                Properties: create
        hidden (bool?): Show the attributes that are marked as hidden.  
                Use the 'on' state to get hidden attributes; the 'off' state  
                to get non-hidden attributes.  
                Properties: create
        inherited (bool?): Filter the attributes based on whether they belong to the node type directly  
                or have been inherited from a root type (e.g. meshShape/direct or  
                dagObject/inherited).  
                Use the 'on' state to get only inherited attributes, the 'off' state  
                to get only directly owned attributes, and leave the flag unspecified to  
                get both.  
                Properties: create
        internal (bool?): Show the attributes that are marked as internal to the node.  
                Use the 'on' state to get internal attributes; the 'off' state  
                to get non-internal attributes.  
                Properties: create
        leaf (bool?): Show the attributes that are complex leaves (ie. that have parent attributes  
                and have no children themselves).  
                Use the 'on' state to get leaf attributes; the 'off' state  
                to get non-leaf attributes.  
                Properties: create
        logicalAnd (bool?): The default is to take the logical 'or' of the above conditions.  
                Specifying this flag switches to the logical 'and' instead.  
                Properties: create
        multi (bool?): Show the attributes that are multis.  
                Use the 'on' state to get multi attributes; the 'off' state  
                to get non-multi attributes.  
                Properties: create
        short (bool?): Show the short attribute names instead of the long names.  
                Properties: create
        userInterface (bool?): Show the UI-friendly attribute names instead of the Maya ASCII names.  
                Takes precedence over the -s/-short flag if both are specified.  
                Properties: create
        writable (bool?): Show the attributes that are writable (ie. can have input connections).  
                Use the 'on' state to get writable attributes; the 'off' state  
                to get non-writable attributes.  
                Properties: create
        type (str?): static node type from which to get 'affects' information  
                Properties: create

    Returns:
        List[str]: List of attributes matching criteria

    Example:
    """

