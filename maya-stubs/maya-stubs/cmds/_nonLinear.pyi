from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nonLinear(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., autoParent: bool = ..., before: bool = ..., commonParent: bool = ..., components: bool = ..., defaultScale: bool = ..., deformerTools: bool = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., selectedComponents: bool = ..., split: bool = ..., type: str = ..., useComponentTags: bool = ...) -> Union[List[str], bool, str, Multiuse[str]]:
    """This command creates a functional deformer of the specified type that
    will deform the selected objects.  The deformer consists of
    three nodes: The deformer driver that gets connected to the
    history of the selected objects, the deformer handle transform
    that controls position and orientation of the axis of the deformation
    and the deformer handle that maintains the deformation parameters.
    The type of the deformer handle shape created depends on the
    specified type of the deformer.  The deformer handle
    will be positioned at the center of the selected objects' bounding
    box and oriented to match the orientation of the leading object
    in the selection list.  The deformer handle transform will be
    selected when the command is completed.The nonLinear command has some flags which are specific to the
    nonLinear type specified with the -type flag. The flags correspond to
    the primary keyable attributes related to the specific type of
    nonLinear node. For example, if the type is "bend", then the flags
    "-curvature", "-lowBound" and "-highBound" may be used to initialize,
    edit or query those attribute values on the bend node. Examples
    of this are covered in the example section below.
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
        autoParent (bool?): Parents the deformer handle under the selected object's  
                transform. This flag is valid only when a single object  
                is selected.  
                Properties: create
        before (bool?): If the default behavior for insertion/appending into/onto  
                the existing chain is not the desired behavior then this flag  
                can be used to force the command to place the deformer  
                node before the selected node in the chain even if  
                a new geometry shape has to be created in order to do so.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        commonParent (bool?): Creates a new transform and parents the selected object  
                and the deformer handle under it.  This flag is valid only  
                when a single object is selected.  
                Properties: create
        components (bool?): Returns the components used by the deformer  
                Properties: query
        defaultScale (bool?): Sets the scale of the deformation handle to 1.  By default  
                the deformation handle is scaled to the match the largest  
                dimension of the selected objects' bounding box.  
                [deformerFlags]  
                The attributes of the deformer handle shape  
                can be set upon creation, edited and queried as normal flags  
                using either the long or the short attribute name.  e.g.  
                Properties: create
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
        selectedComponents (bool?): Returns the components used by the deformer that are currently selected.  
                This intersects the current selection with the components affected by the deformer.  
                Properties: query
        split (bool?): Branches off a new chain in the dependency graph instead  
                of inserting/appending the deformer into/onto an  
                existing chain.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        type (str?): Specifies the type of deformation. The current valid  
                deformation types are:  bend, twist, squash, flare,  
                sine and wave  
                Properties: create
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create

    Returns:
        List[str]: Deformer driver name, deformer handle transform name.

    Example:
    """

