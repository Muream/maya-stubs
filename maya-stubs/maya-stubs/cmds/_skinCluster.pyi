from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def skinCluster(*args: str, edit: bool = ..., query: bool = ..., addInfluence: Multiuse[str] = ..., addToSelection: bool = ..., after: bool = ..., afterReference: bool = ..., baseShape: Multiuse[str] = ..., before: bool = ..., bindMethod: Queryable[int] = ..., components: bool = ..., deformerTools: bool = ..., dropoffRate: Queryable[float] = ..., exclusive: Queryable[str] = ..., forceNormalizeWeights: bool = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., heatmapFalloff: float = ..., ignoreBindPose: bool = ..., ignoreHierarchy: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., influence: Queryable[str] = ..., lockWeights: bool = ..., maximumInfluences: Queryable[int] = ..., moveJointsMode: bool = ..., multi: bool = ..., name: str = ..., normalizeWeights: Queryable[int] = ..., nurbsSamples: int = ..., obeyMaxInfluences: bool = ..., parallel: bool = ..., polySmoothness: float = ..., prune: bool = ..., recacheBindMatrices: bool = ..., remove: Multiuse[bool] = ..., removeFromSelection: bool = ..., removeInfluence: Multiuse[str] = ..., removeUnusedInfluence: bool = ..., selectInfluenceVerts: str = ..., selectedComponents: bool = ..., skinMethod: Queryable[int] = ..., smoothWeights: float = ..., smoothWeightsMaxIterations: int = ..., split: bool = ..., toSelectedBones: bool = ..., toSkeletonAndTransforms: bool = ..., unbind: bool = ..., unbindKeepHistory: bool = ..., useComponentTags: bool = ..., useGeometry: bool = ..., volumeBind: float = ..., volumeType: int = ..., weight: float = ..., weightDistribution: Queryable[int] = ..., weightedInfluence: bool = ...) -> Union[str, int, bool, float, Multiuse[str]]:
    """The skinCluster command is used for smooth skinning in maya. It
    binds the selected geometry to the selected
    joints or skeleton by means of a skinCluster node.  Each point of the bound
    geometry can be affected by any number of joints.
    The extent to which each joint affects the motion of each point is
    regulated by a corresponding weight factor.  Weight factors can be
    modified using the skinPercent command.  The command returns the name
    of the new skinCluster.The skinCluster binds only a single geometry at a time. Thus, to bind
    multiple geometries, multiple skinCluster commands must be issued.Upon creation of a new skinCluster, the command can be used to add
    and remove transforms (not necessarily joints) that influence the
    motion of the bound skin points.The skinCluster command can also be used to adjust parameters such
    as the dropoff, nurbs samples, polygon smoothness on a particular
    influence object. Note: Any custom weights on a skin point that
    the influence object affects will be lost after adjusting these
    parameters.
    Args:
        addInfluence (Multiuse[str]?): The specified transform or joint will be added to the  
                list of transforms that influence the bound geometry.  
                The maximum number of influences will be observed  
                and only the weights of the cv's that the specified  
                transform effects will change.  
                This flag is multi-use.  
                Properties: edit, multiuse
        addToSelection (bool?): When used in conjunction with the selectInfluenceVerts flag, causes the vertices  
                afftected by the influence to be added to the current selection, without first  
                de-selecting other vertices.  
                Properties: edit
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
        baseShape (Multiuse[str]?): This flag can be used in conjunction with  
                the -addInfluence flag to specify the shape that will  
                be used as the base shape when an influence object with  
                geometry is added to the skinCluster.  If the flag  
                is not used then the command will make a copy of the  
                influence object's shape and use that as a base shape.  
                Properties: edit, multiuse
        before (bool?): If the default behavior for insertion/appending into/onto  
                the existing chain is not the desired behavior then this flag  
                can be used to force the command to place the deformer  
                node before the selected node in the chain even if  
                a new geometry shape has to be created in order to do so.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        bindMethod (Queryable[int]?): This flag sets the binding method.  
                0. Closest distance between a joint and a point of the geometry.  
                1. Closest distance between a joint, considering the skeleton  
                hierarchy, and a point of the geometry.  
                2. Surface heat map diffusion.  
                3. Geodesic voxel binding.  geomBind command must be called after creating a skinCluster with this method.  
                Properties: create, query
        components (bool?): Returns the components used by the deformer  
                Properties: query
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        dropoffRate (Queryable[float]?): Sets the rate at which the influence of a transform  
                drops as the distance from that transform increases.  
                The valid range is between 0.1 and 10.0.  In Create  
                mode it sets the dropoff rate for all the bound  
                joints.  In Edit mode the flag is used together with the  
                inf/influence flag to set the dropoff rate of a  
                particular influence.  Note: When the flag is used in  
                Edit mode, any custom weights on the skin points the  
                given transform influences will be lost.  
                Properties: create, query, edit
        exclusive (Queryable[str]?): Puts the deformation set in a deform partition.  
                Properties: create, query
        forceNormalizeWeights (bool?): If the normalization mode is none or post, it is possible (indeed likely) for the weights in the skin  
                cluster to no longer add up to 1.  This flag forces all weights to add back to 1 again.  
                Properties: edit
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
        heatmapFalloff (float?): This flag sets the heatmap binding falloff. If set to 0.0 (default) the  
                deformation will be smoother due to many small weights spread over the mesh  
                surface per influence. However, if set to 1.0, corresponding to maximum falloff,  
                the number of influences per point will be reduced and points will tend to be  
                greatly influenced by their closest joint decreasing the overall spread of small  
                weights.  
                This flag only works when using heatmap binding.  
                Properties: create
        ignoreBindPose (bool?): This flag is deprecated and no longer used.  It will be ignored  
                if used.  
                Properties: create, edit
        ignoreHierarchy (bool?): Deprecated. Use bindMethod flag instead.  
                Disregard the place of the joints in the skeleton  
                hierarchy when computing the closest joints that influence  
                a point of the geometry.  
                Properties: create, query
        ignoreSelected (bool?): Tells the command to not deform objects on the  
                current selection list  
                Properties: create
        includeHiddenSelections (bool?): Apply the deformer to any visible and hidden objects in the selection list.  
                Default is false.  
                Properties: create
        influence (Queryable[str]?): This flag specifies the influence object that  
                will be used for the current edit operation. In query  
                mode, returns a string array of the influence objects  
                (joints and transform).  
                      In query mode, this flag can accept a value.  
                Properties: query, edit
        lockWeights (bool?): Lock the weights of the specified influence object  
                to their current value or to the value specified by  
                the -weight flag.  
                Properties: query, edit
        maximumInfluences (Queryable[int]?): Sets the maximum number of transforms that can influence  
                a point (have non-zero weight for the point) when  
                the skinCluster is first created or a new influence  
                is added.  Note: When this flag is used in Edit mode  
                any custom weights will be lost and new weights will be  
                reassigned to the whole skin.  
                Properties: create, query, edit
        moveJointsMode (bool?): If set to true, puts the skin into a mode where joints can be moved  
                without modifying the skinning. If set to false, takes the skin out  
                of move joints mode.  
                Properties: edit
        multi (bool?): If true then the command will allow multiple skin clusters to be created  
                on the target geometry. If false the command will generate an error if  
                when trying to add a second skin cluster to the geometry.  
                Properties: create
        name (str?): Used to specify the name of the node being created.  
                Properties: create
        normalizeWeights (Queryable[int]?): This flag sets the normalization mode. 0. none,  
                1. interactive, 2. post (default)  
                Interactive normalization makes sure the weights on the influences add up to 1.0, always.  
                Everytime a weight is changed, the weights are automatically normalized.  This may make  
                it difficult to perform weighting operations, as the normalization may interfere with  
                the weights the user has set.  Post normalization leaves the weights the user has set  
                as is, and only normalizes the weights at the moment it is needed  
                (by dividing by the sum of the weights).  This makes it easier for users to weight their skins.  
                Properties: create, query, edit
        nurbsSamples (int?): Sets the number of sample points that will be used  
                along an influence curve or in each direction on an  
                influence NURBS surface to influence the bound skin.  
                The more the sample points the more closely the skin  
                follows the influence NURBS curve/surface.  
                Properties: create, edit
        obeyMaxInfluences (bool?): When true, the skinCluster will continue to enforce the maximum  
                influences each time the user modifies the weight, so that any  
                given point is only weighted by the number of influences in the  
                skinCluster's maximumInfluences attribute.  
                Properties: create, query, edit
        parallel (bool?): Inserts the new deformer in a parallel chain to any existing deformers in  
                the history of the object. A blendShape is inserted to blend the parallel  
                results together.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        polySmoothness (float?): This flag controls how accurately the skin control  
                points follow a given polygon influence object.  
                The higher the value of polySmoothnmess the  
                more rounded the deformation resulting from a polygonal  
                influence object will be.  
                Properties: create, edit
        prune (bool?): Removes any points not being deformed by the deformer in  
                its current configuration from the deformer set.  
                Properties: edit
        recacheBindMatrices (bool?): Forces the skinCluster node to recache its bind matrices.  
                Properties: edit
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        removeFromSelection (bool?): When used in conjunction with the selectInfluenceVerts flag, causes the vertices  
                afftected by the influence to be removed from the current selection.  
                Properties: edit
        removeInfluence (Multiuse[str]?): Remove the specified transform or joint from the list of  
                transforms that influence the bound geometry  
                The weights for the affected points are renormalized.  
                This flag is multi-use.  
                Properties: edit, multiuse
        removeUnusedInfluence (bool?): If this flag is set to true then transform or joint whose weights are all zero  
                (they have no effect) will not be bound to the geometry.  Having this  
                option set will help speed-up the playback of animation. In query mode,  
                returns the number of transforms or joints whose weights are all zero.  
                Properties: create, query, edit
        selectInfluenceVerts (str?): Given the name of a transform, this will select the verts or control points  
                being influenced by this transform, so users may visualize which vertices are  
                being influenced by the transform.  
                Properties: edit
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        skinMethod (Queryable[int]?): This flag set the skinning method. 0. classical linear skinning (default).  
                1. dual quaternion (volume preserving), 2. a weighted blend between the two.  
                Properties: create, query, edit
        smoothWeights (float?): This flag is used to detect sudden jumps in skin weight values, which often  
                indicates bad weighting, and then smooth out those jaggies in skin weights.  
                The argument is the error tolerance ranging from 0 to 1.  A value of 1 means  
                that the algorithm will smooth a vertex only if there is a 100% change in  
                weight values from its neighbors.  The recommended default to use is 0.5  
                (50% change in weight value from the neighbors).  
                Properties: edit
        smoothWeightsMaxIterations (int?): This flag is valid only with the smooth weights flag.  It is possible that not  
                all the vertices detected as needing smoothing can be smoothed in 1 iteration  
                (because all of their neighbors also have bad weighting and need to be smoothed).  
                With more iterations, more vertices can be smoothed.  This flag controls the  
                maximum number of iterations the algorithm will attempt to smooth weights.  
                The default is 2 for this flag.  
                Properties: edit
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        toSelectedBones (bool?): geometry will be bound to the selected bones only.  
                Properties: create
        toSkeletonAndTransforms (bool?): geometry will be bound to the skeleton and any transforms in the hierarchy.  
                If any of the transforms are also bindable objects, assume that only the  
                last object passed to the command is the bindable object. The rest are  
                treated as influences.  
                Properties: create
        unbind (bool?): Unbinds the geometry from the skinCluster and deletes  
                the skinCluster node  
                Properties: edit
        unbindKeepHistory (bool?): Unbinds the geometry from the skinCluster, but keeps  
                the skinCluster node so that its weights can be used  
                when the skin is rebound. To rebind, use the skinCluster  
                command.  
                Properties: edit
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create
        useGeometry (bool?): When adding an influence to a skinCluster, use the geometry  
                parented under the influence transform to determine  
                the weight dropoff of that influence.  
                Properties: edit
        volumeBind (float?): Creates a volume bind node and attaches it to the new skin cluster node. This  
                node holds hull geometry parameters for a volume based weighting system. This system is  
                used in interactive skinning. The value passed will determine the minimum weight  
                value when initializing the volume. The volume in be increase to enclose all the vertices  
                that are above this value.  
                Properties: create
        volumeType (int?): Defines the initial shape of the binding volume (see volumeBind). 0. Default (currently set to a capsule)  
                1. Capsule, 2. Cylinder.  
                Properties: create
        weight (float?): This flag is only valid in conjunction with the -addInfluence flag.  
                It sets the weight for the influence object that is being added.  
                Properties: edit
        weightDistribution (Queryable[int]?): This flag sets the weight distribution mode.  
                0. distance (default), 1. neighbors  
                When normalizeWeights is in effect, and a weight has been reduced  
                or removed altogether, the sum is usually brought back up to 1.0  
                by increasing the contributions of the other non-zero weights.  
                However, if there are no other non-zero weights, the algorithm  
                has to create some weights from thin air and distribute the residual  
                weight between them.  
                This attribute controls how that is done.  
                "Distance" - the algorithm calculates weights from  
                the world-space distances from the component to the transforms.  
                "Neighbors" - the algorithm calculates weights from  
                the weights on the neighboring components.  
                Properties: create, query, edit
        weightedInfluence (bool?): This flag returns a string array of the influence objects  
                (joints and transform) that have non-zero weighting.  
                Properties: query

    Returns:
        str: (the skinCluster node name)

    Example:
    """

