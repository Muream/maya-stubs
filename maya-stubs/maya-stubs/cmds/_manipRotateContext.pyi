from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def manipRotateContext(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeHandle: Queryable[int] = ..., alignAlong: Tuple[float, float, float] = ..., bakePivotOri: bool = ..., centerTrackball: bool = ..., constrainAlongNormal: bool = ..., currentActiveHandle: Queryable[int] = ..., editPivotMode: bool = ..., editPivotPosition: bool = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., lastMode: Queryable[int] = ..., manipVisible: bool = ..., mode: Queryable[int] = ..., modifyTranslation: bool = ..., orientAxes: Queryable[Tuple[float, float, float]] = ..., orientObject: str = ..., orientTowards: Tuple[float, float, float] = ..., pinPivot: bool = ..., pivotOriHandle: bool = ..., position: bool = ..., postCommand: Callable[..., Any] = ..., postDragCommand: Tuple[Callable[..., Any], str] = ..., preCommand: Callable[..., Any] = ..., preDragCommand: Tuple[Callable[..., Any], str] = ..., preserveChildPosition: bool = ..., preserveUV: bool = ..., reflection: bool = ..., reflectionAbout: int = ..., reflectionAxis: int = ..., reflectionTolerance: float = ..., resetPivotMode: Queryable[int] = ..., rotate: Queryable[Tuple[float, float, float]] = ..., snap: bool = ..., snapPivotOri: bool = ..., snapPivotPos: bool = ..., snapRelative: bool = ..., snapValue: Queryable[float] = ..., tweakMode: bool = ..., useCenterPivot: bool = ..., useManipPivot: bool = ..., useObjectPivot: bool = ..., xformConstraint: Queryable[str] = ...) -> Union[str, int, bool, Tuple[float, float, float], float]:
    """This command can be used to create, edit, or query a rotate manip context.
    Args:
        activeHandle (Queryable[int]?): Sets the default active handle for the manip.  That is, the handle  
                which should be initially active when the tool is activated.  
                Values can be:  
              
                0. X axis handle is active  
                1. Y axis handle is active  
                2. Z axis handle is active  
                3. View rotation handle (outer ring) is active (default)  
                Properties: query, edit
        alignAlong (Tuple[float, float, float]?): Aligns active handle along vector.  
                Properties: create, edit
        bakePivotOri (bool?): Bake pivot orientation. Automatically bake pivot orientation changes into the transform hierarchy / geometry.  
                Properties: query, edit
        centerTrackball (bool?): Specify if the center is to be handled like a trackball  
                Properties: create, query, edit
        constrainAlongNormal (bool?): When true, transform constraints are applied along the vertex normal first  
                and only use the closest point when no intersection is found along the normal.  
                Properties: query, edit
        currentActiveHandle (Queryable[int]?): Sets the active handle for the manip.  
                Values can be:  
              
                0. X axis handle is active  
                1. Y axis handle is active  
                2. Z axis handle is active  
                3. View rotation handle (outer ring) is active  
                4. Arc Ball is active  
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
        lastMode (Queryable[int]?): Returns the previous rotation mode.  
                Properties: query
        manipVisible (bool?): Returns true if the rotate manipulator is visible.  
                Properties: query
        mode (Queryable[int]?): Rotate mode:  
              
                0. Object Space (default)  
                1. World Space  
                2. Gimbal Mode  
                3. Custom Axis Orientation  
                10. Component Space  
                Properties: query, edit
        modifyTranslation (bool?): When false, and an object is rotated about a point other than its rotate pivot,  
                its rotateTranslate attribute is modified to put the object at the  
                correct position. When true, its translate attribute is used instead.  
                Default is false.  
                Properties: query, edit
        orientAxes (Queryable[Tuple[float, float, float]]?): Orients manipulator rotating around axes by specified angles  
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
        position (bool?): Returns the current position of the manipulator.  
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
        preserveChildPosition (bool?): When false, the children objects move when their parent is rotated.  
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
        rotate (Queryable[Tuple[float, float, float]]?): Returns the rotation of the manipulator for its current orientation/mode.  
                Properties: query, edit
        snap (bool?): Specify that the manipulation is to use absolute snap  
                Properties: create, query, edit
        snapPivotOri (bool?): Snap pivot orientation. Modify pivot orientation when snapping the pivot to a component.  
                Properties: query, edit
        snapPivotPos (bool?): Snap pivot position. Modify pivot position when snapping the pivot to a component.  
                Properties: query, edit
        snapRelative (bool?): Specify that the manipulation is to use relative snap  
                Properties: create, query, edit
        snapValue (Queryable[float]?): Specify the snapping value  
                Properties: create, query, edit
        tweakMode (bool?): When true, the manipulator is hidden and highlighted components can be selected  
                and rotated in one step using a click-drag interaction.  
                Properties: query, edit
        useCenterPivot (bool?): When true, use the center of the selection's bounding box as the center of the rotation  
                (for all objects).  
                Properties: query, edit
        useManipPivot (bool?): When true, use the manipulator's center as the center of the rotation  
                (for all objects).  
                Properties: query, edit
        useObjectPivot (bool?): When true, use each object's pivot as the center of its rotation.  
                Properties: query, edit
        xformConstraint (Queryable[str]?): none - no transform constraint  
                edge - edge transform constraint  
                surface - surface transform constraint  
                Properties: query, edit

    Returns:
        str: (name of the new context)

    Example:
    """

