from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def workspaceLayoutManager(*, edit: bool = ..., query: bool = ..., collapseMainWindowControls: Tuple[str, bool] = ..., current: bool = ..., delete: str = ..., i: str = ..., listLayouts: bool = ..., listModuleLayouts: bool = ..., listUserLayouts: bool = ..., modified: str = ..., parentWorkspaceControl: str = ..., reset: bool = ..., restoreMainWindowControls: bool = ..., save: bool = ..., saveAs: str = ..., setCurrent: str = ..., setCurrentCallback: str = ..., setModifiedCallback: str = ..., type: str = ...) -> Union[List[str], bool]:
    """The Workspace Layout Manager loads and saves the layout of the various toolbars and windows in the user interface.
    This command allows listing and managing their properties.
    Args:
        collapseMainWindowControls (Tuple[str, bool]?): Saves main window layout and collapses all other controls in main window except the given one (first parameter)  
                if it does not have any size constraint. Second parameter specifies if main window UI elements should be hidden or not.  
                Properties: create
        current (bool?): Get the name of the current layout.  
                Properties: create, query
        delete (str?): Delete the given workspace. The string is the name of the layout, not the file name.  
                Properties: create
        i (str?): Import the given workspace file to the workspaces directory. The string is an absolute path.  
                Properties: create
        listLayouts (bool?): List the names of all registered layouts.  
                Properties: create
        listModuleLayouts (bool?): List the names of module layouts.  
                Properties: create
        listUserLayouts (bool?): List the names of user layouts.  
                Properties: create
        modified (str?): Check whether or not the specified layout has been modified.  
                Properties: create
        parentWorkspaceControl (str?): Returns the parent workspace control of the given UI (panel) or an empty string if it does not exist.  
                Properties: create
        reset (bool?): Reset the current workspace to its original layout. Factory layouts will be reverted to default while user layouts will be reloaded from disk.  
                Properties: create
        restoreMainWindowControls (bool?): Restores the main window layout to the one saved with the -cmw/-collapseMainWindowControls flag.  
                The loaded workspace file will be deleted once it is restored.  
                Properties: create
        save (bool?): Save the current layout.  
                Properties: create
        saveAs (str?): Save the current layout under the specified name.  
                Properties: create
        setCurrent (str?): Load the given workspace.  The string is the name of the layout, not the file name.  
                Properties: create
        setCurrentCallback (str?): MEL only.  The string is interpreted as a MEL callback, which is called  
                each time a layout is set as current (with -setCurrent flag).  
                The callback is of the form:  
              
                global proc MySetCurrentCallback(string $layoutName)  
                Properties: create
        setModifiedCallback (str?): MEL only.  The string is interpreted as a MEL callback, which is called  
                each time a layout is modified or restored, that is, each time the -modified flag value changes.  
                The callback is of the form:  
              
                global proc MySetModifiedCallback()  
                Properties: create
        type (str?): Get the type of the specified layout: FACTORY, FACTORY_OVERRIDE, MODULE, MODULE_OVERRIDE or USER.  
                Properties: create

    Returns:
        List[str]: depending on arguments

    Example:
    """

