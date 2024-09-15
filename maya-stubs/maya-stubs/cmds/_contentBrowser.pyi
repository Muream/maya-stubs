from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def contentBrowser(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addContentPath: str = ..., context: Queryable[Union[Tuple[str], Tuple[str, str], Tuple[str, str, str]]] = ..., control: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., exists: bool = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., highlightConnection: Queryable[str] = ..., location: str = ..., lockMainConnection: bool = ..., mainListConnection: Queryable[str] = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., preview: bool = ..., refreshTreeView: bool = ..., removeContentPath: str = ..., saveCurrentContext: bool = ..., selectionConnection: Queryable[str] = ..., stateString: bool = ..., thumbnailView: bool = ..., treeView: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ...) -> Union[str, Union[Tuple[str], Tuple[str, str], Tuple[str, str, str]], bool]:
    """This command is used to edit and query a Content Browser. The Content Browser is
    a unique panel, so only one instance of it can exist at a given time.
    The optional argument is the name of the control.
    Args:
        addContentPath (str?): Adds the given path(s) to the libraries displayed on the Examples tab.  
                Also updates the corresponding MAYA_CONTENT_PATH environment variable.  
                Properties: edit
        context (Queryable[Union[Tuple[str], Tuple[str, str], Tuple[str, str, str]]]?): Sets the default location for the given context. The two optional arguments  
                (Python only) are the category (tab) and location. To clear the content use  
                empty strings for category and location.  
              
                In query mode, it returns the context of the content browser in an array of 3 strings :  
                the name of the context, the default category name, the default location.  
                Properties: query, edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        filter (Queryable[str]?): Specifies the name of an itemFilter object to be used with this editor.  
                This filters the information coming onto the main list  
                of the editor.  
                Properties: create, query, edit
        forceMainConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will only  
                display items contained in the selectionConnection object. This is  
                a variant of the -mainListConnection flag in that it will force a  
                change even when the connection is locked. This flag is used to  
                reduce the overhead when using the -unlockMainConnection  
                , -mainListConnection, -lockMainConnection flags in immediate  
                succession.  
                Properties: create, query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        location (str?): Switches to the Examples tab and selects the given library location.  
                Properties: edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        preview (bool?): Shows / hides the preview panel.  
                Note: this flag will not affect the currently opened Content Browser, but only  
                any subsequently opened ones.  
                Properties: edit
        refreshTreeView (bool?): Forces a refresh of the Examples tab tree view pane.  
                Properties: edit
        removeContentPath (str?): Removes the given path(s) from the libraries displayed on the Examples tab.  
                Also updates the corresponding MAYA_CONTENT_PATH environment variable.  
                Properties: edit
        saveCurrentContext (bool?): Saves the context for the current Content Browser tab.  
                Properties: edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        thumbnailView (bool?): Shows / hides the thumbnail panel.  
                Note: this flag will not affect the currently opened Content Browser, but only  
                any subsequently opened ones.  
                Properties: edit
        treeView (bool?): Shows / hides the tree view panel.  
                Note: this flag will not affect the currently opened Content Browser, but only  
                any subsequently opened ones.  
                Properties: edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: The name of the panel

    Example:
    """

