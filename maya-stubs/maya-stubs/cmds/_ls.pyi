from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ls(*args: str, absoluteName: bool = ..., allPaths: bool = ..., assemblies: bool = ..., cameras: bool = ..., containerType: Multiuse[str] = ..., containers: bool = ..., dagObjects: bool = ..., defaultNodes: bool = ..., dependencyNodes: bool = ..., exactType: Multiuse[str] = ..., excludeType: Multiuse[str] = ..., flatten: bool = ..., geometry: bool = ..., ghost: bool = ..., head: int = ..., hilite: bool = ..., intermediateObjects: bool = ..., invisible: bool = ..., leaf: bool = ..., lights: bool = ..., live: bool = ..., lockedNodes: bool = ..., long: bool = ..., materials: bool = ..., modified: bool = ..., noIntermediate: bool = ..., nodeTypes: bool = ..., objectsOnly: bool = ..., orderedSelection: bool = ..., partitions: bool = ..., persistentNodes: bool = ..., planes: bool = ..., preSelectHilite: bool = ..., readOnly: bool = ..., recursive: bool = ..., referencedNodes: bool = ..., references: bool = ..., renderGlobals: bool = ..., renderQualities: bool = ..., renderResolutions: bool = ..., renderSetups: bool = ..., selection: bool = ..., sets: bool = ..., shapes: bool = ..., shortNames: bool = ..., showNamespace: bool = ..., showType: bool = ..., tail: int = ..., templated: bool = ..., textures: bool = ..., transforms: bool = ..., type: Multiuse[str] = ..., ufeObjects: bool = ..., undeletable: bool = ..., untemplated: bool = ..., uuid: bool = ..., visible: bool = ...) -> List[str]:
    """Thecommand returns the names (and
    optionally the type names) of objects in the scene.The most common use ofis to filter or
    match objects based on their name (using wildcards) or based on their
    type.
    By defaultwill match any object in the
    scene but it can also be used to filter or list the selected
    objects when used in conjunction with the -selection flag.If type names are requested, using the showType flag, they
    will be interleaved with object names so the result will be
    pairs ofvalues.Internal nodes (for example itemFilter nodes) are typically filtered
    so that only scene objects are returned. However, using a wildcard
    will cause all the nodes matching the wild card to show up, including
    internal nodes.  For example,will list all
    nodes whether internal or not.Use the syntax "::" to denote a recursive namespace search when listing nodes.
    For example,would match objects named
    "pSphere1" in any namespace, at any depth.would match any node in namespace "ns" or children namespaces.When Maya is in relativeNames mode, thecommand
    will return namesto the current namespace andwill list from the the current namespace.
    For more details, please refer to theflag of thecommand.The command may also be passed node UUIDs instead of names/paths, and
    can return UUIDs instead of names via the -uuid flag.
    Args:
        absoluteName (bool?): This flag can be used in conjunction with the showNamespace flag to specify  
                that the namespace(s) returned by the command be in absolute namespace format.  
                The absolute name of the namespace is a full namespace path, starting from the root namespace ":"  
                and including all parent namespaces.  For example ":ns:ball" is an absolute namespace  
                name while "ns:ball" is not.  
                The absolute namespace name is invariant and is not affected by the current namespace or  
                relative namespace modes.  
                Properties: create
        allPaths (bool?): List all paths to nodes in DAG. This flag only works  
                if -dag is also specified or if an object name is  
                supplied.  
                Properties: create
        assemblies (bool?): List top level transform Dag objects  
                Properties: create
        cameras (bool?): List camera shapes.  
                Properties: create
        containerType (Multiuse[str]?): List containers with the specified user-defined type.  
                 This flag cannot be used in conjunction with the type or exactType flag.  
                Properties: create, multiuse
        containers (bool?): List containers. Includes both standard containers as well as other types of  
                containers such as dagContainers.  
                Properties: create
        dagObjects (bool?): List Dag objects of any type. If object name arguments are  
                passed to the command then this flag will list all Dag objects  
                below the specified object(s).  
                Properties: create
        defaultNodes (bool?): Returns default nodes.  
                A default node is one that Maya creates automatically and does not get  
                saved out with the scene, although some of its attribute values may.  
                Properties: create
        dependencyNodes (bool?): List dependency nodes. (including Dag objects)  
                Properties: create
        exactType (Multiuse[str]?): List all objects of the specified type, but not objects that are  
                descendents of that type. This flag can appear  
                multiple times on the command line. Note: the type passed to  
                this flag is the same type name returned from the showType  
                flag.  
                 This flag cannot be used in conjunction with the type or excludeType flag.  
                Properties: create, multiuse
        excludeType (Multiuse[str]?): List all objects that are not of the specified type.  
                This flag can appear multiple times on the command line. Note: the type passed to  
                this flag is the same type name returned from the showType flag.  
                 This flag cannot be used in conjunction with the type or exactType flag.  
                Properties: create, multiuse
        flatten (bool?): Flattens the returned list of objects so that each component  
                is identified individually.  
                Properties: create
        geometry (bool?): List geometric Dag objects.  
                Properties: create
        ghost (bool?): List ghosting objects.  
                Properties: create
        head (int?): This flag  specifies the maximum number of elements to be  
                returned from the beginning of the list of items.  
                Note: each type flag will return at most this many items so  
                if multiple type flags are specified then the number of items  
                returned can be greater than this amount.  
                Properties: create
        hilite (bool?): List objects that are currently hilited for component selection.  
                Properties: create
        intermediateObjects (bool?): List only intermediate dag nodes.  
                Properties: create
        invisible (bool?): List only invisible dag nodes.  
                Properties: create
        leaf (bool?): List all leaf nodes in Dag. This flag is a modifier and must  
                be used in conjunction with the -dag flag.  
                Properties: create
        lights (bool?): List light shapes.  
                Properties: create
        live (bool?): List objects that are currently live.  
                Properties: create
        lockedNodes (bool?): Returns locked nodes, which cannot be deleted or renamed. However, their status may change.  
                Properties: create
        long (bool?): Return full path names for Dag objects. By default the  
                shortest unique name is returned.  
                Properties: create
        materials (bool?): List materials or shading groups.  
                Properties: create
        modified (bool?): When this flag is set, only nodes modified since the last save will be returned.  
                Properties: create
        noIntermediate (bool?): List only non intermediate dag nodes.  
                Properties: create
        nodeTypes (bool?): Lists all registered node types.  
                Properties: create
        objectsOnly (bool?): When this flag is set only object names will be returned and  
                components/attributes will be ignored.  
                Properties: create
        orderedSelection (bool?): List objects and components that are currently selected in their order of selection.  This flag depends  
                on the value of the -tso/trackSelectionOrder flag of the selectPref command.  If that flag is not  
                enabled than this flag will return the same thing as the -sl/selection flag would.  
                Properties: create
        partitions (bool?): List partitions.  
                Properties: create
        persistentNodes (bool?): Returns persistent nodes, which are nodes that stay in the Maya session after a file > new.  
                These are a special class of default nodes that do not get reset on file > new.  
                Ex: itemFilter and selectionListOperator nodes.  
                Properties: create
        planes (bool?): List construction plane shapes.  
                Properties: create
        preSelectHilite (bool?): List components that are currently hilited for pre-selection.  
                Properties: create
        readOnly (bool?): Returns referenced nodes. Referenced nodes are read only.  
                NOTE: Obsolete. Please use "-referencedNodes".  
                Properties: create
        recursive (bool?): When set to true, this command will look for name matches  
                in all namespaces. When set to false, this command will only look  
                for matches in namespaces that are requested (e.g. by specifying  
                a name containing the ':'... "ns1. pSphere1").  
                Properties: create
        referencedNodes (bool?): Returns referenced nodes. Referenced nodes are read only.  
                Properties: create
        references (bool?): List references associated with files. Excludes special reference  
                nodes such as the sharedReferenceNode and unknown reference nodes.  
                Properties: create
        renderGlobals (bool?): List render globals.  
                Properties: create
        renderQualities (bool?): List named render qualities.  
                Properties: create
        renderResolutions (bool?): List render resolutions.  
                Properties: create
        renderSetups (bool?): Alias for -renderGlobals.  
                Properties: create
        selection (bool?): List objects that are currently selected.  
                Properties: create
        sets (bool?): List sets.  
                Properties: create
        shapes (bool?): List shape objects.  
                Properties: create
        shortNames (bool?): Return short attribute names. By default long attribute names  
                are returned.  
                Properties: create
        showNamespace (bool?): Show the namespace of each object after the object name.  
                 This flag cannot be used in conjunction with the showType flag.  
                Properties: create
        showType (bool?): List the type of each object after its name.  
                Properties: create
        tail (int?): This flag specifies the maximum number of elements to be  
                returned from the end of the list of items.  
                Note: each    type flag will return at most this many items so  
                if multiple type flags are specified then the number of items  
                returned can be greater than this amount  
                Properties: create
        templated (bool?): List only templated dag nodes.  
                Properties: create
        textures (bool?): List textures.  
                Properties: create
        transforms (bool?): List transform objects.  
                Properties: create
        type (Multiuse[str]?): List all objects of the specified type. This flag can appear  
                multiple times on the command line. Note: the type passed to  
                this flag is the same type name returned from the showType  
                flag. Note: some selection items in Maya do not have a specific  
                object/data type associated with them and will return "untyped"  
                when listed with this flag.  
                 This flag cannot be used in conjunction with the exactType or excludeType flag.  
                Properties: create, multiuse
        ufeObjects (bool?): When used in conjunction with the -sl/selection flag, will return objects that are  
                defined through the UFE interface as well as native Maya objects.  
                Properties: create
        undeletable (bool?): Returns nodes that cannot be deleted (which includes locked nodes). These nodes also cannot be renamed.  
                Properties: create
        untemplated (bool?): List only un-templated dag nodes.  
                Properties: create
        uuid (bool?): Return node UUIDs instead of names.  
                Note that there are no "UUID paths" - combining this  
                flag with e.g. the -long flag will not result in a path  
                formed of node UUIDs.  
                Properties: create
        visible (bool?): List only visible dag nodes.  
                Properties: create

    Returns:
        List[str]: Command result

    Example:
    """

