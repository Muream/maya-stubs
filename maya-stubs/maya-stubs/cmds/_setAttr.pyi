from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def setAttr(*args: str, edit: bool = ..., query: bool = ..., alteredValue: bool = ..., caching: bool = ..., capacityHint: int = ..., channelBox: bool = ..., clamp: bool = ..., keyable: bool = ..., lock: bool = ..., size: int = ..., type: str = ...) -> bool:
    """Sets the value of a dependency node attribute.  No value for
    the attribute is needed when theflags are used.
    Theflag is only required when setting a non-numeric attribute.For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".The following chart outlines the syntax of setAttr for non-numeric
    data types:In order to run its examples, first execute these commands to
    create the sample attribute types:
    Args:
        alteredValue (bool?): The value is only the current value, which may change in the  
                next evalution (if the attribute has an incoming connection).  
                This flag is only used during file I/O, so that attributes  
                with incoming connections do not have their data overwritten  
                during the first evaluation after a file is opened.  
                Not supported for Ufe attributes.  
                Properties: create
        caching (bool?): Sets the attribute's internal caching on or off. Not all attributes  
                can be defined as caching. Only those attributes that are not defined  
                by default to be cached can be made caching.  As well, multi attribute  
                elements cannot be made caching. Caching also affects child attributes  
                for compound attributes.  
                Not supported for Ufe attributes.  
                Properties: create
        capacityHint (int?): Used to provide a memory allocation hint to attributes  
                where the -size flag cannot provide enough information.  
                This flag is optional and is primarily intended to be  
                used during file I/O.  
                Only certain attributes make use of this flag, and  
                the interpretation of the flag value varies per attribute.  
                Not supported for Ufe attributes.  
                This flag is currently used by (node.attribute):  
              
                mesh.face - hints the total number of elements in the face edge lists  
                Properties: create
        channelBox (bool?): Sets the attribute's display in the channelBox on or off.  
                Keyable attributes are always display in the channelBox regardless of  
                the channelBox settting.  
                Not supported for Ufe attributes. The display of Ufe attributes in  
                the Channel Box is controlled using the channelBox command flag  
                -ual/ufeFixedAttrList.  
                Properties: create
        clamp (bool?): For numeric attributes, if the value is outside the  
                range of the attribute, clamp it to the min or max instead  
                of failing.  
                Not supported for Ufe attributes.  
                Properties: create
        keyable (bool?): Sets the attribute's keyable state on or off.  
                Not supported for Ufe attributes.  
                Properties: create
        lock (bool?): Sets the attribute's lock state on or off.  
                Properties: create
        size (int?): Defines the size of a multi-attribute array. This is only a hint,  
                used to help allocate memory as efficiently as possible.  
                Not supported for Ufe attributes.  
                Properties: create
        type (str?): Identifies the type of data.  If the -type flag  
                is not present, a numeric type is assumed.  
                Not supported for Ufe attributes.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

