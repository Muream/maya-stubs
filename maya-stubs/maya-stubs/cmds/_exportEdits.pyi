from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def exportEdits(*args: str, query: bool = ..., excludeHierarchy: bool = ..., excludeNode: Queryable[Multiuse[str]] = ..., exportSelected: bool = ..., force: bool = ..., includeAnimation: bool = ..., includeConstraints: bool = ..., includeDeformers: bool = ..., includeNetwork: bool = ..., includeNode: Queryable[Multiuse[str]] = ..., includeSetAttrs: bool = ..., includeSetDrivenKeys: bool = ..., includeShaders: bool = ..., selected: bool = ..., type: Queryable[str] = ..., editCommand: Queryable[Multiuse[str]] = ..., onReferenceNode: Queryable[Multiuse[str]] = ...) -> Union[List[str], bool, Multiuse[str], str]:
    """Use this command to export edits made in the scene to a file.
    The exported file can be subsequently imported to another scene.
    Edits may include: nodes, connections and reference edits such as value changes.
    The nodes that are included in the exported file will be based on the
    options used.
    At least one option flag that describes the set of target nodes to include in the
    exported file must be specified (e.g. 'selected', 'onReferenceNode').
    Use the inclusion flags ('includeAnimation', 'includeShaders', 'includeNetwork') to
    specify which additional related nodes will be added to the export list.
    In export mode, when the command completes successfully, the name of the exported file will
    be returned.
    In query mode, this command will return information about the contents of the exported
    file.
    The query mode will return the list of nodes that will be considered for
    inclusion in the exported file based on the specified flags.reference, export, node, import
    Args:
        excludeHierarchy (bool?): By default, all DAG parents and DAG history are written to the export file.  
                To prevent any DAG relations not otherwise connected to the target nodes to be  
                included, specify the -excludeHierarchy flag.  
                Properties: create, query
        excludeNode (Queryable[Multiuse[str]]?): Prevent the node from being included in the list of nodes being  
                exported. This flag is useful to exclude specific scene nodes that might  
                otherwise be exported. In the case where more than one Maya node has the  
                same name, the DAG path can be specified to uniquely identify the node.  
                Properties: create, query, multiuse
        exportSelected (bool?): The selected nodes and their connections to each other will be exported. Additionally,  
                any dangling connections to non-exported nodes will be exported.  
                Default nodes are ignored and never exported.  
                Note that when using the exportSelected flag, only selected nodes are exported, and  
                -include/-exclude flags such as -includeHierarchy are ignored.  
                Properties: create, query
        force (bool?): Force the export action to take place. This flag is required to overwrite an existing file.  
                Properties: create, query
        includeAnimation (bool?): Additionally include animation nodes and animation helper nodes associated with  
                the target nodes being exported.  
                Properties: create, query
        includeConstraints (bool?): Additionally include constraint-related nodes associated with the target nodes being exported.  
                Properties: create, query
        includeDeformers (bool?): Additionally include deformer networks associated with the target nodes being exported.  
                Properties: create, query
        includeNetwork (bool?): Additionally include the network of nodes connected to the target nodes being exported.  
                Properties: create, query
        includeNode (Queryable[Multiuse[str]]?): Additionally include the named node in the list of nodes being  
                exported. In the case where more than one Maya node has the  
                same name, the DAG path can be specified to uniquely identify the node.  
                Properties: create, query, multiuse
        includeSetAttrs (bool?): When using the -selected/-sel flag, if any of the selected nodes are referenced,  
                also include/exclude any setAttr edits on those nodes. If used with the -onReferenceNode/-orn  
                flag, include/exclude any setAttr edits on the reference.  
                Properties: create, query
        includeSetDrivenKeys (bool?): Additionally include setDrivenKey-related nodes associated with the target nodes being exported.  
                Properties: create, query
        includeShaders (bool?): Additionally include shaders associated with the target nodes being exported.  
                Properties: create, query
        selected (bool?): Export will operate on the list of nodes currently selected. This flag differs from the  
                exportSelected flag in that the selected nodes are not exported, only the edits on  
                them, and any nodes found via the include flags that are used (such as includeAnimation,  
                includeNetwork and so on).  
                Properties: create, query
        type (Queryable[str]?): Set the type of the exported file.  
                Valid values are "editMA" or "editMB".  
                Note that this command respects the global "defaultExtensions" setting  
                for file naming that is controlled with the file command defaultExtensions  
                option.  See the file command for more information.  
                Properties: create, query
        editCommand (Queryable[Multiuse[str]]?): This is a secondary flag used to indicate which type of reference edits should  
                be considered by the command.  
                If this flag is not specified all edit types will be included.  
                This flag requires a string parameter. Valid values are: "addAttr",  
                "connectAttr", "deleteAttr", "disconnectAttr", "parent", "setAttr",  
                "lock" and "unlock". In some contexts, this flag may be specified  
                more than once to specify multiple edit types to consider.  
                Properties: create, query, multiuse
        onReferenceNode (Queryable[Multiuse[str]]?): This is a secondary flag used to indicate that only those edits which are stored  
                on the indicated reference node should be considered. This flag only supports  
                multiple uses when specified with the "exportEdits" command.  
                Properties: create, query, multiuse

    Returns:
        List[str]: For query execution.

    Example:
    """

