from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def textureDeformer(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., components: bool = ..., deformerTools: bool = ..., direction: str = ..., envelope: float = ..., exclusive: Queryable[str] = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., name: str = ..., offset: float = ..., parallel: bool = ..., pointSpace: str = ..., prune: bool = ..., remove: Multiuse[bool] = ..., selectedComponents: bool = ..., split: bool = ..., strength: float = ..., useComponentTags: bool = ..., vectorOffset: Tuple[float, float, float] = ..., vectorSpace: str = ..., vectorStrength: Tuple[float, float, float] = ...) -> Union[str, bool, Multiuse[str]]:
    """This command creates a texture deformer for the object.
    The selected objects are the input geometry objects.
    The deformer node name will be returned.
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
        direction (str?): Set the deformation direction of texture deformer  
                It can only handle three types: "Normal", "Handle" and "Vector".  
                "Normal"  each vertices use its own normal vector.  
                "Handle"  all vertices use Up vector of the handle.  
                "Vector"  each vertices use RGB color vector  
                strings.  
                Properties: create
        envelope (float?): Set the envelope of texture deformer.  
                Envelope determines the percent  
                of deformation. The final result is  
                (color * normal * strength + offset) * envelope  
                Properties: create
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
        offset (float?): Set the offset of texture deformer.  
                Offset plus a translation on the final  
                deformed vertices.  
                Properties: create
        parallel (bool?): Inserts the new deformer in a parallel chain to any existing deformers in  
                the history of the object. A blendShape is inserted to blend the parallel  
                results together.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        pointSpace (str?): Set the point space of texture deformer.  
                It can only handle three strings: "World", "Local" and "UV".  
                "World"   map world space to color space.  
                "Local"	  map local space to color space.  
                "UV"	  map UV space to color space.  
                strings.  
                Properties: create
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
        strength (float?): Set the strength of texture deformer.  
                Strength determines how strong the  
                object is deformed.  
                Properties: create
        useComponentTags (bool?): When this flag is specified a setup using componentTags will be created.  
                This means no groupId, groupParts, tweak or objectSet nodes will be  
                created and connected to the new deformer.  
                Properties: create
        vectorOffset (Tuple[float, float, float]?): Set the vector offset of texture deformer.  
                Vector offset indicates the offset of the  
                deformation on the vector mode.  
                Properties: create
        vectorSpace (str?): Set the vector space of texture deformer.  
                It can only handle three strings: "Object", "World" and "Tangent".  
                "Object"   	use color vector in object space  
                "World"	 	use color vector in world space  
                "Tangent"	use color vector in tangent space  
                strings.  
                Properties: create
        vectorStrength (Tuple[float, float, float]?): Set the vector strength of texture deformer.  
                Vector strength determines how strong the  
                object is deformed on the vector mode.  
                Properties: create

    Returns:
        str: Texture deformer node name

    Example:
    """

