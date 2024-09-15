from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def menuEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., cellHeight: Queryable[int] = ..., cellWidth: Queryable[int] = ..., cellWidthHeight: Tuple[int, int] = ..., checkBoxPresent: Queryable[Tuple[bool, str, int]] = ..., checkBoxState: Queryable[Tuple[bool, str, int]] = ..., command: Queryable[Tuple[str, str, int]] = ..., defineTemplate: str = ..., delete: Tuple[str, int] = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., iconMenuCallback: str = ..., image: Queryable[Tuple[str, str, int]] = ..., isObscured: bool = ..., label: Queryable[Tuple[str, str, int]] = ..., manage: bool = ..., menuItemTypes: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., optionBoxCommand: Queryable[Tuple[str, str, int]] = ..., optionBoxPresent: Queryable[Tuple[bool, str, int]] = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., radioButtonPresent: Queryable[Tuple[bool, str, int]] = ..., radioButtonState: Queryable[Tuple[bool, str, int]] = ..., separator: Queryable[Tuple[str, int]] = ..., statusBarMessage: str = ..., style: Queryable[str] = ..., subMenuAt: Tuple[str, int] = ..., subMenuEditorWindow: str = ..., subMenuEditorsOpen: bool = ..., subMenuOf: Tuple[str, str, int] = ..., topLevelMenu: Queryable[str] = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], int, Tuple[bool, str, int], Tuple[str, str, int], bool, Tuple[str, int], Callable[..., Any]]:
    """A menuEditor displays the contents of a popup menu and allows the
    menu's items to be edited. Menu items are represented by labelled
    icons which can be dragged around within the editor to change the
    menu's layout.  Various objects can be dragged and dropped into
    the menuEditor to create new menu items: toolButtons from the shelf
    or toolbox, shelfButtons from the shelf, iconTextButtons with attached
    commands, and scripts from the command window.When editing a Marking Menu, the radial menu items correspond to 8
    icons arranged in a circle within the menuEditor.  Overflow items in
    the Marking Menu (or linear items in a normal menu) are displayed in
    a column below the radial items.To edit a submenu of a popup menu, a new menuEditor instance must be
    created (typically within its own window) and attached to its parent
    menuEditor.Some flags require the position of a menu item to be passed in as an
    argument.  For these, positions are specified with a (string,int)
    pair, where the string corresponds to a radial position
    (possibily "None") and the int corresponds to a linear position
    (possibly equal to 0 for none).  Radial positions are specified by
    one of ("N",0), ("NE",0), ("E",0), ("SE",0), ("S",0), ("SW",0),
    ("W",0) or ("NW",0).  Overflow, or linear positions, are specified
    with ("None",i), where i is a 1-based index giving the position of
    the item within the overflow column.This command is not meant to be called explicitly. It was
    created to support the Marking Menu editor. It is recommended that you
    use that editor to modify marking menus.
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
        cellHeight (Queryable[int]?): The height of the icons in the menuEditor.  
                Properties: query, edit
        cellWidth (Queryable[int]?): The width of the icons in the menuEditor.  
                Properties: query, edit
        cellWidthHeight (Tuple[int, int]?): The width and height of the icons in the menuEditor.  
                Properties: edit
        checkBoxPresent (Queryable[Tuple[bool, str, int]]?): This controls whether a menu item has a check box or not.  
                The arguments are a flag indicating presence, followed by the position of the menu item.  
                This flag is ignored if the menu item is a submenu item.  
                If queried, an array of booleans is returned containing all the flags.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        checkBoxState (Queryable[Tuple[bool, str, int]]?): The state of the check box associated with a menu item.  
                The arguments are a flag indicating state, followed by the position of the menu item.  
                This flag is ignored if the menu item does not have a check box.  
                If queried, an array of booleans is returned containing all the flags.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        command (Queryable[Tuple[str, str, int]]?): The command or script executed by a menu item.  
                The arguments are the command string or script name, followed by the  
                position of the menu item. This flag is ignored if the menu item is  
                a submenu item or a separator item.  
                If queried, an array of strings is returned containing all the commands.  
                The first 8 entries of the array correspond to radial items (in  
                order, "N", "NE", ... "NW"), and all later entries correspond to  
                overflow (or linear) menu items.  
                Properties: query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        delete (Tuple[str, int]?): Deletes the menu item at the given position, removing it from  
                the menu.  If the menu item has a submenu, and a sub-menuEditor is  
                open and attached to it, then the sub-menuEditor's window and  
                all its child menuEditor windows will be closed recursively.  
                Properties: edit
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
        iconMenuCallback (str?): This is the name of a MEL callback procedure that is called to  
                create the popup menus attached to icons in the menuEditor.  The  
                callback is called once for each newly created icon, and once each  
                time an icon is moved within the menuEditor.  Popup menus created  
                by the callback should contain commands for editing the menu item  
                associated with the icon.  Operations accessible through the menu  
                should include deletion of the item, editing of the  
                item's label/command/image/checkbox/optionbox, creation of a submenu,  
                and popping up a sub-menuEditor.  
              
                The arguments to the callback must match this form:  
              
                callbackProc(string $menuEditorName, string $parentIconName, string $menuTitle, string $radialPosition, int $overflowRow);  
              
                The popup menu's parent should be $parentIconName.  
              
                Note that when a sub-menuEditor is created, this flag need not be  
                re-specified as it adopts a default value equal to the value of  
                its parent menuEditor's -imc/iconMenuCallback flag.  
                Properties: create
        image (Queryable[Tuple[str, str, int]]?): The filename of the icon associated with a menu item.  
                This icon is displayed by the menuEditor to represent the menu item.  
                The arguments are the icon filename, followed by the position of the menu item.  
                If queried, an array of strings is returned containing all the icon filenames.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        label (Queryable[Tuple[str, str, int]]?): The label of a menu item.  
                The arguments are the label text, followed by the position of the  
                menu item. If queried, an array of strings is returned containing  
                all the labels. The first 8 entries of the array correspond to radial  
                items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        menuItemTypes (bool?): This is a query only flag.  Returns an array of strings indicating the type of contents in  
                each cell of the menuEditor.  Cells can be "vacant", or may contain a regular menu "item",  
                or a "separator", or a "submenu" item.  In each case, the corresponding string is returned.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        optionBoxCommand (Queryable[Tuple[str, str, int]]?): The command or script executed by a menu item's associated option box item.  
                The arguments are the command string or script name, followed by the position of the menu item.  
                This flag is ignored if the menu item does not have an associated option box item.  
                If queried, an array of strings is returned containing all the commands.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        optionBoxPresent (Queryable[Tuple[bool, str, int]]?): This controls whether a menu item has an associated option box item or not.  
                The arguments are a flag indicating presence, followed by the position of the menu item.  
                This flag is ignored if the menu item is a submenu item.  
                If queried, an array of booleans is returned containing all the flags.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        radioButtonPresent (Queryable[Tuple[bool, str, int]]?): This controls whether a menu item has a radio button or not.  
                The arguments are a flag indicating presence, followed by the position of the menu item.  
                This flag is ignored if the menu item is a submenu item.  
                If queried, an array of booleans is returned containing all the flags.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        radioButtonState (Queryable[Tuple[bool, str, int]]?): The state of the radio button associated with a menu item.  
                The arguments are a flag indicating state, followed by the position of the menu item.  
                This flag is ignored if the menu item does not have a radio button.  
                If queried, an array of booleans is returned containing all the flags.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        separator (Queryable[Tuple[str, int]]?): In edit mode this adds a separator to the menuEditor at the  
                specified position. The parameters are the radialPosition and the  
                overflowRow. If queried, an array of booleans is returned indicating  
                if the item is a separator item. The first 8 entries of the array  
                correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        style (Queryable[str]?): This is the style of icons within the menuEditor. Valid styles  
                are "iconOnly", "textOnly", "iconAndTextHorizontal"  
                and "iconAndTextVertical".  
                Properties: query, edit
        subMenuAt (Tuple[str, int]?): Creates a submenu item at the given position.  A submenu item  
                created within the radial portion of a menu will overwrite whatever  
                item (if any) is currently at the given position. A submenu item  
                created within the overflow (linear) portion of a menu will be  
                inserted before  
                the item currently at the given position.  
                Properties: edit
        subMenuEditorWindow (str?): The name of the window which contains a sub-menuEditor.  Only use  
                when creatitg a sub-menuEditor. This window will automatically be  
                closed if a parent menuEditor is closed or if a parent menu item  
                is deleted.  
                Properties: create
        subMenuEditorsOpen (bool?): This is a query only flag.  Returns an array of booleans, each of which indicates if a  
                sub-menuEditor is open and attached to the menu item in a particular cell.  One boolean  
                is returned for each cell in the menuEditor, even if the cell is vacant or contains  
                a non-submenu item (false will be returned in both these cases).  Only when a cell contains  
                a submenu item can true possibily be returned.  
                The first 8 entries of the array correspond to radial items (in order, "N", "NE", ... "NW"),  
                and all later entries correspond to overflow (or linear) menu items.  
                Properties: query
        subMenuOf (Tuple[str, str, int]?): Attaches a sub-menuEditor to its parent menuEditor.  Only use when  
                creatitg a sub-menuEditor. The arguments are the name  
                of the parent menuEditor, followed by the position of a submenu item  
                within the parent. A submenu item must already exist within the parent  
                at the given position. A submenu item cannot have multiple  
                sub-menuEditors attached to it.  
                Properties: create
        topLevelMenu (Queryable[str]?): The popup menu to attach to the editor.  All editing operations  
                performed in the editor (i.e. inserting/deleting/moving an item) will  
                be immediately reflected in this menu. This flag is ignored if the  
                editor is a sub-menuEditor.  The editor will update gracefully if the  
                value of the flag is changed from its initial value.  
                Properties: query, edit
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
        str: Full path name to the editor.

    Example:
    """

