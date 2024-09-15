from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hotkey(arg0: str = ..., /, *, query: bool = ..., altModifier: bool = ..., autoSave: bool = ..., commandModifier: bool = ..., ctrlModifier: bool = ..., ctxClient: Queryable[str] = ..., dragPress: bool = ..., factorySettings: bool = ..., isModifier: bool = ..., keyShortcut: str = ..., name: Queryable[str] = ..., pressCommandRepeat: bool = ..., releaseCommandRepeat: bool = ..., releaseName: Queryable[str] = ..., shiftModifier: bool = ..., sourceUserHotkeys: bool = ...) -> Union[bool, str]:
    """This command sets the single-key hotkeys for the entire application.
    Args:
        altModifier (bool?):   
                Properties: create, query
        autoSave (bool?): If set to true then the hotkeys will always be saved when  
                you quit.  If false then the hotkeys are not saved unless  
                "savePrefs -hotkeys" is used.  
                Properties: create
        commandModifier (bool?): The Command key must be pressed to get the hotkey.  
                This is only available on systems which have a separate  
                command key.  
                Note that if menu item accelerator keys are being used  
                (menuItem -ke/keyEquivalent), then the accelerator key  
                settings override the hotkey settings.  
                Properties: create
        ctrlModifier (bool?): The Ctrl key must be pressed to get the hotkey.  
                Note that if menu item accelerator keys are being used  
                (menuItem -ke/keyEquivalent), then the accelerator key  
                settings override the hotkey settings.  
                Properties: create, query
        ctxClient (Queryable[str]?): Specifies the hotkey context. It is used together with the other flags to modify or query  
                the hotkey for a certain hotkey context. If it is not specified, the global hotkey context will be taken into  
                account. Check hotkeyCtx command to see how the hotkeys work with the hotkey contexts.  
                Properties: create, query
        dragPress (bool?): Specify true and the command may be executed during  
                manipulator dragging, if the tool context also allows  
                this. This flag is false by default.  
                Properties: create
        factorySettings (bool?): Resets the hotkeys back to the initial defaults.  
                Properties: create
        isModifier (bool?): This flag is obsolete and should no longer be used.  
                Properties: create
        keyShortcut (str?): Specify what key is being set. The key must be either a single  
                ascii character (capital and lowercase can be set independently)  
                or one of the keyword  
                strings for the special keyboard characters.  
              
                The valid keywords are:  
                Up, Down, Right, Left,  
                Home, End, Page_Up, Page_Down, Insert  
                Return, Space  
                F1 to F12  
                Tab (Will only work when modifiers are specified)  
                Delete, Backspace (Will only work when modifiers are specified)  
                Properties: create
        name (Queryable[str]?): The name of the namedCommand object that will be executed when the key is pressed.  
                Properties: create, query
        pressCommandRepeat (bool?): Specify true and the command may be repeated by executing  
                the command repeatLast. This flag is false by default.  
                Properties: create
        releaseCommandRepeat (bool?): Specify true and the command may be repeated by executing  
                the command repeatLast. This flag is false by default.  
                Properties: create
        releaseName (Queryable[str]?): The name of the namedCommand object that will be executed when the key is released.  
                Properties: create, query
        shiftModifier (bool?): The Shift key must be pressed to get the hotkey.  
                Properties: create, query
        sourceUserHotkeys (bool?): This flag is obsolete. Please use import flag from hotkeySet command  
                to import the user hotkeys.  
                Properties: create

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

