from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sculpt(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., dropoffDistance: Queryable[float] = ..., dropoffType: Queryable[str] = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., groupWithLocator: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., insideMode: Queryable[str] = ..., maxDisplacement: Queryable[float] = ..., mode: Queryable[str] = ..., name: str = ..., objectCentered: bool = ..., parallel: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., sculptTool: str = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ...) -> Union[List[str], bool, float, str, Multiuse[str]]:
    """This command creates/edits/queries a sculpt object deformer. By default
    for creation mode an implicit sphere will be used as the sculpting
    object if no sculpt tool is specified. The name of the created/edited
    object is returned.
    Args:
        after (bool?): If the default behavior for insertion/appending into/onto  
                the existing chain is not the desired behavior then this flag  
                can be used to force the command to place the deformer  
                node after the selected node in the chain even if  
                a new geometry shape has to be created in order to do so.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        afterReference (bool?): The -afterReference flag is used to specify deformer ordering in a hybrid way that  
                choses between -before and -after automatically. If the geometry being  
                deformed is referenced then the -after mode is used when adding the new deformer,  
                otherwise the -before mode is used. The net effect when using -afterReference to build  
                deformer chains is that internal shape nodes in the deformer chain will only  
                appear at reference file boundaries, leading to lightweight deformer networks that  
                may be more amicable to reference swapping.  
                Properties: create, edit
        before (bool?): If the default behavior for insertion/appending into/onto  
                the existing chain is not the desired behavior then this flag  
                can be used to force the command to place the deformer  
                node before the selected node in the chain even if  
                a new geometry shape has to be created in order to do so.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        components (bool?): Returns the components used by the deformer  
                Properties: query
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        dropoffDistance (Queryable[float]?): Specifies the distance from the surface of the sculpt  
                object at which the sculpt object produces no deformation  
                effect. Default is 1.0. When queried, this flag returns a float.  
                Properties: create, query, edit
        dropoffType (Queryable[str]?): Specifies how the deformation effect drops off from  
                maximum effect at the surface of the sculpt object to no effect  
                at dropoff distance limit. Valid values are: linear | none.  
                Default is linear. When queried, this flag returns a string.  
                Properties: create, query, edit
        exclusive (Queryable[str]?): Puts the deformation set in a deform partition.  
                Properties: create, query
        frontOfChain (bool?): This command is used to specify that the new deformer  
                node should be placed ahead (upstream) of existing deformer  
                and skin nodes in the shape's history (but not ahead of  
                existing tweak nodes). The input to the  
                deformer will be the upstream shape rather than the visible  
                downstream shape, so the behavior of this flag is the most  
                intuitive if the downstream deformers are in their reset  
                (hasNoEffect) position when the new deformer is added.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        geometry (Queryable[Multiuse[str]]?): The specified object will be added to the list of  
                objects being deformed by this deformer object, unless  
                the -rm flag is also specified. When queried, this flag  
                returns string string string ...  
                Properties: query, edit, multiuse
        geometryIndices (bool?): Complements the -geometry flag in query mode. Returns  
                the multi index of each geometry.  
                Properties: query
        groupWithLocator (bool?): Groups the sculptor and its locator together under  
                a single transform. Default is off.  
                Properties: create
        ignoreSelected (bool?): Tells the command to not deform objects on the  
                current selection list  
                Properties: create
        includeHiddenSelections (bool?): Apply the deformer to any visible and hidden objects in the selection list.  
                Default is false.  
                Properties: create
        insideMode (Queryable[str]?): Specifies how the deformation algorithm deals with  
                points that are inside the sculpting primitve. The choices are:  
                ring | even. The default is even. When queried, this flag  
                returns a string. Ring mode will tend to produce a contour like  
                ring of points around the sculpt object as it passes through an  
                object while even mode will try to spread the points out as  
                evenly as possible across the surface of the sculpt object.  
                Properties: create, query, edit
        maxDisplacement (Queryable[float]?): Defines the maximum amount the sculpt object may move  
                a point on an object which it is deforming. Default is 1.0. When  
                queried, this flag returns a float.  
                Properties: create, query, edit
        mode (Queryable[str]?): Specifies which deformation algorithm the sculpt  
                object should use. The choices are: flip | project | stretch.  
                The default is stretch. When queried, this flag returns a string.  
                Properties: create, query, edit
        name (str?): Used to specify the name of the node being created.  
                Properties: create
        objectCentered (bool?): Places the sculpt and locator in the center of the  
                bounding box of the selected object(s) or  
                components. Default is off which centers the  
                sculptor and locator at the origin.  
                Properties: create
        parallel (bool?): Inserts the new deformer in a parallel chain to any existing deformers in  
                the history of the object. A blendShape is inserted to blend the parallel  
                results together.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        prune (bool?): Removes any points not being deformed by the deformer in  
                its current configuration from the deformer set.  
                Properties: edit
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        sculptTool (str?): Use the specified NURBS object as the sculpt tool instead  
                of the default implicit sphere.  
                Properties: create
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create

    Returns:
        List[str]: Sculpt algorithm node name, sculpt sphere name, and sculpt stretch origin name

    Example:
    """

