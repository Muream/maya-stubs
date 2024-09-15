from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def characterMap(*args: str, edit: bool = ..., query: bool = ..., mapAttr: Queryable[Tuple[str, str]] = ..., mapMethod: str = ..., mapNode: Queryable[Tuple[str, str]] = ..., mapping: Queryable[str] = ..., proposedMapping: bool = ..., unmapAttr: Tuple[str, str] = ..., unmapNode: Tuple[str, str] = ...) -> Union[str, Tuple[str, str], bool]:
    """This command is used to create a correlation between the attributes of 2 or more characters.character, clip, animation
    Args:
        mapAttr (Queryable[Tuple[str, str]]?): In query mode, this flag can be used to query the mapping stored by the specified map node. It returns an array of strings.  
                In non-query mode, this flag can be used to create a mapping between the specified character members. Any previous mapping on the attributes is removed in favor of the newly specified mapping.  
                Properties: create, query, edit
        mapMethod (str?): This is is valid in create mode only. It specifies how the mapping should be done. Valid options are: "byNodeName", "byAttrName", and "byAttrOrder". "byAttrOrder" is the default. The flags mean the following: "byAttrOrder" maps using the order that the character stores the attributes internally, "byAttrName" uses the attribute name to find a correspondence, "byNodeName" uses the node name *and* the attribute name to find a correspondence.  
                Properties: create
        mapNode (Queryable[Tuple[str, str]]?): This flag can be used to map all the attributes on the source node to their matching attributes on the destination node.  
                Properties: create, query
        mapping (Queryable[str]?): This flag is valid in query mode only. It must be used before the query flag with a string argument. It is used for querying the mapping for a particular attribute.  A string array is returned.  
                Properties: query
        proposedMapping (bool?): This flag is valid in query mode only. It is used to get an array of the mapping that the character map would prvide if called with the specified characters and the (optional) specified mappingMethod. If a character map exists on the characters, the map is not affected by the query operation.  A string array is returned.  
                Properties: query
        unmapAttr (Tuple[str, str]?): This flag can be used to unmap the mapping stored by the specified map node.  
                Properties: create, edit
        unmapNode (Tuple[str, str]?): This flag can be used to unmap all the attributes on the source node to their matching attributes on the destination node. Note that mapped attributes which do not have matching names, will not be unmapped.  
                Properties: create

    Returns:
        str: characterMap name

    Example:
    """

