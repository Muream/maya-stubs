from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dirmap(arg0: str = ..., /, *, query: bool = ..., convertDirectory: str = ..., enable: bool = ..., getAllMappings: bool = ..., getMappedDirectory: str = ..., mapDirectory: Tuple[str, str] = ..., unmapDirectory: str = ...) -> Union[str, None, bool]:
    """Use this command to map a directory to another directory. The first
    argument is the directory to map, and the second is the destination
    directory to map to.Directories
    must both be absolute paths, and should be separated with forward
    slashes ('/'). The mapping is case-sensitive on all platforms.
    This command can be useful when moving projects to
    another machine where some textures may not be contained in the Maya
    project, or when a texture archive moves to a new location. This
    command is not necessary when moving a (self-contained) project from
    one machine to another - instead copy the entire project over and set
    the Maya project to the new location.For one-time directory moves, if the command is enabled and the mapping
    configured correctly, when a scene is opened and saved the mapped
    locations will be reflected in the filenames saved with the file.
    To set up a permanent mapping the command should
    be enabled and the mappings set up in a script which is executed every
    time you launch Maya (userSetup.mel is sourced on startup).
    The directory mappings and enabled state are not preserved between
    Maya sessions.
    This command requires one "main" flag that specifies the action to take.
    Flags are:
    Args:
        convertDirectory (str?): Convert a file or directory.  
                Returns the name of the mapped file or directory, if the command is  
                enabled. If the given string  
                contains one of the mapped directories, the return value will have that  
                substring replaced with the mapped one. Otherwise the given argument  
                string will be returned. If the command is disabled the given argument  
                is always returned. Checks are not  
                made for whether the file or directory exists. If the given string  
                is a directory it should have a trailing '/'.  
                Properties: create
        enable (bool?): Enable directory mapping.  
                Directory mapping is off when you start Maya. If enabled, when opening  
                Maya scenes, file texture paths (and other file paths) will be converted  
                when the scene is opened. The -cd flag only returns mapped directories  
                when -enable is true.  
                Query returns whether mapping has been enabled.  
                Properties: create, query
        getAllMappings (bool?): Get all current mappings.  
                Returns string array of current mappings in format:  
                [redirect1, replacement1, ... redirectN, replacementN]  
                Properties: create
        getMappedDirectory (str?): Get the mapped redirected directory. The given argument must  
                exactly match the first string used with the -mapDirectory flag.  
                Properties: create
        mapDirectory (Tuple[str, str]?): Map a directory - the first argument is mapped to the second.  
                Neither directory needs to exist on the local machine at the time  
                of invocation.  
                Properties: create
        unmapDirectory (str?): Unmap a directory. The given argument must exactly match the  
                argument used with the -mapDirectory flag.  
                Properties: create

    Returns:
        str: when convertDirectory is used
        None: when convertDirectory is not used

    Example:
    """

