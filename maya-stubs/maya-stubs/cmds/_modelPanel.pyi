from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def modelPanel(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., barLayout: bool = ..., camera: Queryable[str] = ..., control: bool = ..., copy: str = ..., createString: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., editString: bool = ..., exists: bool = ..., init: bool = ..., isUnique: bool = ..., label: Queryable[str] = ..., menuBarRepeatLast: bool = ..., menuBarVisible: bool = ..., modelEditor: bool = ..., needsInit: bool = ..., parent: str = ..., popupMenuProcedure: Queryable[Callable[..., Any]] = ..., replacePanel: str = ..., tearOff: bool = ..., tearOffCopy: str = ..., tearOffRestore: bool = ..., unParent: bool = ..., useTemplate: str = ...) -> Union[str, bool, Callable[..., Any]]:
    """This command creates a panel consisting of a model editor. See
    thecommand documentation for more information.
    Args:
        barLayout (bool?): This flag returns the name of the layout which is the parent of  
                the panels icon bar.  
                Properties: query
        camera (Queryable[str]?): Query or edit the camera in a modelPanel.  
                Properties: query, edit
        control (bool?): Returns the top level control for this panel.  
                Usually used for getting a parent to attach popup menus.  
                CAUTION: panels may not have controls at times.  This  
                flag can return "" if no control is present.  
                Properties: query
        copy (str?): Makes this panel a copy of the specified panel.  Both  
                panels must be of the same type.  
                Properties: edit
        createString (bool?): Command string used to create a panel  
                Properties: edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        docTag (Queryable[str]?): Attaches a tag to the Maya panel.  
                Properties: create, query, edit
        editString (bool?): Command string used to edit a panel  
                Properties: edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        init (bool?): Initializes the panel's default state.  This is usually done  
                automatically on file -new and file -open.  
                Properties: create, edit
        isUnique (bool?): Returns true if only one instance of this panel type is allowed.  
                Properties: query
        label (Queryable[str]?): Specifies the user readable label for the panel.  
                Properties: query, edit
        menuBarRepeatLast (bool?): Controls whether clicking on the menu header with the middle mouse button would repeat the last selected menu item.  
                Properties: create, query, edit
        menuBarVisible (bool?): Controls whether the menu bar for the panel is displayed.  
                Properties: create, query, edit
        modelEditor (bool?): This flag returns the name of the model editor  
                contained by the panel.  
                Properties: query
        needsInit (bool?): (Internal) On Edit will mark the panel as requiring initialization.  
                Query will return whether the panel is marked for initialization.  Used  
                during file -new and file -open.  
                Properties: query, edit
        parent (str?): Specifies the parent layout for this panel.  
                Properties: create
        popupMenuProcedure (Queryable[Callable[..., Any]]?): Specifies the procedure called for building the panel's popup menu(s).  
                The default value is "buildPanelPopupMenu".  The procedure should take  
                one string argument which is the panel's name.  
                Properties: query, edit
        replacePanel (str?): Will replace the specified panel with this panel.  If the  
                target panel is within the same layout it will perform a swap.  
                Properties: edit
        tearOff (bool?): Will tear off this panel into a separate window with a paneLayout  
                as the parent of the panel. When queried this flag will return if the  
                panel has been torn off into its own window.  
                Properties: query, edit
        tearOffCopy (str?): Will create this panel as a torn of copy of the specified source panel.  
                Properties: create
        tearOffRestore (bool?): Restores panel if it is torn off and focus is given to it.  
                If docked, becomes the active panel in the docked window.  
                This should be the default flag that is added to all panels  
                instead of -to/-tearOff flag which should only be used to tear off the panel.  
                Properties: create, edit
        unParent (bool?): Specifies that the panel should be removed from its layout.  
                This (obviously) cannot be used with query.  
                Properties: edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: The name of the panel.

    Example:
    """

