from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def gridLayout(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowEmptyCells: bool = ..., annotation: Queryable[str] = ..., autoGrow: bool = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., cellHeight: Queryable[int] = ..., cellWidth: Queryable[int] = ..., cellWidthHeight: Tuple[int, int] = ..., childArray: bool = ..., columnsResizable: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., generalSpacing: int = ..., gridOrder: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., manage: bool = ..., margins: int = ..., noBackground: bool = ..., numberOfChildren: bool = ..., numberOfColumns: Queryable[int] = ..., numberOfPopupMenus: bool = ..., numberOfRows: Queryable[int] = ..., numberOfRowsColumns: Tuple[int, int] = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., position: Multiuse[Tuple[str, int]] = ..., preventOverride: bool = ..., statusBarMessage: str = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, Callable[..., Any]]:
    """This layout arranges children in a grid fashion where every
    cell in the grid is the same size.  You may specify the number
    of rows and columns as well as the width and height of the grid
    cells.
    Args:
        allowEmptyCells (bool?): Specify true if you want free positioning of the children  
                in the layout and potentially leaving empty cells between children.  
                Set to false if you want the children to always be packed together.  
                The default is true.  
                Properties: create, query
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        autoGrow (bool?): Specify true if you want the grid layout size to grow as  
                children are added.  For example, if the grid layout has 2 columns  
                and 2 rows then adding a fifth child will cause the grid to expand  
                to 3 rows if this flag is true, otherwise the grid will remain the  
                same size and the new child will be hidden from view until you  
                expand the size of the grid using the appropriate flags.  The  
                default is true.  
                Properties: create, query
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        cellHeight (Queryable[int]?): A positive non-zero integer value indicating the height  
                of cells in the grid layout.  
                Properties: create, query, edit
        cellWidth (Queryable[int]?): A positive non-zero integer value indicating the width  
                of cells in the grid layout.  
                Properties: create, query, edit
        cellWidthHeight (Tuple[int, int]?): Two positive non-zero integer values for indicating the  
                width and height, respectively, of the cells in the grid layout.  
                Properties: create, edit
        childArray (bool?): Returns a string array of the names of the layout's  
                immediate children.  
                Properties: query
        columnsResizable (bool?): Specify true if you want the number of columns to adjust  
                according to the width of the layout.  Set to false if you want  
                the number of columns to remain fixed when the width of the  
                layout is changed.  The default is false.  
                Properties: create, query
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
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        generalSpacing (int?): Sets the spacing for this layout.  
                Properties: edit
        gridOrder (bool?): As opposed to the childArray flag, the gridOrder flag  
                returns the children of the grid Layout in the order they  
                are diplayed in the window.  
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
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        margins (int?): Sets the content margins for this layout.  
                Properties: edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfChildren (bool?): Returns in an int the number of immediate children of the layout.  
                Properties: query
        numberOfColumns (Queryable[int]?): A positive non-zero integer value indicating the number  
                of columns in the grid layout.  
                Properties: create, query, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        numberOfRows (Queryable[int]?): A positive non-zero integer value indicating the number  
                of rows in the grid layout.  
                Properties: create, query, edit
        numberOfRowsColumns (Tuple[int, int]?): Two positive non-zero integer values for the number  
                of rows and columns, respectively, in the grid layout.  
                Properties: create, edit
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        position (Multiuse[Tuple[str, int]]?): Specify the name of a child control in the grid layout along  
                with a 1. based integer value indicating the desired  
                position of the child.  Positions increase from left to right  
                within a row and then wrap around to the next row increasing from  
                top to bottom.  For example, a grid layout with 3 columns and 2  
                rows has 6 visible positions where 1, 2 and 3 occupy the first row  
                and 4, 5 and 6 occupy the second.  
                Properties: create, edit, multiuse
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
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
        str: Full path name to the control.

    Example:
    """

