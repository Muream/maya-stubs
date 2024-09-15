from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def viewManip(*args: Any, query: bool = ..., bottomLeft: bool = ..., bottomRight: bool = ..., compassAngle: Queryable[float] = ..., dragSnap: bool = ..., drawCompass: bool = ..., fitToView: bool = ..., frontParameters: Queryable[str] = ..., goDefault: bool = ..., goHome: bool = ..., homeParameters: Queryable[str] = ..., levelCamera: bool = ..., minOpacity: Queryable[float] = ..., namespace: Queryable[str] = ..., postCommand: Queryable[str] = ..., preCommand: Queryable[str] = ..., preserveSceneUp: bool = ..., resetFront: bool = ..., resetHome: bool = ..., restoreCenter: bool = ..., selectionLockParameters: Queryable[str] = ..., setFront: bool = ..., setHome: bool = ..., size: Queryable[str] = ..., toggleSelectionLock: bool = ..., topLeft: bool = ..., topRight: bool = ..., visible: bool = ..., zoomToFitScene: bool = ...) -> Union[bool, float, str]:
    """Mel access to the view cube manipulator.
    Args:
        bottomLeft (bool?): Positions the cube in the bottom left of the screen.  
                Properties: create, query
        bottomRight (bool?): Positions the cube in the bottom right of the screen.  
                Properties: create, query
        compassAngle (Queryable[float]?): Angle (in degrees) to rotate the compass.  
                Properties: create, query
        dragSnap (bool?): Enable snapping of orbit direction to view cube part directions during drag operation.  
                Properties: create, query
        drawCompass (bool?): Show compass below the view cube.  
                Properties: create, query
        fitToView (bool?): Fits the scene bounding box to the active view.  
                Properties: create
        frontParameters (Queryable[str]?): Parameter string for the front position  
                Properties: create, query
        goDefault (bool?): Go to the default position  
                Properties: create, query
        goHome (bool?): Go to the home position  
                Properties: create, query
        homeParameters (Queryable[str]?): Parameter string for the home position  
                Properties: create, query
        levelCamera (bool?): Flattens the camera view rotation relative to the ground plane.  
                Properties: create
        minOpacity (Queryable[float]?): Opacity level (in range [0,1]) on view cube when the cursor is away from it (it is fully opaque when the cursor is in the view cube area).  
                Properties: create, query
        namespace (Queryable[str]?): Namespace to use for the object  
                Properties: create, query
        postCommand (Queryable[str]?): Command to run after moving  
                Properties: create, query
        preCommand (Queryable[str]?): Command to run before moving  
                Properties: create, query
        preserveSceneUp (bool?): Specify whether the scene "up" direction should be preserved  
                Properties: create, query
        resetFront (bool?): Reset the front position  
                Properties: create, query
        resetHome (bool?): Reset the home position  
                Properties: create, query
        restoreCenter (bool?): Repositions the pivot point for orbiting/tumbling the scene to the center  
                of the scene's bounding box.  
                Properties: create
        selectionLockParameters (Queryable[str]?): String containing the selection lock parameters  
                Properties: create, query
        setFront (bool?): Set the front view to the current one  
                Properties: create
        setHome (bool?): Set the home view to the current one  
                Properties: create
        size (Queryable[str]?): Set or query the size of the View Cube, which can be one of "tiny",  
                "small", "normal", "large" or "auto". When set to "auto" the View Cube  
                will be automatically set to the size most appropriate for the view.  
                Properties: create, query
        toggleSelectionLock (bool?): Toggle the selection lock  
                Properties: create
        topLeft (bool?): Positions the cube in the top left of the screen.  
                Properties: create, query
        topRight (bool?): Positions the cube in the top right of the screen.  
                Properties: create, query
        visible (bool?): Shows/hides the view manip.  
                Properties: create, query
        zoomToFitScene (bool?): Zoom the camera during animated transitions to fit the scene object in the viewport.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

