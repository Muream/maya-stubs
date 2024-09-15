from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def selectPref(*, query: bool = ..., affectsActive: bool = ..., allowHiliteSelection: bool = ..., autoSelectContainer: bool = ..., autoSelectOutlinerSetMembers: bool = ..., autoUseDepth: bool = ..., clickBoxSize: Queryable[int] = ..., clickDrag: bool = ..., containerCentricSelection: bool = ..., disableComponentPopups: bool = ..., expandPopupList: bool = ..., ignoreSelectionPriority: bool = ..., manipClickBoxSize: Queryable[int] = ..., paintSelect: bool = ..., paintSelectWithDepth: bool = ..., popupMenuSelection: bool = ..., preSelectBackfacing: bool = ..., preSelectClosest: bool = ..., preSelectDeadSpace: Queryable[int] = ..., preSelectHilite: bool = ..., preSelectHiliteSize: Queryable[float] = ..., preSelectTweakDeadSpace: Queryable[int] = ..., selectTypeChangeAffectsActive: bool = ..., selectionChildHighlightMode: Queryable[int] = ..., singleBoxSelection: bool = ..., straightLineDistance: bool = ..., trackSelectionOrder: bool = ..., useDepth: bool = ..., xformNoSelect: bool = ...) -> Union[bool, int, float]:
    """This command controls state variables used to selection UI behavior.
    Args:
        affectsActive (bool?): Set affects-active toggle which when on  
                causes the active list to be affected when  
                changing between object and component  
                selection mode.  
                Properties: create, query
        allowHiliteSelection (bool?): When in component selection mode, allow selection of  
                objects for editing.  If an object is selected for  
                editing, it appears in the hilite color and its  
                selectable components are automatically displayed.  
                Properties: create, query
        autoSelectContainer (bool?): When enabled, with container centric selection also on, whenever the root transform is selected in the viewport, the container node will automatically be selected as well.  
                Properties: query
        autoSelectOutlinerSetMembers (bool?): When enabled selecting a set in the Outliner will automatically select the set members instead.  
                Properties: query
        autoUseDepth (bool?): When enabled, useDepth and paintSelectWithDepth will be automatically enabled  
                in shaded display mode and disabled in wireframe display mode.  
                Properties: query
        clickBoxSize (Queryable[int]?): When click selecting, this value defines the size of  
                square picking region surrounding the cursor. The size of  
                the square is twice the specified value. That is, the  
                value defines the amount of space on all four sides of the  
                cursor position. The size must be positive.  
                Properties: create, query
        clickDrag (bool?): Set click/drag selection interaction on/off  
                Properties: create, query
        containerCentricSelection (bool?): When enabled, selecting any DAG node in a container in the viewport will select the container's  
                root transform if there is one.  If there is no root transform then the highest  
                DAG node in the container will be selected.  There is no effect when selecting  
                nodes which are not in a container.  
                Properties: query
        disableComponentPopups (bool?): A separate preference to allow users to disable popup  
                menus when selecting components.  This pref is only meaningful  
                if the popupMenuSelection pref is enabled.  
                Properties: create, query
        expandPopupList (bool?): When in popup selection mode, if this is set then  
                all selection items that contain multiple objects or  
                components will be be expanded such that each object or  
                component will be a single new selection item.  
                Properties: create, query
        ignoreSelectionPriority (bool?): If this is set, selection priority will be ignored  
                when performing selection.  
                Properties: create, query
        manipClickBoxSize (Queryable[int]?): When selecting a manipulator, this value defines the size of  
                square picking region surrounding the cursor. The size of  
                the square is twice the specified value. That is, the  
                value defines the amount of space on all four sides of the  
                cursor position. The size must be positive.  
                Properties: create, query
        paintSelect (bool?): When enabled, the select tool will use drag selection instead of marquee selection.  
                Properties: query
        paintSelectWithDepth (bool?): When enabled, paint selection will not select components that are behind the surface  
                in the current camera view.  
                Properties: query
        popupMenuSelection (bool?): If this is set, a popup menu will be displayed  
                and used to determine the object to select. The menu  
                lists the current user box (marquee) of selected  
                candidate objects.  
                Properties: create, query
        preSelectBackfacing (bool?): When enabled preselection will highlight backfacing components whose normals face away from the camera.  
                Properties: query
        preSelectClosest (bool?): When enabled and the cursor is over a surface, preselection highlighting will try  
                to preselect the closest component to the cursor regardless of distance.  
                Properties: query
        preSelectDeadSpace (Queryable[int]?): This value defines the size of the region around the cursor used for preselection highlighting  
                when the cursor is outside the surface.  
                Properties: query
        preSelectHilite (bool?): When enabled, the closest component under the cursor will be highlighted to indicate that  
                clicking will select that component.  
                Properties: query
        preSelectHiliteSize (Queryable[float]?): This value defines the size of the region around the cursor used for preselection highlighting.  
                Within this region the closest component to the cursor will be highlighted.  
                Properties: query
        preSelectTweakDeadSpace (Queryable[int]?): This value defines the size of the region around the cursor used for preselection highlighting  
                when the cursor is outside the surface in tweak mode.  
                Properties: query
        selectTypeChangeAffectsActive (bool?): If true then the active list will be updated according to the new selection preferences.  
                Properties: query
        selectionChildHighlightMode (Queryable[int]?): Controls the highlighting of the children of a selected object. Valid modes are:  
              
                0. Always highlight children  
                1. Never highlight children  
                2. Use per-object "Selection Child Highlight" setting.  
              
                Default mode is (0): Always highlight children.  
              
                For (2), each DAG object has an individual "Selection Child Highlight" boolean flag.  
                By default, this flag will be TRUE. When mode (2) is enabled, the control is deferred  
                to the selected object's "Selection Child Highlight" flag.  
                Properties: create, query
        singleBoxSelection (bool?): Set single box selection on/off.  
                This flag indicates whether just single object  
                will be selected when the user box (marquee) selects  
                several objects if flag set to true.  Otherwise, all  
                those objects inside the box will be selected.  
                Properties: create, query
        straightLineDistance (bool?): If true then use straight line distances for selection proximity.  
                Properties: query
        trackSelectionOrder (bool?): When enabled, the order of selected objects and components will be tracked.  The 'ls' command will be able  
                to return the active list in the order of selection which will allow scripts to be written that depend  
                on the order.  
                Properties: query
        useDepth (bool?): When enabled, marquee selection will not select components that are behind the surface  
                in the current camera view.  
                Properties: query
        xformNoSelect (bool?): Disable selection in xform tools  
                Properties: create, query

    Returns:
        bool: in the query mode.

    Example:
    """

