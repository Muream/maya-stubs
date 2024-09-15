from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def jointLattice(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., creasing: Queryable[float] = ..., deformerTools: bool = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., joint: str = ..., lengthIn: Queryable[float] = ..., lengthOut: Queryable[float] = ..., lowerBindSkin: str = ..., lowerTransform: str = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., rounding: Queryable[float] = ..., selectedComponents: bool = ..., split: bool = ..., upperBindSkin: str = ..., upperTransform: str = ..., useComponentTags: bool = ..., widthLeft: Queryable[float] = ..., widthRight: Queryable[float] = ...) -> Union[str, bool, float, Multiuse[str]]:
    """This command creates/edits/queries a jointLattice deformer. The name
    of the created/edited object is returned. Usually you would make use of
    this functionality through the higher level flexor command.
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
        creasing (Queryable[float]?): Affects the bulging of lattice points on the inside of  
                the bend.  Positive/negative values cause the points to bulge  
                outwards/inwards. Default value is 0.0. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
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
        joint (str?): Specifies the joint which will be used to drive the  
                bulging behaviours.  
                Properties: create
        lengthIn (Queryable[float]?): Affects the location of lattice points on the parent  
                bone.  Positive/negative values cause the points to move  
                away/towards the joint. Changing this parameter also modifies  
                the regions affected by the creasing, rounding and width  
                parameters. Default value is 0.0. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        lengthOut (Queryable[float]?): Affects the location of lattice points on the child bone.  
                Positive/negative values cause the points to move away/towards  
                the joint. Changing this parameter also modifies the regions  
                affected by the creasing, rounding and width parameters. Default  
                value is 0.0. When queried, this flag returns a float.  
                Properties: create, query, edit
        lowerBindSkin (str?): Specifies the node which is performing the bind skin  
                operation on the geometry associated with the lower bone.  
                Properties: create
        lowerTransform (str?): Specifies which dag node is being used to rigidly transform  
                the lower part of the lattice which this node is going to deform.  
                If this flag is not specified an identity matrix will be assumed.  
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
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        rounding (Queryable[float]?): Affects the bulging of lattice points on the outside  
                of the bend. Positive/negative values cause the points to bulge  
                outwards/inwards. Default value is 0.0. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        upperBindSkin (str?): Specifies the node which is performing the bind skin  
                operation on the geometry associated with the upper bone.  
                Properties: create
        upperTransform (str?): Specifies which dag node is being used to rigidly transform  
                the upper part of the lattice which this node is going to deform.  
                If this flag is not specified an identity matrix will be assumed.  
                Properties: create
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create
        widthLeft (Queryable[float]?): Affects the bulging of lattice points on the left side  
                of the bend. Positive/negative values cause the points to bulge  
                outwards/inwards. Default value is 0.0. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        widthRight (Queryable[float]?): Affects the bulging of lattice points on the right  
                side of the bend. Positive/negative values cause the points to  
                bulge outwards/inwards. Default value is 0.0. When queried, this  
                flag returns a float.  
                Properties: create, query, edit

    Returns:
        str: Name of joint lattice algorithm node created/edited.

    Example:
    """

