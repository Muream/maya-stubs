from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def makePaintable(arg0: str = ..., arg1: str = ..., /, *, query: bool = ..., activate: bool = ..., activateAll: bool = ..., altAttribute: Queryable[Multiuse[str]] = ..., attrType: Queryable[str] = ..., clearAll: bool = ..., remove: bool = ..., shapeMode: Queryable[str] = ..., uiName: Queryable[str] = ...) -> Union[bool, Multiuse[str], str]:
    """Make attributes of nodes paintable to Attribute Paint Tool.
    This command is used to register new attributes to the
    Attribute Paint tool as paintable. Once registered the
    attributes will be recognized by the Attribute Paint tool
    and the user will be able to paint them.attributes, paint
    Args:
        activate (bool?): Activate / deactivate the given paintable attribute. Used  
                to filter out some nodes in the attribute paint tool.  
                Properties: create, query
        activateAll (bool?): Activate / deactivate all the registered paintable attributes. Used  
                to filter out some nodes in the attribute paint tool.  
                Properties: create, query
        altAttribute (Queryable[Multiuse[str]]?): Define an alternate attribute which will also receive the same  
                values. There can be multiple such flags.  
                Properties: create, query, multiuse
        attrType (Queryable[str]?): Paintable attribute type.  
                   Supported types: intArray, doubleArray, vectorArray, multiInteger, multiFloat, multiDouble, multiVector.  
                Properties: create, query
        clearAll (bool?): Removes all paintable attribute definitions.  
                Properties: create, query
        remove (bool?): Make the attribute not paintable any more.  
                Properties: create, query
        shapeMode (Queryable[str]?): This flag controls how Artisan correlates the paintable node to a  
                corresponding shape node.  It is used for attributes of type multi  
                of multi, where the first multi dimension corresponds to the shape  
                index (i.e. cluster nodes). At present, only one value of this flag  
                is supported: "deformer". By default this flag is an empty string,  
                which means that there is a direct indexing (no special mapping  
                required) of the attribute with respect to vertices on the shape.  
                Properties: create, query
        uiName (Queryable[str]?): UI name. Default is the attribute name.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

