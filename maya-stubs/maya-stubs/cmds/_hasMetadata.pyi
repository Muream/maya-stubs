from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hasMetadata(*args: str, asList: bool = ..., ignoreDefault: bool = ..., memberName: str = ..., channelName: Queryable[str] = ..., channelType: Queryable[str] = ..., endIndex: str = ..., index: Queryable[Multiuse[str]] = ..., indexType: Queryable[str] = ..., scene: bool = ..., startIndex: str = ..., streamName: Queryable[str] = ...) -> Union[List[str], List[bool], str, Multiuse[str], bool]:
    """This command is used to query for the presence of metadata elements on a node,
    components, or scene. The command works at all levels of metadata presence, from
    the existence of any metadata at all on a node or scene right down to the presence
    of metadata values set on a particular metadata Stream index.metadata, component, stream, channel, association
    Args:
        asList (bool?): Use this flag when you want to return string values indicating where the  
                metadata lives rather than boolean values. See the command description  
                for more details on what this flag will return.  
                Properties: create
        ignoreDefault (bool?): Use this flag when you want to skip over any metadata that has only  
                default values. i.e. the metadata may exist but it hasn't had a new  
                value set yet (non-zero for numerics, non-empty strings, etc.)  
                See the command description for more details on how this flag filters  
                the search.  
                Properties: create
        memberName (str?): Name of the Structure member being checked. The names of the members are  
                set up in the Structure definition, either through the description passed  
                in through the "dataStructure" command or via the API used to create that  
                Structure. As the assignment of metadata is on a per-structure basis this  
                flag only needs to be specified when querying for non-default values. If  
                you query for non-default values and omit this flag then it checks that  
                any of the members have a non-default value.  
                Properties: create
        channelName (Queryable[str]?): Filter the metadata selection to only recognize metadata belonging to  
                the specified named Channel (e.g. "vertex"). This flag is ignored if the  
                components on the selection list are being used to specify the metadata  
                of interest.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        channelType (Queryable[str]?): Obsolete - use the 'channelName' flag instead.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        endIndex (str?): The metadata is stored in a Stream, which is an indexed list. If you have  
                mesh components selected then the metadata indices are implicit in the list  
                of selected components. If you select only the node or scene then this flag  
                may be used in conjunction with the startIndex flag to specify a range  
                of indices from which to retrieve the metadata. It is an error to have the  
                value of startIndex be greater than that of endIndex.  
              
              
                See also the index flag for an alternate way to specify multiple  
                indices. This flag can only be used on index types that support a range  
                (e.g. integer values - it makes no sense to request a range between two  
                strings)  
              
                			In query mode, this flag can accept a value.  
                Properties: create
        index (Queryable[Multiuse[str]]?): In the typical case metadata is indexed using a simple integer value.  
                Certain types of data may use other index types. e.g. a "vertexFace"  
                component will use a "pair" index type, which is two integer values; one  
                for the face ID of the component and the second for the vertex ID.  
              
              
                The index flag takes a string, formatted in the way the  
                specified indexType requires. All uses of the  
                index flag have the same indexType. If the type was  
                not specified it is assumed to be a simple integer value.  
              
                			In query mode, this flag can accept a value.  
                Properties: create, query, multiuse
        indexType (Queryable[str]?): Name of the index type the new Channel should be using. If not specified this  
                defaults to a simple integer index. Of the native types only a mesh  
                "vertexFace" channel is different, using a "pair" index type.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        scene (bool?): Use this flag when you want to add metadata to the scene as a whole rather than to  
                any individual nodes. If you use this flag and have nodes selected the nodes will  
                be ignored and a warning will be displayed.  
                Properties: create, query
        startIndex (str?): The metadata is stored in a Stream, which is an indexed list. If you have  
                mesh components selected then the metadata indices are implicit in the list  
                of selected components. If you select only the node or scene then this flag  
                may be used in conjunction with the endIndex flag to specify a range of  
                indices from which to retrieve the metadata. It is an error to have the value  
                of startIndex be greater than that of endIndex.  
              
              
                See also the index flag for an alternate way to specify multiple  
                indices. This flag can only be used on index types that support a range  
                (e.g. integer values - it makes no sense to request a range between two  
                strings)  
              
                			In query mode, this flag can accept a value.  
                Properties: create
        streamName (Queryable[str]?): Name of the metadata Stream. Depending on context it could be the name of a  
                Stream to be created, or the name of the Stream to pass through the filter.  
                			In query mode, this flag can accept a value.  
                Properties: create, query

    Returns:
        List[str]: List of indexes in the filtered list which contain metadata
        List[bool]: List of answers to whether the specified item(s) have metadata

    Example:
    """

