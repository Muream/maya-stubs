from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dockControl(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowedArea: Queryable[Multiuse[str]] = ..., annotation: Queryable[str] = ..., area: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., closeCommand: Callable[..., Any] = ..., content: Queryable[str] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dockStation: str = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., enablePopupOption: bool = ..., exists: bool = ..., fixedHeight: bool = ..., fixedWidth: bool = ..., floatChangeCommand: Callable[..., Any] = ..., floating: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., label: Queryable[str] = ..., manage: bool = ..., moveable: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., r: bool = ..., retain: bool = ..., sizeable: bool = ..., splitLayout: str = ..., state: Queryable[str] = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Multiuse[str], Tuple[float, float, float], bool, int, Callable[..., Any]]:
    """Create a dockable control, also known as tool palette or utility window.
    Dock controls are secondary windows placed in the dock area around the central control in a main window.
    Dock windows can be moved inside their current area, moved into new areas and floated (e.g. undocked).
    Dock control consists of a title bar and the content area. The titlebar displays the dock control window title, a float button and a close button.
    Depending on the state of the dock control, the float and close buttons may be either disabled or not shown at all.
    Args:
        allowedArea (Queryable[Multiuse[str]]?): Areas where the dock control may be placed. Valid values are "top", "left", "bottom", "right" and "all".  The default is "all".  
                Properties: create, query, edit, multiuse
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        area (Queryable[str]?): The initial dock area for this dock control. This is a required flag.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        closeCommand (Callable[..., Any]?): Script executed after the dock control is closed.  
                Properties: create, edit
        content (Queryable[str]?): The name of the control that is the content of this dock control.  This is a required flag.  
                Properties: create, query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        docTag (Queryable[str]?): Add a documentation flag to the control.  The documentation flag  
                has a directory structure.  
                (e.g., -dt render/multiLister/createNode/material)  
                Properties: create, query, edit
        dockStation (str?): The name of the control the window can be docked into.  
                If this is not set it is assumed to be the main window.  
                Properties: create
        dragCallback (Callable[..., Any]?): Adds a callback that is called when the middle mouse button  
                is pressed.  The MEL version of the callback is of the form:  
              
                global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  
              
                The proc returns a string array that is transferred to the drop site.  
                By convention the first string in the array describes the user settable  
                message type.  Controls that are application defined drag sources may  
                ignore the callback. $mods allows testing for the key modifiers CTRL and  
                SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,  
                3 == CTRL + SHIFT.  
              
                In Python, it is similar, but there are two ways to specify the callback.  The  
                recommended way is to pass a Python function object as the argument.  In that  
                case, the Python callback should have the form:  
              
                def callbackName( dragControl, x, y, modifiers ):  
              
                The values of these arguments are the same as those for the MEL version above.  
              
                The other way to specify the callback in Python is to specify a string to be  
                executed.  In that case, the string will have the values substituted into it  
                via the standard Python format operator.  The format values are passed in a  
                dictionary with the keys "dragControl", "x", "y", "modifiers".  The  
                "dragControl" value is a string and the other values are integers (eg the  
                callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")  
                Properties: create, edit
        dropCallback (Callable[..., Any]?): Adds a callback that is called when a drag and drop  
                operation is released above the drop site.  The MEL version of the callback is  
                of the form:  
              
                global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  
              
                The proc receives a string array that is transferred from the drag source.  
                The first string in the msgs array describes the user defined message type.  
                Controls that are application defined drop sites may ignore the  
                callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  
              
                In Python, it is similar, but there are two ways to specify the callback.  The  
                recommended way is to pass a Python function object as the argument.  In that  
                case, the Python callback should have the form:  
              
                def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  
              
                The values of these arguments are the same as those for the MEL version above.  
              
                The other way to specify the callback in Python is to specify a string to be  
                executed.  In that case, the string will have the values substituted into it  
                via the standard Python format operator.  The format values are passed in a  
                dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",  
                "type".  The "dragControl" value is a string and the other values are integers  
                (eg the callback string could be  
                "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")  
                Properties: create, edit
        enable (bool?): The enable state of the control.  By default, this flag is  
                set to true and the control is enabled.  Specify false and the control  
                will appear dimmed or greyed-out indicating it is disabled.  
                Properties: create, query, edit
        enableBackground (bool?): Enables the background color of the control.  
                Properties: create, query, edit
        enableKeyboardFocus (bool?): If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.  
                This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.  
                If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).  
                Properties: create, query, edit
        enablePopupOption (bool?): Whether or not the menu option for the dock control in the UI Elements popup menu is enabled.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fixedHeight (bool?): Whether or not the dockControl height may be interactively resized.  
                Properties: create, query, edit
        fixedWidth (bool?): Whether or not the dockControl width may be interactively resized.  
                Properties: create, query, edit
        floatChangeCommand (Callable[..., Any]?): The script executed when the floating state of the dock widget changes.  
                Properties: create, edit
        floating (bool?): Whether the dock widget is floating.  
                A floating dock widget is presented to the user as an independent window "on top" of main window, instead of being docked in the main window.  
                Properties: create, query, edit
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        highlightColor (Queryable[Tuple[float, float, float]]?): The highlight color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query, edit
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        label (Queryable[str]?): The label text.  The default label is the name of the control.  
                Properties: create, query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        moveable (bool?): Control over whether or not the dockControl may be undocked/redocked.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        r (bool?): Whether the dock widget is visible and either floating or at the top of its dock widget area.  
                Properties: query, edit
        retain (bool?): Control over whether or not the window and its contents are deleted when closed.  
                The default is true.  The window and its contents are retained when closed unless this is set to false.  
                Properties: create, query, edit
        sizeable (bool?): Whether or not the dockControl width may be interactively resized.  
                Deprecated!!  Use the fixedWidth flag instead.  
                Properties: create, query, edit
        splitLayout (str?): When two windows are added to a single docking area they are by default tabbed together.  
                Setting a value for splitLayout will allow it to be placed next to another control in the same area.  
                The flag's argument controls the orientation of the split.  
                Valid values are "horizontal" or "vertical".  
                Properties: create
        state (Queryable[str]?): When queried this flag will return a string holding the dock control state information.  
                This string is a hexadecimal representation of a binary string and is not meant to be humanly readable,  
                but can be saved and loaded using the optionVar command to restore a dock control's state across sessions of Maya.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        visible (bool?): The visible state of the control.  A control is created  
                visible by default.  Note that a control's actual appearance is  
                also dependent on the visible state of its parent layout(s).  
                Properties: create, query, edit
        visibleChangeCommand (Queryable[Callable[..., Any]]?): Command that gets executed when visible state of the control changes.  
                Properties: create, query, edit
        width (Queryable[int]?): The width of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit

    Returns:
        str: Full path name to the control.

    Example:
    """

