from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def filePathEditor(*args: str, query: bool = ..., attributeOnly: bool = ..., attributeType: Queryable[str] = ..., byType: str = ..., copyAndRepath: Tuple[str, str] = ..., deregisterType: str = ..., force: bool = ..., listDirectories: str = ..., listFiles: str = ..., listRegisteredTypes: bool = ..., preview: bool = ..., recursive: bool = ..., refresh: bool = ..., registerType: str = ..., relativeNames: bool = ..., repath: str = ..., replaceAll: bool = ..., replaceField: str = ..., replaceString: Tuple[str, str] = ..., status: bool = ..., temporary: bool = ..., typeLabel: str = ..., unresolved: bool = ..., withAttribute: bool = ...) -> Union[bool, str]:
    """Maya can reference and use external files, such as textures or other Maya
    scenes. This command is used to get the information about those file paths and
    modify them in bulk.
    By default, only the most frequently used types of files are presented to the
    user:For the command to manage more file types, those must be explicitly requested by
    the caller using the "registerType" flag. This flag tells the command about
    attributes or nodes that are to reveal their paths when the command is used.Currently, the attributes specified through this flag must have the
    "usedAsFileName" property. Supported nodes are "reference" and plug-in nodes.
    For example: "brush.flowerImage" or "reference" can be used as value for this
    flag.Conversely, the "deregisterType" flag can be used to tell the command to stop
    handling certain attributes or nodes.Once the set of attributes and nodes to be searched for external files is
    selected, the command can be used to obtain a list of plugs that contain file
    names. Additional information can be obtained, such as each file's name,
    directory, and report whether the file exists. Additional information about the
    associated node or plug can also be obtained, such as its name, type and label.Finally, the command can be used to perform various manipulations such as
    editing the paths, remapping the files or verifying the presence of
    identically-named files in target directories. See the "repath",
    "copyAndRepath" and "replaceField" flags for more information.The results of these manipulations can be previewed before they are applied
    using the "preview" flag.filepath, editor, repath
    Args:
        attributeOnly (bool?): Used with "listFiles" to return the node and attribute name that  
                are using the files.  
                Properties: query
        attributeType (Queryable[str]?): Query the attribute type for the specified plug.  
                Properties: query
        byType (str?): Used with "listFiles" to query files that are  
                used by the specified node type or attribute type.  
                			In query mode, this flag needs a value.  
                Properties: query
        copyAndRepath (Tuple[str, str]?): Copy a source file to the destination path and repath the plug data to the new  
                file.  
                The source file must have the same name as the one in the plug.  
                The command will look for the file at the specified location first. If not  
                found, the command will try to use the original file in the plug.  
                If the file is still not found, nothing is done.  
                Properties: create
        deregisterType (str?): Deregister a file type from the list of registered types so the command stops  
                handling it.  
                Unless the "temporary" flag is used, the type will be removed from the  
                preferences will not reappear on application restart. When the "temporary" flag  
                is specified, the deregistration is only effective for the current session.  
                The deregistration will be rejected if the type has already been unregistered.  
                However, it is valid to deregister permanently (without the "temporary" flag)  
                a type after it has been temporarily deregistered.  
                Properties: create
        force (bool?): Used with flag "repath" to repath all files to the new location, including  
                the resolved files. Otherwise, "repath" will only deal with the missing files.  
                Used with flag "copyAndRepath" to overwrite any colliding file at the  
                destination. Otherwise, "copyAndRepath" will use the existing file at the  
                destination instead of overwriting it.  
                The default value is off.  
                Properties: create
        listDirectories (str?): List all sub directories of the specified directory.  Only directories  
                containing at least one file whose type is registered (see "registerType") will  
                be listed.  
                If no directory is provided, all directories applicable to the scene will be  
                returned.  
                			In query mode, this flag needs a value.  
                Properties: query
        listFiles (str?): List files in the specified directory. No recursion in subdirectories will be  
                performed.  
                			In query mode, this flag needs a value.  
                Properties: query
        listRegisteredTypes (bool?): Query the list of registered attribute types. The registered types include  
                the auto-loaded types from the preference file and the types explicitly  
                registered by the user, both with and without the "temporary" flag.  
                Properties: query
        preview (bool?): Used with "repath", "replaceString" or "copyAndRepath" to preview the result of  
                the operation instead of excuting it.  
                When it is used with "repath" or "replaceString", the command returns the new  
                file path and a status flag indicating whether the new file exists (1) or not  
                (0).  
                The path name and the file status are listed in pairs.  
                When it is used with "copyAndRepath", the command returns the files that need  
                copying.  
                Properties: create
        recursive (bool?): Used with flag "repath" to search the files in the target directory and its  
                subdirectories recursively. If the flag is on, the command will repath the plug  
                to a file that has the same name in the target directory or sub directories.  
                If the flag is off, the command will apply the directory change without  
                verifying that the resulting file exists.  
                Properties: create
        refresh (bool?): Clear and re-collect the file information in the scene.  
                The command does not automatically track file path modifications in the scene.  
                So it is the users responsibility to cause refreshes in order to get up-to-date  
                information.  
                Properties: create
        registerType (str?): Register a new file type that the command will handle and recognize from now on.  
                Unless the "temporary" flag is used, the registered type is saved in the  
                preferences and reappears on application restart.  
                The new type will be rejected if it collides with an existing type or label.  
                One exception to this is when registering a type without the "temporary" flag  
                after the type has been registered with it. This is considered as modifying  
                the persistent/temporary property of the existing type, rather than registering  
                a new type.  
                Properties: create
        relativeNames (bool?): Used with "listDirectories" or "listFiles" to return the relative path  
                of each directory or file.  Paths are relative to the current project  
                folder.  
                If a file or the directory is not under the current project folder,  
                the returned path will still be a full path.  
                Properties: query
        repath (str?): Replace the directory part of a file path with a specified location.  
                The file name will be preserved.  
                Properties: create
        replaceAll (bool?): Used with flag "replaceString", specifies how many times the matched string will  
                be replaced. When the flag is false, only the first matched string will be  
                replaced. Otherwise, all matched strings will be replaced.  
                The default value is false.  
                Properties: create
        replaceField (str?): Used with the "replaceString" flag to control the scope of the replacement.  
                Possible values are:  
                "pathOnly" - only replace strings in the directory part.  
                "nameOnly" - only replace strings in the file name, without the directory.  
                "fullPath" - replace strings anywhere in the full name.  
                The default argument is "fullPath".  
                Properties: create
        replaceString (Tuple[str, str]?): Replace the target string with the new string in the file paths.  
                The flag needs two arguments: the first one is the target string and the second  
                one is the new string.  
                See the "replaceField" and "replaceAll" flags to control how the replacement is  
                performed.  
                Properties: create
        status (bool?): Used with "listFiles", this will cause the returned list of files to include  
                one status flag per file: 0 if it cannot be resolved and 1 if it can.  
                Used with "listDirectories", this will cause the returned list of directories to  
                include one status flag per directory: 0 if it cannot be resolved, 1 if it can  
                and 2 if the resolution is partial.  
                The status will be interleaved with the file/directory names, with the name  
                appearing first. See the example for "listFiles".  See the "withAttribute" flag  
                for another way of getting per-file information.  When multiple per-entry items  
                appear in the list (e.g.: plug name), the status is always last.  
                Properties: query
        temporary (bool?): Make the effect of the "register"/"deregister" flag only applicable in the  
                current session.  
                Normally, a type registration/deregistration is permanent and is made persistent  
                via a preference file. When the "temporary" flag is specified, the changes will  
                not be saved to the preference file. When the application restarts, any type  
                that has been previously temporarily registered will not appear and any type  
                that was temporarily deregistered will re-appear.  
                Properties: create
        typeLabel (str?): Used with "registerType" to set the label name for the new file type.  
                Used with "query" to return the type label for the specified attribute type.  
                For default types, the type label is the localized string.  
                For other types, the type label is supplied by user.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        unresolved (bool?): Used with "listFiles" to query the unresolved files  
                that are being used in the scene.  
                Properties: query
        withAttribute (bool?): Used with "listFiles" to return the name of the plug using a given file.  
                For example, if "file.jpg" is used by the plug "node1.fileTextureName",  
                then the returned string will become the pair  
                "file.jpg node1.fileTextureName".  See the "status" flag for another  
                way to get per-file information.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

