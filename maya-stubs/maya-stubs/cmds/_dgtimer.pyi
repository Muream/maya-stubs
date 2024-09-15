from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dgtimer(*, query: bool = ..., combineType: bool = ..., hide: Queryable[Multiuse[str]] = ..., hierarchy: bool = ..., maxDisplay: Queryable[int] = ..., name: Queryable[str] = ..., noHeader: bool = ..., outputFile: str = ..., overhead: bool = ..., rangeLower: float = ..., rangeUpper: float = ..., reset: bool = ..., returnCode: Queryable[str] = ..., returnType: Queryable[str] = ..., show: Queryable[Multiuse[str]] = ..., sortMetric: Queryable[str] = ..., sortType: Queryable[str] = ..., threshold: Queryable[float] = ..., timerOff: bool = ..., timerOn: bool = ..., trace: bool = ..., type: Queryable[str] = ..., uniqueName: bool = ..., updateHeatMap: int = ...) -> Union[float, bool, Multiuse[str], int, str]:
    """This command measures dependency graph node performance by managing
    timers on a per-node basis. Logically, each DG node has a timer
    associated with it which records the amount of real time spent
    in various operations on its plugs. The time measurement includes the cost
    of copying data to the node on behalf of the operation, MEL commands
    executed by an expression contained in an expression invoked by the
    node, and includes
    any wait time such as when a fileTexture node loads an image file from
    disk. Most DG operations are reported including compute, draw, and dirty
    propagation.The various operations we measure are called "metrics" and the types of
    timers are called "timer types". The various metrics are always measured
    when timing is on, but are only queried when specified via the -show and
    -hide flags. The metrics currently supported are listed in detail under
    the -show flag below. For each metric we support a standard set of timer
    types. There are three of these:
    "self" for self time (the time specific to the node and not its children),
    "inclusive" (time including children of the node), and
    "count" (number of operations of the given metric on the node).The timing mechanism which is used byis built into the DG
    itself, thus ALL depend nodes can be timed and there is no need for
    programmers writing plug-ins using the OpenMaya API to add any special
    code in order for their nodes to be timed -- its all
    handled transparently.Thecommand allows node timers to be turned on, off, reset
    to zero, and have their current value displayed, and these operations
    can be performed globally on all nodes or on a specific set of nodes
    defined by name, type or parentage. Note that all timer measurements are
    computed in "real time" (the same time measurement you get from a
    wristwatch) as opposed to "CPU time" (which only measures time when the
    processor is executing your code). All times are displayed in seconds.Use the -query flag to display the current timer values on a node,use -on to turn on timing,use -off to turn off timing,and -reset to reset timers to zero.To display the values measured during timing, there are two approaches.
    The first method is to use the -query flag can be used to report the information which
    has been measured. The second method is to use the query methods available on
    the OpenMaya class MFnDependencyNode (see the OpenMaya documentation for details).What follows is a description of what is generated via -query. The output
    is broken out into several sections and these are described as follows:Section 1 of the dgtimer output contains global information. This section
    can be disabled via the -hoHeader flag.
    These values are reset whenever a global timer reset
    occurs (i.e.is specified). The global values which are
    reported are:Section 2 of the dgtimer -query output contains per-node information. There is a header which
    describes the meaning of each column, followed by the actual per-node data, and this is
    ultimately followed by a footer which summarises the totals per column. Note that the data
    contained in the footer is the global total for each metric and will include any nodes that
    have been deleted since the last reset, so the value in the footer MAY exceed what you get when you total the
    individual values in the column. To prevent the header
    and footer from appearing, use the -noHeader flag to just display the per-node data.The columns which are displayed are as follows:Section 3 of the dgtimer -query output describes time spent in callbacks. Note that
    section 3 only appears when the CALLBACK metric is shown (see the -show flag).The first part is SECTION 3.1 lists the time per callback with each entry comprising:At the bottom of SECTION 3.1 is the per-column total. The values printed match the summation at
    the bottom of the listing in section 2. Note that the values from SECTION 3.1
    include any nodes that have been deleted since the last reset. The thresholding parameters
    (-threshold, -rangeLower, -rangeUpper and -maxDisplay) are honoured when generating the listing.
    The sorting of the
    rows and display of the Percent and Cumulative columns obeys the -sortType flag. As the listing
    can be long, zero entries are not displayed.The second part is SECTION 3.2 which lists the data per callbackId. As noted earlier, the
    callbackId is an identifying
    number which is unique to each client that is registered to a callback and can
    be deduced by the user, such as through the OpenMaya API. The entries in SECTION 3.2 appear
    as follows:The third part is SECTION 3.3 which lists data per-callback per-node. The
    nodes are sorted based on the -sortType flag, and for each node, the
    callbacks are listed, also sorted based on the -sortType flag. As this
    listing can be long, zero entries are not displayed. An important note for SECTION 3.3 is
    that only nodes which still exist are displayed. If a node has been deleted, no infromation
    is listed.dependency, graph, optimize, performance
    Args:
        combineType (bool?): Causes all nodes of the same type (e.g. animCurveTA) to be combined in the  
                output display.  
                Properties: query
        hide (Queryable[Multiuse[str]]?): This flag is the converse of -show. As with -show, it is a query-only  
                flag which can be specified multiple times. If you do specify -hide, we display  
                all columns except those listed by the -hide flags.  
                Properties: create, query, multiuse
        hierarchy (bool?): Used to specify that a hierarchy of the dependency graph be affected,  
                thus "-reset -hierarchy -name ball" will reset the timers on the node  
                named "ball" and all of its descendents in the dependency graph.  
                Properties: create, query
        maxDisplay (Queryable[int]?): Truncates the display so that only the most expenive "n" entries are  
                printed in the output display.  
                Properties: query
        name (Queryable[str]?): Used in conjunction with -reset or -query to specify the name of the node  
                to reset or print timer values for. When querying a single timer, only a  
                single line of output is generated (i.e. the global timers and header  
                information is omitted). Note that one can force output to the script editor  
                window via the "-outputFile MEL" option to make it easy to grab the values  
                in a MEL script. Note: the -name and -type flag cannot be used together.  
                Properties: create, query
        noHeader (bool?): Used in conjunction with -query to prevent any header or footer information  
                from being printed. All that will be output is the per-node timing data.  
                This option makes it easier to parse the output such as when you output the  
                query to a file on disk using the -outputFile option.  
                Properties: create, query
        outputFile (str?): Specifies where the output of timing or tracing is displayed. The flag takes a string  
                argument which accepts three possible values:  
              
              
                The name of a file on disk.  
                Or the keyword "stdout", which causes output to be displayed on the terminal window (Linux and Macintosh), and the status window on Windows.  
                Or the keyword "MEL", which causes output to be displayed in the Maya Script Editor (only supported with -query).  
              
                The "stdout" setting is the default behaviour.  
              
                This flag can be used with the -query flag as well as the -trace flag.  
              
                When used with the -trace flag, any tracing output will be displayed on the destination  
                specified by the -outputFile (or stdout if -outputFile is omitted). Tracing operations  
                will continue to output to the destination until you specify the -trace and -outputFile  
                flags again.  
              
                When used with the -query flag, timing output will be displayed to the destination  
                specified by the -outputFile (or "stdout" if -outputFile is omitted).  
              
                Here are some examples of how to use the -query, -trace and -outputFile flags:  
              
                Example: output the timing information to a single file on disk:  
              
              
                dgtimer -on;                                       // Turn on timing  
                create some animated scene content;  
                play -wait;                                        // Play the scene through  
                dgtimer -query -outputFile "/tmp/timing.txt"       // Output node timing information to a file on disk  
              
              
                Example: output the tracing information to a single file on disk:  
              
              
                dgtimer -on;                                       // Turn on timing  
                create some animated scene content;  
                dgtimer -trace on -outputFile "/tmp/trace.txt"     // Turn on tracing and output the results to file  
                play -wait;                                        // Play the scene through; trace info goes to /tmp/trace.txt  
                dgtimer -query;                                    // But the timing info goes to the terminal window  
                play -wait;                                        // Play the scene again, trace info still goes to /tmp/trace.txt  
              
              
                Example: two runs, outputting the trace information and timing information to separate files:  
              
              
                dgtimer -on;                                       // Turn on timing  
                create some animated scene content;  
                dgtimer -trace on -outputFile "/tmp/trace1.txt"    // Turn on tracing and output the results to file  
                play -wait;                                        // Play the scene through  
                dgtimer -query -outputFile "/tmp/query1.txt"       // Output node timing information to another file  
                dgtimer -reset;  
                dgtimer -trace on -outputFile "/tmp/trace2.txt"    // Output tracing results to different file  
                play -wait;                                        // Play the scene through  
                dgtimer -query -outputFile "/tmp/query2.txt"       // Output node timing information to another file  
              
              
                Tips and tricks:  
              
              
                Outputting the timing results to the script editor makes it easy to  
                use the results in MEL e.g. string $timing[] = `dgtimer -query -outputFile MEL`.  
                It is important to note that the -outputFile you specify with -trace is  
                totally independent from the one you specify with -query.  
                If the file you specify already exists, Maya will empty the file first  
                before outputting data to it (and if the file is not writable, an error is  
                generated instead).  
              
                In query mode, this flag needs a value.  
                Properties: query
        overhead (bool?): Turns on and off the measurement of timing overhead. Under ordinary circumstances the  
                amount of timing overhead is minimal compared with the events being measured, but in  
                complex scenes, one might find the overhead to be measurable. By default this option  
                is turned off. To enable it, specify "dgtimer -overhead true" prior to starting timing.  
                When querying timing, the overhead is reported in SECTION 1.2 of the dgtimer output and  
                is not factored out of each individual operation.  
                Properties: create, query
        rangeLower (float?): This flag can be specified to limit the range of nodes which are displayed  
                in a query, or the limits of the heat map with -updateHeatMap. The value  
                is the lower percentage cutoff for the nodes which are processed. There is also  
                a -rangeLower flag which sets the lower range limit. The default value is 0,  
                meaning that all nodes with timing value below the upper range limit are considered.  
                Properties: create
        rangeUpper (float?): This flag can be specified to limit the range of nodes which are displayed  
                in a query, or the limits of the heat map with -updateHeatMap. The value  
                is the upper percentage cutoff for the nodes which are processed. There is also  
                a -rangeLower flag which sets the lower range limit. The default value is 100,  
                meaning that all nodes with timing value above the lower range limit are considered.  
                Properties: create
        reset (bool?): Resets the node timers to zero. By default, the timers on all nodes as  
                well as the global timers are reset, but if specified with the -name or  
                -type flags, only the timers on specified nodes are reset.  
                Properties: create
        returnCode (Queryable[str]?): This flag has been replaced by the more general -returnType flag.  
                The -returnCode flag was unfortunately specific to the compute metric only.  
                It exists only for backwards compatability purposes.  
                It will be removed altogether in a future release.  
              
                Here are some handy equivalences:  
              
                To get the total number of nodes:  
                OLD WAY: dgtimer -rc nodecount -q;  
                // Result:325//  
              
                NEW WAY: dgtimer -returnType total -sortType none -q;  
                // Result:325//  
              
                OLD WAY: dgtimer -rc count -q;  
                // Result:1270//  
              
                To get the sum of the compute count column:  
                NEW WAY: dgtimer -returnType total -sortMetric compute -sortType count -q;  
                // Result:1270//  
              
                OLD WAY: dgtimer -rc selftime -q;  
                // Result:0.112898//  
              
                To get the sum of the compute self column:  
                NEW WAY: dgtimer -returnType total -sortMetric compute -sortType self -q;  
                // Result:0.112898//  
                Properties: create, query
        returnType (Queryable[str]?): This flag specifies what the double value returned by the dgtimer command represents.  
                By default, the value returned is the global total as displayed in SECTION 1 for the  
                column we are sorting on in the per-node output (the sort column can be specified  
                via the -sortMetric and -sortType flags). However, instead of the  
                total being returned, the user can instead request the individual entries for  
                the column. This flag is useful mainly for querying without forcing any output.  
                The flag accepts the values "total", to just display the column total, or  
                "all" to display all entries individually.  
              
                For example, if you want to get the total of draw self time without any other  
                output simply specify the following:  
              
                dgtimer -returnType total -sortMetric draw -sortType self -threshold 100. noHeader -query;  
                // Result: 7718.01 //  
              
                To instead get each individual entry, change the above query to:  
              
                dgtimer -returnType all -sortMetric draw -sortType self -threshold 100. noHeader -query;  
                // Result: 6576.01 21.91 11.17 1108.92 //  
              
                To get the inclusive dirty time for a specific node, use -name as well as -returnType all:  
              
                dgtimer -name "virginia" -returnType all -sortMetric dirty -sortType inclusive -threshold 100. noHeader -query;  
              
                Note: to get the total number of nodes, use "-sortType none -returnType total".  To get  
                the on/off status for each node, use "-sortType none -returnType all".  
                Properties: query
        show (Queryable[Multiuse[str]]?): Used in conjunction with -query to specify which columns are to be displayed  
                in the per-node section of the output. -show takes an argument, which can  
                be  
                "all" (to display all columns),  
                "callback" (to display the time spent during any callback processing on the node not due to evaluation),  
                "compute" (to display the time spent in the node's compute methods),  
                "dirty" (to display time spent propagating dirtiness on behalf of the node),  
                "draw" (to display time spent drawing the node),  
                "compcb" (to display time spent during callback processing on node due to compute),  
                and  
                "compncb" (to display time spent during callback processing on node NOT due to compute).  
                The -show flag can be used multiple  
                times, but cannot be specified with -hide. By default, if neither -show,  
                -hide, or -sort are given, the effective display mode is:  
                "dgtimer -show compute -query".  
                Properties: create, query, multiuse
        sortMetric (Queryable[str]?): Used in conjunction with -query to specify which metric is to be sorted on  
                when the per-node section of the output is generated, for example "draw" time.  
                Note that the -sortType flag can also be specified to define which timer is  
                sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will  
                sort the output by the number of times each node was drawn. Both -sortMetric and  
                -sortType are optional and you can specify one without the other. The -sortMetric  
                flag can only be specified at most once. The flag takes the following arguments:  
                "callback" (to sort on time spent during any callback processing on the node),  
                "compute" (to sort on the time spent in the node's compute methods),  
                "dirty" (to sort on the time spent propagating dirtiness on behalf of the node),  
                "draw" (to sort on time spent drawing the node),  
                "fetch" (to sort on time spent copying data from the datablock),  
                The default, if -sortMetric is omitted, is to sort on the first displayed column.  
                Note that the sortMetric is  
                independent of which columns are displayed via -show and -hide. Sort on a hidden  
                column is allowed.  
                The column selected by -sortMetric and -sortType specifies which total is returned  
                by the dgtimer command on the MEL command line.  
                This flag is also used with -updateHeatMap to specify which metric to build the heat map for.  
                Properties: create, query
        sortType (Queryable[str]?): Used in conjunction with -query to specify which timer is to be sorted on  
                when the per-node section of the output is generated, for example "self" time.  
                Note that the -sortMetric flag can also be specified to define which metric is  
                sorted on: for example "dgtimer -sortMetric draw -sortType count -query" will  
                sort the output by the number of times each node was drawn. Both -sortMetric and  
                -sortType are optional and you can specify one without the other. The -sortType  
                flag can be specified at most once. The flag takes the following arguments:  
                "self" (to sort on self time, which is the time specific to the node and not its children),  
                "inclusive" (to sort on the time including children of the node),  
                "count" (to sort on the number of times the node was invoked).  
                and  
                "none" (to sort on self time, but do not display the Percent and Cumulative columns  
                in the per-node display, as well as cause the total number of nodes in Maya to be  
                returned on the command line).  
                The default, if -sortType is omitted, is to sort on self time.  
                The column selected by -sortMetric and -sortType specifies which total is returned  
                by the dgtimer command on the MEL command line. The global total as displayed in  
                SECTION 1 of the listing is returned. The special case of "-sortType none"  
                causes the number of nodes in Maya to instead be returned.  
                This flag is also used with -updateHeatMap to specify which metric to build the heat map for.  
                Properties: create, query
        threshold (Queryable[float]?): Truncates the display once the value falls below the threshold value. The  
                threshold applies to whatever timer is being used for sorting. For example, if  
                our sort key is self compute time (i.e. -sortMetric is "compute" and -sortType  
                is "self") and the threshold parameter is 20.0, then only nodes with a compute  
                self-time of 20.0 or higher will be displayed. (Note that -threshold uses  
                absolute time. There are the similar -rangeUpper and -rangeLower parameters  
                which specify a range using percentage).  
                Properties: query
        timerOff (bool?): Turns off node timing. By default, the timers on all nodes are turned off,  
                but if specified with the -name or  
                -type flags, only the timers on specified nodes are turned off.  
                If the timers on all nodes become turned off, then global timing is also  
                turned off as well.  
                Properties: create, query
        timerOn (bool?): Turns on node timing. By default, the timers on all nodes are turned on,  
                but if specified with the -name or  
                -type flags, only the timers on specified nodes are turned on.  
                The global timers are also turned on by this command.  
                Note that turning on timing does NOT reset the timers to zero. Use the -reset  
                flag to reset the timers. The idea for NOT resetting the timers is to allow the  
                user to arbitrarily turn timing on and off and continue to add to the  
                existing timer values.  
                Properties: create, query
        trace (bool?): Turns on or off detailed execution tracing.  
                By default, tracing is off. If enabled, each timeable operation is logged when it starts and  
                again when it ends. This flag can be used in conjunction with -outputFile to specify where the  
                output is generated to. The following example shows how the output is formatted:  
              
                dgtimer:begin: compute 3 particleShape1Deformed particleShape1Deformed.lastPosition  
              
                The above is an example of the output when -trace is true that marks the start  
                of an operation. For specific details on each field: the "dgtimer:begin:" string  
                is an identifying marker to flag that this is a begin operation record. The  
                second argument, "compute" in our example, is the operation metric. You can view  
                the output of each given metric via "dgtimer -q" by specifying the -show flag.  
                The integer which follows (3 in this case) is the depth in the operation stack,  
                and the third argument is the name of the node (particleShape1Deformed). The  
                fourth argument is specific to the metric. For "compute", it gives the name of  
                the plug being computed. For "callback", its the internal Maya name of the callback.  
                For "dirty", its the name of the plug that dirtiness is being propagated from.  
              
                dgtimer:end: compute 3 particleShape1Deformed 0.000305685 0.000305685  
              
                The above is the end operation record. The "compute", "3" and "particleShapeDeformed"  
                arguments were described in the "dgtimer:begin" overview earlier. The two floating-point  
                arguments are self time and inclusive time for the operation measured in seconds.  
                The inclusive measure lists the total time since the matching "dgtimer:begin:" entry  
                for this operation, while the self measure lists the inclusive time minus any time  
                consumed by child operations which may have occurred during execution of the current operation.  
                As noted elsewhere in this document, these two times are "wall clock times", measuring  
                elapsed time including any time in which Maya was idle or performing system calls.  
              
                Since dgtimer can measure some non-node qualities in Maya, such as global message  
                callbacks, a "-" is displayed where the node name would ordinarily be displayed.  
                The "-" means "not applicable".  
                Properties: create
        type (Queryable[str]?): Used in conjunction with -reset or -query to specify the type of the node(s)  
                (e.g. animCurveTA) to reset or print timer values for.  
                When querying, use of the -combineType flag will cause all nodes of the  
                same type to be combined into one entry, and only one line of output is  
                generated (i.e. the global timers and header information is omitted).  
                Note: the -name and -type flag cannot be used together.  
                Properties: create, query
        uniqueName (bool?): Used to specify that the DAG nodes listed in the output should be  
                listed by their unique names.  The full DAG path to the object  
                will be printed out instead of just the node name.  
                Properties: create, query
        updateHeatMap (int?): Forces Maya's heat map to rebuild based on the specified parameters.  
                The heat map is an internal dgtimer structure used in mapping  
                intensity values to colourmap entries during display by the HyperGraph  
                Editor. There is one heat map shared by all editors that are using heat  
                map display mode. Updating the heat map causes the timer values on all  
                nodes to be analysed to compose the distribution of entries in the heat map.  
                The parameter is the integer number of divisions in the map and should equal  
                the number of available colours for displaying the heat map. This flag can  
                be specified with the -rangeLower and -rangeUpper flags  
                to limit the range of displayable to lie between the percentile range.  
                The dgtimer command returns the maximum timing value for all nodes in Maya  
                for the specified metric and type.  
                Note: when the display range includes 0, the special zeroth (exactly zero)  
                slot in the heat map is avilable.  
                Properties: create

    Returns:
        float: By default, the total of self-compute time for all nodes. Can be modified via the -returnType, -sortMetric and -sortType flags.

    Example:
    """

