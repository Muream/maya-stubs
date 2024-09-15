from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def floatSlider2(*args: Any, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand1: str = ..., changeCommand2: str = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., manage: bool = ..., maximum: Queryable[float] = ..., minimum: Queryable[float] = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., polarity: Queryable[int] = ..., popupMenuArray: bool = ..., positionControl1: str = ..., positionControl2: str = ..., preventOverride: bool = ..., statusBarMessage: str = ..., useTemplate: str = ..., value1: Queryable[float] = ..., value2: Queryable[float] = ..., values: Tuple[float, float] = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, int, float, Callable[..., Any]]:
    """This command creates a float slider containing two handles.
    The two handles are arranged such that they cannot pass one
    another, thus handle 1 will always have a value less than
    or or equal to handle 2 when you adjust the values.
    Each handle may have a MEL command associated with it which is
    issued when the handle moves and thus can be used to update the
    values of plugs such as via a setAttr command. Each handle can
    also be associated with a float textfield to display the current
    value of the handle.Note: the floatSlider2 widget currently only supports vertical
    (columnLayout) orientation.
    Args:
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        changeCommand1 (str?): Command to be associated with handle 1 and issued  
                whenever the value of the handle is changed (except when values  
                are changed via the -hv/handleValue flag). An example command might be  
                "setAttr nurbsSphere1.tx" and if handle 1 were to move to  
                value 0.23 the slider would issue the command  
                "setAttr nurbsSphere1.tx 0.23;".  
                Properties: create, edit
        changeCommand2 (str?): Command to be associated with handle 2 and issued  
                whenever the value of the handle is changed (except when values  
                are changed via the -hv/handleValue flag). An example command might be  
                "setAttr nurbsSphere1.tx" and if handle 2 were to move to  
                value 0.23 the slider would issue the command  
                "setAttr nurbsSphere1.tx 0.23;".  
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
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        maximum (Queryable[float]?): Maximum limit of the slider. The default value is 10.0.  
                The maximum value occurs at the top(right) end of the slider  
                unless -polarity was specified. Note: you cannot set the  
                maximum value greater than or equal to the current minimum.  
                Properties: create, query, edit
        minimum (Queryable[float]?): Minimum limit of the slider. The default value is 0.0.  
                The minimum value occurs at the bottom end of the slider  
                unless -polarity was specified. Note: you cannot set the  
                minimum value greater than or equal to the current maximum.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        polarity (Queryable[int]?): Specifies the polarity of the slider. If 0 (the default), the minimum  
                value (specified by the -minimum flag) occurs at the bottom end of  
                the slider and maximum at the top(right), with values increasing as the slider  
                handles are moved towards the upper end of the slider. If the polarity  
                is specified as 1, the reverse behaviour occurs, with the maximum  
                occurring at the bottom end, the mimimum occuring at the top(right) end  
                and values decreasing as the handles are moved towards the upper end.  
                Properties: create, query, edit
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        positionControl1 (str?): Set the name of the control (if any) which is associated with  
                handle 1 of this slider. The control must be a "floatField". The  
                control always displays the value of the handle, and is updated as  
                the handle moves.  
                Properties: create, edit
        positionControl2 (str?): Set the name of the control (if any) which is associated with  
                handle 2 of this slider. The control must be a "floatField". The  
                control always displays the value of the handle, and is updated as  
                the handle moves.  
                Properties: create, edit
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        value1 (Queryable[float]?): Value of handle 1. To ensure that handle 1 stays at  
                or below handle 2, an error will occur if the value specified  
                is too large. If you wish to set both handles simultaneously,  
                use the -values flag.  
                Properties: create, query, edit
        value2 (Queryable[float]?): Value of handle 2. To ensure that handle 2 stays at  
                or above handle 2, an error will occur if the value specified  
                is too large. If you wish to set both handles simultaneously,  
                use the -values flag.  
                Properties: create, query, edit
        values (Tuple[float, float]?): Sets the value for handles 1 and 2 simulteneously. The  
                first argument is applied to handle 1 and must be less than  
                or equal to the second (handle 2) argument or an error will  
                be issued.  
                Properties: create, edit
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
        str: The name of the port created or modified

    Example:
    """

