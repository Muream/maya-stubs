from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def scriptedPanelType(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addCallback: Queryable[str] = ..., copyStateCallback: Queryable[str] = ..., createCallback: Queryable[str] = ..., customView: bool = ..., defineTemplate: str = ..., deleteCallback: Queryable[str] = ..., exists: bool = ..., hotkeyCtxClient: Queryable[str] = ..., initCallback: Queryable[str] = ..., label: Queryable[str] = ..., obsolete: bool = ..., removeCallback: Queryable[str] = ..., retainOnFileOpen: bool = ..., saveStateCallback: Queryable[str] = ..., unique: bool = ..., useTemplate: str = ...) -> Union[str, bool]:
    """This command defines the callbacks for a type of scripted panel.  The panel type
    created by this command is then used when creating a scripted panel.  See also
    the 'scriptedPanel' command.
    Args:
        addCallback (Queryable[str]?): This flag specifies the callback procedure for adding the panel  
                to a particular control layout.  The parent layout is guaranteed to be  
                the current default layout when the proc is called.  If its name is  
                required then it can be queried with 'setParent -q'.  Any editors should  
                be parented here.  
                global proc procName (string $panelName) { .... }  
                Properties: create, query, edit
        copyStateCallback (Queryable[str]?): This flag specifies the callback procedure for copying the state of  
                the panel when a tear-off copy of the panel is made.  The callback proc has the form:  
                global proc procName (string $panelName, string $newPanelName) { .... }  
                This procedure will be executed immediately after the addCallback  
                procedure has finished executing. At that point, the copied panel will be  
                fully created and accessible to facilitate copying of panel settings.  
                Note: the addCallback procedure is called after the createCallback  
                procedure has been called.  
                Properties: create, query, edit
        createCallback (Queryable[str]?): This flag specifies the callback procedure for initially creating  
                the panel object.  No UI should be created here.  Any editors owned  
                by the panel should be created here unparented.  
                The callback proc has the form:  
                global proc procName (string $panelName) { .... }  
                Properties: create, query, edit
        customView (bool?): This flag specifies if this view is a custom 3d view for  
                MPx3dModelView types. This flag should only be used for  
                MPx3dModelView types.  
                Properties: create, query, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deleteCallback (Queryable[str]?): This flag specifies the callback procedure for final deletion of  
                the panel.  The callback proc has the form:  
                global proc procName (string $panelName) { .... }  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        hotkeyCtxClient (Queryable[str]?): This flag is used to specify the name of the hotkey context client for this panel type.  
                By default, it is the same as the panel type.  
                Properties: create, query, edit
        initCallback (Queryable[str]?): This flag specifies the callback procedure for the initialize  
                callback.  This will be called on file -new and file -open to give the  
                panel an opportunity to re-initialize to a starting state, if required.  
                The panel may be parented or unparented at this time.  
                The callback proc has the form:  
                global proc procName (string $panelName) { .... }  
                Properties: create, query, edit
        label (Queryable[str]?): Label for the panel  
                Properties: create, query, edit
        obsolete (bool?): This flag specifies that this type is no longer used in Maya.  
                Properties: create, query, edit
        removeCallback (Queryable[str]?): This flag specifies the callback procedure for removing the panel  
                from its current control layout.  Any editors should be unparented here.  
                The callback proc has the form:  
                global proc procName (string $panelName) { .... }  
                Properties: create, query, edit
        retainOnFileOpen (bool?): This flag specifies if panels of this type should be retained after  
                restoring panel cofiguration during file open. Default value is false.  
                Properties: create, query, edit
        saveStateCallback (Queryable[str]?): This flag specifies the callback procedure for saving the state of  
                the panel.  The callback proc has the form:  
                global proc string procName (string $panelName) { .... }  
                Note that the proc returns a string.  This string will be executed after  
                the createCallback has been called to facilitate restoring the panel  
                state.  
                Properties: create, query, edit
        unique (bool?): This flag specifies if only one instance of this type of panel can exist  
                at a given time.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: The name of the scripted panel type.

    Example:
    """

