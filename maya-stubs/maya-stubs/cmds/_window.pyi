from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def window(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., backgroundColor: Tuple[float, float, float] = ..., closeCommand: Callable[..., Any] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dockCorner: Multiuse[Tuple[str, str]] = ..., dockStation: bool = ..., dockingLayout: Queryable[str] = ..., exists: bool = ..., frontWindow: bool = ..., height: Queryable[int] = ..., iconName: Queryable[str] = ..., iconify: bool = ..., interactivePlacement: bool = ..., leftEdge: Queryable[int] = ..., mainMenuBar: bool = ..., mainWindow: bool = ..., maximizeButton: bool = ..., menuArray: bool = ..., menuBar: bool = ..., menuBarCornerWidget: Queryable[Tuple[str, str]] = ..., menuBarResize: bool = ..., menuBarVisible: bool = ..., menuIndex: Tuple[str, int] = ..., minimizeButton: bool = ..., minimizeCommand: Callable[..., Any] = ..., nestedDockingEnabled: bool = ..., numberOfMenus: bool = ..., parent: str = ..., resizeToFitChildren: bool = ..., restoreCommand: Callable[..., Any] = ..., retain: bool = ..., sizeable: bool = ..., state: Queryable[str] = ..., title: Queryable[str] = ..., titleBar: bool = ..., titleBarMenu: bool = ..., toolbox: bool = ..., topEdge: Queryable[int] = ..., topLeftCorner: Queryable[Tuple[int, int]] = ..., useTemplate: str = ..., visible: bool = ..., width: Queryable[int] = ..., widthHeight: Queryable[Tuple[int, int]] = ...) -> Union[str, bool, int, Tuple[str, str], Tuple[int, int]]:
    """This command creates a new window but leaves it invisible. It is most
    efficient to add the window's elements and then make it visible with
    the showWindow command. The window can have an optional menu bar. Also,
    the title bar and minimize/maximize buttons can be turned on or off. If the
    title bar is off, then you cannot have minimize or maximize buttons.Note: The window will require a control layout of some kind
    to arrange the controls (buttons, sliders, fields, etc.).  Examples of
    control layouts are columnLayout, formLayout, rowLayout, etc.Note: This command will clear the uiTemplate stack.  Templates for
    a window need to be set after the window cmd.
    Args:
        backgroundColor (Tuple[float, float, float]?): The background color of the window. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, edit
        closeCommand (Callable[..., Any]?): Script executed after the window is closed.  
                Properties: create, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        docTag (Queryable[str]?): Attach a tag to the window.  
                Properties: create, query, edit
        dockCorner (Multiuse[Tuple[str, str]]?): Specifies which docking areas occupied the four different corners of the window.  
                By default docking windows on the bottom or top will span the whole window.  
                Use multiple instances of this flag to allow the left and right docking areas to occupy the corners.  
                This method has two arguments: docking corner and docking area.  
                Possible values for docking corner are "topLeft", "topRight", bottomLeft", and "bottomRight".  
                Possible values for docking area are "left", "right", "top", and "bottom".  
                Properties: create, multiuse
        dockStation (bool?): When set this flag specifies that this window can contain other docked sub-windows.  
                Properties: create
        dockingLayout (Queryable[str]?): When queried this flag will return a string holding the docking layout information.  
                This string can be set when creating or editing a docking station to restore the previous docking layout.  
                This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,  
                but can be saved and loaded using the optionVar command to restore layouts across sessions of Maya.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        frontWindow (bool?): Return the name of the front window.  Note: you must supply  
                the name of any window (the window does not need to exist).  
                Returns "unknown" if the front window cannot be determined.  
                Properties: query
        height (Queryable[int]?): Height of the window excluding any window frame in pixels.  
                Properties: create, query, edit
        iconName (Queryable[str]?): The window's icon title.  By default it is the same as the  
                window's title.  
                Properties: create, query, edit
        iconify (bool?): Icon state of the window.  
                Properties: create, query, edit
        interactivePlacement (bool?): Deprecated flag. Recognized but not implemented.  
                This flag will be removed in a future version of Maya.  
                Properties: create
        leftEdge (Queryable[int]?): Position of the left edge of the window.  
                Properties: create, query, edit
        mainMenuBar (bool?): If this flag is used then the main menu bar will be enabled.  
                Properties: create, query, edit
        mainWindow (bool?): Main window for the application.  The main window  
                has an 'Exit' item in the Window Manager menu.  By default, the  
                first created window becomes the main window.  
                Properties: create, query, edit
        maximizeButton (bool?): Turns the window's maximize button on or off.  
                Properties: create, query, edit
        menuArray (bool?): Return a string array containing the names of the menus in  
                the window's menu bar.  
                Properties: query
        menuBar (bool?): Adds an empty menu bar to the window.  
                The Qt name of the object will be m_menubar_nameOfTheWindow.  
                Properties: create, query
        menuBarCornerWidget (Queryable[Tuple[str, str]]?): This flag specifies a widget to add to a corner of the parent window.  
                The first argument corresponds to the widget name and the second to the position of the widget.  
                Possible values for widget position are "topLeft", "topRight", "bottomLeft", "bottomRight".  
                In query mode this flag returns all the corner widget names in the following order: topLeft, topRight, bottomLeft, bottomRight.  
                Add the -mbr/-menuBarResize flag to the changeCommand of widget passed (first argument) so that it will always have an  
                appropriate size.  
                Properties: query, edit
        menuBarResize (bool?): This flag should be used with the -mcw/-menuBarCornerWidget flag. This is used to resize the  
                menu bar so that the corner widgets are updated.  
                Properties: edit
        menuBarVisible (bool?): Visibility of the menu bar (if there is one).  
                Properties: create, query, edit
        menuIndex (Tuple[str, int]?): Sets the index of a specified menu.  
                Properties: edit
        minimizeButton (bool?): Turns the window's minimize button on or off.  
                Properties: create, query, edit
        minimizeCommand (Callable[..., Any]?): Script executed after the window is minimized (iconified).  
                Properties: create, edit
        nestedDockingEnabled (bool?): Controls whether nested docking is enabled or not.  Nested docking allows  
                for docking windows next to other docked windows for more possible arrangement styles.  
                Properties: create
        numberOfMenus (bool?): Return the number of menus attached to the window's menu bar.  
                Properties: query
        parent (str?): Specifies a parent window or layout which the created window is  
                always on top of. Note: If the parent is a window the created window  
                is not modal, so events are still propagated to the parent window.  
                Properties: create
        resizeToFitChildren (bool?): The window will always grow/shrink to just fit  
                the controls it contains.  
                Properties: create, query, edit
        restoreCommand (Callable[..., Any]?): Script executed after the window is restored from  
                it's minimized (iconified) state.  
                Properties: create, edit
        retain (bool?): Retains the window after it has been closed.  The default is  
                to delete the window when it is closed.  
                Properties: create
        sizeable (bool?): Whether or not the window may be interactively resized.  
                Properties: create, query, edit
        state (Queryable[str]?): When queried this flag will return a string holding the window state information.  
                This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,  
                but can be saved and loaded using the optionVar command to restore window state across sessions of Maya.  
                Properties: create, query, edit
        title (Queryable[str]?): The window's title.  
                Properties: create, query, edit
        titleBar (bool?): Turns the window's title bar on or off.  
                Properties: create, query, edit
        titleBarMenu (bool?): Controls whether the title bar menu exists in the window  
                title bar. Only valid if -tb/titleBar is true. This Windows  
                only flag is true by default.  
                Properties: create, query, edit
        toolbox (bool?): Makes this a toolbox style window.  A Windows only  
                flag that makes the title bar smaller and uses a slightly  
                different display style.  
                Properties: create, query, edit
        topEdge (Queryable[int]?): Position of the top edge of the window.  
                Properties: create, query, edit
        topLeftCorner (Queryable[Tuple[int, int]]?): Position of the window's top left corner.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        visible (bool?): The window's visibility.  
                Properties: create, query, edit
        width (Queryable[int]?): Width of the window excluding any window frame in pixels.  
                Properties: create, query, edit
        widthHeight (Queryable[Tuple[int, int]]?): Window's width and height excluding any window frame in pixels.  
                Properties: create, query, edit

    Returns:
        str: Name to the window.

    Example:
    """

