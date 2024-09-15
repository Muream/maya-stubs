from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def paneLayout(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeFrameThickness: Queryable[int] = ..., activePane: Queryable[str] = ..., activePaneIndex: Queryable[int] = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., childArray: bool = ..., configuration: Queryable[str] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., generalSpacing: int = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., manage: bool = ..., margins: int = ..., noBackground: bool = ..., numberOfChildren: bool = ..., numberOfPopupMenus: bool = ..., numberOfVisiblePanes: bool = ..., pane1: bool = ..., pane2: bool = ..., pane3: bool = ..., pane4: bool = ..., paneSize: Queryable[Multiuse[Tuple[int, int, int]]] = ..., paneUnderPointer: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., separatorMovedCommand: Callable[..., Any] = ..., separatorThickness: Queryable[int] = ..., setPane: Multiuse[Tuple[str, int]] = ..., staticHeightPane: int = ..., staticWidthPane: int = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, int, Tuple[float, float, float], bool, Multiuse[Tuple[int, int, int]], Callable[..., Any]]:
    """This command creates a pane layout.  A pane layout may have any
    number of children but at any one time only certain children may be
    visible, as determined by the current layout configuration.  For
    example a horizontally split pane shows only two children, one on top
    of the other and a visible separator between the two.  The separator
    may be moved to vary the size of each pane.  Various other pane
    configurations are available and all display a moveable separator
    that define the size of each pane in the layout.
    Args:
        activeFrameThickness (Queryable[int]?): The thickness of the frame drawn around the active frame.  
                Specify an integer value greater than or equal to 0.  
                Properties: create, query, edit
        activePane (Queryable[str]?): The active pane has a colored border surrounding it.  Only  
                one pane may be active at any one time.  Using either of the  
                flags -ap/activePane    or -api/activePaneIndex will  
                automatically deactivate the previously active pane.  The argument  
                is the full or short name of the child control.  
                Properties: create, query, edit
        activePaneIndex (Queryable[int]?): The active pane index.  The active pane has a  
                colored border surrounding it.  Only one pane may be active  
                at any one time.  Using either of the flags -ap/activePane  
                or -api/activePaneIndex will automatically deactivate the  
                previously active pane.  The argument is an integer  
                value ranging from 1 to 4.  Panes for any particular configuration  
                are numbered clockwise beginning with the pane in the top left  
                corner of the layout.  If any other index is specified then the  
                current active pane is deactivated.  
                Properties: create, query, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        childArray (bool?): Returns a string array of the names of the layout's  
                immediate children.  
                Properties: query
        configuration (Queryable[str]?): Set the layout configuration for the panes.  Valid values  
                are:  
                "single", "horizontal2", "vertical2", "horizontal3", "vertical3",  
                "top3", "left3", "bottom3", "right3", "horizontal4", "vertical4",  
                "top4", "left4", "bottom4", "right4", "quad"  
                Properties: create, query, edit
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
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        generalSpacing (int?): Sets the spacing for this layout.  
                Properties: edit
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
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        margins (int?): Sets the content margins for this layout.  
                Properties: edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfChildren (bool?): Returns in an int the number of immediate children of the layout.  
                Properties: query
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        numberOfVisiblePanes (bool?): Return the number of panes visible for the present  
                configuration.  
                Properties: query
        pane1 (bool?):   
                Properties: query
        pane2 (bool?):   
                Properties: query
        pane3 (bool?):   
                Properties: query
        pane4 (bool?): Return the name of the control in the respective pane.  
                Properties: query
        paneSize (Queryable[Multiuse[Tuple[int, int, int]]]?): The size of a pane in the current pane layout  
                configuration.  The first argument specifies the pane index and  
                is an integer value ranging from 1 to 4.  Panes for any particular  
                configuration are numbered clockwise beginning with the pane in  
                the top left corner of the layout.  The width and height of the  
                pane are specified by the last two arguments.  Both are  
                integer values and they indicate the percentage of the total  
                pane layout size rather that the number of pixels.  
                Properties: create, query, edit, multiuse
        paneUnderPointer (bool?): Return the name of the child occupying the  
                pane that the pointer is currently over.  An empty string is  
                returned if the pointer is not over a pane.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        separatorMovedCommand (Callable[..., Any]?): This command executed when the pane separators are moved.  
                Properties: create, edit
        separatorThickness (Queryable[int]?): The thickness of the separators between the panes.  
                Specify an integer value greater than 0. This flag has no effect  
                on Windows systems.  
                Properties: create, query, edit
        setPane (Multiuse[Tuple[str, int]]?): This flag allows you to put a child of this layout in a  
                particular pane.  The first argument is the full or short name of  
                the control.  The second argument is an integer value ranging from  
                1 to 4.  Panes for any particular configuration are numbered  
                clockwise beginning with the pane in the top left corner of the  
                layout.  
                Properties: create, edit, multiuse
        staticHeightPane (int?): Set a pane to have a static height, i.e. its height will not  
                change when the layout is dynamically resized. Only one pane  
                can be set to have a static height at one time. This state  
                will be retained even if another child is switched into the  
                pane. Specify 0 to set a pane back to the default state. Any  
                state will be lost if the pane configuration is changed.  
                Properties: create, edit
        staticWidthPane (int?): Set a pane to have a static width, i.e. its width will not  
                change when the layout is dynamically resized. Only one pane  
                can be set to have a static width at one time. This state  
                will be retained even if another child is switched into the  
                pane. Specify 0 to set a pane back to the default state. Any  
                state will be lost if the pane configuration is changed.  
                Properties: create, edit
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

