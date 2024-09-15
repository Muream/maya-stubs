from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def blendShape(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., automatic: bool = ..., before: bool = ..., components: bool = ..., copyDelta: Tuple[int, int, int] = ..., copyInBetweenDelta: Tuple[int, int, int, int] = ..., copyWeights: Tuple[int, int, int] = ..., deformerTools: bool = ..., editTarget: bool = ..., envelope: Queryable[float] = ..., exclusive: Queryable[str] = ..., export: str = ..., exportTarget: Multiuse[Tuple[int, int]] = ..., flipTarget: Multiuse[Tuple[int, int]] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., ip: str = ..., inBetween: bool = ..., inBetweenIndex: int = ..., inBetweenType: str = ..., includeHiddenSelections: bool = ..., mergeSource: Multiuse[int] = ..., mergeTarget: int = ..., mirrorDirection: int = ..., mirrorTarget: Multiuse[Tuple[int, int]] = ..., name: str = ..., normalizationGroups: bool = ..., origin: str = ..., parallel: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., resetTargetDelta: Multiuse[Tuple[int, int]] = ..., selectedComponents: bool = ..., split: bool = ..., suppressDialog: bool = ..., symmetryAxis: Queryable[str] = ..., symmetryEdge: Queryable[Multiuse[str]] = ..., symmetrySpace: Queryable[int] = ..., tangentSpace: bool = ..., target: Queryable[Multiuse[Tuple[str, int, str, float]]] = ..., topologyCheck: bool = ..., transform: Queryable[str] = ..., useComponentTags: bool = ..., weight: Queryable[Multiuse[Tuple[int, float]]] = ..., weightCount: Queryable[int] = ...) -> Union[List[str], bool, float, str, Multiuse[str], int, Multiuse[Tuple[str, int, str, float]], Multiuse[Tuple[int, float]]]:
    """This command creates a blendShape deformer, which blends in specified
    amounts of each target shape to the initial base shape.
    Each base shape is deformed by its own set of target shapes.
    Every target shape has an index that associates it with one of
    the shape weight values.In the create mode the first item on the selection list is treated
    as the base and the remaining inputs as targets. If the first item
    on the list has multiple shapes grouped beneath it, the targets must
    have an identical shape hierarchy. Additional base shapes
    can be added in edit mode using the deformers -g flag.
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
        automatic (bool?): The -automatic flag is used to specify deformer ordering in a way that  
                choses between -frontOfChain and -before automatically. If the geometry being  
                deformed is only affected by invertible deformers, the -frontOfChain mode is used, otherwise  
                the -before mode is used.  
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
        copyDelta (Tuple[int, int, int]?): Set the base, source, and destination delta index values.  
                Properties: edit
        copyInBetweenDelta (Tuple[int, int, int, int]?): Set the base, target, source, and destination delta index values.  
                Properties: edit
        copyWeights (Tuple[int, int, int]?): Copy base, source, and destination weight index values.  
                Properties: edit
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        editTarget (bool?): Returns the name of the edit target of a blendShape, if any, as it appears in  
                the Shape Editor. If the target being edited is an in-between, it will append  
                the value of the in-between to the shape name (e.g., pSphere2_0.564).  
                Properties: query
        envelope (Queryable[float]?): Set the envelope value for the deformer, controlling  
                how much of the total deformation gets applied. Default is 1.0.  
                Properties: create, query, edit
        exclusive (Queryable[str]?): Puts the deformation set in a deform partition.  
                Properties: create, query
        export (str?): Export the shapes to the named file path.  
                Properties: edit
        exportTarget (Multiuse[Tuple[int, int]]?): Specify the base and target index pairs for the export.  
                Properties: edit, multiuse
        flipTarget (Multiuse[Tuple[int, int]]?): Flip the list of base and target pairs.  
                Properties: edit, multiuse
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
        ip (str?): Import the shapes from the named file path.  
                Properties: edit
        inBetween (bool?): Indicate that the specified target should serve as  
                an inbetween. An inbetween target is one that serves as an  
                intermediate target between the base shape and another target.  
                Properties: create, edit
        inBetweenIndex (int?): Only used with the -rtd/-resetTargetDelta flag to remove delta values  
                for points in the inbetween target geometry defined by this index.  
                Properties: edit
        inBetweenType (str?): Specify if the in-between target to be created is relative to the hero  
                target or if it is absolute.  
                If it is relative to hero targets, the in-between target will get any changes made to the hero target.  
                Valid values are "relative" and "absolute".  
                This flag should always be used with the -ib/-inBetween and -t/-target flags.  
                Properties: create, edit
        includeHiddenSelections (bool?): Apply the deformer to any visible and hidden objects in the selection list.  
                Default is false.  
                Properties: create
        mergeSource (Multiuse[int]?): List of source indexes for a merge.  
                Properties: edit, multiuse
        mergeTarget (int?): Target index of a merge  
                Properties: edit
        mirrorDirection (int?): Mirror direction; 0 = negative, 1 = positive  
                Properties: edit
        mirrorTarget (Multiuse[Tuple[int, int]]?): Mirror the list of base and target pairs.  
                Properties: edit, multiuse
        name (str?): Used to specify the name of the node being created.  
                Properties: create
        normalizationGroups (bool?): Returns a list of the used normalization group IDs.  
                Properties: query
        origin (str?): blendShape will be performed with respect to the  
                world by default. Valid values are "world" and "local". The local flag will cause the blend  
                shape to be performed with respect to the shape's local  
                origin.  
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
        resetTargetDelta (Multiuse[Tuple[int, int]]?): Remove all delta values for points in the target geometry,  
                including all sequential targets defined by target index.  
                Parameter list:  
              
                uint: the base object index  
                uint: the target index  
                Properties: edit, multiuse
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        suppressDialog (bool?): Suppress dialog box and run the command as defined by the user.  
                Properties: create, edit
        symmetryAxis (Queryable[str]?): Axis for symmetry. Valid values are "X", "Y", and "Z".  
                Properties: query, edit
        symmetryEdge (Queryable[Multiuse[str]]?): One or two symmetry edge names, separated by a ".". See the blendShape node's  
                symmetryEdge attribute for legal values.  
                Properties: query, edit, multiuse
        symmetrySpace (Queryable[int]?): Space for symmetry. 0 = Topological, 1 = Object, 2 = UV  
                Properties: query, edit
        tangentSpace (bool?): Indicate that the delta of the specified target should be relative to  
                the tangent space of the surface.  
                Properties: create, edit
        target (Queryable[Multiuse[Tuple[str, int, str, float]]]?): Set target object as the index target shape for the base shape base  
                object. The full influence of target shape takes effect when its shape  
                weight is targetValue.  
                Parameter list:  
              
                string: the base object  
                int: index  
                string: the target object  
                double: target value  
                Properties: create, query, edit, multiuse
        topologyCheck (bool?): Set the state of checking for a topology match between the  
                shapes being blended. Default is on.  
                Properties: create
        transform (Queryable[str]?): Set transform for target, then the deltas will become relative to a post transform. Typically the  
                best workflow for this option is to choose a joint that is related to the fix you have introduced.  
                This flag should be used only if the "Deformation order" of blendShape node is "Before".  
                Properties: query, edit
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create
        weight (Queryable[Multiuse[Tuple[int, float]]]?): Set the weight value (second parameter) at index (first parameter).  
                Properties: create, query, edit, multiuse
        weightCount (Queryable[int]?): Set the number of shape weight values.  
                Properties: create, query, edit

    Returns:
        List[str]: (the blendShape node name)

    Example:
    """

