from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def editMetadata(*args: str, memberName: str = ..., remove: bool = ..., stringValue: Multiuse[str] = ..., value: Multiuse[float] = ..., channelName: Queryable[str] = ..., channelType: Queryable[str] = ..., endIndex: str = ..., index: Queryable[Multiuse[str]] = ..., indexType: Queryable[str] = ..., scene: bool = ..., startIndex: str = ..., streamName: Queryable[str] = ...) -> Union[str, Multiuse[str], bool]:
    """This command is used to set metadata elements onto or remove metadata
    elements from an object. Before using this command you must first attach
    a metadata stream type to the object using thecommand
    or an API equivalent. The command has four basic variations:The difference between theandvariations
    (1,3 vs. 2,4) is thatrequires both a member name to be set
    and a new value to be set. (The reason removal doesn't use a member
    name is that you can only remove an entire metadata structural element,
    you cannot remove only a single member from it.)When metadata values are set or removed the action is performed on
    every selected component or index. This provides an easy method to
    set or remove a bunch of metadata en masse.The general usage (variations 3, 4) lets you select specific pieces
    of metadata through theandflags. Note that sinceis a multi-use flag you
    can select many different elements from the same Channel and set or
    remove the metadata on all of them in one command.Metadata on meshes is special in that the Channel types "vertex",
    "edge", "face", and "vertexFace" are directly connected to the
    components of the same name. To make setting these metadata
    Channels easier you can simply select or specify on the command
    line the corresponding components rather than using theandflags. For example the selection "myMesh.vtx[8:10]"
    corresponds toand(as a multi-use flag).Note that the metadata is assigned to an object and except in the special
    case of mesh geometry does not flow through the dependency graph. In
    meshes the metadata will move from node to node wherever the geometry
    is connected, although it will not adjust itself automatically for changes
    in topology. Internal data is arranged to minimize the amount of copying
    no matter how many other nodes are connected to it.Only a single node or scene, component type, channel type, and value type
    are allowed in a single command. This keeps the data simple at the possible
    cost of requiring multiple calls to the command to set more than one
    structure member's value.Certain nodes have metadata supplied by input attributes. If you edit one
    of those with an incoming connection on such an attribute then the metadata
    edit will not be applied directly it will be put into an 'editMetadata' node
    for application during DG evaluation. Since the details of the metadata are
    not known until the evaluation happens less rigorous compatibility checking
    is performed. The editMetadata node has its own facilities for verifying and
    reporting illegal metadata edits. Successive edits to the same metadata in
    this way appends each edit to the same editMetadata node.metadata, component, stream, channel, association
    Args:
        memberName (str?): Name of the Structure member being edited. The names of the members are  
                set up in the Structure definition, either through the description passed  
                in through the "dataStructure" command or via the API used to create that  
                Structure.  
                Properties: create
        remove (bool?): If the remove flag is set then the metadata will be removed rather  
                than have values set. In this mode the "memberName", "value", and  
                "stringValue" flags are ignored. "memberName" is ignored because when  
                deleting metadata all members of a structure must be removed as a group.  
                The others are ignored since when deleting you don't need a value to be set.  
                Properties: create
        stringValue (Multiuse[str]?): String value to be set into the specified metadata locations. This flag  
                can only be used when the data member is a numeric type. If the member has  
                N dimensions (e.g. string[2]) then this flag must appear N times (e.g. 2 times)  
                The same values are applied to the specified metadata member on all affected  
                components or metadata indices.  
                Only one of the value, and stringValue flags can be specified at once and the  
                type must match the type of the structure member named by the "member" flag.  
                Properties: create, multiuse
        value (Multiuse[float]?): Numeric value to be set into the specified metadata locations. This flag  
                can only be used when the data member is a numeric type. If the member has  
                N dimensions (e.g. float[3]) then this flag must appear N times (e.g. 3 times)  
                The same values are applied to the specified metadata member on all affected  
                components or metadata indices. All numeric member types should use this type  
                of value specification, i.e. everything except string and matrix types.  
                Only one of the value, and stringValue flags can be specified at once and the  
                type must match the type of the structure member named by the "member" flag.  
                Properties: create, multiuse
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
        str: Name of the node where the new edits reside, empty string if edits failed. It will be an editMetadata node if construction history was present.

    Example:
    """

