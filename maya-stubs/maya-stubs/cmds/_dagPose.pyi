from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dagPose(*args: str, edit: bool = ..., query: bool = ..., addToPose: bool = ..., atPose: bool = ..., bindPose: bool = ..., g: bool = ..., members: bool = ..., name: Queryable[str] = ..., remove: bool = ..., reset: bool = ..., restore: bool = ..., save: bool = ..., selection: bool = ..., worldParent: bool = ...) -> Union[str, bool]:
    """This command is used to save and restore the matrix information for
    a dag hierarchy. Specifically, the data stored will restore the
    translate, rotate, scale, scale pivot, rotate pivot, rotation order,
    and (for joints) joint order for all the objects on the hierarchy.
    Data for other attributes is not stored by this command.This command can also be used to store a bindPose for an object.
    When you skin an object, a dagPose is automatically created for the
    skin.
    Args:
        addToPose (bool?): Allows adding the selected items to the dagPose.  
                Properties: create
        atPose (bool?): Query whether the hierarchy is at same position as the pose.  
                Names of hierarchy members that are not at the pose position will  
                be returned. An empty return list indicates that the hierarchy is at the  
                pose.  
                Properties: query
        bindPose (bool?): Used to specify the bindPose for the selected hierarchy.  
                Each hierarchy can have only  
                a single bindPose, which is saved automatically at the time of a skin  
                bind. The bindPose is used when adding influence objects,  
                binding new skins, or adding flexors. Take care when modifying  
                the bindPose with the -rs/-reset  
                or -rm/-remove flags, since if the bindPose is ill-defined it can  
                cause problems with subsequent skinning operations.  
                Properties: create, query
        g (bool?): This flag can be used in conjunction with the restore flag to  
                signal that the members of the pose should be restored to the  
                global pose. The global pose means not only is each object  
                locally oriented with respect to its parents, it is also in the  
                same global position that it was at when the pose was saved.  
                If a hierarchy's parenting has been changed since the time that  
                the pose was saved, you may have trouble reaching the global pose.  
                Properties: create
        members (bool?): Query the members of the specified pose. The pose should be  
                specified using the selection list, the -bp/-bindPose or the -n/-name flag.  
                Properties: query
        name (Queryable[str]?): Specify the name of the pose. This can be used during create,  
                restore, reset, remove, and query operations to specify the pose  
                to be created or acted upon.  
                Properties: create, query
        remove (bool?): Remove the selected joints from the specified pose.  
                Properties: create
        reset (bool?): Reset the pose on the selected joints. If  
                you are resetting pose data for a bindPose, take care. It is appropriate  
                to use the -rs/-reset flag if a joint has been reparented and/or appears to  
                be exactly at the bindPose. However, a bindPose that is much different  
                from the exact bindPose can cause problems with subsequent skinning operations.  
                Properties: create
        restore (bool?): Restore the hierarchy to a saved pose. To specify the pose,  
                select the pose node, or use the -bp/-bindPose or -n/-name flag.  
                Properties: create
        save (bool?): Save a dagPose for the selected dag hierarchy. The name of the  
                new pose will be returned.  
                Properties: create
        selection (bool?): Whether or not to store a pose for all items in the hierarchy,  
                or for only the selected items.  
                Properties: create, query
        worldParent (bool?): Indicates that the selected pose member should be recalculated as if it is  
                parented to the world. This is typically used when you plan to reparent  
                the object to world as the next operation.  
                Properties: create

    Returns:
        str: Name of pose

    Example:
    """

