from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def uiTemplate(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., defineTemplate: str = ..., exists: bool = ..., useTemplate: str = ...) -> str:
    """This command creates a new command template object. Template objects can
    hold default flag arguments for multiple UI commands. The command arguments
    are specified with the individual commands using the -defineTemplate
    flag and the desired flags and arguments.  See also
    Args:
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: The name of the uiTemplate created.

    Example:
    """

