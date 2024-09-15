from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def componentTag(*args: str, create: bool = ..., delete: bool = ..., injectionLocation: str = ..., modify: str = ..., newTagName: str = ..., queryEdit: bool = ..., rename: bool = ..., tagName: Multiuse[str] = ..., uniqueTagName: bool = ...) -> Any:
    """This command allows you to create, delete and modify component tags
    Args:
        create (bool?): This creates a componentTag on the geometry. The name can be specified with the  
                -newTagName option. If no new name is specified one will be generated.  
                The name of the created tag is returned  
                Properties: create
        delete (bool?): This deletes the componentTags specified with the -tagName option.  
                Properties: create
        injectionLocation (str?): The name of the injection node at which the componentTag will be edited.  
                This is only necessary in the rare case where a particular componentTag  
                can be altered at multiple injection locations.  
                Properties: create
        modify (str?): This modifies the componentTag specified with the -tagName option.  
                The mode determines whether components are, replaced, cleared, added or removed.  
                Properties: create
        newTagName (str?): The name of the new componentTag to be created or the new name  
                of the componentTag that is being renamed.  
                Properties: create
        queryEdit (bool?): This returns what edits are allowed with the given parameters. When the command  
                is issued in Python a dictionary object containing what is allowed is returned.  
                Properties: create
        rename (bool?): This renames the componentTag specified with the -tagName option to the  
                name specified with the -newTagName option  
                Properties: create
        tagName (Multiuse[str]?): The name(s) of the componentTags to be edited. This can be a single name or  
                a list of names. The names can contain wildcard like '*' to match multiple  
                existing componentTags.  
                Properties: create, multiuse
        uniqueTagName (bool?): This flag is used along the create and newTagName flags. It makes  
                the command generate a unique tag name if the name provided by newTagName  
                is already used by a tag on the injectionNode or its parents.  
                Properties: create

    Returns:
        Any: The name of the created componentTag, or whether the command succeeded or the information
            about what can be edited

    Example:
    """

