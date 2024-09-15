from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def fileBrowserDialog(*, actionName: str = ..., dialogStyle: int = ..., fileCommand: Callable[..., Any] = ..., fileType: str = ..., filterList: Multiuse[str] = ..., includeName: str = ..., mode: int = ..., operationMode: str = ..., tipMessage: str = ..., windowTitle: str = ...) -> str:
    """The fileBrowserDialog and fileDialog commands have now been deprecated.
    Both commands are still callable, but it is recommended that the fileDialog2 command
    be used instead.  To maintain some backwards compatibility, both fileBrowserDialog and
    fileDialog will convert the flags/values passed to them into the appropriate flags/values
    that the fileDialog2 command uses and will call that command internally.  It is not
    guaranteed that this compatibility will be able to be maintained in future versions so
    any new scripts that are written should use fileDialog2.See below for an example of how to change a script to use fileDialog2.
    Args:
        actionName (str?): Script to be called when the file is validated.  
                Properties: create
        dialogStyle (int?): 0 for old style dialog  
                1 for Windows 2000 style Explorer style  
                2 for Explorer style with "Shortcut" tip at bottom  
                Properties: create
        fileCommand (Callable[..., Any]?): The script to run on command action  
                Properties: create
        fileType (str?): Set the type of file to filter.  By default this can be any one of:  
                "mayaAscii", "mayaBinary", "mel", "OBJ", "directory", "plug-in", "audio", "move", "EPS", "Illustrator", "image".  
                plug-ins may define their own types as well.  
                Properties: create
        filterList (Multiuse[str]?): Specify file filters. Used with dialog style  
                1 and 2. Each string should be a description followed by a  
                comma followed by a semi-colon separated list of file  
                extensions with wildcard.  
                Properties: create, multiuse
        includeName (str?): Include the given string after the actionName in parentheses.  
                If the name is too long, it will be shortened to fit on the  
                dialog (for example, /usr/alias/commands/scripts/fileBrowser.mel  
                might be shortened to /usr/...pts/fileBrowser.mel)  
                Properties: create
        mode (int?): Defines the mode in which to run the file brower:  
              
                0 for read  
                1 for write  
                2 for write without paths (segmented files)  
                4 for directories have meaning when used with the action  
              
                +100 for returning short names  
                Properties: create
        operationMode (str?): Enables the option dialog. Valid strings are:  
              
                "Import"  
                "Reference"  
                "SaveAs"  
                "ExportAll"  
                "ExportActive"  
                Properties: create
        tipMessage (str?): Message to be displayed at the bottom of the style 2 dialog box.  
                Properties: create
        windowTitle (str?): Set the window title of a style 1 or 2 dialog box  
                Properties: create

    Returns:
        str: Dialog name

    Example:
    """

