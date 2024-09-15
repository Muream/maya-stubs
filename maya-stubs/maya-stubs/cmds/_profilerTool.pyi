from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def profilerTool(*args: Any, edit: bool = ..., query: bool = ..., categoryView: bool = ..., collapseSelectedEvents: bool = ..., collapseSelectedEventsRepetition: bool = ..., cpuView: bool = ..., destroy: bool = ..., eventTypes: bool = ..., exists: bool = ..., expandSelectedEvents: bool = ..., expandSelectedEventsRepetition: bool = ..., findNext: bool = ..., findPrevious: bool = ..., frameAll: bool = ..., frameSelected: bool = ..., isolateSegment: int = ..., make: bool = ..., matchWholeWord: bool = ..., searchEvent: str = ..., segmentCount: bool = ..., showAllEvent: bool = ..., showCriticalPath: bool = ..., showHotspot: bool = ..., showSelectedEvents: bool = ..., showSelectedEventsRepetition: bool = ..., threadView: bool = ..., unisolateSegment: bool = ...) -> bool:
    """This script is intended to be used by the profilerPanel to interact with the profiler tool's view (draw region).
    It can be used to control some behaviors about the profiler Tool.profiler, tool, profilerTool, timing, performance, profiling
    Args:
        categoryView (bool?): Change view mode to category view  
                Properties: edit
        collapseSelectedEvents (bool?): Hide all sub-events of selected events so that only top-level events show  
                Properties: edit
        collapseSelectedEventsRepetition (bool?): Hide all sub-events repetition of selected events based on their comment  
                Properties: edit
        cpuView (bool?): Change view mode to cpu view  
                Properties: edit
        destroy (bool?): Destroy the profiler tool  
                Internal flag. Should not be used by user.  
                Properties: create
        eventTypes (bool?): Return JSON data containing the list of event types on currently existing events.  
                If the value of the flag is true then show only event types for selected events,  
                otherwise show them for all events.  The JSON return string will contain the event  
                type information in the following format:  
              
                {  
                    "eventSummary" : [  
                        { "type"        : EVENT_TYPE_NAME,  
                        , "description" : EVENT_TYPE_DESCRIPTION,  
                        , "color"       : [ RED_AS_FLOAT, GREEN_AS_FLOAT, BLUE_AS_FLOAT ]  
                        , "category"    : CATEGORY_NAME  
                        , "count"       : EVENT_TYPE_COUNT  
                        }  
                    ]  
                }  
              
                "type" and "description" may be omitted, indicating that the results  
                correspond to anonymous events.  
                Properties: query
        exists (bool?): Query if the profiler tool view exists.  
                Profiler tool can only exist after "profilerTool -make" is called.  
                Properties: query
        expandSelectedEvents (bool?): Show all sub-events of selected events  
                Properties: edit
        expandSelectedEventsRepetition (bool?): Show all sub-events repetition of selected events based on their comment  
                Properties: edit
        findNext (bool?): This flag is used along with flag -searchEvent.  
                Properties: query
        findPrevious (bool?): This flag is used along with flag -searchEvent.  
                Properties: query
        frameAll (bool?): Frame on all events in the profilerToolView  
                Properties: edit
        frameSelected (bool?): Frame on all selected events in the profilerToolView  
                Properties: edit
        isolateSegment (int?): Isolate a specified segment.  
                A segment is a set of events that happened in one animation frame.  
                You can use flag -segmentCount to query the number of segments in the event buffer.  
                The segment index starts from 0.  
                If the specified segment does not exist, an error will be thrown.  
                Properties: edit
        make (bool?): Make the profiler tool and parent it to the most recent layout created  
                Internal flag. Should not be used by user.  
                Properties: create
        matchWholeWord (bool?): Tells profiler tool if it should match whole word when searching event(s).  
                The default value is false.  
                Properties: edit
        searchEvent (str?): Search event(s).  
                You can set -matchWholeWord before you use -searchEvent.  
                If -matchWholeWord has been set to true, the profiler tool will search event(s) whose name exactly matches with the string.  
                If -matchWholeWord has been set to false, the profiler tool will search event(s) whose name contains the string.  
                If -findNext is also used along with this flag, the profiler tool will find the first event next to the current selected event.  
                If -findPrevious is also used along with this flag, the profiler tool will find the first event previous to the current selected event.  
                If currently don't have a selected event or there are multiple selected events, the search will start at  
                the first event in profiler buffer.  
                If -findNext and -findPrevious are not used along with this flag, the profiler tool will find all events.  
                			In query mode, this flag needs a value.  
                Properties: query
        segmentCount (bool?): Returns the number of segments in the event buffer.  
                Properties: query
        showAllEvent (bool?): Show all events (if events were hidden by filtering) (true) or  
                Hide all events (false)  
                Properties: edit
        showCriticalPath (bool?): Show critical path of selected frame  
                Properties: edit
        showHotspot (bool?): Show hotspot of selected frame  
                Properties: edit
        showSelectedEvents (bool?): Show only the selected events (true) or  
                hide all selected events (false)  
                Properties: edit
        showSelectedEventsRepetition (bool?): Show only the selected events repetition based on their comment (true) or  
                Hide all selected events repetition based on their comment (false)  
                Properties: edit
        threadView (bool?): Change view mode to thread view  
                Properties: edit
        unisolateSegment (bool?): Unisolate current isolated segment.  
                If no segment is currently isolated, nothing will happen.  
                Properties: edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

