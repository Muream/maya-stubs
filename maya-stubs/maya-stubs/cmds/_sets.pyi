from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sets(*args: str, edit: bool = ..., query: bool = ..., addElement: str = ..., afterFilters: bool = ..., anyMember: str = ..., clear: str = ..., color: Queryable[int] = ..., copy: str = ..., edges: bool = ..., editPoints: bool = ..., empty: bool = ..., facets: bool = ..., flatten: str = ..., forceElement: str = ..., include: str = ..., intersection: str = ..., isIntersecting: str = ..., isMember: str = ..., layer: bool = ..., name: str = ..., noIntermediate: bool = ..., noSurfaceShader: bool = ..., noWarnings: bool = ..., nodesOnly: bool = ..., remove: str = ..., renderable: bool = ..., size: bool = ..., split: str = ..., subtract: str = ..., text: Queryable[str] = ..., union: str = ..., vertices: bool = ...) -> Union[str, List[str], bool, int]:
    """This command is used to create a set, query some state of
    a set, or perform operations to update the membership of a set.
    A set is a logical grouping of an arbitrary collection of objects,
    attributes, or components of objects. Sets are dependency nodes.
    Connections from objects to a set define membership in the set.Sets are used throughout Maya in a multitude of ways. They are used
    to define an association of material properties to objects, to define
    an association of lights to objects, to define a bookmark or named
    collection of objects, to define a character, and to define the
    components to be deformed by some deformation operation.Sets can be connected to any number of partitions. A partition is
    a node which enforces mutual exclusivity amoung the sets in the
    partition. That is, if an object is in a
    set which is in a partition, that object cannot be a member of any
    other set that is in the partition.Without any flags, thecommand will create a set with a
    default name of "set#" (where # is an integer). If no items are
    specified on the command line, the currently selected items are added
    to the set. The -em/empty flag can be used to create an empty
    set and not have the selected items added to the set.Sets can be created to have certain restrictions on membership. There
    can be "renderable" sets which only allow renderable objects (such as
    nurbs geometry or polymesh faces) to be members of the set. There can
    also be vertex (or control point), edit point, edge, or face sets
    which only allow those types of components to be members of a set.
    Note that for these sets, if an object with a valid type of component
    is to be added to a set, the components of the object are
    added to the set instead.Sets can have an associated color which is only of use
    when creating vertex sets. The color can be one of the eight user
    defined colors defined in the color preferences. This color can
    be used, for example to distinguish which vertices are being deformed
    by a particular deformation.Objects, components, or attributes can be added to a set using one of
    three flags. The -add/addElement flag will add the objects to a set as
    long as this won't break any mutual exclusivity constraints. If there
    are any items which can't be added, the command will fail. The
    -in/include flag will only add those items which can be added and
    warn of those which can't. The -fe/forceElement flag will add all the
    items to the set but will also remove any of those items that are in
    any other set which is in the same partition as the set.There are several operations on sets that can be performed with thecommand. Membership can be queried. Tests for whether
    an item is in a set or whether two sets share the same item
    can be performed. Also, the union, intersection and
    difference of sets can be performed which returns a list of members
    of the sets which are a result of the operation.
    Args:
        addElement (str?): Adds the list of items to the given set.  If some of the  
                items cannot be added to the set because they are in another  
                set which is in the same partition as the set to edit, the  
                command will fail.  
                Properties: edit
        afterFilters (bool?): Default state is false. This flag is valid in edit mode only.  
                This flag is for use on sets that are acted on by deformers  
                such as sculpt, lattice, blendShape. The default edit mode  
                is to edit the membership of the group acted on by the deformer.  
                If you want to edit the group but not change the membership of  
                the deformer, set the flag to true.  
                Properties: edit
        anyMember (str?): An operation which tests whether any of the given items  
                are members of the given set.  
                Properties: create
        clear (str?): An operation which removes all items from the given set making  
                the set empty.  
                Properties: edit
        color (Queryable[int]?): Defines the hilite color of the set. Must be a value in  
                range [-1, 7] (one of the user defined colors).  -1 marks the  
                color has being undefined and therefore not having any affect.  
                Only the vertices of a vertex set will be displayed in this  
                color.  
                Properties: create, query, edit
        copy (str?): Copies the members of the given set to a new set.  
                This flag is for use in creation mode only.  
                Properties: create
        edges (bool?): Indicates the new set can contain edges only.  
                This flag is for use in creation or query mode only.  
                The default value is false.  
                Properties: create, query
        editPoints (bool?): Indicates the new set can contain editPoints only.  
                This flag is for use in creation or query mode only.  
                The default value is false.  
                Properties: create, query
        empty (bool?): Indicates that the set to be created should be empty. That is,  
                it ignores any arguments identifying objects to be added to  
                the set. This flag is only valid for operations that create a new set.  
                Properties: create
        facets (bool?): Indicates the new set can contain facets only.  
                This flag is for use in creation or query mode only.  
                The default value is false.  
                Properties: create, query
        flatten (str?): An operation that flattens the structure of the given set.  
                That is, any sets contained by the given set will be replaced by  
                its members so that the set no longer contains other sets but  
                contains the other sets' members.  
                Properties: edit
        forceElement (str?): For use in edit mode only. Forces addition of the items  
                to the set. If the items are in another set which is in the  
                same partition as the given set, the items will be removed  
                from the other set in order to keep the sets in the partition  
                mutually exclusive with respect to membership.  
                Properties: edit
        include (str?): Adds the list of items to the given set.  If some of the  
                items cannot be added to the set, a warning will be issued.  
                This is a less strict version of the -add/addElement operation.  
                Properties: edit
        intersection (str?): An operation that returns a list of items which are members of  
                all the sets in the list.  
                Properties: create
        isIntersecting (str?): An operation which tests whether the sets in the list have  
                common members.  
                Properties: create
        isMember (str?): An operation which tests whether all the given items  
                are members of the given set.  
                Properties: create
        layer (bool?): OBSOLETE. DO NOT USE.  
                Properties: create
        name (str?): Assigns string as the name for a new set. This flag is  
                only valid for operations that create a new set.  
                Properties: create
        noIntermediate (bool?): Excludes intermediate objects when querying set members or  
                using the subtract, union, itersection, or isIntersecting  
                flags.  
                Properties: create, query
        noSurfaceShader (bool?): If set is renderable, do not connect it to the default surface  
                shader.  Flag has no meaning or effect for non renderable sets.  
                This flag is for use in creation mode only.  
                The default value is false.  
                Properties: create
        noWarnings (bool?): Indicates that warning messages should not be reported such  
                as when trying to add an invalid item to a set. (used by UI)  
                Properties: create
        nodesOnly (bool?): This flag is usable with the -q/query flag but is ignored if  
                used with another queryable flags. This flag modifies the results  
                of the set membership query such that  
                when there are attributes (e.g. sphere1.tx) or components of  
                nodes included in the set, only the nodes will be listed.  
                Each node will only be listed once, even if more than one attribute  
                or component of the node exists in the set.  
                Properties: query
        remove (str?): Removes the list of items from the given set.  
                Properties: edit
        renderable (bool?): This flag indicates that a special type of set should  
                be created. This type of set (shadingEngine as opposed to  
                objectSet) has certain restrictions on its membership in that  
                it can only contain renderable elements such as lights and  
                geometry. These sets are referred to as shading groups and  
                are automatically connected to the "renderPartition" node when  
                created (to ensure mutual exclusivity of the set's members with  
                the other sets in the partition).  
                This flag is for use in creation or query mode only.  
                The default value is false which means a normal set is  
                created.  
                Properties: create, query
        size (bool?): Use the size flag to query the length of the set.  
                Properties: query
        split (str?): Produces a new set with the list of items and removes  
                each item in the list of items from the given set.  
                Properties: create
        subtract (str?): An operation between two sets which returns the members of the  
                first set that are not in the second set.  
                Properties: create
        text (Queryable[str]?): Defines an annotation string to be stored with the set.  
                Properties: create, query, edit
        union (str?): An operation that returns a list of all the members of all sets  
                listed.  
                Properties: create
        vertices (bool?): Indicates the new set can contain vertices only.  
                This flag is for use in creation or query mode only.  
                The default value is false.  
                Properties: create, query

    Returns:
        str: For creation operations (name of the set that was created or edited)
        List[str]: For query operation (names of items in the set)
        bool: For isIntersecting and isMember operations

    Example:
    """

