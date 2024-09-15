from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def rowLayout(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., adjustableColumn: Multiuse[int] = ..., adjustableColumn1: int = ..., adjustableColumn2: int = ..., adjustableColumn3: int = ..., adjustableColumn4: int = ..., adjustableColumn5: int = ..., adjustableColumn6: int = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., childArray: bool = ..., columnAlign: Multiuse[Tuple[int, str]] = ..., columnAlign1: str = ..., columnAlign2: Tuple[str, str] = ..., columnAlign3: Tuple[str, str, str] = ..., columnAlign4: Tuple[str, str, str, str] = ..., columnAlign5: Tuple[str, str, str, str, str] = ..., columnAlign6: Tuple[str, str, str, str, str, str] = ..., columnAttach: Multiuse[Tuple[int, str, int]] = ..., columnAttach1: str = ..., columnAttach2: Tuple[str, str] = ..., columnAttach3: Tuple[str, str, str] = ..., columnAttach4: Tuple[str, str, str, str] = ..., columnAttach5: Tuple[str, str, str, str, str] = ..., columnAttach6: Tuple[str, str, str, str, str, str] = ..., columnOffset1: int = ..., columnOffset2: Tuple[int, int] = ..., columnOffset3: Tuple[int, int, int] = ..., columnOffset4: Tuple[int, int, int, int] = ..., columnOffset5: Tuple[int, int, int, int, int] = ..., columnOffset6: Tuple[int, int, int, int, int, int] = ..., columnWidth: Multiuse[Tuple[int, int]] = ..., columnWidth1: int = ..., columnWidth2: Tuple[int, int] = ..., columnWidth3: Tuple[int, int, int] = ..., columnWidth4: Tuple[int, int, int, int] = ..., columnWidth5: Tuple[int, int, int, int, int] = ..., columnWidth6: Tuple[int, int, int, int, int, int] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., generalSpacing: int = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., manage: bool = ..., margins: int = ..., noBackground: bool = ..., numberOfChildren: bool = ..., numberOfColumns: Queryable[int] = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., rowAttach: Multiuse[Tuple[int, str, int]] = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, int, Callable[..., Any]]:
    """This command creates a layout capable of positioning children into
    a single horizontal row.
    Args:
        adjustableColumn (Multiuse[int]?): Specifies which column has an adjustable size that changes  
                with the sizing of the layout.  
                Properties: create, edit, multiuse
        adjustableColumn1 (int?): Specifies that the first column has an adjustable size that  
                changes with the size of the parent layout.  
                Ignored if there isn't exactly one column.  
                Properties: create
        adjustableColumn2 (int?): Specifies which of the two columns has an adjustable size  
                that changes with the size of the parent layout.  
                Ignored if there isn't exactly two columns.  
                Properties: create
        adjustableColumn3 (int?): Specifies which of the three columns has an adjustable size  
                that changes with the size of the parent layout.  
                Ignored if there isn't exactly three columns.  
                Properties: create
        adjustableColumn4 (int?): Specifies which of the four columns has an adjustable size  
                that changes with the size of the parent layout.  
                Ignored if there isn't exactly four columns.  
                Properties: create
        adjustableColumn5 (int?): Specifies which of the five columns has an adjustable size  
                that changes with the size of the parent layout.  
                Ignored if there isn't exactly five columns.  
                Properties: create
        adjustableColumn6 (int?): Specifies which of the six columns has an adjustable size  
                that changes with the size of the parent layout.  
                Ignored if there isn't exactly six columns.  
                Properties: create
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
        columnAlign (Multiuse[Tuple[int, str]]?): Text alignment for the specified column.  
                Valid values are "left", "right", and "center"  
                Properties: create, edit, multiuse
        columnAlign1 (str?): Text alignment for the first column.  
                Valid values are "left", "right", and "center".  
                Ignored if there isn't exactly one column.  
                Properties: create
        columnAlign2 (Tuple[str, str]?): Text alignment for both columns.  
                Valid values are "left", "right", and "center".  
                Ignored if there isn't exactly two columns.  
                Properties: create
        columnAlign3 (Tuple[str, str, str]?): Text alignment for all three columns.  
                Valid values are "left", "right", and "center".  
                Ignored if there isn't exactly three columns.  
                Properties: create
        columnAlign4 (Tuple[str, str, str, str]?): Text alignment for all four columns.  
                Valid values are "left", "right", and "center".  
                Ignored if there isn't exactly four columns.  
                Properties: create
        columnAlign5 (Tuple[str, str, str, str, str]?): Text alignment for all five columns.  
                Valid values are "left", "right", and "center".  
                Ignored if there isn't exactly five columns.  
                Properties: create
        columnAlign6 (Tuple[str, str, str, str, str, str]?): Text alignment for all six columns.  
                Valid values are "left", "right", and "center".  
                Ignored if there isn't exactly six columns.  
                Properties: create
        columnAttach (Multiuse[Tuple[int, str, int]]?): Horizontally attach a particular column.  The first  
                argument is a 1. based index specifying the column.  The second  
                argument is the attachment, valid values are "left", "right",  
                and "both".  The third argument is the offset value.  
                Properties: create, edit, multiuse
        columnAttach1 (str?): Attachment type for the first column.  Ignored if there isn't  
                exactly one column. Valid values are "left", "right", and "both".  
                Properties: create
        columnAttach2 (Tuple[str, str]?): Attachment type for both columns.  Ignored if there isn't  
                exactly two columns. Valid values are "left", "right", and "both".  
                Properties: create
        columnAttach3 (Tuple[str, str, str]?): Attachment type for all three columns.  Ignored if there  
                isn't exactly three columns. Valid values are "left", "right",  
                and "both".  
                Properties: create
        columnAttach4 (Tuple[str, str, str, str]?): Attachment type for all four columns.  Ignored if there isn't  
                exactly four columns. Valid values are "left", "right", and "both".  
                Properties: create
        columnAttach5 (Tuple[str, str, str, str, str]?): Attachment type for all five columns.  Ignored if there isn't  
                exactly five columns. Valid values are "left", "right", and "both".  
                Properties: create
        columnAttach6 (Tuple[str, str, str, str, str, str]?): Attachment type for all six columns.  Ignored if there isn't  
                exactly six columns. Valid values are "left", "right", and "both".  
                Properties: create
        columnOffset1 (int?): Used in conjunction with the -columnAttach1 flag.  If that  
                flag is not used then this flag will be ignored.  Sets the offset  
                for the first column.  The offsets applied are based on the  
                attachments specified with the -columnAttach1 flag.  
                Ignored if there isn't exactly one column.  
                Properties: create
        columnOffset2 (Tuple[int, int]?): Used in conjunction with the -columnAttach2 flag.  If that  
                flag is not used then this flag will be ignored.  Sets the offset  
                for both columns.  The offsets applied are based on the  
                attachments specified with the -columnAttach2 flag.  
                Ignored if there isn't exactly two columns.  
                Properties: create
        columnOffset3 (Tuple[int, int, int]?): Used in conjunction with the -columnAttach3 flag.  If that  
                flag is not used then this flag will be ignored.  Sets the offset  
                for all three columns.  The offsets applied are based on the  
                attachments specified with the -columnAttach3 flag.  
                Ignored if there isn't exactly three columns.  
                Properties: create
        columnOffset4 (Tuple[int, int, int, int]?): Used in conjunction with the -columnAttach4 flag.  If that  
                flag is not used then this flag will be ignored.  Sets the offset  
                for all four columns.  The offsets applied are based on the  
                attachments specified with the -columnAttach4 flag.  
                Ignored if there isn't exactly four columns.  
                Properties: create
        columnOffset5 (Tuple[int, int, int, int, int]?): Used in conjunction with the -columnAttach5 flag.  If that  
                flag is not used then this flag will be ignored.  Sets the offset  
                for all five columns.  The offsets applied are based on the  
                attachments specified with the -columnAttach5 flag.  
                Ignored if there isn't exactly five columns.  
                Properties: create
        columnOffset6 (Tuple[int, int, int, int, int, int]?): Used in conjunction with the -columnAttach6 flag.  If that  
                flag is not used then this flag will be ignored.  Sets the offset  
                for all six columns.  The offsets applied are based on the  
                attachments specified with the -columnAttach6 flag.  
                Ignored if there isn't exactly six columns.  
                Properties: create
        columnWidth (Multiuse[Tuple[int, int]]?): Width of a particular column.  The first argument is a  
                1. based index specifying the column.  The second argument is the  
                width value.  
                Properties: create, edit, multiuse
        columnWidth1 (int?): Width for the first column.  Ignored if there isn't exactly  
                one column.  
                Properties: create
        columnWidth2 (Tuple[int, int]?): Widths for both columns.  Ignored if there isn't  
                exactly two columns.  
                Properties: create
        columnWidth3 (Tuple[int, int, int]?): Widths for all three columns.  Ignored if there isn't  
                exactly three columns.  
                Properties: create
        columnWidth4 (Tuple[int, int, int, int]?): Widths for all four columns.  Ignored if there isn't  
                exactly four columns.  
                Properties: create
        columnWidth5 (Tuple[int, int, int, int, int]?): Widths for all five columns.  Ignored if there isn't  
                exactly five columns.  
                Properties: create
        columnWidth6 (Tuple[int, int, int, int, int, int]?): Widths for all six columns.  Ignored if there isn't  
                exactly six columns.  
                Properties: create
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
        numberOfColumns (Queryable[int]?): Number of columns in the row.  The specified number of  
                columns must be a value greater than 0.  
                Properties: create, query
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
        rowAttach (Multiuse[Tuple[int, str, int]]?): Vertically attach a particular column.  The first argument  
                is a 1. based index specifying the column.  The second argument is  
                the attachment, valid values are "top", "bottom", and "both".  The  
                third argument is the offset value.  
                Properties: create, edit, multiuse
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

