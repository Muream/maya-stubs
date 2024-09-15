from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listAttr(*args: str, array: bool = ..., attributeType: Multiuse[str] = ..., caching: bool = ..., category: Multiuse[str] = ..., changedSinceFileOpen: bool = ..., channelBox: bool = ..., connectable: bool = ..., extension: bool = ..., fromPlugin: bool = ..., fullNodeName: bool = ..., hasData: bool = ..., hasNullData: bool = ..., inUse: bool = ..., keyable: bool = ..., leaf: bool = ..., locked: bool = ..., multi: bool = ..., nodeName: bool = ..., output: bool = ..., ramp: bool = ..., read: bool = ..., readOnly: bool = ..., scalar: bool = ..., scalarAndArray: bool = ..., settable: bool = ..., shortNames: bool = ..., string: Multiuse[str] = ..., unlocked: bool = ..., usedAsFilename: bool = ..., userDefined: bool = ..., visible: bool = ..., write: bool = ...) -> List[str]:
    """This command lists the attributes of a node.  If no flags are specified
    all attributes are listed.
    Args:
        array (bool?): only list array (not multi) attributes  
                Properties: create
        attributeType (Multiuse[str]?): Return attributes of a particular type.  
                Properties: create, multiuse
        caching (bool?): only show attributes that are cached internally  
                Properties: create
        category (Multiuse[str]?): only show attributes belonging to the given category.  
                Category string can be a regular expression.  
                Properties: create, multiuse
        changedSinceFileOpen (bool?): Only list the attributes that have been changed  
                since the file they came from was opened. Typically useful  
                only for objects/attributes coming from referenced files.  
                Properties: create
        channelBox (bool?): only show non-keyable attributes that appear in the channelbox  
                Properties: create
        connectable (bool?): only show connectable attributes  
                Properties: create
        extension (bool?): list user-defined attributes for all nodes of this type (extension attributes)  
                Properties: create
        fromPlugin (bool?): only show attributes that were created by a plugin  
                Properties: create
        fullNodeName (bool?): Return full node name in result.  
                Properties: create
        hasData (bool?): list only attributes that have data (all attributes  
                except for message attributes)  
                Properties: create
        hasNullData (bool?): list only attributes that have null data.  
                This will list all attributes that have  
                data (see hasData flag) but the data value  
                is uninitialized.  
                A common example where an attribute may have null  
                data is when a string attribute is  
                created but not yet assigned an initial value.  
                Similarly array attribute data is often null until  
                it is initialized.  
                Properties: create
        inUse (bool?): only show attributes that are currently marked as in use. This flag indicates  
                that an attribute affects the scene data in some way. For example it has a  
                non-default value or it is connected to another attribute.  This is the  
                general concept though the precise implementation is subject to change.  
                Properties: create
        keyable (bool?): only show attributes that can be keyframed  
                Properties: create
        leaf (bool?): Only list the leaf-level name of the attribute.  
                controlPoints[44].xValue would be listed as "xValue".  
                Properties: create
        locked (bool?): list only attributes which are locked  
                Properties: create
        multi (bool?): list each currently existing element of a multi-attribute  
                Properties: create
        nodeName (bool?): Return node name in result.  
                Properties: create
        output (bool?): List only the attributes which are numeric or which  
                are compounds of numeric attributes.  
                Properties: create
        ramp (bool?): list only attributes which are ramps  
                Properties: create
        read (bool?): list only attributes which are readable  
                Properties: create
        readOnly (bool?): List only the attributes which are readable and not  
                writable.  
                Properties: create
        scalar (bool?): only list scalar numerical attributes  
                Properties: create
        scalarAndArray (bool?): only list scalar and array attributes  
                Properties: create
        settable (bool?): list attribute which are settable  
                Properties: create
        shortNames (bool?): list short attribute names (default is to list long names)  
                Properties: create
        string (Multiuse[str]?): List only the attributes that match the other  
                criteria AND match the string(s) passed from this flag.  
                String can be a regular expression.  
                Properties: create, multiuse
        unlocked (bool?): list only attributes which are unlocked  
                Properties: create
        usedAsFilename (bool?): list only attributes which are designated to be treated as filenames  
                Properties: create
        userDefined (bool?): list user-defined (dynamic) attributes  
                Properties: create
        visible (bool?): only show visible or non-hidden attributes  
                Properties: create
        write (bool?): list only attributes which are writable  
                Properties: create

    Returns:
        List[str]: : List of attributes matching criteria

    Example:
    """

