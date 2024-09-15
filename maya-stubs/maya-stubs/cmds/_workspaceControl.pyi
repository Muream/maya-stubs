from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def workspaceControl(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., actLikeMayaUIElement: bool = ..., checksPlugins: bool = ..., close: bool = ..., closeCommand: Callable[..., Any] = ..., collapse: bool = ..., defineTemplate: str = ..., dockToControl: Tuple[str, str] = ..., dockToMainWindow: Tuple[str, bool] = ..., dockToPanel: Tuple[str, str, bool] = ..., duplicatable: bool = ..., exists: bool = ..., floating: bool = ..., height: bool = ..., heightProperty: Queryable[str] = ..., horizontal: bool = ..., initCallback: Queryable[str] = ..., initialHeight: int = ..., initialWidth: int = ..., label: Queryable[str] = ..., layoutDirectionCallback: Queryable[str] = ..., loadImmediately: bool = ..., minimumHeight: Queryable[int] = ..., minimumWidth: Queryable[int] = ..., r: bool = ..., requiredControl: Multiuse[str] = ..., requiredPlugin: Multiuse[str] = ..., resizeHeight: int = ..., resizeWidth: int = ..., restore: bool = ..., retain: bool = ..., stateString: Queryable[str] = ..., tabPosition: Queryable[Tuple[str, bool]] = ..., tabToControl: Tuple[str, int] = ..., uiScript: Callable[..., Any] = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Callable[..., Any] = ..., width: bool = ..., widthProperty: Queryable[str] = ...) -> Union[str, bool, int, Tuple[str, bool]]:
    """Creates and manages the widget used to host windows in a layout that enables docking and stacking windows together.
    Args:
        actLikeMayaUIElement (bool?): Controls whether or not this workspace control acts like Maya UI Elements such as the Shelf  
                and the Tool Box.  
              
                For example, this hides the tab bar and shows a toolbar grip on the end of the control to  
                allow undocking.  
                Properties: create, query, edit
        checksPlugins (bool?): Sets whether the UI (as defined by the uiScript) checks the loaded state of one or more plug-ins in its code.  
                The UI will not be loaded until the auto-loading of plug-ins is complete. Default value is false.  
                Properties: create, edit
        close (bool?): Closes the workspace control.  
                Properties: edit
        closeCommand (Callable[..., Any]?): Command that gets executed when the workspace control is closed.  
                Properties: create, edit
        collapse (bool?): Collapse or expand the tab widget parent of the workspace control.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        dockToControl (Tuple[str, str]?): Dock this workspace control next to the given control. The first argument is the control name,  
                the second is dock position relative to the control (valid values are: "left", "right", "top", "bottom").  
                Properties: create, edit
        dockToMainWindow (Tuple[str, bool]?): Dock this workspace control into the main window. The first argument is the dock position along the sides of  
                the main window (valid values are: "left", "right", "top", "bottom"), the second specifies whether the  
                control should be tabbed into the first control found at the dock position.  
                Properties: create, edit
        dockToPanel (Tuple[str, str, bool]?): Dock this workspace control into the workspace docking panel that the given workspace control is in. The first argument  
                is the control name, the second is dock position along the sides of the panel (valid values are: "left", "right", "top",  
                "bottom"), the third specifies whether the control should be tabbed into the first control found at the dock position.  
                Properties: create, edit
        duplicatable (bool?): Controls whether or not this workspace control can be duplicated.  
              
                The default duplicate state is controlled by whether or not the panel is unique. Unique panels cannot be  
                duplicated or copied. Workspace controls without a panel also cannot be duplicated, unless specifically  
                set as such using this flag.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        floating (bool?): Whether the workspace control is floating.  
                Properties: create, query, edit
        height (bool?): Query only flag returning the current height of the control.  
                Properties: query
        heightProperty (Queryable[str]?): Set height property of the workspace control.  
                Valid values are:  
              
                fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing  
                preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing  
                free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing  
              
                Default: free   
                In query mode returns the current height property of the workspace control.  
                Properties: create, query, edit
        horizontal (bool?): Orientation of the control. This flag is true by default, which corresponds to a horizontally oriented widget.  
              
                Note: currently only "Toolbox" and "Shelf" support a vertical orientation.  
                Properties: create, query, edit
        initCallback (Queryable[str]?): Adds a mel command to be executed when the control is added to the layout.  
                The command should be a mel proc and it will be called with the workspaceControl name as parameter.  
                The mel command should take the form:  
              
                global proc callbackName(string $workspaceControlName)  
              
                If "save" is appended to the command name, it will be called during the layout save.  
              
                global proc callbackNameSave(string $workspaceControlName)  
                Properties: create, query, edit
        initialHeight (int?): The initial height of the workspace control when first shown.  
                Properties: create, edit
        initialWidth (int?): The initial width of the workspace control when first shown.  
                Properties: create, edit
        label (Queryable[str]?): The label text. The default label is the name of the workspace control.  
                Properties: create, query, edit
        layoutDirectionCallback (Queryable[str]?): Set a mel procedure to be called when the control changes orientation. The procedure is  
                called with argument 1 for horizontal and 0 for vertical.  
                Properties: create, query, edit
        loadImmediately (bool?): Sets whether the UI (as defined by the uiScript) will be built immediately on workspace control  
                creation (true) or delayed until the control is actually shown (false). Default value is false.  
                Properties: create, edit
        minimumHeight (Queryable[int]?): Sets the minimum height of control to the given value.  
              
                If given value is 0 (False), minimum height is set to 0.  
                If given value is 1 (True), minimum height is set to initial height.  
                If given value is greater than 1, minimum height is set to the given value.  
              
                In query mode returns current minimum height of the control.  
                Properties: create, query, edit
        minimumWidth (Queryable[int]?): Sets the minimum width of control to the given value.  
                This flag parameter was changed from bool to int in 2018 and old settings are still respected according to the following.  
              
                If given value is 0 (False), minimum width is set to 0.  
                If given value is 1 (True), minimum width is set to initial width.  
                If given value is greater than 1, minimum width is set to the given value.  
              
                In query mode returns current minimum width of the control.  
                Properties: create, query, edit
        r (bool?): Raises a workspace control to the top and makes it active.  
                In Query mode, this flag will return whether the workspace control is active or not.  
                Note that this flag won't raise a control if is minimized or collapsed. Use the flag -rs/restore instead.  
                Properties: query, edit
        requiredControl (Multiuse[str]?): The name of a workspace control that needs to be open in order for this workspace control to properly function.  
                This workspace control will not be created if the required control is not open, and will be closed when the  
                required control is closed.  
                Properties: create, edit, multiuse
        requiredPlugin (Multiuse[str]?): The name of a plug-in that needs to be loaded in order to build the workspace control UI.  
                Properties: create, edit, multiuse
        resizeHeight (int?): Resizes a floating workspace control's height to the given value.  
                Properties: edit
        resizeWidth (int?): Resizes a floating workspace control's width to the given value.  
                Properties: edit
        restore (bool?): Restores the control according to the following rules:  
              
                If collapsed then the control will be expanded  
                If hidden then the control will be shown  
                If minimized then the control will be restored  
                If the control is an inactive tab into a tab group then it will become the active tab  
                Properties: create, edit
        retain (bool?): Sets whether the workspace control is retained (i.e. only hidden) or deleted when closed. Default value is true.  
                Properties: create
        stateString (Queryable[str]?): String containing the state of the control.  
                Can be used with the initCallback flag.  
                Properties: create, query, edit
        tabPosition (Queryable[Tuple[str, bool]]?): Changes the tab position. The possible values are: "north", "east" and "west".  
                The boolean value, if set to true, changes the tab positions of all the controls in the parent widget.  
                If it is not set, only the current control will get its position changed.  
                A control can have a different orientation than the tab widget.  
                If the control tab position is different from the tab widget's one, the tab position will be changed when the control becomes the only control in the tab widget.  
                On query, only the control's tab position will be returned, not the tab widget's position. They may differ.  
                Properties: create, query, edit
        tabToControl (Tuple[str, int]?): Tab this workspace control into the given control. The first argument is the control name,  
                the second is the index position within the containing tab widget (invalid values mean append).  
                Properties: create, edit
        uiScript (Callable[..., Any]?): The specified script will be invoked to build the UI of the workspaceControl.  This is a required flag.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        visible (bool?): The visible state of the workspace control. A control is created visible by default.  
                If the control is created as not visible, the control will be created in a closed state.  
                To make it appear, edit the control to set the flags floating or the flag visible to true.  
                Use -r/raise flag to get the active status of a control as this flag will return true when the control  
                is minimized or collapsed.  
                Properties: create, query, edit
        visibleChangeCommand (Callable[..., Any]?): Command that gets executed when visible state of the workspace control changes.  
                Properties: create, edit
        width (bool?): Query only flag returning the current width of the control.  
                Properties: query
        widthProperty (Queryable[str]?): Set width property of the workspace control.  
                Valid values are:  
              
                fixed	  - Cannot be resized manually and will not be given any extra space while maximizing/dynamically resizing  
                preferred - Can be resized manually but will not be given any extra space while maximizing/dynamically resizing  
                free	  - Can be resized manually and will be given extra space while maximizing/dynamically resizing  
              
                Default: free   
                In query mode returns the current width property of the workspace control.  
                Properties: create, query, edit

    Returns:
        str: Full path name to the control.

    Example:
    """

