from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def applyMetadata(arg0: str = ..., /, *, format: str = ..., scene: bool = ..., value: str = ...) -> bool:
    """Define the values of a particular set of metadata on selected objects.
    This command is used in preservation of metadata through Maya file formats
    (.ma/.mb). If any metadata already exists it will be kept and merged with
    the new metadata, overwriting duplicate entries. (i.e. if this command
    specifies data at index N and you already have a value at index N then
    the one this command specifies will be the new value and the old one
    will cease to exist.)Unlike thecommand it is not necessary to first use
    thecommand or API equivalent to attach a metadata
    stream to the object, this command will do both assignment of structure
    and of metadata values. You do have to use thecommand or API equivalent to create the structure being assigned first
    though.The formatted input will be in a form expected by the data
    associations serializer (see adsk::Data::AssociationsSerializer for
    more information). The specific serialization type will be the default
    'raw' if theflag is not used.For example the "raw" format input string
    "channel face\\n[STREAMDATA]\\nendChannels\\nendAssociations"
    with no flags is equivalent to the input "[STREAMDATA]\\nendChannels" with
    theflag set to 'face'metadata, component, stream, channel, association
    Args:
        format (str?): Name of the data association format type to use in the value flag parsing.  
                Default value is "raw".  
                Properties: create
        scene (bool?): Use this flag when you want to apply metadata to the scene as a whole  
                rather than to any individual nodes. If you use this flag and have  
                nodes selected the nodes will be ignored and a warning will be displayed.  
                Scene metadata is incompatible with referenced scenes. Node associated  
                metadata from referenced files will still be readable from master scenes  
                but scene specific metadata of referenced files will not be accessible  
                from a any master scene. This will ensure that referenced files metadata  
                will not end up corrupting the master file scene-metadata.  
                Properties: create
        value (str?): String containing all of the metadata to be assigned to the selected  
                object.  
                Properties: create

    Returns:
        bool: True if the application succeeded

    Example:
    """

