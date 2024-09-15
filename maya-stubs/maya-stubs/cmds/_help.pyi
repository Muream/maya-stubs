from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def help(arg0: str = ..., /, *, query: bool = ..., documentation: bool = ..., language: str = ..., list: bool = ..., popupDisplayTime: Queryable[int] = ..., popupMode: bool = ..., popupPauseTime: Queryable[int] = ..., popupSimpleMode: bool = ..., rolloverMode: bool = ..., syntaxOnly: bool = ...) -> Union[bool, int]:
    """With no arguments, help tells how to use help. If a command name is
    specified, help will return the quick help for that command. Other
    flags can be used to open the online documentation, or to list
    available commands based on a pattern.Pattern follows the following syntax:
    Args:
        documentation (bool?): Use a browser to show the documentation associated with the single  
                command name given. A pattern cannot be used with this flag. If no  
                command name is specified, then this flag will go to the main  
                documentation index.  
                Properties: create
        language (str?): Show the help for this command in the specified language.  
                Valid values are "mel" and "python".  
                The default is Mel.  
                Used with the doc flag.  
                Properties: create
        list (bool?): List all the commands whose names match the regular expression. Pass the  
                regular expression as the first argument to the command specified.  
                Properties: create
        popupDisplayTime (Queryable[int]?): Set the amount of time, in seconds, that the popup help  
                will be displayed.  The default is 4 seconds.  
                This flag is mutually exclusive of the list and doc flags.  
                Properties: create, query
        popupMode (bool?): Turn on or off popup help mode.  This flag is mutually exclusive  
                of the list and doc flags.  
                Properties: create, query
        popupPauseTime (Queryable[int]?): Set the amount of time, in milliseconds, before the popup help  
                will be displayed. The default is 800 milliseconds.  
                This flag is mutually exclusive of the list and doc flags.  
                Properties: create, query
        popupSimpleMode (bool?): Turn on or off simple popup help mode. If set, ToolClips will display  
                only name and keyboard shortcut.  
                Properties: create, query
        rolloverMode (bool?): Turn on or off rollover help mode.  This flag is mutually exclusive  
                with the list and doc flags.  
                Properties: create, query
        syntaxOnly (bool?): When no other flag is specified, return only the syntax part of the  
                quick help.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

