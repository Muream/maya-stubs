from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getAttr(*args: str, asString: bool = ..., caching: bool = ..., channelBox: bool = ..., expandEnvironmentVariables: bool = ..., keyable: bool = ..., lock: bool = ..., multiIndices: bool = ..., settable: bool = ..., silent: bool = ..., size: bool = ..., time: int = ..., type: bool = ...) -> Any:
    """This command returns the value of the named object's attribute.For Ufe attributes, the input attribute string should be
    "<ufe_path_string>.<ufe_attribute_name>".UI units are used where applicable.Currently, the types of attributes that can be displayed are:Other data types cannot be retrieved. No result is returned if the
    attribute contains no data.
    Args:
        asString (bool?): This flag is only valid for enum attributes. It allows you to  
                get the attribute values as strings instead of integer values.  
                Note that the returned string value is dependent on the  
                UI language Maya is running in (about -uiLanguage).  
                Not supported for Ufe attributes.  
                Properties: create
        caching (bool?): Returns whether the attribute is set to be cached internally  
                Not supported for Ufe attributes.  
                Properties: create
        channelBox (bool?): Returns whether the attribute is set to show in the Channel Box.  
                Keyable attributes also show in the Channel Box.  
                Not supported for Ufe attributes. The display of Ufe attributes in  
                the Channel Box is controlled using the channelBox command flag  
                -ual/ufeFixedAttrList.  
                Properties: create
        expandEnvironmentVariables (bool?): Expand any environment variable and (tilde characters on UNIX)  
                found in string attributes which are returned.  
                Not supported for Ufe attributes.  
                Properties: create
        keyable (bool?): Returns the keyable state of the attribute.  
                Not supported for Ufe attributes.  
                Properties: create
        lock (bool?): Returns the lock state of the attribute.  
                Properties: create
        multiIndices (bool?): If the attribute is a multi, this will return a list containing  
                all of the valid indices for the attribute.  
                Not supported for Ufe attributes.  
                Properties: create
        settable (bool?): Returns 1 if this attribute is currently settable by setAttr,  
                0 otherwise. An attribute is settable if it's not locked  
                and either not connected, or has only keyframed animation.  
                For Ufe attributes an attribute is settable if it's not locked.  
                Properties: create
        silent (bool?): When evaluating an attribute that is not a numeric or string  
                value, suppress the error message saying that the data cannot be  
                displayed. The attribute will be evaluated even though its data  
                cannot be displayed. This flag does not suppress all error messages,  
                only those that are benign.  
                Not supported for Ufe attributes.  
                Properties: create
        size (bool?): Returns the size of a multi-attribute array.  Returns 1 if non-multi.  
                Not supported for Ufe attributes.  
                Properties: create
        time (int?): Evaluate the attribute at the given time instead of the current time.  
                Not supported for Ufe attributes.  
                Properties: create
        type (bool?): Returns the type of data currently in the attribute.  
              
                Attributes of simple types such as strings and numerics always contain  
                data, but attributes of complex types (arrays, meshes, etc) may contain no data  
                if none has ever been assigned to them. When this happens the command will  
                return with no result: not an empty string, but no result at all.  
                Attempting to directly compare this non-result to another value or use it  
                in an expression will result in an error, but you can assign it to a  
                variable in which case the variable will be set to the default value for  
                its type (e.g. an empty string for a string variable, zero for an integer  
                variable, an empty array for an array variable). So to be safe when using this  
                flag, always assign its result to a string variable, never try to use it  
                directly.  
                Properties: create

    Returns:
        Any: Value or state of the attribute. The number and type
            of values returned is dependent on the attribute type.

    Example:
    """

