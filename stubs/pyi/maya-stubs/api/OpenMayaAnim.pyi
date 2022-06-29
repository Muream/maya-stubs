from typing import *
from typing_extensions import Self

if TYPE_CHECKING:
    from _typeshed import Incomplete
else:
    Incomplete = Any
from maya.api.OpenMaya import *

__builtins__: dict
__cached__: str
__doc__: NoneType
__file__: str
__loader__: SourceFileLoader
__name__: str
__package__: str
__spec__: ModuleSpec
key: str
ourdict: dict
py2dict: dict
val: str

class MAnimControl:
    __doc__: str = ...
    def animationEndTime(self, *args: Any, **kwargs: Any) -> Any:
        """animationEndTime() -> MTime

        Return an MTime specifying the last frame of the animation, as specified by the Maya user in the Range Slider UI.
        """
    def animationStartTime(self, *args: Any, **kwargs: Any) -> Any:
        """animationStartTime() -> MTime

        Return an MTime specifying the first frame of the animation, as specified by the Maya user in the Range Slider UI.
        """
    def autoKeyMode(self, *args: Any, **kwargs: Any) -> Any:
        """autoKeyMode() -> bool

        Return the autoKeyMode.
        """
    def currentTime(self, *args: Any, **kwargs: Any) -> Any:
        """currentTime() -> MTime

        Return an MTime instance containing the current animation frame.
        """
    def globalInTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """globalInTangentType() -> int

        Return the current global in tangent type.
        """
    def globalOutTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """globalOutTangentType() -> int

        Return the current global out tangent type.
        """
    def isPlaying(self, *args: Any, **kwargs: Any) -> Any:
        """isPlaying() -> bool

        Return a value indicating whether Maya is currently playing the animation
        """
    def isScrubbing(self, *args: Any, **kwargs: Any) -> Any:
        """isScrubbing() -> bool

        Return a value indicating whether interactive scrubbing is occuring while Maya is not currently playing an animation.
        """
    kPlaybackLoop: int = ...
    kPlaybackOnce: int = ...
    kPlaybackOscillate: int = ...
    kPlaybackViewActive: int = ...
    kPlaybackViewAll: int = ...
    def maxTime(self, *args: Any, **kwargs: Any) -> Any:
        """maxTime() -> MTime

        Return an MTime specifying the last frame of the current playback time range.
        """
    def minTime(self, *args: Any, **kwargs: Any) -> Any:
        """minTime() -> MTime

        Return an MTime specifying the first frame of the current playback time range.
        """
    def playBackward(self, *args: Any, **kwargs: Any) -> Any:
        """playBackward() -> None

        Start playing the current animation backwards.
        """
    def playForward(self, *args: Any, **kwargs: Any) -> Any:
        """playForward() -> None

        Start playing the current animation forwards.
        """
    def playbackBy(self, *args: Any, **kwargs: Any) -> Any:
        """playbackBy() -> float

        Return a float specifying the increment between times viewed during the playing of the animation.
        """
    def playbackMode(self, *args: Any, **kwargs: Any) -> Any:
        """playbackMode() -> int

        Return the playback mode currently in effect:
          MAnimControl.kPlaybackOnce         Play once then stop.
          MAnimControl.kPlaybackLoop         Play continuously.
          MAnimControl.kPlaybackOscillate    Play forwards, then backwards continuously.
        """
    def playbackSpeed(self, *args: Any, **kwargs: Any) -> Any:
        """playbackSpeed() -> float

        Return the speed with with to play the animation.
        """
    def setAnimationEndTime(self, *args: Any, **kwargs: Any) -> Any:
        """setAnimationEndTime(MTime) -> None

        Set the value of the last frame in the animation.
        """
    def setAnimationStartEndTime(self, *args: Any, **kwargs: Any) -> Any:
        """setAnimationStartEndTime(MTime, MTime) -> None

        Set the values of the first and last frames in the animation.
        """
    def setAnimationStartTime(self, *args: Any, **kwargs: Any) -> Any:
        """setAnimationStartTime(MTime) -> None

        Set the value of the first frame in the animation.
        """
    def setAutoKeyMode(self, *args: Any, **kwargs: Any) -> Any:
        """setAutoKeyMode(bool) -> None

        Set the autoKeyMode.
        """
    def setCurrentTime(self, *args: Any, **kwargs: Any) -> Any:
        """setMinTime(MTime) -> None

        Set the current animation frame.
        """
    def setGlobalInTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """setGlobalInTangentType(int) -> None

        Set the current global in tangent type
        """
    def setGlobalOutTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """setGlobalOutTangentType(int) -> None

        Set the current global out tangent type.
        """
    def setMaxTime(self, *args: Any, **kwargs: Any) -> Any:
        """setMaxTime(MTime) -> None

        Set the value of the last frame of the current playback time range.
        """
    def setMinMaxTime(self, *args: Any, **kwargs: Any) -> Any:
        """setMinMaxTime(MTime, MTime) -> None

        Set the values of the first and last frames of the playback time range.
        """
    def setMinTime(self, *args: Any, **kwargs: Any) -> Any:
        """setMinTime(MTime) -> None

        Set the value of the first frame of the current playback time range.
        """
    def setPlaybackBy(self, *args: Any, **kwargs: Any) -> Any:
        """setPlaybackBy(float) -> None

        Specify the increment between times viewed during the playing of the animation.
        """
    def setPlaybackMode(self, *args: Any, **kwargs: Any) -> Any:
        """setPlaybackMode(int) -> None

        Set the current playback mode.
        """
    def setPlaybackSpeed(self, *args: Any, **kwargs: Any) -> Any:
        """setPlaybackSpeed(float) -> None

        Set the desired speed factor at which the animation will play back.
        """
    def setViewMode(self, *args: Any, **kwargs: Any) -> Any:
        """setViewMode(int) -> None

        Set the current viewing mode.
        Controls whether the animation is run in only the active view, or simultaneously in all views.
        """
    def setWeightedTangents(self, *args: Any, **kwargs: Any) -> Any:
        """setWeightedTangents(bool) -> None

        Sets whether or not the tangents on the Anim Curve are weighted.
        """
    def stop(self, *args: Any, **kwargs: Any) -> Any:
        """stop() -> None

        Stop playing the current animation.
        """
    def viewMode(self, *args: Any, **kwargs: Any) -> Any:
        """viewMode() -> int

        Return the viewing mode currently in effect:
          MAnimControl.kPlaybackViewAll      Playback in all views.
          MAnimControl.kPlaybackViewActive   Playback in only the active view.
        """
    def weightedTangents(self, *args: Any, **kwargs: Any) -> Any:
        """weightedTangents() -> bool

        Determine whether or not the tangents on the Anim Curve are weighted.
        """

