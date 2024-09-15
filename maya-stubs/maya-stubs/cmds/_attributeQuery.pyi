from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attributeQuery(arg0: str = ..., /, *, affectsAppearance: bool = ..., affectsWorldspace: bool = ..., attributeType: bool = ..., cachedInternally: bool = ..., categories: bool = ..., channelBox: bool = ..., connectable: bool = ..., enum: bool = ..., exists: bool = ..., hidden: bool = ..., indeterminant: bool = ..., indexMatters: bool = ..., internal: bool = ..., internalGet: bool = ..., internalSet: bool = ..., keyable: bool = ..., listChildren: bool = ..., listDefault: bool = ..., listEnum: bool = ..., listParent: bool = ..., listSiblings: bool = ..., localizedListEnum: bool = ..., longName: bool = ..., maxExists: bool = ..., maximum: bool = ..., message: bool = ..., minExists: bool = ..., minimum: bool = ..., multi: bool = ..., niceName: bool = ..., node: str = ..., numberOfChildren: bool = ..., range: bool = ..., rangeExists: bool = ..., readable: bool = ..., renderSource: bool = ..., shortName: bool = ..., softMax: bool = ..., softMaxExists: bool = ..., softMin: bool = ..., softMinExists: bool = ..., softRange: bool = ..., softRangeExists: bool = ..., storable: bool = ..., type: str = ..., typeExact: str = ..., usedAsColor: bool = ..., usedAsFilename: bool = ..., usesMultiBuilder: bool = ..., worldspace: bool = ..., writable: bool = ...) -> Union[List[float], bool]:
    """attributeQuery returns information about the configuration of an attribute.
    It handles both boolean flags, returning true or false, as well as other return values.
    Specifying more than one boolean flag will return the logical "and"
    of all the specified boolean flags.  You may not specify any two flags when both do not
    provide a boolean return type.  (eg. "-internal -hidden" is okay but "-range -hidden" or
    "-range -softRange" is not.)dg, dependency, graph, attribute, query
    Args:
        affectsAppearance (bool?): Return true if the attribute affects the appearance of the node  
                Properties: create
        affectsWorldspace (bool?): Return the status of the attribute flag marking attributes affecting worldspace  
                Properties: create
        attributeType (bool?): Return the name of the attribute type (will be the same type names as described in the addAttr and addExtension commands).  
                Properties: create
        cachedInternally (bool?): Return whether the attribute is cached within the node as well as in the datablock  
                Properties: create
        categories (bool?): Return the categories to which the attribute belongs or an empty list if it does not belong to any.  
                Properties: create
        channelBox (bool?): Return whether the attribute should show up in the channelBox or not  
                Properties: create
        connectable (bool?): Return the connectable status of the attribute  
                Properties: create
        enum (bool?): Return true if the attribute is a enum attribute  
                Properties: create
        exists (bool?): Return true if the attribute exists  
                Properties: create
        hidden (bool?): Return the hidden status of the attribute  
                Properties: create
        indeterminant (bool?): Return true if this attribute might be used in evaluation but it's not known for sure until evaluation time  
                Properties: create
        indexMatters (bool?): Return the indexMatters status of the attribute  
                Properties: create
        internal (bool?): Return true if the attribute is either internalSet or internalGet  
                Properties: create
        internalGet (bool?): Return true if the attribute come from getCachedValue  
                Properties: create
        internalSet (bool?): Return true if the attribute must be set through setCachedValue  
                Properties: create
        keyable (bool?): Return the keyable status of the attribute  
                Properties: create
        listChildren (bool?): Return the list of children attributes of the given attribute.  
                Properties: create
        listDefault (bool?): Return the default values of numeric and compound numeric attributes.  
                Properties: create
        listEnum (bool?): Return the list of enum strings for the given attribute.  
                Properties: create
        listParent (bool?): Return the parent of the given attribute.  
                Properties: create
        listSiblings (bool?): Return the list of sibling attributes of the given attribute.  
                Properties: create
        localizedListEnum (bool?): Return the list of localized enum strings for the given attribute.  
                Properties: create
        longName (bool?): Return the long name of the attribute.  
                Properties: create
        maxExists (bool?): Return true if the attribute has a hard maximum. A min does not have to be present.  
                Properties: create
        maximum (bool?): Return the hard maximum of the attribute's value  
                Properties: create
        message (bool?): Return true if the attribute is a message attribute  
                Properties: create
        minExists (bool?): Return true if the attribute has a hard minimum. A max does not have to be present.  
                Properties: create
        minimum (bool?): Return the hard minimum of the attribute's value  
                Properties: create
        multi (bool?): Return true if the attribute is a multi-attribute  
                Properties: create
        niceName (bool?): Return the nice name (or "UI name") of the attribute.  
                Properties: create
        node (str?): Use all attributes from node named NAME  
                Properties: create
        numberOfChildren (bool?): Return the number of children the attribute has  
                Properties: create
        range (bool?): Return the hard range of the attribute's value  
                Properties: create
        rangeExists (bool?): Return true if the attribute has a hard range. Both min and max must be present.  
                Properties: create
        readable (bool?): Return the readable status of the attribute  
                Properties: create
        renderSource (bool?): Return whether this attribute is marked as a render source or not  
                Properties: create
        shortName (bool?): Return the short name of the attribute.  
                Properties: create
        softMax (bool?): Return the soft max (slider range) of the attribute's value  
                Properties: create
        softMaxExists (bool?): Return true if the attribute has a soft maximum. A min does not have to be present.  
                Properties: create
        softMin (bool?): Return the soft min (slider range) of the attribute's value  
                Properties: create
        softMinExists (bool?): Return true if the attribute has a soft minimum. A max does not have to be present.  
                Properties: create
        softRange (bool?): Return the soft range (slider range) of the attribute's value  
                Properties: create
        softRangeExists (bool?): Return true if the attribute has a soft range. Both min and max must be present.  
                Properties: create
        storable (bool?): Return true if the attribute is storable  
                Properties: create
        type (str?): Use static attributes from nodes of type TYPE.  Includes attributes inherited from parent class nodes.  
                Properties: create
        typeExact (str?): Use static attributes only from nodes of type TYPE.  Does not included inherited attributes.  
                Properties: create
        usedAsColor (bool?): Return true if the attribute should bring up a color picker  
                Properties: create
        usedAsFilename (bool?): Return true if the attribute should bring up a file browser  
                Properties: create
        usesMultiBuilder (bool?): Return true if the attribute is a multi-attribute and it uses the multi-builder to handle its data  
                Properties: create
        worldspace (bool?): Return the status of the attribute flag marking worldspace attribute  
                Properties: create
        writable (bool?): Return the writable status of the attribute  
                Properties: create

    Returns:
        List[float]: when querying ranges or default values
        bool: when querying attribute flags

    Example:
    """

