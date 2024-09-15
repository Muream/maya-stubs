from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def workspace(arg0: str = ..., /, *, query: bool = ..., active: bool = ..., baseWorkspace: Queryable[str] = ..., create: str = ..., directory: Queryable[str] = ..., expandName: Queryable[str] = ..., fileRule: Queryable[Tuple[str, str]] = ..., fileRuleEntry: Queryable[str] = ..., fileRuleList: bool = ..., filter: bool = ..., fullName: bool = ..., list: bool = ..., listFullWorkspaces: bool = ..., listWorkspaces: bool = ..., newWorkspace: bool = ..., objectType: Queryable[Tuple[str, str]] = ..., objectTypeEntry: Queryable[str] = ..., objectTypeList: bool = ..., openWorkspace: bool = ..., projectPath: Queryable[str] = ..., removeFileRuleEntry: str = ..., removeVariableEntry: str = ..., renderType: Queryable[Tuple[str, str]] = ..., renderTypeEntry: Queryable[str] = ..., renderTypeList: bool = ..., rootDirectory: bool = ..., saveWorkspace: bool = ..., shortName: bool = ..., update: bool = ..., updateAll: bool = ..., variable: Queryable[Tuple[str, str]] = ..., variableEntry: Queryable[str] = ..., variableList: bool = ...) -> Union[None, str, List[str], bool, Tuple[str, str]]:
    """Create, open, or edit a workspace associated with a given workspace
    file.The string argument represents the workspace. If no workspace is
    specified then the current workspace is assumed.A workspace provides the underlying definition of a Maya Project.
    Each project has an associated workspace file, named workspace.mel, which is stored in the project root directory.
    The workspace file defines a set of rules that map file types to their storage, either relative to the
    project root or as an absolute location.  These rules are used when resolving file paths at runtime.The workspace command operates directly on the low-level definition of the workspace to read, change and store
    the definition to the underlying file.  Use of this command is not generally required, for most purposes
    it is recommended that project definition changes be done via the Project Window in the User Interface. Multiple
    actions go under the assumption that given paths exist.
    Args:
        active (bool?): This flag is a synonym for -o/openWorkspace.  
                Properties: create, query
        baseWorkspace (Queryable[str]?): A workspace may be based on another workspace.  This means  
                that all the file rules and variables in the base workspace  
                apply to this workspace unless they are explicitly overridden.  
                By default, a new workspace has the workspace "default" as  
                it's base workspace. Note that "duplicated" file rules  
                containing relative paths are not verified nor created when  
                creating a new workspace or when changing the base workspace.  
                Properties: query
        create (str?): Create a new directory.  If the directory name is not  
                a full path name, it will be created as a subdirectory of  
                the "current" directory set with the -dir flag. Note that this  
                flag does not create a workspace.  
                Properties: create
        directory (Queryable[str]?): This option will set the current workspace directory to the  
                path specified. When queried it will return the current workspace  
                directory. This directory is used as an initial directory for the  
                fileBrowser and is part of the search path used for locating  
                files. It should not be confused with the current working  
                directory as used by the pwd and chdir commands.  
                When the file browser is used, it will set this value to the last  
                location navigated to.  
                Properties: create, query
        expandName (Queryable[str]?): Query for the full path location of a filename using the current workspace definition.  
                The path may be a project relative file name, a full path name or a variable name.  
                The return value is always a full path name.  
                If the path is an empty string, the return value will be the project root directory.  
                Variable expansion is supported, and will consider both variables defined in the workspace  
                as well as environment variables.  
                There are three formats supported for expanding variable names:  
                %variableName%, $variableName, ${variableName}.  
                Maya will first attempt to find matching variables defined in the current workspace,  
                then search for a matching environment variable.  
                The tilde character ('~') is also supported.  
                If a tilde is located at the beginning of a variable, Maya  
                will only consider and expand environment variables, and will leave the tilde in the  
                expanded result.  
                On linux and mac platforms, a tilde can be used to expand a user's home directory,  
                using the form ~username, ~, or ~/.  When specified as ~username, it will be replaced  
                with the corresponding user's home directory.  When specified as ~ or ~/, it will  
                be replaced with the value of the HOME environment variable.  
                Properties: create, query
        fileRule (Queryable[Tuple[str, str]]?): Set the default location for a file. The first parameter is  
                the fileRule name(scenes, images, etc) and the second is the location. When  
                queried, it returns a list of strings.  The elements of the  
                returned list alternate between fileRule names and the corresponding  
                location.  There is typically one file rule for each available  
                translator. Environment variables are supported.  
                You can set multiple path for the file rule by separating them with  
                semicolons (;) on Windows and colons(:) on MacOSX and Linux.  
                Note that whitespace at the beginning and end of each item in the  
                separated sequence is significant and will be included as part of the  
                path name (which is not usually desired unless the pathname does  
                actually start or end with spaces).  
                A valid filerule name cannot contain multiple byte characters. Note that  
                creating a filerule does not create any directories. It is the user's  
                responsibility to ensure that all paths are valid.  
                Properties: create, query
        fileRuleEntry (Queryable[str]?): Return the location for the given fileRule.  
                Properties: create, query
        fileRuleList (bool?): Returns a list of the currently defined file rules.  
                Properties: create, query
        filter (bool?): This flag is obsolete.
        fullName (bool?): Return the full name of the workspace.  
                Properties: create, query
        list (bool?): This option will list the current workspace directory. If a  
                path is specified for the "workspaceFile" then the contents of that  
                directory will be listed.  Otherwise, the contents of the directory  
                set with the -dir flag will be listed.  
                Properties: create, query
        listFullWorkspaces (bool?): Returns a list of the full path names of all the currently  
                defined workspaces.  
                Properties: create, query
        listWorkspaces (bool?): Returns a list of all the currently defined workspace  
                names.  
                Properties: create, query
        newWorkspace (bool?): This specifies that a new workspace is being created with a given  
                path (full path or relative to "current" directory). If a  
                workspace with this path already exists, the command will fail.  
                Note that the application is creating a virtual workspace without creating  
                any new directories. If given a relative path, it will map the  
                new workspace to the "current" directory set with the -dir flag  
                concatenated with the given path. If the path does not exist, it  
                will default the workspace root directory -rd to the system's root  
                path (e.g. C:\\ or '/'). It is the user's responsibility to ensure  
                that all paths exist.  
                Properties: create
        objectType (Queryable[Tuple[str, str]]?): This flag is obsolete. All default locations will be added to the  
                fileRules going forward.  
                Properties: create, query
        objectTypeEntry (Queryable[str]?): This flag is obsolete. This will now return the same as fileRuleEntry.  
                Properties: create, query
        objectTypeList (bool?): This flag is obsolete. This will now return the same results as  
                fileRuleList going forward.  
                Properties: create, query
        openWorkspace (bool?): Open the workspace.  The workspace becomes the current  
                workspace.  
                Properties: create, query
        projectPath (Queryable[str]?): Convert filePath passed as argument to a filename that is relative to the  
                project root directory (if possible) and return it.  If the  
                filePath is not under the project root directory, a full path  
                name will be returned.  
                Properties: create, query
        removeFileRuleEntry (str?): Remove the given file rule from the specified workspace. If the  
                workspace name is not specified, the given file rule will be removed from  
                the current workspace.  
                Properties: create
        removeVariableEntry (str?): Remove the given variable from the specified workspace. If the  
                workspace name is not specified, the given variable will be removed from  
                the current workspace.  
                Properties: create
        renderType (Queryable[Tuple[str, str]]?): This flag is obsolete. All default render types will be added to  
                fileRules going forward.  
                Properties: create, query
        renderTypeEntry (Queryable[str]?): This flag is obsolete, use fileRuleEntry going forward  
                Properties: create, query
        renderTypeList (bool?): This flag is obsolete, use fileRuleList going forward.  
                Properties: create, query
        rootDirectory (bool?): Returns the root directory of the workspace.  
                Properties: query
        saveWorkspace (bool?): Save the workspace.  Workspaces are normally saved when  
                Maya exits but this flag will make sure that the data is  
                flushed to disk.  
                Properties: create
        shortName (bool?): Query the short name of the workspace.  
                Properties: create, query
        update (bool?): This flag reads all the workspace definitions from the project  
                directory.  It is used by Maya at startup time to find the available  
                workspaces.  
                Properties: create
        updateAll (bool?): This flag is a synonym for -u/update.  
                Properties: create
        variable (Queryable[Tuple[str, str]]?): Set or query the value of a project variable. Project variables  
                are used when expanding names. See the -en/expandName flag below.  
                Properties: create, query
        variableEntry (Queryable[str]?): Given a variable name, will return its value.  
                Properties: create, query
        variableList (bool?): Return a list of all variables in the workspace.  
                Properties: create, query

    Returns:
        None: Depending upon the requested action.
        str: Project short name when querying the 'shortName' flag.
        str: Project full name when querying the 'fullName' flag.
        str: Current workspace name when querying the 'openWorkspace' flag and there is a current one.
        str: Working space directory when querying the 'directory' flag.
        str: File rule on the current workspace when querying one of the 'renderTypeEntry', 'fileRuleEntry', or 'objectTypeEntry' flags.
        str: File rule on the current workspace when querying the 'variableEntry' flag.
        str: Resolved full name of the given file name, or the current root directory if no name given when querying the 'expandName' flag.
        str: Path to the current project workspace when querying the 'projectPath' flag.
        str: Current workspace's base workspace name when querying the 'baseWorkspace' flag.
        str: Current workspace's root directory when querying the 'rootDirectory' flag.
        List[str]: List of file rules when querying the 'fileRule' flag.
        List[str]: List of variables when querying the 'variableList' flag.
        List[str]: List of all workspaces when querying the 'listWorkspaces' flag.
        List[str]: List of full names of all workspaces when querying the 'listFullWorkspaces' flag.
        List[str]: List of path names for all workspace in the directory named when querying the 'list' flag or the current workspace if no directory is named.
        List[str]: List of alternating (file rule, rule location) strings corresponding to the current workspace's file rules.
        List[str]: List of alternating (variable, value) strings corresponding to the current workspace's variables.

    Example:
    """

