from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def clipEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allTrackHeights: int = ..., autoFit: Queryable[str] = ..., autoFitTime: Queryable[str] = ..., clipDropCmd: str = ..., clipStyle: Queryable[int] = ..., control: bool = ..., defineTemplate: str = ..., deleteCmd: str = ..., deselectAll: bool = ..., displayActiveKeyTangents: str = ..., displayActiveKeys: str = ..., displayInfinities: str = ..., displayKeys: str = ..., displayTangents: str = ..., displayValues: str = ..., docTag: Queryable[str] = ..., exists: bool = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., frameAll: bool = ..., frameRange: Queryable[Tuple[float, float]] = ..., highlightConnection: Queryable[str] = ..., highlightedBlend: Queryable[Tuple[str, str]] = ..., highlightedClip: Queryable[Tuple[str, str]] = ..., initialized: bool = ..., listAllCharacters: bool = ..., listCurrentCharacters: bool = ..., lockMainConnection: bool = ..., lookAt: str = ..., mainListConnection: Queryable[str] = ..., manageSequencer: bool = ..., menuContext: Queryable[str] = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., selectBlend: Queryable[Tuple[str, str, str]] = ..., selectClip: Queryable[Tuple[str, str]] = ..., selectionConnection: Queryable[str] = ..., snapTime: Queryable[str] = ..., snapValue: Queryable[str] = ..., stateString: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ...) -> Union[str, int, bool, Tuple[float, float], Tuple[str, str], Tuple[str, str, str]]:
    """Create a clip editor with the given name.
    Args:
        allTrackHeights (int?): OBSOLETE flag. Use clipStyle instead.
        autoFit (Queryable[str]?): on | off | tgl  
                Auto fit-to-view.  
                Properties: query, edit
        autoFitTime (Queryable[str]?): on | off | tgl  
                Auto fit-to-view along the time axis, as well.  
                Properties: query, edit
        clipDropCmd (str?): Command executed when clip node is dropped on the TraX editor  
                Properties: edit
        clipStyle (Queryable[int]?): Set/return the clip track style in the specified editor. Default is 2. Valid values are 1. 3.  
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
        deleteCmd (str?): Command executed when backspace key is pressed  
                Properties: edit
        deselectAll (bool?): Deselect all clips and blends in the editor.  
                Properties: edit
        displayActiveKeyTangents (str?): on | off | tgl  
                Display active key tangents in the editor.  
                Properties: edit
        displayActiveKeys (str?): on | off | tgl  
                Display active keys in the editor.  
                Properties: edit
        displayInfinities (str?): on | off | tgl  
                Display infinities in the editor.  
                Properties: edit
        displayKeys (str?): on | off | tgl  
                Display keyframes in the editor.  
                Properties: edit
        displayTangents (str?): on | off | tgl  
                Display tangents in the editor.  
                Properties: edit
        displayValues (str?): on | off | tgl  
                Display active keys and tangents values in the editor.  
                Properties: edit
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
        frameAll (bool?): Frame view around all clips in the editor.  
                Properties: edit
        frameRange (Queryable[Tuple[float, float]]?): The editor's current frame range.  
                Properties: query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        highlightedBlend (Queryable[Tuple[str, str]]?): Returns the highlighted blend, listed as scheduler and index  
                Properties: query
        highlightedClip (Queryable[Tuple[str, str]]?): Returns the highlighted clip, listed as scheduler and index  
                Properties: query
        initialized (bool?): Returns whether the clip editor is fully initialized, and has a port to draw through.  
                If not, the -frameRange and -frameAll flags will fail.  
                Properties: query
        listAllCharacters (bool?): List all characters in the editor and outliner.  
                Properties: edit
        listCurrentCharacters (bool?): List only the characters in the editor and outliner.  
                Properties: edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        lookAt (str?): all | selected | currentTime  
                FitView helpers.  
                Properties: edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        manageSequencer (bool?): Sets/returns whether the clip editor should manage sequencer nodes.  If so,  
                animation clips and characters are not represented.  
                Properties: create, query, edit
        menuContext (Queryable[str]?): Returns a string array denoting the type of data object the cursor  
                is over.  Returned values are:  
                {"timeSlider"}  
                {"nothing"}  
                {"track", "track index", "character node name", "group name"}  
                {"clip", "clip node name"}  
                Properties: query
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        selectBlend (Queryable[Tuple[str, str, str]]?): Select the blends specified by the scheduler name and the indicies  
                of the two clips used in the blend.  
                When queried, a string containing the scheduler name and the  
                two clip indicies for all of the selected blends is returned.  
                Properties: query, edit
        selectClip (Queryable[Tuple[str, str]]?): Selects the clip specified by the scheduler name and the clip index.  
                When queried, a string containing the scheduler and clip index  
                of all of the selected clips is returned.  
                Properties: query, edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        snapTime (Queryable[str]?): none | integer | keyframe  
                Keyframe move snap in time.  
                Properties: query, edit
        snapValue (Queryable[str]?): none | integer | keyframe  
                Keyframe move snap in values.  
                Properties: query, edit
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
        str: Editor name

    Example:
    """

