from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def transferAttributes(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., colorBorders: int = ..., components: bool = ..., deformerTools: bool = ..., exclusive: Queryable[str] = ..., flipUVs: int = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., matchChoice: int = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., sampleSpace: int = ..., searchMethod: int = ..., searchScaleX: float = ..., searchScaleY: float = ..., searchScaleZ: float = ..., selectedComponents: bool = ..., sourceColorSet: str = ..., sourceUvSet: str = ..., sourceUvSpace: str = ..., split: bool = ..., targetColorSet: str = ..., targetUvSet: str = ..., targetUvSpace: str = ..., transferColors: int = ..., transferNormals: int = ..., transferPositions: int = ..., transferUVs: int = ..., useComponentTags: bool = ...) -> Union[str, bool, Multiuse[str]]:
    """Samples the attributes of a source surface (first argument) and
    transfers them onto a target surface (second argument).
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
        colorBorders (int?): Controls whether color borders are preserved when transferring color  
                data. If this is non-zero, any color borders will be mapped onto the nearest  
                edge on the target geometry. 0 means any color borders will be  
                smoothly blended onto the vertices of the target geometry.  
                Properties: create, edit
        components (bool?): Returns the components used by the deformer  
                Properties: query
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        exclusive (Queryable[str]?): Puts the deformation set in a deform partition.  
                Properties: create, query
        flipUVs (int?): Controls how sampled UV data is flipped before being transferred  
                to the target. 0 means no flipping; 1 means UV data is flipped in the  
                U direction; 2 means UV data is flipped in the V direction; and 3 means  
                it is flipped in both directions. In conjunction with mirroring, this  
                allows the creation of symmetric UV mappings (e.g. the left hand side of the  
                character on one side of the UV map, the right hand side on the other).  
                Properties: create, edit
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
        matchChoice (int?): When using topological component matching, selects between possible matches.  
                If the meshes involved in the transfer operation have symmetries in their  
                topologies, there may be more than one possible topological match.  
                Maya scores the possible matches (by comparing the shapes of the meshes)  
                and assigns them an index, starting at zero.  
                Match zero, the default, is considered the best, but in the event that Maya  
                chooses the wrong one, changing this value will allow the user to explore the  
                other matches.  
                Properties: create, edit
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
        sampleSpace (int?): Selects which space the attribute transfer is performed in.  
                0 is world space, 1 is model space, 4 is component-based, 5 is topology-based. The default is world space.  
                Properties: create, edit
        searchMethod (int?): Specifies which search method to use when correlating points.  
                0 is closest along normal, 3 is closest to point. The default is closest to point.  
                Properties: create, edit
        searchScaleX (float?): Specifies an optional scale that should be applied to the x-axis  
                of the target model before transferring data. A value of 1.0 (the  
                default) means no scaling; a value of -1.0 would indicate mirroring  
                along the x-axis.  
                Properties: create, edit
        searchScaleY (float?): Specifies an optional scale that should be applied to the y-axis  
                of the target model before transferring data. A value of 1.0 (the  
                default) means no scaling; a value of -1.0 would indicate mirroring  
                along the y-axis.  
                Properties: create, edit
        searchScaleZ (float?): Specifies an optional scale that should be applied to the z-axis  
                of the target model before transferring data. A value of 1.0 (the  
                default) means no scaling; a value of -1.0 would indicate mirroring  
                along the z-axis.  
                Properties: create, edit
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        sourceColorSet (str?): Specifies the name of a single color set on the source surface(s) that  
                should be transferred to the target. This value is only used when  
                the operation is configured to transfer a single color set (see the  
                transferColors flag).  
                Properties: create
        sourceUvSet (str?): Specifies the name of a single UV set on the source surface(s) that  
                should be transferred to the target. This value is only used when  
                the operation is configured to transfer a single UV set (see the  
                transferUVs flag).  
                Properties: create
        sourceUvSpace (str?): Specifies the name of the UV set on the source surface(s) that  
                should be used as the transfer space. This value is only used when  
                the operation is configured to transfer attributes in UV space.  
                Properties: create
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        targetColorSet (str?): Specifies the name of a single color set on the target surface that  
                should be receive the sampled color data. This value is only used when  
                the operation is configured to transfer a single color set (see the  
                transferColors flag).  
                Properties: create
        targetUvSet (str?): Specifies the name of a single UV set on the target surface that  
                should be receive the sampled UV data. This value is only used when  
                the operation is configured to transfer a single UV set (see the  
                transferUVs flag).  
                Properties: create
        targetUvSpace (str?): Specifies the name of the UV set on the target surface( that  
                should be used as the transfer space. This value is only used when  
                the operation is configured to transfer attributes in UV space.  
                Properties: create
        transferColors (int?): Controls color set transfer. 0 means no color sets are transferred,  
                1 means that a single color set (specified by sourceColorSet and targetColorSet)  
                is transferred, and 2 means that all color sets are transferred.  
                Properties: create, edit
        transferNormals (int?): A non-zero value indicates vertex normals should be sampled  
                and written into user normals on the target surface.  
                Properties: create, edit
        transferPositions (int?): A non-zero value indicates vertex position should be sampled,  
                causing the target surface to "wrap" to the source surface(s).  
                Properties: create, edit
        transferUVs (int?): Controls UV set transfer. 0 means no UV sets are transferred,  
                1 means that a single UV set (specified by sourceUVSet and targetUVSet)  
                is transferred, and 2 means that all UV sets are transferred.  
                Properties: create, edit
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create

    Returns:
        str: The node name.

    Example:
    """

