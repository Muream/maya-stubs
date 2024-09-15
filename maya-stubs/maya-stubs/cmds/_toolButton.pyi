from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def toolButton(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowMultipleTools: bool = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand: Callable[..., Any] = ..., collection: str = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., doubleClickCommand: Callable[..., Any] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., imageOverlayLabel: Queryable[str] = ..., isObscured: bool = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., offCommand: Callable[..., Any] = ..., onCommand: Callable[..., Any] = ..., parent: Queryable[str] = ..., popupIndicatorVisible: bool = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., select: bool = ..., statusBarMessage: str = ..., style: str = ..., tool: Queryable[Multiuse[str]] = ..., toolArray: bool = ..., toolCount: bool = ..., toolImage1: Queryable[Multiuse[Tuple[str, str]]] = ..., toolImage2: Queryable[Multiuse[Tuple[str, str]]] = ..., toolImage3: Queryable[Multiuse[Tuple[str, str]]] = ..., useTemplate: str = ..., version: Queryable[str] = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Multiuse[str], Multiuse[Tuple[str, str]], Callable[..., Any]]:
    """This command creates a toolButton that is added to the most recently
    created tool button collection unless theflag is
    used. It also attaches the named tool, activating it when this control
    is selected.By default, this control only handles one tool at a time.  Using
    theflag to associate a new tool will simply override the
    previous attached tool.  If you use theflag then you will be able to attach more than one tool with this
    control.  Only one tool will be current within the control.  To access
    the other tools press the right mouse button to display a popup menu
    containing all the tools associated with this control.  If you set
    theflag then a small arrow will be
    drawn on the control to indicate that additional tools are attached to
    this control.
    Args:
        allowMultipleTools (bool?): Indicates whether this control will allow you to attach more  
                than one tool.  By default, this control accepts only one tool.  
                You can add multiple tools by setting this flag to true.  
                Only one tool will be current and displayed at any one time.  
                Use the pop up menu attached to the right mouse button to view  
                all the tools.  
                Properties: create, query
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        changeCommand (Callable[..., Any]?): Command executed when the control's state is changed.  
                Note that this flag should not be used in conjunction with  
                onCommand and offCommand. That is, one should either use  
                changeCommand and test the state of the control from inside  
                the callback, or use onCommand and offCommand as separate  
                callbacks.  
                Properties: create, edit
        collection (str?): To explicitly add a tool button to a tool collection.  
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
        doubleClickCommand (Callable[..., Any]?): Command executed when the control is double clicked.  
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
        image1 (Queryable[str]?):   
                Properties: create, query, edit
        image2 (Queryable[str]?):   
                Properties: create, query, edit
        image3 (Queryable[str]?): This control supports three images.  The image that best fits the  
                current size of the control will be displayed.  This flag  
                applies the image to the current tool.  
                Properties: create, query, edit
        imageOverlayLabel (Queryable[str]?): A short string (5 characters) label that will be displayed  
                on top of the icon.  
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
        offCommand (Callable[..., Any]?): Command executed when the control is turned off.  
                Properties: create, edit
        onCommand (Callable[..., Any]?): Command executed when the control is turned on.  
                Properties: create, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupIndicatorVisible (bool?): Edit this flag to set the visibility of the popup tool indicator.  
                The indicator is a simple image that appears in the top right corner  
                of the button when more that one tool is associated with this control.  
                This flag is queryable and true by default.  
                Properties: create, query, edit
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        select (bool?): Will set this button as the selected one.  This flag also  
                queries the select state of the control.  
                Properties: create, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        style (str?): The draw style of the control.  Valid styles are "iconOnly",  
                "textOnly", "iconAndTextHorizontal" and "iconAndTextVertical".  
                Properties: create, edit
        tool (Queryable[Multiuse[str]]?): The name of the tool to be attached to the button.  If the  
                tool specified is already attached to this button then it will  
                be selected.  Query this flag to return the current tool.  This  
                flag may be specified more than once to attach more than one  
                tool.  
                Properties: create, query, edit, multiuse
        toolArray (bool?): This query only flag returns the names of all the tools attached  
                to the toolButton control.  
                Properties: query
        toolCount (bool?): This query only flag return the number of tools attached to the  
                toolButton control.  
                Properties: query
        toolImage1 (Queryable[Multiuse[Tuple[str, str]]]?):   
                Properties: create, query, edit, multiuse
        toolImage2 (Queryable[Multiuse[Tuple[str, str]]]?):   
                Properties: create, query, edit, multiuse
        toolImage3 (Queryable[Multiuse[Tuple[str, str]]]?): This control supports three images.  The image that best fits the  
                current size of the control will be displayed.  This flag  
                applies the image to the specified tool.  The first argument is the  
                name of the tool and the second is the name of the image.  When  
                queried an array of tool icon pairs is returned.  
                Properties: create, query, edit, multiuse
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        version (Queryable[str]?): Specify the version that this tool button feature was introduced.  
                The argument should be given as a string of the version number  
                (e.g. "2013", "2014"). Currently only accepts major version  
                numbers (e.g. 2013 Ext 1, or 2013.5 should be given as "2014").  
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
        str: The name of the toolButton created.

    Example:
    """

