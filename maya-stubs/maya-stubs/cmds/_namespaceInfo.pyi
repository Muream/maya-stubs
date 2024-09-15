from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def namespaceInfo(arg0: str = ..., /, *, absoluteName: bool = ..., baseName: bool = ..., currentNamespace: bool = ..., dagPath: bool = ..., fullName: bool = ..., internal: bool = ..., isRootNamespace: bool = ..., listNamespace: bool = ..., listOnlyDependencyNodes: bool = ..., listOnlyNamespaces: bool = ..., parent: bool = ..., recurse: bool = ..., shortName: bool = ...) -> str:
    """This command displays information about a namespace. The target namespace can optionally be specified on the command line.
    If no namespace is specified, the command will display information about the current namespace.A namespace is a simple grouping of objects under a given name.
    Each item in a namespace can then be identified by its own name, along
    with what namespace it belongs to.  Namespaces can contain other
    namespaces like sets, with the restriction that all namespaces
    are disjoint.Namespaces are primarily used to resolve name-clash issues in Maya,
    where a new object has the same name as an existing object
    (from importing a file, for example).
    Using namespaces, you can have two objects with the same name, as long as
    they are contained in different namespaces.Note that namespaces are a simple grouping of names, so
    they do not effect selection, the DAG, the Dependency Graph, or any other
    aspect of Maya.  All namespace names are colon-separated.The namespace format flags are: baseName(shortName), fullName and absoluteName.
    The flags are used in conjunction with the main query flags to specify the desired namespace format of the returned result. They can also be used to return the different formats of a specified namespace.
    By default, when no format is specified, the result will be returned as a full name.
    Args:
        absoluteName (bool?): This is a general flag which can be used to specify the desired format for  
                the namespace(s) returned by the command.  
                The absolute name of the namespace is a full namespace path, starting from the root namespace ":"  
                and including all parent namespaces.  For example ":ns:ball" is an absolute namespace  
                name while "ns:ball" is not.  
                The absolute namespace name is invariant and is not affected by the current namespace or  
                relative namespace modes.  
                See also other format modifiers 'baseName', 'fullName', etc  
                Properties: create
        baseName (bool?): This is a general flag which can be used to specify the desired format for  
                the namespace(s) returned by the command. The base name of the namespace  
                contains only the leaf level name and does not contain its parent namespace(s).  
                For example the base name of an object named "ns:ball" is "ball".  
                This mode will always return the base name in the same manner, and is not affected by the  
                current namespace or relative namespace mode.  
                See also other format modifiers 'absoluteName', 'fullName', etc  
                The flag 'shortName' is a synonym for 'baseName'.  
                Properties: create
        currentNamespace (bool?): Display the name of the current namespace.  
                Properties: create
        dagPath (bool?): This flag modifies the 'listNamespace' and  
                'listOnlyDependencyNodes' flags to indicate that the names  
                of any dag objects returned will include as much of the dag path  
                as is necessary to make the names unique. If this flag is not  
                present, the names returned will not include any dag paths.  
                Properties: create
        fullName (bool?): This is a general flag which can be used to specify the desired format for  
                the namespace(s) returned by the command. The full name of the namespace  
                contains both the namespace path and the base name, but without the leading colon representing  
                the root namespace.  
                For example "ns:ball" is a full name, whereas ":ns:ball" is an absolute name.  
                This mode is affected by the current namespace and relative namespace modes.  
                See also other format modifiers 'baseName', 'absoluteName', etc.  
                Properties: create
        internal (bool?): This flag is used together with the 'listOnlyDependencyNodes' flag.  
                When this flag is set, the returned list will  
                include internal nodes (for example itemFilters) that are not listed by default.  
                Properties: create
        isRootNamespace (bool?): Returns true if the namespace is root(":"), false if not.  
                Properties: create
        listNamespace (bool?): List the contents of the namespace.  
                Properties: create
        listOnlyDependencyNodes (bool?): List all dependency nodes in the namespace.  
                Properties: create
        listOnlyNamespaces (bool?): List all namespaces in the namespace.  
                Properties: create
        parent (bool?): Display the parent of the namespace.  
                By default, the list returned will not include internal nodes (such as itemFilters).  
                To include the internal nodes, use the 'internal' flag.  
                Properties: create
        recurse (bool?): Can be specified with 'listNamespace', 'listOnlyNamespaces'  
                or 'listOnlyDependencyNode' to cause the listing to recursively  
                include any child namespaces of the namespaces;  
                Properties: create
        shortName (bool?): This flag is deprecated and may be removed in future releases of Maya.  
                It is a synonym for the baseName flag. Please use the baseName flag instead.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

