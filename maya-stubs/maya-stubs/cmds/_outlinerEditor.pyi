from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def outlinerEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., allowMultiSelection: bool = ..., alwaysToggleSelect: bool = ..., animLayerFilterOptions: Queryable[str] = ..., attrAlphaOrder: Queryable[str] = ..., attrFilter: Queryable[str] = ..., autoExpand: bool = ..., autoExpandAllAnimatedShapes: bool = ..., autoExpandAnimatedShapes: bool = ..., autoExpandLayers: bool = ..., autoSelectNewObjects: bool = ..., containersIgnoreFilters: bool = ..., control: bool = ..., defineTemplate: str = ..., directSelect: bool = ..., displayMode: Queryable[str] = ..., doNotSelectNewObjects: bool = ..., docTag: Queryable[str] = ..., dropIsParent: bool = ..., editAttrName: bool = ..., exists: bool = ..., expandAllItems: bool = ..., expandAllSelectedItems: bool = ..., expandAttribute: bool = ..., expandConnections: bool = ..., expandObjects: bool = ..., feedbackItemName: bool = ..., feedbackRowNumber: bool = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., getCurrentSetOfItem: Queryable[int] = ..., highlightActive: bool = ..., highlightConnection: Queryable[str] = ..., highlightSecondary: bool = ..., ignoreDagHierarchy: bool = ..., ignoreHiddenAttribute: bool = ..., ignoreOutlinerColor: bool = ..., isChildSelected: Queryable[str] = ..., isSet: Queryable[int] = ..., isSetMember: Queryable[int] = ..., isUfeItem: Queryable[int] = ..., lockMainConnection: bool = ..., longNames: bool = ..., mainListConnection: Queryable[str] = ..., mapMotionTrails: bool = ..., masterOutliner: Queryable[str] = ..., niceNames: bool = ..., object: Queryable[str] = ..., organizeByClip: bool = ..., organizeByLayer: bool = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., parentObject: bool = ..., pinPlug: Queryable[str] = ..., refresh: bool = ..., removeFromCurrentSet: int = ..., renameItem: int = ..., renameSelectedItem: bool = ..., renderFilterActive: bool = ..., renderFilterIndex: Queryable[int] = ..., renderFilterVisible: bool = ..., selectCommand: Queryable[Callable[..., Any]] = ..., selectionConnection: Queryable[str] = ..., selectionOrder: str = ..., setFilter: Queryable[str] = ..., setsIgnoreFilters: bool = ..., showAnimCurvesOnly: bool = ..., showAnimLayerWeight: bool = ..., showAssets: bool = ..., showAssignedMaterials: bool = ..., showAttrValues: bool = ..., showAttributes: bool = ..., showCompounds: bool = ..., showConnected: bool = ..., showContainedOnly: bool = ..., showContainerContents: bool = ..., showDagOnly: bool = ..., showLeafs: bool = ..., showMuteInfo: bool = ..., showNamespace: bool = ..., showNumericAttrsOnly: bool = ..., showParentContainers: bool = ..., showPinIcons: bool = ..., showPublishedAsConnected: bool = ..., showReferenceMembers: bool = ..., showReferenceNodes: bool = ..., showSelected: bool = ..., showSetMembers: bool = ..., showShapes: bool = ..., showTextureNodesOnly: bool = ..., showTimeEditor: bool = ..., showUVAttrsOnly: bool = ..., showUfeItems: bool = ..., showUnitlessCurves: bool = ..., showUpstreamCurves: bool = ..., sortOrder: Queryable[str] = ..., stateString: bool = ..., transmitFilters: bool = ..., ufeFilter: Queryable[Tuple[str, str]] = ..., ufeFilterValue: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., unpinPlug: str = ..., updateMainConnection: bool = ..., useTemplate: str = ...) -> Union[str, bool, int, Callable[..., Any], Tuple[str, str]]:
    """This command creates an outliner editor which can be used to display a list
    of objects.WARNING: some flag combinations may not behave as you expect.  The command
    is really intended for internal use for creating the outliner used by
    the various editors.
    Args:
        allowMultiSelection (bool?): If true then multiple selection will be allowed in the outliner.  
                Properties: create, edit
        alwaysToggleSelect (bool?): If true, then clicking on an item in the outliner will select or  
                deselect it without affecting the selection of other items (unless  
                allowMultiSelection is false). If false, clicking on an item in the  
                outliner will replace the current selection with the selected item.  
                Properties: create, edit
        animLayerFilterOptions (Queryable[str]?): Specifies whether a filter is to be applied when displaying animation layers.  
                If so, the options can be "allAffecting" (no filter), "active" (only the active  
                layers on the object will be displayed) and "animLayerEditor" (the settings will  
                be taken from the animation layer editor).  
                Properties: create, query, edit
        attrAlphaOrder (Queryable[str]?): Specify how attributes are to be sorted. Current recognised values  
                are "default" for no sorting and "ascend" to sort attributes from 'a' to ''z' and  
                "descend" to sort from 'z' to 'a'.  
                Notes: a) this only applies to top level attributes.  
                Properties: create, query, edit
        attrFilter (Queryable[str]?): Specifies the name of an itemFilter object to be placed on this editor.  
                This filters the attributes displayed in the editor.  
                Properties: create, query, edit
        autoExpand (bool?): This flag specifies whether or not objects that are loaded  
                in should have their attributes automatically expanded.  
                Properties: create, query, edit
        autoExpandAllAnimatedShapes (bool?): This flag controls whether or not all levels in the outliner's  
                DAG hierachy are expanded when looking for animated shapes.  When  
                set to false, the outliner expands only the top level of the hieararchy.  
                This flag is enabled by default and has no effect if autoExpand is  
                disabled or autoExpandAnimatedShapes is disabled.  
                Properties: create, query, edit
        autoExpandAnimatedShapes (bool?): This flag specifies whether or not DAG objects that have animated  
                shapes should be automatically expanded to show the shape. This flag  
                is enabled by default and has no effect if autoExpand is disabled.  
                Properties: create, query, edit
        autoExpandLayers (bool?): If true then when a node with animation layer is displayed, all  
                the animation layers will show up in expanded form.  
                Properties: create, query, edit
        autoSelectNewObjects (bool?): This flag specifies whether or not new objects added to the outliner  
                should be automatically selected.  
                Properties: create, query, edit
        containersIgnoreFilters (bool?): This flag specifices whether or not filters should be ignored  
                when displaying container contents.  
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
        directSelect (bool?): If true then clicking on an item in the outliner will add or  
                remove just that item from the selection connection. If false then  
                clicking on an item in the outliner causes the selection connection  
                to be reloaded with the currently selected items in the outliner.  
                Properties: create, edit
        displayMode (Queryable[str]?): Affects how the outliner displays when a filter is applied. List mode  
                is a non-indented flat list. DAG mode indents to represent the  
                hierarchical structure of the model.  
                Properties: create, query, edit
        doNotSelectNewObjects (bool?): If true this flag specifies that new objects added to the outliner  
                will not be selected, even if they are active.  
                Properties: create, query, edit
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        dropIsParent (bool?): This flag specifies the mode for drag and drop. If the flag is true,  
                dropping items will do a reparent. If it is false, dropping will  
                reorder items. By default, the flag is true (parent).  
                Properties: create, query, edit
        editAttrName (bool?): This flag specifies whether or not attribute names can be edited.  
                By default double-clicking on an attribute will open the expression  
                editor for that attribute.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        expandAllItems (bool?): Expand or collapse all items in the outliner.  
                Properties: create, edit
        expandAllSelectedItems (bool?): Expand or collapse all selected items in the outliner.  
                Properties: create, edit
        expandAttribute (bool?): Force the outliner to fill the selection list with only attributes.  
                Properties: edit
        expandConnections (bool?): This flag specifies whether or not attributes should be  
                expanded to show their input connections.  
                Note: currently the expansion will only show animCurves.  
                Properties: create, query, edit
        expandObjects (bool?): This flag specifies whether or not objects that are loaded  
                in should be automatically expanded.  
                Properties: create, query, edit
        feedbackItemName (bool?): Returns the outliner item name at the current mouse position, if any.  
                Properties: query
        feedbackRowNumber (bool?): Returns the outliner row number at the current mouse position, if any.  
                Properties: query
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
        getCurrentSetOfItem (Queryable[int]?): Returns the current set of item at the given row. As an item can belong to number of sets, current set is the set to which the item belongs to currently.  
                Properties: query
        highlightActive (bool?): This flag specifies whether or not the outliner should highlight  
                objects that are active.  
                Note: if the outliner is driving the contents of another editor,  
                setting highlightActive to true may produce unexpected behavior.  
                Properties: create, query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        highlightSecondary (bool?): This flag specifies whether or not the outliner should highlight objects  
                that are contained in the highlightConnection.  
                Properties: create, query, edit
        ignoreDagHierarchy (bool?): This flag specifies whether or not DAG objects are displayed  
                in their DAG hierarchy. Warning: using this flag without  
                some other form of sensible filtering will lead to a very  
                confusing outliner.  
                Properties: create, query, edit
        ignoreHiddenAttribute (bool?): Sets whether or not the outliner ignores the 'hidden in outliner' flag on nodes.  
                Properties: create, query, edit
        ignoreOutlinerColor (bool?): Sets whether or not the outliner ignores the 'use outliner color' flag on nodes.  
                Properties: create, query, edit
        isChildSelected (Queryable[str]?): This flag allows you to query if one or more of the children of the  
                specified item is selected in the outliner. The item should be  
                specified using a unique DAG path. Note that if the specified item  
                appears multiple times in the outliner, the result will be true if one  
                or more children of any occurrence of the specified item in the  
                outliner is/are selected.  
                Properties: query
        isSet (Queryable[int]?): Returns true if the item present at the given row is a set.  
                Properties: query
        isSetMember (Queryable[int]?): Returns true if the item present at the given row is a set member.  
                Properties: query
        isUfeItem (Queryable[int]?): Returns true if the item present at the given row is a UFE item.  
                Properties: query
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        longNames (bool?): Controls whether long or short attribute names will be used  
                in the interface.  Note that this flag is ignored if the -niceNames  
                flag is set.  Default is short names. Queried, returns a boolean.  
                Properties: query, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        mapMotionTrails (bool?): Sets whether or not we replace the motion trail in the outliner with the object it is trailing.  
                Properties: create, query, edit
        masterOutliner (Queryable[str]?): This flag is the name of an outliner that this outliner will share the objects  
                and state from. When an outliner is shared, all of its state information  
                comes from, and is applied to, the primary outliner.  
                Properties: create, query, edit
        niceNames (bool?): Controls whether the attribute names will be displayed in  
                a more user-friendly, readable way.  When this is on, the longNames  
                flag is ignored.  When this is off, attribute names will be displayed  
                either long or short, according to the longNames flag.  
                Default is on. Queried, returns a boolean.  
                Properties: query, edit
        object (Queryable[str]?): This flag is used together with the parentObject flag to get  
                the name of the parent object for the specified object.  
                Properties: query
        organizeByClip (bool?): If true then when a node with Time Editor clips is displayed, attributes  
                will be displayed according to the clip(s) it belongs to.  
                eg:  
              
                Clip1  
                Attr1  
                Attr2  
                Clip2  
                Attr1  
              
                If it is false then the outliner will be organized primarily by attributes.  
                eg:  
              
                Attr1  
                Clip1  
                Clip2  
                Attr2  
                Clip1  
                Properties: create, query, edit
        organizeByLayer (bool?): If true then when a node with animation layer is displayed, attributes  
                will be displayed according to the layer(s) it belongs to.  
                eg:  
              
                Layer1  
                Attr1  
                Attr2  
                Layer2  
                Attr1  
              
                If it is false then the outliner will be organized primarily by attributes.  
                eg:  
              
                Attr1  
                Layer1  
                Layer2  
                Attr2  
                Layer1  
                Properties: create, query, edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        parentObject (bool?):   
                Properties: query
        pinPlug (Queryable[str]?): Pins the named plug, so it always appears in the outliner, irrespective  
                of the incoming selection connection.  
                In query mode, returns a list of the pinned plugs.  
                Properties: create, query, edit
        refresh (bool?): Causes the outliner to refresh itself.  
                Properties: edit
        removeFromCurrentSet (int?): Removes selected members of a set from their current set. Current set is the set to which item at the given row belongs to.  
                If no selected items, the item at the given row is removed from its current set.  
                Properties: edit
        renameItem (int?): Renames the item at the given row index in the outliner.  
                Properties: edit
        renameSelectedItem (bool?): Rename the first selected item in the outliner.  
                Properties: edit
        renderFilterActive (bool?): This is a query only flag which returns true if the render setup filter is Active, i.e one of the four render filters (Inside Selected, Outside Selected, Inside All Layers, Outside All Layers)  
                is applied on the outliner currently, false otherwise.  
                Properties: query
        renderFilterIndex (Queryable[int]?): Sets the Render Setup Filter to the index passed. This only works if the filter is visible in outliner and its selection is not locked.  
                Valid indices are:  
              
                0. Scene  
                2. Inside Selected  
                3. Outside Selected  
                4. Inside All Layers  
                5. Outside All Layers  
              
                Default: Scene  0  
                In query mode returns current index of the filter.  
                Properties: create, query, edit
        renderFilterVisible (bool?): Show/Hide the Render Setup Filter in outliner. In query mode returns whether the Render Setup Filter is visible or not.  
                Properties: create, query, edit
        selectCommand (Queryable[Callable[..., Any]]?): A command to be executed when an item is selected.  
                Only valid Mel commands will be saved when the outlinerEditor  
                will be persisted in a scene or in a JSON layout file.  
                Python commands are never saved.  
                Properties: create, query, edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        selectionOrder (str?): Specify how objects are sorted in selection list. Current recognised values  
                are "chronological" for sorting in selection order and "display" to sort objects in the same order that the outliner does.  
                Properties: edit
        setFilter (Queryable[str]?): Specifies the name of a filter which is used to filter  
                which (if any) sets to display.  
                Properties: create, query, edit
        setsIgnoreFilters (bool?): This flag specifies whether or not the filter should be ignored  
                for expanding sets to show set members (default is true).  
                Properties: create, query, edit
        showAnimCurvesOnly (bool?): This flag modifies the showConnected flag.  If showConnected  
                is set to true then this flag will cause display of only  
                those attributes that are connected to an animCurve. If  
                showConnected is set to false then this flag does nothing.  
                Properties: create, query, edit
        showAnimLayerWeight (bool?): If true then when a node with animation layer is displayed, the  
                weight of the layer will be displayed if it is keyed.  
                Properties: create, query, edit
        showAssets (bool?): This flags specifies whether assets should be shown in the outliner.  
                Properties: create, query, edit
        showAssignedMaterials (bool?): Specifies whether to show assigned materials under shapes.  
                Properties: create, query, edit
        showAttrValues (bool?): This flag specifies whether attribute values or attribute names should  
                be displayed.  
                Note: currently only string attributes can have their values displayed.  
                Properties: create, query, edit
        showAttributes (bool?): Specifies whether to show attributes or not.  
                Properties: create, query, edit
        showCompounds (bool?): This flag specifies whether or not compound attributes should be  
                displayed, or just the leaf attributes.  
                Note: if showConnected is true, and the compound attribute  
                is connected, it will still be displayed.  
                Properties: create, query, edit
        showConnected (bool?): This flag modifies the showAttributes flag.  If showAttributes  
                is set to true then this flag will cause display of only  
                those attributes that are connected in the dependency graph.  
                If showAttributes is set to false then this flag does nothing.  
                Properties: create, query, edit
        showContainedOnly (bool?): This flags specifies whether nodes belonging to containers should be show  
                under the container node only. Otherwise, it will show up under the world  
                as well.  
                Properties: create, query, edit
        showContainerContents (bool?): This flags specifies whether the contents of the container should be  
                shown under the container node in the outliner.  
                Properties: create, query, edit
        showDagOnly (bool?): This flag specifies whether all dependency graph objects will  
                be displayed, or just DAG objects.  
                Properties: create, query, edit
        showLeafs (bool?): This flag specifies whether or not leaf attributes should be  
                displayed, or just the compound attributes.  
                Note: if showConnected is true, and the leaf attribute  
                is connected, it will still be displayed.  
                Properties: create, query, edit
        showMuteInfo (bool?): This flag specifies whether mute information will be displayed  
                Properties: create, query, edit
        showNamespace (bool?): This flag specifies whether all objects will have their  
                namespace displayed, if namespace different than root.  
                Properties: create, query, edit
        showNumericAttrsOnly (bool?): This flag specifies whether or not all attributes should be  
                displayed, or just numeric attributes.  
                Note: if showConnected is true, and the attribute  
                is connected, it will still be displayed.  
                Properties: create, query, edit
        showParentContainers (bool?): This flags specifies whether nodes belonging to containers/assets should show their  
                containers/assets as well in its outliner.  
                Properties: create, query, edit
        showPinIcons (bool?): Sets whether pin icons are shown for unpinned plugs.  
                Properties: create, query, edit
        showPublishedAsConnected (bool?): This flags enables attributes that are published to be displayed in italics.  
                Otherwise, only attributes connected as a destination are shown in italics.  
                Properties: create, query, edit
        showReferenceMembers (bool?): Specifies whether to show reference node members under the reference node in the outliner.  
                Properties: create, query, edit
        showReferenceNodes (bool?): Specifies whether to show reference nodes or not.  
                Properties: create, query, edit
        showSelected (bool?): If true then the selected items are expanded in the outliner.  
                Properties: create, edit
        showSetMembers (bool?): If true then when a set is expanded, the set members  
                will be displayed. If false, then only other sets will be  
                displayed.  
                Properties: create, query, edit
        showShapes (bool?): Specifies whether to show shapes or not.  
                Properties: create, query, edit
        showTextureNodesOnly (bool?): This flag modifies the showConnected flag. If showConnected is set to true then  
                this flag will cause display of only those attributes that are connected to a  
                texture node. If showConnected is set to false then this flag does nothing.  
                Properties: create, query, edit
        showTimeEditor (bool?): If true, all nodes related to the Time Editor will be  
                shown as a hierarchy.  
                Properties: create, query, edit
        showUVAttrsOnly (bool?): This flag specifies whether or not all attributes should be displayed, or  
                just uv attributes.  
                Note: currently the only attribute which will be  
                displayed is Shape.uvSet.uvSetName.  
                Properties: create, query, edit
        showUfeItems (bool?): Specifies whether to show Ufe (non-Maya) items.  
                Properties: create, query, edit
        showUnitlessCurves (bool?): This flag (in combination with -expandConnections) specifies  
                whether or not connection expansion should show unitless  
                animCurves.  
                Properties: create, query, edit
        showUpstreamCurves (bool?): Specifies exactly which attributes are displayed when showAttributes  
                and expandConnections are both true.  
                If true, the dependency graph is searched upstream for all curves  
                that drive the selected plugs (showing multiple curves for example  
                in a typical driven key setup, where first the driven key curve is  
                encountered, followed by the actual animation curve that drives the  
                source object). If false, only the first curves encountered  
                will be shown. Note that, even if false, multiple curves can be shown  
                if e.g. a blendWeighted node is being used to combine multiple curves.  
                Properties: create, query, edit
        sortOrder (Queryable[str]?): Specify how objects are to be sorted.  Current recognised values  
                are "none" for no sorting and "dagName" to sort DAG objects by name.  
                Notes: a) non-DAG objects are always sorted by nodeType and name.  
                b) when sortOrder is set to "dagName", objects cannot be reordered  
                using drag-and-drop, they can however be reparented.  
                Properties: create, query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        transmitFilters (bool?): This flag specifies how the selectionConnection is populated  
                when attribute filters are enabled.  If this flag is set to  
                true, then all the attributes that pass the filter will be  
                placed on the selectionConnection.  By default this flag is  
                false.  
                Properties: create, query, edit
        ufeFilter (Queryable[Tuple[str, str]]?): Specifies what UFE filter attributes should be used for display.  
                This flag must used together with the ufeFilterValue flag to get/set  
                the value of the UFE filter.  
                The first string is the UFE run-time name and the second is the child filter name.  
                Properties: query, edit
        ufeFilterValue (bool?): The value of the UFE filter specified with flag ufeFilter.  
                This flag must used together with the ufeFilter flag.  
                Properties: query, edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        unpinPlug (str?): Unpins the named plug.  
                Properties: create, edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create

    Returns:
        str: (the name of the editor)

    Example:
    """

