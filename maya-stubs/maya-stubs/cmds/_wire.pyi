from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def wire(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., crossingEffect: Queryable[float] = ..., deformerTools: bool = ..., dropoffDistance: Queryable[Multiuse[Tuple[int, float]]] = ..., envelope: Queryable[float] = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., groupWithBase: bool = ..., holder: Queryable[Multiuse[Tuple[int, str]]] = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., localInfluence: Queryable[float] = ..., name: str = ..., parallel: bool = ..., prune: bool = ..., remove: Multiuse[bool] = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ..., wire: Queryable[Multiuse[str]] = ..., wireCount: Queryable[int] = ...) -> Union[List[str], bool, float, Multiuse[Tuple[int, float]], str, Multiuse[str], Multiuse[Tuple[int, str]], int]:
    """This command creates a wire deformer.In the create mode the selection list is treated as the
    object(s) to be deformed, Wires are specified with the -w flag.
    Each wire can optionally have a holder which helps define the
    the regon of the object that is affected by the deformer.
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
        crossingEffect (Queryable[float]?): Set the amount of convolution effect. Varies from fully  
                convolved at 0 to a simple additive effect at 1 (which  
                is what you get with the filter off).  
                Default is 0.  
                 This filter should make its way into all  
                blend nodes that deal with combining effects from  
                multiple sources.  
                Properties: create, query, edit
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        dropoffDistance (Queryable[Multiuse[Tuple[int, float]]]?): Set the dropoff distance (second parameter) for the wire at index (first parameter).  
                Properties: create, query, edit, multiuse
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
        groupWithBase (bool?): Groups the wire with the base wire so that they can easily be moved  
                together to create a ripple effect.  
                Default is false.  
                Properties: create
        holder (Queryable[Multiuse[Tuple[int, str]]]?): Set the specified curve or surface (second parameter  as a holder for the wire at index (first parameter).  
                Properties: create, query, edit, multiuse
        ignoreSelected (bool?): Tells the command to not deform objects on the  
                current selection list  
                Properties: create
        includeHiddenSelections (bool?): Apply the deformer to any visible and hidden objects in the selection list.  
                Default is false.  
                Properties: create
        localInfluence (Queryable[float]?): Set the local control a wire has with respect to other  
                wires irrespective of whether it is deforming the surface.  
                Varies from no local effect at 0 to full local control  
                at 1.  
                Default is 0.  
                Properties: create, query, edit
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
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create
        wire (Queryable[Multiuse[str]]?): Specify or query the wire curve name.  
                Properties: create, query, edit, multiuse
        wireCount (Queryable[int]?): Set the number of wires.  
                Properties: create, query, edit

    Returns:
        List[str]: The wire node name and the wire curve name

    Example:
    """

