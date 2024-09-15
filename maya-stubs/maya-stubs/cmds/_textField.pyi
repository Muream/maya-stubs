from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def textField(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., alwaysInvokeEnterCommandOnReturn: bool = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand: Callable[..., Any] = ..., defineTemplate: str = ..., disableButtons: bool = ..., disableClearButton: bool = ..., disableHistoryButton: bool = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., drawInactiveFrame: bool = ..., dropCallback: Callable[..., Any] = ..., editable: bool = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., enterCommand: Callable[..., Any] = ..., exists: bool = ..., fileName: Queryable[str] = ..., font: Queryable[str] = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., insertText: str = ..., insertionPosition: Queryable[int] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., placeholderText: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., receiveFocusCommand: Callable[..., Any] = ..., searchField: bool = ..., statusBarMessage: str = ..., text: Queryable[str] = ..., textChangedCommand: Callable[..., Any] = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Callable[..., Any]]:
    """Create a text field control.
    Args:
        alwaysInvokeEnterCommandOnReturn (bool?): Sets whether to always invoke the enter command when the return key is  
                pressed by the user.  
                By default, this option is false.  
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
        changeCommand (Callable[..., Any]?): Command executed when the text changes.  This command is  
                not invoked when the value changes via the -tx/text flag.  
                Properties: create, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        disableButtons (bool?): Sets the visibility state of search field buttons to true/false depending on the passed value.  
                In Query mode returns whether both buttons are visible or not.  
                Properties: create, query, edit
        disableClearButton (bool?): Sets the visibility state of search field clear button to true/false depending on the passed value.  
                In Query mode returns whether clear button of search field is visible or not.  
                Properties: create, query, edit
        disableHistoryButton (bool?): Sets the visibility state of search field history button to true/false depending on the passed value.  
                In Query mode returns whether history button of search field is visible or not.  
                Properties: create, query, edit
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
        drawInactiveFrame (bool?): Sets whether the text field draws itself with a frame when it's inactive.  
                By default, this option is false.  
                Properties: create, query, edit
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
        editable (bool?): The edit state of the field.  By default, this flag is  
                set to true and the field value may be changed by typing into it.  
                If false then the field is 'read only' and can not be typed into.  
                The text in the field can always be changed with the -tx/text flag  
                regardless of the state of the -ed/editable flag.  
                Properties: create, query, edit
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
        enterCommand (Callable[..., Any]?): Command executed when the keypad 'Enter' key is pressed.  
                Properties: create, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fileName (Queryable[str]?): Text in the field as a filename. This does conversions between  
                internal and external (UI) file representation.  
                Properties: create, query, edit
        font (Queryable[str]?): The font for the text.  Valid values are  
                "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",  
                "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",  
                "smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".  
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
        insertText (str?): Insert text into the field at the current insertion  
                position (specified by the -ip/insertionPosition flag).  
                Properties: create, edit
        insertionPosition (Queryable[int]?): The insertion position for inserted text.  This is a  
                1 based value where position 1 specifies the beginning of the  
                field.  Position 0 may be used to specify the end of the field.  
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
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        placeholderText (Queryable[str]?): Setting this property makes the line edit display a grayed-out placeholder text as long as the text field is empty and the widget doesn't have focus.  
                By default, this property contains an empty string.  
                Properties: create, query, edit
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        receiveFocusCommand (Callable[..., Any]?): Command executed when the field receives focus.  
                Properties: create, edit
        searchField (bool?): Creates a search field instead of a text field.  
                Properties: create
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        text (Queryable[str]?): The field text.  
                Properties: create, query, edit
        textChangedCommand (Callable[..., Any]?): Command executed immediately when the field text changes.  
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

