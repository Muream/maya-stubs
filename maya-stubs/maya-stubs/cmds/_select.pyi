from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def select(*args: str, add: bool = ..., addFirst: bool = ..., all: bool = ..., allDagObjects: bool = ..., allDependencyNodes: bool = ..., clear: bool = ..., containerCentric: bool = ..., deselect: bool = ..., hierarchy: bool = ..., noExpand: bool = ..., replace: bool = ..., symmetry: bool = ..., symmetrySide: int = ..., toggle: bool = ..., visible: bool = ...) -> bool:
    """This command is used to put objects onto or off of the active list.
    If none of the five flags [-add, -af, -r, -d, -tgl] are specified, the
    default is to replace the objects on the active list with the
    given list of objects.When selecting a set as in "select set1", the behaviour is for all
    the members of the set to become selected instead of the set itself.
    If you want to select a set, the "-ne/noExpand" flag must be used.With the advent of namespaces, selection by name may be
    confusing.  To clarify, without a qualified namespace, name
    lookup is limited to objects in the root namespace ":". There
    are really two parts of a name: the namespace and the name
    itself which is unique within the namespace. If you want to
    select objects in a specific namespace, you need to include
    the namespace separator ":".For example, 'select -r "foo*"' is trying to look for an
    object with the "foo" prefix in the root namespace. It is not
    trying to look for all objects in the namespace with the "foo"
    prefix. If you want to select all objects in a namespace
    (foo), use 'select "foo:*"'.Note: When the application starts up, there are several dependency nodes
    created by the system which must exist. These objects are not deletable
    but are selectable.  All objects (dag and dependency nodes) in the scene
    can be obtained using the "ls" command without any arguments. When using
    the "-all", "adn/allDependencyNodes" or "-ado/allDagObjects" flags, only
    the deletable objects are selected.  The non deletable object can still
    be selected by explicitly specifying their name as in "select time1;".
    Args:
        add (bool?): Indicates that the specified items should be  
                added to the active list without removing existing  
                items from the active list.  
                Properties: create
        addFirst (bool?): Indicates that the specified items should be  
                added to the front of the active list without  
                removing existing items from the active list.  
                Properties: create
        all (bool?): Indicates that all deletable root level dag objects  
                and all deletable non-dag dependency nodes should be  
                selected.  
                Properties: create
        allDagObjects (bool?): Indicates that all deletable root level dag objects  
                should be selected.  
                Properties: create
        allDependencyNodes (bool?): Indicates that all deletable dependency nodes  
                including all deletable dag objects should be selected.  
                Properties: create
        clear (bool?): Clears the active list.  This is more efficient than  
                "select -d;".  Also "select -d;" will not remove sets  
                from the active list unless the "-ne" flag is also  
                specified.  
                Properties: create
        containerCentric (bool?): Specifies that the same selection rules as apply to selection in the main  
                viewport will also be applied to the select command. In particular, if  
                the specified objects are members of a black-boxed container and are not  
                published as nodes, Maya will not select them. Instead, their first parent  
                valid for selection will be selected.  
                Properties: create
        deselect (bool?): Indicates that the specified items should  
                be removed from the active list if they are on the  
                active list.  
                Properties: create
        hierarchy (bool?): Indicates that all children, grandchildren, ...  
                of the specified dag objects should also be selected.  
                Properties: create
        noExpand (bool?): Indicates that any set which is among the specified  
                items should not be expanded to its list of members.  
                This allows sets to be selected as opposed to  
                the members of sets which is the default behaviour.  
                Properties: create
        replace (bool?): Indicates that the specified items should  
                replace the existing items on the active list.  
                Properties: create
        symmetry (bool?): Specifies that components should be selected symmetrically using the  
                current symmetricModelling command settings. If symmetric modeling  
                is not enabled then this flag has no effect.  
                Properties: create
        symmetrySide (int?): Indicates that components involved in the current symmetry  
                object should be selected, according to the supplied parameter.  
                Valid values for the parameter are:  
                -1. Select components in the unsymmetrical region.  
                0. Select components on the symmetry seam.  
                1. Select components on side 1.  
                2. Select components on side 2.  
                If symmetric modeling is not enabled then this flag has no effect.  
                Note: currently only works for topological symmetry.  
                Properties: create
        toggle (bool?): Indicates that those items on the given list which  
                are on the active list should be removed from the active  
                list and those items on the given list which are not on  
                the active list should be added to the active list.  
                Properties: create
        visible (bool?): Indicates that of the specified items only those  
                that are visible should be affected.  
                Properties: create

    Returns:
        bool:

    Example:
    """

