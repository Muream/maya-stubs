from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def channelBox(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., attrBgColor: Queryable[Tuple[float, float, float]] = ..., attrColor: Queryable[Tuple[float, float, float]] = ..., attrFilter: Queryable[str] = ..., attrRegex: Queryable[str] = ..., attributeEditorMode: bool = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., containerAtTop: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., enableLabelSelection: bool = ..., execute: Tuple[str, bool] = ..., exists: bool = ..., fieldWidth: Queryable[int] = ..., fixedAttrList: Queryable[List[str]] = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., historyObjectList: bool = ..., hyperbolic: bool = ..., inputs: bool = ..., isObscured: bool = ..., labelWidth: Queryable[int] = ..., longNames: bool = ..., mainListConnection: Queryable[str] = ..., mainObjectList: bool = ..., manage: bool = ..., maxHeight: Queryable[int] = ..., maxWidth: Queryable[int] = ..., niceNames: bool = ..., noBackground: bool = ..., nodeRegex: Queryable[str] = ..., numberOfPopupMenus: bool = ..., outputObjectList: bool = ..., outputs: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., precision: Queryable[int] = ..., preventOverride: bool = ..., rebuildCommand: Queryable[Callable[..., Any]] = ..., select: Multiuse[str] = ..., selectedHistoryAttributes: bool = ..., selectedMainAttributes: bool = ..., selectedOutputAttributes: bool = ..., selectedShapeAttributes: bool = ..., shapeObjectList: bool = ..., shapes: bool = ..., showNamespace: bool = ..., showTransforms: bool = ..., speed: Queryable[float] = ..., statusBarMessage: str = ..., takeFocus: bool = ..., ufeFixedAttrList: Queryable[Tuple[str, List[str]]] = ..., update: bool = ..., useManips: Queryable[str] = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, int, List[str], Callable[..., Any], float, Tuple[str, List[str]]]:
    """This command creates a channel box, which is sensitive to the active
    list.  It displays certain attributes (channels) of the last node on
    the active list, and provides a two-way connection to keep the widget
    up to date.Note: when setting the color of attribute names, that color is only valid
    for its current Maya session; each subsequent session will display the default
    color for the attribute name(s) listed in the Channel Box. Any subsequent
    attributes that are added to the Channel Box will be affected by prior
    regular expressions in their current Maya session.
    Args:
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        attrBgColor (Queryable[Tuple[float, float, float]]?): Controls the background text color of specific attribute names. As with the foreground  
                option, this text coloring also depends on the node name choice for the nodeRegex flag.  
                Arguments correspond to the red, green, and blue color components.  
                Each component ranges in value from 0.0 to 1.0. If attrRegex is  
                unspecified then it will assume a value of "*" for a regular expression.  
                The same idea simultaneously applies to the flag nodeRegex.  
                Note: nodes that are renamed will have their node name coloring be affected  
                in the channel box.  
                Properties: create, query, edit
        attrColor (Queryable[Tuple[float, float, float]]?): Controls the foreground text color of specific attribute names. This  
                text coloring also depends on the node name choice for the nodeRegex flag.  
                Arguments correspond to the red, green, and blue color components.  
                Each component ranges in value from 0.0 to 1.0. If attrRegex is  
                unspecified then it will assume a value of "*" for a regular expression.  
                The same idea simultaneously applies to the flag nodeRegex.  
                Note: nodes that are renamed will have their node name coloring be affected  
                in the channel box.  
                Properties: create, query, edit
        attrFilter (Queryable[str]?): Specifies the name of an itemFilter object to be placed on the channel box.  
                This filters the attributes displayed. A filter of "0" can be used to reset the  
                filter.  
                Properties: query, edit
        attrRegex (Queryable[str]?): Specifies a valid regular expression to specify which attribute names  
                should be selected for foreground text coloring. If attrRegex is  
                unspecified then it will assume a value of "*" for a regular expression.  
                The same idea simultaneously applies to the flag nodeRegex.  
                The attrColor flag is required to be specified.  
                Note: this regular expression will be treated as though it were case-insensitve  
                Properties: create, query, edit
        attributeEditorMode (bool?): Modifies what appears in the channel box for use in the  
                attribute editor. Default is false. Queried, returns a boolean.  
                Properties: query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        containerAtTop (bool?): This flag can be used to specify whether or not the container is drawn at the  
                top of the channel box when a node in the container is selected.  
                Properties: query, edit
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
        enableLabelSelection (bool?): Enables the selection of attributes in the channelBox  
                when used in conjunction with -attributeEditorMode.  
                Default is false.  Queried, returns a boolean.  
                Properties: query, edit
        execute (Tuple[str, bool]?): Immediately executes the command string once for every cell (or every  
                selected cell, if the boolean argument is TRUE) in the  
                channel box, for every matching selected object (ie, for every object would  
                be affected if you changed a cell value.)  Before the command is executed,  
                "#A" is substituted with the name of the attribute, and "#N" with the name  
                of the node, and "#P" with the full path name of the node.  
                Properties: edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fieldWidth (Queryable[int]?): An optional flag which is used to modify the width assigned  
                to fields appearing in the channelBox.  
                Properties: query, edit
        fixedAttrList (Queryable[List[str]]?): Forces the channel box to only display attributes with the  
                specified names, in the order they are specified.  If an empty  
                list is specified, then the channel box will revert to its default  
                behaviour of listing all keyable attributes.  
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
        historyObjectList (bool?): Returns a list of strings, the names of every INPUT node associated with  
                an object on the main object list that is of the same type as the node  
                displayed in the INPUT section of the channel box.  
                Properties: query
        hyperbolic (bool?): Determines whether or not the distance that the mouse has been dragged  
                should be interpreted as a linear or hyperbolic function.  The default  
                is set to hyperbolic being false.  
                Properties: create, query, edit
        inputs (bool?): Returns the items shown under the 'INPUTS' heading in the channel box.  
                Properties: query
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        labelWidth (Queryable[int]?): An optional flag which is used to modify the width assigned  
                to labels appearing in the channelBox.  
                Properties: query, edit
        longNames (bool?): Controls whether long or short attribute names will be used  
                in the interface.  Note that this flag is ignored if the -niceNames  
                flag is set.  Default is short names. Queried, returns a boolean.  
                Properties: query, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object which the  
                editor will use as its source of content.  The channel box will  
                only display the (last) item contained in the selectionConnection object.  
                If a NULL string ("") is specified, then the channel box will revert  
                to its default behaviour of working on the active list.  
                Properties: create, query, edit
        mainObjectList (bool?): Returns a list of strings, the names of every object on the active  
                list that is the same type as the object displayed in the top (main)  
                section of the channel box.  
                Properties: query
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        maxHeight (Queryable[int]?): An optional flag which is used to limit the height of the  
                channelBox.  
                Properties: query, edit
        maxWidth (Queryable[int]?): An optional flag which is used to limit the width of the  
                channelBox.  
                Properties: query, edit
        niceNames (bool?): Controls whether the attribute names will be displayed in  
                a more user-friendly, readable way.  When this is on, the longNames  
                flag is ignored.  When this is off, attribute names will be displayed  
                either long or short, according to the longNames flag.  
                Default is on. Queried, returns a boolean.  
                Properties: query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        nodeRegex (Queryable[str]?): Specifies a valid regular expression to specify which node names should  
                (potentially) have their attributes selected for foreground text coloring.  
                If nodeRegex is unspecified then it will assume a value of "*' for a  
                regular expression. The same idea simultaneously applies to the flag  
                attrRegex. The attrColor flag is required to be specified.  
                Note: this regular expression will be treated as though it were case-insensitve  
                Note: nodes in namespaces have regular expressions applied as though those  
                nodes weren't in namespaces  
                Properties: create, query, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        outputObjectList (bool?): Returns a list of strings, the names of every OUTPUT node associated  
                an object on the main object list that is of the same type as the node  
                displayed in the OUTPUT section of the channel box.  
                Properties: query
        outputs (bool?): Returns the items shown under the 'OUTPUTS' heading in the channel box.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        precision (Queryable[int]?): Controls the number of digits to the right of the decimal  
                point that will be displayed for float-valued channels.  
                Default is 3.  Queried, returns an int.  
                Properties: query, edit
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        rebuildCommand (Queryable[Callable[..., Any]]?): Command that gets executed when the channel box is rebuilt, e.g. when a new  
                object is selected.  
                Properties: create, query, edit
        select (Multiuse[str]?): Allows programmatic selection of items (nodes or plugs) in the channel box.  
                Selection is equivalent to clicking the item with the mouse; therefore  
                only items currently shown in the channel box can be selected this way.  
                Properties: edit, multiuse
        selectedHistoryAttributes (bool?): Returns a list of strings, the names of all the selected attributes  
                in the INPUT section of the channel box.  
                Properties: query
        selectedMainAttributes (bool?): Returns a list of strings, the names of all the selected attributes in the  
                top section of the channel box.  
                Properties: query
        selectedOutputAttributes (bool?): Returns a list of strings, the names of all the selected attributes  
                in the OUTPUT section of the channel box.  
                Properties: query
        selectedShapeAttributes (bool?): Returns a list of strings, the names of all the selected attributes  
                in the middle (shape) section of the channel box.  
                Properties: query
        shapeObjectList (bool?): Returns a list of strings, the names of every shape associated with  
                an object on the main object list that is of the same type as the object  
                displayed in the middle (shape) section of the channel box.  
                Properties: query
        shapes (bool?): Returns the items shown under the 'SHAPES' heading in the channel box.  
                Properties: query
        showNamespace (bool?): Controls whether or not the namespace of an object is displayed  
                if the object is not in the root namespace.  
                Properties: create, query, edit
        showTransforms (bool?): Controls whether this control will display transform attributes  
                only, or all other attributes. False by default. Queried, returns a  
                boolean.  
                Properties: query, edit
        speed (Queryable[float]?): Controls the speed at which the attributes are changed based on the  
                distance the mouse has been dragged.  Common settings for  
                slow/medium/fast are 0.1/1.0/10.0 respectively.  The default is 1.0.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        takeFocus (bool?): causes the channel box to take over the keyboard focus, if it can.  
                Properties: edit
        ufeFixedAttrList (Queryable[Tuple[str, List[str]]]?): Forces the channel box to only display attributes for the given  
                UFE runtime with the specified names, in the order they are specified.  
                The attribute list accepts wildcard ('?' for one char, '*' for many) and  
                will use pattern matching for finding attributes to display.  
                If an empty list is specified, then the channel box will display no  
                attributes for the given UFE runtime (since there is no keyable  
                attribute concept in UFE).  
                      In query mode, this flag can accept a value.  
                Properties: create, query, edit
        update (bool?): This flag can be used to force an update of the channel box display, for  
                example after changing a display preference.  
                Properties: edit
        useManips (Queryable[str]?): When you click on a field or label in the channel box, the  
                tool switches to a manipulator that can change that value if you  
                drag in the 3d view.  This flag controls the kind of manips.  Allowed  
                values are "none" (self-explanatory), "invisible" (you won't see anything,  
                but dragging in the window will adjust any of the selected attributes),  
                and "standard" (the same as invisible, except for scale, rotate, and  
                translate, which will be represented by their usual manips.)  
                Properties: create, query, edit
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
        str: (the name of the new channel box)

    Example:
    """

