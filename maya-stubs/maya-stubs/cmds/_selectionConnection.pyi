from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectionConnection(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., activeCacheList: bool = ..., activeCharacterList: bool = ..., activeList: bool = ..., addScript: Queryable[Callable[..., Any]] = ..., addTo: str = ..., characterList: bool = ..., clear: bool = ..., connectionList: bool = ..., defineTemplate: str = ..., deselect: str = ..., editor: Queryable[str] = ..., exists: bool = ..., filter: Queryable[str] = ..., findObject: Queryable[str] = ..., g: bool = ..., highlightList: bool = ..., identify: bool = ..., keyframeList: bool = ..., lock: bool = ..., modelList: bool = ..., object: Queryable[str] = ..., parent: Queryable[str] = ..., remove: str = ..., removeScript: Queryable[Callable[..., Any]] = ..., select: str = ..., setList: bool = ..., switch: bool = ..., useTemplate: str = ..., worldList: bool = ...) -> Union[str, Callable[..., Any], bool]:
    """This command creates a named selectionConnection object. This object
    is simply a shared selection list. It may be used by editors to
    share their highlight data. For example, an outliner may attach its
    selected list to one of these objects, and a graph editor may use the
    same object as a list source. Then, the graph editor would only
    display objects that are selected in the outliner.Selection connections are UI objects which contain a list of model
    objects. Selection connections are useful for specifying which objects
    are to be displayed within a particular editor. Editor's have threewhere a selection connection may be attached.
    They are:There are several different types of selection connections that may be
    created. They include:Below is an example selectionConnection network between two
    editors. Editor 1 is setup to display objects on the activeList.
    Editor 2 is setup to display objects which are selected within Editor
    1, and objects that are selected in Editor 2 are highlighted within
    Editor 1:The following commands will establish this network:Note: to delete ause the deleteUI commandNote: commands which expect objects may be given a selection connection
    instead, and the command will operate upon the objects wrapped by the
    selection connectionNote: the graph editor and the dope sheet are the only editors which can use the
    editor connection to the highlightConnection of another editorWARNING: some flag combinations may not behave as you expect.  The command
    is really intended for internal use for managing the outliner used by
    the various editors.
    Args:
        activeCacheList (bool?): Specifies that this connection should reflect the cache that objects  
                on the active list belong to.  
                Properties: create
        activeCharacterList (bool?): Specifies that this connection should reflect the characters that objects  
                on the active list belong to.  
                Properties: create
        activeList (bool?): Specifies that this connection should reflect the active  
                list (geometry objects and keys).  
                Properties: create
        addScript (Queryable[Callable[..., Any]]?): Specify a script to be called when something is added to the  
                selection.  
                Properties: create, query, edit
        addTo (str?): The name of a selection connection that should be added to this  
                list of connections.  
                Properties: create, edit
        characterList (bool?): Specifies that this connection should reflect all the characters in  
                the world.  
                Properties: create
        clear (bool?): Remove everything from the selection connection.  
                Properties: create, edit
        connectionList (bool?): Specifies that this connection should contain a list of selection  
                connections.  
                Properties: create, query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        deselect (str?): Remove something from the selection.  
                Properties: create, edit
        editor (Queryable[str]?): Specifies that this connection should reflect the -mainListConnection  
                of the specified editor.  
                Properties: create, query, edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        filter (Queryable[str]?): Optionally specifies an itemFilter for this connection.  
                An empty string ("") clears the current filter.  
                If a filter is specified, all the information going into  
                the selectionConnection must first pass through the filter  
                before being accepted.  
              
                NOTE: filters can only be attached to regular selectionConnections.  
                They cannot be attached to any connection created using  
                the -act, -mdl, -key, -wl, -sl, -cl, -lst, -obj, or -ren flags.  
                We strongly recommend that you do not attach filters to a  
                selectionConnection --- it is better to attach your filter  
                to the editor that is using the selectionConnection instead.  
                Properties: create, query, edit
        findObject (Queryable[str]?): Find a selection connection in this list that wraps the specified  
                object.  
                Properties: query
        g (bool?): A global selection connection cannot be deleted by any script  
                commands.  
                Properties: create, query, edit
        highlightList (bool?): Specifies that this connection is being used as a highlight list.  
                Properties: create
        identify (bool?): Find out what type of selection connection this is.  May be:  
                activeList | modelList | keyframeList | worldList | objectList  
                listList | editorList | connection | unknown  
                Properties: query
        keyframeList (bool?): Specifies that this connection should reflect the animation  
                portion of the active list.  
                Properties: create
        lock (bool?): For activeList connections, locking the connection means that  
                it will not listen to activeList changes.  
                Properties: create, query, edit
        modelList (bool?): Specifies that this connection should reflect the modeling  
                (i.e. excluding keys) portion of the active list.  
                Properties: create
        object (Queryable[str]?): Specifies that this connection should wrap around the specified  
                object (which may be a set).  Query will return all the members of the  
                selection connection (if the connection wraps a set, the set members will  
                be returned)  
                Properties: create, query, edit
        parent (Queryable[str]?): The name of a UI object this should be attached to.  When the  
                parent is destroyed, the selectionConnection will auto-delete.  
                If no parent is specified, the connection is created in the  
                current controlLayout.  
                Properties: create, query, edit
        remove (str?): The name of a selection connection that should be removed from  
                this list of connections.  
                Properties: create, edit
        removeScript (Queryable[Callable[..., Any]]?): Specify a script to be called when something is removed from  
                the selection.  
                Properties: create, query, edit
        select (str?): Add something to the selection. This does not replace the  
                existing selection.  
                Properties: create, edit
        setList (bool?): Specifies that this connection should reflect all the sets in  
                the world.  
                Properties: create
        switch (bool?): Acts as a modifier to -connectionList which sets the list of objects  
                to be the first non-empty selection connection.  selection connections  
                are tested in the order in which they are added.  
                Properties: create, query
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        worldList (bool?): Specifies that this connection should reflect all objects  
                in the world.  
                Properties: create

    Returns:
        str: Value of the queried flag

    Example:
    """

