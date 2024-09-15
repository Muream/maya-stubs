from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def referenceEdit(*args: str, applyFailedEdits: bool = ..., changeEditTarget: Tuple[str, str] = ..., failedEdits: bool = ..., removeEdits: bool = ..., successfulEdits: bool = ..., editCommand: Queryable[Multiuse[str]] = ..., onReferenceNode: Queryable[Multiuse[str]] = ...) -> Union[bool, Multiuse[str]]:
    """Use this command to remove and change the modifications which have
    been applied to references. A valid commandTarget is either a reference node,
    a reference file, a node in a reference, or a plug from a reference.
    Only modifications that have been made from the currently open scene can
    be changed or removed. The 'referenceQuery -topReference' command can be used
    to determine what modifications have been made to a given commandTarget.
    Additionally only unapplied edits will be affected. Edits are unapplied
    when the node(s) which they affect are unloaded, or when they could
    not be successfully applied. By default this command only works on failed
    edits (this can be adjusted using the "-failedEdits" and
    "-successfulEdits" flags).
    Specifying a reference node as the command target is equivalent to
    specifying every node in the target reference file as a target. In this
    situation the results may differ depending on whether the target
    reference is loaded or unloaded. When it is unloaded, edits that affect both
    a node in the target reference and a node in one of its descendant references
    may be missed (e.g. those edits may not be removed). This is because when a
    reference is unloaded Maya no longer retains detailed information about which
    nodes belong to it. However, edits that only affect nodes in the target reference
    or in one of its ancestral references should be removed as expected.
    When the flags -removeEdits and -editCommand are used together, by default
    all connectAttr edits are removed from the specified source object. To remove
    only edits that connect to a specific target object, the target object can be
    passed as an additional argument to the command. This narrows the match criteria,
    so that only edits that connect the source object to the provided target in this
    additional argument are removed. See the example below.
    NOTE:
    When specifying a plug it is important to use the appropriate long attribute
    name.reference, attribute, node
    Args:
        applyFailedEdits (bool?): Attempts to apply any unapplied edits. This flag is useful if previously  
                failing edits have been fixed using the -changeEditTarget flag. This flag  
                can only be used on loaded references. If the command target is a referenced  
                node, the associated reference is used instead.  
                Properties: create
        changeEditTarget (Tuple[str, str]?): Used to change a target of the specified edits.  
                This flag takes two parameters: the old target of the edits, and the  
                new target to change it to. The target can either be a node name ("node"), a  
                node and attribute name ("node.attr"), or just an attribute name (".attr").  
                If an edit currently affects the old target, it will be changed to affect  
                the new target.  
                Flag 'referenceQuery' should be used to determine the format of the edit targets.  
                As an example most edits store the long name of the attribute  
                (e.g. "translateX"), so when specifying the old target, a long name must also  
                be used. If the short name is specified (e.g. "tx"), chances are the edit  
                won't be retargeted.  
                Properties: create
        failedEdits (bool?): This is a secondary flag used to indicate whether or not failed  
                edits should be acted on (e.g. queried, removed, etc...). A failed  
                edit is an edit which could not be successfully applied the last  
                time its reference was loaded.  
                An edit can fail for a variety of reasons (e.g. the referenced  
                node to which it applies was removed from the referenced file).  
                By default failed edits will be acted on.  
                Properties: create
        removeEdits (bool?): Remove edits which affect the specified unloaded commandTarget.  
                Properties: create
        successfulEdits (bool?): This is a secondary flag used to indicate whether or not successful  
                edits should be acted on (e.g. queried, removed, etc...). A successful  
                edit is any edit which was successfully applied the last time its  
                reference was loaded. This flag will have no affect if the  
                commandTarget is loaded.  
                By default successful edits will not be acted on.  
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
        bool:

    Example:
    """