class MAnimCurveChange:
    __doc__: str = ...
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def redoIt(self, *args: Any, **kwargs: Any) -> Any:
        """Redo all of the Anim Curve changes in this cache."""
    def undoIt(self, *args: Any, **kwargs: Any) -> Any:
        """Undo all of the Anim Curve changes in this cache."""

class MAnimCurveClipboard:
    __doc__: str = ...
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clears the clipboard.
        """
    def clipboardItems(self, *args: Any, **kwargs: Any) -> Any:
        """clipboardItems() -> MAnimCurveClipboardItemArray

        Returns the clipboard items.
        """
    @property
    def endTime(*args: Any, **kwargs: Any) -> Any:
        """The end time of the clipboard."""
    @endTime.setter
    def endTime(*args: Any, **kwargs: Any) -> Any:
        """The end time of the clipboard."""
    @property
    def endUnitlessInput(*args: Any, **kwargs: Any) -> Any:
        """The end unitless input of the clipboard."""
    @endUnitlessInput.setter
    def endUnitlessInput(*args: Any, **kwargs: Any) -> Any:
        """The end unitless input of the clipboard."""
    @property
    def isEmpty(*args: Any, **kwargs: Any) -> Any:
        """Whether the clipboard is empty."""
    @isEmpty.setter
    def isEmpty(*args: Any, **kwargs: Any) -> Any:
        """Whether the clipboard is empty."""
    def set(self, *args: Any, **kwargs: Any) -> Any:
        """set( clipboard ) -> self
        set( items ) -> self
        set( items, startTime, endTime, startUnitlessInput, endUnitlessInput, strictValidation=True ) -> self

        Sets the content of the clipboard.
        'items' may be either an MAnimClipboardItemArray or a sequence of MAnimClipboardItems.
        """
    @property
    def startTime(*args: Any, **kwargs: Any) -> Any:
        """The start time of the clipboard."""
    @startTime.setter
    def startTime(*args: Any, **kwargs: Any) -> Any:
        """The start time of the clipboard."""
    @property
    def startUnitlessInput(*args: Any, **kwargs: Any) -> Any:
        """The start unitless input of the clipboard."""
    @startUnitlessInput.setter
    def startUnitlessInput(*args: Any, **kwargs: Any) -> Any:
        """The start unitless input of the clipboard."""
    theAPIClipboard: MAnimCurveClipboard = ...

class MAnimCurveClipboardItem:
    __doc__: str = ...
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    @property
    def animCurve(*args: Any, **kwargs: Any) -> Any:
        """The anim curve."""
    @animCurve.setter
    def animCurve(*args: Any, **kwargs: Any) -> Any:
        """The anim curve."""
    def animCurveType(self, *args: Any, **kwargs: Any) -> Any:
        """animCurveType() -> MFnAnimCurve.AnimCurveType

        Returns the type of the item's anim curve.
        """
    @property
    def fullAttributeName(*args: Any, **kwargs: Any) -> Any:
        """The full attribute name."""
    @fullAttributeName.setter
    def fullAttributeName(*args: Any, **kwargs: Any) -> Any:
        """The full attribute name."""
    def getAddressingInfo(self, *args: Any, **kwargs: Any) -> Any:
        """getAddressingInfo() -> (unsigned int, unsigned int, unsigned int)

        Returns the addressing information for this clipboard item
        as (rowCount, childCount, attributeCount).
        """
    @property
    def leafAttributeName(*args: Any, **kwargs: Any) -> Any:
        """The leaf attribute name."""
    @leafAttributeName.setter
    def leafAttributeName(*args: Any, **kwargs: Any) -> Any:
        """The leaf attribute name."""
    @property
    def nodeName(*args: Any, **kwargs: Any) -> Any:
        """The node name."""
    @nodeName.setter
    def nodeName(*args: Any, **kwargs: Any) -> Any:
        """The node name."""
    def setAddressingInfo(self, *args: Any, **kwargs: Any) -> Any:
        """setAddressingInfo(rowCount, childCount, attributeCount) -> self

        Sets the addressing information for this clipboard item.
        """
    def setAnimCurve(self, *args: Any, **kwargs: Any) -> Any:
        """setAnimCurve(object) -> self

        Sets the anim curve MObject.
        """
    def setNameInfo(self, *args: Any, **kwargs: Any) -> Any:
        """setNameInfo(nodeName, fullName, leafName) -> self

        Sets the name information for this clipboard item.
        """

class MAnimCurveClipboardItemArray:
    def __add__(self, value: Any) -> Any:
        """Return self+value."""
    def __contains__(self, key: Any) -> Any:
        """Return key in self."""
    def __delitem__(self, key: Any) -> Any:
        """Delete self[key]."""
    __doc__: str = ...
    def __getitem__(self, key: Any) -> Any:
        """Return self[key]."""
    def __iadd__(self, value: Any) -> Any:
        """Implement self+=value."""
    def __imul__(self, value: Any) -> Any:
        """Implement self*=value."""
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __len__(self) -> Any:
        """Return len(self)."""
    def __mul__(self, value: Any) -> Any:
        """Return self*value."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __repr__(self) -> Any:
        """Return repr(self)."""
    def __rmul__(self, value: Any) -> Any:
        """Return value*self."""
    def __setitem__(self, key: Any, value: Any) -> Any:
        """Set self[key] to value."""
    def __str__(self) -> Any:
        """Return str(self)."""
    def append(self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MAnimMessage(MMessage):
    __doc__: str = ...
    def addAnimCurveEditedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addAnimCurveEditedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an
        AnimCurve is edited.

         * function - callable which will be passed a MObjectArray object containing
           an array of AnimCurves which have been edited, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addAnimKeyframeEditCheckCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addAnimKeyframeEditCheckCallback(function, clientData=None) -> id

        This method registers a callback that is used by the setKeyframe command
        to allow a user to consider the set keyframe request and cancel it if
        needed. The callback method should return False to abort the keyframe
        setting.

         * function - callable which will be passed a MPlug indicating the
           plug being keyframed and the clientData object.
           Return False to abort the keyframe action, otherwise return True
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addAnimKeyframeEditedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addAnimKeyframeEditedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an
        a group of keys are modified.  The callback is invoked once per
        atomic change to single or group of keyframes. For example, if
        a user selects a group 5 of keys and moves them 5 units in the value
        axis, then a single callback event will be invoked with a MObject
        for each of the 5 keyframes.  The MObjects can then be used in the
        MFnKeyframeDelta function set. Refer to MFnKeyframeDelta function set
        documentation for more info.

         * function - callable which will be passed a MObjectArray object containing
           an array of keyframes that were edited, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addDisableImplicitControlCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addDisableImplicitControlCallback(function, clientData=None) -> id

        This method registers a callback that is called from bakeResults
        command after baking operation is completed, if disableImplicitControl
        is enabled. One example usage of this callback is to create the anim curve
        that is used to drive Maya rigidbody's bakeSimulationIndex, which defines
        if the rigid body should take its input from anim curve or rigid body
        simulation.

         * function - callable which will be passed a MPlugArray containing the baked plugs
           (they can be replaced but must have the same number of plugs), a MDGModifier used
           if bakeResults command is undone or redone and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeAnimKeyframeEditedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addNodeAnimKeyframeEditedCallback(animNode, function, clientData=None) -> id

        This method registers a callback that is called whenever an a
        group of keys are modified.  The callback is invoked once per
        atomic change to single or group of keyframes on the specified
        animation curve node. For example, if a user selects a group 5
        of keys and moves them 5 units in the value axis, then a single
        callback event will be invoked with a MObject for each of the 5
        keyframes.  The MObjects can then be used in the MFnKeyframeDelta
        function set. Refer to MFnKeyframeDelta function set documentation
        for more info.

         * animNode (MObject) - the param curve node you want to watch.
         * function - callable which will be passed a MObject indicating the
           edited animation node, a MObjectArray containing an array of keyframes
           that were edited and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addPostBakeResultsCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addPostBakeResultsCallback(function, clientData=None) -> id

        This method registers a callback that is called from bakeResults
        command after the simulation. If the plugArray is replaced, then
        the anim curves created from baking will be connected to the new
        plugs.

         * function - callable which will be passed a MPlugArray containing the baked
           plugs to which the resulting anim curves will be connected (they can be
           replaced but must have the same number of plugs),a MDGModifier used if
           bakeResults command is undone or redone and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addPreBakeResultsCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addPreBakeResultsCallback(function, clientData=None) -> id

        This method registers a callback that is called from bakeResults
        command before the simulation. One example usage is handle the runup to
        the first frame in a dynamic system. If plugArray is set to zero
        length in the callback, the baking will be aborted.

         * function - callable which will be passed a MPlugArray containing the plugs
           to be baked (they can be replaced but must have the same number of plugs)
           ,a MDGModifier used if bakeResults command is undone or redone and the
           clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def flushAnimKeyframeEditedCallbacks(self, *args: Any, **kwargs: Any) -> Any:
        """flushAnimKeyframeEditedCallbacks() -> None

        Animation keyframe edited callbacks are queued to only be issued on an
        idle event. There may be times when it is desired to issue the callback
        at a specific time. This method provides this functionality. It will
        flush all animation keyframe edited callbacks and force them to issue
        their callbacks with the data contained within.
        """

class MAnimUtil:
    __doc__: str = ...
    def findAnimatablePlugs(self, *args: Any, **kwargs: Any) -> Any:
        """findAnimatablePlugs(MSelectionList) -> MPlugArray

        Find the list of attributes (MPlugs) on any member of an MSelectionList
        that is animatable.

        In addition to normal objects, components such as mesh vertices or
        faces can be easily described on an MSelectionList, making this a
        good way to determine if parts of a shape are animatable or not.
        """
    def findAnimatedPlugs(self, *args: Any, **kwargs: Any) -> Any:
        """findAnimatedPlugs(MObject, bool) -> MPlugArray
        findAnimatedPlugs(MDagPath, bool) -> MPlugArray
        findAnimatedPlugs(MSelectionList selectionList, bool checkParent) -> MPlugArray

        Find the list of attributes (MPlugs) on the input object that is animated.
        """
    def findAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """findAnimation(MPlug) -> MObjectArray

        Find the animCurve(s) that are animating a given attribute (MPlug).
        In most cases an attribute is animated by a single animCurve and so
        just that animCurve will be returned.  It is possible to setup a
        series of connections where an attribute is animated by more than
        one animCurve, although Maya does not currently offer a UI to do so.
        Compound attributes are not expanded to include any child attributes.
        """
    def findConstraint(self, *args: Any, **kwargs: Any) -> Any:
        """findConstraint(Mplug) -> (MObject, MObjectArray)

        Find any constraint that is directly driving the specified attribute.
        If a constraint is found, this method will also find the constraint
        targets. Return false if no constraint exists on the attribute.

        Compound attributes are not expanded to include any child attributes.
        """
    def findSetDrivenKeyAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """findSetDrivenKeyAnimation(MPlug) -> (MObjectArray, MPlugArray)

        Find any driven keyframe animCurves, the blendWeighted node and the
        driver attribute(s) that are animating a given attribute (MPlug).
        Or return false if no driven keyframe exists on the attribute.

        A driven keyframe is similar to a regular keyframe. However, while a
        standard keyframe always has an x-axis of time in the graph editor,
        for a drivenkeyframe the user may choose any attribute
        as the x-axis of the graph editor. This attribute is called the driver.

        In the case where there is only one driver, the animation curve
        will be connected directly to the driven attribute. When there are
        multiple drivers, the driven keyframe animCurves feed into a
        blendWeighted node which drives the attribute.

        Compound attributes are not expanded to include any child attributes.
        """
    def isAnimated(self, *args: Any, **kwargs: Any) -> Any:
        """isAnimated(MObject, bool) -> bool
        isAnimated(MDagPath, bool) -> bool
        isAnimated(MPlug, bool) -> bool
        isAnimated(MSelectionList selectionList, bool checkParent) -> bool

        Determine whether or not an MObject is animated.
        If the MObject is a hierarchical object (such as a dag node) then
        you may also specify whether or not the input object's parents are examined.
        """

class MFnAnimCurve(MFnDependencyNode):
    __doc__: str = ...
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def addKey(self, *args: Any, **kwargs: Any) -> Any:
        """addKey(at, value, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, change=None) -> unsigned int

        Adds a new key with the given value at the specified time.
        at and value can both be either MTime or double,depending on what is appropriate for the animCurve type.
        change is an optional MAnimCurveChange.
        """
    def addKeys(self, *args: Any, **kwargs: Any) -> Any:
        """addKeys(times, values, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, keepExistingKeys=False, change=None) -> self

        Add a set of new keys with the given corresponding values and tangent typesat the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU.
        """
    def addKeysWithTangents(self, *args: Any, **kwargs: Any) -> Any:
        """addKeysWithTangents(times, values, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, tangentInTypeArray=None, tangentOutTypeArray=None, tangentInXArray=None, tangentInYArray=None, tangentOutXArray=None, tangentOutYArray=None, tangentsLockedArray=None, weightsLockedArray=None, convertUnits=True, keepExistingKeys=False, change=None) -> self

        Add a set of new keys with the given corresponding values, tangent types and tangents at the specified times.  This method only works for animCurves of typekAnimCurveTA, kAnimCurveTL and kAnimCurveTU.
        """
    @property
    def animCurveType(*args: Any, **kwargs: Any) -> Any:
        """Anim curve type."""
    @animCurveType.setter
    def animCurveType(*args: Any, **kwargs: Any) -> Any:
        """Anim curve type."""
    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(node, attribute, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
        create(plug, animCurveType=kAnimCurveUnknown [, modifier] ) -> MObject
        create(animCurveType [, modifier] ) -> MObject

        Creates a new animCurve node.
        If node and attribute (MObject) are supplied, the animCurvewill be connected to the given attribute on the given node.
        If plug (MPlug) is supplied, the animCurvewill be connected to the given plug.
        modifier is an optional MDGModifier which can be used to later undo the operation.
        animCurveType specifies the type of animCurve to create. Valid values are:
        kAnimCurveTA		Time to Angular
        kAnimCurveTL		Time to Linear
        kAnimCurveTT		Time to Time
        kAnimCurveTU		Time to Unitless
        kAnimCurveUA		Unitless to Angular
        kAnimCurveUL		Unitless to Linear
        kAnimCurveUT		Unitless to Time
        kAnimCurveUU		Unitless to Unitless
        kAnimCurveUnknown	Unknown type
        """
    def evaluate(self, *args: Any, **kwargs: Any) -> Any:
        """evaluate(at) -> value

        Evalutes the curve.
        For curves of type kAnimCurveTA, kAnimCurveTL and kAnimCurveTU,the at parameter is an MTime, otherwise it is a double.
        For curves of type kAnimCurveTT and kAnimCurveUT,the value is an MTime, otherwise it is a double.
        """
    def find(self, *args: Any, **kwargs: Any) -> Any:
        """find(at) -> unsigned int

        Determines the index of the key which is set at the specifiedMTime (time-input curves) or double (unitless-input curves).
        Returns None if the key is not found.
        """
    def findClosest(self, *args: Any, **kwargs: Any) -> Any:
        """findClosest(at) -> unsigned int

        Determines the index of the key which is set at theMTime (time-input curves) or double (unitless-input curves)closest to the specified time.
        """
    def getTangentAngleWeight(self, *args: Any, **kwargs: Any) -> Any:
        """getTangentAngleWeight(index, isInTangent) -> (MAngle,double)

        Determines the angle and weight of the in- or out-tangent to the curvefor the key at the specified index
        """
    def getTangentXY(self, *args: Any, **kwargs: Any) -> Any:
        """getTangentXY(index, isInTangent) -> (x,y)

        Determines the x,y value representing the vector of the in- orout-tangent (depending on the value of the isInTangent parameter) tothe curve for the key at the specified index.  The values returnedwill be in Maya's internal units (seconds for time, centimeters forlinear, radians for angles).
        """
    def inTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """inTangentType(index) -> TangentType

        Determines the type of the tangent to the curve entering the current key.
        """
    def input(self, *args: Any, **kwargs: Any) -> Any:
        """input(index) -> MTime or double

        Determines the input (MTime for T* curves or double for U* curves) of the key at the specified index.
        """
    def insertKey(self, *args: Any, **kwargs: Any) -> Any:
        """addKey(time, breakdown=False, change=None) -> unsigned int

        Inserts a new key at the specified time adjusting neighboring
        tangents to maintain curve shape. This method is the API equivalent
        to maya.cmds.setKeyframe(insert=True).
        breakdown specifies the breakdown state of the newly inserted key.
        change is an optional MAnimCurveChange.
        Returns the index of the newly inserted key.
        """
    def isBreakdown(self, *args: Any, **kwargs: Any) -> Any:
        """isBreakdown(index) -> bool

        Determines whether or not a key is a breakdown.
        """
    @property
    def isStatic(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve is static."""
    @isStatic.setter
    def isStatic(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve is static."""
    @property
    def isTimeInput(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve has time as an input."""
    @isTimeInput.setter
    def isTimeInput(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve has time as an input."""
    @property
    def isUnitlessInput(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve has unitless input."""
    @isUnitlessInput.setter
    def isUnitlessInput(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve has unitless input."""
    @property
    def isWeighted(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve has weighted tangents."""
    @isWeighted.setter
    def isWeighted(*args: Any, **kwargs: Any) -> Any:
        """Whether the curve has weighted tangents."""
    kTangentAuto: int = ...
    kTangentAutoCustom: int = ...
    kTangentAutoEase: int = ...
    kTangentAutoMix: int = ...
    kTangentCustomEnd: int = ...
    kTangentCustomStart: int = ...
    kTangentShared1: int = ...
    kTangentShared2: int = ...
    kTangentShared3: int = ...
    kTangentShared4: int = ...
    kTangentShared5: int = ...
    kTangentShared6: int = ...
    kTangentShared7: int = ...
    kTangentShared8: int = ...
    kTangentStepNext: int = ...
    kTangentTypeCount: int = ...
    @property
    def numKeys(*args: Any, **kwargs: Any) -> Any:
        """Number of keys."""
    @numKeys.setter
    def numKeys(*args: Any, **kwargs: Any) -> Any:
        """Number of keys."""
    def outTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """outTangentType(index) -> TangentType

        Determines the type of the tangent to the curve leaving the current key.
        """
    @property
    def postInfinityType(*args: Any, **kwargs: Any) -> Any:
        """The curve's post-infinity type."""
    @postInfinityType.setter
    def postInfinityType(*args: Any, **kwargs: Any) -> Any:
        """The curve's post-infinity type."""
    @property
    def preInfinityType(*args: Any, **kwargs: Any) -> Any:
        """The curve's pre-infinity type."""
    @preInfinityType.setter
    def preInfinityType(*args: Any, **kwargs: Any) -> Any:
        """The curve's pre-infinity type."""
    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove(index, change=None) -> self

        Removes the key at the specified index.
        change is an optional MAnimCurveChange.
        """
    def setAngle(self, *args: Any, **kwargs: Any) -> Any:
        """setAngle(index, setAngle, isInTangent, change=None) -> self

        Sets the in- or out-angle of the tangent for the key at the given index.
        isInTangent is True to modify the inTangent or False to modify the outTangent.
        """
    def setInTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """setInTangentType(index, tangentType, change=None) -> self

        Sets the type of the tangent to the curve entering the key at thespecified index.
        Valid values for tangentType are:
        kTangentGlobal		Global
        kTangentFixed		Fixed
        kTangentLinear		Linear
        kTangentFlat		Flag
        kTangentSmooth		Smooth
        kTangentStep		Step
        kTangentSlow		OBSOLETE kTangentSlow should not be used. Using this tangent type may produce unwanted and unexpected results.
        kTangentFast		OBSOLETE kTangentFast should not be used. Using this tangent type may produce unwanted and unexpected results.
        kTangentClamped	Clamped
        kTangentPlateau	Plateau
        kTangentStepNext	StepNext
        kTangentAuto		AutokTangentAutoMix		AutoMixkTangentAutoEase		AutoEasekTangentAutoCustom		AutoCustom
        """
    def setInput(self, *args: Any, **kwargs: Any) -> Any:
        """setInput(index, at, change=None) -> self

        Sets the input (MTime for T* curves or double for U* curves) of the key at the specified index.  This will fail ifsetting the input would require re-ordering of the keys.
        """
    def setIsBreakdown(self, *args: Any, **kwargs: Any) -> Any:
        """setIsBreakdown(index, isBreakdown, change=None) -> self

        Sets the breakdown state of a key at a given index.
        """
    def setIsWeighted(self, *args: Any, **kwargs: Any) -> Any:
        """setIsWeighted(isWeighted, change=None) -> self

        Sets whether or not the curve has weighted tangents.
        """
    def setOutTangentType(self, *args: Any, **kwargs: Any) -> Any:
        """setOutTangentType(index, tangentType, change=None) -> self

        Sets the type of the tangent to the curve leaving the key at thespecified index.
        """
    def setPostInfinityType(self, *args: Any, **kwargs: Any) -> Any:
        """setPostInfinityType(infinityType, change=None) -> self

        Sets the behaviour of the curve for the range occurring after the last key.
        """
    def setPreInfinityType(self, *args: Any, **kwargs: Any) -> Any:
        """setPreInfinityType(infinityType, change=None) -> self

        Sets the behaviour of the curve for the range occurring before the first key.
        Valid values for infinityType are:
        kConstant			Constant
        kLinear			Linear
        kCycle				Cycle
        kCycleRelative		Cycle relative
        kOscillate			Oscillate
        """
    def setTangent(self, *args: Any, **kwargs: Any) -> Any:
        """setTangent(index, xOrAngle, yOrWeight, isInTangent, change=None, convertUnits=True) -> self

        Sets the tangent for the key at the specified index.
        The tangent can be specified as an x/y pair, oras an MAngle and a weight.
        isInTangent is True to modify the inTangent or False to modify the outTangent.
        """
    def setTangentTypes(self, *args: Any, **kwargs: Any) -> Any:
        """setTangentTypes(indexArray, tangentInType=kTangentGlobal, tangentOutType=kTangentGlobal, change=None) -> self

        Sets the tangent types for multiple keys.
        """
    def setTangentsLocked(self, *args: Any, **kwargs: Any) -> Any:
        """setTangentsLocked(index, locked, change=None) -> self

        Lock or unlock the tangents at the given key.
        """
    def setValue(self, *args: Any, **kwargs: Any) -> Any:
        """setValue(index, value, change=None) -> self

        Sets the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U.
        """
    def setWeight(self, *args: Any, **kwargs: Any) -> Any:
        """setWeight(index, weight, isInTangent, change=None) -> self

        Sets the in- or out-weight of the tangent for the key at the given index.
        isInTangent is True to modify the inTangent or False to modify the outTangent.
        """
    def setWeightsLocked(self, *args: Any, **kwargs: Any) -> Any:
        """setWeightsLocked(index, locked, change=None) -> self

        Lock or unlock the weights at the given key.
        """
    def tangentsLocked(self, *args: Any, **kwargs: Any) -> Any:
        """tangentsLocked(index) -> bool

        Determines whether the tangents are locked at the given key.
        """
    def timedAnimCurveTypeForPlug(self, *args: Any, **kwargs: Any) -> Any:
        """timedAnimCurveTypeForPlug(plug) -> AnimCurveType

        Returns the timed animCurve type appropriate for the specified plug.
        """
    def unitlessAnimCurveTypeForPlug(self, *args: Any, **kwargs: Any) -> Any:
        """unitlessAnimCurveTypeForPlug(plug) -> AnimCurveType

        Returns the unitless animCurve type appropriate for the specified plug.
        """
    def value(self, *args: Any, **kwargs: Any) -> Any:
        """value(index) -> double

        Determines the value of the key at the specified index.  This methodshould only be used on Anim Curves of type kAnimCurve*A, kAnimCurve*Lor kAnimCurve*U.
        """
    def weightsLocked(self, *args: Any, **kwargs: Any) -> Any:
        """weightsLocked(index) -> bool

        Determines whether the weights are locked at the given key.
        """

class MFnGeometryFilter(MFnDependencyNode):
    __doc__: str = ...
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    @property
    def deformerSet(*args: Any, **kwargs: Any) -> Any:
        """Object set containing the objects that are deformed. Adding new
        components to the deformer set will cause them to be deformed.
        Removing components from the deformer set will prevent them from
        being influenced by the deformer.

        Note that the wrap deformer and the skinCluster deformers are
        special cases: they allow only a single object to be deformed per
        wrap/skinCluster, so adding additional geometries to them will have
        no effect.
        """
    @deformerSet.setter
    def deformerSet(*args: Any, **kwargs: Any) -> Any:
        """Object set containing the objects that are deformed. Adding new
        components to the deformer set will cause them to be deformed.
        Removing components from the deformer set will prevent them from
        being influenced by the deformer.

        Note that the wrap deformer and the skinCluster deformers are
        special cases: they allow only a single object to be deformed per
        wrap/skinCluster, so adding additional geometries to them will have
        no effect.
        """
    @property
    def envelope(*args: Any, **kwargs: Any) -> Any:
        """A global scale factor that is applied to all the values."""
    @envelope.setter
    def envelope(*args: Any, **kwargs: Any) -> Any:
        """A global scale factor that is applied to all the values."""
    def getComponentAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getComponentAtIndex(index) -> MObject

        Returns the component which contains the members of the deformer
        at the given index.
        """
    def getInputGeometry(self, *args: Any, **kwargs: Any) -> Any:
        """getInputGeometry() -> MObjectArray

        Returns the DAG nodes which provide input geometry to the deformer.
        These are found by traversing the graph to find upstream shape nodes.
        It is possible for there to be nodes in between the shape and the
        deformer so that the returned shape may have a different topology or
        tweaks then the input data to the deformer. If the actual input
        geometry data for the deformer is required, this information can be
        accessed by using MPlug::getValue() to query the inputGeometry
        attribute on the deformer.
        """
    def getOutputGeometry(self, *args: Any, **kwargs: Any) -> Any:
        """getOutputGeometry() -> MObjectArray

        Returns the DAG nodes which receive output geometry from the deformer.
        """
    def getPathAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getPathAtIndex(plugIndex) -> MDagPath

        Returns the DAG path of the specified output geometry.

        * plugIndex (unsigned int) - Plug index of the desired geometry.
        """
    def groupIdAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """groupIdAtIndex(plugIndex) -> long

        Returns the groupId associated with the specified geometry.

        * plugIndex (unsigned int) - Plug index of the desired geometry.
        """
    def indexForGroupId(self, *args: Any, **kwargs: Any) -> Any:
        """indexForGroupId(groupId) -> plugIndex

        Returns the plug index of the geometry associated with the specified groupId.

        * groupId (unsigned int) - groupId of the desired geometry.
        """
    def indexForOutputConnection(self, *args: Any, **kwargs: Any) -> Any:
        """indexForOutputConnection(connIndex) -> plugIndex

        Returns the plug index corresponding to a connection index. The
        connection index is the contiguous (physical) index of the output
        connection, ranging from 0 to numOutputConnections()-1. The plug
        index is the sparse (logical) index of the connection.

        * connIndex (unsigned int) - Connection index of the desired geometry.
        """
    def indexForOutputShape(self, *args: Any, **kwargs: Any) -> Any:
        """indexForOutputShape(shape) -> plugIndex

        Returns the plug index for the specified output shape.

        * shape (MObject) - Shape for which the plug index is requested.
        """
    def inputShapeAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """inputShapeAtIndex(plugIndex) -> MObject

        Returns the input shape corresponding to the plug index.

        * plugIndex (unsigned int) - Plug index of the desired shape.
        """
    def numOutputConnections(self, *args: Any, **kwargs: Any) -> Any:
        """numOutputConnections() -> long

        Returns the number of output geometries connected to this node. This
        is typically equal to the number of input geometries unless an input
        or output geometry has been deleted, or a connection to an input or
        output geometry has been broken.

        This method is useful in conjunction with indexForOutputConnection()
        to iterate through the affected objects.
        """
    def outputShapeAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """outputShapeAtIndex(index) -> MObject

        Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject.
        """

class MFnSkinCluster(MFnGeometryFilter):
    __doc__: str = ...
    def __init__(self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __new__(self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def getBlendWeights(self, *args: Any, **kwargs: Any) -> Any:
        """getBlendWeights(shape, components) -> MDoubleArray

        Returns blend weights for the specified components of the deformed
        shape. Blend weights are used to determine the blending between
        classical linear skinning and dual quaternion bases skinning on a
        per vertex basis. The returned array contains one weight per component
        in the order given by 'components'.

        * shape     (MDagPath) - the object being deformed by the skinCluster
        * components (MObject) - components for which weights should be returned
        """
    def getPointsAffectedByInfluence(self, *args: Any, **kwargs: Any) -> Any:
        """getPointsAffectedByInfluence(influence) -> (MSelectionList, MDoubleArray)

        During deformation, the skinCluster algorithm is applied for a given
        influence object on all points in the deformer's set whose weights
        are non-zero. This returns the non-zero weights for a particular
        influence object.

        The return value is a tuple consisting of a selection list, which
        contains the dag path and components that are affected by the
        specified influence object, and the corresponding weights for the
        components. If no components are weighted for a specified influence
        the selection list will be empty.

        * influence (MDagPath) - the influence object of interest
        """
    def getWeights(self, *args: Any, **kwargs: Any) -> Any:
        """getWeights(shape, components) -> (MDoubleArray, int)
        getWeights(shape, components, influence) -> MDoubleArray
        getWeights(shape, components, influences) -> MDoubleArray

        Returns the skinCluster weights of the given influence objects on
        the specified components of the deformed shape.


        If no influence index is provided then a tuple containing the weights
        and the number of influence objects will be returned.

        If a single influence index is provided the an array of weights will
        be returned, one per component in the same order as in 'components'.

        If an array of influence indices is provided an array of weights will
        be returned containing as many weights for each component as there
        are influences in the 'influenceIndices' array. The weights will be
        in component order: i.e. all of the weight values for the first
        component, followed by all the weight values for the second component,
        and so on.

        * shape       (MDagPath) - the object being deformed by the skinCluster
        * components   (MObject) - components to return weights for
        * influence        (int) - index of the single influence to return weights for
        * influences (MIntArray) - indices of multiple influences to return weights for
        """
    def indexForInfluenceObject(self, *args: Any, **kwargs: Any) -> Any:
        """indexForInfluenceObject(influenceObj) -> long

        Returns the logical index of the matrix array attribute where the
        specified influence object is attached.

        * influenceObj (MObject) - influence object for which the index is requested.
        """
    def influenceObjects(self, *args: Any, **kwargs: Any) -> Any:
        """influenceObjects() -> MDagPathArray

        Returns an array of paths to the influence objects for the skinCluster.
        """
    def setBlendWeights(self, *args: Any, **kwargs: Any) -> Any:
        """setBlendWeights(shape, components, weights) -> self

        Sets blend weights for the specified components of the shape being
        deformed by the skinCluster. Blend weights are used to determine the
        blending between classical linear skinning and dual quaternion bases
        skinning on a per vertex basis.

        * shape       (MDagPath) - object being deformed by the skinCluster
        * components   (MObject) - components of 'shape' to set blend weights for
        * weights (MDoubleArray) - weights to set, one per component. If the
                                   length of this array does match the number
                                   of components provided then the lesser of
                                   the two will be used.
        """
    def setWeights(self, *args: Any, **kwargs: Any) -> Any:
        """setWeights(shape, components, influence, weight, normalize=True, returnOldWeights=False) -> None or MDoubleArray
        setWeights(shape, components, influences, weights, normalize=True, returnOldWeights=False) -> None or MDoubleArray

        Sets the skinCluster weights for one or more influence objects on
        the specified components of the given shape. If 'returnOldWeights'
        is True then the old weights will be returned, otherwise None will
        be returned

        If only a single influence index and weight are specified then that
        weight is applied to all of the specified components. The returned
        array of old weights, if requested, will contain weights for ALL of
        the skinCluster's influence objects, not just the one specified by
        the 'influence' parameter.

        If arrays of influence indices and weights are provided then the
        behaviour depends upon the number of elements in the 'weights' array.
        If it's equal to the number of influences specified then each weight
        will be used for all of components for the corresponding influence
        object. If it's equal to the number of influences times the number of
        components provided, then a separate weight will be used for each
        component, with all of the weights for the first component coming
        first in the 'weights' array, followed by all of the weights for the
        second component, and so on. Within each component the weights will
        will correspond with the ordering of influence indices in the
        'influences' array. The returned old weights, if requested, will
        consist of a separate weight for

        The returned old weights will be ordered by influence within
        component, i.e. all of the influence weights for the first component
        will come first in the array, followed by all the weights for the
        second component, and so on.

        * shape       (MDagPath) - object being deformed by the skinCluster
        * components   (MObject) - the components to set weights on
        * influence        (int) - physical index of a single influence object
        * weight         (float) - single weight to be applied to all components.
        * influences (MIntArray) - physical indices of several influence objects.
        * weights (MDoubleArray) - weights to be used with several influence objects.
        * normalize       (bool) - if True, normalize weights on other influence objects
        * returnOldWeights(bool) - if True, return the old weights, otherwise return None
        """
