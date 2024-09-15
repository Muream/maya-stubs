from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def iconTextScrollList(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowMultiSelection: bool = ..., annotation: Queryable[str] = ..., append: Multiuse[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand: Callable[..., Any] = ..., defineTemplate: str = ..., deselectAll: bool = ..., docTag: Queryable[str] = ..., doubleClickCommand: Callable[..., Any] = ..., dragCallback: Callable[..., Any] = ..., dragFeedbackVisible: bool = ..., dropCallback: Callable[..., Any] = ..., dropRectCallback: Callable[..., Any] = ..., editIndexed: int = ..., editable: bool = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., itemAt: Tuple[int, int] = ..., itemTextColor: Multiuse[Tuple[int, float, float, float]] = ..., manage: bool = ..., noBackground: bool = ..., numberOfIcons: Queryable[int] = ..., numberOfPopupMenus: bool = ..., numberOfRows: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., removeAll: bool = ..., selectCommand: Callable[..., Any] = ..., selectIndexedItem: Queryable[Multiuse[int]] = ..., selectItem: Queryable[Multiuse[str]] = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., visualRectAt: Tuple[int, int] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Multiuse[int], Multiuse[str], Callable[..., Any]]:
    """This command creates/edits/queries a text scrolling list. The
    list can be in single select mode where only one item at at time
    is selected, or in multi-select mode where many items may be
    selected.
    Args:
        allowMultiSelection (bool?): Specify multi or single selection mode.  
                Properties: create, query, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        append (Multiuse[str]?): Add an item to the end of the list.  
                Properties: create, edit, multiuse
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        changeCommand (Callable[..., Any]?): Script to run when the list changes  
                Properties: create, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deselectAll (bool?): Deselect all items.  
                Properties: create, edit
        docTag (Queryable[str]?): Add a documentation flag to the control.  The documentation flag  
                has a directory structure.  
                (e.g., -dt render/multiLister/createNode/material)  
                Properties: create, query, edit
        doubleClickCommand (Callable[..., Any]?): Specify the command to be executed when an item is double clicked.  
                Properties: create, edit
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
        dragFeedbackVisible (bool?): Should the drag feedback be shown in the scrollbar?  
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
        dropRectCallback (Callable[..., Any]?): Adds a callback that is called when a drag and drop  
                operation is hovering above the drop site.  It returns the shape of the  
                rectangle to be drawn to highlight the entry, if the control can receive  
                the dropped data. The MEL version of the callback is of the form:  
              
                global proc int[] callbackName(string $dropControl, int $x, int $y)  
              
                The return value is an array of size 4, with the parameters, in order, being  
                the left and top coordinates of the rectangle to be drawn, followed by the  
                width and height.  
                This functionality is currently only implemented in MEL.  
                Properties: edit
        editIndexed (int?): Index of the edited field  
                Properties: create, edit
        editable (bool?): Set the field to be editable or not  
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
        itemAt (Tuple[int, int]?): Return the name of the item, if any, located at given point  
                      In query mode, this flag needs a value.  
                Properties: query
        itemTextColor (Multiuse[Tuple[int, float, float, float]]?): Set the text color of the item at the given index. Arguments are:  
                index, red, green, and blue. Indices are 1. based. Each color  
                component ranges in value from 0.0 to 1.0.  
                Properties: create, edit, multiuse
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfIcons (Queryable[int]?): Number of icons.  
                Properties: query
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        numberOfRows (bool?): Number of visible rows.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        removeAll (bool?): Remove all items.  
                Properties: create, edit
        selectCommand (Callable[..., Any]?): Specify the command to be executed when an item is selected.  
                Properties: create, edit
        selectIndexedItem (Queryable[Multiuse[int]]?): Select the indexed item. Indices are 1. based.  
                Properties: create, query, edit, multiuse
        selectItem (Queryable[Multiuse[str]]?): Select the item that contains the specified text.  
                Properties: create, query, edit, multiuse
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
        visualRectAt (Tuple[int, int]?): Return the visual rectangle of the item, if any, located at given point. The  
                result is a an array of 4 integers, in local coordinates, describing the  
                rectangle, in the following order: left, top, width, height.  
                      In query mode, this flag needs a value.  
                Properties: query
        width (Queryable[int]?): The width of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit

    Returns:
        str: Full path name to the control.

    Example:
    """

