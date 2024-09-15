from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def jointCtx(*args: Any, edit: bool = ..., query: bool = ..., autoJointOrient: Queryable[str] = ..., autoPriorityH: bool = ..., createIKHandle: bool = ..., degreeOfFreedomJ: Queryable[str] = ..., exists: bool = ..., forceSolverH: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., jointAutoLimits: bool = ..., jointOrientationJ: Queryable[Tuple[float, float, float]] = ..., largeBoneLength: Queryable[float] = ..., largeBoneRadius: Queryable[float] = ..., poWeightH: Queryable[float] = ..., priorityH: Queryable[int] = ..., scaleCompensateJ: bool = ..., scaleJ: Queryable[Tuple[float, float, float]] = ..., scaleOrientationJ: Queryable[Tuple[float, float, float]] = ..., secondaryAxisOrient: Queryable[str] = ..., smallBoneLength: Queryable[float] = ..., smallBoneRadius: Queryable[float] = ..., snapHandleH: bool = ..., solverTypeH: Queryable[str] = ..., stickyH: Queryable[str] = ..., symmetry: bool = ..., symmetryAxis: Queryable[str] = ..., variableBoneSize: bool = ..., weightH: Queryable[float] = ...) -> Union[str, bool, Tuple[float, float, float], float, int]:
    """The joint context command (jointCtx) updates the parameters of the
    joint tool. The options for the tool will be set by the flags the user
    specifies.
    Args:
        autoJointOrient (Queryable[str]?): Specifies the joint orientation. Valid string choices are  
                permutations of the axes; "none", "xyz", "yzx", "zxy", "xzy", "yxz",  
                "zyx". The first letter determines which axis is aligned with the  
                bone.  
                C: The default is "xyz".  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        autoPriorityH (bool?): Specifies if the ikHandle's priority is assigned  
                automatically.  
                C: The default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        createIKHandle (bool?): Enables the joint tool to create an ikHandle when the tool  
                is completed.  
                C: The default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        degreeOfFreedomJ (Queryable[str]?): Specifies the degrees of freedom for all of the joints  
                created by the tool. Valid string choices are the free axes;  
                "x", "y", "z", "xy", "xz", "yz", "xyz", and "none".  
                C: The default is "xyz".  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        forceSolverH (bool?): Specifies if the ikSolver for the ikHandle is enabled.  
                C: The default is on.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        jointAutoLimits (bool?): Automatically computes the joint limits based on the  
                kind of joint created.   
                C: The default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        jointOrientationJ (Queryable[Tuple[float, float, float]]?): Sets the orientation of the joints created by the tool.  
                If autoJointOrient in on, these values will be ignored.  
                C: The default is 0 0 0.  
                Q: When queried, this flag returns an array of three floats.  
                Properties: create, query, edit
        largeBoneLength (Queryable[float]?): Specifies the length above which bones should be assigned the largeBoneRadius.  
                Properties: create, query, edit
        largeBoneRadius (Queryable[float]?): Specifies the radius for bones whose length is above the largeBoneLength  
                Properties: create, query, edit
        poWeightH (Queryable[float]?): Specifies the position/orientation weight of the ikHandle.  
                C: The default is 1.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        priorityH (Queryable[int]?): Specifies the priority of the ikHandle.  
                C: The default is on.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        scaleCompensateJ (bool?): Specifies if scale compensate is enabled.  
                C: The default is on.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        scaleJ (Queryable[Tuple[float, float, float]]?): Sets the scale for the joints created by the tool.  
                C: The default is 1 1 1.  
                Q: When queried, this flag returns an array of three floats.  
                Properties: create, query, edit
        scaleOrientationJ (Queryable[Tuple[float, float, float]]?): Sets the current value for the scale orientation.  
                If autoJointOrient in on, these values will be ignored.  
                C: The default is 0 0 0.  
                Q: When queried, this flag returns an array of three floats.  
                Properties: create, query, edit
        secondaryAxisOrient (Queryable[str]?): Specifies the orientation of the secondary rotate axis.  
                Valid string choices are: "xup", "xdown",  
                "yup", "ydown", "zup", "zdown", "none".  
                Properties: create, query, edit
        smallBoneLength (Queryable[float]?): Specifies the length below which bones should be assigned the smallBoneRadius.  
                Properties: create, query, edit
        smallBoneRadius (Queryable[float]?): Specifies the radius for bones whose length is below the smallBoneLength.  
                Properties: create, query, edit
        snapHandleH (bool?): Sepcifies if snapping is enabled for the ikHandle.   
                C: The default is on.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        solverTypeH (Queryable[str]?): Sets the name of the solver to use with the ikHandle.   
                C: The default is the solver set to the default in the user  
                preferences.  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        stickyH (Queryable[str]?): Specifies if the ikHandle is sticky or not. If "sticky" is  
                passed then the ikHandle will be sticky. If "off" is used then  
                ikHandle stickiness will be turned off.  
                C: The default is "off".  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        symmetry (bool?): Automaticaly create a symmetry joint based if symmetry is on.   
                C: The default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        symmetryAxis (Queryable[str]?): Automaticaly create a symmetry joint use x, y , z axis or combination to do the symmetry.   
                C: The default is x.  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        variableBoneSize (bool?): Specifies whether or not variable bone length and radius settings should be used.  
                Properties: create, query, edit
        weightH (Queryable[float]?): Specifies the weight of the ikHandle. The weight is  
                relative to the other ikHandles in the scene.  
                C: The default is 1.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit

    Returns:
        str: The name of the context.

    Example:
    """

