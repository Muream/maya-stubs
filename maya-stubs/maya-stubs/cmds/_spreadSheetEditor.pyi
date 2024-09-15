from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def spreadSheetEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allAttr: bool = ..., attrRegExp: Queryable[str] = ..., control: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., execute: str = ..., exists: bool = ..., filter: Queryable[str] = ..., fixedAttrList: Queryable[List[str]] = ..., forceMainConnection: Queryable[str] = ..., highlightConnection: Queryable[str] = ..., keyableOnly: bool = ..., lockMainConnection: bool = ..., longNames: bool = ..., mainListConnection: Queryable[str] = ..., niceNames: bool = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., precision: Queryable[int] = ..., selectedAttr: bool = ..., selectionConnection: Queryable[str] = ..., showShapes: bool = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ...) -> Union[str, bool, List[str], int]:
    """This command creates a new spread sheet editor in the
    current layout.
    Args:
        allAttr (bool?): Returns a list of all the attribute names  
                currently being displayed.  This flag is ignored when not being queried.  
                Properties: query
        attrRegExp (Queryable[str]?): Filter the current displayed attribute names.  
                This expression matches the case-insensitive substring of attribute names.  
                Properties: create, query, edit
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
        execute (str?): Immediately executes the command string once for every selected  
                cell in the spreadSheet.  Before the command is executed, "#A" is  
                substituted with the name of the cell's attribute, "#N" is substituted  
                with the name of the cell's node, and "#P" is substituted with the  
                full path name of the node.  
                Properties: edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        filter (Queryable[str]?): Specifies the name of an itemFilter object to be used with this editor.  
                This filters the information coming onto the main list  
                of the editor.  
                Properties: create, query, edit
        fixedAttrList (Queryable[List[str]]?): Forces the editor to only display attributes with the  
                specified names.  
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
        keyableOnly (bool?): Limits the displayed attributes to be those that are keyable.  
                True by default  
                Properties: create, query, edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        longNames (bool?): Controls whether the attributes are displayed using their  
                long names or their short names.  
                Properties: create, query, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        niceNames (bool?): Controls whether the attribute names will be displayed in  
                a more user-friendly, readable way.  When this is on, the longNames  
                flag is ignored.  When this is off, attribute names will be displayed  
                either long or short, according to the longNames flag.  
                Default is on. Queried, returns a boolean.  
                Properties: create, query, edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        precision (Queryable[int]?): Specifies the maximum number of digits displayed to the right  
                of the decimal place.  Can be 0 to 20.  
                Properties: create, query, edit
        selectedAttr (bool?): Returns a list of all the attribute names  
                that are selected.  This flag is ignored when not being queried.  
                Properties: query
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        showShapes (bool?): If true, when transforms are selected their shapes will  
                be displayed instead.  
                Properties: create, query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
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
        str: The name of the editor

    Example:
    """

