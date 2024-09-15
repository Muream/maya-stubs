from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def hyperGraph(*args: Any, edit: bool = ..., query: bool = ..., addBookmark: bool = ..., addDependGraph: str = ..., addDependNode: str = ..., animateTransition: bool = ..., attributeEditor: str = ..., backward: bool = ..., bookmarkName: bool = ..., breakConnectionCommand: Queryable[str] = ..., clear: bool = ..., collapseContainer: bool = ..., connectionDrawStyle: str = ..., control: bool = ..., currentEdge: Queryable[str] = ..., currentNode: Queryable[str] = ..., debug: str = ..., defineTemplate: str = ..., deleteBookmark: str = ..., dependGraph: bool = ..., dependNode: str = ..., directoryPressCommand: str = ..., docTag: Queryable[str] = ..., down: bool = ..., downstream: bool = ..., dragAndDropBehaviorCommand: str = ..., dropNode: Queryable[str] = ..., dropTargetNode: Queryable[str] = ..., edgeDblClickCommand: str = ..., edgeDimmedDblClickCommand: str = ..., edgeDropCommand: str = ..., edgePressCommand: str = ..., edgeReleaseCommand: str = ..., enableAutomaticLayout: bool = ..., exists: bool = ..., expandContainer: bool = ..., feedbackGadget: Queryable[str] = ..., feedbackNode: Queryable[str] = ..., filter: Queryable[str] = ..., filterDetail: Tuple[str, bool] = ..., fitImageToHeight: bool = ..., fitImageToWidth: bool = ..., focusCommand: str = ..., fold: bool = ..., forceMainConnection: Queryable[str] = ..., forceRefresh: bool = ..., forward: bool = ..., frame: bool = ..., frameBranch: bool = ..., frameGraph: bool = ..., frameGraphNoRebuild: bool = ..., frameHierarchy: bool = ..., freeform: bool = ..., fromAttr: Queryable[str] = ..., fromNode: Queryable[str] = ..., getNodeList: bool = ..., getNodePosition: Queryable[str] = ..., graphDescription: bool = ..., graphLayoutStyle: Queryable[str] = ..., graphType: Queryable[str] = ..., heatMapDisplay: bool = ..., highlightConnection: Queryable[str] = ..., iconSize: Queryable[str] = ..., image: Queryable[str] = ..., imageEnabled: bool = ..., imageForContainer: bool = ..., imagePosition: Queryable[Tuple[float, float]] = ..., imageScale: Queryable[float] = ..., initializeScript: str = ..., isHotkeyTarget: bool = ..., layout: bool = ..., layoutSelected: str = ..., limitGraphTraversal: int = ..., lockMainConnection: bool = ..., look: Tuple[float, float] = ..., mainListConnection: Queryable[str] = ..., mergeConnections: bool = ..., navigateHome: bool = ..., navup: bool = ..., newInputConnection: str = ..., newOutputConnection: str = ..., nextView: bool = ..., nodeConnectCommand: str = ..., nodeDblClickCommand: str = ..., nodeDropCommand: str = ..., nodeMenuCommand: str = ..., nodePressCommand: str = ..., nodeReleaseCommand: str = ..., opaqueContainers: bool = ..., orientation: Queryable[str] = ..., panView: Tuple[float, float] = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., popupMenuScript: str = ..., previousView: bool = ..., range: Queryable[Tuple[float, float]] = ..., rebuild: bool = ..., removeNode: str = ..., rename: bool = ..., resetFreeform: bool = ..., restoreBookmark: str = ..., scrollUpDownNoZoom: bool = ..., selectionConnection: Queryable[str] = ..., setNodePosition: Tuple[str, float, float] = ..., showCachedConnections: bool = ..., showConnectionFromSelected: bool = ..., showConnectionToSelected: bool = ..., showConstraintLabels: bool = ..., showConstraints: bool = ..., showDeformers: bool = ..., showExpressions: bool = ..., showInvisible: bool = ..., showRelationships: bool = ..., showShapes: bool = ..., showUnderworld: bool = ..., stateString: bool = ..., toAttr: Queryable[str] = ..., toNode: Queryable[str] = ..., transitionFrames: Queryable[int] = ..., unParent: bool = ..., unfold: bool = ..., unfoldAll: bool = ..., unfoldAllShapes: bool = ..., unfoldHidden: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., updateNodeAdded: bool = ..., updateSelection: bool = ..., upstream: bool = ..., useDrawOverrideColor: bool = ..., useFeedbackList: bool = ..., useTemplate: str = ..., viewOption: Queryable[str] = ..., visibility: bool = ..., zoom: float = ...) -> Union[str, bool, Tuple[float, float], float, int]:
    """The following is an overview of the basic features of the hypergraph.
    A more detailed description is given in the user manuals.The hypergraph provides the user with the ability to view and edit
    the maya scene graph.  The hypergraph supports two types of graphs:
    the DAG or scene hierarchy and the dependency graph.The default view of the hypergraph editor is the DAG view.
    The user can show the dependency graph for a collection of nodes by
    first selecting the nodes and navigating to the dependency graph using one
    of the graph options.  The user can save any view by setting a
    bookmark to that view.  The user can also show previous views using
    the view options provided.The hypergraph supports a simple editing mechanism for editing hierarchy
    in the DAG view and connections in dependency graph view.
    In the DAG  view, the user can reparent or reorder nodes in the graph
    using drag-and-drop. In the dependency graph view, the user can select
    connections and delete them or make new connections by dragging and
    dropping nodes or existing connections.The hypergraph supports two layout modes in the DAG view: automatic and
    freeform.  In automatic mode, the graph nodes are automatically
    positioned according to the layout preferences.  In freeform mode, the
    user can position nodes manually.  The node position is saved in the scene.
    A background image can be placed behind DG or DAG in freeform mode.
    This can be used as a template for positioning nodes in a user-defined
    layout.Nodes in the DAG view can be expanded or collapsed.  The state is saved
    in the scene.  The performance of the graph drawing will increase
    as hierarchies are collapsed.In addition to hierachy relationships, the hypergraph can show
    expression, constraint and deformation relationships in the DAG.
    These can be enabled/disabled through the options provided.  There
    are also additional filters for showing shape nodes and invisible
    nodes.  The amount of detail show may affect the speed of the display
    of the graph.Most of the UI features of the hypergraph are addressable through the
    hypergraph command-line interface.  The available command-line
    options are described in the next section.
    Args:
        addBookmark (bool?): Create a bookmark for the current hypergraph view.  
                Properties: create, edit
        addDependGraph (str?): Add a dependency graph starting at the named node to the view  
                Properties: create, edit
        addDependNode (str?): Add a dependency node to the dependency graph view  
                Properties: create, edit
        animateTransition (bool?): Turns animate transitions off and on.  
                Properties: create, query, edit
        attributeEditor (str?): Launches attribute editor on selected node.  
                Properties: create, edit
        backward (bool?): Navigate backward one step.  
                Properties: create, edit
        bookmarkName (bool?): Returns the bookmark name for the most recently created bookmark.  
                Properties: query
        breakConnectionCommand (Queryable[str]?): Specify the command to call when a connection is broken.  
                Properties: create, query, edit
        clear (bool?): Clears the current hypergraph view and deletes the graph UI.  
                (see also -rebuild flag)  
                Properties: create, edit
        collapseContainer (bool?): Collapses containers selected in DG graph.  
                Properties: create, edit
        connectionDrawStyle (str?): Specify how connections between nodes should be drawn. Valid  
                values are "center" (draws connection lines from the center of one node  
                to the center of the other) and "side" (draws connection lines from the  
                right side of the source node to the left side of the destination  
                node). The default is "center". This flag does not apply to Hypershade  
                graphs, which are always drawn with the "side" connection draw style.  
                Properties: create, edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        currentEdge (Queryable[str]?): Return the current edge name.  
                Properties: query, edit
        currentNode (Queryable[str]?): Return the current node name.  
                Properties: query, edit
        debug (str?): Run a debug method on the graph  
                Properties: create, edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deleteBookmark (str?): Delete the bookmark with the corresponding node name.  
                Properties: create, edit
        dependGraph (bool?): Displays dependency graph iterated from specified node.  
                Properties: create, edit
        dependNode (str?): Displays dependency node in view.  
                Properties: create, edit
        directoryPressCommand (str?): Specify a command to run when a directory is pressed.  
                Properties: create, edit
        docTag (Queryable[str]?): Attaches a tag to the editor.  
                Properties: create, query, edit
        down (bool?): Navigate down to the dependency graph containing the current selection.  
                Shows upstream and downstream connections.  
                Properties: create, edit
        downstream (bool?): Show downstream dependency graph of selected node(s).  
                Properties: create, edit
        dragAndDropBehaviorCommand (str?): Mel proc called when a drag and drop onto a hyperGraph  
                node has occurred. Proc signature is  
                procName (string $editor, string $sourceNode, string $destinationNode).  
                Properties: create, edit
        dropNode (Queryable[str]?): Returns the name of the source node in a drag and drop connection,  
                when called during processing of a drop.  
                Properties: query
        dropTargetNode (Queryable[str]?): Returns the name of the destination node in a drag and drop  
                connection, when called during processing of a drop.  
                Properties: query
        edgeDblClickCommand (str?): Mel proc called when an edge is double clicked.  Proc signature is  
                procName (string $editor, string $edge).  
                Properties: create, edit
        edgeDimmedDblClickCommand (str?): Mel proc called when a dimmed edge is double clicked.  Proc signature is  
                procName (string $editor, string $edge).  
                Properties: create, edit
        edgeDropCommand (str?): Command to execute when an edge drop occurs.  
                Properties: create, edit
        edgePressCommand (str?): Command to execute when an edge press occurs.  
                Properties: create, edit
        edgeReleaseCommand (str?): Command to execute when an edge release occurs.  
                Properties: create, edit
        enableAutomaticLayout (bool?): Rebuild the graph if a node is added or removed from the graph  
                via drag and drop or dg messages. Default is true.  
                Properties: create, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        expandContainer (bool?): Expands containers selected in DG graph.  
                Properties: create, edit
        feedbackGadget (Queryable[str]?): Returns the name of the current gadget.  
                Properties: query
        feedbackNode (Queryable[str]?): Returns the name of the current feedback or highlight node.  
                Properties: query
        filter (Queryable[str]?): Specifies the name of an itemFilter object to be used with this editor.  
                This filters the information coming onto the main list  
                of the editor.  
                Properties: create, query, edit
        filterDetail (Tuple[str, bool]?): This flag is obsolete. Use the showConstraints, showExpressions,  
                showDeformer, showInvisible, showShapes and showUnderworld flags  
                instead.  
                Properties: create, edit
        fitImageToHeight (bool?): Changes position and scale of background image, so its height fits current editor view.  
                Properties: create
        fitImageToWidth (bool?): Changes position and scale of background image, so its width fits current editor view.  
                Properties: create
        focusCommand (str?): Mel proc to be run when the mouse is clicked in the hyper  
                graph. Primarily of use in setting the window focus.  
                Properties: create, edit
        fold (bool?): Folds (Collapses) selected object.  
                Properties: create, edit
        forceMainConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will only  
                display items contained in the selectionConnection object. This is  
                a variant of the -mainListConnection flag in that it will force a  
                change even when the connection is locked. This flag is used to  
                reduce the overhead when using the -unlockMainConnection  
                , -mainListConnection, -lockMainConnection flags in immediate  
                succession.  
                Properties: create, query, edit
        forceRefresh (bool?): Forces the hypergraph to refresh (redraw) its contents.  
                Properties: create, edit
        forward (bool?): Navigate forward one step.  
                Properties: create, edit
        frame (bool?): Frames the selected objects  
                Properties: create, edit
        frameBranch (bool?): Frames the the branch from the selected node on downward.  
                Properties: create, edit
        frameGraph (bool?): Frames the entire graph.  
                Properties: create, edit
        frameGraphNoRebuild (bool?): Specify that on zoom out the graph should not rebuild; for efficiency.  
                Properties: create, edit
        frameHierarchy (bool?): Frames the hierarchy that contains the selected node.  
                Properties: create, edit
        freeform (bool?): Enable freeform layout mode.  
                Properties: create, query, edit
        fromAttr (Queryable[str]?): Returns the name of the source attribute in a drag and drop  
                connection, when called during processing of a drop.  
                Properties: query
        fromNode (Queryable[str]?): Returns the name of the source node in a drag and drop  
                connection, when called during processing of a drop.  
                Properties: query
        getNodeList (bool?): Returns a string array that represents a list  
                of all the nodes in the graph.  
                Properties: query
        getNodePosition (Queryable[str]?): Returns the position of a specified node in x,y graph coords.  
                This flag and its argument must be passed to the command before the  
                -q flag (see examples).  
                      In query mode, this flag can accept a value.  
                Properties: query
        graphDescription (bool?): When used, return a description of the current graph.  
                Properties: create, edit
        graphLayoutStyle (Queryable[str]?): This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".  
                Use of any other style will trigger a warning.  
                Properties: create, query, edit
        graphType (Queryable[str]?): Returns the type name of the current graph in the view  
                (either DAG or DG).  
                Properties: query
        heatMapDisplay (bool?): Specify whether the heat map should be shown or not.  
                Properties: query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        iconSize (Queryable[str]?): Set or query the icon size for this hyper graph editor.  
                The currently allowed icon sizes are "smallIcons", "mediumIcons",  
                "largeIcons" and "superIcons".  
                Properties: create, query, edit
        image (Queryable[str]?): Specify background image to be loaded from the project image directory.  
                Properties: create, query, edit
        imageEnabled (bool?): Enable display of a loaded background image (Freeform DAG view or DG view)  
                Properties: create, query, edit
        imageForContainer (bool?): Specify that the following flags work on selected containers instead of the whole image:  
                -imageScale,-imagePosition, fitImageToWidth, -fitImageToHeight, -image  
                Properties: create, query, edit
        imagePosition (Queryable[Tuple[float, float]]?): Position of the background image.  
                Properties: create, query, edit
        imageScale (Queryable[float]?): Uniform scale of the background image.  
                Properties: create, query, edit
        initializeScript (str?): Script to call when the graph is initialized.  
                Properties: create, edit
        isHotkeyTarget (bool?): For internal use.  
                Properties: query
        layout (bool?): Perform an automatic layout on the graph.  
                Properties: create, edit
        layoutSelected (str?): This flag is obsolete.  The only supported graph layout style is "hierarchicalLayout".  
                Use of any other style will trigger a warning.  
                Properties: create, edit
        limitGraphTraversal (int?): Limit the graph traversal to a certain number of levels.  
                Properties: create, edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        look (Tuple[float, float]?): Look at a coordinate in the graph view  
                Properties: create, edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        mergeConnections (bool?): Merge groups of connections into 'fat' connections.  
                Properties: create, query, edit
        navigateHome (bool?): Navigate to the home (DAG) view.  
                Properties: create, edit
        navup (bool?): Navigate up to the dependency graph containing the current selection.  
                Shows upstream and downstream connections.  
                Properties: create, edit
        newInputConnection (str?): Specify a new connection, input side  
                Properties: create, edit
        newOutputConnection (str?): Specify a new connection, output side  
                Properties: create, edit
        nextView (bool?): Changes the view to the next DAG view.  
                Properties: create, edit
        nodeConnectCommand (str?): Command to call when a node is connected.  
                Properties: create, edit
        nodeDblClickCommand (str?): Command to call when a node is double-clicked.  
                Properties: create, edit
        nodeDropCommand (str?): Set the command to be called when a node is dropped in the  
                hypergraph window.  
                Properties: create, edit
        nodeMenuCommand (str?): Command to call when a node menu is activated.  
                Properties: create, edit
        nodePressCommand (str?): Set the command to be called when the user presses a mouse button  
                while the cursor is over a node in the hypergraph window.  
                Properties: create, edit
        nodeReleaseCommand (str?): Set the command to be called when the user releases a mouse button  
                while the cursor is over a node in the hypergraph window.  
                Properties: create, edit
        opaqueContainers (bool?): Sets expanded container background opacity.  
                Properties: query, edit
        orientation (Queryable[str]?): Selects orientation style of graph: "horiz"|"vert"  
                Properties: create, query, edit
        panView (Tuple[float, float]?): Pan the view to a new center.  
                Properties: create, edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        popupMenuScript (str?): Set the script to be called to register the popup menu with the  
                control for this hypergraph. The script will be called with a string  
                argument which gives the name of the hypergraph whose control the popup  
                menu should be parented to.  
                Properties: create, edit
        previousView (bool?): Changes the view back to the previous DAG view.  
                Properties: create, edit
        range (Queryable[Tuple[float, float]]?): Limits the display of nodes to only those within the range.  
                There are two float values expected, the first the lower threshold  
                of the range and the second the upper threshold of the range.  
                The values are absolute timing values, not percentages.  
                Properties: create, query, edit
        rebuild (bool?): Rebuilds graph  
                Properties: create, edit
        removeNode (str?): Removes the node identified by string from the graph.  
                Properties: create, edit
        rename (bool?): Pops up text field over selected object for renaming  
                Properties: create, edit
        resetFreeform (bool?): Resets freeform position on all nodes.  
                Properties: create, edit
        restoreBookmark (str?): Restore the view corresponding to the bookmark.  
                Properties: create, edit
        scrollUpDownNoZoom (bool?): Specify if we want to be in the  
                scroll along y only with no free zooming mode.  
                By default, hyper graph editor allows user to  
                pan left and right.  
                Properties: create, edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        setNodePosition (Tuple[str, float, float]?): Sets the node identified by string to the (x,y) position  
                in the window specified by the two floats. If  
                the node is not in the graph than it will be added to the  
                graph and then moved to the new position.  
                Properties: create, edit
        showCachedConnections (bool?): Specify whether cached connections should be shown.  
                Properties: create, edit
        showConnectionFromSelected (bool?): Show the connects (constraints, expresions, and deformers - see showConstraints for example)  
                leaving from selected nodes. This can be combined with showConnectionToSelected to show both  
                arrive and leaving connects. If both flags are false then all the connections will be shown.  
                Properties: create, query, edit
        showConnectionToSelected (bool?): Show the connects (constraints, expresions, and deformers - see showConstraints for example)  
                arriving at selected nodes. This can be combined with  
                showConnectionFromSelected to show both arrive and leaving connects. If both flags  
                are false then all the connections will be shown.  
                Properties: create, query, edit
        showConstraintLabels (bool?): Specify whether constraint labels should be shown.  
                Properties: create, edit
        showConstraints (bool?): Show constraint relationships in the DAG.  
                Properties: create, query, edit
        showDeformers (bool?): Show deformer or geometry filter relationships in the DAG.  
                Properties: create, query, edit
        showExpressions (bool?): Show expression relationships in the DAG.  
                Properties: create, query, edit
        showInvisible (bool?): Show invisible nodes in the DAG.  
                Properties: create, query, edit
        showRelationships (bool?): Show relationship (message) connections.  
                Properties: create, query, edit
        showShapes (bool?): Show shape nodes in the DAG.  
                Properties: create, query, edit
        showUnderworld (bool?): Show underworld graphs in the DAG.  
                Properties: create, query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        toAttr (Queryable[str]?): Returns the name of the destination attribute in a drag and drop  
                connection, when called during processing of a drop.  
                Properties: query
        toNode (Queryable[str]?): Returns the name of the destination node in a drag and drop  
                connection, when called during processing of a drop.  
                Properties: query
        transitionFrames (Queryable[int]?): Specify te number of transition frames for animate transitions.  
                Properties: create, query, edit
        unParent (bool?): Specifies that the editor should be removed from its layout.  
                This cannot be used in query mode.  
                Properties: create, edit
        unfold (bool?): Unfolds (expands) selected object.  
                Properties: create, edit
        unfoldAll (bool?): Unfolds everything under selected object.  
                Properties: create, edit
        unfoldAllShapes (bool?): Unfolds all shapes.  
                Properties: create, edit
        unfoldHidden (bool?): Unfolds all hidden objects.  
                Properties: create, edit
        unlockMainConnection (bool?): Unlocks the mainConnection, effectively restoring the original  
                mainConnection (if it is still available), and dynamic updates.  
                Properties: create, edit
        updateMainConnection (bool?): Causes a locked mainConnection to be updated from the orginal  
                mainConnection, but preserves the lock state.  
                Properties: create, edit
        updateNodeAdded (bool?): Update graph when a new node is added to the database  
                Properties: create, query, edit
        updateSelection (bool?): Update selection state in the graph when the selection state of  
                database changes.  
                Properties: create, query, edit
        upstream (bool?): Show upstream dependency graph of selected node(s).  
                Properties: create, edit
        useDrawOverrideColor (bool?): Specify whether or not to use draw override coloring.  
                Properties: create, edit
        useFeedbackList (bool?): Use feedback or highlight list as the target selection when  
                processing other hypergraph command-line options.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        viewOption (Queryable[str]?): Set or query the view option for this hyper graph editor.  
                The currently allowed views are "asIcons" and "asList".  
                Properties: create, query, edit
        visibility (bool?): Set the visible state of the selected node(s).  
                Properties: create, edit
        zoom (float?): Specify the zoom factor for animating transitions  
                Properties: create, edit

    Returns:
        str: the name of the panel

    Example:
    """

