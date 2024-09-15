from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def namespace(*, query: bool = ..., absoluteName: bool = ..., addNamespace: str = ..., collapseAncestors: str = ..., deleteNamespaceContent: bool = ..., exists: str = ..., force: bool = ..., isRootNamespace: Queryable[str] = ..., mergeNamespaceWithOther: str = ..., mergeNamespaceWithParent: bool = ..., mergeNamespaceWithRoot: bool = ..., moveNamespace: Tuple[str, str] = ..., parent: str = ..., recurse: bool = ..., relativeNames: bool = ..., removeNamespace: str = ..., rename: Tuple[str, str] = ..., setNamespace: str = ..., validateName: str = ...) -> Union[str, bool]:
    """This command allows a namespace to be created, set or removed.A namespace is a simple grouping of objects under a given name.
    Namespaces are primarily used to resolve name-clash issues in Maya,
    where a new object has the same name as an existing object (from
    importing a file, for example).  Using namespaces, you can have two
    objects with the same name, as long as they are contained in
    differenct namespaces.Namespaces are reminiscent of hierarchical structures like file
    systems where namespaces are analogous to directories and objects are
    analogous to files. The colon (':') character is the separator used to
    separate the names of namespaces and nodes instead of the slash ('/')
    or backslash ('\\') character.  Namespaces can contain other namespaces
    as well as objects.  Like objects, the names of namespaces must be
    unique within another namespace. Objects and namespaces can be in only
    one namespace. Namespace names and object names don't clash so a
    namespace and an object contained in another namespace can have the
    same name.There is an unnamed root namespace specified with a leading colon
    (':').  Any object not in a named namespace is in the root namespace.
    Normally, the leading colon is omitted from the name of an object as
    it's presence is implied. The presence of a leading colon is
    important when moving objects between namespaces using the 'rename'
    command.  For the 'rename' command, the new name is relative to the
    current namespace unless the new name is fully qualified with a
    leading colon.Namespaces are created using the 'add/addNamespace' flag. By default they are
    created under the current namespace. Changing the current namespace is
    done with the 'set/setNamespace' flag. To reset the current namespace to
    the root namespace, use 'namespace -set ":";'. Whenever an object is
    created, it is added by default to the current namespace.When creating a new namespace using a qualified name, any intervening namespaces which do
    not yet exist will be automatically created. For example, if the name of
    the new namespace is specified as "A:B" and the current namespace already
    has a child namespace named "A" then a new child namespace named "B" will
    be created under "A". But if the current namespace does not yet have a
    child named "A" then it will be created automatically. This applies
    regardless of the number of levels in the provided name (e.g. "A:B:C:D").The 'p/parent' flag can be used to explicitly specify the parent namespace
    under which the new one should be created, rather than just defaulting to
    the current namespace.If the name given for the new namespace is absolute (i.e. it begins with a
    colon, as in ":A:B") then both the current namespace and the 'parent' flag
    will be ignored and the new namespace will be created under the root namespace.The relativeNamespace flag can be used to change the way node names
    are displayed in the UI and returned by the 'ls' command. Here are
    some specific details on how the return from the 'ls' command works in
    relativeNamespace mode:
    Args:
        absoluteName (bool?): This is a general flag which can be used to specify the desired format for  
                the namespace(s) returned by the command.  
                The absolute name of the namespace is a full namespace path, starting from the root namespace ":"  
                and including all parent namespaces.  For example ":ns:ball" is an absolute namespace  
                name while "ns:ball" is not.  
                Properties: create, query
        addNamespace (str?): Create a new namespace with the given name. Both qualified names ("A:B") and unqualified names ("A") are acceptable. If any of the higher-level namespaces in a qualified name do not yet exist, they will be created.  
                If the supplied name contains invalid characters it will first be modified as per the validateName flag.  
                Properties: create
        collapseAncestors (str?): Delete all empty ancestors of the given namespace.  
                An empty namespace is a a namespace that does not contain any objects  
                or other nested namespaces  
                Properties: create
        deleteNamespaceContent (bool?): Used with the 'rm/removeNamespace' flag to indicate that when removing a namespace  
                the contents of the namespace will also be removed.  
                Properties: create
        exists (str?): Returns true if the specified namespace exists, false if not.  
                Properties: create
        force (bool?): Used with 'mv/moveNamespace' to force the move operation to ignore  
                name clashes.  
                Properties: create
        isRootNamespace (Queryable[str]?): Returns true if the specified namespace is root, false if not.  
                Properties: query
        mergeNamespaceWithOther (str?): Used with the 'rm/removeNamespace' flag.  
                When removing a namespace, move the rest of the namespace  
                content to the specified namespace.  
                Properties: create
        mergeNamespaceWithParent (bool?): Used with the 'rm/removeNamespace' flag.  
                When removing a namespace, move the rest of the namespace  
                content to the parent namespace.  
                Properties: create
        mergeNamespaceWithRoot (bool?): Used with the 'rm/removeNamespace' flag.  
                When removing a namespace, move the rest of the namespace  
                content to the root namespace.  
                Properties: create
        moveNamespace (Tuple[str, str]?): Move the contents of the first namespace into the second namespace.  
                Child namespaces will also be moved.  
              
                Attempting to move a namespace containing referenced nodes will  
                result in an error; use the 'file' command ('file -edit -namespace')  
                to change a reference namespace.  
              
                If there are objects in the source namespace with the same name as  
                objects in the destination namespace, an error will be issued. Use  
                the 'force' flag to override this error - name clashes will be  
                resolved by renaming the objects to ensure uniqueness.  
                Properties: create
        parent (str?): Used with the 'addNamespace' or 'rename' flags to specifiy  
                the parent of the new namespace. The full namespace parent path is required.  
                When using 'addNamespace' with an absolute name, the 'parent' will be ignored  
                and the command will display a warning  
                Properties: create
        recurse (bool?): Can be used with the 'exists' flag to recursively look for the  
                specified namespace  
                Properties: query
        relativeNames (bool?): Turns on relative name lookup, which causes name lookups within Maya  
                to be relative to the current namespace. By default this is off, meaning  
                that name lookups are always relative to the root namespace. Be careful  
                turning this feature on since commands such as setAttr will behave  
                differently. It is wise to only turn this feature on while executing  
                custom procedures that you have written to be namespace independent and  
                turning relativeNames off when returning control from your custom procedures.  
                Note that Maya will turn on relative naming during file I/O. Although it  
                is not recommended to leave relativeNames turned on, if you try to toggle  
                the value during file I/O you may notice that the value stays "on" because  
                Maya has already temporarily enabled it internally.  
              
                When relativeNames are enabled, the returns provided by the 'ls' command  
                will be relative to the current namespace. See the main description of this  
                command for more details.  
                Properties: create, query
        removeNamespace (str?): Deletes the given namespace.  The namespace  
                must be empty for it to be deleted.  
                Properties: create
        rename (Tuple[str, str]?): Rename the first namespace to second namespace name. Child namespaces will  
                also be renamed. Both names are relative to the current namespace. Use the  
                'parent' flag to specify a parent namespace for the renamed namespace.  
                An error is issued if the second namespace name already exists.  
                If the supplied name contains invalid characters it will first be modified  
                as per the validateName flag.  
                Properties: create
        setNamespace (str?): Sets the current namespace.  
                Properties: create
        validateName (str?): Convert the specified name to a valid name to make it contain no illegal characters.  
                The leading illegal characters will be removed and other illegal characters will be converted to '_'.  
                Specially, the leading numeric characters and trailing space characters will be also removed.  
              
                Full name path can be validated as well. However, if the namespace of the path does not exist, command will only  
                return the base name. For example, ":nonExistentNS:name" will be converted to "name".  
              
                If the entire name consists solely of illegal characters, e.g. "123" which contains only leading digits, then the returned string will be empty.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

