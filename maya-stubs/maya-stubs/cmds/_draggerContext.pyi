from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def draggerContext(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., anchorPoint: Queryable[Tuple[float, float, float]] = ..., button: Queryable[int] = ..., currentStep: Queryable[int] = ..., cursor: Queryable[str] = ..., dragCommand: Queryable[Callable[..., Any]] = ..., dragPoint: Queryable[Tuple[float, float, float]] = ..., drawString: str = ..., exists: bool = ..., finalize: Queryable[Callable[..., Any]] = ..., helpString: Queryable[str] = ..., history: bool = ..., holdCommand: Queryable[Callable[..., Any]] = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., initialize: Queryable[Callable[..., Any]] = ..., modifier: Queryable[str] = ..., name: str = ..., plane: Tuple[float, float, float] = ..., prePressCommand: Queryable[Callable[..., Any]] = ..., pressCommand: Queryable[Callable[..., Any]] = ..., projection: Queryable[str] = ..., releaseCommand: Queryable[Callable[..., Any]] = ..., snapping: bool = ..., space: Queryable[str] = ..., stepsCount: Queryable[int] = ..., undoMode: Queryable[str] = ...) -> Union[str, Tuple[float, float, float], int, Callable[..., Any], bool]:
    """The draggerContext allows the user to program the behavior of the mouse
    or an equivalent dragging device in MEL.
    Args:
        anchorPoint (Queryable[Tuple[float, float, float]]?): Anchor point (double array) where dragger was initially pressed.  
                Properties: query
        button (Queryable[int]?): Returns the current mouse button (1,2,3).  
                Properties: query
        currentStep (Queryable[int]?): Current step (press-drag-release sequence) for dragger context.  
                When queried before first press event happened, returns 0.  
                Properties: query
        cursor (Queryable[str]?): Cursor displayed while context is active.  Valid values are:  
                "default", "hand", "crossHair", "dolly", "track", and "tumble".  
                Properties: create, query, edit
        dragCommand (Queryable[Callable[..., Any]]?): Command called when mouse dragger is dragged.  
                Properties: create, query, edit
        dragPoint (Queryable[Tuple[float, float, float]]?): Drag point (double array) current position of dragger during drag.  
                Properties: query
        drawString (str?): A string to be drawn at the current position of the pointer.  
                Properties: create, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        finalize (Queryable[Callable[..., Any]]?): Command called when the tool is exited.  
                Properties: create, query, edit
        helpString (Queryable[str]?): Help string for context  
                Properties: query
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
                Properties: create
        holdCommand (Queryable[Callable[..., Any]]?): Command called when mouse dragger is held.  
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
        initialize (Queryable[Callable[..., Any]]?): Command called when the tool is entered.  
                Properties: create, query, edit
        modifier (Queryable[str]?): Returns the current modifier type:  ctrl, alt or none.  
                Properties: query
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        plane (Tuple[float, float, float]?): Provide normal of projection plane (see -projection flag for details).  
                Properties: create, edit
        prePressCommand (Queryable[Callable[..., Any]]?): Command called when mouse dragger is pressed. It is called before  
                pressCommand, so it can be used for initialization of context.  
                Properties: create, query, edit
        pressCommand (Queryable[Callable[..., Any]]?): Command called when mouse dragger is pressed.  
                Properties: create, query, edit
        projection (Queryable[str]?): Sets current projection of drag point. Valid types are:  
              
              
                viewPlane  
                project to view plane  
              
              
                objectViewPlane  
                project to object plane (parallel to view plane)  
              
              
                objectPlane  
                project to specified plane defined by object location and normal (default) 0,1,0  
              
              
                plane  
                project to specified plane defined by origin and normal (default) 0,1,0  
              
              
                sketchPlane  
                project to sketch plane  
              
              
                xAxis  
                project to closest point on X axis  
              
              
                yAxis  
                project to closest point on Y axis  
              
              
                zAxis  
                project to closest point on Z axis  
              
              
                boundingSphere  
                project to closest point on object sphere bounds  
              
              
                boundingBox  
                project to closest point on object bounding box  
                Properties: create, query, edit
        releaseCommand (Queryable[Callable[..., Any]]?): Command called when mouse dragger is released.  
                Properties: create, query, edit
        snapping (bool?): Enable/disable snapping for dragger context.  
                Properties: create, query, edit
        space (Queryable[str]?): Sets current space that coordinates are reported in. Types are:  
              
              
                world  
                world space (global)  
              
              
                object  
                object space (local)  
              
              
                screen  
                screen space  
                Properties: create, query, edit
        stepsCount (Queryable[int]?): Number of steps (press-drag-release sequences) for dragger context.  
                When combined with undoMode flag, several steps might be recorded as  
                single undo action.  
                Properties: create, query, edit
        undoMode (Queryable[str]?): Undo queue mode for the context actions.  
                Acceptable values are:  
              
                "all" default behaviour when every action that happens during  
                dragger context activity is recorded as an individual undo chunk.  
                "step" - all the actions that happen between each press and  
                release are combined into one undo chunk.  
                "sequence" - all the actions that happen between very first press  
                and very last release are combined into single undo chunk. This works  
                exactly the same as "step" for a single step dragger context.  
                Properties: create, query, edit

    Returns:
        str: The name of the context.

    Example:
    """

