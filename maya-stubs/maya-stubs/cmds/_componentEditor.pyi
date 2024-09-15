from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def componentEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., control: bool = ..., defineTemplate: str = ..., docTag: Queryable[str] = ..., exists: bool = ..., filter: Queryable[str] = ..., floatField: Queryable[str] = ..., floatSlider: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., hidePathName: bool = ..., hideZeroColumns: bool = ..., highlightConnection: Queryable[str] = ..., justifyHeaders: Queryable[int] = ..., lockInput: bool = ..., lockMainConnection: bool = ..., mainListConnection: Queryable[str] = ..., newTab: Tuple[str, str, str] = ..., normalizeWeights: int = ..., operationCount: bool = ..., operationLabels: bool = ..., operationType: Queryable[int] = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., precision: Queryable[int] = ..., removeTab: str = ..., selected: bool = ..., selectionConnection: Queryable[str] = ..., setOperationLabel: Tuple[int, str] = ..., showNamespaces: bool = ..., showObjects: bool = ..., showSelected: bool = ..., sortAlpha: bool = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ...) -> Union[str, bool, int]:
    """This command creates a new component editor
    in the current layout.
    Args:
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
        floatField (Queryable[str]?): assigns a float field that the component editor will  
                use for editing groups of values.  
                Properties: create, query, edit
        floatSlider (Queryable[str]?): assigns a float slider that the component editor will  
                use for editing groups of values.  
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
        hidePathName (bool?): Hides path name of displayed element.  By default  
                this flag is set to false.  
                Properties: create, query, edit
        hideZeroColumns (bool?): Hides columns whose elements are all zero.  By default  
                this flag is set to false.  
                Properties: create, query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        justifyHeaders (Queryable[int]?): Set justification mode for headers of columns.  Possible values  
                are 0 (right justify), or 1 (left justify). By default  
                this flag is set to 0.  
                Properties: create, query, edit
        lockInput (bool?): Prevents the editor from responding to changes in  
                the active list. Independent of selection connection.  
                Properties: create, query, edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        newTab (Tuple[str, str, str]?): Creates a new tab, named by the first argument, based on an existing tab, given as the second argument  
                using elements from a set, given in the third argument  
                Properties: create, edit
        normalizeWeights (int?): Specifies automatic normalization mode of skin clusters. Can be 0, meaning "None", or 1,  
                meaning "Interactive", or 2, meaning "Post". It corresponds to the "normalizeWeights" attribute  
                of skinCluster node.  
                Properties: edit
        operationCount (bool?): returns the total number of operation types  
                known to the component editor.  
                Properties: query
        operationLabels (bool?): returns a string array containing the names for all  
                operation types known to the editor.  
                Properties: query
        operationType (Queryable[int]?): Tells the editor which of its known operation types  
                it should be performing. This is a 0. based index.  
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
        removeTab (str?): Removes the tab based on the set provided  
                Properties: edit
        selected (bool?): Returns a list of strings, containing the labels of the currently selected columns  
                Properties: query
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        setOperationLabel (Tuple[int, str]?): uses the string as the new name for the existing operation type  
                specified by the integer index. Note that there is no messaging  
                system which allows UI to be informed of changes made by this flag.  
                Properties: edit
        showNamespaces (bool?): Show the namespaces for objects, if any.  By default  
                this flag is set to true.  
                Properties: create, query, edit
        showObjects (bool?): Restricts the display to columns that are in the current active list.  
                Properties: create
        showSelected (bool?): Restricts the display to those columns which are currently selected. By default  
                this flag is set to false, so all columns are selected. The results from this flag  
                obey the current -hideZeroColumns setting.  
                Properties: create, edit
        sortAlpha (bool?): Controls alphabetical (true), or hierarchical sorting of columns  
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
        str: The panel name

    Example:
    """

