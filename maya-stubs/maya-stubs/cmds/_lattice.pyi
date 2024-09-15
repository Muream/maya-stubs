from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def lattice(*args: str, edit: bool = ..., query: bool = ..., after: bool = ..., afterReference: bool = ..., before: bool = ..., commonParent: bool = ..., components: bool = ..., deformerTools: bool = ..., divisions: Queryable[Tuple[int, int, int]] = ..., dualBase: bool = ..., exclusive: Queryable[str] = ..., freezeMapping: bool = ..., frontOfChain: bool = ..., geometry: Queryable[Multiuse[str]] = ..., geometryIndices: bool = ..., ignoreSelected: bool = ..., includeHiddenSelections: bool = ..., latticeReset: bool = ..., ldivisions: Queryable[Tuple[int, int, int]] = ..., minimumSize: float = ..., name: str = ..., objectCentered: bool = ..., outsideFalloffDistance: float = ..., outsideLattice: int = ..., parallel: bool = ..., position: Tuple[float, float, float] = ..., prune: bool = ..., remove: Multiuse[bool] = ..., removeTweaks: bool = ..., rotation: Tuple[float, float, float] = ..., scale: Tuple[float, float, float] = ..., selectedComponents: bool = ..., split: bool = ..., useComponentTags: bool = ...) -> Union[List[str], bool, Tuple[int, int, int], str, Multiuse[str]]:
    """This command creates a lattice deformer that will deform the selected
    objects. If the object centered flag is used, the initial lattice will
    fit around the selected objects. The lattice will be selected
    when the command is completed. The lattice deformer has an associated
    base lattice. Only objects which are contained by the base lattice
    will be deformed by the lattice.
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
        commonParent (bool?): Group the base lattice and the deformed lattice under  
                a common transform. This means that you can resize the lattice  
                without affecting the deformation by resizing the common  
                transform.  
                Properties: create
        components (bool?): Returns the components used by the deformer  
                Properties: query
        deformerTools (bool?): Returns the name of the deformer tool objects (if any)  
                as string string ...  
                Properties: query
        divisions (Queryable[Tuple[int, int, int]]?): Set the number of lattice slices in x, y, z. Default  
                is 2, 5, 2. When queried, this flag returns float float float.  
                When you change the number of divisions, any tweaking or  
                animation of lattice points must be redone.  
                Properties: create, query, edit
        dualBase (bool?): Create a special purpose ffd deformer node which  
                accepts 2 base lattices. The default is off which results  
                in the creation of a normal ffd deformer node.  
                Intended for internal usage only.  
                Properties: create
        exclusive (Queryable[str]?): Puts the deformation set in a deform partition.  
                Properties: create, query
        freezeMapping (bool?): The base position of the geometries points is fixed  
                at the time this flag is set.  When mapping is frozen, moving  
                the geometry with respect to the lattice will not cause the  
                deformation to be recomputed.  
                Properties: create, query, edit
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
        latticeReset (bool?): Reset the lattice to match its base position. This will  
                undo any deformations that the lattice is causing. The lattice  
                will only deform points that are enclosed within the lattice's  
                reset (base) position.  
                Properties: edit
        ldivisions (Queryable[Tuple[int, int, int]]?): Set the number of local lattice slices in x, y, z.  
                Properties: create, query, edit
        minimumSize (float?): Set the minimum size of a side of the lattice during creation  
                using the objectCentered flag which causes the lattice size to  
                be determined from the geometry that is being deformed.  
                When f.e. the object is a flat plane this can avoid the lattice  
                to have size 0.0 along one side.  
                Properties: create
        name (str?): Used to specify the name of the node being created.  
                Properties: create
        objectCentered (bool?): Centers the lattice around the selected object(s) or  
                components. Default is off which centers the  
                lattice at the origin.  
                Properties: create
        outsideFalloffDistance (float?): Set the falloff distance used when the setting for  
                transforming points outside of the base lattice is set to 2.  
                The distance value is a positive number which specifies the  
                size of the falloff distance as a multiple of the base lattice  
                size, thus a value of 1.0 specifies that only points up to  
                the base lattice width/height/depth away are transformed.  
                A value of 0.0 is equivalent to an outsideLattice value of  
                0 (i.e. no points outside the base lattice are transformed).  
                A huge value is equivalent to transforming an outsideLattice  
                value of 1 (i.e. all points are transformed).  
                Properties: create
        outsideLattice (int?): Set the mode describing how points outside the base  
                lattice are transformed. 0 (the default) specifies that no  
                outside points are transformed. 1 specifies that all outside  
                points are transformed, and 2 specifies that only those  
                outside points which fall within the "falloff distance" (see  
                the -ofd/outsideFalloffDistance flag) are transformed. When  
                querying, the current setting for the lattice is returned.  
                Properties: create
        parallel (bool?): Inserts the new deformer in a parallel chain to any existing deformers in  
                the history of the object. A blendShape is inserted to blend the parallel  
                results together.  
                Works in create mode (and edit mode if the deformer has  
                no geometry added yet).  
                Properties: create, edit
        position (Tuple[float, float, float]?): Used to specify the position of the newly created lattice.  
                Properties: create
        prune (bool?): Removes any points not being deformed by the deformer in  
                its current configuration from the deformer set.  
                Properties: edit
        remove (Multiuse[bool]?): Specifies that objects listed after the -g flag should  
                be removed from this deformer.  
                Properties: edit, multiuse
        removeTweaks (bool?): Remove any lattice deformations caused by moving lattice  
                points. Translations/rotations and scales on the lattice itself  
                are not removed.  
                Properties: edit
        rotation (Tuple[float, float, float]?): Used to specify the initial rotation of the newly created lattice.  
                Properties: create
        scale (Tuple[float, float, float]?): Used to specify the initial scale of the newly created lattice.  
                Properties: create
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

    Returns:
        List[str]: Ffd node name, lattice name, base lattice name.

    Example:
    """

