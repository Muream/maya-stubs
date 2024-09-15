from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def appHome(*, edit: bool = ..., query: bool = ..., iconVisible: bool = ..., instrument: str = ..., setTab: str = ..., toggleVisibility: bool = ..., updateRecentFiles: bool = ..., visible: bool = ...) -> bool:
    """Used for displaying and hiding application home.
    Args:
        iconVisible (bool?): Query or set application home icon visibility preference.  
              
                Note: Icon visibility cannot be modified if the MAYA_NO_HOME_ICON  
                environment variable is defined.  
                Properties: create, query, edit
        instrument (str?): Instrument the app home command with the given string.  
                Properties: create
        setTab (str?): Navigate app home to the specified tab.  
              
                Available tabs are:  
                Recent  
                GettingStarted  
                Learning  
                WhatsNew  
                Community  
                Properties: create, edit
        toggleVisibility (bool?): Toggle application home widget visibility.  
                Properties: create, edit
        updateRecentFiles (bool?): Update the recent file list data.  
                Properties: create, edit
        visible (bool?): Query or set application home widget visibility.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

