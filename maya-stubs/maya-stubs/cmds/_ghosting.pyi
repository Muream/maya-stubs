from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ghosting(*args: str, edit: bool = ..., query: bool = ..., action: str = ..., allGhostedObjects: bool = ..., allInRange: bool = ..., customFrames: Queryable[Multiuse[int]] = ..., enable: bool = ..., farOpacity: Queryable[float] = ..., frames: bool = ..., geometryFilter: bool = ..., ghostedObjects: bool = ..., ghostsStep: Queryable[int] = ..., hierarchy: bool = ..., jointFilter: bool = ..., locatorFilter: bool = ..., mode: Queryable[str] = ..., nearOpacity: Queryable[float] = ..., postColor: Queryable[Tuple[float, float, float]] = ..., postFrames: Queryable[int] = ..., preColor: Queryable[Tuple[float, float, float]] = ..., preFrames: Queryable[int] = ..., preset: Queryable[str] = ..., resetAll: bool = ..., useDriver: bool = ...) -> Union[bool, List[str], List[float], float, str, List[int], Multiuse[int], int, Tuple[float, float, float]]:
    """Provides an aggregated interface to all of the node-base ghosting parameters, as well
    as the global preferences used by this command for ghosting actions.
    Query the 'enable' flag to check if ghost drawing is currently enabled.
    If you run in create mode with no 'action' set then you will be modifying the current values of the ghosting parameters.
    If you have 'action=ghost' set then you will be modifying the current values of the ghosting parameters and then applying them to selected objects.OGS, ghosting
    Args:
        action (str?): Define the actions to be performed by the command. Legal values are  
                "ghost", "unghost", and "unghostAll".  
                The "ghost" will try to enable ghosting on all _visible_ DAG objects in the selection list.  
                Imtermediate transform nodes will only be ghosted if axis display are active.  
                Properties: create
        allGhostedObjects (bool?): Only works in edit mode, specifying that the edits are to be applied to all ghosted objects instead of just the selected ones.  
                Properties: edit
        allInRange (bool?): In create mode, define the default value for whether keyframe mode should use every keyframe in the playback range or use the specified values.  
                In edit mode, modify the all-in-range value for all ghosts.  
                In create mode with the "ghost" action, also set the custom ghost all-in-range value for the selected objects.  
                Properties: create, query, edit
        customFrames (Queryable[Multiuse[int]]?): In create mode, define the default value for the list of custom ghost frames.  
                In edit mode, modify the custom ghost frames for all ghosts. The special frame number "-9999999" is used  
                to remove all custom frames, circumventing a quirk in the command engine that does not allow passing an empty list.  
                In create mode with the "ghost" action, also set the custom ghost frames for the selected objects.  
                Properties: create, query, edit, multiuse
        enable (bool?): Enables or disables ghost visibility on the entire scene. This does not modify  
                any of the node ghosting attributes, it only globally enables or disables the  
                drawing of any ghosts that have been defined on nodes.  
                This is a preference-based flag so its value will persist between sessions,  
                even if you load a new file with different ghost attribute settings.  
                Properties: create, query
        farOpacity (Queryable[float]?): In create mode, define the default value for the opacity value for ghosts farthest away from the current time.  
                In edit mode, modify the opacity value of ghosts farthest away from the current time for all ghosts.  
                In create mode with the "ghost" action, also set the opacity value of ghosts farthest away from the current time for the selected objects.  
                Properties: create, query, edit
        frames (bool?): Queries the current set of ghost frames on the selected objects based on the ghosting  
                mode, parameters set on the object, and the current time when relevant. Ignores the state  
                of the ghosting enabled flag.  
                Properties: query
        geometryFilter (bool?): In create mode, enable or disable the default ghost geometry filter.  
                In create mode with the "ghost" action set, also filter the selection to omit geometry nodes if this flag is false.  
                Properties: create, query, edit
        ghostedObjects (bool?): Only works in query mode to find the names of all currently ghosted DAG nodes.  
                Properties: query
        ghostsStep (Queryable[int]?): In create mode, define the default value for the number of steps (keyframes or frames) between ghosts.  
                In edit mode, modify the number of steps (keyframes or frames) between ghosts.  
                In create mode with the "ghost" action, also set the default number of steps (keyframes or frames) between ghosts for the selected objects.  
                Properties: create, query, edit
        hierarchy (bool?): Enables or disables the ghost hierarchy default value. When no ghosting action is set it does  
                not modify any of the node ghosting attributes, it only sets the preference for how  
                future commands will filter the list of affected nodes.  
                When used in conjunction with a ghosting action it will fist set the preference value and  
                then use that new value as a filter on the ghosting action. If a ghosting action is specified  
                without this flag then the current value of the preference is used in its place.  
                This is a preference-based flag so its value will persist between sessions,  
                even if you load a new file with different ghost attribute settings.  
                Properties: create, query, edit
        jointFilter (bool?): In create mode, enable or disable the default ghost joint filter.  
                In create mode with the "ghost" action set, also filter the selection to omit joint nodes if this flag is false.  
                Properties: create, query, edit
        locatorFilter (bool?): In create mode, enable or disable the default ghost locator filter.  
                In create mode with the "ghost" action set, also filter the selection to omit locator nodes if this flag is false.  
                Properties: create, query, edit
        mode (Queryable[str]?): Define the default mode for ghosting actions. Legal values are "preAndPost",  
                "pre", "post", "custom", and "keyframes".  
                Properties: create, query, edit
        nearOpacity (Queryable[float]?): In create mode, define the default value for the opacity value for ghosts nearest to the current time.  
                In edit mode, modify the opacity value of ghosts nearest to the current time for all ghosts.  
                In create mode with the "ghost" action, also set the opacity value of ghosts nearest to the current time for the selected objects.  
                Properties: create, query, edit
        postColor (Queryable[Tuple[float, float, float]]?): In create mode, define the default value for the color of ghosts after the current time.  
                In edit mode, modify the color of ghosts after the current time for all ghosts.  
                In create mode with the "ghost" action, also set the color of ghosts after the current time for the selected objects.  
                Properties: create, query, edit
        postFrames (Queryable[int]?): In create mode, define the default value for the number of ghosted frames after the current time.  
                In edit mode, modify the number of ghosted frames after the current time for all ghosts.  
                In create mode with the "ghost" action, also set the default number of ghosted frames after the current time for the selected objects.  
                Properties: create, query, edit
        preColor (Queryable[Tuple[float, float, float]]?): In create mode, define the default value for the color of ghosts before the current time.  
                In edit mode, modify the color of ghosts before the current time for all ghosts.  
                In create mode with the "ghost" action, also set the color of ghosts before the current time for the selected objects.  
                Properties: create, query, edit
        preFrames (Queryable[int]?): In create mode, define the default value for the number of ghosted frames before the current time.  
                In edit mode, modify the number of ghosted frames before the current time for all ghosts.  
                In create mode with the "ghost" action, also set the default number of ghosted frames before the current time for the selected objects.  
                Properties: create, query, edit
        preset (Queryable[str]?): Define the default mode for ghosting presets. Legal values are "1s", "2s", "4s", "5s", "10s", and "Custom".  
                Setting anything other than "Custom" fixes ghosts at 3 pre frames, 3 post frames, with a step value of the preset  
                (e.g. "2s" means show ghosts at every second frame or keyframe)  
                Properties: create, query, edit
        resetAll (bool?): Reset all ghosting options to their default values. Use with caution!  
                Properties: create, edit
        useDriver (bool?): In create mode, enable or disable the default ghost use driver value.  
                In edit mode, modify the use driver value of all existing ghosts.  
                In create mode with the "ghost" action, also set the use driver value for the selected objects.  
                Properties: create, query, edit

    Returns:
        bool: the previous global state of ghost visibility (after setting 'enable' flag)
        bool: the global state of ghost visibility (query 'enabled' flag)
        bool: the global state of the default ghost all-in-range value (query 'allInRange' flag)
        bool: the global state of the default ghost hierarchy (query 'hierarchy' flag)
        bool: the global state of the default ghost geometry filter (query 'geometryFilter' flag)
        bool: the global state of the default ghost joint filter (query 'jointFilter' flag)
        bool: the global state of the default ghost locator filter (query 'locatorFilter' flag)
        bool: the global state of the default post frame count (query 'postFrames' flag)
        bool: the global state of the default pre frame count (query 'preFrames' flag)
        bool: the global state of the default ghost frames step count (query 'ghostsStep' flag)
        List[str]: List of all objects for which ghosting was enabled ('action="ghost"' in create mode)
        List[str]: List of all objects for which ghosting was disabled ('action="unghost"' or 'action="unghostAll"' in create mode)
        List[str]: List of all objects for which ghosting is currently enabled (query 'ghostedObjects' flag)
        List[str]: List of affected objects (any flag in edit mode)
        List[float]: List of (frame1, frame2, ...) that is the union of ghosted frames on all selected objects (query 'frames' flag)
        float: Current opacity value for ghosts farthest from the current time (query 'farOpacity' flag)
        float: Current opacity value for ghosts closest to the current time (query 'nearOpacity' flag)
        float: The previous opacity value for ghosts farthest from the current time (set 'farOpacity' flag)
        float: The previous opacity value for ghosts closest to the current time (set 'nearOpacity' flag)
        str: Current ghosting mode (query 'mode' flag)
        str: The previous ghosting mode (set 'mode' flag)
        List[float]: Color as [red, green, blue] used for ghosts after the current time (query 'postColor' flag)
        List[float]: Previous color as [red, green, blue] used for ghosts after the current time (set 'postColor' flag)
        List[float]: Color as [red, green, blue] used for ghosts before the current time (query 'preColor' flag)
        List[float]: Previous color as [red, green, blue] used for ghosts before the current time (set 'preColor' flag)
        List[int]: Custom frame list for the 'frames' mode (query 'customFrames' flag)
        List[int]: Previous custom frame list (set 'customFrames' flag)

    Example:
    """

