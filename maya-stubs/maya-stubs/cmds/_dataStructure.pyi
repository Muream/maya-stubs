from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dataStructure(*, query: bool = ..., asFile: Queryable[str] = ..., asString: Queryable[str] = ..., dataType: bool = ..., format: Queryable[str] = ..., listMemberNames: Queryable[str] = ..., name: Queryable[str] = ..., remove: bool = ..., removeAll: bool = ...) -> Union[str, List[str], bool]:
    """Takes in a description of the structure and creates it, adding it to
    the list of available data structures. The structure definition can
    either be supplied in theflag or exist in a file that is
    referenced by theflag.If theflag is specified with aflag then the data
    structure will be removed. This is to keep all structure operations
    in a single command rather than create separate commands to create,
    remove, and query the data structures. When you use theflag then every existing metadata structure is removed. Use with care!
    Note that removed structures may still be in use in metadata Streams after
    removal, they are just no longer available for the creation of new Streams.Both the creation modes and the remove mode are undoable.Creation of an exact duplicate of an existing structure (including name)
    will succeed silently without actually creating a new structure.
    Attempting to create a new non-duplicate structure with the same name
    as an existing structure will fail as there is no way to disambiguate
    two structures with the same name.Querying modes are defined to show information both on the created
    structures and the structure serialization formats that have been
    registered. The serialization formats preserve the structure
    information as text (e.g. raw, XML, JSON). Since thestructure
    type is built in it will be assumed when none are specified.General query with no flags will return the list of names of all
    currently existing structures.Querying theflag will return the list of all registered structure
    serialization formats.Querying with thesupplied before theflag will
    show the detailed description of that particular structure
    serialization format.Querying theflag with a structure name and serialization
    format supplied before theflag will return a string
    representing the named data structure in the serialization format
    specified by theflag. Even if the format is the same as
    the one that created the structure the query return string may not
    be identical since the queried value is formatted in a standard
    way - original formatting is not preserved.Querying theflag with a structure name supplied before theflag will return the original file from which the structure
    was generated. If the structure was created using theflag or through the API then an empty string will be returned.Querying theflag returns the list of all structures created
    so far.metadata, component
    Args:
        asFile (Queryable[str]?): Specify a file that contains the serialized data which describes the  
                structure.  The format of the data is specified by the 'format' flag.  
                Properties: create, query
        asString (Queryable[str]?): Specify the string containing the serialized data which describes the  
                structure. The format of the data is specified by the 'format' flag.  
                Properties: create, query
        dataType (bool?): Used with the flag 'listMemberNames' to query the type of the member.  
                The type is appended after each relative member in the array.  
                For example, if the format is "name=idStructure:int32=id:string=name"  
                the returned array is "id int32 name string".  
                Properties: create, query
        format (Queryable[str]?): Format of data to expect in the structure description. "raw" is supported  
                natively and will be assumed if the format type is omitted. Others are  
                available via plug-in. You can query the available formats by using this  
                flag in query mode.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        listMemberNames (Queryable[str]?): Query the member names in the dataStructure. The member names will be  
                returned in an array. The name of the data structure will not be returned.  
                To get the type of each member, use 'dataType' together. Then the type of  
                the member will be appended in the array after their relative member.  
                For example, if the format is "name=idStructure:int32=id:string=name"  
                the returned array is "id int32 name string".  
                Properties: create, query
        name (Queryable[str]?): Query mode only.  Name of the data structure to be queried, or set to  
                list the available names.  
                			In query mode, this flag can accept a value.  
                Properties: query
        remove (bool?): Remove the named data structure. It's an error if it doesn't exist.  
                Properties: create
        removeAll (bool?): Remove all metadata structures. This flag can not be used in conjunction with  
                any other flags.  
                Properties: create

    Returns:
        str: Name of the resulting structure, should match the name defined in the structure description
        List[str]: Name(s) of the removed structures.

    Example:
    """

