from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dbfootprint(*args: str, query: bool = ..., allObjects: bool = ..., outputFile: str = ..., type: Queryable[str] = ...) -> Union[str, List[str]]:
    """This command lets you explore the memory usage of specific parts of the
    scene. Query the 'type' flag to see what all of the different types are,
    and query a specific type to get a description of what information it will
    provide.
    All output is in JSON format so that it can easily be processed and formatted
    to highlight areas of interest.dbtrace, dbpeek
    Args:
        allObjects (bool?): Ignore any specified or selected objects and measure all applicable  
                objects. The definition of "allObjects" will vary based on the type of  
                objects being measured - see the type documentation for details on  
                what it means for that type.  
                By default if no objects are selected or specified then it will behave  
                as though this flag were set.  
                Properties: create
        outputFile (str?): Specify the location of a file to which the information is to be  
                dumped. Default will return the value from the command.  Use the  
                special names stdout, cout, stderr, or cerr to redirect  
                to the standard output or error locations.  
                Properties: create
        type (Queryable[str]?): Specify the type of object footprint to measure. The various types are registered at  
                run time and can be listed by querying this flag without a value. If you query it  
                with a value then you get a description of what that particular type is going to  
                measure.  
                			In query mode, this flag can accept a value.  
                Properties: create, query

    Returns:
        str: JSON data representing the memory usage of the requested objects
        List[str]: List of types for which footprint measurements can be made (Query with no flags)
        str: Description of what a particular type will measure (Query with a 'type' flag)

    Example:
    """

