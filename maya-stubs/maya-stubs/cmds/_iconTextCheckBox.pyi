from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def iconTextCheckBox(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., align: Queryable[str] = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., changeCommand: Queryable[Callable[..., Any]] = ..., defineTemplate: str = ..., disabledImage: Queryable[str] = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., flat: bool = ..., flipX: bool = ..., flipY: bool = ..., font: Queryable[str] = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., highlightImage: Queryable[str] = ..., image: Queryable[str] = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., imageOverlayLabel: Queryable[str] = ..., isObscured: bool = ..., label: Queryable[str] = ..., labelOffset: Queryable[int] = ..., manage: bool = ..., marginHeight: Queryable[int] = ..., marginWidth: Queryable[int] = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., offCommand: Queryable[Callable[..., Any]] = ..., onCommand: Queryable[Callable[..., Any]] = ..., overlayLabelBackColor: Queryable[Tuple[float, float, float, float]] = ..., overlayLabelColor: Queryable[Tuple[float, float, float]] = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., rotation: Queryable[float] = ..., selectionHighlightImage: Queryable[str] = ..., selectionImage: Queryable[str] = ..., statusBarMessage: str = ..., style: Queryable[str] = ..., useAlpha: bool = ..., useTemplate: str = ..., value: bool = ..., version: Queryable[str] = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], Callable[..., Any], bool, int, Tuple[float, float, float, float], float]:
    """This control supports up to 3 icon images and 4 different display
    styles.  The icon image displayed is the one that best fits the
    current size of the control given its current style.This command creates an iconTextCheckBox.
    Args:
        align (Queryable[str]?): The label alignment.  Alignment values are "left",  
                "right", and "center". By default, the label is aligned "center".  
                Currently only available when -st/style is set to "iconAndTextCentered".  
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
        changeCommand (Queryable[Callable[..., Any]]?): Command executed when the control's state is changed.  
                Note that this flag should not be used in conjunction with  
                onCommand and offCommand. That is, one should either use  
                changeCommand and test the state of the control from inside  
                the callback, or use onCommand and offCommand as separate  
                callbacks.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        disabledImage (Queryable[str]?): Image used when the button is disabled. Image size must  
                be the same as the image specified with the i/image flag.  
                This is a Windows only flag.  
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
        flat (bool?): Sets whether the control will be a flat button (0 false, 1 true).  
                Properties: create, query, edit
        flipX (bool?): Is the image flipped horizontally?  
                Properties: create, query, edit
        flipY (bool?): Is the image flipped vertically?  
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
        highlightImage (Queryable[str]?): Highlight image displayed while the cursor is over the  
                control. Image size must be the same as the image specified with  
                the -i/image flag. This is a Windows only flag.  
                Properties: create, query, edit
        image (Queryable[str]?): If you are not providing images with different sizes then you may  
                use this flag for the control's image. If the "iconOnly" style is  
                set, the icon will be scaled to the size of the control.  
                Properties: create, query, edit
        image1 (Queryable[str]?): First of three possible icons. The icon that best fits the  
                current size of the control will be displayed.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons. The icon that best fits the  
                current size of the control will be displayed.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons. The icon that best fits the  
                current size of the control will be displayed.  
                Properties: create, query, edit
        imageOverlayLabel (Queryable[str]?): A short string, up to 6 characters, representing a label that will be displayed  
                on top of the image.  
                Properties: create, query, edit
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        label (Queryable[str]?): The text that appears in the control.  
                Properties: create, query, edit
        labelOffset (Queryable[int]?): The label offset. Default is 0. Currently only available  
                when -st/style is set to "iconAndTextCentered".  
                Properties: create, query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        marginHeight (Queryable[int]?): The number of pixels above and below the control content.  
                The default value is 1 pixel.  
                Properties: create, query, edit
        marginWidth (Queryable[int]?): The number of pixels on either side of the control content.  
                The default value is 1 pixel.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        offCommand (Queryable[Callable[..., Any]]?): Command executed when the control is turned off.  
                Properties: create, query, edit
        onCommand (Queryable[Callable[..., Any]]?): Command executed when the control is turned on.  
                Properties: create, query, edit
        overlayLabelBackColor (Queryable[Tuple[float, float, float, float]]?): The RGBA color of the shadow behind the label defined by  
                imageOverlayLabel. Default is 50% transparent black: 0 0 0 .5  
                Properties: create, query, edit
        overlayLabelColor (Queryable[Tuple[float, float, float]]?): The RGB color of the label defined by imageOverlayLabel. Default is a  
                light grey: .8 .8 .8  
                Properties: create, query, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        rotation (Queryable[float]?): The rotation value of the image in radians.  
                Properties: create, query, edit
        selectionHighlightImage (Queryable[str]?): Image displayed while the control is selected and the cursor  
                is over the control. Image size  
                must be the same as the image specified with the -i/image  
                flag. This is a Windows only flag.  
                Properties: create, query, edit
        selectionImage (Queryable[str]?): Image displayed while the control is selected. Image size  
                must be the same as the image specified with the -i/image  
                flag. This is a Windows only flag.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        style (Queryable[str]?): The draw style of the control.  Valid styles are "iconOnly",  
                "textOnly", "iconAndTextHorizontal", "iconAndTextVertical", and  
                "iconAndTextCentered". (Note: "iconAndTextCentered" is only available on Windows).  
                If the "iconOnly" style is set, the icon will be scaled to the size of the control.  
                Properties: create, query, edit
        useAlpha (bool?): Is the image using alpha channel?  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        value (bool?): Sets or returns the state of the control.  
                Properties: create, query, edit
        version (Queryable[str]?): Specify the version that this control feature was introduced.  
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
        str: Full path name to the control.

    Example:
    """

