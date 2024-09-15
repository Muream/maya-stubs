from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sceneLint(*args: Any, query: bool = ..., issueType: Queryable[Multiuse[str]] = ..., verbose: bool = ...) -> Union[str, List[str], Multiuse[str], bool]:
    """{
            "sceneLint" : {
                    "ISSUE_CODE" : {
                            "description" : "DETAILED_DESCRIPTION_OF_ISSUE",
                            "mitigation" : [        // List of mitigations that can be applied
                                    {
                                            "objects"     : [ LIST_OF_STRINGS_NAMING_OBJECTS_TO_WHICH_IT_APPLIES ],
                                            "benefit"     : DESCRIPTION_OF_HOW_THE_CODE_MAKES_THE_SCENE_BETTER,
                                            "description" : DESCRIPTION_OF_WHAT_THE_CODE_DOES,
                                            "code"        : PYTHON_MITIGATION_CODE_WITH_LOOP_OVER_INSTANCES
                                    }
                            ]
                    }
            }
    }Thecommand is used to analyze the currently loaded scene
    to find potential areas for improvement in performance, memory use, or reduction
    of clutter.In the query mode it will report back the list of available checks it can do.
    Each check will have an associated short-form which can be passed to the command
    to run specific checks.In create mode the returned string is a JSON format list of issues and mitigations
    that suggest a way to solve the problem it describes.Mitigation can be automatically performed by extracting the mitigation code and arguments
    then running the Python codedebug, performance
    Args:
        issueType (Queryable[Multiuse[str]]?): Specify a set of issue types to be checked. If omitted then all known issue types are checked.  
                In query mode returns a description of what a particular issue type is checking.  
                			In query mode, this flag can accept a value.  
                Properties: create, query, multiuse
        verbose (bool?): If set then include both name and description when querying the list of available issue types.  
                Properties: create, query

    Returns:
        str: JSON formatted results showing the issues that could potentially cause problems in the scene.
        List[str]: When querying issueType shows the description, and benefit values for the named scene issue.
        List[str]: When querying returns the list of all issueTypes by name.

    Example:
    """

