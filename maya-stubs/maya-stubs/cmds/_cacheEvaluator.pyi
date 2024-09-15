from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def cacheEvaluator(*args: str, edit: bool = ..., query: bool = ..., cacheFillMode: Queryable[str] = ..., cacheFillOrder: Queryable[str] = ..., cacheInvalidate: NullableRange[float] = ..., cacheName: str = ..., cachedFrames: bool = ..., cachingPoints: bool = ..., creationParameters: bool = ..., delegateEvaluation: bool = ..., dynamicsAsyncRefresh: bool = ..., dynamicsSupportActive: bool = ..., dynamicsSupportEnabled: bool = ..., flushCache: str = ..., flushCacheRange: Tuple[NullableRange[float], bool] = ..., flushCacheSync: bool = ..., flushCacheWait: bool = ..., hybridCacheMode: Queryable[str] = ..., layeredEvaluationActive: bool = ..., layeredEvaluationCachingPoints: bool = ..., layeredEvaluationEnabled: bool = ..., listCacheNames: bool = ..., listCachedNodes: bool = ..., listValueNames: bool = ..., newAction: str = ..., newActionParam: str = ..., newFilter: str = ..., newFilterParam: str = ..., newRule: str = ..., newRuleParam: str = ..., pauseInvalidation: bool = ..., preventFrameSkip: bool = ..., resetRules: bool = ..., resourceUsage: bool = ..., resumeInvalidation: bool = ..., safeMode: bool = ..., safeModeMessages: bool = ..., safeModeTriggered: bool = ..., valueName: str = ..., waitForCache: float = ...) -> Union[str, bool, List[str], List[int]]:
    """This command controls caching configuration.  It allows interaction with the
    caching system.Caching configuration is done through a set of rules.  Most rules are composed
    of a "filter", which is the test to be perform in order to determine if the rule
    should be applied, and an "action", which is the effect that the rule application
    should have on nodes that satisfy the criteria.A caching mode is therefore a set of rules that determines which nodes are
    being cached.  This mode can be serialized to a JSON string using the
    "creationParameters" flag in query mode.A few cache configuration rules, filters and actions are provided in order to
    support the built-in default caching modes.Note that any combination of cache configuration rules other than the default modes
    is considered unsupported and to be used at one's own risk.  The default modes
    are "Evaluation cache", "VP2 software cache" and "VP2 hardware cache".  The sets
    of rules used to enable each mode are listed in the code examples.In order to get a cache configuration value for a given node or list of nodes,
    theflag can be used in query mode.  Without any additional
    parameters, this query is the same as if theflag was set to
    "active", i.e. it queries whether the given cache is active or not.If the queried node is not a caching point, there will be no caching
    configuration information associated with it and the query will return an
    empty string (which is basically the same as all cache modes being inactive).
    If the queried node is a caching point, the returned string will be the
    requested information from the given cache.  For example, querying the
    "active" value can return "0" or "1".Caching
    Args:
        cacheFillMode (Queryable[str]?): Specifies the cache fill mode. Valid values are: "syncOnly" to fill cache  
                during playback, "syncAsync" to cache during playback and in background,  
                 and "asyncOnly" to fill cache only in background. Query returns current mode.  
                Properties: create, query
        cacheFillOrder (Queryable[str]?): Specifies in which order the cache fills the timeline. Valid values are:  
                "forward" to fill cache in forward direction, "backward" to fill cache backwards,  
                "bidirectional" to fill cache in forward and backward directions simultaneously,  
                 and "forwardFromBegin" to fill cache in forward direction from animation start.  
                 Query returns current cache fill mode.  
                Properties: create, query
        cacheInvalidate (NullableRange[float]?): Specifies the frame range in which cache should be invalidated. The range  
                should be specified as a pair of positive integers.  
              
                    Usage examples:  
                  
                 -ci "10. 20"{Python equivalent: ('10','20')} means all frames  
                        in the range from 10 to 20, inclusive, in the current time unit.   
              
              
                    Omitting one end of a range means using either end of the animation range  
                     (or both), as in the following examples:  
                  
                 -ci "10. " means all frames from time 10 (in the current time unit)  
                        onwards to the maximum time in the animation range (on the timeline).   
                 -ci ":10" means all frames from the minimum time on the animation range  
                        (on the timeline) up to (and including) time 10 (in the current time unit).   
                 -ci ":" is a short form to specify all frames, from minimum to  
                        maximum time on the current animation range.  
                Properties: create
        cacheName (str?): Specifies the name of the cache from which to query a value.  
                			In query mode, this flag needs a value.  
                Properties: query
        cachedFrames (bool?): Get the list of frames with valid cache data.  
                The result is an integer array containing multiple triplets of (cache-status, begin-frame, end-frame)  
                For example,  
                The result is an array of 9 integers [(0b01, 1, 3), (0b10, 7, 10), (0b11, 13, 15)].  
                In MEL, the result is typed as "int[9]".  
                In Python, the result is typed as "Tuple[int,int,int][3]".  
                The result suggests frames 1. 3 (1,2,3), 7. 10 (7,8,9,19), and 13. 15 (13,14,15) are cached.  
                No other frames contain valid cache data.  
                The cache-status numbers are always 1 if "layeredEvaluationActive" is false.  
                The cache-status can be one of {1,2,3}, when "layeredEvaluationActive" is true.  
                It represents whether the frame is valid on animation cache or dynamics cache, the encoding is:  
              
                1 (0b01) : only animation cache is valid  
                2 (0b10) : only dynamics cache is valid  
                3 (0b11) : both animation and dynamics cache are valid  
              
                In the above example, it suggests:  
                frames 1. 3 are only valid in animation cache.  
                frames 7. 10 are only valid in dynamics cache.  
                frames 13. 15 are valid in both and considered as 'fully-cached'.  
                Properties: query
        cachingPoints (bool?): Get list of nodes marked as caching points, i.e. nodes with at least one  
                type of cache active.  
                Properties: query
        creationParameters (bool?): Get the current mode creation parameters.  The result is a JSON string which  
                represents an array with an element for each rule.  Each element is an  
                association between the parameter name and its value when creating the rule.  
                Properties: query
        delegateEvaluation (bool?): Returns whether the specified node(s) are delegating to evaluation.  
                Properties: query
        dynamicsAsyncRefresh (bool?): Enable / Disable Asynchronous Refresh in Dynamics Support mode.  
                Traditionally, edits related to the simulation system require the user to re-playback the scene to see the result.  
                When Asynchronous Refresh is active, Maya will process the simulation in the background and refresh the viewport once the result is ready.  
                Note, the automatic refresh will not happen if the frame contains temproary edits. For example, an object is moved without setting the keyframe.  
                Properties: create, query
        dynamicsSupportActive (bool?): Query if the Dynamics Support mode is active.  
                Dynamics Support mode is used to support Physics Simulation, such as Hair, or Fluid.  
                It will be activated if such nodes are detected in the scene, and "enableDynamicsSupport" is set to true.  
                When Dynamics Support mode is active, you will notice the following behavior:  
              
                Dynamics nodes will be frozen for uncached frame  
                A separate dynamics cache line will appear on the Time Slider  
                Dynamics cache starts after the animation cache was filled  
                Dynamics cache only fills in the background  
                Dynamics cache always fills forward from the beginning  
                Dynamics cache evaluation may refresh foreground dynamics nodes (see the flag "dynamicsAsyncRefresh")  
                Properties: query
        dynamicsSupportEnabled (bool?): Specifies if Dynamics nodes are allowed to participate in Cached Playback  
                When disabled, Dynamics nodes will trigger "Safe mode" and prevent caching.  
                When enabled, Dynamics nodes will participate in caching and trigger "Dynamics support mode".  
                For more information check flag "dynamicsSupportActive".  
                Properties: create, query
        flushCache (str?): Specifies to flush the current cache. Valid values are: "keep" to store the existing  
                cache as backup, and "destroy" to delete the current cache.  
                Properties: create
        flushCacheRange (Tuple[NullableRange[float], bool]?): Specifies the frame range in which cache should be flushed. By default it will  
                destroy the cache - if the 'flushCache' is also set then it will define what  
                to do with the cache range being flushed.  
                The range should be specified as a pair of positive integers and a boolean.  
              
                    Usage examples:  
                  
                 -flushCacheRange "10. 20" on {Python equivalent: ('10','20',True)}  
                                means all frames in the range from 10 to 20, inclusive, in the current time unit.   
                 -flushCacheRange "12. 18" off {Python equivalent: ('12','18',False)}  
                                means all frames before 12 and after 18, not inclusive, in the current time unit.   
              
              
                    Omitting one end of a range means using either end of the animation range  
                     (or both), as in the following examples:  
                  
                 -flushCacheRange "10. " on means all frames from time 10 (in the current time unit)  
                        onwards to the maximum time in the animation range (on the timeline).   
                 -flushCacheRange ":10" on means all frames from the minimum time on the animation range  
                        (on the timeline) up to (and including) time 10 (in the current time unit).   
                 -flushCacheRange ":" on is a short form to specify all frames, from minimum to  
                        maximum time on the current animation range.  
                Properties: create
        flushCacheSync (bool?): Specifies how to flush the cache: synchronously or asynchronously. True for synchronous, False for asynchronous.  
                Properties: create, query
        flushCacheWait (bool?): Wait for the cache destruction to be completed.  
                Properties: create
        hybridCacheMode (Queryable[str]?): Specifies the hybrid cache mode. Valid values are: "disabled", not to use  
                hybrid cache; "smp", to evaluate on the GPU meshes with GPU-supported deformation  
                stacks if they use Smooth Mesh Preview (instead of caching them);  
                "all", to evaluate on the GPU all meshes with PU-supported deformation stacks  
                (instead of caching them). Query returns current mode.  
                Properties: create, query
        layeredEvaluationActive (bool?): Query if the Layered Evaluation mode is active.  
                When Layered Evaluation is active, the background cache fill process will be split into multiple passes for different contents (evaluation nodes).  
                These contents are referred as different 'evaluation layers', representing different level of details (LoD) in animation evaluation.  
                For example:  
              
                The first layer contains regular animations like a character motion.   
                The second layer contains dynamics simulations like a character's hair and cloth.   
              
                Maya will create separated cache and cache fill pass for each of the layers.  
                Additional cache bars will be added to the Time Slider UI to represent these layers.  
                The background cache fill pass for each of the layer will start in order.  
                In the above example, two passes of background cache fill will be observed.  
                In the first pass of background-cache-fill or playback-fill, only Character motions will be evaluated and filled, Hair and Clothes are frozen in-place.  
                After the cache for first layer have been filled for all the frames,  
                the second pass of cache fill will start to simulate Hairs and Clothes physics and fill the cache for the 2nd layer.  
                Once the cache for the 2nd layer is filled for a frame, users can scrub the timeline to view the fully updated effects.  
                Note, when layered evaluation is active, any foreground playback or manipulation will only evaluate the first evaluation layer,  
                and all the FX contents will be frozen in the viewport until the background simulation is complete.  
                For example, when rotating a characterâ€™s head, its hair will not follow in real time.  
                If the flag "dynamicsAsyncRefresh" is enabled, the FX contents will be updated automatically after simulation cached up. Please refer to the flag for more detail.  
                Properties: query
        layeredEvaluationCachingPoints (bool?): Get the list of nodes marked as caching points because of layered evaluation.  
                Properties: query
        layeredEvaluationEnabled (bool?): Enable / Disable Layered Evaluation in Dynamics Support mode.  
                Refering to flags "dynamicsSupportActive" and "layeredEvaluationActive" for details about layered evaluation enabled behavior.  
                This flag is provided to support plugin developers for testing purpose.  
                Disabling this option in production is not recommended.  
                When disabled, dynamics nodes will share the same cache with regular animation.  
                Allows dynamics nodes to be evaluated and stored to cache in the foreground.  
                Background "cacheFillOrder" option will be locked to "forwardFromBegin".  
                When used with cacheFillMode="syncOnly", it can also be used to support legacy dynamics nodes that cannot evaluate in the background.  
                Properties: create, query
        listCacheNames (bool?): Return the list of existing cache names.  
                Properties: query
        listCachedNodes (bool?): Returns the list of cached nodes.  
                Properties: query
        listValueNames (bool?): Return the list of value names that can be queried for the given cache.  
                Properties: query
        newAction (str?): Specifies the name of the new action to create in the new filter/action rule.  
                Properties: create
        newActionParam (str?): Specifies the parameter string to pass to the new action to create in the new filter/action rule.  
                Properties: create
        newFilter (str?): Specifies the name of the new filter to create in the new filter/action rule.  
                Properties: create
        newFilterParam (str?): Specifies the parameter string to pass to the new filter to create in the new filter/action rule.  
                Properties: create
        newRule (str?): Specifies the name of the new rule to create.  
                Properties: create
        newRuleParam (str?): Specifies the parameter string to pass to the new rule to create.  
                Properties: create
        pauseInvalidation (bool?): Pause all incoming invalidation of the cache. Work in symmetry with resumeInvalidation flag.  
                PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation.  
                If queried it will return how much time caching is paused, 0 means it is resumed.  
                Properties: create, query
        preventFrameSkip (bool?): Specifies if frame skipping is enabled. Following behavior is seen when frame  
                skipping is enabled, and playback is set to play in real-time.  
              
                If cache can't be filled at real-time frame rate, frames will NOT be skipped.  
                Once all frames have been looped over(and therefore all frames are cached), and if  
                    playing back from cache still can't be done at real-time frame rate; frames WILL be skipped.  
                If memory limit is reached before all frames are cached, frames WILL be skipped.  
                If cache is invalidated will playing(like flushing it), frames will NOT  
                    be skipped(until the cache is full again).  
                Properties: create, query
        resetRules (bool?): Reset the cache configuration rules to an empty set of rules.  
                Properties: create
        resourceUsage (bool?): Returns the current state of the resource usage as a string. 'unlimited' = the resource limits  
                are being ignored, 'out' = the memory limit has been reached, 'low' = the memory usage is at  
                90% of the specified limit, 'okay' = memory usage is under 90% of the specified limit.  
                Properties: query
        resumeInvalidation (bool?): Resume all incoming invalidation of the cache. Work in symmetry with pauseInvalidation flag.  
                PauseInvalidation can be called several time, useful in nesting situation. The same number of resume need to be called to resume the invalidation.  
                If queried it will return true if cache is resumed, false otherwise.  
                Properties: create, query
        safeMode (bool?): Turns safe mode on or off. In query mode, it returns the status of the safe mode for cache evaluator.  
                Properties: create, query
        safeModeMessages (bool?): Prints the safe mode messages to the console.  
                Properties: query
        safeModeTriggered (bool?): Returns if the safe mode was triggered for cache evaluator.  
                Properties: query
        valueName (str?): Specifies the name of the parameter for which to query the value.  
                			In query mode, this flag needs a value.  
                Properties: query
        waitForCache (float?): Specifies to wait for cache to fill in background, with [Time to wait in seconds] timeout.  
                Properties: create

    Returns:
        str: The state of whether the memory limit has been reached or not ('out', 'okay', 'low', or 'unlimited' with the 'resourceUsage' flag)
        bool: The state of whether the safe mode is enabled (with the 'safeMode' flag)
        bool: The state of whether the safe mode was triggered (with the 'safeModeTriggered' flag)
        bool: The state of whether prevent frame skipping is enabled (with the 'preventFrameSkip' flag)
        bool: The state of whether cache in background was calculated (with the 'waitForCache' flag)
        List[str]: The available cache names (with the 'listCacheNames' flag)
        str: The list of nodes currently cached by the cache evaluator (with the 'listCachedNodes' flag).
        List[str]: The available value names (with the 'listValueNames' flag)
        List[str]: The parameter value for the requested node(s) (with the 'cacheName' flag)
        List[str]: The state of whether delegate evaluation is enabled for the requested node(s) (with the 'delegateEvaluation' flag)
        str: The creation parameters for the current mode as a JSON array (with the 'creationParameters' flag)
        List[str]: The list of nodes marked as caching point (with the 'cachingPoints' flag)
        List[str]: The list of nodes forced as caching points because of layered evaluation (with the 'layeredEvaluationCachingPoints' flag)
        List[int]: The list of frames being cached (with the 'cachedFrames' flag)
        str: The current cache fill mode (with the 'cacheFillMode' flag)
        str: The current cache fill order (with the 'cacheFillOrder' flag)
        str: The list of all the safe mode messages (with the 'safeModeMessages' flag)
        str: The current hybrid cache mode (with the 'hybridCacheMode' flag)

    Example:
    """

