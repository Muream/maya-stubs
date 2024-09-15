from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def panelHistory(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., back: bool = ..., clear: bool = ..., defineTemplate: str = ..., exists: bool = ..., forward: bool = ..., historyDepth: Queryable[int] = ..., isEmpty: bool = ..., suspend: bool = ..., targetPane: Queryable[str] = ..., useTemplate: str = ..., wrap: bool = ...) -> Union[str, int, bool]:
    """This command creates a panel history object.  The object is targeted on a
    particular paneLayout and thereafter notes changes in panel configurations
    within that paneLayout, building up a history list.  The list can be stepped
    through backwards or forwards.
    Args:
        back (bool?): Go back one level on the history list.  
                Properties: edit
        clear (bool?): Clear the history stack  
                Properties: edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        forward (bool?): Go forward one level on the history list.  
                Properties: edit
        historyDepth (Queryable[int]?): Specifies how many levels of history are maintained.  
                Properties: query, edit
        isEmpty (bool?): Returns true if there is currently no panel history.  
                Properties: query
        suspend (bool?): Specifies whether to suspend or resume updates to the panel history.  
                Useful for chunking a number of changes into one history event.  
                Properties: edit
        targetPane (Queryable[str]?): Specifies which paneLayout the history will be maintained for.  
                Properties: create, query
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        wrap (bool?): Specifies whether the history will wrap at the end and  
                beginning.  This value is true by default.  
                Properties: query, edit

    Returns:
        str: The name of the panelHistory object created.

    Example:
    """

