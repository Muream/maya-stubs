from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def treeView(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addItem: Multiuse[Tuple[str, str]] = ..., allowDragAndDrop: bool = ..., allowHiddenParents: bool = ..., allowMultiSelection: bool = ..., allowReparenting: bool = ..., annotation: Queryable[str] = ..., attachButtonRight: int = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., borderHighlite: Tuple[str, bool] = ..., borderHighliteColor: Tuple[str, float, float, float] = ..., buttonErase: Queryable[Multiuse[Tuple[str, bool]]] = ..., buttonState: Multiuse[Tuple[str, int, str]] = ..., buttonStyle: Multiuse[Tuple[str, int, str]] = ..., buttonTextIcon: Multiuse[Tuple[str, int, str]] = ..., buttonTooltip: Multiuse[Tuple[str, int, str]] = ..., buttonTransparencyColor: Multiuse[Tuple[str, int, float, float, float]] = ..., buttonTransparencyOverride: Multiuse[Tuple[str, int, bool]] = ..., buttonVisible: Multiuse[Tuple[str, int, bool]] = ..., children: str = ..., clearSelection: bool = ..., contextMenuCommand: Callable[..., Any] = ..., defineTemplate: str = ..., displayLabel: Multiuse[Tuple[str, str]] = ..., displayLabelSuffix: Multiuse[Tuple[str, str]] = ..., docTag: Queryable[str] = ..., dragAndDropCommand: Callable[..., Any] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., editLabelCommand: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableButton: Multiuse[Tuple[str, int, int]] = ..., enableKeyboardFocus: bool = ..., enableKeys: bool = ..., enableLabel: Tuple[str, int] = ..., exists: bool = ..., expandCollapseCommand: Callable[..., Any] = ..., expandItem: Tuple[str, bool] = ..., flatButton: Queryable[int] = ..., font: Queryable[Tuple[str, str]] = ..., fontFace: Tuple[str, int] = ..., fullPathName: bool = ..., height: Queryable[int] = ..., hideButtons: bool = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., highlite: Tuple[str, bool] = ..., highliteColor: Tuple[str, float, float, float] = ..., ignoreButtonClick: Multiuse[Tuple[str, int, int]] = ..., image: Multiuse[Tuple[str, int, str]] = ..., insertItem: Multiuse[Tuple[str, str, int]] = ..., isItemExpanded: str = ..., isLeaf: str = ..., isObscured: bool = ..., item: str = ..., itemAnnotation: Queryable[Tuple[str, str]] = ..., itemDblClickCommand: Callable[..., Any] = ..., itemDblClickCommand2: Callable[..., Any] = ..., itemExists: str = ..., itemIndex: str = ..., itemParent: str = ..., itemRenamedCommand: Callable[..., Any] = ..., itemSelected: str = ..., itemVisible: Queryable[Tuple[str, bool]] = ..., labelBackgroundColor: Tuple[str, float, float, float] = ..., manage: bool = ..., noBackground: bool = ..., numberOfButtons: int = ..., numberOfPopupMenus: bool = ..., ornament: Tuple[str, int, int, int] = ..., ornamentColor: Tuple[str, float, float, float] = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., pressCommand: Multiuse[Tuple[int, Callable[..., Any]]] = ..., preventOverride: bool = ..., removeAll: bool = ..., removeItem: str = ..., reverseTreeOrder: bool = ..., rightPressCommand: Multiuse[Tuple[int, Callable[..., Any]]] = ..., select: Tuple[str, int] = ..., selectCommand: Callable[..., Any] = ..., selectItem: Queryable[Tuple[str, bool]] = ..., selectionChangedCommand: Callable[..., Any] = ..., selectionColor: Queryable[Tuple[str, float, float, float]] = ..., showItem: str = ..., statusBarMessage: str = ..., textColor: Tuple[str, float, float, float] = ..., useTemplate: str = ..., verticalScrollPosition: Queryable[int] = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], Multiuse[Tuple[str, bool]], int, Tuple[str, str], Tuple[str, bool], Tuple[str, float, float, float], Callable[..., Any]]:
    """This command creates a custom control.
    Args:
        addItem (Multiuse[Tuple[str, str]]?): Adds a tree view item to the tree view.  
                First argument specifies the item's name, second argument specifies the item's parent (use an empty string to have it at the top level of the tree)  
                Properties: create, edit, multiuse
        allowDragAndDrop (bool?): Allow the user to perform drag and drop of treeView items.  If enabled,  
                re-ordering / re-parenting operations can be perfomed with the middle mouse button.  
                This flag takes precendence over other drag and drop related flags.  
                Defaults to true.  
                Properties: create, query, edit
        allowHiddenParents (bool?): If not cleared(default), the treeView will make parent nodes of visible nodes automatically visible  
                Properties: create, query, edit
        allowMultiSelection (bool?): Specify multi or single selection mode.  
                Allow the user to perform multiple selection by holding  
                ctrl or shift key while selecting items of treeView items.  
                Defaults to true.  
                Properties: create, query, edit
        allowReparenting (bool?): Allow the user to reparent items in the tree view using the middle  
                mouse button. Defaults to true. If false, user can still reorder items  
                within a group using the middle mouse button.  
                Properties: create, query, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        attachButtonRight (int?): Sets tree view item's buttons to appear on the right or left.  
                Argument specifies if they are to be attached to the right, if it is set to false they will attach on the left.  
                Properties: create, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        borderHighlite (Tuple[str, bool]?): Sets an item's border as highlit or not.  
                First Argument specifies item, second argument specifies on or off.  
                Properties: create, edit
        borderHighliteColor (Tuple[str, float, float, float]?): Sets the color an item's border highlite will turn when highlite is enabled.  
                first parameter specifies layer  
                three float values specify RGB values, between 0 and 1.  
                Properties: create, edit
        buttonErase (Queryable[Multiuse[Tuple[str, bool]]]?): If buttonErase was set true , then even if the button of the treeView item  is set invisible , the treeView will still erase the buttonRect of this treeView item with background .  
                First argument is the item name, second argument is whether buttonErase was set true or false  
                Properties: create, query, edit, multiuse
        buttonState (Multiuse[Tuple[str, int, str]]?): Sets the state of a button.  
                First argument specifies the layer, second argument specifies which button, third argument specifies the state  
                Possible states:  
                "buttonUp" - button is up  
                "buttonDown" - button is down  
                "buttonThirdState" - button is in state three (used by the "3StateButton" button style)  
                Properties: create, edit, multiuse
        buttonStyle (Multiuse[Tuple[str, int, str]]?): Sets the type of button, used to indicate possible states and if the button is reset upon release.  
                First argument specifies the layer, second argument specifies which button, third argument specifies the type of button  
                Possible button types:  
                "pushButton" - two possible states, button is reset to up upon release  
                "2StateButton" - two possible states, button changes state on click  
                "3StateButton" - three button states, button changes state on click  
                Properties: create, edit, multiuse
        buttonTextIcon (Multiuse[Tuple[str, int, str]]?): Sets a one letter text to use as the icon to use for a specific button on a specific item.  
                First argument specifies the item, second argument specifies the button, third argument specifies the icon text.  
                Properties: create, edit, multiuse
        buttonTooltip (Multiuse[Tuple[str, int, str]]?): Sets a tooltip for specific button on a specific item.  
                First argument specifies the item, second argument specifies the button, third argument specifies the tooltip.  
                Properties: create, edit, multiuse
        buttonTransparencyColor (Multiuse[Tuple[str, int, float, float, float]]?): Sets the background color of a button that will be used if buttonTransparencyOverride is enabled.  
                First argument specifies item, second argument specifies button,  
                three floats specify RGB values, between 0 and 1.  
                Properties: create, edit, multiuse
        buttonTransparencyOverride (Multiuse[Tuple[str, int, bool]]?): Sets a button's background as being overridden or not.  
                First argument specifies item, second argument specifies button, third argument specifies overridden or not.  
                Properties: create, edit, multiuse
        buttonVisible (Multiuse[Tuple[str, int, bool]]?): Sets a button as visible or not.  
                First Argument specifies item.  
                Second Argument specifies a button.  
                Third Argument specifies visible or not.  
                Properties: create, multiuse
        children (str?): Query the children of an item. If the argument is null, all items will be returned.  
                      In query mode, this flag needs a value.  
                Properties: query
        clearSelection (bool?): Clears all selected items.  
                Properties: create, edit
        contextMenuCommand (Callable[..., Any]?): Set the callback function to be invoked just before any attached context  
                menu is shown. This can be used as a replacement to, or in addition to the  
                postMenuCommand flag on the popupMenu command. The function should accept  
                a string which will be the item that was clicked on (empty if no item was hit).  
                The function should return true if the menu should be shown, false otherwise.  
                Properties: create, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displayLabel (Multiuse[Tuple[str, str]]?): Set a label for the item that is different than the  
                string that identifies the item. This label will be used in the  
                display of the item. The first parameter specifies  
                the item, the second specifies the display label.  
                Properties: create, edit, multiuse
        displayLabelSuffix (Multiuse[Tuple[str, str]]?): Set a suffix for the display label for the item. This suffix will  
                not be shown when renaming the item in the tree view.  
                Properties: create, edit, multiuse
        docTag (Queryable[str]?): Add a documentation flag to the control.  The documentation flag  
                has a directory structure.  
                (e.g., -dt render/multiLister/createNode/material)  
                Properties: create, query, edit
        dragAndDropCommand (Callable[..., Any]?): Sets the callback function to be invoked upon drag and drop of layers.  
                the callback function should take as parameters:  
                - a string array of the dropped items  
                - a string array of the items previous parents  
                - an integer array of the items previous indexes  
                - a string for the item(s) new parent  
                - an integer array for the item's new indexes  
                - a string for the item that now comes before the dropped items  
                - a string for the item that now comes after the dropped items  
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
        editLabelCommand (Callable[..., Any]?): Set the callback function to be invoked when the user changes  
                the name of an item by double clicking it in the UI. The callback should  
                accept two string arguments: the item name and the new name. The item  
                name refers to the name of the item and not the display label. The callback  
                function should return a string. An empty string indicates that the rename  
                operation was invalid and the control should revert to the original name.  
                If the rename operation is valid the callback should return a string that  
                identifies the item, possibly different from the new display name entered  
                by the user.  
                Properties: create, edit
        enable (bool?): The enable state of the control.  By default, this flag is  
                set to true and the control is enabled.  Specify false and the control  
                will appear dimmed or greyed-out indicating it is disabled.  
                Properties: create, query, edit
        enableBackground (bool?): Enables the background color of the control.  
                Properties: create, query, edit
        enableButton (Multiuse[Tuple[str, int, int]]?): Sets a specific button on a specific item to being usable or not.  
                First argument specifies the item, second argument specifies the button, third argument specifies on or off.  
                Properties: create, edit, multiuse
        enableKeyboardFocus (bool?): If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.  
                This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.  
                If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).  
                Properties: create, query, edit
        enableKeys (bool?): By default the treeview does not accept input from the keyboard.  By enabling keyboard support  
                The treeview will support up/down navigation using the up/down arrow keys.  
                Properties: edit
        enableLabel (Tuple[str, int]?): enables or disables the label of a tree view item from being displayed. The first parameter specifies  
                the item, the second specifies on or off.  
                Properties: create, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        expandCollapseCommand (Callable[..., Any]?): Set the callback function to be invoked upon hitting the expand/collapse button.  
                The function should take as parameters:  
                - a string for the item for which the expand/collapse button was hit  
                - an integer for the state of expansion  
                Properties: create, edit
        expandItem (Tuple[str, bool]?): Expands or collapses an item's children.  
                First argument specifies the item, second argument specifies expanded or collapsed.  
                Properties: create, edit
        flatButton (Queryable[int]?): Type of flat button to use.  
                Properties: create, query, edit
        font (Queryable[Tuple[str, str]]?): The first parameter specifies the item string for  
                the TtreeViewNode in the TtreeNodeMap.  
                The second string specifies the font for the text.  
                Valid values are  
                "boldLabelFont", "smallBoldLabelFont", "tinyBoldLabelFont",  
                "plainLabelFont", "smallPlainLabelFont", "obliqueLabelFont",  
                "smallObliqueLabelFont", "fixedWidthFont" and "smallFixedWidthFont".  
                Properties: create, query, edit
        fontFace (Tuple[str, int]?): Sets the font face used for the specified item's text:  
                0 for normal,  
                1 for bold,  
                2 for italic.  
                Properties: create, edit
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        hideButtons (bool?): Hides the buttons for an item in the tree view. Can only be used when  
                adding the item to the tree with the "addItem" flag. Space for the buttons  
                is left to make sure items still line up correctly under their parent.  
                Properties: create, edit
        highlightColor (Queryable[Tuple[float, float, float]]?): The highlight color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query, edit
        highlite (Tuple[str, bool]?): Sets an item as highlit. Highliting is shown by outlining the item.  
                First parameter specifies the item, the second specifies the highliting  
                or not.  
                Properties: create, edit
        highliteColor (Tuple[str, float, float, float]?): Sets the color an item's highlite will turn when highlite is enabled.  
                first parameter specifies layer  
                three float values specify RGB values, between 0 and 1.  
                Properties: create, edit
        ignoreButtonClick (Multiuse[Tuple[str, int, int]]?): Sets a specific button on a specific item to ignore the button clicks  
                First argument specifies the item ,second argument specifies the button, third argument specifies on or off  
                Properties: create, edit, multiuse
        image (Multiuse[Tuple[str, int, str]]?): Sets an image to use as the icon for the button.  
                First argument specifies the item, second argument specifies the button, third argument specifies the image.  
                Properties: create, edit, multiuse
        insertItem (Multiuse[Tuple[str, str, int]]?): Create and insert a tree view item to the tree view.  
                First argument specifies the item's name, second argument specifies the item's parent (use an empty string to have it at the top level of the tree), third argument is the child's index position in the children list.  An index less than or equal to 0 inserts as the first child, greater than or equal to the number of children inserts as last child.  
                Properties: create, edit, multiuse
        isItemExpanded (str?): Is the item in the tree view expanded.  
                      In query mode, this flag needs a value.  
                Properties: query
        isLeaf (str?): Query whether an item is a leaf.  
                      In query mode, this flag needs a value.  
                Properties: query
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        item (str?): Specify the item to query. Used with the flag "selectionColor" and "itemAnnotation".  
                      In query mode, this flag needs a value.  
                Properties: query
        itemAnnotation (Queryable[Tuple[str, str]]?): Annotate the specified item with an extra string value.  
                When used for query, this flag has no argument and needs to be used with the  
                flag "item".  
                Properties: create, query, edit
        itemDblClickCommand (Callable[..., Any]?): Set the callback function to be invoked when an item in the tree has been  
                double clicked. The callback should accept one string, the display label of the  
                item that was double clicked. If this callback is defined, it supersedes  
                the normal item renaming behavior.  
                Properties: create, edit
        itemDblClickCommand2 (Callable[..., Any]?): Set the callback function to be invoked when an item in the tree has been  
                double clicked. This callback is similar to itemDblClickCommand(idc), but it accepts two strings:  
                the name and the display label of the item that was double clicked. If this callback is defined,  
                it supersedes the normal item renaming behavior  
                Properties: create, edit
        itemExists (str?): Queries the existence of the specified Tree View item.  
                      In query mode, this flag needs a value.  
                Properties: create, query
        itemIndex (str?): Get the index for the specified item in the list of children of the item's  
                parent. Index is 0. based.  
                      In query mode, this flag needs a value.  
                Properties: create, query
        itemParent (str?): If the specified item is a child, it returns the parent item. If the specified item is not a child it returns nothing.  
                      In query mode, this flag needs a value.  
                Properties: create, query
        itemRenamedCommand (Callable[..., Any]?): Set the callback function to be invoked when an item in the tree has been  
                renamed. This occurs if there is a successful return of the command attached  
                by "editLabelCommand" or unconditionally if there is no editLabelCommand.  
                The callback should accept two strings, the old name and the new name of the  
                item that was renamed.  
                Properties: create, edit
        itemSelected (str?): Queries the item is currently selected or not.  
                      In query mode, this flag needs a value.  
                Properties: query
        itemVisible (Queryable[Tuple[str, bool]]?): Control the given item's visibility.  
                Properties: create, query, edit
        labelBackgroundColor (Tuple[str, float, float, float]?): Set the background color for text label for a particular item  
                in the tree. The first parameter specifies layer.  
                Set (-1.0, -1.0, -1.0) to restore the background  
                to the default of "transparent"  
                Properties: create, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfButtons (int?): Specifies the number of buttons for items in the tree.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        ornament (Tuple[str, int, int, int]?): Sets an item as having an ornament (a small colored circle), its on/off state, if it should have a dot, and its size.  
                First Argument specifies item,  
                second argument specifies on or off,  
                third argument specifies dotted or not,  
                fourth argument specifies radius (in pixels).  
                Properties: create, edit
        ornamentColor (Tuple[str, float, float, float]?): Sets the color an ornament will be draw with for the specified layer.  
                Properties: create, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        pressCommand (Multiuse[Tuple[int, Callable[..., Any]]]?): Sets the callback function to be invoked upon clicking a treeView button.  
                First argument specifies which treeView button.  
                Second argument specifies the callback function to be executed  
                the callback function should take as parameters:  
                - a string for the clicked button's item  
                - an int for the clicked button's state  
                Properties: create, edit, multiuse
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        removeAll (bool?): Removes all items from the tree view.  
                Properties: create, edit
        removeItem (str?): Removes a tree view item from the tree view. If this item has children items, all children items are removed.  
                First argument specifies the item's name.  
                Properties: create, edit
        reverseTreeOrder (bool?): Controls the order the tree will be drawn in (reversed if true).  
                Properties: create, edit
        rightPressCommand (Multiuse[Tuple[int, Callable[..., Any]]]?): Sets the callback function to be invoked upon right clicking a treeView button.  
                First argument specifies which treeView button.  
                Second argument specifies the callback function to be executed  
                the callback function should take as parameters:  
                - a string for the clicked button's item  
                - an int for the clicked button's state  
                Properties: create, edit, multiuse
        select (Tuple[str, int]?): Set selection on an element. The first parameter specifies the item, the second specifies on or off.  
                Properties: create, edit
        selectCommand (Callable[..., Any]?): Set the callback function to be invoked when an item is selected or deselected  
                in the tree. The function should accept one string argument and  
                one integer argument: the item name and the select state respectively. If the  
                function returns true, the select/deselect is considered valid and will  
                occur normally, otherwise it will be disallowed.  
                name and  
                Properties: create, edit
        selectItem (Queryable[Tuple[str, bool]]?): Sets an item's selected state.  
                first argument specifies the item, second argument specifies selection status.  
                When used for query without arguments, return all selected items in the treeview.  
                Properties: create, query, edit
        selectionChangedCommand (Callable[..., Any]?): Set the callback function to be invoked when a complete selection operation  
                triggered by the user has occurred successfully. The callback is invoked if  
                the "selectCommand" callback has returned a non-empty value (or always there  
                is no "selectCommand" callback). This differs from selectCommand in that a  
                simple selection replacement will generate two callbacks with "selectCommand"  
                (one for deselect of the old item and one for select of the new), whereas  
                "selectionChangedCommand" will only be invoked once, after the selection is  
                complete. The callback is not passed any parameters and does not need to  
                return any value (i.e. It is simply a notification mechanism).  
                Properties: create, edit
        selectionColor (Queryable[Tuple[str, float, float, float]]?): Sets the color an item will turn to indicate that it is selected.  
                first parameter specifies the item  
                three float values specify RGB values, between 0 and 1.  
                When used for query, this flag has no argument and needs to be used with the  
                flag "item". It returns the color an item will become if it is selected.  
                Properties: create, query, edit
        showItem (str?): Show the  item. Scroll the list as necessary so that item is visible.  
                Properties: create, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        textColor (Tuple[str, float, float, float]?): Sets the label's text color for the specified layer.  
                first argument specifies layer.  
                three float values specify RGB values, between 0 and 1.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        verticalScrollPosition (Queryable[int]?): The position of the vertical scrollbar.  
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
        str: The full name of the control.

    Example:
    """

