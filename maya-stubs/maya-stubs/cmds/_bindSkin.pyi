from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bindSkin(*args: str, edit: bool = ..., query: bool = ..., byClosestPoint: bool = ..., byPartition: bool = ..., colorJoints: bool = ..., delete: bool = ..., doNotDescend: bool = ..., enable: bool = ..., name: str = ..., partition: str = ..., toAll: bool = ..., toSelectedBones: bool = ..., toSkeleton: bool = ..., unbind: bool = ..., unbindKeepHistory: bool = ..., unlock: bool = ...) -> str:
    """This command binds the currently selected objects to the
    currently selected skeletons.  Shapes which can be bound are:
    meshes, nurbs curves, nurbs surfaces, lattices, subdivision
    surfaces, and API shapes. Multiple shapes and multiple skeletons can be
    bound at once by selecting them or specifying them on the command
    line. Selection order is not important.The skin is bound using the so-called "rigid" bind, in which
    the components are rigidly attached to the closest bone in the
    skeleton. Flexors can later be added to the skeleton to
    smooth out the skinning around joints.The skin(s) can be bound either to the entire skeleton hierarchy
    of the selected joint(s), or to only the selected joints. The
    entire hierarchy is the default. The -tsb/-toSelectedBones flag
    allows binding to only the selected bones.This command can also be used to detach the skin from the skeleton.
    Detaching the skin is useful in a variety of situations, such as:
    inserting additional bones, deleting bones, changing the bind
    position of the skeleton or skin, or simply getting rid of the
    skinning nodes altogether. The options to use when detaching the
    skin depend on how much of the skinning info you want to get rid
    of. Namely: (1) -delete or -unbind: remove all skinning nodes, (2) -unbindKeepHistory: remove the skinning sets, but keep the weights, (3) -disable: disable the skinning but keep the skinning sets and the weights.
    Args:
        byClosestPoint (bool?): bind each point in the object to the segment closest to the point.  
                The byClosestPoint and byPartition flags are mutually  
                exclusive.  The byClosestPoint flag is the default.  
                Properties: create
        byPartition (bool?): bind each group in the partition to the segment  
                closest to the group's centroid. A partition must be specified  
                with the -p/-partition flag  
                Properties: create
        colorJoints (bool?): In bind mode, this flag assigns colors to the joints based  
                on the colors assigned to the joint's skin set.  
                In delete and unlock mode, this flag removes the colors from  
                joints that are no longer bound as skin.  
                In disable and unbindKeepHistory mode, this flag does nothing.  
                Properties: create
        delete (bool?): Detach the skin on the selected skeletons and remove all bind-  
                related construction history.  
                Properties: create
        doNotDescend (bool?): Do not descend to shapes that are parented below the selected  
                object(s).  
                Bind only the selected objects.  
                Properties: create
        enable (bool?): Enable or disable a bind that has been disabled on the selected  
                skeletons.  
                To enable the bind on selected bones only, select the bones and  
                use the -tsb flag with the -en flag. This flag is used when you  
                want to temporarily disable the bind without losing the set  
                information or the weight information of the skinning, for example  
                if you want to modify the bindPose.  
                Properties: create
        name (str?): This flag is obsolete.  
                Properties: create
        partition (str?): Specify a partition to bind by. This is only valid when  
                used with the -bp/-byPartition flag.  
                Properties: create
        toAll (bool?): objects will be bound to the entire selected skeletons. Even bones with zero influence  
                will be bound, whereas the toSkeleton will only bind non-zero influences.  
                Properties: create
        toSelectedBones (bool?): objects will be bound to the selected bones only.  
                Properties: create
        toSkeleton (bool?): objects will be bound to the selected skeletons. The toSkeleton, toAll  
                and toSelectedBones flags are mutually exclusive. The toSkeleton flag is the default.  
                Properties: create
        unbind (bool?): unbind the selected objects. They will no longer move with  
                the skeleton. Any bindSkin history that is no longer used  
                will be deleted.  
                Properties: create
        unbindKeepHistory (bool?): unbind the selected objects. They will no longer move with  
                the skeleton. However, existing weights on the skin  
                will be kept for use the next time the skin is bound. This option  
                is appropriate if you want to modify the skeleton without losing  
                the weighting information on the skin.  
                Properties: create
        unlock (bool?): unlock the selected objects. Since bindSkin will no longer give  
                normal results if bound objects are moved away from the skeleton,  
                bindSkin locks translate, rotate and scale. This command unlocks  
                the selected objects translate, rotate and scale.  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

