from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def stringArrayIntersector(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowDuplicates: bool = ..., defineTemplate: str = ..., exists: bool = ..., intersect: List[str] = ..., reset: bool = ..., useTemplate: str = ...) -> str:
    """The stringArrayIntersector command creates and edits an object which is
    able to efficiently intersect large string arrays. The intersector object
    maintains a sense of "the intersection so far", and updates the
    intersection when new string arrays are provided using the -i/intersect
    flag.Note that the string intersector object may be deleted using the deleteUI
    command.
    Args:
        allowDuplicates (bool?): Should the intersector allow duplicates in the input arrays (true),  
                or combine all duplicate entries into a single, unique entry (false).  
                This flag must be used when initially creating the intersector.  
                Default is 'false'.  
                Properties: create
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        intersect (List[str]?): Intersect the specified string array with the current intersection  
                being maintained by the intersector.  
                Properties: create, edit
        reset (bool?): Reset the intersector to begin a new intersection.  
                Properties: edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: The name of the intersector.

    Example:
    """

