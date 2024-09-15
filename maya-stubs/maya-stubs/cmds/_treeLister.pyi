from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def treeLister(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addFavorite: Multiuse[str] = ..., addItem: Multiuse[Tuple[str, str, Callable[..., Any]]] = ..., addVnnItem: Multiuse[Tuple[str, str, str, str]] = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., clearContents: bool = ..., collapsePath: Multiuse[str] = ..., defineTemplate: str = ..., displayName: Queryable[str] = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., executeItem: str = ..., exists: bool = ..., expandPath: Multiuse[str] = ..., expandToDepth: int = ..., favoritesCallback: Callable[..., Any] = ..., favoritesList: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., itemScript: str = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., refreshCommand: Queryable[Callable[..., Any]] = ..., removeFavorite: Multiuse[str] = ..., removeItem: Multiuse[str] = ..., resultsPathUnderCursor: bool = ..., selectPath: Multiuse[str] = ..., setDisplayName: Multiuse[Tuple[str, str]] = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., vnnString: bool = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, int, Callable[..., Any]]:
    """This command creates/edits/queries the tree lister control.
    The optional argument is the name of the control.
    Args:
        addFavorite (Multiuse[str]?): Add an item path to the favorites folder.  The item path does not have to actually be in the tree.  
                Properties: create, edit, multiuse
        addItem (Multiuse[Tuple[str, str, Callable[..., Any]]]?): Add an item to the control.  The arguments are item-path,icon path,command  
                where item-path is the path from the root of the tree to the item's name  
                icon path is the icon displayed in the results list  
                command is the script which is executed when the item is LMB clicked  
                Properties: create, edit, multiuse
        addVnnItem (Multiuse[Tuple[str, str, str, str]]?): Add a VNN (Virtual Node Network) item to the control.  The arguments are:  
                item-path, icon-path, vnn-string, vnn-action.  
                Where item-path is the path from the root of the tree to the item's name,  
                icon-path is the icon displayed in the results list,  
                vnn-string is used for drag data when MMB dragging the item  
                and vnn-action is the script which is executed when the item is LMB clicked.  
                The vnn-string should be comprised of: 'VNN runtime,VNN library,VNN node',  
                where the VNN library can contain sub-libraries, using / to separate.  
                Properties: create, edit, multiuse
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        clearContents (bool?): Clears the contents of the control.  
                Properties: edit
        collapsePath (Multiuse[str]?): Collapse a path in the tree.  
                Properties: edit, multiuse
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displayName (Queryable[str]?): Query the display name of a given item.  
                Properties: query
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
        executeItem (str?): Execute the command associated with an item.  
                Properties: edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        expandPath (Multiuse[str]?): Expand a path in the tree.  
                Properties: edit, multiuse
        expandToDepth (int?): Expand the tree to the given depth.  
                Properties: edit
        favoritesCallback (Callable[..., Any]?): This script is called whenever a favorite is added or removed.  
                It is passed two arguments: The item's path and a boolean indicating if it  
                is being added to favorites (True) or removed (False).  
                Properties: create, edit
        favoritesList (bool?): Returns the list of favorite items.  
                Properties: query
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
        itemScript (str?): Returns the language and script command of the passed item path as a  
                two-element list, the first element is the string "MEL" or "Python" and  
                the second is the command script. Note that items with Python callable  
                commands will be returned as strings.  
                      In query mode, this flag needs a value.  
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
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        refreshCommand (Queryable[Callable[..., Any]]?): Command executed when the refresh button is pressed.  Note: by default the  
                refresh button is hidden and will be shown automatically when this command  
                script is attached.  
                Properties: create, query, edit
        removeFavorite (Multiuse[str]?): Remove an item from favorites.  Accepts the full favorite path or the tail of the full path.  
                Properties: edit, multiuse
        removeItem (Multiuse[str]?): Remove an item path.  
                Properties: edit, multiuse
        resultsPathUnderCursor (bool?): Returns the path to the result (right-pane) item under the mouse cursor.  
                Returns an empty string if there is no such item.  
                Properties: query
        selectPath (Multiuse[str]?): Select a path in the tree.  
                Properties: edit, multiuse
        setDisplayName (Multiuse[Tuple[str, str]]?): Edit the displayed name of a given item.  
                Properties: edit, multiuse
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
        vnnString (bool?): Returns the VNN (Virtual Node Network) string of the passed item path.  
                Properties: query
        width (Queryable[int]?): The width of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit

    Returns:
        str: The name of the created control.

    Example:
    """

