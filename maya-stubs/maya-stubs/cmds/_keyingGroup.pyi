from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def keyingGroup(*args: str, edit: bool = ..., query: bool = ..., activator: Queryable[str] = ..., addElement: str = ..., afterFilters: bool = ..., anyMember: str = ..., category: Queryable[str] = ..., clear: str = ..., color: Queryable[int] = ..., copy: str = ..., edges: bool = ..., editPoints: bool = ..., empty: bool = ..., excludeDynamic: bool = ..., excludeRotate: bool = ..., excludeScale: bool = ..., excludeTranslate: bool = ..., excludeVisibility: bool = ..., facets: bool = ..., flatten: str = ..., forceElement: str = ..., include: str = ..., intersection: str = ..., isIntersecting: str = ..., isMember: str = ..., layer: bool = ..., minimizeRotation: bool = ..., name: str = ..., noIntermediate: bool = ..., noSurfaceShader: bool = ..., noWarnings: bool = ..., nodesOnly: bool = ..., remove: str = ..., removeActivator: str = ..., renderable: bool = ..., setActiveFilter: Queryable[str] = ..., size: bool = ..., split: str = ..., subtract: str = ..., text: Queryable[str] = ..., union: str = ..., vertices: bool = ...) -> Union[str, List[str], bool, int]:
    """This command is used to manage the membership of a keying group.  Keying
    groups allow users to effectively manage related keyframe data, allowing
    keys on attributes in the keying group to be set and edited as a single
    entity.
    Args:
        activator (Queryable[str]?): Sets the selected node(s) as activators for the given keying group.  
                In query mode, returns list of objects that activate the given keying group  
                Properties: query, edit
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
        category (Queryable[str]?): Sets the keying group's category. This is what the global, active keying  
                group filter will use to match.  
                Properties: create, query, edit
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
        excludeDynamic (bool?): When creating the keying group, exclude dynamic attributes.  
                Properties: create
        excludeRotate (bool?): When creating the keying group, exclude rotate attributes from  
                transform-type nodes.  
                Properties: create
        excludeScale (bool?): When creating the keying group, exclude scale attributes from  
                transform-type nodes.  
                Properties: create
        excludeTranslate (bool?): When creating the keying group, exclude translate attributes from  
                transform-type nodes. For example, if your keying group contains  
                joints only, perhaps you only want to include rotations in the  
                keying group.  
                Properties: create
        excludeVisibility (bool?): When creating the keying group, exclude visibility attribute from  
                transform-type nodes.  
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
        minimizeRotation (bool?): This flag only affects the attribute contained in the immediate keyingGroup.  
                It does not affect attributes in sub-keyingGroups.  
                Those will need to set minimizeRotation on their respective keyingGroups  
                Properties: create, query, edit
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
        removeActivator (str?): Removes the selected node(s) as activators for the given keying group.  
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
        setActiveFilter (Queryable[str]?): Sets the global, active keying group filter, which will affect activation of  
                keying groups. Only keying groups with categories that match the filter will be  
                activated. If the setActiveFilter is set to "NoKeyingGroups", keying groups will  
                not be activated at all. If the setActiveFilter is set to "AllKeyingGroups", we  
                will activate any keying group rather than just those with matching categories.  
                Properties: create, query, edit
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
        str: For creation operations (name of the keying group that was created or edited)
        List[str]: For query operation (names of items in the keying group)
        bool: For isMember operation

    Example:
    """

