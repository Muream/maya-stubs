from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nodePreset(*, attributes: str = ..., custom: str = ..., delete: Tuple[str, str] = ..., exists: Tuple[str, str] = ..., isValidName: str = ..., list: str = ..., load: Tuple[str, str] = ..., save: Tuple[str, str] = ...) -> bool:
    """Command to save and load preset settings for a node.
    This command allows you to take a snapshot of the values of all attributes of a
    node and save it to disk as a preset with user specified name. Later the saved
    preset can be loaded and applied onto a different node of the same type. The
    end result is that the node to which the preset is applied takes on the same
    values as the node from which the preset was generated had at the time of the
    snapshot.preset, render, globals
    Args:
        attributes (str?): A white space separated string of the named attributes to save to the  
                preset file. If not specified, all attributes will be stored.  
                Properties: create
        custom (str?): Specifies a MEL script for custom handling of node attributes that are not  
                handled by the general save preset mechanism (ie. multis, dynamic attributes,  
                or connections). The identifiers #presetName and #nodeName will be expanded  
                before the script is run. The script must return an array of strings which  
                will be saved to the preset file and issued as commands when the preset is  
                applied to another node.  
                The custom script can query #nodeName in determining what should be saved  
                to the preset, or issue commands to query the selected node in deciding how  
                the preset should be applied.  
                Properties: create
        delete (Tuple[str, str]?): Deletes the existing preset for the node specified by the first argument with  
                the name specified by the second argument.  
                Properties: create
        exists (Tuple[str, str]?): Returns true if the node specified by the first argument already has a preset  
                with a name specified by the second argument. This flag can be used to check if  
                the user is about to overwrite an existing preset and thereby provide the user  
                with an opportunity to choose a different name.  
                Properties: create
        isValidName (str?): Returns true if the name consists entirely of valid characters for  
                a preset name. Returns false if not. Because the preset name will  
                become part of a file name and part of a MEL procedure name, some  
                characters must be disallowed. Only alphanumeric characters and underscore  
                are valid characters for the preset name.  
                Properties: create
        list (str?): Lists the names of all presets which can be loaded onto the specified  
                node.  
                Properties: create
        load (Tuple[str, str]?): Sets the settings of the node specified by the first argument according to the  
                preset specified by the second argument. Any attributes on the node which are  
                the destinations of connections or whose children (multi children or compound  
                children) are destinations of connections will not be changed by the preset.  
                Properties: create
        save (Tuple[str, str]?): Saves the current settings of the node specified by the first argument to a  
                preset of the name specified by the second argument. If a preset for that node  
                with that name already exists, it will be overwritten with no warning. You can  
                use the -exists flag to check if the preset already exists. If an attribute of  
                the node is the destination of a connection, the value of the attribute will  
                not be written as part of the preset.  
                Properties: create

    Returns:
        bool: if isValidName or exists is used.

    Example:
    """

