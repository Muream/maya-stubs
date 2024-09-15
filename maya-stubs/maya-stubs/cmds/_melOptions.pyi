from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def melOptions(*, query: bool = ..., duplicateVariableWarnings: bool = ...) -> bool:
    """Set and query options that affect the behavior of Maya's Embedded Language
    (MEL).
    Args:
        duplicateVariableWarnings (bool?): When turned on, this option will cause a warning to be generated whenever a  
                MEL variable is declared within the same scope as another variable with  
                the same name.  
                The warnings will be generated when the script is sourced, not when it  
                is executed. Usually these warnings indicate an error in the script.  
              
                On query the current setting of the option will be returned.  
              
                The corresponding preference optionVar is melDuplicateVariableWarnings.  
                Properties: create, query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

