from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def assignCommand(arg0: int = ..., /, *, edit: bool = ..., query: bool = ..., addDivider: str = ..., altModifier: bool = ..., annotation: Queryable[str] = ..., command: Queryable[Callable[..., Any]] = ..., commandModifier: bool = ..., ctrlModifier: bool = ..., data1: Queryable[str] = ..., data2: Queryable[str] = ..., data3: Queryable[str] = ..., delete: int = ..., dividerString: Queryable[str] = ..., enableCommandRepeat: bool = ..., factorySettings: bool = ..., index: int = ..., keyArray: bool = ..., keyString: Queryable[str] = ..., keyUp: bool = ..., name: bool = ..., numDividersPreceding: Queryable[int] = ..., numElements: bool = ..., optionModifier: bool = ..., sortByKey: bool = ..., sourceUserCommands: bool = ...) -> Union[bool, str, Callable[..., Any], int]:
    """This command allows the user to assign hotkeys and manipulate the internal
    array of named command objects. Each object in the array has an 1-based
    index which is used for referencing. Under expected usage you should
    not need to use this command directly as the Hotkey Editor may be used
    to assign hotkeys.This command is obsolete for setting new hotkeys, instead please use the "hotkey" command.
    Args:
        addDivider (str?): Appends an "annotated divider" item to the end of the list of  
                commands.  
                Properties: edit
        altModifier (bool?): This flag specifies if an alt modifier is used for the key.  
                Properties: edit
        annotation (Queryable[str]?): The string is the english name describing the command.  
                Properties: query, edit
        command (Queryable[Callable[..., Any]]?): This is the command that is executed when this object is  
                mapped to a key or menuItem.  
                Properties: query, edit
        commandModifier (bool?): This flag specifies if a command modifier is used for the key.  
                This is only available on systems which support a separate command key.  
                Properties: edit
        ctrlModifier (bool?): This flag specifies if a ctrl modifier is used for the key.  
                Properties: edit
        data1 (Queryable[str]?): Optional, user-defined data strings may be attached to  
                the nameCommand objects.  
                Properties: query, edit
        data2 (Queryable[str]?): Optional, user-defined data strings may be attached to  
                the nameCommand objects.  
                Properties: query, edit
        data3 (Queryable[str]?): Optional, user-defined data strings may be attached to  
                the nameCommand objects.  
                Properties: query, edit
        delete (int?): This tells the Manager to delete the object at position index.  
                Properties: edit
        dividerString (Queryable[str]?): If the passed index corresponds to a "divider" item, then the  
                divider's annotation is returned.  Otherwise, a null string is  
                returned.  
                Properties: query
        enableCommandRepeat (bool?): This flag specifies whether command repeat is enabled.  
                Properties: edit
        factorySettings (bool?): This flag sets the manager back to factory settings.  
                Properties: edit
        index (int?): The index of the object to operate on. The index value  
                ranges from 1 to the number of name command objects.  
                Properties: edit
        keyArray (bool?): This flag returns all of the hotkeys on the command.  
                Properties: query
        keyString (Queryable[str]?): This specifies a key to assign a command to in edit mode.  
                In query mode this flag returns the key string, modifiers and  
                indicates if the command is mapped to keyUp or keyDown.  
                Properties: query, edit
        keyUp (bool?): This flag specifies if the command is executed on keyUp  
                or keyDown.  
                Properties: edit
        name (bool?): The name of the command object.  
                Properties: query
        numDividersPreceding (Queryable[int]?): If the index of a namedCommand object C is passed in,  
                then this flag returns the number of "divider" items preceding  
                C when the namedCommands are sorted by category.  
                Properties: query
        numElements (bool?): This command returns the number of namedCommands in the system.  
                This flag doesn't require the index to be specified.  
                Properties: query
        optionModifier (bool?): This flag specifies if an option modifier is used for the key.  
                Properties: edit
        sortByKey (bool?): This key tells the manager to sort by key or by order of  
                creation.  
                Properties: query, edit
        sourceUserCommands (bool?): This command sources the user named command file.  
                Properties: edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

