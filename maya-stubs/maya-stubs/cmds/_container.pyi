from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def container(*args: str, edit: bool = ..., query: bool = ..., addNode: List[str] = ..., asset: Queryable[List[str]] = ..., assetMember: str = ..., bindAttr: Queryable[Tuple[str, str]] = ..., connectionList: bool = ..., current: bool = ..., fileName: List[str] = ..., findContainer: List[str] = ..., force: bool = ..., includeHierarchyAbove: bool = ..., includeHierarchyBelow: bool = ..., includeNetwork: bool = ..., includeNetworkDetails: Multiuse[str] = ..., includeShaders: bool = ..., includeShapes: bool = ..., includeTransform: bool = ..., isContainer: bool = ..., name: str = ..., nodeList: bool = ..., nodeNamePrefix: bool = ..., parentContainer: bool = ..., preview: bool = ..., publishAndBind: Tuple[str, str] = ..., publishAsChild: Queryable[Tuple[str, str]] = ..., publishAsParent: Queryable[Tuple[str, str]] = ..., publishAsRoot: Queryable[Tuple[str, bool]] = ..., publishAttr: str = ..., publishConnections: bool = ..., publishName: Queryable[str] = ..., removeContainer: bool = ..., removeNode: List[str] = ..., type: Queryable[str] = ..., unbindAndUnpublish: str = ..., unbindAttr: Queryable[Tuple[str, str]] = ..., unbindChild: str = ..., unbindParent: str = ..., unpublishChild: str = ..., unpublishName: str = ..., unpublishParent: str = ..., unsortedOrder: bool = ...) -> Union[str, List[str], Tuple[str, str], bool, Tuple[str, bool]]:
    """This command can be used to create and query container
    nodes. It is also used to perform operations on containers such as:
    Args:
        addNode (List[str]?): Specifies the list of nodes to add to container.  
                Properties: create, edit
        asset (Queryable[List[str]]?): When queried, if all the nodes in nodeList belong to the same container, returns container's name.  
                Otherwise returns empty string. This flag is functionally equivalent to the findContainer flag.  
                Properties: query
        assetMember (str?): Can be used during query in conjunction with the bindAttr flag to query  
                for the only published attributes related to the specified node within the  
                container.  
                      In query mode, this flag needs a value.  
                Properties: query
        bindAttr (Queryable[Tuple[str, str]]?): Bind a contained attribute to an unbound published name on the interface of the  
                container; returns a list of bound published names.  
                The first string specifies the node and attribute name to be  
                bound in "node.attr" format. The second string specifies the name of the  
                unbound published name. In query mode, returns a string array of the published  
                names and their corresponding attributes. The flag can also be used in query  
                mode in conjunction with the -publishName, -publishAsParent, and  
                -publishAsChild flags.  
                Properties: query, edit
        connectionList (bool?): Returns a list of the exterior connections to the container node.  
                Properties: query
        current (bool?): In create mode, specify that the newly created asset should be current.  
                In edit mode, set the selected asset as current. In query, return the  
                current asset.  
                Properties: create, query, edit
        fileName (List[str]?): Used to query for the assets associated with a given file name.  
                      In query mode, this flag needs a value.  
                Properties: query
        findContainer (List[str]?): When queried, if all the nodes in nodeList belong to the same container, returns container's name.  
                Otherwise returns empty string.  
                      In query mode, this flag needs a value.  
                Properties: query
        force (bool?): This flag can be used in conjunction with -addNode and -removeNode flags only.  
                If specified with -addNode, nodes will be disconnected from their current containers before they are added to new one.  
                If specified with -removeNode, nodes will be removed from all containers, instead of remaining in the parent container if being removed from a nested container.  
                Properties: create, edit
        includeHierarchyAbove (bool?): Used to specify that the parent hierarchy of the supplied node list should  
                also be included in the container (or deleted from the container). Hierarchy  
                inclusion will stop at  
                nodes which are members of other containers.  
                Properties: create, edit
        includeHierarchyBelow (bool?): Used to specify that the hierarchy below the supplied node list should  
                also be included in the container (or delete from the container). Hierarchy  
                inclusion will stop at  
                nodes which are members of other containers.  
                Properties: create, edit
        includeNetwork (bool?): Used to specify that the node network connected to supplied node list  
                should also be included in the container.  
                Network traversal will stop at default nodes and nodes which are members of  
                other containers.  
                Properties: create, edit
        includeNetworkDetails (Multiuse[str]?): Used to specify specific parts of the network that should be included. Valid arguments to this flag are: "channels", "sdk", "constraints", "history" and "expressions", "inputs", "outputs". The difference between this flag and the includeNetwork flag, is that it will include all connected nodes regardless of their type. Note that dag containers include their children, so they will always include constraint nodes that are parented beneath the selected objects, even when constraints are not specified as an input.  
                Properties: create, edit, multiuse
        includeShaders (bool?): Used to specify that for any shapes included, their shaders will  
                also be included in the container.  
                Properties: create, edit
        includeShapes (bool?): Used to specify that for any transforms selected, their direct child shapes  
                will be included in the container (or deleted from the container). This flag  
                is not necessary when  
                includeHierarchyBelow is used since the child shapes and all other  
                descendents will automatically be included.  
                Properties: create, edit
        includeTransform (bool?): Used to specify that for any shapes selected, their parent transform  
                will be included in the container (or deleted from the container).  
                This flag is not necessary when  
                includeHierarchyAbove is used since the parent transform and  
                all of its parents will automatically be included.  
                Properties: create, edit
        isContainer (bool?): Return true if the selected or specified node is a container node.  
                If multiple containers are queried, only the state of the first will be  
                returned.  
                Properties: query
        name (str?): Sets the name of the newly-created container.  
                Properties: create
        nodeList (bool?): When queried, returns a list of nodes in container. The list will be sorted in the order they were added to the container.  
                This will also display any reordering done with the reorderContainer command.  
                Properties: query
        nodeNamePrefix (bool?): Specifies that the name of published attributes should be of the form "node_attr".  
                Must be used with the -publishConnections/-pc flag.  
                Properties: create, edit
        parentContainer (bool?): Flag to query the parent container of a specified container.  
                Properties: query
        preview (bool?): This flag is valid in create mode only. It indicates that you do not  
                want the container to be created, instead you want to preview its contents.  
                When this flag is used, Maya will select the  
                nodes that would be put in the container if you did create the  
                container. For example you can see what would go into the container  
                with -includeNetwork, then modify your selection as desired, and do a  
                create container with the selected objects only.  
                Properties: create
        publishAndBind (Tuple[str, str]?): Publish the given name and bind the attribute to the given name.  
                First string specifies the node and attribute name in "node.attr" format.  
                Second string specifies the name it should be published with.  
                Properties: edit
        publishAsChild (Queryable[Tuple[str, str]]?): Publish contained node to the interface of the container to indicate it can  
                be a child of external nodes. The second string is the name of the published  
                node. In query mode, returns a string of the published names and the  
                corresponding nodes. If -publishName flag is used in query mode, only  
                returns the published names; if -bindAttr flag is used in query mode, only  
                returns the name of the published nodes.  
                Properties: query, edit
        publishAsParent (Queryable[Tuple[str, str]]?): Publish contained node to the interface of the container to indicate it can  
                be a parent to external nodes. The second string is the name of the published  
                node. In query mode, returns a string of array of the published names and  
                the corresponding nodes. If -publishName flag is used in query mode, only  
                returns the published names; if -bindAttr flag is used in query mode, only  
                returns the name of the published nodes.  
                Properties: query, edit
        publishAsRoot (Queryable[Tuple[str, bool]]?): Publish or unpublish a node as a root. The significance of root transform  
                node is twofold. When container-centric selection is enabled, the root  
                transform will be selected if a container node in the hierarchy below it is  
                selected in the main scene view. Also, when exporting a container proxy,  
                any published root transformation attributes such as translate, rotate or  
                scale will be hooked up to attributes on a stand-in node.  
                In query mode, returns the node that has been published as root.  
                Properties: query, edit
        publishAttr (str?): In query mode, can only be used with the -publishName(-pn) flag, and takes  
                an attribute as an argument; returns the published name of the attribute, if  
                any.  
                      In query mode, this flag needs a value.  
                Properties: query
        publishConnections (bool?): Publish all connections from nodes inside the container to nodes outside  
                the container.  
                Properties: create, edit
        publishName (Queryable[str]?): Publish a name to the interface of the container, and returns the actual name  
                published to the interface.  In query mode, returns the  
                published names for the container. If the -bindAttr flag is specified, returns  
                only the names that are bound; if the -unbindAttr flag is specified, returns  
                only the names that are not bound; if the -publishAsParent/-publishAsChild  
                flags are specified, returns only names of published parents/children.  
                if the -publishAttr is specified with an attribute argument in the "node.attr"  
                format, returns the published name for that attribute, if any.  
                Properties: query, edit
        removeContainer (bool?): Disconnects all the nodes from container and deletes container node.  
                Properties: edit
        removeNode (List[str]?): Specifies the list of nodes to remove from container. If node is a member of a nested container, it will be added to the parent container. To remove from all containers completely, use the -force flag.  
                Properties: edit
        type (Queryable[str]?): By default, a container node will be created. Alternatively, the  
                type flag can be used to indicate that a different type of container  
                should be created. At the present time, the only other valid type of  
                container node is "dagContainer".  
                Properties: create, query
        unbindAndUnpublish (str?): Unbind the given attribute (in "node.attr" format) and unpublish its associated name.  
                Unbinding a compound may trigger unbinds of its compound parents/children. So the  
                advantage of using this one flag is that it will automatically unpublish the names  
                associated with these automatic unbinds.  
                Properties: edit
        unbindAttr (Queryable[Tuple[str, str]]?): Unbind a published attribute from its published name on the interface of the  
                container, leaving an unbound published name on the interface of the  
                container; returns a list of unbound published names.  
                The first string specifies the node and attribute name to be  
                unbound in "node.attr" format, and the second string specifies the name of  
                the bound published name. In query mode, can only be used with the -publishName,  
                -publishAsParent and -publishAsChild flags.  
                Properties: query, edit
        unbindChild (str?): Unbind the node published as child, but do not remove its published name  
                from the interface of the container.  
                Properties: edit
        unbindParent (str?): Unbind the node published as parent, but do not remove its published name  
                from the interface of the container.  
                Properties: edit
        unpublishChild (str?): Unpublish node published as child from the interface of the container  
                Properties: edit
        unpublishName (str?): Unpublish an unbound name from the interface of the container.  
                Properties: edit
        unpublishParent (str?): Unpublish node published as parent from the interface of the container  
                Properties: edit
        unsortedOrder (bool?): This flag has no effect on the operation of the container command (OBSOLETE).  
                Properties: query

    Returns:
        str: Name of the node created.

    Example:
    """

