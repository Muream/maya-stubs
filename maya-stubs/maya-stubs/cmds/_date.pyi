from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def date(*, date: bool = ..., format: str = ..., shortDate: bool = ..., shortTime: bool = ..., time: bool = ...) -> str:
    """Returns information about current time and date. Use the predefined formats, or theflag to specify the output format.time, date
    Args:
        date (bool?): Returns the current date. Format is YYYY/MM/DD  
                Properties: create
        format (str?): Specifies a string defining how the date and time should be represented. All  
                occurences of the keywords below will be replaced with the corresponding  
                values:  
              
                KeywordBecomes  
                YYYYCurrent year, using 4 digits  
                YYLast two digits of the current year  
                MMCurrent month, with leading 0 if necessary  
                DDCurrent day, with leading 0 if necessary  
                hhCurrent hour, with leading 0 if necessary  
                mmCurrent minute, with leading 0 if necessary  
                ssCurrent second, with leading 0 if necessary  
                Properties: create
        shortDate (bool?): Returns the current date. Format is MM/DD  
                Properties: create
        shortTime (bool?): Returns the current time. Format is hh:mm  
                Properties: create
        time (bool?): Returns the current time. Format is hh:mm:ss  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

