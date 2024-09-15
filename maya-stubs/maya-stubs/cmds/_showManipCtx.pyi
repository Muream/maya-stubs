from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showManipCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., addAttr: str = ..., currentNodeName: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., incSnap: Queryable[Multiuse[Tuple[int, bool]]] = ..., incSnapRelative: Queryable[Multiuse[Tuple[int, bool]]] = ..., incSnapUI: bool = ..., incSnapValue: Queryable[Multiuse[Tuple[int, float]]] = ..., iveVisible: bool = ..., lockSelection: bool = ..., moveActiveAttrDown: bool = ..., moveActiveAttrToTop: bool = ..., moveActiveAttrUp: bool = ..., name: str = ..., removeAttr: str = ..., resetActiveAttr: bool = ..., selectedAttributes: bool = ..., setAttrActive: str = ..., setNextAttrActive: bool = ..., setPreviousAttrActive: bool = ..., toggleIncSnap: bool = ..., toolFinish: Queryable[Callable[..., Any]] = ..., toolStart: Queryable[Callable[..., Any]] = ...) -> Union[str, bool, Multiuse[Tuple[int, bool]], Multiuse[Tuple[int, float]], Callable[..., Any]]:
    """This command can be used to create a show manip context.  The show manip
    context will display manips for all selected objects that have valid
    manips defined for them.
    Args:
        addAttr (str?): Add a specific attribute to the In View Editor attribute list.  
                Properties: edit
        currentNodeName (bool?): Returns the name of the first node that the context is attached to.  
                Properties: query
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
                Properties: create
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        incSnap (Queryable[Multiuse[Tuple[int, bool]]]?): If true, the manipulator owned by the context will use incremental snapping for specified mode.  
                Properties: create, query, edit, multiuse
        incSnapRelative (Queryable[Multiuse[Tuple[int, bool]]]?): If true, the manipulator owned by the context will use relative incremental snapping for specified mode.  
                Properties: create, query, edit, multiuse
        incSnapUI (bool?): Returns an array of elements indicating what kind of incremental snap UI is  
                required by the manipulator owned by the context.  
                If no UI is required, the result array will contain a single element  
                of with the value 0. The other values and their meanings are:  
              
                1. UI for linear incremental translate  
                2. UI for incremental rotate  
                3. UI for inclremental scale  
                Properties: query
        incSnapValue (Queryable[Multiuse[Tuple[int, float]]]?): Supply the step value which the manipulator owned by the context will use for specified mode.  
                Properties: create, query, edit, multiuse
        iveVisible (bool?): Set the In View Editor visible or not.  
                Properties: query, edit
        lockSelection (bool?): If true, this context will never change the current selection.  
                By default this is set to false.  
                Properties: create, query, edit
        moveActiveAttrDown (bool?): Move the In View Editor active attribute down one in the list.  
                Properties: edit
        moveActiveAttrToTop (bool?): Move the In View Editor active attribute to the top of the list.  
                Properties: edit
        moveActiveAttrUp (bool?): Move the In View Editor active attribute up one in the list.  
                Properties: edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        removeAttr (str?): Remove a specific attribute from the In View Editor attribute list.  
                Properties: edit
        resetActiveAttr (bool?): Reset the In View Editor active attribute to its default value.  
                Properties: edit
        selectedAttributes (bool?): Returns a list of the names of the attributes that are currently visible  
                in the In View Editor.  
                Properties: query
        setAttrActive (str?): Set a specific attribute from the In View Editor attribute list active.  
                Properties: edit
        setNextAttrActive (bool?): Set the next attribute in the In View Editor attribute list active.  
                Properties: edit
        setPreviousAttrActive (bool?): Set the previous attribute in the In View Editor attribute list active.  
                Properties: edit
        toggleIncSnap (bool?): Toggles (enables/disables) snapping for all modes.  
                Properties: create, edit
        toolFinish (Queryable[Callable[..., Any]]?): Supply the script that will be run when the user exits  
                the script.  
                Properties: create, query, edit
        toolStart (Queryable[Callable[..., Any]]?): Supply the script that will be run when the user first  
                enters the script  
                Properties: create, query, edit

    Returns:
        str: The name of the newly created context.

    Example:
    """

