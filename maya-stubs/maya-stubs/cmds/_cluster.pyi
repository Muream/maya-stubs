from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cluster(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., bindState: bool = ..., components: bool = ..., deformerTools: bool = ..., envelope: Queryable[float] = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., relative: bool = ..., remove: Multiuse[bool] = ..., resetGeometry: bool = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., weightedNode: Queryable[Tuple[str, str]] = ...) -> Union[List[str], bool, float, str, Multiuse[str], Tuple[str, str]]:
    """The cluster command creates a cluster or edits the membership of
    an existing cluster. The command returns the name of the cluster
    node upon creation of a new cluster.After creating a cluster, the cluster's weights can be modified
    using the percent command or the set editor window.
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
        bindState (bool?): When turned on, this flag adds in a compensation to ensure  
                the clustered objects preserve their spatial position  
                when clustered. This is required to prevent the geometry  
                from jumping at the time the cluster is created  
                in situations when the  
                cluster transforms at cluster time are not identity.  
                Properties: create
        components (bool?): Returns the components used by the deformer  
                Properties: query
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        envelope (Queryable[float]?): Set the envelope value for the deformer. Default is 1.0  
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
        relative (bool?): Enable relative mode for the cluster. In relative mode,  
                Only the transformations directly above the cluster are used  
                by the cluster. Default is off.  
                Properties: create
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        resetGeometry (bool?): Reset the geometry matrices for the objects being deformed  
                by the cluster. This flag is used to get rid of undesirable  
                effects that happen if you scale an object that  
                is deformed by a cluster.  
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
        weightedNode (Queryable[Tuple[str, str]]?): Transform node in the DAG above the cluster to which all percents are  
                applied. The second DAGobject specifies the descendent of the first  
                DAGobject from where the transformation matrix is evaluated. Default is  
                the cluster handle.  
                Properties: create, query, edit

    Returns:
        List[str]: (the cluster node name and the cluster handle name)

    Example:
    """

