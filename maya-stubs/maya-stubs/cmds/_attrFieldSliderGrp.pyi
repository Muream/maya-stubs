from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def attrFieldSliderGrp(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., adjustableColumn: int = ..., adjustableColumn2: int = ..., adjustableColumn3: int = ..., adjustableColumn4: int = ..., adjustableColumn5: int = ..., adjustableColumn6: int = ..., annotation: Queryable[str] = ..., attribute: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand: Callable[..., Any] = ..., columnAlign: Multiuse[Tuple[int, str]] = ..., columnAlign2: Tuple[str, str] = ..., columnAlign3: Tuple[str, str, str] = ..., columnAlign4: Tuple[str, str, str, str] = ..., columnAlign5: Tuple[str, str, str, str, str] = ..., columnAlign6: Tuple[str, str, str, str, str, str] = ..., columnAttach: Multiuse[Tuple[int, str, int]] = ..., columnAttach2: Tuple[str, str] = ..., columnAttach3: Tuple[str, str, str] = ..., columnAttach4: Tuple[str, str, str, str] = ..., columnAttach5: Tuple[str, str, str, str, str] = ..., columnAttach6: Tuple[str, str, str, str, str, str] = ..., columnOffset2: Tuple[int, int] = ..., columnOffset3: Tuple[int, int, int] = ..., columnOffset4: Tuple[int, int, int, int] = ..., columnOffset5: Tuple[int, int, int, int, int] = ..., columnOffset6: Tuple[int, int, int, int, int, int] = ..., columnWidth: Multiuse[Tuple[int, int]] = ..., columnWidth1: int = ..., columnWidth2: Tuple[int, int] = ..., columnWidth3: Tuple[int, int, int] = ..., columnWidth4: Tuple[int, int, int, int] = ..., columnWidth5: Tuple[int, int, int, int, int] = ..., columnWidth6: Tuple[int, int, int, int, int, int] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., extraButton: bool = ..., extraButtonCommand: Callable[..., Any] = ..., extraButtonIcon: Queryable[str] = ..., fieldMaxValue: Queryable[float] = ..., fieldMinValue: Queryable[float] = ..., fieldStep: Queryable[float] = ..., forceAddMapButton: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., hideMapButton: bool = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., label: Queryable[str] = ..., manage: bool = ..., maxValue: Queryable[float] = ..., minValue: Queryable[float] = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., precision: int = ..., preventOverride: bool = ..., rowAttach: Multiuse[Tuple[int, str, int]] = ..., sliderMaxValue: Queryable[float] = ..., sliderMinValue: Queryable[float] = ..., sliderStep: Queryable[float] = ..., statusBarMessage: str = ..., step: Queryable[float] = ..., useTemplate: str = ..., vertical: bool = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, float, int, Callable[..., Any]]:
    """All of the group commands position their individual controls in columns
    starting at column 1.  The layout of each control (ie. column) can be
    customized using the, andflags.  By default, columns are left aligned
    with no offset and are 100 pixels wide.  Only one column in any group can
    be adjustable.This command creates a pre-packaged collection of label text, float
    field and float slider (for values with a min or max specified)
    The group
    also supports the notion of a larger secondary range of possible
    field values.If an attribute is specified for this object, then it will use any
    min and max values defined in the attribute.  The user-specified
    values can reduce the min and max, but cannot expand them.The field created here
    is an expression field -- while normally operating
    as a float field, the user can type in any expression starting with
    the character "=".  This will expand the field to occupy the space
    previously taken by the slider.The field also has
    an automatic menu brought up by the right mouse button.
    The contents of this menu change depending on the state of
    the attribute being watched by the field.
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
        attribute (Queryable[str]?): The name of a unique attribute of type double or int.  
                This newly created field will be attached to the attribute, so  
                that modifications to one will change the other.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        changeCommand (Callable[..., Any]?): The command string is executed when the value of the slider  
                or floatField changes.  It will be executed only once after a  
                drag of the slider.  
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
        extraButton (bool?): Add an extra icon button to the end of this control.  
                Properties: create
        extraButtonCommand (Callable[..., Any]?): The command string is executed when the extra button is clicked.  
                Properties: create, edit
        extraButtonIcon (Queryable[str]?): The icon file name of the extra button.  
                Properties: create, query, edit
        fieldMaxValue (Queryable[float]?): Set the maximum value for the field.  This flag allows you  
                to specify a maximum bound for the field higher than that  
                of the slider.   (See note above  
                about max and min values.)  
                Properties: create, query, edit
        fieldMinValue (Queryable[float]?): Set the minimum value for the field.  This flag allows you  
                to specify a minimum bound for the field lower than that of  
                the slider.  (See note above  
                about max and min values.)  
                Properties: create, query, edit
        fieldStep (Queryable[float]?): Sets the increment for the float field.  
                Properties: create, query, edit
        forceAddMapButton (bool?): Force adding a map button to this control. If this option is true,  
                option hideMapButton is suppressed.  
                Properties: create
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        hideMapButton (bool?): Force the map button to remain hidden for this control.  
                Properties: create
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
        label (Queryable[str]?): By default, the label of this field will be the name of the  
                attribute.  This flag can be used to override that name with  
                whatever string you want.  
                Properties: create, query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        maxValue (Queryable[float]?): Sets the maximum value for both the slider and the field.  
                (See note above about min and max values)  
                Properties: create, query, edit
        minValue (Queryable[float]?): Sets the minimum value for both the slider and the field.  
                (by default max and min are set according to what is in the  
                attribute, if anything.  If no max and min are specified,  
                or if only one of the two are specified, then no slider  
                is created.)  
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
        precision (int?): Sets the number of digits to the right of the decimal.  
                (If attached to an int attribute, this is automatically  
                set to 0 and cannot be overridden.)  
                Properties: create, edit
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        rowAttach (Multiuse[Tuple[int, str, int]]?): Arguments are : column, attachment type, offset.  
                Possible attachments are: top | bottom | both.  
                Specifies attachment types and offsets for the entire row.  
                Properties: create, edit, multiuse
        sliderMaxValue (Queryable[float]?): Set the maximum value for the slider.  The slider  
                max will be clipped to the field max.  
                Properties: create, query, edit
        sliderMinValue (Queryable[float]?): Set the minimum value for the slider.  The slider min  
                will be clipped to the field min.  
                Properties: create, query, edit
        sliderStep (Queryable[float]?): On Linux the slider step value represents the  
                amount the value will increase or decrease when  
                you click either side of the slider.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        step (Queryable[float]?): Sets the increment for both the slider and float field.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        vertical (bool?): Whether the orientation of the controls in this group  
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

