from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def nodeOutliner(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addCommand: Queryable[Callable[..., Any]] = ..., addObject: str = ..., annotation: Queryable[str] = ..., attrAlphaOrder: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., connectivity: Queryable[str] = ..., currentSelection: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., filter: Queryable[str] = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., lastClickedNode: bool = ..., lastMenuChoice: Queryable[str] = ..., longNames: bool = ..., manage: bool = ..., menuCommand: Callable[..., Any] = ..., menuMultiOption: bool = ..., multiSelect: bool = ..., niceNames: bool = ..., noBackground: bool = ..., noConnectivity: bool = ..., nodesDisplayed: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., pressHighlightsUnconnected: bool = ..., preventOverride: bool = ..., redraw: bool = ..., redrawRow: bool = ..., remove: Multiuse[str] = ..., removeAll: bool = ..., replace: Queryable[str] = ..., selectCommand: Queryable[Callable[..., Any]] = ..., showConnectedOnly: bool = ..., showHidden: bool = ..., showInputs: bool = ..., showNonConnectable: bool = ..., showNonKeyable: bool = ..., showOutputs: bool = ..., showPublished: bool = ..., showReadOnly: bool = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[bool, Callable[..., Any], str, Tuple[float, float, float], int]:
    """The nodeOutliner command creates, edits and queries an outline control
    that shows dependency nodes and their attributes. Compound attributes
    are further expandable to show their children. Additional configure
    flags allow multi selection, customizable commands to issue upon
    selection, and showing connections (and connectability) to a single
    input attribute. There are also the abilities to add/remove/replace
    nodes through the command line interface, and drag/add.In some configurations, dragging a connected attribute of a node will
    load the node at the other end of the connection.There is a right mouse button menu and a flag to attach a command to
    it. The menu is used to list the specific connections of a connected
    attribute. Clicking over any spot but the row of a connected attribute
    will show an empty menu. By default, there is no command attached to
    the menu.
    Args:
        addCommand (Queryable[Callable[..., Any]]?): Command executed when the node outliner adds something.  
                String commands use substitution of the term %node for whatever is added, eg,  
                if you want to print the object added, the command should be  
                "print(\\"%node \\\\n\\")".  Callable python objects are passed the node name.  
                Properties: create, query, edit
        addObject (str?): add the given object to the display  
                Properties: edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        attrAlphaOrder (Queryable[str]?): Specify how attributes are to be sorted.  Current recognised values  
                are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and  
                "descend" to sort from 'z' to 'a'.  
                Notes: a) this only applies to top level attributes.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        connectivity (Queryable[str]?): Takes an attribute argument ("nodeName.attributeName"), dims any attributes  
                that can't connect to the given, and highlights any attributes already connected  
                Properties: query, edit
        currentSelection (bool?): Retruns a string array containing what is currently selected  
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
        filter (Queryable[str]?): filter attributes based on a regular expression  
                Properties: query, edit
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
        lastClickedNode (bool?): Returns a string with the last clicked node  
                Properties: query
        lastMenuChoice (Queryable[str]?): Returns the text of the most recent menu selection.  
                Properties: query
        longNames (bool?): Controls whether long or short attribute names will be used  
                in the interface.  Note that this flag is ignored if the niceNames  
                flag is set.  Default is short names. Queried, returns a boolean.  
                Properties: query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        menuCommand (Callable[..., Any]?): Attaches the given command to each item in the popup menu.  
                Properties: edit
        menuMultiOption (bool?): Sets whether a menu option labelled "next available" will appear as the first  
                option on any multi-attribute's right mouse button menu.  Defaults to True.  
                Properties: query, edit
        multiSelect (bool?): Allow multiSelect; more than one thing to be selected at a time  
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
        noConnectivity (bool?): Reset the node outliner to not show any connectivity, ie, redraw all rows normally.  
                Properties: edit
        nodesDisplayed (bool?): Returns a string array containing the list of nodes showing in the node Outliner  
                Properties: query
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        pressHighlightsUnconnected (bool?): Sets whether clicking on an unconnected plug will select it or not.  Default is True.  
                Properties: query, edit
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        redraw (bool?): Redraws the displayed space  
                Properties: edit
        redrawRow (bool?): Redraws the given row  
                Properties: edit
        remove (Multiuse[str]?): remove the given object from the display  
                Properties: edit, multiuse
        removeAll (bool?): remove all objects from the display  
                Properties: edit
        replace (Queryable[str]?): replace what's displayed with the given objects  
                Properties: query, edit
        selectCommand (Queryable[Callable[..., Any]]?): Command issued by selecting.  Different from the c flag in that this  
                command will only be issued if something is selected.  
                Properties: query, edit
        showConnectedOnly (bool?): show (true) or hide (false) only attributes that are connected matching input/output criteria  
                Properties: query, edit
        showHidden (bool?): show (true) or hide (false) UI invisible attributes that match the input/output criteria  
                Properties: query, edit
        showInputs (bool?): show only UI visible attributes that can be connected to  
                Properties: query, edit
        showNonConnectable (bool?): show (true) or hide (false) non connectable attributes that match the input/output criteria  
                Properties: query, edit
        showNonKeyable (bool?): show (true) or hide (false) non keyframeable (animatable) attributes that match the input/output criteria  
                Properties: query, edit
        showOutputs (bool?): show only UI visible attributes that can be connected from  
                Properties: query, edit
        showPublished (bool?): Show only published attributes for an asset or a member of an asset.  
                This flag is ignored on nodes not related to assets.  
                Properties: query, edit
        showReadOnly (bool?): show only read only attributes attributes that can be connected from  
                Properties: query, edit
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
        bool: In query mode, return type is based on queried flag.

    Example:
    """

