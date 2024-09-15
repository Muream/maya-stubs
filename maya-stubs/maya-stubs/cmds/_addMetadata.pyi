from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def addMetadata(*args: str, query: bool = ..., channelName: Queryable[str] = ..., channelType: Queryable[str] = ..., indexType: Queryable[str] = ..., scene: bool = ..., streamName: Queryable[str] = ..., structure: Queryable[str] = ...) -> Union[List[str], str, bool]:
    """Defines the attachment of a metadata structure to one or more selected
    objects. This creates a placeholder with an empty metadata Stream for
    later population through thecommand. It's similar
    in concept to thecommand for nodes - a data description
    is added but no data is actually set.When assigning a metadata structure you must specify these flags
    -is the metadata channel type (e.g. "vertex"),is the name of the metadata stream to be created,
    andis the name of the structure type defining the
    contents of the metadata. Theflag is optional.
    If it is not present then the index will be presumed to be a standard
    numerical value.You can query metadata information at a variety of levels. See the
    table below for a full list of the queryable arguments. In each case
    the specification of any of the non-queried arguments filters the list
    of metadata to be examined during the query. For all queries a single
    object must be selected for querying.For example querying theflag with no other
    arguments will return the list of all Channel types on the selected
    object that contain any metadata. Querying theflag
    with theflag specified will return only those
    channel types containing metadata streams that use that particular
    type of index.Flag Combinations:metadata, component, stream, channel, association
    Args:
        channelName (Queryable[str]?): Name of the Channel type to which the structure is to be added (e.g. "vertex").  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        channelType (Queryable[str]?): Obsolete - use the 'channelName' flag instead.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        indexType (Queryable[str]?): Name of the index type the new Channel should be using. If not specified this defaults  
                to a simple numeric index. Of the native types only a mesh "vertexFace" channel is  
                different, using a "pair" index type.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        scene (bool?): Use this flag when you want to add metadata to the scene as a whole rather than to  
                any individual nodes. If you use this flag and have nodes selected the nodes will  
                be ignored and a warning will be displayed.  
                Properties: create, query
        streamName (Queryable[str]?): Name of the empty stream being created. In query mode not specifying a value will  
                return a list of streams on the named channel type.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        structure (Queryable[str]?): Name of the structure which defines the metadata to be attached to the object.  
                In query mode this will return the name of the structure attached at a given  
                stream.  
                			In query mode, this flag can accept a value.  
                Properties: create, query

    Returns:
        List[str]: List of nodes to which a new Stream was successfully added (create mode)
        List[str]: List of channel types containing metadata on an object when querying the channelName flag
        List[str]: List of stream names on an object when querying the streamName flag
        List[str]: List of structures used by an object's metadata Streams when querying the structure flag
        List[str]: List of index types used by an object when querying the indexType flag

    Example:
    """

