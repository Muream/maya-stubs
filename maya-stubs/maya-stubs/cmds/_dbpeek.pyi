from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dbpeek(*args: str, query: bool = ..., allObjects: bool = ..., argument: Multiuse[str] = ..., count: Queryable[int] = ..., evaluationGraph: bool = ..., operation: Queryable[str] = ..., outputFile: Queryable[str] = ...) -> Union[List[str], str, int, bool]:
    """Thecommand is used to analyze the Maya data for
    information of interest. See a description of the flags for details
    on what types of things can be analyzed.debug, node, attribute
    Args:
        allObjects (bool?): Ignore any specified or selected objects and peek into all applicable  
                objects. The definition of "allObjects" will vary based on the peek  
                operation being performed - see the flag documentation for details on  
                what it means for a given operation.  
                By default if no objects are selected or specified then it will behave  
                as though this flag were set.  
                Properties: create, query
        argument (Multiuse[str]?): Specify one or more arguments to be passed to the operation. The acceptable  
                values for the argument string are documented in the flag to which they will be  
                applied. If the argument itself takes a value then the value will be of the  
                form "argname=argvalue".  
                			In query mode, this flag needs a value.  
                Properties: create, query, multiuse
        count (Queryable[int]?): Specify a count to be used by the test. Different tests make different use of  
                the count, query the operation to find out how it interprets the value.  
                For example a performance test might use it as the number of iterations to run  
                in the test, an output operation might use it to limit the amount of output it  
                produces.  
                Properties: create, query
        evaluationGraph (bool?): Ignore any nodes that are not explicitly part of the evaluation graph.  
                Usually this means nodes that are affected either directly or indirectly  
                by animation. May also tailor the operation to be EM-specific in the  
                areas where the structure of the DG differs from the structure of the  
                EM, for example, plug configurations.  
                This is a filter on the currently selected nodes, including the use of  
                the "allObjects" flag.  
                Properties: create, query
        operation (Queryable[str]?): Specify the peeking operation to perform. The various operations are registered at  
                run time and can be listed by querying this flag without a value. If you  
                query it with a value then you get the detail values that peek operation accepts and  
                a description of what it does.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        outputFile (Queryable[str]?): Specify the location of a file to which the information is to be  
                dumped. Default will return the value from the command.  Use the  
                special names stdout and stderr to redirect to your  
                command window.  
                The special name msdev is available when debugging on Windows  
                to direct your output to the debug tab in the output window of Visual  
                Studio.  
                Properties: create, query

    Returns:
        List[str]: Query of operation yields a string array with available operations
        List[str]: Query of argument yields a string array with available argument definitions on the specified operation
        str: Query of specific operation without an output file returns a string with help information for that operation
        int: Query of specific operation with an output file dumps the help information for that operation to that file and returns the number of errors encountered

    Example:
    """

