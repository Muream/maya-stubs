from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def deltaMush(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., envelope: Queryable[float] = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., inwardConstraint: Queryable[float] = ..., name: str = ..., outwardConstraint: Queryable[float] = ..., parallel: bool = ..., pinBorderVertices: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., selectedComponents: bool = ..., smoothingIterations: Queryable[int] = ..., smoothingStep: Queryable[float] = ..., split: bool = ..., useComponentTags: bool = ...) -> Union[str, bool, float, Multiuse[str], int]:
    """This command is used to create, edit and query deltaMush nodes.
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
        envelope (Queryable[float]?): Envelope of the delta mush node. The envelope determines the percent of  
                deformation. Value is clamped to [0, 1] range.  
                Default is 1.  
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
        ignoreSelected (bool?): Tells the command to not deform objects on the  
                current selection list  
                Properties: create
        includeHiddenSelections (bool?): Apply the deformer to any visible and hidden objects in the selection list.  
                Default is false.  
                Properties: create
        inwardConstraint (Queryable[float]?): Constrains the movement of the vertex to not move inward from the input  
                deforming shape to preserve the contour. Value is in the [0,1] range.  
                Default is 0.0.  
                Properties: create, query, edit
        name (str?): Used to specify the name of the node being created.  
                Properties: create
        outwardConstraint (Queryable[float]?): Constrains the movement of the vertex to not move outward from the input  
                deforming shape to preserve the contour. Value is in the [0,1] range.  
                Default is 0.0.  
                Properties: create, query, edit
        parallel (bool?): Inserts the new deformer in a parallel chain to any existing deformers in  
                the history of the object. A blendShape is inserted to blend the parallel  
                results together.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        pinBorderVertices (bool?): If enabled, vertices on mesh borders will be pinned to their current  
                position during smoothing. Default is true.  
                Properties: create, query, edit
        prune (bool?): Removes any points not being deformed by the deformer in  
                its current configuration from the deformer set.  
                Properties: edit
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        smoothingIterations (Queryable[int]?): Number of smoothing iterations performed by the delta mush node.  
                Default is 10.  
                Properties: create, query, edit
        smoothingStep (Queryable[float]?): Step amount used per smoothing iteration. Value is clamped to [0, 1] range.  
                A higher value may lead to instabilities but converges faster compared  
                to a lower value. Default is 0.5.  
                Properties: create, query, edit
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
        str: Delta mush deformer node name

    Example:
    """

