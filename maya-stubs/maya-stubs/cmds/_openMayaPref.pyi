from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def openMayaPref(*, edit: bool = ..., query: bool = ..., errlog: bool = ..., lazyLoad: bool = ..., oldPluginWarning: bool = ...) -> Union[int, bool]:
    """Set or query API preferences.
    Args:
        errlog (bool?): toggles whether or not an error log of failed API method  
                calls will be created.  When set to true, a file called  
                "OpenMayaErrorLog" will be created in Maya's current working  
                directory.  Each time an API method fails, a detailed  
                description of the error will be written to the file along  
                with a mini-stack trace that indicates the routine that  
                called the failing method.  
                Defaults to false(off).  
                Properties: create, query, edit
        lazyLoad (bool?): toggles whether or not plugins will be loaded with  
                the RTLD_NOW flag or the RTLD_LAZY flag of dlopen(3C).  If  
                set to true, RTLD_LAZY will be used.  In this mode references  
                to functions that cannot be resolved at load time will not be  
                considered an error.  However, if one of these symbols is  
                actually dereferenced by the plug-in at run time, Maya will crash.  
                Defaults to false(off).  
                Properties: create, query, edit
        oldPluginWarning (bool?): toggles whether or not loadPlugin will generate a  
                warning when plug-ins are loaded that were compiled against  
                an older, and possibly incompatible Maya release.  
                Defaults to true(on).  
                Properties: create, query, edit

    Returns:
        int: indicates success or failure

    Example:
    """

