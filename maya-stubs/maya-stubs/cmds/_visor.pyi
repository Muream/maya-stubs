from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def visor(*args: Any, query: bool = ..., addFolder: bool = ..., addNodes: Queryable[str] = ..., allowPanningInX: bool = ..., allowPanningInY: bool = ..., allowZooming: bool = ..., command: Queryable[str] = ..., deleteFolder: Queryable[str] = ..., editFolder: Queryable[str] = ..., folderList: Queryable[str] = ..., menu: Queryable[str] = ..., name: Queryable[str] = ..., nodeType: Queryable[str] = ..., openDirectories: bool = ..., openFolder: bool = ..., parent: Queryable[str] = ..., path: Queryable[str] = ..., popupMenuScript: Queryable[str] = ..., rebuild: bool = ..., refreshAllSwatches: bool = ..., refreshSelectedSwatches: bool = ..., refreshSwatch: Queryable[str] = ..., reset: bool = ..., restrictPanAndZoom: bool = ..., saveSwatches: bool = ..., scrollBar: Queryable[str] = ..., scrollPercent: Queryable[float] = ..., selectedGadgets: Queryable[str] = ..., showDividers: bool = ..., showFiles: bool = ..., showFolders: bool = ..., showNodes: bool = ..., stateString: bool = ..., style: Queryable[str] = ..., transform: Queryable[str] = ..., type: Queryable[str] = ...) -> Union[str, bool, float]:
    """Command for the creation and manipulation of a Visor UI element. The Visor is
    used to display the contents of a scene (rendering related nodes in
    particular), as well as files on disk which the user may wish to bring into
    the scene (shader and texture libraries for example).render, hypergraph, shader, hypershade
    Args:
        addFolder (bool?): Add a new folder to the current visual browser  
                Properties: create, query
        addNodes (Queryable[str]?): Add dependency graph nodes by name to a user defined custom folder.  The  
                argument is a string encolsed in quotes with 1 one more node names  
                seperated by blanks  
                Properties: create, query
        allowPanningInX (bool?): Specifies whether or not the user should be able to pan the contents of the  
                visor horizontally. Default is true.  
                Properties: create, query
        allowPanningInY (bool?): Specifies whether or not the user should be able to pan the contents of the  
                visor vertically. Default is true.  
                Properties: create, query
        allowZooming (bool?): Specifies whether or not the user should be able to zoom the contents of the  
                visor. Default is true.  
                Properties: create, query
        command (Queryable[str]?): Mel command which will return a list of nodes to add to a folder  
                Properties: create, query
        deleteFolder (Queryable[str]?): Delete the specified folder and all of its children  
                Properties: create, query
        editFolder (Queryable[str]?): Edit the name and MEL command for an existing folder  
                Properties: create, query
        folderList (Queryable[str]?): Return a string array of the folders in the visor.  
                Properties: query
        menu (Queryable[str]?): Set the name of the script to run to get a popup menu  
                Properties: create, query
        name (Queryable[str]?): Name of the new folder  
                Properties: create, query
        nodeType (Queryable[str]?): A node type used by folders of type nodeTypeInDAG  
                Properties: create, query
        openDirectories (bool?): When adding a new folder indicate if it sub directories will be show.  
                The default is to not show sub directories.  
                Properties: create, query
        openFolder (bool?): When adding a new folder indicate if it will be open or closed by default.  
                The default is closed.  
                Properties: create, query
        parent (Queryable[str]?): Parent folder of this folder  
                Properties: create, query
        path (Queryable[str]?): Path to a file system directory to be displayed in the folder  
                Properties: create, query
        popupMenuScript (Queryable[str]?): Specifies the script to be called when the right mouse button is pressed in  
                the visor. The name of the editor in which the right mouse button was pressed  
                will be appended to the script at the time the script is called.  
                Properties: create, query
        rebuild (bool?): Rebuild the visor after interactively adding a folder  
                Properties: create, query
        refreshAllSwatches (bool?): Refresh the swatches of all files currently displayed in this visor.  
                Properties: create, query
        refreshSelectedSwatches (bool?): Refresh the swatches of all files currently selected in any visor.  
                Properties: create, query
        refreshSwatch (Queryable[str]?): Refresh the swatch of the file with the specified path.  
                Properties: create, query
        reset (bool?): Clear all previously loaded folder descriptions in preperation for  
                building a new visual browser  
                Properties: create, query
        restrictPanAndZoom (bool?): Specifies whether the panning and zooming of the visor should be  
                restricted to keep the contents in the top left corner of the  
                visor when they are smaller than the visible area within the visor.  
                Default is true.  
                Properties: create, query
        saveSwatches (bool?): Save swatches to disk for currently displayed image files.  
                Properties: create, query
        scrollBar (Queryable[str]?): Set the name of the scroll bar associated with visor  
                Properties: create, query
        scrollPercent (Queryable[float]?): Set the percentage value for the scroll bar.  Typically called from a  
                a scroll bars callback.  
                Properties: create, query
        selectedGadgets (Queryable[str]?): Return a string array of the currently selected gadgets (files, folders, nodes)  
                in the visor.  
                Properties: query
        showDividers (bool?): Specifies whether or not the visor should show dividers. The default is true.  
                If -showDividers is set to false, dividers will be drawn as folders instead.  
                Properties: create, query
        showFiles (bool?): Specifies whether or not the visor should show files. The default is true.  
                Properties: create, query
        showFolders (bool?): Specifies whether or not the visor should show folders. The default is true.  
                Properties: create, query
        showNodes (bool?): Specifies whether or not the visor should show nodes. The default is true.  
                Properties: create, query
        stateString (bool?): Return the MEL command string to save the folder setup in visor  
                Properties: create, query
        style (Queryable[str]?): Set display style for the browser.  Options are:  
                    outliner  
                         A single column with an outliner style icon and a text label  
                    singleColumn  
                         A single column with an image style icon and a text label  
                    multiColumn  
                         A multiple column grid of swatches with the text label below the swatch  
                Properties: create, query
        transform (Queryable[str]?): Name of a transform node used by folders of type nodeTypeInDAG  
                Properties: create, query
        type (Queryable[str]?): Type of the new folder.  Options are:   
              
                command   
                         A mel command that will return a list of depend nodes that will  
                         be displayed in the folder  
                connectedNodes   
                         The nodes connected to the specified node name will be displayed  
                         in the folder  
                defaultNodes   
                         A mel command that will generate default node types.  These nodes  
                         will not be part of the scene and are used for drag and drop  
                         creation of new nodes that are in the scene.  The mel command  
                         use with this type is usually "listNodetypes".  
                directory   
                        A directory name in the file system  
                directoryCommand   
                        A mel command that will return a directory name in the file system  
                folder   
                        An empty folder(the default value).  Empty folders can be used  
                        as user defined folders by dropping dependency graph nodes in to them  
                nodeTypeInDAG   
                                List all nodes of a given type under a specified transforms in the  
                                DAG.  For example list all the shaders for a character by specifying  
                        the top transform of the character  
                shelfItems   
                        A directory containing mel files to use as shelf items  
                Properties: create, query

    Returns:
        str: Command result

    Example:
    """

