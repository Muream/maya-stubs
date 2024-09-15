from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def refresh(*, currentView: bool = ..., fileExtension: str = ..., filename: str = ..., force: bool = ..., suspend: bool = ...) -> bool:
    """This command is used to force a redraw during script execution.
    Normally, redraw is suspended while scripts are executing but
    sometimes it is useful to show intermediate results for purposes
    such as capturing images from the screen.If the -cv flag is specified, then only the current active view
    is redrawn.
    Args:
        currentView (bool?): Redraw only the current view (default redraws all views).  
                Properties: create
        fileExtension (str?): Specify the type of file to save using the filename flag.  
                Properties: create
        filename (str?): Specify the name of a file in which to save a snapshot of the  
                viewports, or just the current one if the currentView flag is set.  
                Properties: create
        force (bool?): Force the refresh regardless of the state of the model.  
                Properties: create
        suspend (bool?): Suspends or resumes Maya's handling of refresh events. Specify "on" to  
                suspend refreshing, and "off" to resume refreshing. Note that  
                resuming refresh does not itself cause a refresh -- the next natural refresh  
                event in Maya after "refresh -suspend off" is issued will cause the refresh  
                to occur. Use this flag with caution: although it provides opportunities  
                to enhance performance, much of Maya's dependency graph evaluation in  
                interactive mode is refresh driven, thus use of this flag may lead to  
                slight solve differences when you have a complex dependency graph with  
                interrelations.  
                Properties: create

    Returns:
        bool:

    Example:
    """

