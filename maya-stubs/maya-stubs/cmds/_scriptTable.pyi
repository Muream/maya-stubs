from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scriptTable(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., afterCellChangedCmd: Callable[..., Any] = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., cellBackgroundColorCommand: Callable[..., Any] = ..., cellChangedCmd: Callable[..., Any] = ..., cellForegroundColorCommand: Callable[..., Any] = ..., cellIndex: Tuple[int, int] = ..., cellValue: Queryable[str] = ..., clearRow: int = ..., clearTable: bool = ..., columnFilter: Tuple[int, str] = ..., columnWidth: Multiuse[Tuple[int, int]] = ..., columns: Queryable[int] = ..., defineTemplate: str = ..., deleteRow: int = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., editable: bool = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., excludingHeaders: bool = ..., exists: bool = ..., fullPathName: bool = ..., getCellCmd: Callable[..., Any] = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., insertRow: int = ..., isObscured: bool = ..., label: Multiuse[Tuple[int, str]] = ..., manage: bool = ..., multiEditEnabled: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., preventOverride: bool = ..., rowHeight: Queryable[int] = ..., rows: Queryable[int] = ..., rowsRemovedCmd: Callable[..., Any] = ..., rowsToBeRemovedCmd: Callable[..., Any] = ..., selectedCells: Queryable[List[int]] = ..., selectedColumns: Queryable[List[int]] = ..., selectedRow: bool = ..., selectedRows: Queryable[List[int]] = ..., selectionBehavior: Queryable[int] = ..., selectionChangedCmd: Callable[..., Any] = ..., selectionMode: Queryable[int] = ..., sortEnabled: bool = ..., statusBarMessage: str = ..., underPointerColumn: bool = ..., underPointerRow: bool = ..., useDoubleClickEdit: bool = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], int, bool, List[int], Callable[..., Any]]:
    """This command creates/edits/queries the script table control.
    Args:
        afterCellChangedCmd (Callable[..., Any]?): Sets the script to call after the value of a cell has been  
                changed. The procedure is called with  
                2 integer arguments specifying the row and column for  
                which the value was changed. The 3rd argument is the string  
                which was entered into that cell. The procedure does not need to  
                return any value.  
                The row and column numbers passed in are 1. based  
                (i.e. (1,1) is the upper left cell). The procedure should be  
                of the form:  
              
                global proc procedureName(int $row, int $column, string $value)  
                Properties: create, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        cellBackgroundColorCommand (Callable[..., Any]?): Sets the script to call when it requires  
                the background color of a cell.  
                The procedure is called with  
                2 integer arguments specifying the row and column for  
                which the value is required. The procedure should return  
                an array of ints which is the RGB color value for the cell.  
                The row and column numbers passed in are 1. based  
                (i.e. (1,1) is the upper left cell).  
                The procedure should be of the form:  
              
                global proc int[] procedureName(int $row, int $column) {  
                return {255,0,0}; // return Red as cell background color  
                }  
                Properties: create, edit
        cellChangedCmd (Callable[..., Any]?): Sets the script to call when somebody has  
                changed the value of a cell. The procedure is called with  
                2 integer arguments specifying the row and column for  
                which the value was changed. The 3rd argument is the string  
                which was entered into that cell. The procedure should return  
                an integer value which indicates whether that value should be  
                accepted (return 1 if yes, and 0 if no).  
                The row and column numbers passed in are 1. based  
                (i.e. (1,1) is the upper left cell). The procedure should be  
                of the form:  
              
                global proc int procedureName(int $row, int $column, string $value)  
                Properties: create, edit
        cellForegroundColorCommand (Callable[..., Any]?): Sets the script to call when it requires  
                the foreground color of a cell.  
                The procedure is called with  
                2 integer arguments specifying the row and column for  
                which the value is required. The procedure should return  
                an array of ints which is the RGB color value for the cell.  
                The row and column numbers passed in are 1. based  
                (i.e. (1,1) is the upper left cell).  
                The procedure should be of the form:  
              
                global proc int[] procedureName(int $row, int $column) {  
                return {0,0,0}; // return Black as Text color  
                }  
                Properties: create, edit
        cellIndex (Tuple[int, int]?): used with cellValue , to give the index of row and column  
                This flag and its argument must be passed to the command before the  
                -q flag (see examples).  
                      In query mode, this flag needs a value.  
                Properties: query, edit
        cellValue (Queryable[str]?): query and set the cell value on the table by the index of row and column referred in  
                flag -cellIndex.  
                In edit mode, if flag -multiEditEnabled is True and any cell is selected,  
                the flag -cellIndex is not used and the selected cells will be changed.  
                Properties: query, edit
        clearRow (int?): Clear the contents for all the cells on the specified  
                row. Any procedure specified by the -gcc flag will be  
                called to populate the cleared cells  
                The row number is 1. based (i.e. the first row is 1 not 0).  
                Properties: edit
        clearTable (bool?): Clears the contents of all the cells in the table.  
                Any procedure specified by the -gcc flag will be  
                called to populate the cleared cells  
                Properties: edit
        columnFilter (Tuple[int, str]?): Filter the specified column with the string value provided.  
                Set filter to columns 0 will apply the filter to all columns.  
                The filter is case insensitive and support wildcards.  
                Wildcard Matching: Wildcard matching is much simpler than full regexps and has only four features:  
                c	Any character represents itself apart from those mentioned below. Thus c matches the character c.  
                ?	Matches any single character. It is the same as . in full regexps.  
                *	Matches zero or more of any characters. It is the same as .* in full regexps.  
                [...]	Sets of characters can be represented in square brackets, similar to full regexps.  
                Within the character class, backslash has no special meaning.  
                (i.e. you can search for "MyValue" with "y*u" or "??Val??" or "[MyThe]Value" or any letters in "MyValue"  
                The column number is 1. based (i.e. the first row is 1 not 0).  
                Properties: create, edit
        columnWidth (Multiuse[Tuple[int, int]]?): Set the width of the specified column  
                The column number is 1. based (ie. the first column is 1 not 0).  
                Properties: create, edit, multiuse
        columns (Queryable[int]?): Set the number of columns in the table  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deleteRow (int?): Delete the specified row  
                The row number is 1. based (i.e. the first row is 1 not 0).  
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
        editable (bool?): The edit state of the table.  
                By default, this flag is set to true, and the table can be edited.  
                If false, then the table is 'read only' and cannot be typed into.  
                Properties: create, query, edit
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
        excludingHeaders (bool?): when querying the count for the rows or the columns , the number returned will not include the headers  
                Properties: query
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        getCellCmd (Callable[..., Any]?): Sets the script to call when it requires  
                the contents of a cell. The procedure is called with  
                2 integer arguments specifying the row and column for  
                which the value is required. The procedure should return  
                a string which is the value for the cell.  
                The row and column numbers passed in are 1. based  
                (ie. (1,1) is the upper left cell). The procedure should be  
                of the form:  
              
                global proc string procedureName(int $row, int $column)  
                Properties: create, edit
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        highlightColor (Queryable[Tuple[float, float, float]]?): The highlight color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query, edit
        insertRow (int?): Insert an empty row before the specified row. Any  
                procedure specified by the -gcc flag will be called to  
                populate the new new cells.  
                The row number is 1. based (i.e. the first row is 1 not 0).  
                Properties: edit
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        label (Multiuse[Tuple[int, str]]?): Set the label of the specified column.  
                The column number is 1. based (ie. the first column is 1 not 0).  
                Properties: create, edit, multiuse
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        multiEditEnabled (bool?): True: scriptTable support multi-editing function  
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
        rowHeight (Queryable[int]?): Sets the height for each row in the scriptTable  
                Properties: create, query, edit
        rows (Queryable[int]?): Set the number of rows in the table  
                Properties: create, query, edit
        rowsRemovedCmd (Callable[..., Any]?): Sets the script to call after rows are removed by pressing 'delete' or  
                'backspace' key. The procedure is called with one argument  
                specifying that selected rows have been removed.  
                The rows passed in are 1. based. The procedure should be  
                of the form:  
              
                global proc procedureName(int $rows[])  
                Properties: create, edit
        rowsToBeRemovedCmd (Callable[..., Any]?): Sets the script to call when 'delete' or 'backspace' key is  
                pressed. The procedure is called with one argument  
                specifying the selected rows to be removed. The procedure  
                should return an integer value which indicates whether the  
                selected rows should be removed (return 1 if yes, and 0 if no).  
                The rows passed in are 1. based. The procedure should be  
                of the form:  
              
                global proc int procedureName(int $rows[])  
                Properties: create, edit
        selectedCells (Queryable[List[int]]?): Select the cells or return  the cells currently selected.  
                This returns a list of indices, the first of each pair is the row, the second is the column, repeated for each cell selected  
                The returned cell numbers are 1. based (ie. the first row is 1 not 0, the first column is 1 not 0).  
                Properties: query, edit
        selectedColumns (Queryable[List[int]]?): select the columns or return the columns currently selected.  
                This returns a list of indices of each column completely selected  
                The returned column numbers are 1. based  
                Properties: query, edit
        selectedRow (bool?): The current row selected.  
                The returned row number is 1. based (ie. the first row is 1 not 0).  
                Properties: query
        selectedRows (Queryable[List[int]]?): In edit mode, select the rows given as argument.  
                In query mode, return a list of indices of completely selected rows.  
                The row numbers are 1. based  
                Properties: query, edit
        selectionBehavior (Queryable[int]?): Set the selection behavior, valid values are from 0 to 2 (inclusive)  
                0. Selecting single items.  
                1. Selecting only rows.  
                2. Selecting only columns.  
                Properties: create, query, edit
        selectionChangedCmd (Callable[..., Any]?): Sets the script to call when a complete selection  
                operation triggered by the user has occurred successfully.  
                The script does not pass any parameters and does not need to  
                return any value (i.e. It is simply a notification mechanism).  
                Properties: create, edit
        selectionMode (Queryable[int]?): Set the selection Mode, valid values are from 0 to 4 (inclusive)  
                0. Items cannot be selected.  
                1. When the user selects an item, any already-selected item becomes unselected, and the user cannot unselect the selected item by clicking on it.  
                2. When the user selects an item in the usual way, the selection status of that item is toggled and the other items are left alone. Multiple items can be toggled by dragging the mouse over them.  
                3. When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Ctrl key when clicking on an item, the clicked item gets toggled and all other items are left untouched. If the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item. Multiple items can be selected by dragging the mouse over them.  
                4. When the user selects an item in the usual way, the selection is cleared and the new item selected. However, if the user presses the Shift key while clicking on an item, all items between the current item and the clicked item are selected or unselected, depending on the state of the clicked item.  
                Properties: create, query, edit
        sortEnabled (bool?): enable scriptTable sorted by column  
                default value is false and the whole row will be sorted  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        underPointerColumn (bool?): The column under the pointer.  
                The returned column number is 1. based (i.e. the first column is 1 not 0).  
                Properties: query
        underPointerRow (bool?): The row under the pointer.  
                The returned row number is 1. based (i.e. the first row is 1 not 0).  
                Properties: query
        useDoubleClickEdit (bool?): this controls the cell edit mode  
                False: Click in the cell to select (in Row selection, the last cell of the row is edited, in Column selection, the last cell of the column is edited)(default)   
                True:  Clicked in cell is edited when double-clicked only  
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
        str: The full path name to the created script table control.

    Example:
    """

