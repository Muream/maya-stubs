from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sceneUIReplacement(*, clear: bool = ..., deleteRemaining: bool = ..., getNextFilter: Tuple[str, str] = ..., getNextPanel: Tuple[str, str] = ..., getNextScriptedPanel: Tuple[str, str] = ..., update: str = ...) -> str:
    """This command returns existing scene based UI that can be utilized by
    the scene that is being loaded. It can also delete any such UI that is
    not used by the loading scene.
    Args:
        clear (bool?): Frees any resources allocated by the command.  
                Properties: create
        deleteRemaining (bool?): Delete any UI that is scene dependent and has not been referenced by  
                this command since the last update.  
                Properties: create
        getNextFilter (Tuple[str, str]?): Returns the next filter of the specified type with the specified name.  
                Properties: create
        getNextPanel (Tuple[str, str]?): Returns the next panel of the specified type, preferably with the  
                specified label.  
                Properties: create
        getNextScriptedPanel (Tuple[str, str]?): Returns the next scripted panel of the specified scripted panel type,  
                preferably with the specified label.  
                Properties: create
        update (str?): Updates the state of the command to reflect the current state  
                of the application.  The string argument is the name of the  
                main window pane layout holding the panels.  
                Properties: create

    Returns:
        str: When used with getNextScriptedPanel, getNextPanel, or getNextFilter

    Example:
    """

