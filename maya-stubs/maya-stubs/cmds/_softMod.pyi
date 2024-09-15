from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def softMod(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., bindState: bool = ..., components: bool = ..., curveInterpolation: Multiuse[int] = ..., curvePoint: Multiuse[float] = ..., curveValue: Multiuse[float] = ..., deformerTools: bool = ..., envelope: Queryable[float] = ..., exclusive: Queryable[str] = ..., falloffAroundSelection: bool = ..., falloffBasedOnX: bool = ..., falloffBasedOnY: bool = ..., falloffBasedOnZ: bool = ..., falloffCenter: Tuple[float, float, float] = ..., falloffMasking: bool = ..., falloffMode: int = ..., falloffRadius: float = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., relative: bool = ..., remove: Multiuse[bool] = ..., resetGeometry: bool = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., weightedNode: Queryable[Tuple[str, str]] = ...) -> Union[str, bool, float, Multiuse[str], Tuple[str, str]]:
    """The softMod command creates a softMod or edits the membership of
    an existing softMod. The command returns the name of the softMod
    node upon creation of a new softMod.
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
        bindState (bool?): Specifying this flag adds in a compensation to ensure  
                the softModed objects preserve their spatial position  
                when softModed. This is required to prevent the geometry  
                from jumping at the time the softMod is created  
                in situations when the  
                softMod transforms at softMod time are not identity.  
                Properties: create
        components (bool?): Returns the components used by the deformer  
                Properties: query
        curveInterpolation (Multiuse[int]?): Ramp interpolation corresponding to the specified curvePoint position.  
                Integer values of 0. 3 are valid, corresponding to "none", "linear", "smooth"  
                and "spline" respectively.  
                This flag may only be used in conjunction with the curvePoint and curveValue  
                flag.  
                Properties: create, multiuse
        curvePoint (Multiuse[float]?): Position of ramp value on normalized 0. 1 scale.  
                This flag may only be used in conjunction with the curveInterpolation and  
                curveValue flags.  
                Properties: create, multiuse
        curveValue (Multiuse[float]?): Ramp value corresponding to the specified curvePoint position. This flag  
                may only be used in conjunction with the curveInterpolation and curvePoint  
                flags.  
                Properties: create, multiuse
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        envelope (Queryable[float]?): Set the envelope value for the deformer. Default is 1.0  
                Properties: create, query, edit
        exclusive (Queryable[str]?): Puts the deformation set in a deform partition.  
                Properties: create, query
        falloffAroundSelection (bool?): Falloff will be calculated around any selected components  
                Properties: create
        falloffBasedOnX (bool?): Falloff will be calculated using the X component.  
                Properties: create
        falloffBasedOnY (bool?): Falloff will be calculated using the Y component.  
                Properties: create
        falloffBasedOnZ (bool?): Falloff will be calculated using the Z component.  
                Properties: create
        falloffCenter (Tuple[float, float, float]?): Set the falloff center point of the softMod.  
                Properties: create
        falloffMasking (bool?): Deformation will be restricted to selected components  
                Properties: create
        falloffMode (int?): Set the falloff method used for the softMod.  
                Properties: create
        falloffRadius (float?): Set the falloff radius of the softMod.  
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
        relative (bool?): Enable relative mode for the softMod. In relative mode,  
                Only the transformations directly above the softMod are used  
                by the softMod. Default is off.  
                Properties: create
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        resetGeometry (bool?): Reset the geometry matrices for the objects being deformed  
                by the softMod. This flag is used to get rid of undesirable  
                effects that happen if you scale an object that  
                is deformed by a softMod.  
                Properties: edit
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
        weightedNode (Queryable[Tuple[str, str]]?): Transform node in the DAG above the softMod to which all percents are  
                applied. The second node specifies the descendent of the first node  
                from where the transformation matrix is evaluated. Default is the  
                softMod handle.  
                Properties: create, query, edit

    Returns:
        str: [] (the softMod node name and the softMod handle name)

    Example:
    """

