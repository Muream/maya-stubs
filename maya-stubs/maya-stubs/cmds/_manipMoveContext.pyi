from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def manipMoveContext(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeHandle: Queryable[int] = ..., activeHandleNormal: Queryable[int] = ..., alignAlong: Tuple[float, float, float] = ..., bakePivotOri: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: Queryable[int] = ..., editPivotMode: bool = ..., editPivotPosition: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., interactiveUpdate: bool = ..., lastMode: Queryable[int] = ..., manipVisible: bool = ..., mode: Queryable[int] = ..., orientAxes: Queryable[Tuple[float, float, float]] = ..., orientJoint: Queryable[str] = ..., orientJointEnabled: bool = ..., orientObject: str = ..., orientTowards: Tuple[float, float, float] = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., position: bool = ..., postCommand: Callable[..., Any] = ..., postDragCommand: Tuple[Callable[..., Any], str] = ..., preCommand: Callable[..., Any] = ..., preDragCommand: Tuple[Callable[..., Any], str] = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAbout: int = ..., reflectionAxis: int = ..., reflectionTolerance: float = ..., resetPivotMode: Queryable[int] = ..., secondaryAxisOrient: Queryable[str] = ..., snap: bool = ..., snapComponentsRelative: bool = ..., snapLiveFaceCenter: bool = ..., snapLivePoint: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: Queryable[float] = ..., translate: Queryable[Tuple[float, float, float]] = ..., tweakMode: bool = ..., xformConstraint: Queryable[str] = ...) -> Union[str, int, bool, Tuple[float, float, float], float]:
    """This command can be used to create, edit, or query a move
    manip context.
    Note that the flags -s, -sv, -sr, -scr, -slp, -slf control
    the global behaviour of all move manip context.  Changing one
    context independently is not allowed.  Changing a context's
    behaviour using the above flags, will change all existing move
    manip context.
    Args:
        activeHandle (Queryable[int]?): Sets the default active handle for the manip.  That is, the handle  
                which should be initially active when the tool is activated.  
                Values can be:  
              
                0. X axis handle is active  
                1. Y axis handle is active  
                2. Z axis handle is active  
                3. Center handle (all 3 axes) is active (default)  
                Properties: query, edit
        activeHandleNormal (Queryable[int]?): 0. U axis handle is active  
                1. V axis handle is active  
                2. N axis handle is active ( default )  
                3. Center handle (all 3 axes) is active  
              
                applicable only when the manip mode is 3.  
                Properties: query, edit
        alignAlong (Tuple[float, float, float]?): Aligns active handle along vector.  
                Properties: create, edit
        bakePivotOri (bool?): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.  
                Properties: query, edit
        constrainAlongNormal (bool?): When true, transform constraints are applied along the vertex normal first  
                and only use the closest point when no intersection is found along the normal.  
                Properties: query, edit
        currentActiveHandle (Queryable[int]?): Sets the active handle for the manip.  
                Values can be:  
              
                0. X axis handle is active  
                1. Y axis handle is active  
                2. Z axis handle is active  
                3. Center handle (all 3 axes) is active  
                4. XY plane handle is active  
                5. YZ plane handle is active  
                6. XZ plane handle is active  
                Properties: query, edit
        editPivotMode (bool?): Returns true manipulator is in edit pivot mode  
                Properties: query
        editPivotPosition (bool?): Returns the current position of the edit pivot manipulator.  
                Properties: query
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        interactiveUpdate (bool?): Value can be : true or false.  
                This flag value is valid only if the mode is 3 i.e. move vertex normal.  
                Properties: query, edit
        lastMode (Queryable[int]?): Returns the previous translation mode.  
                Properties: query
        manipVisible (bool?): Returns true if the main translate manipulator is visible.  
                Properties: query
        mode (Queryable[int]?): Translate mode:  
              
                0. Object Space  
                1. Local Space  
                2. World Space (default)  
                3. Move Along Vertex Normal  
                4. Move Along Rotation Axis  
                5. Move Along Live Object Axis  
                6. Custom Axis Orientation  
                10. Component Space  
                Properties: query, edit
        orientAxes (Queryable[Tuple[float, float, float]]?): Orients manipulator rotating around axes by specified angles  
                Properties: query, edit
        orientJoint (Queryable[str]?): Specifies the type of orientation for joint orientation. Valid options are:  
                none, xyz, xzy, yxz, yzx, zxy, zyx.  
                Properties: query, edit
        orientJointEnabled (bool?): Specifies if joints should be reoriented when moved.  
                Properties: query, edit
        orientObject (str?): Orients manipulator to the passed in object/component  
                Properties: create, edit
        orientTowards (Tuple[float, float, float]?): Orients active handle towards world point  
                Properties: create, edit
        pinPivot (bool?): Pin component pivot. When the component pivot is set and pinned selection  
                changes will not reset the pivot position and orientation.  
                Properties: query, edit
        pivotOriHandle (bool?): When true, the pivot manipulator will show the orientation handle during editing.  
                Default is true.  
                Properties: query, edit
        position (bool?): Returns the current position of the manipulator  
                Properties: query
        postCommand (Callable[..., Any]?): Specifies a command to be executed when the tool is exited.  
                Properties: create, edit
        postDragCommand (Tuple[Callable[..., Any], str]?): Specifies a command and a node type. The command will be executed at  
                the end of a drag when a node of the specified type is in the selection.  
                Properties: create, edit
        preCommand (Callable[..., Any]?): Specifies a command to be executed when the tool is entered.  
                Properties: create, edit
        preDragCommand (Tuple[Callable[..., Any], str]?): Specifies a command and a node type. The command will be executed at  
                the start of a drag when a node of the specified type is in the selection.  
                Properties: create, edit
        preserveChildPosition (bool?): When false, the children objects move when their parent is moved.  
                When true, the worldspace position of the children will be maintained as  
                the parent is moved. Default is false.  
                Properties: query, edit
        preserveUV (bool?): When false, the uvs are not changes to match the vertex edit.  
                When true, the uvs are edited to project to new values to stop texture  
                swimming as vertices are moved.  
                Properties: query, edit
        reflection (bool?): This flag is obsolete. Reflection is now managed as part of selection itself  
                using the symmetricModeling command.
        reflectionAbout (int?): This flag is obsolete. Reflection is now managed as part of selection itself  
                using the symmetricModeling command.
        reflectionAxis (int?): This flag is obsolete. Reflection is now managed as part of selection itself  
                using the symmetricModeling command.
        reflectionTolerance (float?): This flag is obsolete. Reflection is now managed as part of selection itself  
                using the symmetricModeling command.
        resetPivotMode (Queryable[int]?): Specifies the mode used when resetting the pivot position. Available modes are:  
              
                0. Center pivot (on bounding box)  
                1. Zero pivot (object-space origin)  
                Properties: query, edit
        secondaryAxisOrient (Queryable[str]?): Specifies the global axis (in world coordinates) that should be used  
                to should be used to align the second axis of the orientJointType triple.  
                Valid options are xup, yup, zup, xdown, ydown, zdown, none.  
                Properties: query, edit
        snap (bool?): Value can be : true or false.  
                Enable/Disable the discrete move.  
                If set to true, the move manipulator of all the  
                move contexts would snap at discrete points  
                along the active handle during mouse drag.  The  
                interval between the points can be controlled  
                using the 'snapValue' flag.  
                Properties: query, edit
        snapComponentsRelative (bool?): Value can be : true or false.  
                If true, while snapping a group of CVs/Vertices, the  
                relative spacing between them will be preserved.  
                If false, all the CVs/Vertices will be snapped to the  
                target point  
                (is used during grid snap(hotkey 'x'), and  
                point snap(hotkey 'v'))  
                Depress the 'x' key before click-dragging the manip handle  
                and check to see the behaviour of moving a bunch of CVs,  
                with this flag ON and OFF.  
                Properties: query, edit
        snapLiveFaceCenter (bool?): Value can be : true or false.  
                If true, while moving on the live polygon object, the  
                move manipulator will snap to the face centers of the object.  
                Properties: query, edit
        snapLivePoint (bool?): Value can be : true or false.  
                If true, while moving on the live polygon object, the  
                move manipulator will snap to the vertices of the object.  
                Properties: query, edit
        snapPivotOri (bool?): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.  
                Properties: query, edit
        snapPivotPos (bool?): Snap pivot position. Modify pivot position when snapping the pivot to a component.  
                Properties: query, edit
        snapRelative (bool?): Value can be : true or false.  
                Applicable only when the snap is enabled.  
                If true, the snapValue is treated relative to the  
                original position before moving.  
                If false, the snapValue is treated relative to the  
                world origin.  
                NOTE:    If in local/object Space Mode,  
                the snapRelative should be ON.  
                Absolute discrete move is not supported  
                in local/object mode.  
                Properties: query, edit
        snapValue (Queryable[float]?): Applicable only when the snap is enabled.  
                The manipulator of all move contexts would move in  
                steps of 'snapValue'  
                Properties: query, edit
        translate (Queryable[Tuple[float, float, float]]?): Returns the translation of the manipulator for its current orientation/mode.  
                Properties: query, edit
        tweakMode (bool?): When true, the manipulator is hidden and highlighted components can be selected  
                and moved in one step using a click-drag interaction.  
                Properties: query, edit
        xformConstraint (Queryable[str]?): none - no transform constraint  
                edge - edge transform constraint  
                surface - surface transform constraint  
                Properties: query, edit

    Returns:
        str: The name of the new context

    Example:
    """

