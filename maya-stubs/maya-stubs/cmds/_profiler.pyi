from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def profiler(*, query: bool = ..., addCategory: str = ..., allCategories: bool = ..., bufferSize: Queryable[int] = ..., categoryIndex: int = ..., categoryIndexToName: int = ..., categoryInfo: Queryable[str] = ..., categoryName: str = ..., categoryNameToIndex: str = ..., categoryRecording: bool = ..., clearAllMelInstrumentation: bool = ..., colorIndex: int = ..., eventCPUId: bool = ..., eventCategory: bool = ..., eventColor: bool = ..., eventCount: bool = ..., eventDescription: bool = ..., eventDuration: bool = ..., eventIndex: int = ..., eventName: bool = ..., eventStartTime: bool = ..., eventThreadId: bool = ..., instrumentMel: bool = ..., load: Queryable[str] = ..., output: Queryable[str] = ..., procedureDescription: str = ..., procedureName: str = ..., removeCategory: str = ..., reset: bool = ..., sampling: bool = ..., signalEvent: bool = ..., signalMelEvent: bool = ...) -> Union[bool, int, str]:
    """The profiler is used to record timing information from key events within Maya,
    as an aid in tuning the performance of scenes, scripts and plug-ins.
    User written plug-ins and Python scripts can also generate profiling information
    for their own code through the MProfilingScope (C++), MProfilingContextManager
    (Python) and MProfiler classes in the API.This command provides the ability to control the collection of profiling data and
    to query information about the recorded events. The recorded information can also
    be viewed graphically in the Profiler window.The buffer size cannot be changed while sampling is active, it will return an error
    The reset flag cannot be called while sampling is active, it will return an error.
    Any changes to the buffer size will only be applied on start of the next recording.
    You can't save and load in the same command, save has priority, load would be ignored.timing, performance, profiling, optimize
    Args:
        addCategory (str?): Add a new category for the profiler.  
                Returns the index of the new category.  
                Properties: create
        allCategories (bool?): Query the names of all categories.  
                If the categoryInfo flag is set then alternate the name of the category  
                with the description of the category.  
                Properties: query
        bufferSize (Queryable[int]?): Toggled : change the buffer size to fit the specified number of events (requires that sampling is off)  
                Query : return the current buffer size  
                The new buffer size will only take effect when next sampling starts.  
                When the buffer is full, the recording stops.  
                Properties: create, query
        categoryIndex (int?): Used in conjunction with other flags, to indicate the index of the category.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        categoryIndexToName (int?): Returns the name of the category with a given index.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        categoryInfo (Queryable[str]?): When used with the addCategory flag set the description of the added profiler category.  
                In query mode return the description of the category referenced by either  
                the categoryIndex or categoryName flags.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        categoryName (str?): Used in conjunction with other flags, to indicate the name of the category.  
                			In query mode, this flag needs a value.  
                Properties: query
        categoryNameToIndex (str?): Returns the index of the category with a given name.  
                			In query mode, this flag needs a value.  
                Properties: create, query
        categoryRecording (bool?): Toggled : Enable/disable the recording of the category.  
                Query : return if the recording of the category is On.  
                Requires the -categoryIndex or -categoryName flag to specify the category to be queried.  
                Properties: create, query
        clearAllMelInstrumentation (bool?): Clear all MEL command or procedure instrumentation.  
                Properties: create
        colorIndex (int?): Used with "-instrumentMel true" to specify the color index to show the  
                profiling result.  
                Properties: create
        eventCPUId (bool?): Query the CPU ID of the event at the given index.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventCategory (bool?): Query the category index the event at the given index belongs to.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventColor (bool?): Query the color of the event at the given index.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventCount (bool?): Query the number of events in the buffer  
                Properties: query
        eventDescription (bool?): Query the description of the event at the given index.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventDuration (bool?): Query the duration of the event at the given index, the time unit is microsecond.  
                Note that a signal event has a 0 duration.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventIndex (int?): Used usually in conjunction with other flags, to indicate the index of the event.  
                			In query mode, this flag needs a value.  
                Properties: query
        eventName (bool?): Query the name of the event at the given index.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventStartTime (bool?): Query the time of the event at the given index, the time unit is microsecond.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        eventThreadId (bool?): Query the thread ID of the event at the given index.  
                Requires the -eventIndex flag to specify the event to be queried.  
                Properties: query
        instrumentMel (bool?): Enable/Diable the instrumentation of a MEL command or procedure.  
                When the instrumentation is enabled, the execution of MEL command  
                or procedure can be profiled and shown in the Profiler window.  
                To enable the instrumentation requires the -procedureName, -colorIndex  
                and -categoryIndex flags.  
                To disable the instrumentation requires the -procedureName flag.  
                Properties: create
        load (Queryable[str]?): Read the recorded events from the specified file  
                Properties: create, query
        output (Queryable[str]?): Output the recorded events to the specified file  
                Properties: create, query
        procedureDescription (str?): Used with "-instrumentMel true" to provide a description of the MEL  
                command or procedure being instrumented.  
                This description can be viewed in the Profiler Tool window.  
                Properties: create
        procedureName (str?): Used with -instrumentMel to specify the name of the procedure to be  
                enabled/disabled the instrumentation.  
                Properties: create
        removeCategory (str?): Remove an existing category for the profiler.  
                Returns the index of the removed category.  
                Properties: create
        reset (bool?): reset the profiler's data (requires that sampling is off)  
                Properties: create, query
        sampling (bool?): Toggled : Enable/disable the recording of events  
                Query : return if the recording of events is On.  
                Properties: create, query
        signalEvent (bool?): Query if the event at the given index is a signal event.  
                Requires the -eventIndex flag to specify the event to be queried.  
                A Signal Event only remembers the start moment and has no knowledge about  
                duration. It can be used in cases when the user does not care about the  
                duration but only cares if this event does happen.  
                Properties: query
        signalMelEvent (bool?): Used with "-instrumentMel true", inform profiler that this instrumented  
                MEL command or procedure will be taken as a signal event during profiling.  
                A Signal Event only remembers the start moment and has no knowledge about  
                duration. It can be used in cases when the user does not care about the  
                duration but only cares if this event does happen.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

