from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def shelfTabLayout(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., borderStyle: Queryable[str] = ..., changeCommand: Callable[..., Any] = ..., childArray: bool = ..., childResizable: bool = ..., closeTab: int = ..., closeTabCommand: Callable[..., Any] = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., doubleClickCommand: Callable[..., Any] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., exists: bool = ..., fullPathName: bool = ..., generalSpacing: int = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., horizontalScrollBarThickness: int = ..., image: Queryable[str] = ..., imageVisible: bool = ..., innerMarginHeight: Queryable[int] = ..., innerMarginWidth: Queryable[int] = ..., isObscured: bool = ..., manage: bool = ..., margins: int = ..., minChildWidth: Queryable[int] = ..., moveTab: Tuple[int, int] = ..., newTabCommand: Callable[..., Any] = ..., noBackground: bool = ..., numberOfChildren: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., postMenuCommand: Callable[..., Any] = ..., preSelectCommand: Callable[..., Any] = ..., preventOverride: bool = ..., scrollable: bool = ..., scrollableTabs: bool = ..., selectCommand: Queryable[Callable[..., Any]] = ..., selectTab: Queryable[str] = ..., selectTabIndex: Queryable[int] = ..., showNewTab: bool = ..., statusBarMessage: str = ..., tabIcon: Queryable[Multiuse[Tuple[str, str]]] = ..., tabIconIndex: Queryable[Multiuse[Tuple[int, str]]] = ..., tabLabel: Queryable[Multiuse[Tuple[str, str]]] = ..., tabLabelIndex: Queryable[Multiuse[Tuple[int, str]]] = ..., tabPosition: Queryable[str] = ..., tabTooltip: Queryable[Multiuse[Tuple[str, str]]] = ..., tabTooltipIndex: Queryable[Multiuse[Tuple[int, str]]] = ..., tabsClosable: bool = ..., tabsVisible: bool = ..., useTemplate: str = ..., verticalScrollBarThickness: int = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., width: Queryable[int] = ...) -> Union[str, Tuple[float, float, float], bool, int, Callable[..., Any], Multiuse[Tuple[str, str]], Multiuse[Tuple[int, str]]]:
    """This command creates/edits/queries a shelf tab group which is essentially
    a normal tabLayout with some drop behaviour in the tab bar.  A garbage can
    icon can appear in the top right corner to dispose of buttons dragged to
    it from shelves.
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
        borderStyle (Queryable[str]?): Specify the style of the border for tab layout. Valid values are:  
                "none", "top", "notop" and "full". By default, it will use "full" to draw a simple frame  
                around the body area of the tab layout.  
              
                "none"  - Do not draw borders around the body area of the tab layout  
                "top"   - Only draw a simple line right below the tabs  
                "notop" - Draw a simple frame on the left/right/bottom (no top) of the tab layout  
                "full"  - Draw a simple frame around the body area of the tab layout  
                Properties: create, query, edit
        changeCommand (Callable[..., Any]?): Command executed when a tab is selected interactively.  
                This command is only invoked when the selected tab changes.  
                Re-selecting the current tab will not invoke this command.  
                Properties: create, edit
        childArray (bool?): Returns a string array of the names of the layout's  
                immediate children.  
                Properties: query
        childResizable (bool?): Set to true if you want the child of the control layout to be  
                as wide as the scroll area.  You may also indicate a minimum  
                width for the child using the -mcw/minChildWidth flag.  
                Properties: create, query
        closeTab (int?): Close the tab at the given index.  
                Properties: create, edit
        closeTabCommand (Callable[..., Any]?): Specify a script to be executed when one of the tabs are closed by clicking on the  
                header widget (MMB or X button).  
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
        doubleClickCommand (Callable[..., Any]?): Command executed when a tab is double clicked on.  Note  
                that the first click will select the tab and the second click  
                will execute the double click command.  Double clicking the  
                current tab will re-invoke the double click command.  
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
        generalSpacing (int?): Sets the spacing for this layout.  
                Properties: edit
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        highlightColor (Queryable[Tuple[float, float, float]]?): The highlight color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query, edit
        horizontalScrollBarThickness (int?): Thickness of the horizontal scroll bar.  Specify an  
                integer value greater than or equal to zero. This flag has  
                no effect on Windows systems.  
                Properties: create, edit
        image (Queryable[str]?): Image appearing in top right corner of tab layout.  
                Properties: create, query, edit
        imageVisible (bool?): Visibility of tab image.  
                Properties: create, query, edit
        innerMarginHeight (Queryable[int]?): Margin height for all tab children.  
                Properties: create, query
        innerMarginWidth (Queryable[int]?): Margin width for all tab children.  
                Properties: create, query
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
        minChildWidth (Queryable[int]?): Specify a positive non-zero integer value indicating the  
                minimum width the tab layout's children.  This flag only has  
                meaning when the -cr/childResizable flag is set to true.  
                Properties: create, query
        moveTab (Tuple[int, int]?): Move the tab from the current index to a new index.  
                Properties: create, edit
        newTabCommand (Callable[..., Any]?): Command executed when the 'New Tab' button (on the tab bar)  
                is clicked.  Note: in order to show the new tab button use  
                the -snt/showNewTab flag.  Using this command will  
                override any internal Maya logic for adding a new tab (only  
                this command will be executed).  
                Properties: create, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfChildren (bool?): Returns in an int the number of immediate children of the layout.  
                Properties: query
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        postMenuCommand (Callable[..., Any]?): Specify a script to be executed when the popup menu is about to be shown.  
                Properties: create, edit
        preSelectCommand (Callable[..., Any]?): Command executed when a tab is selected but before it's  
                contents become visible.  Re-selecting the current tab will not  
                invoke this command.  Note that this command is not executed by  
                using either of the -st/selectTab  
                or -sti/selectTabIndex flags.  
                Properties: create, edit
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        scrollable (bool?): Puts all children of this layout within a scroll area.  
                Properties: create, query
        scrollableTabs (bool?): If true, the active tab in the layout can be scrolled through with the mouse wheel.  
                Default is true.  
                Properties: create, query, edit
        selectCommand (Queryable[Callable[..., Any]]?): Command executed when a tab is selected interactively  This  
                command will be invoked whenever a tab is selected, ie.  
                re-selecting the current tab will invoke this command.  Note that  
                this command is not executed by using either of  
                the -st/selectTab or -sti/selectTabIndex flags.  
                Properties: create, query, edit
        selectTab (Queryable[str]?): The name, in short form, of the selected tab.  An empty  
                string is returned on query if there are no child tabs.  
                Properties: create, query, edit
        selectTabIndex (Queryable[int]?): Identical to the -st/selectTab flag except this  
                flag takes a 1. based index to identify the selected tab.  A value of  
                0 is returned on query if there are no child tabs.  
                Properties: create, query, edit
        showNewTab (bool?): Set to true if you want to have a 'New Tab' button shown at the end of  
                the tab bar.  Note: use the -ntc/newTabCommand flag to set the command  
                executed when this button is clicked.  
                Properties: create, query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        tabIcon (Queryable[Multiuse[Tuple[str, str]]]?): Set an icon for a tab.  The first argument is the name of a  
                control that must be a child of the tab layout.  The second  
                argument is the icon file name.  
                Properties: create, query, edit, multiuse
        tabIconIndex (Queryable[Multiuse[Tuple[int, str]]]?): Identical to the -ti/tabIcon flag except this  
                flag takes a 1. based index to identify the tab you want to set the  
                icon for. If this flag is queried the tab icons for all the  
                children are returned.  
                Properties: create, query, edit, multiuse
        tabLabel (Queryable[Multiuse[Tuple[str, str]]]?): Set a tab label.  The first argument is the name of a  
                control that must be a child of the tab layout.  The second  
                argument is the label for the tab associated with that child.  
                If this flag is queried then the tab labels for all the children  
                are returned.  
                Properties: create, query, edit, multiuse
        tabLabelIndex (Queryable[Multiuse[Tuple[int, str]]]?): Identical to the -tl/tabLabel flag except this  
                flag takes a 1. based index to identify the tab you want to set the  
                label for. If this flag is queried the tab labels for all the  
                children are returned.  
                Properties: create, query, edit, multiuse
        tabPosition (Queryable[str]?): Changes the tab position. The possible values are: "north", "east" and "west".  
                Properties: create, query, edit
        tabTooltip (Queryable[Multiuse[Tuple[str, str]]]?): Set a tab tooltip.  The first argument is the name of a  
                control that must be a child of the tab layout.  The second  
                argument is the tooltip for the tab associated with that child.  
                If this flag is queried then the tab tooltips for all the children  
                are returned.  
                Properties: create, query, edit, multiuse
        tabTooltipIndex (Queryable[Multiuse[Tuple[int, str]]]?): Identical to the -tt/tabTooltip flag except this  
                flag takes a 1. based index to identify the tab you want to set the  
                tooltip for. If this flag is queried the tab tooltips for all the  
                children are returned.  
                Properties: create, query, edit, multiuse
        tabsClosable (bool?): Set to true if you want to have a close button icon on all created tabs.  
                Properties: create, query
        tabsVisible (bool?): Visibility of the tab labels.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        verticalScrollBarThickness (int?): Thickness of the vertical scroll bar.  Specify an  
                integer value greater than or equal to zero. This flag has  
                no effect on Windows systems.  
                Properties: create, edit
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
        str: The name of the shelfTabLayout.

    Example:
    """

