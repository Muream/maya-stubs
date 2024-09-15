from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sculptTarget(*args: str, edit: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., exclusive: str = ..., frontOfChain: bool = ..., geometry: Multiuse[str] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., inbetweenWeight: float = ..., includeHiddenSelections: bool = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., regenerate: bool = ..., remove: Multiuse[bool] = ..., selectedComponents: bool = ..., snapshot: int = ..., split: bool = ..., target: int = ..., useComponentTags: bool = ...) -> bool:
    """This command is used to specify the blend shape target to be
    modified by the sculpting tools and transform manipulators.
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
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...
        exclusive (str?): Puts the deformation set in a deform partition.  
                Properties: create
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
        geometry (Multiuse[str]?): The specified object will be added to the list of  
                objects being deformed by this deformer object, unless  
                the -rm flag is also specified. When queried, this flag  
                returns string string string ...  
                Properties: edit, multiuse
        geometryIndices (bool?): Complements the -geometry flag in query mode. Returns  
                the multi index of each geometry.
        ignoreSelected (bool?): Tells the command to not deform objects on the  
                current selection list  
                Properties: create
        inbetweenWeight (float?): Specifies the in between target weight of the blend shape node that will be  
                made editable by the sculpting and transform tools.  
                Properties: edit
        includeHiddenSelections (bool?): Apply the deformer to any visible and hidden objects in the selection list.  
                Default is false.  
                Properties: create
        name (str?): Used to specify the name of the node being created.  
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
        regenerate (bool?): When this flag is specified a new shape is created for the specified  
                blend shape target, if the shape does not already exist.  
                The name of the new shape is returned.  
                Properties: edit
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.
        snapshot (int?): This flag should only be used internally to add in-between target.  
                When this flag is specified a snapshot of the shape will be  
                taken for the specified in-between target when it does not  
                exist yet.  
                This flag specifies the base shape index and must be used with the  
                -target and -inbetweenWeight flags, which specify the in-between  
                target.  
                Properties: edit
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        target (int?): Specifies the target index of the blend shape node that will be  
                made editable by the sculpting and transform tools.  
                Properties: edit
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create

    Returns:
        bool:

    Example:
    """

