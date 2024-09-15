from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def animCurveEditor(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., areCurvesSelected: bool = ..., autoFit: Queryable[str] = ..., autoFitTime: Queryable[str] = ..., classicMode: bool = ..., clipTime: Queryable[str] = ..., constrainDrag: Queryable[int] = ..., control: bool = ..., curvesShown: bool = ..., curvesShownForceUpdate: bool = ..., defineTemplate: str = ..., denormalizeCurvesCommand: str = ..., displayActiveKeyTangents: str = ..., displayActiveKeys: str = ..., displayInfinities: str = ..., displayKeys: str = ..., displayNormalized: bool = ..., displayTangents: str = ..., displayValues: str = ..., docTag: Queryable[str] = ..., exists: bool = ..., filter: Queryable[str] = ..., forceMainConnection: Queryable[str] = ..., highlightAffectedCurves: bool = ..., highlightConnection: Queryable[str] = ..., keyMinScale: Queryable[float] = ..., keyScale: Queryable[float] = ..., keyingTime: Queryable[str] = ..., limitToSelectedCurves: bool = ..., lockMainConnection: bool = ..., lockPlayRangeShades: Queryable[str] = ..., lookAt: str = ..., mainListConnection: Queryable[str] = ..., menu: Callable[..., Any] = ..., normalizeCurvesCommand: str = ..., outliner: Queryable[str] = ..., panel: Queryable[str] = ..., parent: Queryable[str] = ..., preSelectionHighlight: bool = ..., renormalizeCurves: bool = ..., resultSamples: Queryable[int] = ..., resultScreenSamples: Queryable[int] = ..., resultUpdate: Queryable[str] = ..., selectionConnection: Queryable[str] = ..., showActiveCurveNames: bool = ..., showBufferCurves: Queryable[str] = ..., showCurveNames: bool = ..., showPlayRangeShades: Queryable[str] = ..., showResults: Queryable[str] = ..., showUpstreamCurves: bool = ..., simpleKeyView: bool = ..., smoothness: Queryable[str] = ..., snapTime: Queryable[str] = ..., snapValue: Queryable[str] = ..., stackedCurves: bool = ..., stackedCurvesMax: Queryable[float] = ..., stackedCurvesMin: Queryable[float] = ..., stackedCurvesSpace: Queryable[float] = ..., stateString: bool = ..., timelinePositionTop: bool = ..., unParent: bool = ..., unlockMainConnection: bool = ..., updateMainConnection: bool = ..., useTemplate: str = ..., valueLinesToggle: str = ...) -> Union[str, bool, int, float]:
    """Edit a characteristic of a graph editor
    Args:
        areCurvesSelected (bool?): Returns a boolean to know if at least one curve is selected in the graph editor.  
                Properties: query
        autoFit (Queryable[str]?): on | off | tgl  
                Auto fit-to-view.  
                Properties: query, edit
        autoFitTime (Queryable[str]?): on | off | tgl  
                Auto fit-to-view along the time axis, as well.  
                Properties: query, edit
        classicMode (bool?): When on, the graph editor is displayed in "Classic Mode", otherwise "Suites Mode" is used.  
                Properties: query, edit
        clipTime (Queryable[str]?): Valid values: "on" "off"  
                Display the clips with their offset and scale  
                applied to the anim curves in the clip.  
                Properties: query, edit
        constrainDrag (Queryable[int]?): Constrains all Graph Editor animation curve drag operations  
                to either the X-axis, the Y-axis, or to neither of those axes.  
                Values to supply are: 0 for not constraining any axis,  
                1 for constraing the X-axis, or 2 for constraining the Y-axis.  
                When used in queries, this flag returns the latter values and  
                these values have the same interpretation as above.  
                Note: when the shift key is pressed before dragging the animation  
                curve, the first mouse movement will instead determine (and override)  
                any prior set constrained axis.  
                Properties: create, query, edit
        control (bool?): Query only. Returns the top level control for this editor.  
                Usually used for getting a parent to attach popup menus.  
                Caution: It is possible for an editor to exist without a  
                control. The query will return "NONE" if no control is present.  
                Properties: query
        curvesShown (bool?): Returns a string array containing the names of the animCurve nodes  
                currently displayed in the graph editor.  
                Properties: query
        curvesShownForceUpdate (bool?): Returns a string array containing the names of the animCurve nodes  
                currently displayed in the graph editor. Unlike the curvesShown flag,  
                this will force an update of the graph editor for the case where  
                the mainListConnection has been modified since the last refresh.  
                Properties: query
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        denormalizeCurvesCommand (str?): Sets the script that is run to denormalize curves in the graph editor.  
                This is intended for internal use only.  
                Properties: create, edit
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
        displayNormalized (bool?): When on, display all curves normalized to the range -1 to +1.  
                Properties: query, edit
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
        highlightAffectedCurves (bool?): When on, highlights the curve segment affected by the selected key/tangent  
                Properties: query, edit
        highlightConnection (Queryable[str]?): Specifies the name of a selectionConnection object that  
                the editor will synchronize with its highlight list. Not all  
                editors have a highlight list. For those that do, it is a secondary  
                selection list.  
                Properties: create, query, edit
        keyMinScale (Queryable[float]?): The minimum key selection size in the graph editor.  
                A value of 0.0 means there is no minimum size.  
                A value of 1.0 means the minimum size is the size of a key with keyScale set to 1.0  
                Properties: query, edit
        keyScale (Queryable[float]?): Scales the key size in the graph editor  
                Properties: query, edit
        keyingTime (Queryable[str]?): The current time in the given curve to be keyed in the graph editor.  
                Properties: query
        limitToSelectedCurves (bool?): When on, marquee selection refines the current selection and only  
                affects curves with active keys or tangents.  When off (or when  
                there are no curves, keys, or tangents selected), performs a  
                normal marquee selection and replaces the current selection with  
                everything that is selectable inside the marquee.  
                Properties: query, edit
        lockMainConnection (bool?): Locks the current list of objects within the mainConnection,  
                so that only those objects are displayed within the editor.  
                Further changes to the original mainConnection are ignored.  
                Properties: create, edit
        lockPlayRangeShades (Queryable[str]?): Valid values: "on" "off" "tgl"  
                Lock Play Range Shades.  
                Properties: query, edit
        lookAt (str?): all | selected | currentTime  
                FitView helpers.  
                Properties: edit
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will use as its source of content. The editor will  
                only display items contained in the selectionConnection object.  
                Properties: create, query, edit
        menu (Callable[..., Any]?): Specify a script to be run when the editor  
                is created.  The function will be passed one string  
                argument which is the new editor's name.  
                Properties: create
        normalizeCurvesCommand (str?): Sets the script that is run to normalize curves in the graph editor.  
                This is intended for internal use only.  
                Properties: create, edit
        outliner (Queryable[str]?): The name of the outliner that is associated with the graph editor.  
                Properties: query, edit
        panel (Queryable[str]?): Specifies the panel for this editor. By default if  
                an editor is created in the create callback of a scripted panel it  
                will belong to that panel. If an editor does not belong to a panel  
                it will be deleted when the window that it is in is deleted.  
                Properties: create, query
        parent (Queryable[str]?): Specifies the parent layout for this editor. This flag will only  
                have an effect if the editor is currently un-parented.  
                Properties: create, query, edit
        preSelectionHighlight (bool?): When on, the curve/key/tangent under the mouse pointer is highlighted  
                to ease selection.  
                Properties: query, edit
        renormalizeCurves (bool?): This flag causes the curve normalization factors to be recalculated.  
                Properties: edit
        resultSamples (Queryable[int]?): Specify the sampling for result curves  
                Note: the smaller this number is, the longer it will  
                take to update the display.  
                Properties: query, edit
        resultScreenSamples (Queryable[int]?): Specify the screen base result sampling for result curves.  
                If 0, then results are sampled in time.  
                Properties: query, edit
        resultUpdate (Queryable[str]?): Valid values: "interactive" "delayed"  
                Controls how changes to animCurves are reflected in the  
                result curves (if results are being shown).  If resultUpdate  
                is "interactive", then as interactive changes are being made  
                to the animCurve, the result curves will be updated.  If  
                modelUpdate is delayed (which is the default setting), then  
                result curves are updated once the final change to an  
                animCurve has been made.  
                Properties: query, edit
        selectionConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                editor will synchronize with its own selection list. As the user  
                selects things in this editor, they will be selected in the  
                selectionConnection object. If the object undergoes changes, the  
                editor updates to show the changes.  
                Properties: create, query, edit
        showActiveCurveNames (bool?): Display the active curve(s)'s name.  
                Properties: query, edit
        showBufferCurves (Queryable[str]?): Valid values: "on" "off" "tgl"  
                Display buffer curves.  
                Properties: query, edit
        showCurveNames (bool?): Display the curves's name.  
                Properties: query, edit
        showPlayRangeShades (Queryable[str]?): Valid values: "on" "off" "tgl"  
                Display Play Range Shades.  
                Properties: query, edit
        showResults (Queryable[str]?): Valid values: "on" "off" "tgl"  
                Display result curves from expression or other non-keyed  
                action.  
                Properties: query, edit
        showUpstreamCurves (bool?): If true, the dependency graph is searched upstream for all curves  
                that drive the selected plugs (showing multiple curves for example  
                in a typical driven key setup, where first the driven key curve is  
                encountered, followed by the actual animation curve that drives the  
                source object). If false, only the first curves encountered  
                will be shown. Note that, even if false, multiple curves can be shown  
                if e.g. a blendWeighted node is being used to combine multiple curves.  
                Properties: query, edit
        simpleKeyView (bool?): on | off  
                Display simpler and smaller key.  
                Properties: query, edit
        smoothness (Queryable[str]?): Valid values: "coarse" "rough" "medium" "fine"  
                Specify the display smoothness of animation curves.  
                Properties: query, edit
        snapTime (Queryable[str]?): none | integer | keyframe  
                Keyframe move snap in time.  
                Properties: query, edit
        snapValue (Queryable[str]?): none | integer | keyframe  
                Keyframe move snap in values.  
                Properties: query, edit
        stackedCurves (bool?): Switches the display mode between normal (all curves sharing one set of axes)  
                to stacked (each curve on its own value axis, stacked vertically).  
                Properties: query, edit
        stackedCurvesMax (Queryable[float]?): Sets the maximum value on the per-curve value axis when in stacked mode.  
                Properties: query, edit
        stackedCurvesMin (Queryable[float]?): Sets the minimum value on the per-curve value axis when in stacked mode.  
                Properties: query, edit
        stackedCurvesSpace (Queryable[float]?): Sets the spacing between curves when in stacked mode.  
                Properties: query, edit
        stateString (bool?): Query only flag. Returns the MEL command that will create an  
                editor to match the current editor state. The returned command string  
                uses the string variable $editorName in place of a specific name.  
                Properties: query
        timelinePositionTop (bool?): on | off | tgl  
                Display timeline either at the top or bottom.  
                Properties: query, edit
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
        valueLinesToggle (str?): on | off | tgl  
                Display the value lines for high/low/zero of selected curves in the editor  
                Properties: edit

    Returns:
        str: Editor name

    Example:
    """

