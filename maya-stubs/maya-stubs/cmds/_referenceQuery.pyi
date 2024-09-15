from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def referenceQuery(*args: str, child: bool = ..., isExportEdits: bool = ..., isLoaded: bool = ..., liveEdits: bool = ..., dagPath: bool = ..., editAttrs: bool = ..., editNodes: bool = ..., editStrings: bool = ..., failedEdits: bool = ..., filename: bool = ..., isNodeReferenced: bool = ..., isPreviewOnly: bool = ..., namespace: bool = ..., nodes: bool = ..., parent: bool = ..., parentNamespace: bool = ..., referenceNode: bool = ..., shortName: bool = ..., showDagPath: bool = ..., showFullPath: bool = ..., showNamespace: bool = ..., successfulEdits: bool = ..., topReference: bool = ..., unresolvedName: bool = ..., withoutCopyNumber: bool = ..., editCommand: Queryable[Multiuse[str]] = ..., onReferenceNode: Queryable[Multiuse[str]] = ...) -> Union[List[str], Multiuse[str]]:
    """Use this command to find out information about references and referenced nodes.
    A valid target is either a reference node, a reference file, or a referenced node.
    Some flags don't require a target, see flag descriptions for more information
    on what effect this has.
    When a scene contains multiple levels of file references, those edits which
    affect a nested reference may be stored on several different reference nodes.
    For example:
    A.ma has a reference to B.ma which has a reference to C.ma which contains
    a poly sphere (pSphere1).
    If you were to open B.ma and translate the sphere, an edit would be stored
    on CRN which refers to a node named "C:pSphere1".
    If you were then to open A.ma and parent the sphere, an edit would be
    stored on BRN which refers to a node named "B:C:pSphere1".
    It is important to note that when querying edits which affect a nested
    reference, the edits will be returned in the same format that they were
    applied. In the above example, opening A.ma and querying all edits which affect
    C.ma, would return two edits a parent edit affecting "B:C:pSphere1", and a
    setAttr edit affecting "C:pSphere1". Since there is currently no node named
    C:pSphere1 (only B:C:pSphere1) care will have to be taken when interpreting the
    returned information.
    The same care should be taken when referenced DAG nodes have been parented or
    instanced. Continuing with the previous example, let's say that you were to
    open A.ma and, instead of simply parenting pSphere1, you were to instance it.
    While A.ma is open, "B:C:pSphere1" may now be an amibiguous name, replaced by
    "|B:C:pSphere1" and "group1|B:C:pSphere1". However querying the edits which
    affect C.ma would still return a setAttr edit affecting "C:pSphere1" since it
    was applied prior to B:C:pSphere1 being instanced.
    Some tips:
    1. Use the '-topReference' flag to query only those edits which were applied
       from the currently open file.
    2. Use the '-onReferenceNode' flag to limit the results to those edits where
       are stored on a given reference node. You can then use various string
       manipulation techniques to extrapolate the current name of any affected
       nodes.reference, attribute, node
    Args:
        child (bool?): This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags  
                to indicate the the children of the target reference will be returned.  
                Returns a string array.  
                Properties: create
        isExportEdits (bool?): Returns a boolean indicating whether the specified reference node or file  
                name is an edits file (created with the Export Edits feature)  
                Properties: create
        isLoaded (bool?): Returns a boolean indicating whether the specified reference node or  
                file name refers to a loaded or unloaded reference.  
                Properties: create
        liveEdits (bool?): Specifies that the edits should be returned based on the live edits  
                database. Only valid when used in conjunction with the editStrings flag.  
                Properties: create
        dagPath (bool?): This flag modifies the '-n/-nodes' flag to indicate that the names of  
                any dag objects returned will include as much of the dag path as is  
                necessary to make the names unique. If this flag is not present, the  
                names returned will not include any dag paths.  
                Properties: create
        editAttrs (bool?): Returns string array.  
                A main flag used to query the edits that have  
                been applied to the target. Only the names of  
                the attributes involved in the reference edit will be  
                returned. If an edit involves multiple attributes (e.g. "connectAttr"  
                edits) the nodes will be returned as separate,  
                consecutive entries in the string array. A valid target is either  
                a reference node, a reference file, or a referenced node.  
                If a referenced node is specified, only those edits which  
                affect that node will be returned. If a reference file  
                or reference node is specified any edit which affects  
                a node in that reference will be returned. If no target is  
                specified all edits are returned. This command can  
                be used on both loaded and unloaded references. By default  
                it will return all the edits, formatted as MEL commands,  
                which apply to the target.  
                This flag can be used in combination with the  
                '-ea/-editAttrs' flag to indicate that the names  
                of both the involved nodes and attributes will be  
                returned in the format 'node.attribute'.  
                Properties: create
        editNodes (bool?): Returns string array.  
                A main flag used to query the edits that have  
                been applied to the target. Only the names of  
                the nodes involved in the reference edit will be  
                returned. If an edit involves multiple nodes (e.g. "connectAttr"  
                edits) the nodes will be returned as separate,  
                consecutive entries in the string array. A valid target is either  
                a reference node, a reference file, or a referenced node.  
                If a referenced node is specified, only those edits which  
                affect that node will be returned. If a reference file  
                or reference node is specified any edit which affects  
                a node in that reference will be returned. If no target is  
                specified all edits are returned. This command can  
                be used on both loaded and unloaded references. By default  
                it will return all the edits, formatted as MEL commands,  
                which apply to the target.  
                This flag can be used in combination with the  
                '-ea/-editAttrs' flag to indicate that the names  
                of both the involved nodes and attributes will be  
                returned in the format 'node.attribute'.  
                Properties: create
        editStrings (bool?): Returns string array.  
                A main flag used to query the edits that have  
                been applied to the target. The edit will be returned  
                as a valid MEL command. A valid target is either  
                a reference node, a reference file, or a referenced node.  
                If a referenced node is specified, only those edits which  
                affect that node will be returned. If a reference file  
                or reference node is specified any edit which affects  
                a node in that reference will be returned. If no target is  
                specified all edits are returned. This command can be used  
                on both loaded and unloaded references. By default it will  
                return all the edits, formatted as MEL commands,  
                which apply to the target.  
                This flag cannot be used with either the '-en/-editNodes'  
                or '-ea/-editAttrs' flags.  
                Properties: create
        failedEdits (bool?): This is a secondary flag used to indicate whether or not failed  
                edits should be acted on (e.g. queried, removed, etc...). A failed  
                edit is an edit which could not be successfully applied the last  
                time its reference was loaded.  
                An edit can fail for a variety of reasons (e.g. the referenced  
                node to which it applies was removed from the referenced file).  
                By default failed edits will not be acted on.  
                Properties: create
        filename (bool?): Returns string.  
                A main flag used to query the filename associated with the target reference.  
                Properties: create
        isNodeReferenced (bool?): Returns boolean.  
                A main flag used to determine whether or not the target node comes  
                from a referenced file.  
                true if the target node comes from a referenced file, false if not.  
                Properties: create
        isPreviewOnly (bool?): Returns boolean.  
                This flag is used to determine whether or not the target reference node is  
                only a preview reference node.  
                Properties: create
        namespace (bool?): Returns string.  
                This flag returns the full namespace path of the target reference, starting from the root namespace ":".  
                It can be combined with the shortName flag to return just the base name of the namespace.  
                Properties: create
        nodes (bool?): Returns string array.  
                A main flag used to query the contents of the target reference.  
                Properties: create
        parent (bool?): This flag modifies the '-rfn/-referenceNode' and '-f/-filename' flags  
                to indicate the the parent of the target reference will be returned.  
                Properties: create
        parentNamespace (bool?): A main flag used to query and return the parent namespace of the target reference.  
                Properties: create
        referenceNode (bool?): Returns string.  
                A main flag used to query the reference node associated with the target  
                reference.  
                Properties: create
        shortName (bool?): This flag modifies the '-f/-filename' and '-ns/-namespace' flags.  
                Used with the '-f/-filename' flag indicates that the file name returned will be the short name  
                (i.e. just a file name without any directory paths). If this flag is not present, the full name  
                and directory path will be returned.  
                Used with the '-ns/-namespace' flag indicates that the namespace returned will be the base name of the namespace.  
                (i.e. the base name of the full namespace path ":AAA:BBB:CCC" is "CCC"  )  
                Properties: create
        showDagPath (bool?): Shows/hides the full dag path for edits. If false only displays the  
                node-name of reference edits. Must be used with the -editNodes,  
                -editStrings or -editAttrs flag.  
                Properties: create
        showFullPath (bool?): Return the full path from the root namespace for reference edits.  
                Must be used with the -editNodes, -editStrings or -editAttrs flags.  
                Properties: create
        showNamespace (bool?): Shows/hides the namespaces on nodes in the reference edits.  
                Must be used with the -editNodes, -editStrings or -editAttrs flag  
                Properties: create
        successfulEdits (bool?): This is a secondary flag used to indicate whether or not successful  
                edits should be acted on (e.g. queried, removed, etc...). A successful  
                edit is any edit which was successfully applied the last time its  
                reference was loaded.  
                By default successful edits will be acted on.  
                Properties: create
        topReference (bool?): This flag modifies the '-rfn/-referenceNode' flag  
                to indicate the top level ancestral reference of the target reference will be  
                returned.  
                Properties: create
        unresolvedName (bool?): This flag modifies the '-f/-filename' flag to indicate that the file name  
                returned will be unresolved (i.e. it will be the path originally  
                specified when the file was loaded into Maya; this path may  
                contain environment variables and may not exist on disk). If this  
                flag is not present, the resolved name will     be returned.  
                Properties: create
        withoutCopyNumber (bool?): This flag modifies the '-f/-filename' flag to indicate that the file name  
                returned will not have a copy number (e.g. '{1}') appended to the end. If this  
                flag is not present, the file name returned may have a copy number  
                appended to the end.  
                Properties: create
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

