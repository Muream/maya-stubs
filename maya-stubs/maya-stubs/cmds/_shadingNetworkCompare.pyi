from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shadingNetworkCompare(*args: str, query: bool = ..., byName: bool = ..., byValue: bool = ..., delete: bool = ..., equivalent: bool = ..., network1: bool = ..., network2: bool = ..., upstreamOnly: bool = ...) -> Union[Union[List[str], str, int], bool]:
    """This command allows you to compare two shading networks.shader, shading, network
    Args:
        byName (bool?): Indicates whether the comparison should consider node names.  
                If true, two shading networks will be considered equivalent only  
                if the names of corresponding nodes are the same, ignoring namespaces.  
                If false, two shading networks will be considered equivalent even  
                if corresponding nodes are named differently.  
                Default is 'false'.  
                Properties: create
        byValue (bool?): Indicates whether the comparison should consider the values of  
                unconnected attributes.  
                If true, two shading networks will be considered equivalent only  
                if corresponding, unconnected attributes are the same type and have the  
                same value. Only attributes of type 'int', 'bool', 'float', and 'string'  
                will have their values compared.  
                If false, two shading networks will be considered equivalent even  
                if corresponding, unconnected attributes have different values or  
                are different types.  
                Default is 'true'.  
                Properties: create
        delete (bool?): Deletes the specified comparison from memory.  
                Properties: create
        equivalent (bool?): Returns an int. 1 if the shading networks in the specified comparison are  
                equivalent. 0 otherwise.  
                Properties: query
        network1 (bool?): Returns a string[]. Returns an empty string array if the shading networks  
                in the specified comparison are not equivalent. Otherwise returns the nodes  
                in the first shading network.  
                Properties: query
        network2 (bool?): Returns a string[]. Returns an empty string array if the shading networks  
                in the specified comparison are not equivalent. Otherwise returns the nodes  
                in the second shading network.  
                Properties: query
        upstreamOnly (bool?): Indicates whether the comparison should consider nodes which are  
                connected downstream from shading network nodes.  
                If true, only those nodes which are upstream from the shading  
                group will be considered. If, following only downstream connections,  
                there is no connection path from a node to one of the shader attributes on the  
                shading group, the node will not be considered.  
                If false, a node will be considered if a connection path can found, following  
                either upstream or downstream connections, which terminates with an input  
                connection to one of the shading groups shader attributes. These dangling nodes  
                do not directly contribute to the color, displacement, or volume  
                characteristics of the shading group.  
                Default is 'false'.  
                Properties: create

    Returns:
        Union[List[str], str, int]: Command result

    Example:
    """

