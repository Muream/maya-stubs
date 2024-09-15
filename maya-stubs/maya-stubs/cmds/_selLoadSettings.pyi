from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selLoadSettings(*args: str, edit: bool = ..., query: bool = ..., activeProxy: Queryable[str] = ..., deferReference: bool = ..., fileName: Queryable[str] = ..., numSettings: Queryable[int] = ..., proxyManager: Queryable[str] = ..., proxySetFiles: Queryable[str] = ..., proxySetTags: Queryable[str] = ..., proxyTag: Queryable[str] = ..., referenceNode: Queryable[str] = ..., shortName: bool = ..., unresolvedName: bool = ...) -> Union[str, bool, int]:
    """This command is used to edit and query information about the implicit load
    settings. Currently this is primarily intended for internal use within the
    Preload Reference Editor.
    selLoadSettings acts on load setting IDs. When implict load settings are
    built for a target scene, there will be one load setting for each reference
    in the target scene. Each load setting has a numerical ID which is its index
    in a pre-order traversal of the target reference hierarchy (with the root
    scenefile being assigned an ID of 0). Although the IDs are numerical they must
    be passed to the command as string array.
    Example:
    Given the scene:where:
    a references b and c
    c references d and e
    the IDs will be as follows:
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    selLoadSettings can be used to change the load state of a reference:
    whether it will be loaded or unloaded (deferred) when the target scene is
    opened.
    Note: selLoadSettings can accept multiple command parameters, but the order
    must be selected carefully such that no reference is set to the loaded state
    while its parent is in the unlaoded state.
    Given the scene:where:
    a references b
    b references c
    a = 0
    b = 1
    c = 2
    and b and c are currently in the unloaded state.
    The following command will succeed and change both b and c to the loaded state:
    selLoadSettings -e -deferReference 0 "1" "2";
    whereas the following command will fail and leave both b and c in the unloaded
    state:
    selLoadSettings -e -deferReference 0 "2" "1";
    Bear in mind that the following command will also change both b and c to the
    loaded state:
    selLoadSettings -e -deferReference 0 "1";
    This is because setting a reference to the loaded state automatically sets all
    child references to the loaded state as well. And vice versa, setting a reference
    the the unloaded state automatically sets all child reference to the unloaded state.selective, load, setting, preload, reference
    Args:
        activeProxy (Queryable[str]?): Change or query the active proxy of a proxy set. In query mode, returns the  
                proxyTag of the active proxy; in edit mode, finds the proxy in the proxySet  
                with the given tag and makes it the active proxy.  
                Properties: create, query, edit
        deferReference (bool?): Change or query the load state of a reference.  
                Properties: create, query, edit
        fileName (Queryable[str]?): Return the file name reference file(s) associated with the indicated load setting(s).  
                Properties: create, query
        numSettings (Queryable[int]?): Return the number of settings in the group of implicit load settings. This is  
                equivalent to number of references in the scene plus 1.  
                Properties: create, query
        proxyManager (Queryable[str]?): Return the name(s) of the proxy manager(s) associated with the indicated load setting(s).  
                Properties: create, query
        proxySetFiles (Queryable[str]?): Return the name(s) of the proxy(ies) available in the proxy set associated with the indicated load setting(s).  
                Properties: create, query
        proxySetTags (Queryable[str]?): Return the name(s) of the proxy tag(s) available in the proxy set associated with the indicated load setting(s).  
                Properties: create, query
        proxyTag (Queryable[str]?): Return the name(s) of the proxy tag(s) associated with the indicated load setting(s).  
                Properties: create, query
        referenceNode (Queryable[str]?): Return the name(s) of the reference node(s) associated with the indicated load setting(s).  
                Properties: create, query
        shortName (bool?): Formats the return value of the 'fileName' query flag to only return the short  
                name(s) of the reference file(s).  
                Properties: create, query
        unresolvedName (bool?): Formats the return value of the 'fileName' query flag to return the unresolved  
                name(s) of the reference file(s). The unresolved file name is the file name  
                used when the reference was created, whether or not that file actually exists  
                on disk. When Maya encounters a file name which does not exist on disk it  
                attempts to resolve the name by looking for the file in a number of other  
                locations. By default the 'fileName' flag will return this resolved value.  
                Properties: create, query

    Returns:
        str: For query execution.

    Example:
    """

