from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeControl(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., animCurveNames: bool = ..., animLayerFilterOptions: Queryable[str] = ..., animLayerShowWeight: bool = ..., annotation: Queryable[str] = ..., backgroundColor: Queryable[Tuple[float, float, float]] = ..., beginScrub: bool = ..., currentFrameColor: Tuple[float, float, float, float] = ..., defineTemplate: str = ..., displaySound: bool = ..., docTag: Queryable[str] = ..., dragCallback: Callable[..., Any] = ..., dropCallback: Callable[..., Any] = ..., enable: bool = ..., enableBackground: bool = ..., enableKeyboardFocus: bool = ..., endScrub: bool = ..., exists: bool = ..., forceRedraw: bool = ..., forceRefresh: bool = ..., foregroundColor: Tuple[float, float, float] = ..., fullPathName: bool = ..., globalTime: bool = ..., height: Queryable[int] = ..., highlightColor: Queryable[Tuple[float, float, float]] = ..., isObscured: bool = ..., mainListConnection: Queryable[str] = ..., manage: bool = ..., noBackground: bool = ..., numberOfPopupMenus: bool = ..., parent: Queryable[str] = ..., popupMenuArray: bool = ..., pressCommand: Callable[..., Any] = ..., preventOverride: bool = ..., range: bool = ..., rangeArray: bool = ..., rangeVisible: bool = ..., releaseCommand: Callable[..., Any] = ..., repeatChunkSize: Queryable[float] = ..., repeatOnHold: bool = ..., resample: bool = ..., showKeys: Queryable[str] = ..., showKeysCombined: bool = ..., snap: bool = ..., sound: Queryable[str] = ..., statusBarMessage: str = ..., tickSize: Queryable[int] = ..., tickSpan: Queryable[int] = ..., useTemplate: str = ..., visible: bool = ..., visibleChangeCommand: Queryable[Callable[..., Any]] = ..., waveform: Queryable[str] = ..., width: Queryable[int] = ...) -> Union[str, bool, Tuple[float, float, float], int, float, Callable[..., Any]]:
    """This command creates a control that can be used for
    changing current time, displaying/editing keys, and
    displaying/scrubbing sound.: only one timeControl may be created.  The one Maya creates
    on startup can be accessed from the global string variable $gPlayBackSlider.
    Also, it is not a good idea to delete it.
    Args:
        animCurveNames (bool?): When "showKeys" is not "none", querying this flag will  
                return the names of all the animCurves for which keyframe  
                ticks are being displayed.  Query returns string[].  
                Properties: create, query
        animLayerFilterOptions (Queryable[str]?): Specifies whether a filter is to be applied when displaying animation layers.  
                If so, the options can be "allAffecting" (no filter), "active" (only the active  
                layers on the object will be displayed) and "animLayerEditor" (the settings will  
                be taken from the animation layer editor).  
                Properties: create, query, edit
        animLayerShowWeight (bool?): Specifies or queries whether weights are to be shown when displaying animation layers.  
                Properties: create, query, edit
        annotation (Queryable[str]?): Annotate the control with an extra string value.  
                Properties: create, query, edit
        backgroundColor (Queryable[Tuple[float, float, float]]?): The background color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                When setting backgroundColor, the background is automatically  
                enabled, unless enableBackground is also specified with a false  
                value.  
                Properties: create, query, edit
        beginScrub (bool?): Set this widget up for sound scrubbing.  
                Subsequent changes to current time will result  
                in "sound scrubbing" behavior, until the  
                "-endScrub" command is issued for this widget.  
                Properties: edit
        currentFrameColor (Tuple[float, float, float, float]?): This flag is used to specify the rgba color of the  
                current frame overlay rectangle in the timeControl.  
                Properties: edit
        defineTemplate (str?): Puts the command in a mode where any other flags and arguments are  
                parsed and added to the command template specified in the argument.  
                They will be used as default arguments in any subsequent  
                invocations of the command when templateName is set as the  
                current template.  
                Properties: create
        displaySound (bool?): Turn sound display off.  Query returns int.  
                Properties: query, edit
        docTag (Queryable[str]?): Add a documentation flag to the control.  The documentation flag  
                has a directory structure.  
                (e.g., -dt render/multiLister/createNode/material)  
                Properties: create, query, edit
        dragCallback (Callable[..., Any]?): Adds a callback that is called when the middle mouse button  
                is pressed.  The MEL version of the callback is of the form:  
              
                global proc string[] callbackName(string $dragControl, int $x, int $y, int $mods)  
              
                The proc returns a string array that is transferred to the drop site.  
                By convention the first string in the array describes the user settable  
                message type.  Controls that are application defined drag sources may  
                ignore the callback. $mods allows testing for the key modifiers CTRL and  
                SHIFT. Possible values are 0 == No modifiers, 1 == SHIFT, 2 == CTRL,  
                3 == CTRL + SHIFT.  
              
                In Python, it is similar, but there are two ways to specify the callback.  The  
                recommended way is to pass a Python function object as the argument.  In that  
                case, the Python callback should have the form:  
              
                def callbackName( dragControl, x, y, modifiers ):  
              
                The values of these arguments are the same as those for the MEL version above.  
              
                The other way to specify the callback in Python is to specify a string to be  
                executed.  In that case, the string will have the values substituted into it  
                via the standard Python format operator.  The format values are passed in a  
                dictionary with the keys "dragControl", "x", "y", "modifiers".  The  
                "dragControl" value is a string and the other values are integers (eg the  
                callback string could be "print '%(dragControl)s %(x)d %(y)d %(modifiers)d'")  
                Properties: create, edit
        dropCallback (Callable[..., Any]?): Adds a callback that is called when a drag and drop  
                operation is released above the drop site.  The MEL version of the callback is  
                of the form:  
              
                global proc callbackName(string $dragControl, string $dropControl, string $msgs[], int $x, int $y, int $type)  
              
                The proc receives a string array that is transferred from the drag source.  
                The first string in the msgs array describes the user defined message type.  
                Controls that are application defined drop sites may ignore the  
                callback. $type can have values of 1 == Move, 2 == Copy, 3 == Link.  
              
                In Python, it is similar, but there are two ways to specify the callback.  The  
                recommended way is to pass a Python function object as the argument.  In that  
                case, the Python callback should have the form:  
              
                def pythonDropTest( dragControl, dropControl, messages, x, y, dragType ):  
              
                The values of these arguments are the same as those for the MEL version above.  
              
                The other way to specify the callback in Python is to specify a string to be  
                executed.  In that case, the string will have the values substituted into it  
                via the standard Python format operator.  The format values are passed in a  
                dictionary with the keys "dragControl", "dropControl", "messages", "x", "y",  
                "type".  The "dragControl" value is a string and the other values are integers  
                (eg the callback string could be  
                "print '%(dragControl)s %(dropControl)s %(messages)r %(x)d %(y)d %(type)d'")  
                Properties: create, edit
        enable (bool?): The enable state of the control.  By default, this flag is  
                set to true and the control is enabled.  Specify false and the control  
                will appear dimmed or greyed-out indicating it is disabled.  
                Properties: create, query, edit
        enableBackground (bool?): Enables the background color of the control.  
                Properties: create, query, edit
        enableKeyboardFocus (bool?): If enabled, the user can navigate to the control with the tab key and select values with the keyboard or mouse.  
                This flag would typically be used to turn off focus support from controls that get it by default, like Edit and List controls.  
                If disabled, text in text fields can still be selected with the mouse but cannot be copied (except on Linux when "Middle Click Paste" is enabled).  
                Properties: create, query, edit
        endScrub (bool?): End sound scubbing for this widget.  This stops  
                sound scrubbing behavior and should be issued  
                before any subsequent "-beginScrub" flags  
                Properties: edit
        exists (bool?): Returns whether the  
                specified object exists or not. Other flags are ignored.  
                Properties: create
        forceRedraw (bool?): Force a redraw of the time control UI. Similiar to forceRefresh but  
                does not rebuild key information.  
                Properties: create, edit
        forceRefresh (bool?): Force a refresh of the time control UI.  
                Properties: create, edit
        foregroundColor (Tuple[float, float, float]?): This flag is used to specify the rgb color of the  
                vertical lines and numeric text in the timeControl.  
                Properties: edit
        fullPathName (bool?): Return the full path name of the widget, which includes all the parents.  
                Properties: query
        globalTime (bool?): "true" means this widget controls and displays the global,  
                dependency graph time.  "false" means time changes here  
                do NOT affect the dependency graph. Query returns int.  
                Properties: create, query, edit
        height (Queryable[int]?): The height of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit
        highlightColor (Queryable[Tuple[float, float, float]]?): The highlight color of the control. The arguments correspond  
                to the red, green, and blue color components. Each component ranges  
                in value from 0.0 to 1.0.  
                Properties: create, query, edit
        isObscured (bool?): Return whether the control can actually be seen by the user.  
                The control will be obscured if its state is invisible, if it is  
                blocked (entirely or partially) by some other control, if it or a  
                parent layout is unmanaged, or if the control's window is  
                invisible or iconified.  
                Properties: query
        mainListConnection (Queryable[str]?): Specifies the name of a selectionConnection object that the  
                time slider will use as its source of content.  The time slider will  
                only display keys for items contained in the selectionConnection object.  
                Properties: create, query, edit
        manage (bool?): Manage state of the control.  An unmanaged control is  
                not visible, nor does it take up any screen real estate.  All  
                controls are created managed by default.  
                Properties: create, query, edit
        noBackground (bool?): Clear/reset the control's background.  
                Passing true means the background should not be drawn at all, false means the background should be drawn.  The state of this flag is inherited by children of this control.  
                Properties: create, edit
        numberOfPopupMenus (bool?): Return the number of popup menus attached to this control.  
                Properties: query
        parent (Queryable[str]?): The parent layout for this control.  
                Properties: create, query
        popupMenuArray (bool?): Return the names of all the popup menus attached to this  
                control.  
                Properties: query
        pressCommand (Callable[..., Any]?): script to run on mouse-down in this control.  
                Properties: create, edit
        preventOverride (bool?): If true, this flag prevents overriding the control's  
                attribute via the control's right mouse button menu.  
                Properties: create, query, edit
        range (bool?): Returns string representing the currently highlighted  
                range visible on the time slider.  A range from 10 to 20  
                would be returned as "10. 20".  When there's no range  
                visible on the time slider, the query returns a range  
                spanning the current time: for example, "10. 11".  These  
                values are in the current time unit.  
                Properties: create, query
        rangeArray (bool?): Returns a float array representing the currently highlighted  
                range visible on the time slider.  A range from 10 to 20  
                would be returned as { 10.0, 20.0 }.  When there's no range  
                visible on the time slider, the query returns values spanning  
                the current time: { 10.0, 11.0 }.  These values are in the current time unit.  
                Properties: create, query
        rangeVisible (bool?): Returns true if a currently highlighted range is visible  
                on the time slider, false if no.  
                Properties: create, query
        releaseCommand (Callable[..., Any]?): script to run on mouse-up in this control.  
                Properties: create, edit
        repeatChunkSize (Queryable[float]?): How much sound (in the current time unit) is repeated  
                when -repeatOnHold is true.  Default is 1.0.  
                Properties: query, edit
        repeatOnHold (bool?): Repeat sound during mouse-down events  
                Properties: query, edit
        resample (bool?): Resample the sound display to fit the widget  
                Properties: edit
        showKeys (Queryable[str]?): "active" will show tick marks for keyframes on all active  
                objects.  "none" shows no tick marks.  Any other name is  
                taken as the name of a channel box whose selected attributes  
                will display tick marks.  Default "active".  Query returns string.  
                Properties: create, query, edit
        showKeysCombined (bool?): This flag can be used in conjunction with the showKeys flag to  
                enable a combination of "active" + "channel box" behavior.  
                Specifically, if channel box attributes are selected, tick marks will  
                be shown for those attributes. If no channel box attributes are  
                selected, tick marks will be shown for keyframes on all active objects.  
                Properties: create, query, edit
        snap (bool?): "true" means this widget is constrained to having  
                values that are integers representing the current time unit..  
                "false" means the current time indicator is "free floating"  
                and not constrained.  
                Properties: create, query, edit
        sound (Queryable[str]?): Name of audio depend node whose data should display in the  
                sound-display widget. Query returns string.  
                Properties: query, edit
        statusBarMessage (str?): Extra string to display in the status bar when the mouse is over the control.  
                Properties: create, edit
        tickSize (Queryable[int]?): Specifies the width of keyframe ticks drawn in the time slider.  
                The value will be clamped to the range [1, 63].  
                Properties: create, query, edit
        tickSpan (Queryable[int]?): Specifies the interval between keyframe ticks in the timeControl. For example,  
                a value of 10, will place ticks at 0, 10, 20, etc.  
                Properties: create, query, edit
        useTemplate (str?): Forces the command to use a command template other than  
                the current one.  
                Properties: create
        visible (bool?): The visible state of the control.  A control is created  
                visible by default.  Note that a control's actual appearance is  
                also dependent on the visible state of its parent layout(s).  
                Properties: create, query, edit
        visibleChangeCommand (Queryable[Callable[..., Any]]?): Command that gets executed when visible state of the control changes.  
                Properties: create, query, edit
        waveform (Queryable[str]?): Determines what part of the sound waveform to display,  
                when -displaySound is "true". Valid values are "top", "bottom",  
                and "both".  Default is "top". Query returns string.  
                Properties: query, edit
        width (Queryable[int]?): The width of the control.  The control will attempt to  
                be this size if it is not overruled by parent layout conditions.  
                Properties: create, query, edit

    Returns:
        str: Name of created or edited control

    Example:
    """

