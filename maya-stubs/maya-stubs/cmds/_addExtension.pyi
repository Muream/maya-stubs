from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def addExtension(*, edit: bool = ..., query: bool = ..., nodeType: Queryable[str] = ..., attributeType: Queryable[str] = ..., binaryTag: Queryable[str] = ..., cachedInternally: bool = ..., category: Queryable[Multiuse[str]] = ..., dataType: Queryable[Multiuse[str]] = ..., defaultValue: Queryable[float] = ..., disconnectBehaviour: Queryable[int] = ..., enumName: Queryable[str] = ..., exists: bool = ..., fromPlugin: bool = ..., hasMaxValue: bool = ..., hasMinValue: bool = ..., hasSoftMaxValue: bool = ..., hasSoftMinValue: bool = ..., hidden: bool = ..., indexMatters: bool = ..., internalSet: bool = ..., keyable: bool = ..., longName: Queryable[str] = ..., maxValue: Queryable[float] = ..., minValue: Queryable[float] = ..., multi: bool = ..., niceName: Queryable[str] = ..., numberOfChildren: Queryable[int] = ..., parent: Queryable[str] = ..., proxy: Queryable[str] = ..., readable: bool = ..., shortName: Queryable[str] = ..., softMaxValue: Queryable[float] = ..., softMinValue: Queryable[float] = ..., storable: bool = ..., usedAsColor: bool = ..., usedAsFilename: bool = ..., usedAsProxy: bool = ..., worldSpace: bool = ..., writable: bool = ...) -> Union[bool, str, Multiuse[str], float, int]:
    """This command is used to add an extension attribute to a node type.
    Either the longName or the shortName or both must be specified.
    If neither a dataType nor an attributeType is specified, a double
    attribute will be added.  The dataType flag can be specified more than
    once indicating that any of the supplied types will be accepted (logical-or).To add a non-double attribute the following criteria
    can be used to determine whether the dataType or the attributeType
    flag is appropriate.  Some types, such ascan use either.
    In these cases theflag should be used when you only wish to
    access the data as an atomic entity (eg. you never want to access the
    three individual values that make up a).  In general it
    is best to use thein these cases for maximum flexibility.
    In most cases theversion will not display in the attribute
    editor as it is an atomic type and you are not allowed to change
    individual parts of it.All attributes flagged as "(compound)" below or the compound attribute itself
    are not actually added to the node until all of the children are defined
    (using the "-p" flag to set their parent to the compound being created).  See
    the EXAMPLES section for more details.attribute, dependency, graph, add, dynamic, create
    Args:
        nodeType (Queryable[str]?): Specifies the type of node to which the attribute will be added.  
                See the nodeType command for the names of different node types.  
                Properties: create, query, edit
        attributeType (Queryable[str]?): Specifies the attribute type, see above table for more details.  
                Note that the attribute types "float", "matrix" and "string"  
                are also MEL keywords and must be enclosed in quotes.  
                Properties: create, query
        binaryTag (Queryable[str]?): This flag is obsolete and does not do anything any more  
                Properties: create, query
        cachedInternally (bool?): Whether or not attribute data is cached internally in the node.  
                This flag defaults to true for writable attributes and false  
                for non-writable attributes. A warning will be issued if  
                users attempt to force a writable attribute to be uncached as  
                this will make it impossible to set keyframes.  
                Properties: create, query
        category (Queryable[Multiuse[str]]?): An attribute category is a string associated with the attribute to identify it.  
                (e.g. the name of a plugin that created the attribute, version information, etc.)  
                Any attribute can be associated with an arbitrary number of categories however  
                categories can not be removed once associated.  
                Properties: create, query, edit, multiuse
        dataType (Queryable[Multiuse[str]]?): Specifies the data type.  See "setAttr" for  
                more information on data type names.  
                Properties: create, query, multiuse
        defaultValue (Queryable[float]?): Specifies the default value for the attribute  
                (can only be used for numeric attributes).  
                Properties: create, query, edit
        disconnectBehaviour (Queryable[int]?): defines the Disconnect Behaviour 2 Nothing, 1 Reset, 0 Delete  
                Properties: create, query
        enumName (Queryable[str]?): Flag used to specify the ui names corresponding to the enum values. The specified string should contain a colon-separated list of the names, with optional values. If values are not specified, they will treated as sequential integers starting with 0. For example: -enumName "A:B:C" would produce options: A,B,C with values of 0,1,2; -enumName "zero:one:two:thousand=1000" would produce four options with values 0,1,2,1000; and -enumName "solo=1. triplet=3. quintet=5" would produce three options with values 1,3,5.  (Note that there is a current limitation of the Channel Box that will sometimes incorrectly display an enumerated attribute's pull-down menu.  Extra menu items can appear that represent the numbers inbetween non-sequential option values.  To avoid this limitation, specify sequential values for the options of any enumerated attributes that will appear in the Channel Box.  For example: "solo=1. triplet=2. quintet=3".)  
                Properties: create, query, edit
        exists (bool?): Returns true if the attribute queried is a user-added, dynamic attribute; false if not.  
                Properties: create, query
        fromPlugin (bool?): Was the attribute originally created by a plugin? Normally set  
                automatically when the API call is made - only added here to support  
                storing it in a file independently from the creating plugin.  
                Properties: create, query
        hasMaxValue (bool?): Flag indicating whether an attribute has a maximum value.  
                (can only be used for numeric attributes).  
                Properties: create, query, edit
        hasMinValue (bool?): Flag indicating whether an attribute has a minimum value.  
                (can only be used for numeric attributes).  
                Properties: create, query, edit
        hasSoftMaxValue (bool?): Flag indicating whether a numeric attribute has a soft maximum.  
                Properties: create, query
        hasSoftMinValue (bool?): Flag indicating whether a numeric attribute has a soft minimum.  
                Properties: create, query
        hidden (bool?): Will this attribute be hidden from the UI?  
                Properties: create, query
        indexMatters (bool?): Sets whether an index must be used when connecting  
                to this multi-attribute. Setting indexMatters to false forces the  
                attribute to non-readable.  
                Properties: create, query
        internalSet (bool?): Whether or not the internal cached value is set when  
                this attribute value is changed.  This is an internal flag  
                used for updating UI elements.  
                Properties: create, query
        keyable (bool?): Is the attribute keyable by default?  
                Properties: create, query
        longName (Queryable[str]?): Sets the long name of the attribute.  
                Properties: create, query
        maxValue (Queryable[float]?): Specifies the maximum value for the attribute  
                (can only be used for numeric attributes).  
                Properties: create, query, edit
        minValue (Queryable[float]?): Specifies the minimum value for the attribute  
                (can only be used for numeric attributes).  
                Properties: create, query, edit
        multi (bool?): Makes the new attribute a multi-attribute.  
                Properties: create, query
        niceName (Queryable[str]?): Sets the nice name of the attribute for display in the UI.  Setting the  
                attribute's nice name to a non-empty string overrides the default  
                behaviour of looking up the nice name from Maya's  
                string catalog.   (Use the MEL commands  
                "attributeNiceName" and "attributeQuery -niceName" to lookup an attribute's  
                nice name in the catalog.)  
                Properties: create, query, edit
        numberOfChildren (Queryable[int]?): How many children will the new attribute have?  
                Properties: create, query
        parent (Queryable[str]?): Attribute that is to be the new attribute's parent.  
                Properties: create, query
        proxy (Queryable[str]?): Proxy another node's attribute. Proxied plug will be connected as source. The UsedAsProxy flag is automatically set in this case.  
                Properties: create, query
        readable (bool?): Can outgoing connections be made from this attribute?  
                Properties: create, query
        shortName (Queryable[str]?): Sets the short name of the attribute.  
                Properties: create, query
        softMaxValue (Queryable[float]?): Soft maximum, valid for numeric attributes only.  Specifies the  
                upper default limit used in sliders for this attribute.  
                Properties: create, query, edit
        softMinValue (Queryable[float]?): Soft minimum, valid for numeric attributes only.  Specifies the  
                lower default limit used in sliders for this attribute.  
                Properties: create, query, edit
        storable (bool?): Can the attribute be stored out to a file?  
                Properties: create, query
        usedAsColor (bool?): Is the attribute to be used as a color definition?  
                Must have 3 DOUBLE or 3 FLOAT children to use this  
                flag.  The attribute type "-at" should be "double3"  
                or "float3" as appropriate.  It can also be used to  
                less effect with data types "-dt" as "double3" or  
                "float3" as well but some parts of the code do not  
                support this alternative.  The special attribute  
                types/data "spectrum" and "reflectance" also support  
                the color flag and on them it is set by default.  
                Properties: create, query
        usedAsFilename (bool?): Is the attribute to be treated as a filename definition?  
                This flag is only supported on attributes with data type "-dt" of "string".  
                Properties: create, query
        usedAsProxy (bool?): Set if the specified attribute should be treated as a proxy to another attributes.  
                Properties: create, query
        worldSpace (bool?): Sets whether this attribute should be treated as worldspace.  
                Being worldspace indicates the attribute is dependent on the worldSpace  
                transformation of this node, and will be marked dirty by any attribute  
                changes in the hierarchy that affects the worldSpace transformation. The  
                attribute needs to be an array since during instancing there are  
                multiple worldSpace paths to the node and Maya requires one array element  
                per path for worldSpace attributes. Remarks:  
                1. Can only be used on array attributes.  
                2. This property is ignored on non-dag nodes.  
                3. The attribute should be affected by another attribute or have a connection.  
                   Otherwise, the attribute will not get computed and will not get dirty again.  
                Properties: create, query
        writable (bool?): Can incoming connections be made to this attribute?  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

