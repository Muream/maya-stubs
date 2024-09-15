from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def listConnections(*args: str, connections: bool = ..., destination: bool = ..., exactType: bool = ..., fullNodeName: bool = ..., plugs: bool = ..., shapes: bool = ..., skipConversionNodes: bool = ..., source: bool = ..., type: str = ...) -> List[str]:
    """This command returns a list of all attributes/objects of
    a specified type that are connected to the given object(s).
    If no objects are specified then the command lists the connections
    on selected nodes.connection, dg, dependency, graph, plug, connect
    Args:
        connections (bool?): If true, return both attributes involved in the connection. The one  
                on the specified object is given first.  Default false.  
                Properties: create
        destination (bool?): Give the attributes/objects that are on the "destination" side of  
                connection to the given object.  Default true.  
                Properties: create
        exactType (bool?): When set to true, -t/type only considers node of this exact  
                type. Otherwise, derived types are also taken into account.  
                Properties: create
        fullNodeName (bool?): Return full node name in result.  
                Properties: create
        plugs (bool?): If true, return the connected attribute names; if false, return the  
                connected object names only.  Default false;  
                Properties: create
        shapes (bool?): Actually return the shape name instead of the transform when the  
                shape is "selected".  Default false.  
                Properties: create
        skipConversionNodes (bool?): If true, skip over unit conversion nodes and return the  
                node connected to the conversion node on the other side.  Default false.  
                Properties: create
        source (bool?): Give the attributes/objects that are on the "source" side of  
                connection to the given object.  Default true.  
                Properties: create
        type (str?): If specified, only take objects of a specified type.  
                Properties: create

    Returns:
        List[str]: List of connection plugs/nodes

    Example:
    """

