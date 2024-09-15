from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def radioButtonGrp(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., adjustableColumn: int = ..., adjustableColumn2: int = ..., adjustableColumn3: int = ..., adjustableColumn4: int = ..., adjustableColumn5: int = ..., adjustableColumn6: int = ..., annotation: Queryable[str] = ..., annotation1: Queryable[str] = ..., annotation2: Queryable[str] = ..., annotation3: Queryable[str] = ..., annotation4: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand: Callable[..., Any] = ..., changeCommand1: Callable[..., Any] = ..., changeCommand2: Callable[..., Any] = ..., changeCommand3: Callable[..., Any] = ..., changeCommand4: Callable[..., Any] = ..., columnAlign: Multiuse[Tuple[int, str]] = ..., columnAlign2: Tuple[str, str] = ..., columnAlign3: Tuple[str, str, str] = ..., columnAlign4: Tuple[str, str, str, str] = ..., columnAlign5: Tuple[str, str, str, str, str] = ..., columnAlign6: Tuple[str, str, str, str, str, str] = ..., columnAttach: Multiuse[Tuple[int, str, int]] = ..., columnAttach2: Tuple[str, str] = ..., columnAttach3: Tuple[str, str, str] = ..., columnAttach4: Tuple[str, str, str, str] = ..., columnAttach5: Tuple[str, str, str, str, str] = ..., columnAttach6: Tuple[str, str, str, str, str, str] = ..., columnOffset2: Tuple[int, int] = ..., columnOffset3: Tuple[int, int, int] = ..., columnOffset4: Tuple[int, int, int, int] = ..., columnOffset5: Tuple[int, int, int, int, int] = ..., columnOffset6: Tuple[int, int, int, int, int, int] = ..., columnWidth: Multiuse[Tuple[int, int]] = ..., columnWidth1: int = ..., columnWidth2: Tuple[int, int] = ..., columnWidth3: Tuple[int, int, int] = ..., columnWidth4: Tuple[int, int, int, int] = ..., columnWidth5: Tuple[int, int, int, int, int] = ..., columnWidth6: Tuple[int, int, int, int, int, int] = ..., data1: Queryable[int] = ..., data2: Queryable[int] = ..., data3: Queryable[int] = ..., data4: Queryable[int] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., editable: bool = ..., enable: bool = ..., enable1: bool = ..., enable2: bool = ..., enable3: bool = ..., enable4: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., label: Queryable[str] = ..., label1: Queryable[str] = ..., label2: Queryable[str] = ..., label3: Queryable[str] = ..., label4: Queryable[str] = ..., labelAnnotation: Queryable[str] = ..., labelArray2: Queryable[Tuple[str, str]] = ..., labelArray3: Queryable[Tuple[str, str, str]] = ..., labelArray4: Queryable[Tuple[str, str, str, str]] = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., numberOfRadioButtons: int = ..., offCommand: Callable[..., Any] = ..., offCommand1: Callable[..., Any] = ..., offCommand2: Callable[..., Any] = ..., offCommand3: Callable[..., Any] = ..., offCommand4: Callable[..., Any] = ..., onCommand: Callable[..., Any] = ..., onCommand1: Callable[..., Any] = ..., onCommand2: Callable[..., Any] = ..., onCommand3: Callable[..., Any] = ..., onCommand4: Callable[..., Any] = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., rowAttach: Multiuse[Tuple[int, str, int]] = ..., select: Queryable[int] = ..., shareCollection: str = ..., statusBarMessage: str = ..., useTemplate: str = ..., vertical: bool = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], int, bool, Tuple[str, str], Tuple[str, str, str], Tuple[str, str, str, str], Callable[..., Any]]:
    """All of the group commands position their individual controls in columns
    starting at column 1.  The layout of each control (ie. column) can be
    customized using the, andflags.  By default, columns are left aligned
    with no offset and are 100 pixels wide.  Only one column in any group can
    be adjustable.This command creates from one to four radio buttons in a single row.
    By default the radio buttons will share a single collection, but they
    can also share the collection of another radio button group.  The buttons
    can also have an optional text label.
    Args:
        adjustableColumn (int?): Specifies which column has an adjustable size that changes with the  
                sizing of the layout.  The column value is a 1. based index.  
                Passing 0 as argument turns off the previous adjustable column.  
                Properties: create, edit
        adjustableColumn2 (int?): Specifies which column has an adjustable size that changes with  
                the size of the parent layout. Ignored if there are not exactly  
                two columns.  
                Properties: create, edit
        adjustableColumn3 (int?): Specifies that the column has an adjustable size that changes with  
                the size of the parent layout. Ignored if there are not exactly  
                three columns.  
                Properties: create, edit
        adjustableColumn4 (int?): Specifies which column has an adjustable size that changes with  
                the size of the parent layout. Ignored if there are not exactly  
                four columns.  
                Properties: create, edit
        adjustableColumn5 (int?): Specifies which column has an adjustable size that changes with  
                the size of the parent layout. Ignored if there are not exactly  
                five columns.  
                Properties: create, edit
        adjustableColumn6 (int?): Specifies which column has an adjustable size that changes with  
                the size of the parent layout. Ignored if there are not exactly  
                six columns.  
                Properties: create, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        annotation1 (Queryable[str]?): specifies the tooptip of the first radiobutton  
                Properties: create, query, edit
        annotation2 (Queryable[str]?): specifies the tooptip of the second radiobutton  
                Properties: create, query, edit
        annotation3 (Queryable[str]?): specifies the tooptip of the third radiobutton  
                Properties: create, query, edit
        annotation4 (Queryable[str]?): specifies the tooptip of the fourth radiobutton  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        changeCommand (Callable[..., Any]?): Command executed when the group changes state.  
                Note that this flag should not be used in conjunction with  
                onCommand and offCommand. That is, one should either use  
                changeCommand and test the state of a radio button from inside  
                the callback, or use onCommand and offCommand as separate  
                callbacks.  
                Properties: create, edit
        changeCommand1 (Callable[..., Any]?):   
                Properties: create, edit
        changeCommand2 (Callable[..., Any]?):   
                Properties: create, edit
        changeCommand3 (Callable[..., Any]?):   
                Properties: create, edit
        changeCommand4 (Callable[..., Any]?): Specify a changed state command for each respective radio  
                button.  
                Properties: create, edit
        columnAlign (Multiuse[Tuple[int, str]]?): Arguments are : column number, alignment type.  
                Possible alignments are: left | right | center.  
                Specifies alignment type for the specified column.  
                Properties: create, edit, multiuse
        columnAlign2 (Tuple[str, str]?): Sets the text alignment of both columns.  Ignored if there are not  
                exactly two columns. Valid values are "left", "right", and "center".  
                Properties: create, edit
        columnAlign3 (Tuple[str, str, str]?): Sets the text alignment for all three columns.  Ignored if there are not  
                exactly three columns. Valid values are "left", "right", and "center".  
                Properties: create, edit
        columnAlign4 (Tuple[str, str, str, str]?): Sets the text alignment for all four columns.  Ignored if there are not  
                exactly four columns. Valid values are "left", "right", and "center".  
                Properties: create, edit
        columnAlign5 (Tuple[str, str, str, str, str]?): Sets the text alignment for all five columns.  Ignored if there are not  
                exactly five columns. Valid values are "left", "right", and "center".  
                Properties: create, edit
        columnAlign6 (Tuple[str, str, str, str, str, str]?): Sets the text alignment for all six columns.  Ignored if there are not  
                exactly six columns. Valid values are "left", "right", and "center".  
                Properties: create, edit
        columnAttach (Multiuse[Tuple[int, str, int]]?): Arguments are : column number, attachment type, and offset.  
                Possible attachments are: left | right | both.  
                Specifies column attachment types and offets.  
                Properties: create, edit, multiuse
        columnAttach2 (Tuple[str, str]?): Sets the attachment type of both columns. Ignored if there are not  
                exactly two columns. Valid values are "left", "right", and "both".  
                Properties: create, edit
        columnAttach3 (Tuple[str, str, str]?): Sets the attachment type for all three columns. Ignored if there are not  
                exactly three columns. Valid values are "left", "right", and "both".  
                Properties: create, edit
        columnAttach4 (Tuple[str, str, str, str]?): Sets the attachment type for all four columns. Ignored if there are not  
                exactly four columns. Valid values are "left", "right", and "both".  
                Properties: create, edit
        columnAttach5 (Tuple[str, str, str, str, str]?): Sets the attachment type for all five columns. Ignored if there are not  
                exactly five columns. Valid values are "left", "right", and "both".  
                Properties: create, edit
        columnAttach6 (Tuple[str, str, str, str, str, str]?): Sets the attachment type for all six columns. Ignored if there are not  
                exactly six columns. Valid values are "left", "right", and "both".  
                Properties: create, edit
        columnOffset2 (Tuple[int, int]?): This flag is used in conjunction with the -columnAttach2 flag.  If that  
                flag is not used then this flag will be ignored.  It sets the offset for  
                the two columns.  The offsets applied are based on the attachments  
                specified with the -columnAttach2 flag.  Ignored if there are not exactly  
                two columns.  
                Properties: create, edit
        columnOffset3 (Tuple[int, int, int]?): This flag is used in conjunction with the -columnAttach3 flag.  If that  
                flag is not used then this flag will be ignored.  It sets the offset for  
                the three columns.  The offsets applied are based on the attachments  
                specified with the -columnAttach3 flag.  Ignored if there are not exactly  
                three columns.  
                Properties: create, edit
        columnOffset4 (Tuple[int, int, int, int]?): This flag is used in conjunction with the -columnAttach4 flag.  If that  
                flag is not used then this flag will be ignored.  It sets the offset for  
                the four columns.  The offsets applied are based on the attachments  
                specified with the -columnAttach4 flag.  Ignored if there are not exactly  
                four columns.  
                Properties: create, edit
        columnOffset5 (Tuple[int, int, int, int, int]?): This flag is used in conjunction with the -columnAttach5 flag.  If that  
                flag is not used then this flag will be ignored.  It sets the offset for  
                the five columns.  The offsets applied are based on the attachments  
                specified with the -columnAttach5 flag.  Ignored if there are not exactly  
                five columns.  
                Properties: create, edit
        columnOffset6 (Tuple[int, int, int, int, int, int]?): This flag is used in conjunction with the -columnAttach6 flag.  If that  
                flag is not used then this flag will be ignored.  It sets the offset for  
                the six columns.  The offsets applied are based on the attachments  
                specified with the -columnAttach6 flag.  Ignored if there are not exactly  
                six columns.  
                Properties: create, edit
        columnWidth (Multiuse[Tuple[int, int]]?): Arguments are : column number, column width.  
                Sets the width of the specified column where the first parameter specifies  
                the column (1 based index) and the second parameter specifies the width.  
                Properties: create, edit, multiuse
        columnWidth1 (int?): Sets the width of the first column. Ignored if there is not  
                exactly one column.  
                Properties: create, edit
        columnWidth2 (Tuple[int, int]?): Sets the column widths of both columns. Ignored if there are not  
                exactly two columns.  
                Properties: create, edit
        columnWidth3 (Tuple[int, int, int]?): Sets the column widths for all 3 columns. Ignored if there are not  
                exactly 3 columns.  
                Properties: create, edit
        columnWidth4 (Tuple[int, int, int, int]?): Sets the column widths for all 4 columns. Ignored if there are not  
                exactly 4 columns.  
                Properties: create, edit
        columnWidth5 (Tuple[int, int, int, int, int]?): Sets the column widths for all 5 columns. Ignored if there are not  
                exactly 5 columns.  
                Properties: create, edit
        columnWidth6 (Tuple[int, int, int, int, int, int]?): Sets the column widths for all 6 columns. Ignored if there are not  
                exactly 6 columns.  
                Properties: create, edit
        data1 (Queryable[int]?):   
                Properties: create, query, edit
        data2 (Queryable[int]?):   
                Properties: create, query, edit
        data3 (Queryable[int]?):   
                Properties: create, query, edit
        data4 (Queryable[int]?): Internal data associated with each radio button.  
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
        editable (bool?): The edit state of the group.  By default, this flag  
                is set to true and the radio button values may be changed by  
                clicking on them.  If false then the radio buttons are 'read only'  
                and can not be clicked on. The value of the radio button can  
                always be changed with the sl/select flags regardless of  
                the state of the ed/editable flag.  
                Properties: create, query, edit
        enable (bool?): The enable state of the control.  By default, this flag is  
                set to true and the control is enabled.  Specify false and the control  
                will appear dimmed or greyed-out indicating it is disabled.  
                Properties: create, query, edit
        enable1 (bool?):   
                Properties: create, query, edit
        enable2 (bool?):   
                Properties: create, query, edit
        enable3 (bool?):   
                Properties: create, query, edit
        enable4 (bool?): Enable state of the individual radio buttons.  
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
        label (Queryable[str]?): When present on creation an optional text label will be  
                built with the group.  The string specifies the label text.  
                Properties: create, query, edit
        label1 (Queryable[str]?):   
                Properties: create, query, edit
        label2 (Queryable[str]?):   
                Properties: create, query, edit
        label3 (Queryable[str]?):   
                Properties: create, query, edit
        label4 (Queryable[str]?): Specify label strings for the respective radio buttons in  
                the group.  
                Properties: create, query, edit
        labelAnnotation (Queryable[str]?): when present on creation an optional text label will be  
                built with the group . The string specifies the label tooltip  
                Properties: create, query, edit
        labelArray2 (Queryable[Tuple[str, str]]?):   
                Properties: create, query, edit
        labelArray3 (Queryable[Tuple[str, str, str]]?):   
                Properties: create, query, edit
        labelArray4 (Queryable[Tuple[str, str, str, str]]?): Specify multiple labels in a single flag.  These flags  
                are ignored if the number of radio buttons doesn't match.  
                Properties: create, query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        numberOfRadioButtons (int?): Number of radio buttons in the group (1. 4).  
                Properties: create
        offCommand (Callable[..., Any]?): Command executed when any radio button turns off.  
                Properties: create, edit
        offCommand1 (Callable[..., Any]?):   
                Properties: create, edit
        offCommand2 (Callable[..., Any]?):   
                Properties: create, edit
        offCommand3 (Callable[..., Any]?):   
                Properties: create, edit
        offCommand4 (Callable[..., Any]?): Off command for each respective radio button.  
                Properties: create, edit
        onCommand (Callable[..., Any]?): Command executed when any radio button turns on.  
                Properties: create, edit
        onCommand1 (Callable[..., Any]?):   
                Properties: create, edit
        onCommand2 (Callable[..., Any]?):   
                Properties: create, edit
        onCommand3 (Callable[..., Any]?):   
                Properties: create, edit
        onCommand4 (Callable[..., Any]?): On command for each respective radio button.  
                Properties: create, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        rowAttach (Multiuse[Tuple[int, str, int]]?): Arguments are : column, attachment type, offset.  
                Possible attachments are: top | bottom | both.  
                Specifies attachment types and offsets for the entire row.  
                Properties: create, edit, multiuse
        select (Queryable[int]?): Selected radio button.  The argument is a 1 based integer.  
                Properties: create, query, edit
        shareCollection (str?): Specify the radioButtonGrp that this radio group is to be  
                associated with.  By default the radio group will be a separate  
                collection.  
                Properties: create
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        vertical (bool?): Whether the orientation of the radio buttons in this group  
                are horizontal (default) or vertical.  
                Properties: create, query
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

