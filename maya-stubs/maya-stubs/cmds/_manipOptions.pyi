from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def manipOptions(*, query: bool = ..., enableSmartDuplicate: bool = ..., enableSmartExtrude: bool = ..., forceRefresh: bool = ..., handleSize: Queryable[float] = ..., hideManipOnCtrl: bool = ..., hideManipOnShift: bool = ..., hideManipOnShiftCtrl: bool = ..., linePick: Queryable[float] = ..., lineSize: Queryable[float] = ..., middleMouseRepositioning: bool = ..., pivotRotateHandleOffset: Queryable[int] = ..., planeHandleOffset: Queryable[int] = ..., pointSize: Queryable[float] = ..., preselectHighlight: bool = ..., refreshMode: Queryable[int] = ..., relative: bool = ..., rememberActiveHandle: bool = ..., rememberActiveHandleAfterToolSwitch: bool = ..., scale: Queryable[float] = ..., showExtrudeSliders: bool = ..., showPivotRotateHandle: bool = ..., showPlaneHandles: bool = ..., smartDuplicateType: Queryable[int] = ...) -> Union[bool, float, int]:
    """Changes the global manipulator parameters
    Args:
        enableSmartDuplicate (bool?): Enables Shift-Duplicate option on t/r/s manips.  
                Properties: create, query
        enableSmartExtrude (bool?): Enables Shift-Extrude option on t/r/s manips.  
                Properties: create, query
        forceRefresh (bool?): Force a refresh if there is any deferred evaluation.  
                Properties: create
        handleSize (Queryable[float]?): Sets the maximum handles size in pixels, for small handles  
                Properties: create, query
        hideManipOnCtrl (bool?): Hide transform manip when the Ctrl key is pressed.  
                Properties: create, query
        hideManipOnShift (bool?): Hide transform manip when the Shift key is pressed.  
                Properties: create, query
        hideManipOnShiftCtrl (bool?): Hide transform manip when the Shift and Ctrl keys are both pressed.  
                Properties: create, query
        linePick (Queryable[float]?): Set the width of picking zone for long handles  
                Properties: create, query
        lineSize (Queryable[float]?): Set the width of long handles (drawn as lines)  
                Properties: create, query
        middleMouseRepositioning (bool?): Specify if the middle mouse should reposition  
                Properties: create, query
        pivotRotateHandleOffset (Queryable[int]?): Set the offset of the pivot rotation handle.  
                Properties: create, query
        planeHandleOffset (Queryable[int]?): Set the offset of the planar drag handles.  
                Properties: create, query
        pointSize (Queryable[float]?): Set the size of points (used to display previous states)  
                Properties: create, query
        preselectHighlight (bool?): Set whether manip handles should be highlighted when moving mouse.  
                Properties: create, query
        refreshMode (Queryable[int]?): Set the global refresh mode.  
                Properties: create, query
        relative (bool?): All values are interpreted as multiplication factors instead  
                of final values.  
                Properties: create
        rememberActiveHandle (bool?): Set whether manip handles should be remembered after selection change.  
                Properties: create, query
        rememberActiveHandleAfterToolSwitch (bool?): Set whether manip handles should be remembered after manipulator change.  
                Properties: create, query
        scale (Queryable[float]?): Global scaling factor of all manipulators  
                Properties: create, query
        showExtrudeSliders (bool?): Specify if the extrude sliders are to be shown on the manip  
                Properties: create, query
        showPivotRotateHandle (bool?): Toggles the visibility of the pivot rotation handle.  
                Properties: create, query
        showPlaneHandles (bool?): Toggles the visibility of the planar drag handles.  
                Properties: create, query
        smartDuplicateType (Queryable[int]?): Change Shift-Duplicate or Shift-Extrude between Copy and Instance on t/r/s manips.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

