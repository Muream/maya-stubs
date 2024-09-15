from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def joint(*args: str, edit: bool = ..., query: bool = ..., absolute: bool = ..., angleX: Queryable[float] = ..., angleY: Queryable[float] = ..., angleZ: Queryable[float] = ..., assumePreferredAngles: bool = ..., automaticLimits: bool = ..., children: bool = ..., component: bool = ..., degreeOfFreedom: Queryable[str] = ..., exists: Queryable[str] = ..., limitSwitchX: bool = ..., limitSwitchY: bool = ..., limitSwitchZ: bool = ..., limitX: Queryable[Tuple[float, float]] = ..., limitY: Queryable[Tuple[float, float]] = ..., limitZ: Queryable[Tuple[float, float]] = ..., name: Queryable[str] = ..., orientJoint: str = ..., orientation: Queryable[Tuple[float, float, float]] = ..., position: Queryable[Tuple[float, float, float]] = ..., radius: Queryable[float] = ..., relative: bool = ..., rotationOrder: Queryable[str] = ..., scale: Queryable[Tuple[float, float, float]] = ..., scaleCompensate: bool = ..., scaleOrientation: Queryable[Tuple[float, float, float]] = ..., secondaryAxisOrient: str = ..., setPreferredAngles: bool = ..., stiffnessX: Queryable[float] = ..., stiffnessY: Queryable[float] = ..., stiffnessZ: Queryable[float] = ..., symmetry: bool = ..., symmetryAxis: str = ..., zeroScaleOrient: bool = ...) -> Union[str, bool, float, Tuple[float, float], Tuple[float, float, float]]:
    """The joint command is used to create, edit, and query, joints
    within Maya. (The standard edit(-e) and query(-q) flags are
    used for edit and query functions). If the object is not
    specified, the currently selected object (dag object) will be
    used.Multiple objects are allowed only for the edit mode. The same
    edit flags will be applied on all the joints selected, except
    for -p without -r (set joint position in the world space). An
    ik handle in the object list is equivalent to the list of
    joints the ik handle commands. When -ch/children is present,
    all the child joints of the specified joints, including the
    joints implied by possible ik handles, will also be included.In the creation mode, a new joint will be created as a child
    of a selected transform or starts a hierarchy by itself if no
    transform is selected. An ik handle will be treated as a
    transform in the creation mode.The default values of the arguments are:-degreeOfFreedom xyz-name "Joint#"-position 0 0 0-absolute-dof "xyz"-scale 1.0 1.0 1.0-scaleCompensate true-orientation 0.0 0.0 0.0-scaleOrientation 0.0 0.0 0.0-limitX -360 360-limitY -360 360-limitZ -360 360-angleX 0.0-angleY 0.0-angleZ 0.0-stiffnessX 0.0-stiffnessY 0.0-stiffnessZ 0.0-limitSwitchX no-limitSwitchY no-limitSwitchZ no-rotationOrder xyzThose arguments can be specified in the creation mode,
    editied in the edit mode (-e), or queried in the query mode
    (-q).
    Args:
        absolute (bool?): The joint center position is in absolute world coordinates.  
                (This is the default.)  
                Properties: create, query, edit
        angleX (Queryable[float]?): Set the x-axis angle. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        angleY (Queryable[float]?): Set the y-axis angle. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        angleZ (Queryable[float]?): Set the z-axis angle. When queried, this flag  
                returns a float.  
                Properties: create, query, edit
        assumePreferredAngles (bool?): Meaningful only in the edit mode. It sets the  
                joint angles to the corresponding preferred  
                angles.  
                Properties: edit
        automaticLimits (bool?): Meaningful only in edit mode. It sets the joint to  
                appropriate hinge joint with joint limits. It modifies  
                the joint only if (a) it connects exactly to two  
                joints (one parent, one child), (b) it does not lie on  
                the line drawn between the two connected joints, and  
                the plane it forms with the two connected joints  
                is perpendicular to one of its rotation axes.  
                Properties: create
        children (bool?): It tells the command to apply all the edit options  
                not only to the selected joints, but also to their  
                descendent joints in the DAG.  
                Properties: edit
        component (bool?): Use with the -position switch to position the joint  
                relative to its parent (like -relative) but to compute  
                new positions for all children joints so their world  
                coordinate positions do not change.  
                Properties: create, edit
        degreeOfFreedom (Queryable[str]?): Specifies the degrees of freedom for the IK.  
                Valid strings consist of non-duplicate letters from x,  
                y, and z. The letters in the string indicate what  
                rotations are to be used by IK. The order a letter  
                appear in the string does not matter. Examples are x,  
                yz, xyz. When queried, this flag returns a string.  
                Modifying dof will change the locking state of the  
                corresponding rotation attributes. The rule is: if an  
                rotation is turned into a dof, it will be unlocked if  
                it is currently locked. When it is turned into a  
                non-dof, it will be locked if it is not currently  
                locked.  
                Properties: create, query, edit
        exists (Queryable[str]?): Does the named joint exist? When queried, this flag  
                returns a boolean.  
                Properties: query
        limitSwitchX (bool?): Use the limit the x-axis rotation? When  
                queried, this flag returns a boolean.  
                Properties: create, query, edit
        limitSwitchY (bool?): Use the limit the y-axis rotation? When  
                queried, this flag returns a boolean.  
                Properties: create, query, edit
        limitSwitchZ (bool?): Use the Limit the z-axis rotation? When  
                queried, this flag returns a boolean.  
                Properties: create, query, edit
        limitX (Queryable[Tuple[float, float]]?): Set lower and upper limits on the x-axis of  
                rotation.  Also turns on  
                the joint limit. When queried, this flag returns 2 floats.  
                Properties: create, query, edit
        limitY (Queryable[Tuple[float, float]]?): Set lower and upper limits on the y-axis of  
                rotation.  Also turns on  
                the joint limit. When queried, this flag returns 2 floats.  
                Properties: create, query, edit
        limitZ (Queryable[Tuple[float, float]]?): Set lower and upper limits on the z-axis of  
                rotation.  Also turns on  
                the joint limit. When queried, this flag returns 2 floats.  
                Properties: create, query, edit
        name (Queryable[str]?): Specifies the name of the joint. When queried,  
                this flag returns a string.  
                Properties: create, query, edit
        orientJoint (str?): The argument can be one of the following strings: xyz,  
                yzx, zxy, zyx, yxz, xzy, none.  
              
                It modifies the joint orientation and scale orientation  
                so that the axis indicated by the first letter in the argument  
                will be aligned with the vector from this joint to its first  
                child joint. For example, if the argument is "xyz", the x-axis will  
                point towards the child joint.  
              
                The alignment of the remaining two joint orient axes are  
                dependent on whether or not the -sao/-secondaryAxisOrient flag  
                is used. If the -sao flag is used, see the documentation for  
                that flag for how the remaining axes are aligned.  
              
                In the absence of a user specification for the secondary axis  
                orientation, the rotation axis indicated by the last letter in  
                the argument will be aligned with the vector perpendicular to  
                first axis and the vector from this joint to its parent joint.  
              
                The remaining axis is aligned according the right hand rule.  
              
                If the argument is "none", the joint orientation  
                will be set to zero and its effect to the hierarchy  
                below will be offset by modifying the scale  
                orientation.  
              
                The flag will be ignored if:  
              
                A. the joint has non-zero rotations when the argument  
                is not "none".  
              
                B. the joint does not have child joint, or the  
                distance to the child joint is zero when the argument  
                is not "none".  
              
                C. either flag -o or -so is set.  
                Properties: edit
        orientation (Queryable[Tuple[float, float, float]]?): The joint orientation. When queried, this flag  
                returns 3 floats.  
                Properties: create, query, edit
        position (Queryable[Tuple[float, float, float]]?): Specifies the position of the center of the joint.  
                This position may be relative to the joint's parent  
                or in absolute world coordinates (see -r and -a  
                below). When queried, this flag returns 3 floats.  
                Properties: create, query, edit
        radius (Queryable[float]?): Specifies the joint radius.  
                Properties: create, query, edit
        relative (bool?): The joint center position is relative to the joint's parent.  
                Properties: create, query, edit
        rotationOrder (Queryable[str]?): The rotation order of the joint. The  
                argument can be one of the following strings: xyz,  
                yzx, zxy, zyx, yxz, xzy.  
                Properties: create, query, edit
        scale (Queryable[Tuple[float, float, float]]?): Scale of the joint. When queried, this flag  
                returns 3 floats.  
                Properties: create, query, edit
        scaleCompensate (bool?): It sets the scaleCompenstate attribute of  
                the joint to the given argument. When this is true,  
                the scale of the parent joint will be compensated  
                before any rotation of this joint is applied, so that  
                the bone to the joint is scaled but not the bones to  
                its child joints. When queried, this flag returns an  
                boolean.  
                Properties: create, query, edit
        scaleOrientation (Queryable[Tuple[float, float, float]]?): Set the orientation of the coordinate axes for  
                scaling. When queried, this flag returns 3 floats.  
                Properties: create, query, edit
        secondaryAxisOrient (str?): The argument can be one of the following strings: xup, xdown,  
                yup, ydown, zup, zdown, none.  
              
                This flag is used in conjunction with the -oj/orientJoint  
                flag. It specifies the scene axis that the second axis should  
                align with. For example, a flag combination of "-oj yzx -sao yup"  
                would result in the y-axis pointing down the bone, the  
                z-axis oriented with the scene's positive y-axis, and  
                the x-axis oriented according to the right hand rule.  
                Properties: edit
        setPreferredAngles (bool?): Meaningful only in the edit mode. It sets the  
                preferred angles to the current joint angles.  
                Properties: edit
        stiffnessX (Queryable[float]?): Set the stiffness (from 0 to 100.0) for x-axis.  
                When queried, this flag returns a float.  
                Properties: create, query, edit
        stiffnessY (Queryable[float]?): Set the stiffness (from 0 to 100.0) for y-axis.  
                When queried, this flag returns a float.  
                Properties: create, query, edit
        stiffnessZ (Queryable[float]?): Set the stiffness (from 0 to 100.0) for z-axis.  
                When queried, this flag returns a float.  
                Properties: create, query, edit
        symmetry (bool?): Create a symmetric joint from the current joint.  
                Properties: create, edit
        symmetryAxis (str?): This flag specifies the axis used to mirror symmetric joints. Any combination of x, y, z can be used. This option is only used when the symmetry flag is set to True.  
                Properties: create, edit
        zeroScaleOrient (bool?): It sets the scale orientation to zero and  
                compensate the change by modifing the translation and  
                joint orientation for joint or rotation for general  
                transform of all its child transformations.  
              
                The flag will be ignored if the flag -so is set.  
                Properties: edit

    Returns:
        str: Command result

    Example:
    """

