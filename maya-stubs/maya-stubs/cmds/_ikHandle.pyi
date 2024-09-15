from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikHandle(*args: str, edit: bool = ..., query: bool = ..., autoPriority: bool = ..., connectEffector: bool = ..., createCurve: bool = ..., createRootAxis: bool = ..., curve: Queryable[str] = ..., disableHandles: bool = ..., enableHandles: bool = ..., endEffector: Queryable[str] = ..., exists: str = ..., forceSolver: bool = ..., freezeJoints: bool = ..., jointList: bool = ..., name: Queryable[str] = ..., numSpans: int = ..., parentCurve: bool = ..., positionWeight: Queryable[float] = ..., priority: Queryable[int] = ..., rootOnCurve: bool = ..., rootTwistMode: bool = ..., setupForRPsolver: bool = ..., simplifyCurve: bool = ..., snapCurve: bool = ..., snapHandleFlagToggle: bool = ..., snapHandleToEffector: bool = ..., solver: Queryable[str] = ..., startJoint: Queryable[str] = ..., sticky: Queryable[str] = ..., twistType: Queryable[str] = ..., weight: Queryable[float] = ...) -> Union[str, bool, float, int]:
    """The handle command is used to create, edit, and query a handle
    within Maya.  The standard edit (-e) and query (-q) flags are
    used for edit and query functions.If there are 2 joints selected and neither -startJoint nor
    -endEffector flags are not specified, then the handle will be
    created from the selected joints.If a single joint is selected and neither -startJoint nor
    -endEffector flags are specified, then the handle will be
    created with the selected joint as the end-effector and the
    start joint will be the top of the joint chain containing the
    end effector.The default values of the flags are:These attributes can be specified in creation mode, edited in
    edit mode (-e) or queried in query mode (-q).
    Args:
        autoPriority (bool?): Specifies that this handle's priority is assigned  
                automatically.  The assigned priority will be based on  
                the hierarchy distance from the root of the skeletal  
                chain to the start joint of the handle.  
                Properties: edit
        connectEffector (bool?): This option is set to true as default, meaning that  
                end-effector translate is connected with the endJoint translate.  
                Properties: create, edit
        createCurve (bool?): Specifies if a curve should automatically be created for  
                the ikSplineHandle.  
                Properties: create
        createRootAxis (bool?): Specifies if a root transform should automatically  
                be created above the joints affected by the ikSplineHandle.  
                This option is used to prevent the root flipping singularity  
                on a motion path.  
                Properties: create
        curve (Queryable[str]?): Specifies the curve to be used by the ikSplineHandle. Joints  
                will be moved to align with this curve. This flag is mandatory if you use  
                the -freezeJoints option.  
                Properties: create, query, edit
        disableHandles (bool?): set given handles to full fk (ikBlend attribute = 0.0)  
                Properties: edit
        enableHandles (bool?): set given handles to full ik (ikBlend attribute = 1.0)  
                Properties: edit
        endEffector (Queryable[str]?): Specifies the end-effector of the handle's joint chain.  
                The end effector may be specified with a joint or an  
                end-effector.  If a joint is specified, an end-effector will  
                be created at the same position as the joint and this  
                new end-effector will be used as the end-effector.  
                Properties: create, query, edit
        exists (str?): Indicates if the specified handle exists or not.  
                Properties: edit
        forceSolver (bool?): Forces the solver to be used everytime.  
                It could also be known as animSticky. So, after you set  
                the first key the handle is sticky.  
                Properties: create, query, edit
        freezeJoints (bool?): Forces the curve, specfied by -curve option, to align itself along the existing joint chain.  
                When false, or unspecified, the joints will be moved to positions along the specified curve.  
                Properties: create, edit
        jointList (bool?): Returns the list of joints that the handle is manipulating.  
                Properties: edit
        name (Queryable[str]?): Specifies the name of the handle.  
                Properties: create, query, edit
        numSpans (int?): Specifies the number of spans in the  
                automatically generated curve of the ikSplineHandle.  
                Properties: create
        parentCurve (bool?): Specifies if the curve should automatically  
                be parented to the parent of the first joint affected  
                by the ikSplineHandle.  
                Properties: create
        positionWeight (Queryable[float]?): Specifies the position/orientation weight of a handle.  
                This is used to compute the "distance" between the goal  
                position and the end-effector position.  A positionWeight of  
                1.0 computes the distance as the distance between  
                positions only and ignores the orientations.  A positionWeight  
                of 0.0 computes the distance as the distance between the  
                orientations only and ignores the positions.  A positionWeight  
                of 0.5 attempts to weight the distances equally but  
                cannot actually compute this due to unit differences.  
                Because there is no way to add linear units and angular units.  
                Properties: create, query, edit
        priority (Queryable[int]?): Sets the priority of the handle.  Logically, all handles  
                with a lower number priority are solved before any  
                handles with a higher numbered priority.  (All handles  
                of priority 1 are solved before any handles of priority  
                2 and so on.)  Handle priorities must be ] 0.  
                Properties: create, query, edit
        rootOnCurve (bool?): Specifies if the root is  
                locked onto the curve of the ikSplineHandle.  
                Properties: create, query, edit
        rootTwistMode (bool?): Specifies whether the start joint is allowed to  
                twist or not. If not, then the required twist is distributed over the  
                remaining joints. This applies to all the twist types.  
                Properties: create, query, edit
        setupForRPsolver (bool?): If the flag is set and ikSolver is ikRPsolver, call  
                RPRotateSetup for the new ikHandle. It is for ikRPsolver only.  
                Properties: edit
        simplifyCurve (bool?): Specifies if the ikSplineHandle curve should be simplified.  
                Properties: create
        snapCurve (bool?): Specifies if the curve should automatically  
                snap to the first joint affected by the ikSplineHandle.  
                Properties: create
        snapHandleFlagToggle (bool?): Specifies that the handle position should be snapped to  
                the end-effector position if the end-effector is moved  
                by the user.  Setting this flag on allows you to use  
                forward kinematics to pose or adjust your skeleton and  
                then to animate it with inverse kinematics.  
                Properties: create, query, edit
        snapHandleToEffector (bool?): All handles are immediately moved so that the handle  
                position and orientation matches the end-effector  
                position and orientation.  
                Properties: edit
        solver (Queryable[str]?): Specifies the solver.  The complete list of  
                available solvers may not be known until run-time  
                because some of the solvers may be implemented as  
                plug-ins.  Currently the only valid solver are  
                ikRPsolver, ikSCsolver and ikSplineSolver.  
                Properties: create, query, edit
        startJoint (Queryable[str]?): Specifies the start joint of the handle's joint chain.  
                Properties: create, query, edit
        sticky (Queryable[str]?): Specifies that this handle is "sticky". Valid values are "off",  
                "sticky", "superSticky". Sticky handles  
                are solved when the skeleton is being manipulated  
                interactively.  If a character has sticky feet, the  
                solver will attempt to keep them in the same position as  
                the user moves the character's root.  If they were not  
                sticky, they would move along with the root.  
                Properties: create, query, edit
        twistType (Queryable[str]?): Specifies the type of interpolation to  
                be used by the ikSplineHandle.  The interpolation options are  
                "linear", "easeIn", "easeOut", and "easeInOut".  
                Properties: create, query, edit
        weight (Queryable[float]?): Specifies the handles weight in error calculations.  The  
                weight only applies when handle goals are in conflict  
                and cannot be solved simultaneously.  When this happens,  
                a solution is computed that weights the "distance" from  
                each goal to the solution by the handle's weight and  
                attempts to minimize this value.  The weight must be ]= 0.  
                Properties: create, query, edit

    Returns:
        str: Command result

    Example:
    """

