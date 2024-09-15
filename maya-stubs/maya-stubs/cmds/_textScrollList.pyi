from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def textScrollList(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allItems: bool = ..., allItemsUniqueTags: bool = ..., allowAutomaticSelection: bool = ..., allowMultiSelection: bool = ..., annotation: Queryable[str] = ..., append: Multiuse[str] = ..., appendPosition: Multiuse[Tuple[int, str]] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., defineTemplate: str = ..., deleteKeyCommand: Callable[..., Any] = ..., deselectAll: bool = ..., deselectIndexedItem: Multiuse[int] = ..., deselectItem: Multiuse[str] = ..., docTag: Queryable[str] = ..., doubleClickCommand: Callable[..., Any] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., emptyLabel: Queryable[str] = ..., enable: bool = ..., enableAll: bool = ..., enableBackground: bool = ..., enableIndexedItem: Multiuse[Tuple[int, bool]] = ..., enableItem: Multiuse[Tuple[str, bool]] = ..., enableKeyboardFocus: bool = ..., enableUniqueTagItem: Multiuse[Tuple[str, bool]] = ..., exists: bool = ..., font: Queryable[str] = ..., fullPathName: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., lineFont: Multiuse[Tuple[int, str]] = ..., manage: bool = ..., noBackground: bool = ..., numberOfItems: bool = ..., numberOfPopupMenus: bool = ..., numberOfRows: Queryable[int] = ..., numberOfSelectedItems: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., removeAll: bool = ..., removeIndexedItem: Multiuse[int] = ..., removeItem: Multiuse[str] = ..., selectCommand: Callable[..., Any] = ..., selectIndexedItem: Queryable[Multiuse[int]] = ..., selectItem: Queryable[Multiuse[str]] = ..., selectUniqueTagItem: Queryable[Multiuse[str]] = ..., showIndexedItem: int = ..., statusBarMessage: str = ..., uniqueTag: Multiuse[str] = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Multiuse[int], Multiuse[str], Callable[..., Any]]:
    """This command creates/edits/queries a text scrolling list. The
    list can be in single select mode where only one item at time
    is selected, or in multi-select mode where many items may be
    selected.Note: The -dgc/dragCallback flag works only on Windows.
    Args:
        allItems (bool?): All the items.  
                Properties: query
        allItemsUniqueTags (bool?): Return all the items as unique tags.  
                Properties: query
        allowAutomaticSelection (bool?): Specify automatic selection mode.  When automaticSelection  
                is on each item that the mouse is over (during dragging once an  
                item has been selected) will be selected.  Thus,  
                if -sc/selectCommand someCommand is set, someCommand  
                will be called for each selected item.  
                If -aas/allowAutomaticSelection is off, then only the item  
                selected when the mouse button is up will be the selected item,  
                so -sc/selectCommand someCommand is only called once if  
                it is set.  
                Properties: create, query, edit
        allowMultiSelection (bool?): Specify multi or single selection mode.  
                Properties: create, query, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        append (Multiuse[str]?): Add an item to the end of the list.  
                Properties: create, edit, multiuse
        appendPosition (Multiuse[Tuple[int, str]]?): Append an item at the specified position.  
                The position is a 1. based index.  
                Properties: create, edit, multiuse
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deleteKeyCommand (Callable[..., Any]?): Specify the command to be executed when the delete or  
                backspace key is pressed.  
                Properties: create, edit
        deselectAll (bool?): Deselect all items.  
                Properties: create, edit
        deselectIndexedItem (Multiuse[int]?): Deselect the indexed item.  Indices are 1. based.  
                Properties: create, edit, multiuse
        deselectItem (Multiuse[str]?): Deselect the item that contains the specified text.  
                Properties: create, edit, multiuse
        docTag (Queryable[str]?): Add a documentation flag to the control.  The documentation flag  
                has a directory structure.  
                (e.g., -dt render/multiLister/createNode/material)  
                Properties: create, query, edit
        doubleClickCommand (Callable[..., Any]?): Specify the command to be executed when an item is double  
                clicked.  
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
        emptyLabel (Queryable[str]?): String that is displayed when the list is empty.  
                Properties: create, query, edit
        enable (bool?): The enable state of the control.  By default, this flag is  
                set to true and the control is enabled.  Specify false and the control  
                will appear dimmed or greyed-out indicating it is disabled.  
                Properties: create, query, edit
        enableAll (bool?): Enable all items.  
                Properties: create, edit
        enableBackground (bool?): Enables the background color of the control.  
                Properties: create, query, edit
        enableIndexedItem (Multiuse[Tuple[int, bool]]?): Enable/disable an item using on the item index. Indices are 1. based.  
                Properties: create, edit, multiuse
        enableItem (Multiuse[Tuple[str, bool]]?): Enable/disable an item using the item text.  
                Properties: create, edit, multiuse
        enableKeyboardFocus (bool?): If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.  
                This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.  
                If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).  
                Properties: create, query, edit
        enableUniqueTagItem (Multiuse[Tuple[str, bool]]?): Enable/disable an item using on the unique item tag.  
                Properties: create, edit, multiuse
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        font (Queryable[str]?): The font for the list items.  Valid values are  
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
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        lineFont (Multiuse[Tuple[int, str]]?): Specify the font for a specific line of the list.  
                The indices are 1. based. Valid font values are  
                "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",  
                "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",  
                "smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".  
                Properties: create, edit, multiuse
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfItems (bool?): Number of items.  
                Properties: query
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        numberOfRows (Queryable[int]?): Number of visible rows.  
                Properties: create, query, edit
        numberOfSelectedItems (bool?): Number of selected items.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        removeAll (bool?): Remove all items.  
                Properties: create, edit
        removeIndexedItem (Multiuse[int]?): Remove the indexed item. Indices are 1. based.  
                Properties: create, edit, multiuse
        removeItem (Multiuse[str]?): Remove the item with the specified text.  
                Properties: create, edit, multiuse
        selectCommand (Callable[..., Any]?): Specify the command to be executed when an item is selected.  
                Properties: create, edit
        selectIndexedItem (Queryable[Multiuse[int]]?): Select the indexed item. Indices are 1. based.  
                Properties: create, query, edit, multiuse
        selectItem (Queryable[Multiuse[str]]?): Select the item that contains the specified text.  
                Properties: create, query, edit, multiuse
        selectUniqueTagItem (Queryable[Multiuse[str]]?): Allow item selections based on the unique tag.  
                In query mode, it will return the unique tag of the selected items.  
                Properties: create, query, edit, multiuse
        showIndexedItem (int?): Show the indexed item.  Scroll the list as necessary so that  
                the indexed item is visible.  Indices are 1. based.  
                Properties: create, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        uniqueTag (Multiuse[str]?): This flag can only be used in conjunction with the append or the appendPosition flag.  
                The string specifies a unique tag for the appended item; the tag can then be used to query an item.  
                This tag provides an alternate way to uniquely identify a list item using a string instead of by index.  
                Tags are case insensitive.  
                Properties: create, edit, multiuse
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

