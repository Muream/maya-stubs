from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def formLayout(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., attachControl: Multiuse[Tuple[str, str, int, str]] = ..., attachForm: Multiuse[Tuple[str, str, int]] = ..., attachNone: Multiuse[Tuple[str, str]] = ..., attachOppositeControl: Multiuse[Tuple[str, str, int, str]] = ..., attachOppositeForm: Multiuse[Tuple[str, str, int]] = ..., attachPosition: Multiuse[Tuple[str, str, int, int]] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., childArray: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., generalSpacing: int = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., manage: bool = ..., margins: int = ..., noBackground: bool = ..., numberOfChildren: bool = ..., numberOfDivisions: Queryable[int] = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, int, Callable[..., Any]]:
    """This command creates a form layout control. A form layout allows
    absolute and relative positioning of the controls that are
    its immediate children.Controls have four edges: top, left, bottom and right.
    There are only two directions that children can be positioned in,
    right-left and up-down. The attach flags take the direction of
    an attachment from the argument that names the edge to attach
    (the second argument). Any or all edges of a child may be
    attached. There are six ways to attach them:Each edge attachment may have an offset that acts to separate
    controls visually.There is no default positioning relationship so to have children
    appear in the form they must have at least one edge attached in
    each direction.In the flag definitions the arguments follow these
    rules:These are multi-use flags so any number of attachments
    may be made in a single command.Avoid making control attachments that form a loop in
    control dependencies. For example:$btn2 is attached to $btn1, $btn3 is attached to $btn2, and $btn1 is
    attached to $btn3. Thus, the placement of $btn1 is dependent on the
    placement of $btn3, which is dependent on the placement of $btn2, which
    is dependent on the placement of $btn1. The last control attachment will
    have created a loop in the dependencies.To prevent runtime errors, Maya will ignore this attachment and instead
    issue a warning that a cyclical control attachment has been detected in
    the script.
    Args:
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        attachControl (Multiuse[Tuple[str, str, int, str]]?): Arguments are: control, edge, offset, control  
                Valid edge values are: "top" | "bottom" | "left" | "right".  
                Attach a control to another control.  
                Properties: create, edit, multiuse
        attachForm (Multiuse[Tuple[str, str, int]]?): Arguments are: control, edge, offset.  
                Valid edge values are: "top" | "bottom" | "left" | "right".  
                Attach the specified control to the form, offset by the specified  
                amount.  
                Properties: create, edit, multiuse
        attachNone (Multiuse[Tuple[str, str]]?): Arguments are: control, edge  
                Valid edge values are: "top" | "bottom" | "left" | "right".  
                Attach a control to nothing.  
                Properties: create, edit, multiuse
        attachOppositeControl (Multiuse[Tuple[str, str, int, str]]?): Arguments are: control, edge, offset, control  
                Valid edge values are: "top" | "bottom" | "left" | "right".  
                Attach a control to the opposite side of another control.  
                Properties: create, edit, multiuse
        attachOppositeForm (Multiuse[Tuple[str, str, int]]?): Arguments are: control, edge, offset.  
                Valid edge values are: "top" | "bottom" | "left" | "right".  
                Attach a control to the opposite side of the form.  
                Properties: create, edit, multiuse
        attachPosition (Multiuse[Tuple[str, str, int, int]]?): Arguments are: control, edge, offset, position  
                Valid edge values are: "top" | "bottom" | "left" | "right".  
                Attach a control to a position in the form.  
                Properties: create, edit, multiuse
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
        numberOfDivisions (Queryable[int]?): Specify the number of horizontal and vertical divisions  
                across the form. Value must be greater than 0.  
                Properties: create, query, edit
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
        str: The full name of the control.

    Example:
    """

