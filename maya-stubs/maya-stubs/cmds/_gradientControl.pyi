from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def gradientControl(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., adaptiveScaling: bool = ..., annotation: Queryable[str] = ..., attribute: str = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., clearAttribute: bool = ..., defineTemplate: str = ..., displayKeyInfo: bool = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., highlightMode: Queryable[str] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfControls: Queryable[int] = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., readOnly: bool = ..., refreshOnRelease: Queryable[int] = ..., selectedColorControl: str = ..., selectedInterpControl: str = ..., selectedPositionControl: str = ..., staticNumberOfControls: bool = ..., staticPositions: bool = ..., statusBarMessage: str = ..., upperLimitControl: Queryable[str] = ..., useTemplate: str = ..., verticalLayout: bool = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Callable[..., Any]]:
    """This command creates a control that displays
    the gradient attribute specified. The gradient attribute must be
    of the correct form and naming. It should be a multi attribute
    with each entry a compound composed of:Currently the routines to get the value of a ramp structure
    (with interpolation) are not available through MEL, which limits
    the use of this control by end users. The MEL command AEaddRampControl
    should be used to attach this control to an attribute from attribute
    editor templates.
    Args:
        adaptiveScaling (bool?): Allow the ramp widget display to scale vertically to  
                accommodate values greater than 1.0. True if adaptive scaling is  
                enabled, false (the default) if not.  
                Properties: create, query, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        attribute (str?): Specifies the name of the gradient attribute to control.  
                Properties: create, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        clearAttribute (bool?): Removes the gradient attribute that controls the widget.  
                A new attribute can be set again using the attribute flag  
                Properties: edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displayKeyInfo (bool?): Specifies if key position should be displayed in a tooltip when the user  
                hovers over or drags a control point.  
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
        highlightMode (Queryable[str]?): Specifies when the ramp should be highlighted. Only applies to curves.  
                Possible values are "off", "hover" and "always". Default is "off".  
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
        numberOfControls (Queryable[int]?): Returns the number of controls in the ramp widget  
                Properties: query
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
        readOnly (bool?): Specifies if the ramp is read only or not. If true, the ramp  
                can't be edited and control points will be hidden.  
                Properties: create, query, edit
        refreshOnRelease (Queryable[int]?): Define how updates are dispatched during interactive  
                editing of the ramp widget. True causes updates to only dispatch  
                after releasing the mouse button after editing. False (the default)  
                causes updates to dispatch interactively during editing (e.g. while  
                moving ramp curve points). Note that the global update mode, if  
                set to "on release" can disable the effect of this option.  
                Properties: create, query, edit
        selectedColorControl (str?): Specifies the name of a color control to edit the selected color.  
                Properties: create, edit
        selectedInterpControl (str?): Specifies the name of an enum control to edit the selected  
                interpolation.  
                Properties: create, edit
        selectedPositionControl (str?): Specifies the name of a float slider to edit the selected  
                position.  
                Properties: create, edit
        staticNumberOfControls (bool?): When 'true', this flag disables the creation/deletion of  
                ramp entries (control points) via ramp widget interaction. Default  
                is false.  
                Properties: create, query, edit
        staticPositions (bool?): When 'true', this flag disables the interactive modification  
                of ramp entry positions. Default is false.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        upperLimitControl (Queryable[str]?): Specify the name of a text control which is updated with the  
                current upper display limit for the ramp. This option is only  
                effective when adaptiveScaling is specified.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        verticalLayout (bool?): When 'true', this makes the control orient vertically rather than  
                horizontally. The default is `false` or horizontal.  
                Properties: create, query, edit
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

