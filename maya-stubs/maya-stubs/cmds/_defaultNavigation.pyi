from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def defaultNavigation(arg0: str = ..., arg1: str = ..., /, *, connectToExisting: bool = ..., createNew: bool = ..., defaultAttribute: bool = ..., defaultTraversal: bool = ..., defaultWorkingNode: bool = ..., delete: bool = ..., destination: str = ..., disconnect: bool = ..., force: bool = ..., ignore: bool = ..., navigatorDecisionString: str = ..., quiet: bool = ..., relatedNodes: bool = ..., source: str = ..., unignore: bool = ...) -> str:
    """The defaultNavigation command defines default behaviours when
    creating or manipulating connections between nodes and when
    navigating between nodes via those connections. This command is
    primarily used by attribute editors.
    Args:
        connectToExisting (bool?): Connect the destination (which is a node.attribute or simply  
                node) to an existing source. If the source is specified (as  
                node.attribute or simply as node), the command will proceed  
                immediately. If the source is not specified, the user will  
                be prompted to specify one. Once a source has been specified,  
                a best guess will be made about what the user is trying to  
                accomplish by connecting the two, based on the type of source and  
                type of destination. The command will connect the nodes/attributes  
                according to the best guess. The destination is specified using  
                the destination flag and the source specified using the  
                source flag.  
                Properties: create
        createNew (bool?): Create a new node and connect it to the node.attribute specified  
                using the destination flag.  
                Properties: create
        defaultAttribute (bool?): Returns the name of the attribute to which a connectNodeToNode  
                would connect, given the source (attribute) and destination  
                (node) flags.  
                Returns a string.  
                Properties: create
        defaultTraversal (bool?): Returns the name of the node to which it would make the most  
                sense to navigate to from the destination node.attribute specified.  
                The destination is specified using the destination flag.  
                Returns a string.  
                Properties: create
        defaultWorkingNode (bool?): Returns the name of the node which the user is most likely to  
                want to work with if they are interested in the attributes of  
                the destination node.  
                The destination is specified using the destination flag.  
                Returns a string.  
                Properties: create
        delete (bool?): Delete nodes with connections flowing into the node.attribute  
                specified by the destination flag.  
                Properties: create
        destination (str?): Specifies an existing destination attribute for a createNew or connectToExisting.  
                Properties: create
        disconnect (bool?): If used then disconnect the destination if it exists.  
                Properties: create
        force (bool?): If set to true, then an attempt to connect a source attribute to  
                a destination attribute which already has a source will cause the  
                existing source to be disconnected and the new source to be  
                connected in its place. Default value is true.  
                Properties: create
        ignore (bool?): Ignore any connections flowing into the node.attribute specified  
                by the destination flag.  
                Properties: create
        navigatorDecisionString (str?): This is your opportunity to pass the navigator a string that  
                can help it decide what behaviour to execute.  
                Properties: create
        quiet (bool?): If set to true, then under no circumstances should the user be  
                prompted for more information. Default value is false.  
                Properties: create
        relatedNodes (bool?): List nodes which are conceptually related to the node.attribute  
                specified by the destination. Related nodes may include,  
                but are not limited to, nodes which are directly or indirectly  
                connected to the destination.  
                The destination is specified using the destination flag.  
                Returns an array of strings.  
                Properties: create
        source (str?): Specifies an existing source attribute for a connectToExisting.  
                Properties: create
        unignore (bool?): Stop ignoring any connections flowing into the node.attribute  
                specified by the destination flag.  
                Properties: create

    Returns:
        str: or array of strings

    Example:
    """

