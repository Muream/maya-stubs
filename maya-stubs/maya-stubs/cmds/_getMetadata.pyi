from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def getMetadata(*args: str, dataType: bool = ..., listChannelNames: bool = ..., listMemberNames: bool = ..., listStreamNames: bool = ..., memberName: str = ..., channelName: Queryable[str] = ..., channelType: Queryable[str] = ..., endIndex: str = ..., index: Queryable[Multiuse[str]] = ..., indexType: Queryable[str] = ..., scene: bool = ..., startIndex: str = ..., streamName: Queryable[str] = ...) -> Union[List[int], List[float], List[str], str, Multiuse[str], bool]:
    """This command is used to retrieve the values of metadata elements from a node or scene.
    It is restricted to returning a single structure member at a time. For convenience
    the detail required is only enough to find a single Member of a single Structure
    on a single metadata Channel.In the simplest case if there is a single Stream on one metadata Channel
    which uses a Structure with only one Member then all that is required is the
    name of the object containing the metadata. In the most complex case the
    'channelName', 'streamName', and 'memberName' are all required to narrow down
    the metadata to a single unique Member.In general for scripting it's a good idea to use all flags anyway since there
    could be metadata added anywhere. The shortcuts are mainly for quick entry when
    entering commands directly in the script editor or command line.When an Index is specified where data is not present the command fails with a
    message telling you which Index or Indices didn't have values. Use thecommand first to determine where metadata exists if you
    need to know in advance where to find valid metadata.Metadata on meshes is special in that the Channel types "vertex",
    "edge", "face", and "vertexFace" are directly connected to the
    components of the same name. To make getting these metadata
    Channels easier you can simply select or specify on the command
    line the corresponding components rather than using theandflags. For
    example the selection "myMesh.vtx[8:10]" corresponds toand eitheras a multi-use flag orOnly a single node or scene and unique metadata Structure Member are
    allowed in a single command. This keeps the data simple at the possible
    cost of requiring multiple calls to the command to get more than one
    Structure Member's value.When the data is returned it will be in Index order with an entire Member
    appearing together. For example if you were retrieving float[3] metadata on
    three components you would get the nine values back in the order:
    index[0]-float[0], index[0]-float[1], index[0]-float[2],
    index[1]-float[0], index[1]-float[1], index[1]-float[2],
    index[2]-float[0], index[2]-float[1], index[2]-float[2]. In the Python
    implementation the float[3] values will be an array each so you would
    get back three float[3] arrays.metadata, component, stream, channel, association
    Args:
        dataType (bool?): Used with the flag 'streamName' and 'memberName' to query the dataType  
                of the specfied member.  
                Properties: create
        listChannelNames (bool?): Query the channel names on the shape.  
                This flag can be used with some flags to filter the results.  
                It can be used with the flag 'streamName' to get the channel  
                with the specfied stream and the flag 'memberName' to get the channel  
                in which the stream contains the specified member.  
                It cannot be used with the flag 'channelName'.  
                Properties: create
        listMemberNames (bool?): Query the member names on the shape.  
                This flag can be used with some flags to filter the results. It can be used with  
                'streamName' to get the member which is in the specified stream and the flag  
                'channelName' to get the member which is used in the specfied channel.  
                It cannot be used with the flag 'memberName'.  
                Properties: create
        listStreamNames (bool?): Query the stream names on the shape.  
                This flag can be used with some flags to filter the results. It can be  
                used with the flag 'channelName' to get the stream names on the specified channel  
                and the flag 'memberName' to get the stream names which has the specified member.  
                It cannot be used with the flag 'streamName'.  
                Properties: create
        memberName (str?): Name of the Structure member being retrieved. The names of the members are  
                set up in the Structure definition, either through the description passed  
                in through the "dataStructure" command or via the API used to create that  
                Structure. This flag is only necessary when selected Structures have more  
                than one member.  
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
        List[int]: List of integer values from the metadata member
        List[float]: List of real values from the metadata member
        List[str]: List of string values from the metadata member

    Example:
    """

