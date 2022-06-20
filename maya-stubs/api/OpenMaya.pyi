from typing import *
from typing_extensions import Self
from _typeshed import Incomplete

def getStringResource(*args: Any, **kwargs: Any) -> Any: ...

key: str
ourdict: dict
py2dict: dict

def registerStringResource(*args: Any, **kwargs: Any) -> Any: ...
def registerStringResources(*args: Any, **kwargs: Any) -> Any: ...

val: str

class MAngle:
    def asAngMinutes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to minutes of arc."""
    def asAngSeconds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to seconds of arc."""
    def asDegrees(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to degrees."""
    def asRadians(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to radians."""
    def asUnits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to the specified units."""
    def internalToUI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Converts a value from Maya's internal units to the units used in the UI."""
    def internalUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular unit used internally by Maya."""
    kAngMinutes: int = ...
    kAngSeconds: int = ...
    kDegrees: int = ...
    kInvalid: int = ...
    kLast: int = ...
    kRadians: int = ...

    def setUIUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the angular unit used in Maya's UI."""
    def uiToInternal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Converts a value from the units used in the UI to Maya's internal units."""
    def uiUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the units used to display angles in Maya's UI."""
    @property
    def unit(*args: Any, **kwargs: Any) -> Any:
        """Angular units used by the angle."""
    @unit.setter
    def unit(*args: Any, **kwargs: Any) -> Any:
        """Angular units used by the angle."""
    @property
    def value(*args: Any, **kwargs: Any) -> Any:
        """Value of the angle."""
    @value.setter
    def value(*args: Any, **kwargs: Any) -> Any:
        """Value of the angle."""

class MArgParser:
    def commandArgumentBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentBool(argIndex) -> bool

        Returns the specified command argument as a bool.
        """
    def commandArgumentDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Alias for commandArgumentFloat()."""
    def commandArgumentFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentFloat(argIndex) -> float

        Returns the specified command argument as a float.
        """
    def commandArgumentInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentInt(argIndex) -> int

        Returns the specified command argument as an int.
        """
    def commandArgumentMAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMAngle(argIndex) -> MAngle

        Returns the specified command argument as an MAngle.
        """
    def commandArgumentMDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMDistance(argIndex) -> MDistance

        Returns the specified command argument as an MDistance.
        """
    def commandArgumentMTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMTime(argIndex) -> MTime

        Returns the specified command argument as an MTime.
        """
    def commandArgumentString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentString(argIndex) -> unicode string

        Returns the specified command argument as a string.
        """
    def flagArgumentBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentBool(flagName, argIndex) -> bool

        Returns the specified argument of the specified single-use flag as
        a bool.
        """
    def flagArgumentDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentDouble(flagName, argIndex) -> float

        Alias for flagArgumentFloat().
        """
    def flagArgumentFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentFloat(flagName, argIndex) -> float

        Returns the specified argument of the specified single-use flag as
        a float.
        """
    def flagArgumentInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentInt(flagName, argIndex) -> int

        Returns the specified argument of the specified single-use flag as
        an int.
        """
    def flagArgumentMAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMAngle(flagName, argIndex) -> MAngle

        Returns the specified argument of the specified single-use flag as
        an MAngle.
        """
    def flagArgumentMDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMDistance(flagName, argIndex) -> MDistance

        Returns the specified argument of the specified single-use flag as
        an MDistance.
        """
    def flagArgumentMTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMTime(flagName, argIndex) -> MTime

        Returns the specified argument of the specified single-use flag as
        an MTime.
        """
    def flagArgumentString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentString(flagName, argIndex) -> string

        Returns the specified argument of the specified single-use flag as
        a string.
        """
    def getFlagArgumentList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFlagArgumentList(flagName, occurrence) -> MArgList

        Returns the arguments for the specified occurrence of the given
        multi-use flag as an MArgList. Raises RuntimeError if the flag has
        not been enabled for multi-use. Raises IndexError if occurrence is
        out of range.
        """
    def getFlagArgumentPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFlagArgumentPosition(flagName, occurrence) -> int

        Returns the position in the argument list of the specified occurrence
        of the given flag. Raises IndexError if occurrence is out of range.
        """
    def getObjectStrings(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getObjectStrings() -> tuple of unicode strings

        If the command's MSyntax has set the object format to kStringObjects
        then this method will return the objects passed to the command as a
        tuple of strings. If any other object format is set then an empty
        tuple will be returned.
        """
    @property
    def isEdit(*args: Any, **kwargs: Any) -> Any:
        """True if the edit flag is present."""
    @isEdit.setter
    def isEdit(*args: Any, **kwargs: Any) -> Any:
        """True if the edit flag is present."""
    def isFlagSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isFlagSet(flagName) -> bool

        Returns True if the given flag appears on the command line.
        """
    @property
    def isQuery(*args: Any, **kwargs: Any) -> Any:
        """True if the query flag is present."""
    @isQuery.setter
    def isQuery(*args: Any, **kwargs: Any) -> Any:
        """True if the query flag is present."""
    def numberOfFlagUses(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numberOfFlagUses(flagName) -> int

        Returns the number of times that the flag appears on the command
        line.
        """
    @property
    def numberOfFlagsUsed(*args: Any, **kwargs: Any) -> Any:
        """Number of different flags used on the command line. If the same flag appears multiple times it is only counted once."""
    @numberOfFlagsUsed.setter
    def numberOfFlagsUsed(*args: Any, **kwargs: Any) -> Any:
        """Number of different flags used on the command line. If the same flag appears multiple times it is only counted once."""

class MArgDatabase(MArgParser):
    def commandArgumentMSelectionList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMSelectionList(argIndex) -> MSelectionList

        Returns the specified command argument as an MSelectionList.
        """
    def flagArgumentMSelectionList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMSelectionList(flagName, argIndex) -> MSelectionList

        Returns the specified argument of the specified single-use flag as
        an MSelectionList.
        """
    def getObjectList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getObjectList() -> MSelectionList

        If the command's MSyntax has set the object format to kSelectionList
        then this method will return the objects passed to the command as an
        MSelectionList. If any other object format is set then an empty
        selection list will be returned.
        """

class MArgList:
    def addArg(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addArg(arg) -> self , 'arg' is a numeric value, MAngle, MDistance,
        MTime, MPoint or	MVector.

        Add an argument to the end of the arg list.
        """
    def asAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asAngle(index) -> MAngle

        Return an argument as an MAngle.
        """
    def asBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asBool(index) -> bool

        Return an argument as a boolean.
        """
    def asDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDistance(index) -> MDistance

        Return an argument as an MDistance.
        """
    def asDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDouble(index) -> float

        Alias for asFloat().
        """
    def asDoubleArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDoubleArray(index) -> MDoubleArray

        Return a sequence of arguments as an MDoubleArray.
        """
    def asFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloat(index) -> float

        Return an argument as a float.
        """
    def asInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asInt(index) -> int

        Return an argument as an integer.
        """
    def asIntArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asIntArray(index) -> MIntArray

        Return a sequence of arguments as an MIntArray.
        """
    def asMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asMatrix(index) -> MMatrix

        Return a sequence of arguments as an MMatrix.
        """
    def asPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asPoint(index) -> MPoint

        Return a sequence of arguments as an MPoint.
        """
    def asString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asString(index) -> string

        Return an argument as a string.
        """
    def asStringArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asStringArray(index) -> list of strings

        Return a sequence of arguments as a list of strings.
        """
    def asTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asTime(index) -> MTime

        Return an argument as an MTime.
        """
    def asVector(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asVector(index) -> MVector

        Return a sequence of arguments as an MVector.
        """
    def flagIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """flagIndex(shortFlag, longFlag=None) -> int

        Return index of first occurrence of specified flag.
        """
    kInvalidArgIndex: int = ...

    def lastArgUsed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lastArgUsed() -> int

        Return index of last argument used by the most recent as*() method.
        """

class MArrayDataBuilder:
    def addElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElement(index) -> MDataHandle

        Adds a new element to the array at the given index.

        * index (int) - the index at which we wish to add the new element

        Returns The handle for the new element
        """
    def addElementArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElementArray(index) -> MArrayDataHandle

        Adds a new element to the array at the given index.  The added element is also an array.

        * index (int) - the index at which we wish to add the new element

        Returns The handle for the new array element
        """
    def addLast(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addLast() -> MDataHandle

        Adds a new element to the end of the array.  The index of the element will be the current highest index + 1.

        Returns The handle for the new element
        """
    def addLastArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addLastArray() -> MArrayDataHandle

        Adds a new element to the end of the array.  The added element is also an array.  The index of the element will the current highest index + 1.

        Returns The handle for the new array element
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source builder.

        * source (MArrayDataBuilder) - The source object to copy from
        """
    def growArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """growArray(amount) -> self

        Grows the array storage by the given amount.

        * amount (int) - the amount to grow the array by
        """
    def removeElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeElement(index) -> self

        Removes the specified element from the array

        * index (int) - the element of the array to remove
        """
    def setGrowSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGrowSize(size) -> self

        Sets the grow size of the array.  As elements are added to the array, the builder will allocate memory in chunks.  This method tells the builder how many elements to allocate each time it grows the array.

        * size (int) - the number of elements to allocate when growing the array
        """

class MArrayDataHandle:
    def builder(self: Self, *args: Any, **kwargs: Any) -> Any:
        """builder() -> MArrayDataBuilder

        Returns a builder for this handle's array so that it can be expanded.

        This method will raise an exception if the current array does not support array data builders. This can be changed in a node's initialize routine using the usesArrayDataBuilder attribute in MFnAttribute.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source array.

        * source (MArrayDataHandle) - The source object to copy from
        """
    def elementLogicalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """elementLogicalIndex() -> int

        Returns the index that we are currently at in the array.  It is possible for the index to be invalid, in which case the return status will report an error.  These may be sparse arrays so the element index returned will be a logical index.

        Raises an exception if there is no current element (e.g. if there are no elements).
        """
    def inputArrayValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inputArrayValue() -> MArrayDataHandle

        Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
    def inputValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inputValue() -> MDataHandle

        Gets a handle into this data block for the current array element.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Specifies whether or not there are more elements to iterate over.
        """
    def jumpToLogicalElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """jumpToLogicalElement(index) -> self

        Jump to a specific logical element in the array.
        Since the logical array is sparse its indices may not be consecutive and a binary search is used internally to find the element.
        Thus when iterating through the elements of the array it is much faster to do so using physical indices.

        * index (int) - the logical index to jump to
        """
    def jumpToPhysicalElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """jumpToPhysicalElement(position) -> self

        Jump to a specific physical element in the array.
        Since physical elements are contiguous no search is required.

        * position (int) - the array position to jump to
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> bool

        Advance to the next element in the array.
        Return True if there was a next element and False if there wasn't.
        """
    def outputArrayValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputArrayValue() -> MArrayDataHandle

        Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays. The array's elements are not evaluated and may no longer be valid. Therefore, this handle should only be used for writing over the data.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """
    def outputValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputValue() -> MDataHandle

        Gets a handle into this data block for the current array element. The element is not evaluated so its data may not be valid. Therefore, this handle should only be used for writing over the data.

        This method can also be used to retrieve handles to individual elements of  non-datablock array handles, such as those returned by MPlug.getValue() and MPlug.asMDataHandle().
        """
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set(builder) -> self

        Sets the data for this array from the data in the builder object

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().

        * builder (MArrayDataBuilder) - the builder object
        """
    def setAllClean(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAllClean() -> self

        Marks every element of the array attribute represented by the handle as clean.  This method should be used if a compute function is asked to compute a single element of a multi, but instead calculates all the elements.  Calling <i>setAllClean</i> in this situation will prevent further calls to the node's compute method for the other elements of the multi.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()
        """
    def setClean(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClean() -> self

        Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """

class MAttributeIndex:
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source index.

        * source (MAttributeIndex) - The source index to copy from
        """
    def getLower(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLower() -> int/float

        Returns the lower bound of the index.
        """
    def getUpper(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUpper() -> int/float

        Returns the upper bound of the index.
        """
    def getValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getValue() -> int/float

        Returns the current value of the index.
        Raises an exception if the index is a range.
        """
    def hasLowerBound(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasLowerBound() -> bool

        Returns True if a lower bound is specified.
        """
    def hasRange(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasRange() -> bool

        Returns True if a range was specified.
        """
    def hasUpperBound(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUpperBound() -> bool

        Returns True if an upper bound is specified.
        """
    def hasValidRange(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasValidRange() -> bool

        Returns True if upper bound is greater than lower bound.
        """
    def isBounded(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isBounded() -> bool

        Returns True if the index is bounded.
        """
    kFloat: int = ...
    kInteger: int = ...

    def setLower(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setLower(value) -> self

        Sets the lower bound of the index.
        """
    def setType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setType(type) -> self

        Sets the type of attribute index.
        See type() for a list of valid index types.

        * type (int) - the index type to set
        """
    def setUpper(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUpper(value) -> self

        Sets the upper bound of the index.
        """
    def setValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setValue(value) -> self

        Sets the value of the index.

        Remark: calling this method with an integer value will change its type to kInteger, and subsequently calling with a float value will change it to kFloat.
        """
    def type(self: Self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Returns the type of attribute index.

        Valid index types:
          kInteger	Integer index (e.g. mesh.cp[5])
          kFloat		Floating-poing index (e.g. curve.u[1.3])
        """

class MAttributePattern:
    def addRootAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add the given root attribute to this pattern."""
    def attrPattern(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the specified pattern indexed from the global list."""
    def attrPatternCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the global number of patterns created."""
    def findPattern(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return a pattern with the given name, None if not found."""
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the name of the attribute pattern."""
    def removeRootAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the nth or passed-in root attribute from this pattern."""
    def rootAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the nth root attribute in this pattern."""
    def rootAttrCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the number of root attributes in this pattern."""

class MAttributeSpec:
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source specification.

        * source (MAttributeSpec) - The source specification to copy from
        """
    @property
    def dimensions(*args: Any, **kwargs: Any) -> Any:
        """The dimensions of the attribute specification."""
    @dimensions.setter
    def dimensions(*args: Any, **kwargs: Any) -> Any:
        """The dimensions of the attribute specification."""
    @property
    def name(*args: Any, **kwargs: Any) -> Any:
        """The name of the attribute specification."""
    @name.setter
    def name(*args: Any, **kwargs: Any) -> Any:
        """The name of the attribute specification."""

class MAttributeSpecArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MBoundingBox:
    @property
    def center(*args: Any, **kwargs: Any) -> Any:
        """Center point"""
    @center.setter
    def center(*args: Any, **kwargs: Any) -> Any:
        """Center point"""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Empties the bounding box, setting its corners to (0, 0, 0)."""
    def contains(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a point lies within the bounding box."""
    @property
    def depth(*args: Any, **kwargs: Any) -> Any:
        """Size in Z"""
    @depth.setter
    def depth(*args: Any, **kwargs: Any) -> Any:
        """Size in Z"""
    def expand(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Expands the bounding box to include a point or other bounding box."""
    @property
    def height(*args: Any, **kwargs: Any) -> Any:
        """Size in Y"""
    @height.setter
    def height(*args: Any, **kwargs: Any) -> Any:
        """Size in Y"""
    def intersects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if any part of a given bounding box lies within this one."""
    @property
    def max(*args: Any, **kwargs: Any) -> Any:
        """Maximum corner point"""
    @max.setter
    def max(*args: Any, **kwargs: Any) -> Any:
        """Maximum corner point"""
    @property
    def min(*args: Any, **kwargs: Any) -> Any:
        """Minimum corner point"""
    @min.setter
    def min(*args: Any, **kwargs: Any) -> Any:
        """Minimum corner point"""
    def transformUsing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the bounding box's corners by a matrix."""
    @property
    def width(*args: Any, **kwargs: Any) -> Any:
        """Size in X"""
    @width.setter
    def width(*args: Any, **kwargs: Any) -> Any:
        """Size in X"""

class MCacheSchema:
    def add(self: Self, *args: Any, **kwargs: Any) -> Any:
        """add(attribute) -> self

        Force the attribute to be cached

        this method allows you to cache input attributes or other animatedattributes that are not fully understood by EM

        * attribute (MObject) - Attribute to cache
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset()

        Reset this schema to the minimal.
        """

class MCallbackIdArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MMessage:
    def currentCallbackId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentCallbackId() -> id

        Returns the callback ID of the currently executing callback. If called
        outside of a callback, an invalid MCallbackId and failed status will
        be returned.
        """
    kDefaultAction: int = ...
    kDoAction: int = ...
    kDoNotDoAction: int = ...

    def nodeCallbacks(self: Self, *args: Any, **kwargs: Any) -> Any:
        """nodeCallbacks(node) -> ids

        Returns a list of callback IDs registered to a given node.

         * node (MObject) - Node to query for callbacks.
         * ids (MCallbackIdArray) - Array to store the list of callback IDs.
        """
    def removeCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeCallback(id) -> None

        Removes the specified callback from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.

         * id (MCallbackId) - identifier of callback to be removed
        """
    def removeCallbacks(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeCallbacks(ids) -> None

        Removes all of the specified callbacks from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.

         * idList (MCallbackIdArray) - list of callbacks to be removed.
        """

class MCameraMessage(MMessage):
    def addBeginManipulationCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addBeginManipulationCallback(node, function, clientData=None) -> id

        Registers callbacks for camera manipulation beginning messages.

         * node (MObject) - The node to register the callback for.
         * function (MMessage::MNodeFunction) - the callback function
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addEndManipulationCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addEndManipulationCallback(node, function, clientData=None) -> id

        Registers callbacks for camera manipulation ending messages.

         * node (MObject) - The node to register the callback for.
         * function (MMessage::MNodeFunction) - the callback function
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MColor:
    @property
    def a(*args: Any, **kwargs: Any) -> Any:
        """alpha component"""
    @a.setter
    def a(*args: Any, **kwargs: Any) -> Any:
        """alpha component"""
    @property
    def b(*args: Any, **kwargs: Any) -> Any:
        """blue component"""
    @b.setter
    def b(*args: Any, **kwargs: Any) -> Any:
        """blue component"""
    @property
    def g(*args: Any, **kwargs: Any) -> Any:
        """green component"""
    @g.setter
    def g(*args: Any, **kwargs: Any) -> Any:
        """green component"""
    def getColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the color's components, in the specified color model."""
    kByte: int = ...
    kCMY: int = ...
    kCMYK: int = ...
    kFloat: int = ...
    kHSV: int = ...
    kOpaqueBlack: MColor = ...
    kRGB: int = ...
    kShort: int = ...

    @property
    def r(*args: Any, **kwargs: Any) -> Any:
        """red component"""
    @r.setter
    def r(*args: Any, **kwargs: Any) -> Any:
        """red component"""
    def setColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the color's components and color model."""

class MColorArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MCommandMessage(MMessage):
    def addCommandCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCommandCallback(function, clientData=None) -> id

        This method registers a callback for command messages that are
        issued every time a MEL command is executed. It is only called
        when actual commands are executed and not when scripts are
        executed.

        NOTE: Setting up a callback using this method will
        degrade the performance of Maya since the installed callback will be
        invoked repeatedly as MEL operations are processed.

         * function - callable which will be passed a string containing the
           MEL command being executed, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addCommandOutputCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCommandOutputCallback(function, clientData=None) -> id

        This method registers a callback for whenever commands generate
        output such as that which is printed into the command window.

         * function - callable which will be passed a string containing the
           MEL command being executed, a MessageType constant (see class docs
           for a list) indicating the message type and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addCommandOutputFilterCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCommandOutputFilterCallback(function, clientData=None) -> id

        This method registers a callback for whenever commands generate
        output such as that which is printed into the command window.

        Returning True in the callback will filter the output from the
        script editor and command line., returning False will keep the output.

         * function - callable which will be passed a string containing the
           MEL command being executed, a MessageType constant (see class docs
           for a list) indicating the message type and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addProcCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addProcCallback(function, clientData=None) -> id

        This method registers a callback that is executed every time a MEL
        procedure is run. The callback will be executed once when the procedure
        is about to be executed, and again when it has exited. If a non-existent
        procedure is called the callback will be called once for entry but there
        will be no call on exit.

        The callback cannot be registered multiple times. To register a new
        callback function for this, please de-register the original callback first

        NOTE: Setting up a callback using this method can potentially degrade the
        performance of Maya since the installed callback will be invoked
        repeatedly as MEL procedures are executed.

         * function - callable which will be passed a string containing the name
           of the procedure being invoked, an integer indicating the ID for the
           procedure's invocation, a bool set to True if the procedure is being entered,
           false otherwise, a ProcType constant (see below for a list) indicating the
           type of call this is (MEL proc or MEL command), and the clientData object
           ProcType constant can take the folowing values:
             kMELProc
             kMELCommand
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    kError: int = ...
    kResult: int = ...
    kStackTrace: int = ...
    kWarning: int = ...

class MConditionMessage(MMessage):
    def addConditionCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addConditionCallback(conditionName, function, clientData=None) -> id

        This method registers a callback for condition changed messages.
        The callback function will be passed the new state of the
        condition and any client data that the user wishes to pass in.

         * conditionName (string) - the condition to register the
        callback for
         * function - callable which will be passed a bool indicating
           the new state of the condition, and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def getConditionNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConditionNames() -> (string, string, ...)

        This method returns the list of available condition names.

         * return: tuple of available condition names.
        """
    def getConditionState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConditionState(name) -> bool

        This method returns the current state of a condition.

         * name (string) - the name of the condition.


         * return: The current state of the condition.
        """

class MContainerMessage(MMessage):
    def addBoundAttrCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addBoundAttrCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an attribute
        is bound or unbound on a container.

         * function - callable which will be passed a Node (the container)
           ,a string indicating the name of the bound attr, and
           the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addPublishAttrCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPublishAttrCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an attribute
        is published or unpublished from a container.

         * function - callable which will be passed a Node (the container)
           ,a string indicating the name of the published attr, and
           the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MDAGDrawOverrideInfo:
    @property
    def displayType(*args: Any, **kwargs: Any) -> Any:
        """Display type (kDisplayTypeNormal, kDisplayTypeReference or kDisplayTypeTemplate)"""
    @displayType.setter
    def displayType(*args: Any, **kwargs: Any) -> Any:
        """Display type (kDisplayTypeNormal, kDisplayTypeReference or kDisplayTypeTemplate)"""
    @property
    def enableShading(*args: Any, **kwargs: Any) -> Any:
        """Whether allow to draw shaded item"""
    @enableShading.setter
    def enableShading(*args: Any, **kwargs: Any) -> Any:
        """Whether allow to draw shaded item"""
    @property
    def enableTexturing(*args: Any, **kwargs: Any) -> Any:
        """Whether allow to draw textured item"""
    @enableTexturing.setter
    def enableTexturing(*args: Any, **kwargs: Any) -> Any:
        """Whether allow to draw textured item"""
    @property
    def enableVisible(*args: Any, **kwargs: Any) -> Any:
        """Whether the whole geometry is visible"""
    @enableVisible.setter
    def enableVisible(*args: Any, **kwargs: Any) -> Any:
        """Whether the whole geometry is visible"""
    kDisplayTypeNormal: int = ...
    kDisplayTypeReference: int = ...
    kDisplayTypeTemplate: int = ...
    kLODBoundingBox: int = ...
    kLODFull: int = ...

    @property
    def lod(*args: Any, **kwargs: Any) -> Any:
        """Level of detail (kLODFull or kLODBoundingBox)"""
    @lod.setter
    def lod(*args: Any, **kwargs: Any) -> Any:
        """Level of detail (kLODFull or kLODBoundingBox)"""
    @property
    def overrideEnabled(*args: Any, **kwargs: Any) -> Any:
        """Draw override enabled or not"""
    @overrideEnabled.setter
    def overrideEnabled(*args: Any, **kwargs: Any) -> Any:
        """Draw override enabled or not"""
    @property
    def playbackVisible(*args: Any, **kwargs: Any) -> Any:
        """Whether the object is visible during playback"""
    @playbackVisible.setter
    def playbackVisible(*args: Any, **kwargs: Any) -> Any:
        """Whether the object is visible during playback"""

class MDGContext:
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source context.

        * source (MDGContext) - The source object to copy from
        """
    def current(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the current context being used for evaluation."""
    def getTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the time at which this context is set to evaluate."""
    def isCurrent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the context is currently being used for evaluation. Returns False if some other context is being used for evaluation."""
    def isNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the context is set to evaluate normally. Returns False if the context is set to evaluate at a specific time."""
    kNormal: MDGContext = ...

    def makeCurrent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Makes this context the new current one being used for evaluation. Returns the previous evaluation context."""

class MDGMessage(MMessage):
    def addConnectionCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addConnectionCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a connection
        is made or broken in the dependency graph. This callback is triggered
        after the given connection has been made or broken, unlike the addPreConnectionCallback
        which is triggered before the operation.

         * function - callable which will be passed a MPlug indicating the source
           plug of the connection, a MPlug indicating the destination plug of the
           connection, a boolean set to True if a new connection will be made,
           False if it will be broken and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addDelayedTimeChangeCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addDelayedTimeChangeCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph, but after the time changed callback.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addDelayedTimeChangeRunupCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addDelayedTimeChangeRunupCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph, but after the other time changed callbacks
        which can be used to invoke a dynamics solve or runup if needed

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addForceUpdateCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addForceUpdateCallback(function, clientData=None) -> id

        This method registers a callback that is called after the time
        changes and after all nodes have been evaluated in the
        dependency graph.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeAddedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeAddedCallback(function, nodeType, clientData=None) -> id

        This method registers a callback that is called whenever a new node
        is added to the dependency graph.
        The nodeType argument allows you to specify the type of nodes that
        will trigger the callback. The default node type is "dependNode" which
        matches all nodes.

         * function - callable which will be passed a MObject indicating
           the new node and the clientData object
         * nodeType (MString) - type of node that will trigger the callback
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeChangeUuidCheckCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeChangeUuidCheckCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a node
        may have its UUID changed. Possible causes include the 'rename' command,
        and the UUID for a node being read from a file during file I/O.

        Note that nodes are assigned a UUID when they are created; this does
        not invoke this callback. During file I/O the stored UUID is applied as
        a separate step after creation (which does invoke this callback).

        Depending on the situation Maya may or may not use the new UUID by default.
        For example, when importing a file, Maya reads the UUID from the file
        but does not use it. The boolean argument to the callback function lets
        the callback know whether Maya is intending to use the UUID or not.

        The callback returns a MMessage.Action constant:
                * kDefaultAction - The callback does not want to change whether the
                  UUID is used or not.
                * kDoNotDoAction - Do not use the new UUID.
                * kDoAction - Use the new UUID.

        In any case, the callback may leave the new uuid as is, or may provide
        a new uuid of its own choosing to be used instead.

         * function - callable which will be passed a boolean indicating whether
           the UUID will be applied, a MObject indicating the node whose UUID may
           be changed, the MUuid that may be applied to the node (typically the one
           read from the file, during file I/O) - the callback may provide its own
           uuid to be applied by changing this parameter - and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeRemovedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeRemovedCallback(function, nodeType, clientData=None) -> id

        This method registers a callback that is called whenever a new node
        is removed from the dependency graph.
        The nodeType argument allows you to specify the type of nodes that
        will trigger the callback. The default node type is "dependNode" which
        matches all nodes.

         * function - callable which will be passed a MObject indicating
           the node being removed and the clientData object
         * nodeType (MString) - type of node that will trigger the callback
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addPreConnectionCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPreConnectionCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any connection
        is made or broken in the dependency graph. This callback is triggered before
        the given connection has been made or broken, unlike the addConnectionCallback
        which is triggered after the operation.

         * function - callable which will be passed a MPlug indicating the source
           plug of the connection, a MPlug indicating the destination plug of the
           connection, a boolean set to True if a new connection will be made,
           False if it will be broken and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addTimeChangeCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addTimeChangeCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MDGModifier:
    def addAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAttribute(MObject node, MObject attribute) -> self

        Adds an operation to the modifier to add a new dynamic attribute to the
        given dependency node. If the attribute is a compound its children will
        be added as well, so only the parent needs to be added using this method.
        """
    def addExtensionAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

        Adds an operation to the modifier to add a new extension attribute to
        the given node class. If the attribute is a compound its children will be
        added as well, so only the parent needs to be added using this method.
        """
    def commandToExecute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """commandToExecute(command) -> self

        Adds an operation to the modifier to execute a MEL command. The command
        should be fully undoable otherwise unexpected results may occur. If
        the command contains no undoable portions whatsoever, the call to
        doIt() may fail, but only after executing the command. It is best to
        use multiple commandToExecute() calls rather than batching multiple
        commands into a single call to commandToExecute(). They will still be
        undone together, as a single undo action by the user, but Maya will
        better be able to recover if one of the commands fails.
        """
    def connect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connect(MPlug source, MPlug dest) -> self
        connect(MObject sourceNode, MObject sourceAttr,
                MObject destNode,   MObject destAttr) -> self

        Adds an operation to the modifier that connects two plugs in the
        dependency graph. It is the user's responsibility to ensure that the
        source and destination attributes are of compatible types. For instance,
        if the source attribute is a nurbs surface then the destination must
        also be a nurbs surface.
        Plugs can either be specified with node and attribute MObjects or with
        MPlugs.
        """
    def createNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createNode(typeName) -> MObject
        createNode(MTypeId typeId) -> MObject

        Adds an operation to the modifier to create a node of the given type.
        The new node is created and returned but will not be added to the
        Dependency Graph until the modifier's doIt() method is called. Raises
        TypeError if the named node type does not exist or if it is a DAG node
        type.
        """
    def deleteNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteNode(MObject node) -> selfdeleteNode(MObject node, bool includeParents) -> self

        Adds an operation to the modifier which deletes the specified node from
        the Dependency Graph. If deleteNode() is called to delete nodes in a graph
        while other items are also in the queue, it might end up deleting the nodes
        before all the other tasks in the queue.

        In order to prevent unexpected outcomes, the modifier's doIt() should be called
        before the deleteNode operation is added so that the queue is emptied. Then,
        deleteNode() can be called and added to the queue. doIt() should be called
        immediately after to ensure that the queue is emptied before any other
        operations are added to it.

        The default behaviour when deleting a DAG node is to also include empty
        parents of the DAG node in the delete operation. If you do not want this
        behaviour set the includeParents argument to False.
        """
    def disconnect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """disconnect(MPlug source, MPlug dest) -> self
        disconnect(MObject sourceNode, MObject sourceAttr,
                   MObject destNode,   MObject destAttr) -> self

        Adds an operation to the modifier that breaks a connection between two
        plugs in the dependency graph.
        Plugs can either be specified with node and attribute MObjects or with
        MPlugs.
        """
    def doIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """doIt() -> self

        Executes the modifier's operations. If doIt() is called multiple times
        in a row, without any intervening calls to undoIt(), then only the
        operations which were added since the previous doIt() call will be
        executed. If undoIt() has been called then the next call to doIt() will
        do all operations.
        """
    def linkExtensionAttributeToPlugin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """linkExtensionAttributeToPlugin(MObject plugin, MObject attribute) -> self

        The plugin can call this method to indicate that the extension attribute
        defines part of the plugin, regardless of the node type to which it
        attaches itself. This requirement is used when the plugin is checked to
        see if it is in use or if is able to be unloaded or if it is required as
        part of a stored file. For compound attributes only the topmost parent
        attribute may be passed in and all of its children will be included,
        recursively. Thus it's not possible to link a child attribute to a
        plugin by itself. Note that the link is established immediately and is
        not affected by the modifier's doIt() or undoIt() methods.
        """
    def newPlugValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValue(MPlug plug, MObject value) -> self

        Adds an operation to the modifier to set the value of a plug, where
        value is an MObject data wrapper, such as created by the various
        MFn*Data classes.
        """
    def newPlugValueBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueBool(MPlug plug, bool value) -> self

        Adds an operation to the modifier to set a value onto a bool plug.
        """
    def newPlugValueChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueChar(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto a char (single
        byte signed integer) plug.
        """
    def newPlugValueDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueDouble(MPlug plug, float value) -> self

        Adds an operation to the modifier to set a value onto a double-precision
        float plug.
        """
    def newPlugValueFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueFloat(MPlug plug, float value) -> self

        Adds an operation to the modifier to set a value onto a single-precision
        float plug.
        """
    def newPlugValueInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueInt(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto an int plug.
        """
    def newPlugValueMAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueMAngle(MPlug plug, MAngle value) -> self

        Adds an operation to the modifier to set a value onto an angle plug.
        """
    def newPlugValueMDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueMDistance(MPlug plug, MDistance value) -> self

        Adds an operation to the modifier to set a value onto a distance plug.
        """
    def newPlugValueMTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueMTime(MPlug plug, MTime value) -> self

        Adds an operation to the modifier to set a value onto a time plug.
        """
    def newPlugValueShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueShort(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto a short
        integer plug.
        """
    def newPlugValueString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueString(MPlug plug, string value) -> self

        Adds an operation to the modifier to set a value onto a string plug.
        """
    def pythonCommandToExecute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pythonCommandToExecute(callable) -> selfpythonCommandToExecute(commandString) -> self

        Adds an operation to the modifier to execute a Python command, which
        can be passed as either a Python callable or a string containing the
        text of the Python code to be executed. The command should be fully
        undoable otherwise unexpected results may occur. If the command
        contains no undoable portions whatsoever, the call to doIt() may fail,
        but only after executing the command. It is best to use multiple calls
        rather than batching multiple commands into a single call to
        pythonCommandToExecute(). They will still be undone together, as a
        single undo action by the user, but Maya will better be able to
        recover if one of the commands fails.
        """
    def removeAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeAttribute(MObject node, MObject attribute) -> self

        Adds an operation to the modifier to remove a dynamic attribute from the
        given dependency node. If the attribute is a compound its children will
        be removed as well, so only the parent needs to be removed using this
        method. The attribute MObject passed in will be set to kNullObj. There
        should be no function sets attached to the attribute at the time of the
        call as their behaviour may become unpredictable.
        """
    def removeExtensionAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

        Adds an operation to the modifier to remove an extension attribute from
        the given node class. If the attribute is a compound its children will
        be removed as well, so only the parent needs to be removed using this
        method. The attribute MObject passed in will be set to kNullObj. There
        should be no function sets attached to the attribute at the time of the
        call as their behaviour may become unpredictable.
        """
    def removeExtensionAttributeIfUnset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeExtensionAttributeIfUnset(MNodeClass nodeClass,
                                        MObject attribute) -> self

        Adds an operation to the modifier to remove an extension attribute from
        the given node class, but only if there are no nodes in the graph with
        non-default values for this attribute. If the attribute is a compound
        its children will be removed as well, so only the parent needs to be
        removed using this method. The attribute MObject passed in will be set
        to kNullObj. There should be no function sets attached to the attribute
        at the time of the call as their behaviour may become unpredictable.
        """
    def removeMultiInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeMultiInstance(MPlug plug, bool breakConnections) -> self

        Adds an operation to the modifier to remove an element of a multi (array) plug.
        """
    def renameAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renameAttribute(MObject node, MObject attribute,
        string newShortName, string newShortName) -> self

        Adds an operation to the modifer that renames a dynamic attribute on the given dependency node.
        """
    def renameNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renameNode(MObject node, string newName) -> self

        Adds an operation to the modifer to rename a node.
        """
    def setNodeLockState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setNodeLockState(MObject node, bool newState) -> self

        Adds an operation to the modifier to set the lockState of a node.
        """
    def undoIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """undoIt() -> self

        Undoes all of the operations that have been given to this modifier. It
        is only valid to call this method after the doIt() method has been
        called.
        """
    def unlinkExtensionAttributeFromPlugin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unlinkExtensionAttributeFromPlugin(MObject plugin,
                                           MObject attribute) -> self

        The plugin can call this method to indicate that it no longer requires
        an extension attribute for its operation. This requirement is used when
        the plugin is checked to see if it is in use or if is able to be unloaded
        or if it is required as part of a stored file. For compound attributes
        only the topmost parent attribute may be passed in and all of its
        children will be unlinked, recursively. Thus it's not possible to unlink
        a child attribute from a plugin by itself. Note that the link is broken
        immediately and is not affected by the modifier's doIt() or undoIt()
        methods.
        """

class MDagMessage(MMessage):
    def addAllDagChangesCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAllDagChangesCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any
        DAG change is made to any DAG node.

         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback (see class
                  docs for a list), a MDagPath to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addAllDagChangesDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAllDagChangesDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a DAG
        change is made to the specified DAG path.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback (see class
                  docs for a list), a MDagPath to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addChildAddedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChildAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        added in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addChildAddedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChildAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        added to the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addChildRemovedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChildRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        removed in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addChildRemovedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChildRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        removed from the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addChildReorderedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChildReorderedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        reordered in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addChildReorderedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChildReorderedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child of
        the specified DAG node is reordered

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addDagCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addDagCallback(msgType, function, clientData=None) -> id

        This method registers a callback that is called for specified
        DAG changes on all nodes. The callback will also receive the
        DagMessage

         * msgType (DagMessage) - The type of DAG change to trigger the callback
         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback (see class
                  docs for a list), a MDagPath to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addDagDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addDagDagPathCallback(node, msgType, function, clientData=None) -> id

        This method registers a callback that is called for specified a DAG
        change is made to the specified DAG path. The callback receives the
        DagMessage as well.

         * node (MDagPath) - the DAG node to register the callback for
         * msgType (DagMessage) - The type of DAG change to trigger the callback
          (see class docs for a list)
         * function - callable which will be passed a DagMessage constant
           indicating the operation which triggered the callback, a MDagPath
           to the parent, a MDagPath to the child
           ,and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addInstanceAddedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any node in the DAG
        is instanced.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addInstanceAddedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever the specified node
        is instanced

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addInstanceRemovedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an instance of any DAG
        node is removed or deleted.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addInstanceRemovedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever an instance of the specified
        node is removed.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addMatrixModifiedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addMatrixModifiedCallback(node, function, clientData=None) -> id

        This method registers a callback that is called when the local matrix
        on the specified DAG node changes.

        If the node's transformation is already dirty (i.e. it has not been
        evaluated since it was last changed) then the callback will not be triggered.
        So if the node's transformation is modified multiple times between
        evaluations, only the first one will result in the callback being called.

         * affectedNode (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           whose transformation has changed, a MatrixModifiedFlags constant showing
           what has changed (see below for complete list) and the clientData object
         * clientData - User defined data passed to the callback function

        Available MatrixModifiedFlags constants:
        Individual flags:
          kScaleX		kScaleY			kScaleZ
          kShearXY		kShearXZ		kShearYZ
          kRotateX		kRotateY		kRotateZ
          kTranslateX	kTranslateY		kTranslateZ
          kScalePivotX	kScalePivotY	kScalePivotZ
          kRotatePivotX	kRotatePivotY	kRotatePivotZ
          kScaleTransX	kScaleTransY	kScaleTransZ
          kRotateTransX	kRotateTransY	kRotateTransZ
          kRotateOrientX	kRotateOrientY	kRotateOrientZ
          kRotateOrder
        Composite flags
          kAll
          kScale         	= kScaleX        | kScaleY        | kScaleZ
          kShear         	= kShearXY       | kShearXZ       | kShearYZ
          kRotation      	= kRotateX       | kRotateY       | kRotateZ
          kTranslation   	= kTranslateX    | kTranslateY    | kTranslateZ
          kScalePivot    	= kScalePivotX   | kScalePivotY   | kScalePivotZ
          kRotatePivot   	= kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
          kScalePivotTrans	= kScaleTransX   | kScaleTransY   | kScaleTransZ
          kRotatePivotTrans	= kRotateTransX  | kRotateTransY  | kRotateTransZ
          kRotateOrient  	= kRotateOrientX | kRotateOrientY | kRotateOrientZ

         * return: Identifier used for removing the callback.
        """
    def addParentAddedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addParentAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        added in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addParentAddedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addParentAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        added to the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addParentRemovedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addParentRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        removed in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addParentRemovedDagPathCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addParentRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        removed from the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addWorldMatrixModifiedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addWorldMatrixModifiedCallback(node, function, clientData=None) -> id

        This method registers a callback that is called when a parent matrix of the
        specified DAG node changes.

        Since a node's worldMatrix is affected by the transforms of its ancestors in
        the DAG, it's possible for there to be two different nodes involved: the
        "trigger" node, whose transform has changed, and the "affected" node, whose
        worldMatrix is affected by the change to the trigger.

        The callback is placed on the affected node, but it is the trigger node which
        is passed to the callback.

        If the trigger node's transformation is already dirty (i.e. it has not been
        evaluated since it was last changed) then the callback will not be triggered.
        So if the trigger node's transformation is modified multiple times between
        evaluations, only the first one will result in the callback being called.

         * affectedNode (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           whose transformation has changed, a MatrixModifiedFlags constant showing
           what has changed (see below for complete list) and the clientData object
         * clientData - User defined data passed to the callback function

        Available MatrixModifiedFlags constants:
        Individual flags:
          kScaleX		kScaleY			kScaleZ
          kShearXY		kShearXZ		kShearYZ
          kRotateX		kRotateY		kRotateZ
          kTranslateX	kTranslateY		kTranslateZ
          kScalePivotX	kScalePivotY	kScalePivotZ
          kRotatePivotX	kRotatePivotY	kRotatePivotZ
          kScaleTransX	kScaleTransY	kScaleTransZ
          kRotateTransX	kRotateTransY	kRotateTransZ
          kRotateOrientX	kRotateOrientY	kRotateOrientZ
          kRotateOrder
        Composite flags
          kAll
          kScale         	= kScaleX        | kScaleY        | kScaleZ
          kShear         	= kShearXY       | kShearXZ       | kShearYZ
          kRotation      	= kRotateX       | kRotateY       | kRotateZ
          kTranslation   	= kTranslateX    | kTranslateY    | kTranslateZ
          kScalePivot    	= kScalePivotX   | kScalePivotY   | kScalePivotZ
          kRotatePivot   	= kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
          kScalePivotTrans	= kScaleTransX   | kScaleTransY   | kScaleTransZ
          kRotatePivotTrans	= kRotateTransX  | kRotateTransY  | kRotateTransZ
          kRotateOrient  	= kRotateOrientX | kRotateOrientY | kRotateOrientZ

         * return: Identifier used for removing the callback.
        """
    kAll: int = ...
    kChildRemoved: int = ...
    kChildReordered: int = ...
    kInstanceAdded: int = ...
    kInstanceRemoved: int = ...
    kInvalidMsg: int = ...
    kLast: int = ...
    kRotateOrder: int = ...
    kRotateOrient: int = ...
    kRotateOrientX: int = ...
    kRotateOrientY: int = ...
    kRotateOrientZ: int = ...
    kRotatePivot: int = ...
    kRotatePivotTrans: int = ...
    kRotatePivotX: int = ...
    kRotatePivotY: int = ...
    kRotatePivotZ: int = ...
    kRotateTransX: int = ...
    kRotateTransY: int = ...
    kRotateTransZ: int = ...
    kRotateX: int = ...
    kRotateY: int = ...
    kRotateZ: int = ...
    kRotation: int = ...
    kScale: int = ...
    kScalePivot: int = ...
    kScalePivotTrans: int = ...
    kScalePivotX: int = ...
    kScalePivotY: int = ...
    kScalePivotZ: int = ...
    kScaleTransX: int = ...
    kScaleTransY: int = ...
    kScaleTransZ: int = ...
    kScaleZ: int = ...
    kShear: int = ...
    kShearXY: int = ...
    kShearXZ: int = ...
    kShearYZ: int = ...
    kTranslateX: int = ...
    kTranslateY: int = ...
    kTranslateZ: int = ...
    kTranslation: int = ...

class MDagModifier(MDGModifier):
    def createNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createNode(typeName, parent=MObject.kNullObj) -> new DAG node MObject
        createNode(typeId,   parent=MObject.kNullObj) -> new DAG node MObject

        Adds an operation to the modifier to create a DAG node of the specified
        type. If a parent DAG node is provided the new node will be parented
        under it. If no parent is provided and the new DAG node is a transform
        type then it will be parented under the world. In both of these cases
        the method returns the new DAG node.

        If no parent is provided and the new DAG node is not a transform type
        then a transform node will be created and the child parented under that. The new transform will be parented under the world and it is the
        transform node which will be returned by the method, not the child.

        None of the newly created nodes will be added to the DAG until the
        modifier's doIt() method is called.
        """
    def reparentNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reparentNode(MObject node, newParent=MObject.kNullObj) -> self

        Adds an operation to the modifier to reparent a DAG node under a
        specified parent.

        If no parent is provided then the DAG node will be reparented under the
        world, so long as it is a transform type. If it is not a transform type
        then the doIt() will raise a RuntimeError.
        """

class MDagPath:
    def apiType(self: Self) -> int:
        """Returns the type of the object at the end of the path."""
    def child(self: Self, chlidNum: int) -> MObject:
        """Returns the specified child of the object at the end of the path."""
    def childCount(self: Self) -> int:
        """Returns the number of objects parented directly beneath the object at the end of the path."""
    def exclusiveMatrix(self: Self) -> MMatrix:
        """Returns the matrix for all transforms in the path, excluding the end object."""
    def exclusiveMatrixInverse(self: Self) -> MMatrix:
        """Returns the inverse of exclusiveMatrix()."""
    def extendToShape(self: Self, shapeNum: int = ...) -> str:
        """Extends the path to the specified shape node parented directly beneath the transform at the current end of the path."""
    def fullPathName(self: Self) -> str:
        """Returns a string representation of the path from the DAG root to the path's last node."""
    def getAPathTo(self: Self, node: MObject) -> MDagPath:
        """Returns the first path found to the given node."""
    def getAllPathsTo(self: Self, node: MObject) -> MDagPathArray:
        """Returns all paths to the given node."""
    def getDisplayStatus(self: Self) -> int:
        """Returns the display status for this path."""
    def getDrawOverrideInfo(self: Self) -> MDAGDrawOverrideInfo:
        """Returns the draw override information for this path."""
    def getPath(self: Self, pathNum: int = ...) -> MDagPath:
        """Returns the specified sub-path of this path."""
    def hasFn(self: Self, type: int) -> bool:
        """Returns True if the object at the end of the path supports the given function set."""
    def inclusiveMatrix(self: Self) -> MMatrix:
        """Returns the matrix for all transforms in the path, including the end object, if it is a transform."""
    def inclusiveMatrixInverse(self: Self) -> MMatrix:
        """Returns the inverse of inclusiveMatrix()."""
    def instanceNumber(self: Self) -> int:
        """Returns the instance number of this path to the object at the end."""
    def isInstanced(self: Self) -> bool:
        """Returns True if the object at the end of the path can be reached by more than one path."""
    def isTemplated(self: Self) -> bool:
        """Returns true if the DAG Node at the end of the path is templated."""
    def isValid(self: Self) -> bool:
        """Returns True if this is a valid path."""
    def isVisible(self: Self) -> bool:
        """Returns true if the DAG Node at the end of the path is visible."""
    def length(self: Self) -> int:
        """Returns the number of nodes on the path, not including the DAG's root node."""
    def matchTransform(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Do some new stuff."""
    def node(self: Self) -> MObject:
        """Returns the DAG node at the end of the path."""
    def numberOfShapesDirectlyBelow(self: Self) -> int:
        """Returns the number of shape nodes parented directly beneath the transform at the end of the path."""
    def partialPathName(self: Self) -> str:
        """Returns the minimum string representation which will uniquely identify the path."""
    def pathCount(self: Self) -> int:
        """Returns the number of sub-paths which make up this path."""
    def pop(self: Self, nom: int = ...) -> Self:
        """Removes objects from the end of the path."""
    def push(self: Self, child: MObject) -> Self:
        """Extends the path to the specified child object, which must be parented directly beneath the object currently at the end of the path."""
    def set(self: Self, path: MDagPath) -> Self:
        """Replaces the current path held by this object with another."""
    def transform(self: Self) -> MObject:
        """Returns the last transform node on the path."""

class MDagPathArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MDataBlock:
    def context(self: Self, *args: Any, **kwargs: Any) -> Any:
        """context() -> MDGContext

        Returns a copy of the dependecy graph context for which this data block was created. The context is used to specify how a dependency node is going to be evaluated.
        """
    def inputArrayValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inputArrayValue(plug) -> MArrayDataHandle
        inputArrayValue(attribute) -> MArrayDataHandle

        Gets an array handle to this data block for the given plug/attribute's data.  This is only valid if the given plug has array data.  The data represented by the handle will be valid.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned.  If the plug has not been set to a particular value, then the default value will be returned.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute whose data you wish to access
        """
    def inputValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inputValue(plug) -> MDataHandle
        inputValue(attribute) -> MDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  The data represented by the handle is guaranteed to be valid for reading.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned. If the plug has not been set to a particular value, then the default value will be returned.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
        """
    def isClean(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isClean(plug) -> bool
        isClean(attribute) -> bool

        Queries the dependency graph to see whether the given plug/attribute is clean.

        * plug (MPlug) - the plug that is to be query
         OR
        * attribute (MObject) - the attribute that is to be query.
        """
    def outputArrayValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputArrayValue(plug) -> MArrayDataHandle
        outputArrayValue(attribute) -> MArrayDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  No dependency graph evaluations will be done, and therefore the data is not guaranteed to be valid (i.e. it may be dirty).  Typically, this method is used to get the handle during compute in order to write output data to it.

        Another usage of this method is to access an input array attribute without evaluating any of its array elements. One can then use MArrayDataHandle.jumpToElement() to get to the particular element of interest, and evaluate its value using MArrayDataHandle.inputValue().

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute whose data you wish to access
        """
    def outputValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """outputValue(plug) -> MDataHandle
        outputValue(attribute) -> MDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  The data is not guaranteed to be valid.  No dependency graph evaluations will be done. Therefore, this handle should be used only for writing.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
        """
    def setClean(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClean(plug) -> self
        setClean(attribute) -> self

        Tells the dependency graph that the given plug/attribute has been updated and is now clean.  This should be called after the data in the plug has been recalculated from the inputs of the node.

        * plug (MPlug) - the plug that is to be marked clean
         OR
        * attribute (MObject) - the attribute that is to be marked clean
        """
    def setContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setContext(ctx) -> self

        Set the dependency graph context for this data block. The context is used to specify how a dependency node is going to be evaluated, thus replacing the context for the given datablock. This does not modify the dirty state of the datablock so that they apply to the new context.

        This function should not be used for timed evaluation.

        * ctx (MDGContext) - the dependency graph context
        """

class MDataHandle:
    def acceptedTypeIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acceptedTypeIds() -> array of MTypeIds

        This method returns an array of MTypeIds.
        """
    def asAddr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asAddr() -> long

        Returns the data represented by this handle in the data block.
        """
    def asAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asAngle() -> MAngle

        Returns the data represented by this handle in the data block.
        """
    def asBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asBool() -> bool

        Returns the data represented by this handle in the data block.
        """
    def asChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asChar() -> int

        Returns the data represented by this handle in the data block.
        """
    def asDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDistance() -> MDistance

        Returns the data represented by this handle in the data block.
        """
    def asDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDouble() -> float

        Returns the data represented by this handle in the data block.
        """
    def asDouble2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDouble2() -> [float, float]

        Returns the data represented by this handle in the data block.
        """
    def asDouble3(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDouble3() -> [float, float, float]

        Returns the data represented by this handle in the data block.
        """
    def asDouble4(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asDouble4() -> [float, float, float, float]

        Returns the data represented by this handle in the data block.
        """
    def asFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloat() -> float

        Returns the data represented by this handle in the data block.
        """
    def asFloat2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloat2() -> [float, float]

        Returns the data represented by this handle in the data block.
        """
    def asFloat3(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloat3() -> [float, float, float]

        Returns the data represented by this handle in the data block.
        """
    def asFloatMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloatMatrix() -> MFloatMatrix

        Returns the data represented by this handle in the data block.
        """
    def asFloatVector(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asFloatVector() -> MFloatVector

        Returns the data represented by this handle in the data block.
        """
    def asGenericBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asGenericBool() -> bool

        Returns the generic data represented by this handle in the data block.
        """
    def asGenericChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asGenericChar() -> int

        Returns the generic data represented by this handle in the data block.
        """
    def asGenericDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asGenericDouble() -> float

        Returns the generic data represented by this handle in the data block.
        """
    def asGenericFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asGenericFloat() -> float

        Returns the generic data represented by this handle in the data block.
        """
    def asGenericInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asGenericInt() -> int

        Returns the generic data represented by this handle in the data block.
        """
    def asGenericShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asGenericShort() -> int

        Returns the generic data represented by this handle in the data block.
        """
    def asInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asInt() -> int

        Returns the data represented by this handle in the data block.
        """
    def asInt2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asInt2() -> [int, int]

        Returns the data represented by this handle in the data block.
        """
    def asInt3(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asInt3() -> [int, int, int]

        Returns the data represented by this handle in the data block.
        """
    def asMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asMatrix() -> MMatrix

        Returns the data represented by this handle in the data block.This method is only valid for attributes created using the MFnMatrixAttribute function set.
        """
    def asMesh(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asMesh() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set and iterators.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the mesh function set and iterators.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
    def asMeshTransformed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asMeshTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set (MFnMesh) or any of the mesh iterators.

        If the incoming mesh comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the mesh that is returned will be the mesh as it exists in world space.

        The mesh that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
    def asNurbsCurve(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsCurve() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The curve returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the nurbs curve function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
    def asNurbsCurveTransformed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsCurveTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set (MFnNurbsCurve) or the nurbs curve CV iterator (MItCurveCV).

        If the incoming curve comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the curve that is returned will be the curve as it exists in world space.

        The curve that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
    def asNurbsSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsSurface() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix.  This means that world space operations may be performed on this object using the nurbs surface function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
    def asNurbsSurfaceTransformed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsSurfaceTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set (MFnNurbsSurface) or the nurbs surface CV iterator (MItSurfaceCV).

        If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

        The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
    def asPluginData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asPluginData() -> MPxData

        Returns the data represented by this handle in the data block.  The object is returned as plugin data.  This should be used to access data types defined by plugins.
        """
    def asShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asShort() -> int

        Returns the data represented by this handle in the data block.
        """
    def asShort2(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asShort2() -> [int, int]

        Returns the data represented by this handle in the data block.
        """
    def asShort3(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asShort3() -> [int, int, int]

        Returns the data represented by this handle in the data block.
        """
    def asString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asString() -> MString

        Returns the data represented by this handle in the data block.
        """
    def asSubdSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asSubdSurface() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The subdivision surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space	transformation matrix. This means that world space operations may be performed on this object using the subdivision surface function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """
    def asSubdSurfaceTransformed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asSubdSurfaceTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set (MFnSubdSurface) or the subdivision surface iterators (MItSubdVertex, MItSubdFace, MItSubdEdge).

        If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

        The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """
    def asTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asTime() -> MTime

        Returns the data represented by this handle in the data block.
        """
    def asUChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asUChar() -> int

        Returns the data represented by this handle in the data block.
        """
    def asVector(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asVector() -> MVector

        Returns the data represented by this handle in the data block.
        """
    def child(self: Self, *args: Any, **kwargs: Any) -> Any:
        """child(MPlug) -> MDataHandle
        child(MObject) -> MDataHandle

        Get a handle to a child of this handle.  This is used if you have a handle to a compound attribute.
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(src) -> self

        Copies the attribute from the src attribute to the attribute referenced by this handle.  This is the only method which can completely copy a compound attribute from one handle to another.  The construct outputHandle.set (inputHandle.data()) will not work for compound or multi attributes.

        * src (MDataHandle) - the handle to the attribute to copy.
        """
    def copyWritable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyWritable(src) -> self

        Copies the attribute from the <i>src</i> attribute to the attribute referenced by this handle.  When the copy is made it ensures that the data in this handle is writable. That is, if the src handle has a writable copy of the data then it will be duplicated, otherwise this handle will claim the writer status for the data.

        * src (MDataHandle) - the handle to the attribute to copy.
        """
    def data(self: Self, *args: Any, **kwargs: Any) -> Any:
        """data() -> MObject

        Returns the data object from this handle.  The object returned should be used with the appropriate data function set.  This method is not valid for simple numeric types.
        """
    def datablock(self: Self, *args: Any, **kwargs: Any) -> Any:
        """datablock() -> MDataBlock

        Returns a reference to the datablock assigned to this data handle.
        """
    def geometryTransformMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geometryTransformMatrix() -> MMatrix

        This method returns a reference to the local-to-world transformation matrix that can accompany a geometry data object.  Only use this method on handles to geometry data (curves, surfaces, and meshes).

        If no local-to-world transformation information has been provided then this will be an identity matrix.
        """
    def isGeneric(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isGeneric() -> [bool, isNumeric, isNull]

        Returns True if this handle is for generic data.  There are 2 forms of generic data.  The first is for simple data and is used if the isNumeric parameter returns True.  In this case, the asGeneric*() and setGeneric*() methods of this class are used to query and set values.
        The second form of generic data is for more complex attribute types.  As a result the type of the object must be checked and an appropriate attribute function set initialized with the object.Returns isNumeric True if this handle is for simple generic numeric data.
        Returns isNull True if this handle is not set.
        """
    def isNumeric(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isNumeric() -> bool

        Returns True if this handle is for simple numeric data. That means that the numeric data is directly accessible through the non-generic as*() and set*() methods of this handle. For example, depending on handle initialization, the asBool() may be called but the asGenericBool() should not be called.
        """
    def numericType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numericType() -> int

        Returns the type of data represented by this handle.  This method is only valid for data handles of simple numeric types.
        """
    def set2Double(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set2Double(float, float) -> self

        Set the data that this handle represents in the data block.
        """
    def set2Float(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set2Float(float, float) -> self

        Set the data that this handle represents in the data block.
        """
    def set2Int(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set2Int(int, int) -> self

        Set the data that this handle represents in the data block.
        """
    def set2Short(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set2Short(int, int) -> self

        Set the data that this handle represents in the data block.
        """
    def set3Double(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set3Double(float, float, float) -> self

        Set the data that this handle represents in the data block.
        """
    def set3Float(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set3Float(float, float, float) -> self

        Set the data that this handle represents in the data block.
        """
    def set3Int(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set3Int(int, int, int) -> self

        Set the data that this handle represents in the data block.
        """
    def set3Short(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set3Short(int, int, int) -> self

        Set the data that this handle represents in the data block.
        """
    def set4Double(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set4Double(float, float, float, float) -> self

        Set the data that this handle represents in the data block.
        """
    def setBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setBool(bool) -> self

        Set the data that this handle represents in the data block.
        """
    def setChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setChar(int) -> self

        Set the data that this handle represents in the data block.
        """
    def setClean(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setClean() -> self

        Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.
        """
    def setDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDouble(float) -> self

        Set the data that this handle represents in the data block.
        """
    def setFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFloat(float) -> self

        Set the data that this handle represents in the data block.
        """
    def setGenericBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGenericBool(bool, force) -> self

        Set the data that this handle represents in the data block.
        """
    def setGenericChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGenericChar(int, force) -> self

        Set the data that this handle represents in the data block.
        """
    def setGenericDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGenericDouble(float, force) -> self

        Set the data that this handle represents in the data block.
        """
    def setGenericFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGenericFloat(float, force) -> self

        Set the data that this handle represents in the data block.
        """
    def setGenericInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGenericInt(int, force) -> self

        Set the data that this handle represents in the data block.
        """
    def setGenericShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setGenericShort(int, force) -> self

        Set the data that this handle represents in the data block.
        """
    def setInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setInt(int) -> self

        Set the data that this handle represents in the data block.
        """
    def setMAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMAngle(MAngle) -> self

        Set the data that this handle represents in the data block.
        """
    def setMDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMDistance(MDistance) -> self

        Set the data that this handle represents in the data block.
        """
    def setMFloatMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMFloatMatrix(MFloatMatrix) -> self

        Set the data that this handle represents in the data block.
        """
    def setMFloatVector(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMFloatVector(MFloatVector) -> self

        Set the data that this handle represents in the data block.
        """
    def setMMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMMatrix(MMatrix) -> self

        Set the data that this handle represents in the data block.
        """
    def setMObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMObject(MObject) -> self

        Set the data that this handle represents in the data block.  This method assumes that the MObject is a dependency graph data object.  These objects can be created using the appropriate MFn..Data function set.
        Note that this method cannot be used to copy compound or multi attributes from one handle to another via the construct outputHandle.set (inputHandle.data()).
        To copy these user defined attributes, the method MDataHandle.copy() must be used.
        """
    def setMPxData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMPxData(MPxData) -> self

        Set the data that this handle represents in the data block.  This method takes a pointer to a user defined data object.  The data block will become the new owner of the data object that you pass in.  Do not delete it.
        """
    def setMTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMTime(MTime) -> self

        Set the data that this handle represents in the data block.
        """
    def setMVector(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMVector(MVector) -> self

        Set the data that this handle represents in the data block.
        """
    def setShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setShort(int) -> self

        Set the data that this handle represents in the data block.
        """
    def setString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setString(string) -> self

        Set the data that this handle represents in the data block.
        """
    def type(self: Self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Returns the type of data represented by this handle.
        """
    def typeId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Returns the type of data represented by this handle as a type id.  A type id is a four character code that is used to identify the data type.
        If no data exists for this handle, the type id will be 0x0.
        """

class MDistance:
    def asCentimeters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to centimeters."""
    def asFeet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to feet."""
    def asInches(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to inches."""
    def asKilometers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to kilometers."""
    def asMeters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to meters."""
    def asMiles(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to miles."""
    def asMillimeters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to millimeters."""
    def asUnits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to the specified units."""
    def asYards(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to yards."""
    def internalToUI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert a value from Maya's internal units to the units used in the UI."""
    def internalUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance unit used internally by Maya."""
    kCentimeters: int = ...
    kFeet: int = ...
    kInches: int = ...
    kInvalid: int = ...
    kKilometers: int = ...
    kLast: int = ...
    kMeters: int = ...
    kMiles: int = ...
    kMillimeters: int = ...
    kYards: int = ...

    def setUIUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Change the units used to display distances in Maya's UI."""
    def uiToInternal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert a value from the units used in the UI to Maya's internal units."""
    def uiUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the units used to display distances in Maya's UI."""
    @property
    def unit(*args: Any, **kwargs: Any) -> Any:
        """Distance units currently in use."""
    @unit.setter
    def unit(*args: Any, **kwargs: Any) -> Any:
        """Distance units currently in use."""
    @property
    def value(*args: Any, **kwargs: Any) -> Any:
        """Value of the distance in the current units."""
    @value.setter
    def value(*args: Any, **kwargs: Any) -> Any:
        """Value of the distance in the current units."""

class MDoubleArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MEulerRotation:
    def alternateSolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation which is not simply a multiple."""
    def asMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent matrix."""
    def asQuaternion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent quaternion."""
    def asVector(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the X, Y and Z rotations as a vector."""
    def bound(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new MEulerRotation having this rotation, but with each rotation component bound within +/- PI."""
    def boundIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place bounding of each rotation component to lie wthin +/- PI."""
    def closestCut(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation which is full spin multiples of this one and comes closest to target."""
    def closestSolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the equivalent rotation which comes closest to a target."""
    def computeAlternateSolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation which is not simply a multiple."""
    def computeBound(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation with each rotation component bound within +/- PI."""
    def computeClosestCut(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation which is full spin multiples of the src and comes closest to target."""
    def computeClosestSolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the equivalent rotation which comes closest to a target."""
    def decompose(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Extracts a rotation from a matrix."""
    def incrementalRotateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Increase this rotation by a given angle around the specified axis. The update is done in series of small increments to avoid flipping."""
    def inverse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new MEulerRotation containing the inverse rotation of this one and reversed rotation order."""
    def invertIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place inversion of the rotation. Rotation order is also reversed."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if this rotation has the same order as another and their X, Y and Z components are within a tolerance of each other."""
    def isZero(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the X, Y and Z components are each within a tolerance of 0.0."""
    kIdentity: MEulerRotation = ...
    kTolerance: float = ...
    kXYZ: int = ...
    kXZY: int = ...
    kYXZ: int = ...
    kYZX: int = ...
    kZXY: int = ...
    kZYX: int = ...

    @property
    def order(*args: Any, **kwargs: Any) -> Any:
        """Rotation order"""
    @order.setter
    def order(*args: Any, **kwargs: Any) -> Any:
        """Rotation order"""
    def reorder(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new MEulerRotation having this rotation, reordered to use the given rotation order."""
    def reorderIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place reordering to use the given rotation order."""
    def setToAlternateSolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace this rotation with an alternate solution."""
    def setToClosestCut(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace this rotation with the closest cut to a target."""
    def setToClosestSolution(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace this rotation with the closest solution to a target."""
    def setValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set the rotation."""
    @property
    def x(*args: Any, **kwargs: Any) -> Any:
        """X rotation in radians"""
    @x.setter
    def x(*args: Any, **kwargs: Any) -> Any:
        """X rotation in radians"""
    @property
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y rotation in radians"""
    @y.setter
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y rotation in radians"""
    @property
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z rotation in radians"""
    @z.setter
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z rotation in radians"""

class MEvaluationNode:
    def datablock(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the datablock for this node."""
    def dependencyNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the dependency node this evaluation node represents."""
    def dirtyPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the top-most plug for the specified attribute if the attribute has dirty plugs. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to access a networked plug which is going to be dirty and computed."""
    def dirtyPlugExists(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the specified attribute has a dirty plug. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to verify which plugs are going to be dirty and computed."""
    def iterator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an iterator at the beginning of the dirty plug list."""

class MEvaluationNodeIterator:
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Checks to see if the iterator has reached the end of the iteration."""
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Advances the iterator to the next position in the dirty plug list."""
    def plug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the dirty plug at the current iterator position. Returns an empty plug if the iterator is illegal."""
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Resets the iterator to the first position in the dirty plug list."""

class MEventMessage(MMessage):
    def addEventCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addEventCallback(eventName, function, clientData=None) -> id

        This method registers a callback for event occurred messages.
        The callback function will be passed the any client data that
        was provided when the callback was registered.

         * eventName (string) - the event to register the
        callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def getEventNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEventNames() -> (string, string, ...)

        This method returns the list of available event names.

         * return: tuple of available event names.
        """

class MExternalContentInfoTable:
    def addResolvedEntry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addResolvedEntry(key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles) -> self

        Add an entry in the table.

        * key (string) - An arbitrary string defined by the caller. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.
        * unresolvedLocation (string) - Path as stored in the node (i.e. without any token replacement performed).
        * resolvedLocation (string) - Full path to the content if it exists at the time of creation of this object.
        * contextNodeFullName (string) - The fullname of the URI owner (node) if it applies, an empty string otherwise.
        * roles (list of strings) - An enumeration of all roles this content plays in the context of the node. The actual strings are not rigidly defined as of this writing. This is mostly for offline browsing of the content info: to assist in sorting content by role.  A better content type system may be introduced later on to	formalize this.
        """
    def addUnresolvedEntry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUnresolvedEntry(key, unresolvedLocation, contextNodeFullName, roles=None) -> self

        Add an entry in the table. The resolved location will be inferred from the application's built-in file resolving for the specified file type. This will automatically add entries into the roles vector that correspond to the search rules for this file type.

        * key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * unresolvedLocation (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * contextNodeFullName (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * roles (list of strings) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        """
    def getEntry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEntry(index) -> [key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

        Retrieves external content entry based on its position in the table.

        * index (unsigned int) - Position of the entry to retrieve information from.
        """
    def getInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getInfo(key) -> [unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

        Retrieves external content information based on its key.

        * key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        """

class MExternalContentLocationTable:
    def addEntry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addEntry(key, location) -> self

        Adds an external content location and its key to the table.

        * key (string) - An arbitrary string defined by the node. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.* location (string) - Full path to the content referenced by the key.
        """
    def getEntry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEntry(index) -> [key, location]

        Retrieves external content entry based on its position in the table.

        * index (unsigned int) - Position of the entry to retrieve information from.
        """
    def getLocation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLocation(key) -> string

        Retrieves an entry's location based on the associated key.

        * key (string) - See documentation of MExternalContentLocationTable.addEntry().
        """

class MFileObject:
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source file object.

        * source (MFileObject) - The source file object to copy from
        """
    def exists(self: Self, *args: Any, **kwargs: Any) -> Any:
        """exists(index=None) -> bool

        Checks to see if the file exists and is readable.
        If index is None tests for the fullName file, else tests the file constructed from the indicated portion of the path element and filename element.

        * index (int) - Index of the path element to be used in searching for the file.
        """
    def expandedFullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """expandedFullName() -> string

        Returns the pathname of a file constructed from the unresolved file object values. The file name will consist of the the expanded raw path and raw name elements.
        All variables in the path element are expanded, and the first path (the part before the first separator (':') in the path) is prepended to the filename element to construct the fullName.

        After expanding environment variables Maya may perform additional modifications to the full file name in order to resolve it to a valid location on disk. This resolved full file name can be accessed through resolvedFullName().
        """
    def expandedPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """expandedPath() -> string

        Returns the raw path element of the unresolved file object with all environment variables expanded. In the case that the path expands to multiple paths, the first expanded path will be returned.

        After expanding environment variables Maya may perform additional modifications to the path in order to resolve it to a valid location on disk. This resolved path can be accessed through resolvedPath().
        """
    def fullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fullName(index) -> string

        Returns the pathname of a file constructed from the indicated portion of the path element and filename element.
        All variables in the path element are expanded, and the indicated path portion is prepended to the filename element to construct the fullName.

        * index (int) - the index of the desired path portion.
        """
    def getResolvedFullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getResolvedFullName(rawFullName) -> string

        Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful.

        * rawFullName (string) - The fully specified unresolved path.
        """
    def getResolvedFullNameAndExistsStatus(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getResolvedFullNameAndExistsStatus(rawFullName, method=kNone) -> (string, bool)

        Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful, and a boolean that indicate if the resolved path exists or not.

        * rawFullName (string) - The fully specified unresolved path
        * resolveMethod (int) - To resolve method to use, default is kNone.

        Valid resolve methods:
          kNone                    The resolved path is simply the resulting path after converting
                                   the raw value to its expanded form. If the path contains environment variables,
                                   the resolved value will be the first path returned from their expansion.
                                   Relative paths will be considered to be relative to root of the current project.
                                   The resolution algorithm will not check if this file actually exists - the
                                   resolution will be considered successful whether it exists or not.
                                   With this mode, the resolver will not continue on to attempt to resolve
                                   using any other resolve method.
                                   The user must explicitly check MFileObject.exists() to determine if it is an
                                   existing path.
          kExact                   Checks if expanded paths exist. If paths are relative, assume it's relative to
                                   the current workspace (so check workspace current directory, file-rule directory and
                                   root directory).
          kDirMap                  Checks path against mappings defined with the dirmap command. Only for absolute paths
          kReferenceMappings       Check path against any previously re-mapped reference locations. If kRelative/kBaseName
                                   are set, then even if we have an absolute path, convert to relative and/or baseName and
                                   look for them in directories provided to the missing reference dialog.
          kRelative                Strips away the project directory, and treats path as relative. Relative to the current
                                   workspace, that is. So look in the workspace current directory, file-rules directory
                                   and the root directory.
          kBaseName                Strips away everything but the base file name and look in the current workspace,
          kInputFile               This mode is the default on file open and import, and is suitable for
                                   files that are to be used as input files.  The file will be checked for
                                   existence.
                                   Combination of kExact, kDirMap, kRelative and kBaseName.
          kInputReference          This mode is the default on file reference. In addition to the checks done for
                                   a regular input file, it will also check the reference mappings.
                                   Combination of kInputFile and kReferenceMappings.
          kStrict                  Combination of kExact and kDirMap.
        """
    def isAbsolutePath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isAbsolutePath(fileName) -> bool

        Checks a file path string and determines if it represents an absolute file path. An absolute path can uniquely identify a directory or file.

        * fileName (string) - the string used to check if it is absolute
        """
    def isSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isSet() -> bool

        Checks to see if both file and path elements of the file object have been set.
        """
    kBaseName: int = ...
    kDirMap: int = ...
    kExact: int = ...
    kInputFile: int = ...
    kInputReference: int = ...
    kNone: int = ...
    kReferenceMappings: int = ...
    kRelative: int = ...
    kStrict: int = ...

    def overrideResolvedFullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """overrideResolvedFullName(fullFileName, reresolveType=False) -> self

        Normally when a raw file name is set, Maya will perform a series of operations on it in an attempt to resolve it to a valid file name. This final resolved file name can be accessed through the resolvedName(), resolvedPath(), and resolvedFullFileName() methods and can be quite different from the originally specified raw file name.

        This method will override the normal Maya path resolution process and explicitly set the resolved file name. This path does not have to be a valid file path, but if any '/' characters appear in the given name then the resolved path element of the file object is set to everything in name up to, but not including the last '/'. The resolved filename is set to the part of name after the final '/'.

        Once the resolved file name is set, it is only guaranteed to be retained in the file object so long as the raw file path is not updated. Once the rawPath, rawName or rawFullName are set, the normal Maya path resolution process will be re-invoked and the resolved path and filename will be updated.

        - fullFileName (string) - the string used to override the path and filename.- reresolveType (bool) - if Maya should re-resolve the file type/translator.
        """
    def path(self: Self, *args: Any, **kwargs: Any) -> Any:
        """path(index) -> string

        Returns the indicated portion of the path element of the file object.  All variables in the path element are expanded, and the portion indicated by the argument is extracted and returned.

        * index (int) - the index of the desired path portion.
        """
    def pathCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pathCount() -> int

        Returns the number of paths in the path element of the file object.
        This will be equal to one more than the number of ':' characters specified of the rawPath attribute.
        """
    def rawFullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rawFullName() -> string

        Returns the unresolved full file name (path plus filename) of the MFileObject with all environment variables unexpanded.

        This method differs from expandedFullName() in that it returns the unexpanded instead of expanded values.
        """
    def rawName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rawName() -> string

        Returns the unresolved filename element of the MFileObject.
        """
    def rawPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rawPath() -> string

        Returns the path element of the MFileObject with all environment variables unexpanded.
        """
    def rawURI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rawURI() -> MURI

        Returns the unresolved URI of the MFileObject, if any.

        This will be empty if the MFileObject was not resolved from a URI.
        """
    @property
    def resolveMethod(*args: Any, **kwargs: Any) -> Any:
        """The file-path resolution steps this file object will use."""
    @resolveMethod.setter
    def resolveMethod(*args: Any, **kwargs: Any) -> Any:
        """The file-path resolution steps this file object will use."""
    def resolvedFullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resolvedFullName() -> string

        Returns the first pathname of a file constructed from the path and filename elements.  All variables in the path element are expanded, and the first path (the part before the first ':' in the path) is prepended to the filename element. After expanding all environment	variables Maya may then perform additional modifications, such	as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.

        The resolution is performed using the ResolveMethod of the file object.
        By default, this will be set to kNone. While this is suitable in many situations, it may not be appropriate if the file is expected to exist.
        Refer to getResolvedFullNameAndExistsStatus() for more information about how the  resolution mode is used.

        Failure to resolve the path according to the specifications of the file object will result in an empty return value.
        """
    def resolvedName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resolvedName() -> string

        Returns the resolved filename element of the file object.
        """
    def resolvedPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resolvedPath() -> string

        Returns the resolved path element of the file object. In order to build the resolved path, Maya first expands all environment variables and then may perform additional modifications, such as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.
        """
    def setRawFullName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRawFullName(fullFileName) -> self

        This method combines the functions of the setRawName and setRawPath methods in that it sets both the path and filename from the given name.

        If any '/' characters appear in the given name then the path element of the MFileObject is set to everything in name up to, but not including the last '/'.  The filename is set to the part of name after the final '/'.

        If no '/' characters appear in the given name then the path element is set to "." and the filename is set to the given name.

        Note that if the specified fullFileName is relative, contains environment variables, or does not exist, the full names returned by resolvedFullName() and expandedFullName() may not match the fullFileName. See the description of resolvedFullName() and expandedFullName() for more information.

        Also note that for URI-based file paths (e.g. "arrow:uri_path_to_file"),  setRawFullName will not call setRawName and setRawPath (raw name and path will remain empty). Use resolvedName and resolvedPath to retrieve the resolved file path, or rawFullName to retrieve the unresolved file path.

        * fullFileName (string) - The string used to initialize the path and filename.
        """
    def setRawName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRawName(fileName) -> self

        Set the unresolved filename element of the MFileObject instance.  This name should not contain any '/' characters, it should indicate simply the name of a file.  The directories in which this name will be searched for are specified by setRawPath.

        * fileName (string) - The filename to set.
        """
    def setRawPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRawPath(pathName) -> self

        Set the unresolved path element of the MFileObject instance.  This should contain a list of directories, each separated by a single ':' character.  The pathnames can contain Unix environment variables in the form $VARNAME.  These will be expanded when paths to actual filenames are constructed.

        Note that if the specified pathName is relative, contains environment variables, or does not exist, the paths returned by resolvedPath() and expandedPath() may not match the rawPath. See the description of resolvedPath() and expandedPath() for more information.

        * pathName (string) - The path string.
        """
    def setRawURI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRawURI(uri) -> self

        Set the unresolved URI of the MFileObject instance.

        * uri (string or MURI) - The unresolved URI.
        """

class MFloatArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MFloatMatrix:
    def adjoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's adjoint."""
    def det3x3(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""
    def det4x4(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns this matrix's determinant."""
    def getElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix element for the specified row and column."""
    def homogenize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing the homogenized version of this matrix."""
    def inverse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's inverse."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two matrices, within a tolerance."""
    kTolerance: float = ...

    def setElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the matrix element for the specified row and column."""
    def setToIdentity(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the identity."""
    def setToProduct(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the product of the two matrices passed in."""
    def transpose(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's transpose."""

class MFloatPoint:
    def cartesianize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to cartesian form."""
    def distanceTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return distance between this point and another."""
    def homogenize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to homogenous form."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two points, within a tolerance."""
    kOrigin: MFloatPoint = ...
    kTolerance: float = ...

    def rationalize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to rational form."""
    @property
    def w(*args: Any, **kwargs: Any) -> Any:
        """W coordinate"""
    @w.setter
    def w(*args: Any, **kwargs: Any) -> Any:
        """W coordinate"""
    @property
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @x.setter
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @property
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @y.setter
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @property
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""
    @z.setter
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""

class MFloatPointArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MFloatVector:
    def angle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angle, in radians, between this vector and another."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within a given tolerance of being equal."""
    def isParallel(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within the given tolerance of being parallel."""
    kOneVector: MFloatVector = ...
    kTolerance: float = ...
    kXaxisVector: MFloatVector = ...
    kXnegAxisVector: MFloatVector = ...
    kYaxisVector: MFloatVector = ...
    kYnegAxisVector: MFloatVector = ...
    kZaxisVector: MFloatVector = ...
    kZeroVector: MFloatVector = ...
    kZnegAxisVector: MFloatVector = ...

    def length(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the magnitude of this vector."""
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector containing the normalized version of this one."""
    def normalize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Normalizes this vector in-place and returns a new reference to it."""
    def transformAsNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix and then normalizing the result."""
    @property
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @x.setter
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @property
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @y.setter
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @property
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""
    @z.setter
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""

class MFloatVectorArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MFn:
    kAISEnvFacade: int = ...
    kAddDoubleLinear: int = ...
    kAdskMaterial: int = ...
    kAffect: int = ...
    kAimConstraint: int = ...
    kAimMatrix: int = ...
    kAir: int = ...
    kAlignCurve: int = ...
    kAlignManip: int = ...
    kAlignSurface: int = ...
    kAmbientLight: int = ...
    kAngle: int = ...
    kAngleBetween: int = ...
    kAnimBlend: int = ...
    kAnimBlendInOut: int = ...
    kAnimCurve: int = ...
    kAnimCurveTimeToAngular: int = ...
    kAnimCurveTimeToDistance: int = ...
    kAnimCurveTimeToTime: int = ...
    kAnimCurveTimeToUnitless: int = ...
    kAnimCurveUnitlessToAngular: int = ...
    kAnimCurveUnitlessToDistance: int = ...
    kAnimCurveUnitlessToTime: int = ...
    kAnimCurveUnitlessToUnitless: int = ...
    kAnimLayer: int = ...
    kAnisotropy: int = ...
    kAnnotation: int = ...
    kAnyGeometryVarGroup: int = ...
    kArcLength: int = ...
    kAreaLight: int = ...
    kArrayMapper: int = ...
    kArrowManip: int = ...
    kArubaTesselate: int = ...
    kAssembly: int = ...
    kAsset: int = ...
    kAttachCurve: int = ...
    kAttachSurface: int = ...
    kAttribute: int = ...
    kAttribute2Double: int = ...
    kAttribute2Float: int = ...
    kAttribute2Int: int = ...
    kAttribute2Short: int = ...
    kAttribute3Double: int = ...
    kAttribute3Float: int = ...
    kAttribute3Int: int = ...
    kAttribute3Short: int = ...
    kAttribute4Double: int = ...
    kAudio: int = ...
    kAverageCurveManip: int = ...
    kAvgCurves: int = ...
    kAvgNurbsSurfacePoints: int = ...
    kAvgSurfacePoints: int = ...
    kAxesActionManip: int = ...
    kBackground: int = ...
    kBallProjectionManip: int = ...
    kBarnDoorManip: int = ...
    kBase: int = ...
    kBaseLattice: int = ...
    kBendLattice: int = ...
    kBevel: int = ...
    kBevelManip: int = ...
    kBevelPlus: int = ...
    kBezierCurve: int = ...
    kBezierCurveData: int = ...
    kBezierCurveToNurbs: int = ...
    kBinaryData: int = ...
    kBirailSrf: int = ...
    kBlend: int = ...
    kBlendColorSet: int = ...
    kBlendColors: int = ...
    kBlendDevice: int = ...
    kBlendFalloff: int = ...
    kBlendManip: int = ...
    kBlendMatrix: int = ...
    kBlendNodeAdditiveRotation: int = ...
    kBlendNodeAdditiveScale: int = ...
    kBlendNodeBase: int = ...
    kBlendNodeBoolean: int = ...
    kBlendNodeDouble: int = ...
    kBlendNodeDoubleAngle: int = ...
    kBlendNodeDoubleLinear: int = ...
    kBlendNodeEnum: int = ...
    kBlendNodeFloat: int = ...
    kBlendNodeFloatAngle: int = ...
    kBlendNodeFloatLinear: int = ...
    kBlendNodeInt16: int = ...
    kBlendNodeInt32: int = ...
    kBlendNodeTime: int = ...
    kBlendShape: int = ...
    kBlendTwoAttr: int = ...
    kBlendWeighted: int = ...
    kBlindData: int = ...
    kBlindDataTemplate: int = ...
    kBlinn: int = ...
    kBlinnMaterial: int = ...
    kBoundary: int = ...
    kBox: int = ...
    kBoxData: int = ...
    kBrownian: int = ...
    kBrush: int = ...
    kBulge: int = ...
    kBulgeLattice: int = ...
    kBump: int = ...
    kBump3d: int = ...
    kButtonManip: int = ...
    kCacheBase: int = ...
    kCacheBlend: int = ...
    kCacheFile: int = ...
    kCacheTrack: int = ...
    kCacheableNode: int = ...
    kCaddyManipBase: int = ...
    kCamera: int = ...
    kCameraManip: int = ...
    kCameraPlaneManip: int = ...
    kCameraSet: int = ...
    kCameraView: int = ...
    kCenterManip: int = ...
    kChainToSpline: int = ...
    kCharacter: int = ...
    kCharacterMap: int = ...
    kCharacterMappingData: int = ...
    kCharacterOffset: int = ...
    kChecker: int = ...
    kChoice: int = ...
    kChooser: int = ...
    kCircle: int = ...
    kCircleManip: int = ...
    kCirclePointManip: int = ...
    kCircleSweepManip: int = ...
    kClampColor: int = ...
    kClientDevice: int = ...
    kClip: int = ...
    kClipGhostShape: int = ...
    kClipLibrary: int = ...
    kClipScheduler: int = ...
    kClipToGhostData: int = ...
    kCloseCurve: int = ...
    kCloseSurface: int = ...
    kClosestPointOnMesh: int = ...
    kClosestPointOnSurface: int = ...
    kCloth: int = ...
    kCloud: int = ...
    kCluster: int = ...
    kClusterFilter: int = ...
    kClusterFlexor: int = ...
    kCoiManip: int = ...
    kCollision: int = ...
    kColorBackground: int = ...
    kColorMgtGlobals: int = ...
    kColorProfile: int = ...
    kCombinationShape: int = ...
    kCommCornerManip: int = ...
    kCommCornerOperManip: int = ...
    kCommEdgeOperManip: int = ...
    kCommEdgePtManip: int = ...
    kCommEdgeSegmentManip: int = ...
    kComponent: int = ...
    kComponentFalloff: int = ...
    kComponentListData: int = ...
    kComponentManip: int = ...
    kComponentMatch: int = ...
    kComposeMatrix: int = ...
    kCompoundAttribute: int = ...
    kConcentricProjectionManip: int = ...
    kCondition: int = ...
    kCone: int = ...
    kConstraint: int = ...
    kContainer: int = ...
    kContainerBase: int = ...
    kContourProjectionManip: int = ...
    kContrast: int = ...
    kControl: int = ...
    kControllerTag: int = ...
    kCopyColorSet: int = ...
    kCopyUVSet: int = ...
    kCpManip: int = ...
    kCrater: int = ...
    kCreaseSet: int = ...
    kCreate: int = ...
    kCreateBPManip: int = ...
    kCreateBezierManip: int = ...
    kCreateCVManip: int = ...
    kCreateColorSet: int = ...
    kCreateEPManip: int = ...
    kCreateSectionManip: int = ...
    kCreateUVSet: int = ...
    kCrossSectionEditManip: int = ...
    kCrossSectionManager: int = ...
    kCubicProjectionManip: int = ...
    kCurve: int = ...
    kCurveCVComponent: int = ...
    kCurveCurveIntersect: int = ...
    kCurveEPComponent: int = ...
    kCurveEdManip: int = ...
    kCurveFromMeshCoM: int = ...
    kCurveFromMeshEdge: int = ...
    kCurveFromSubdivEdge: int = ...
    kCurveFromSubdivFace: int = ...
    kCurveFromSurface: int = ...
    kCurveFromSurfaceBnd: int = ...
    kCurveFromSurfaceCoS: int = ...
    kCurveFromSurfaceIso: int = ...
    kCurveInfo: int = ...
    kCurveKnotComponent: int = ...
    kCurveNormalizerAngle: int = ...
    kCurveNormalizerLinear: int = ...
    kCurveParamComponent: int = ...
    kCurveSegmentManip: int = ...
    kCurveVarGroup: int = ...
    kCustomEvaluatorClusterNode: int = ...
    kCylinder: int = ...
    kCylindricalProjectionManip: int = ...
    kDOF: int = ...
    kDPbirailSrf: int = ...
    kDagContainer: int = ...
    kDagNode: int = ...
    kDagPose: int = ...
    kDagSelectionItem: int = ...
    kData: int = ...
    kData2Double: int = ...
    kData2Float: int = ...
    kData2Int: int = ...
    kData2Short: int = ...
    kData3Double: int = ...
    kData3Float: int = ...
    kData3Int: int = ...
    kData3Short: int = ...
    kData4Double: int = ...
    kDblTrsManip: int = ...
    kDecayRegionCapComponent: int = ...
    kDecayRegionComponent: int = ...
    kDecomposeMatrix: int = ...
    kDefaultLightList: int = ...
    kDeformBend: int = ...
    kDeformBendManip: int = ...
    kDeformFlare: int = ...
    kDeformFlareManip: int = ...
    kDeformFunc: int = ...
    kDeformSine: int = ...
    kDeformSineManip: int = ...
    kDeformSquash: int = ...
    kDeformSquashManip: int = ...
    kDeformTwist: int = ...
    kDeformTwistManip: int = ...
    kDeformWave: int = ...
    kDeformWaveManip: int = ...
    kDeleteColorSet: int = ...
    kDeleteComponent: int = ...
    kDeleteUVSet: int = ...
    kDeltaMush: int = ...
    kDependencyNode: int = ...
    kDetachCurve: int = ...
    kDetachSurface: int = ...
    kDiffuseMaterial: int = ...
    kDimension: int = ...
    kDimensionManip: int = ...
    kDirectedDisc: int = ...
    kDirectionManip: int = ...
    kDirectionalLight: int = ...
    kDiscManip: int = ...
    kDiskCache: int = ...
    kDispatchCompute: int = ...
    kDisplacementShader: int = ...
    kDisplayLayer: int = ...
    kDisplayLayerManager: int = ...
    kDistance: int = ...
    kDistanceBetween: int = ...
    kDistanceManip: int = ...
    kDofManip: int = ...
    kDoubleAngleAttribute: int = ...
    kDoubleArrayData: int = ...
    kDoubleIndexedComponent: int = ...
    kDoubleLinearAttribute: int = ...
    kDoubleShadingSwitch: int = ...
    kDrag: int = ...
    kDropOffFunction: int = ...
    kDropoffLocator: int = ...
    kDropoffManip: int = ...
    kDummy: int = ...
    kDummyConnectable: int = ...
    kDynAirManip: int = ...
    kDynArrayAttrsData: int = ...
    kDynAttenuationManip: int = ...
    kDynBase: int = ...
    kDynBaseFieldManip: int = ...
    kDynEmitterManip: int = ...
    kDynFieldsManip: int = ...
    kDynGlobals: int = ...
    kDynNewtonManip: int = ...
    kDynParticleSetComponent: int = ...
    kDynSpreadManip: int = ...
    kDynSweptGeometryData: int = ...
    kDynTurbulenceManip: int = ...
    kDynamicConstraint: int = ...
    kDynamicsController: int = ...
    kEdgeComponent: int = ...
    kEditCurve: int = ...
    kEditCurveManip: int = ...
    kEditMetadata: int = ...
    kEditsManager: int = ...
    kEmitter: int = ...
    kEnableManip: int = ...
    kEnumAttribute: int = ...
    kEnvBall: int = ...
    kEnvChrome: int = ...
    kEnvCube: int = ...
    kEnvFacade: int = ...
    kEnvFogMaterial: int = ...
    kEnvFogShape: int = ...
    kEnvSky: int = ...
    kEnvSphere: int = ...
    kExplodeNurbsShell: int = ...
    kExpression: int = ...
    kExtendCurve: int = ...
    kExtendCurveDistanceManip: int = ...
    kExtendSurface: int = ...
    kExtendSurfaceDistanceManip: int = ...
    kExtract: int = ...
    kExtrude: int = ...
    kExtrudeManip: int = ...
    kFFD: int = ...
    kFFblendSrf: int = ...
    kFFfilletSrf: int = ...
    kFacade: int = ...
    kFalloffEval: int = ...
    kFfdDualBase: int = ...
    kField: int = ...
    kFileBackground: int = ...
    kFileTexture: int = ...
    kFilletCurve: int = ...
    kFilter: int = ...
    kFilterClosestSample: int = ...
    kFilterEuler: int = ...
    kFilterSimplify: int = ...
    kFitBspline: int = ...
    kFixedLineManip: int = ...
    kFlexor: int = ...
    kFloatAngleAttribute: int = ...
    kFloatArrayData: int = ...
    kFloatLinearAttribute: int = ...
    kFloatMatrixAttribute: int = ...
    kFloatVectorArrayData: int = ...
    kFlow: int = ...
    kFluid: int = ...
    kFluidData: int = ...
    kFluidEmitter: int = ...
    kFluidGeom: int = ...
    kFluidTexture2D: int = ...
    kFluidTexture3D: int = ...
    kFollicle: int = ...
    kForceUpdateManip: int = ...
    kFosterParent: int = ...
    kFourByFourMatrix: int = ...
    kFractal: int = ...
    kFreePointManip: int = ...
    kFreePointTriadManip: int = ...
    kGammaCorrect: int = ...
    kGenericAttribute: int = ...
    kGeoConnectable: int = ...
    kGeoConnector: int = ...
    kGeomBind: int = ...
    kGeometric: int = ...
    kGeometryConstraint: int = ...
    kGeometryData: int = ...
    kGeometryFilt: int = ...
    kGeometryOnLineManip: int = ...
    kGeometryVarGroup: int = ...
    kGlobalCacheControls: int = ...
    kGlobalStitch: int = ...
    kGranite: int = ...
    kGravity: int = ...
    kGreasePencilSequence: int = ...
    kGreasePlane: int = ...
    kGreasePlaneRenderShape: int = ...
    kGrid: int = ...
    kGroundPlane: int = ...
    kGroupId: int = ...
    kGroupParts: int = ...
    kGuide: int = ...
    kGuideLine: int = ...
    kHairConstraint: int = ...
    kHairSystem: int = ...
    kHairTubeShader: int = ...
    kHandleRotateManip: int = ...
    kHardenPointCurve: int = ...
    kHardwareReflectionMap: int = ...
    kHardwareRenderGlobals: int = ...
    kHardwareRenderingGlobals: int = ...
    kHeightField: int = ...
    kHikEffector: int = ...
    kHikFKJoint: int = ...
    kHikFloorContactMarker: int = ...
    kHikGroundPlane: int = ...
    kHikHandle: int = ...
    kHikIKEffector: int = ...
    kHikSolver: int = ...
    kHistorySwitch: int = ...
    kHsvToRgb: int = ...
    kHwShaderNode: int = ...
    kHyperGraphInfo: int = ...
    kHyperLayout: int = ...
    kHyperLayoutDG: int = ...
    kHyperView: int = ...
    kIkEffector: int = ...
    kIkHandle: int = ...
    kIkRPManip: int = ...
    kIkSolver: int = ...
    kIkSplineManip: int = ...
    kIkSystem: int = ...
    kIllustratorCurve: int = ...
    kImageAdd: int = ...
    kImageBlur: int = ...
    kImageColorCorrect: int = ...
    kImageData: int = ...
    kImageDepth: int = ...
    kImageDiff: int = ...
    kImageDisplay: int = ...
    kImageFilter: int = ...
    kImageLoad: int = ...
    kImageMotionBlur: int = ...
    kImageMultiply: int = ...
    kImageNetDest: int = ...
    kImageNetSrc: int = ...
    kImageOver: int = ...
    kImagePlane: int = ...
    kImageRender: int = ...
    kImageSave: int = ...
    kImageSource: int = ...
    kImageUnder: int = ...
    kImageView: int = ...
    kImplicitCone: int = ...
    kImplicitSphere: int = ...
    kInsertKnotCrv: int = ...
    kInsertKnotSrf: int = ...
    kInstancer: int = ...
    kInt64ArrayData: int = ...
    kIntArrayData: int = ...
    kIntersectSurface: int = ...
    kInvalid: int = ...
    kIsoparmComponent: int = ...
    kIsoparmManip: int = ...
    kItemList: int = ...
    kJiggleDeformer: int = ...
    kJoint: int = ...
    kJointCluster: int = ...
    kJointClusterManip: int = ...
    kJointTranslateManip: int = ...
    kKeyframeDelta: int = ...
    kKeyframeDeltaAddRemove: int = ...
    kKeyframeDeltaBlockAddRemove: int = ...
    kKeyframeDeltaBreakdown: int = ...
    kKeyframeDeltaInfType: int = ...
    kKeyframeDeltaMove: int = ...
    kKeyframeDeltaScale: int = ...
    kKeyframeDeltaTangent: int = ...
    kKeyframeDeltaWeighted: int = ...
    kKeyframeRegionManip: int = ...
    kKeyingGroup: int = ...
    kLambert: int = ...
    kLambertMaterial: int = ...
    kLattice: int = ...
    kLatticeComponent: int = ...
    kLatticeData: int = ...
    kLatticeGeom: int = ...
    kLayeredShader: int = ...
    kLayeredTexture: int = ...
    kLeastSquares: int = ...
    kLeather: int = ...
    kLight: int = ...
    kLightDataAttribute: int = ...
    kLightFogMaterial: int = ...
    kLightInfo: int = ...
    kLightLink: int = ...
    kLightList: int = ...
    kLightManip: int = ...
    kLightProjectionGeometry: int = ...
    kLightSource: int = ...
    kLightSourceMaterial: int = ...
    kLimitManip: int = ...
    kLineArrowManip: int = ...
    kLineManip: int = ...
    kLineModifier: int = ...
    kLinearLight: int = ...
    kLocator: int = ...
    kLodGroup: int = ...
    kLodThresholds: int = ...
    kLookAt: int = ...
    kLuminance: int = ...
    kMCsolver: int = ...
    kMPbirailSrf: int = ...
    kMakeGroup: int = ...
    kMandelbrot: int = ...
    kMandelbrot3D: int = ...
    kManip2DContainer: int = ...
    kManipContainer: int = ...
    kManipulator: int = ...
    kManipulator2D: int = ...
    kManipulator3D: int = ...
    kMarble: int = ...
    kMarker: int = ...
    kMarkerManip: int = ...
    kMaterial: int = ...
    kMaterialFacade: int = ...
    kMaterialInfo: int = ...
    kMaterialTemplate: int = ...
    kMatrixAdd: int = ...
    kMatrixArrayData: int = ...
    kMatrixAttribute: int = ...
    kMatrixData: int = ...
    kMatrixFloatData: int = ...
    kMatrixHold: int = ...
    kMatrixMult: int = ...
    kMatrixPass: int = ...
    kMatrixWtAdd: int = ...
    kMembrane: int = ...
    kMentalRayTexture: int = ...
    kMergeVertsToolManip: int = ...
    kMesh: int = ...
    kMeshComponent: int = ...
    kMeshData: int = ...
    kMeshEdgeComponent: int = ...
    kMeshFaceVertComponent: int = ...
    kMeshFrEdgeComponent: int = ...
    kMeshGeom: int = ...
    kMeshMapComponent: int = ...
    kMeshPolygonComponent: int = ...
    kMeshVarGroup: int = ...
    kMeshVertComponent: int = ...
    kMeshVtxFaceComponent: int = ...
    kMessageAttribute: int = ...
    kMidModifier: int = ...
    kMidModifierWithMatrix: int = ...
    kModel: int = ...
    kModifyEdgeBaseManip: int = ...
    kModifyEdgeCrvManip: int = ...
    kModifyEdgeManip: int = ...
    kMorph: int = ...
    kMotionPath: int = ...
    kMotionPathManip: int = ...
    kMountain: int = ...
    kMoveUVShellManip2D: int = ...
    kMoveVertexManip: int = ...
    kMultDoubleLinear: int = ...
    kMultiSubVertexComponent: int = ...
    kMultilisterLight: int = ...
    kMultiplyDivide: int = ...
    kMute: int = ...
    kNBase: int = ...
    kNCloth: int = ...
    kNComponent: int = ...
    kNId: int = ...
    kNIdData: int = ...
    kNLE: int = ...
    kNObject: int = ...
    kNObjectData: int = ...
    kNParticle: int = ...
    kNRigid: int = ...
    kNamedObject: int = ...
    kNearestPointOnCurve: int = ...
    kNewton: int = ...
    kNodeGraphEditorBookmarkInfo: int = ...
    kNodeGraphEditorBookmarks: int = ...
    kNodeGraphEditorInfo: int = ...
    kNoise: int = ...
    kNonAmbientLight: int = ...
    kNonDagSelectionItem: int = ...
    kNonExtendedLight: int = ...
    kNonLinear: int = ...
    kNormalConstraint: int = ...
    kNucleus: int = ...
    kNumericAttribute: int = ...
    kNumericData: int = ...
    kNurbsBoolean: int = ...
    kNurbsCircular2PtArc: int = ...
    kNurbsCircular3PtArc: int = ...
    kNurbsCube: int = ...
    kNurbsCurve: int = ...
    kNurbsCurveData: int = ...
    kNurbsCurveGeom: int = ...
    kNurbsCurveToBezier: int = ...
    kNurbsPlane: int = ...
    kNurbsSquare: int = ...
    kNurbsSurface: int = ...
    kNurbsSurfaceData: int = ...
    kNurbsSurfaceGeom: int = ...
    kNurbsTesselate: int = ...
    kNurbsToSubdiv: int = ...
    kObjectAttrFilter: int = ...
    kObjectBinFilter: int = ...
    kObjectFilter: int = ...
    kObjectMultiFilter: int = ...
    kObjectNameFilter: int = ...
    kObjectRenderFilter: int = ...
    kObjectScriptFilter: int = ...
    kObjectTypeFilter: int = ...
    kOcean: int = ...
    kOceanDeformer: int = ...
    kOceanShader: int = ...
    kOffsetCos: int = ...
    kOffsetCosManip: int = ...
    kOffsetCurve: int = ...
    kOffsetCurveManip: int = ...
    kOffsetSurface: int = ...
    kOffsetSurfaceManip: int = ...
    kOldGeometryConstraint: int = ...
    kOpticalFX: int = ...
    kOrientConstraint: int = ...
    kOrientationComponent: int = ...
    kOrientationLocator: int = ...
    kOrientationMarker: int = ...
    kOrthoGrid: int = ...
    kPASolver: int = ...
    kPairBlend: int = ...
    kParamDimension: int = ...
    kParentConstraint: int = ...
    kParticle: int = ...
    kParticleAgeMapper: int = ...
    kParticleCloud: int = ...
    kParticleColorMapper: int = ...
    kParticleIncandecenceMapper: int = ...
    kParticleSamplerInfo: int = ...
    kParticleTransparencyMapper: int = ...
    kPartition: int = ...
    kPassContributionMap: int = ...
    kPfxGeometry: int = ...
    kPfxHair: int = ...
    kPfxToon: int = ...
    kPhong: int = ...
    kPhongExplorer: int = ...
    kPhongMaterial: int = ...
    kPickMatrix: int = ...
    kPivotComponent: int = ...
    kPivotManip2D: int = ...
    kPlace2dTexture: int = ...
    kPlace3dTexture: int = ...
    kPlanarProjectionManip: int = ...
    kPlanarTrimSrf: int = ...
    kPlane: int = ...
    kPlugin: int = ...
    kPluginBlendShape: int = ...
    kPluginCameraSet: int = ...
    kPluginClientDevice: int = ...
    kPluginConstraintNode: int = ...
    kPluginData: int = ...
    kPluginDeformerNode: int = ...
    kPluginDependNode: int = ...
    kPluginEmitterNode: int = ...
    kPluginFieldNode: int = ...
    kPluginGeometryData: int = ...
    kPluginGeometryFilter: int = ...
    kPluginHardwareShader: int = ...
    kPluginHwShaderNode: int = ...
    kPluginIkSolver: int = ...
    kPluginImagePlaneNode: int = ...
    kPluginLocatorNode: int = ...
    kPluginManipContainer: int = ...
    kPluginManipulatorNode: int = ...
    kPluginMotionPathNode: int = ...
    kPluginObjectSet: int = ...
    kPluginParticleAttributeMapperNode: int = ...
    kPluginShape: int = ...
    kPluginSkinCluster: int = ...
    kPluginSpringNode: int = ...
    kPluginThreadedDevice: int = ...
    kPluginTransformNode: int = ...
    kPlusMinusAverage: int = ...
    kPointArrayData: int = ...
    kPointConstraint: int = ...
    kPointLight: int = ...
    kPointManip: int = ...
    kPointMatrixMult: int = ...
    kPointOnCurveInfo: int = ...
    kPointOnCurveManip: int = ...
    kPointOnLineManip: int = ...
    kPointOnPolyConstraint: int = ...
    kPointOnSurfaceInfo: int = ...
    kPointOnSurfaceManip: int = ...
    kPoleVectorConstraint: int = ...
    kPolyAppend: int = ...
    kPolyAppendVertex: int = ...
    kPolyArrow: int = ...
    kPolyAutoProj: int = ...
    kPolyAutoProjManip: int = ...
    kPolyAverageVertex: int = ...
    kPolyBevel: int = ...
    kPolyBevel2: int = ...
    kPolyBevel3: int = ...
    kPolyBlindData: int = ...
    kPolyBoolOp: int = ...
    kPolyBridgeEdge: int = ...
    kPolyCBoolOp: int = ...
    kPolyCaddyManip: int = ...
    kPolyChipOff: int = ...
    kPolyCircularize: int = ...
    kPolyClean: int = ...
    kPolyCloseBorder: int = ...
    kPolyCollapseEdge: int = ...
    kPolyCollapseF: int = ...
    kPolyColorDel: int = ...
    kPolyColorMod: int = ...
    kPolyColorPerVertex: int = ...
    kPolyComponentData: int = ...
    kPolyCone: int = ...
    kPolyConnectComponents: int = ...
    kPolyContourProj: int = ...
    kPolyCreaseEdge: int = ...
    kPolyCreateFacet: int = ...
    kPolyCreateToolManip: int = ...
    kPolyCreator: int = ...
    kPolyCube: int = ...
    kPolyCut: int = ...
    kPolyCutManip: int = ...
    kPolyCutManipContainer: int = ...
    kPolyCylProj: int = ...
    kPolyCylinder: int = ...
    kPolyDelEdge: int = ...
    kPolyDelFacet: int = ...
    kPolyDelVertex: int = ...
    kPolyDuplicateEdge: int = ...
    kPolyEdgeToCurve: int = ...
    kPolyEditEdgeFlow: int = ...
    kPolyExtrudeEdge: int = ...
    kPolyExtrudeFacet: int = ...
    kPolyExtrudeManip: int = ...
    kPolyExtrudeManipContainer: int = ...
    kPolyExtrudeVertex: int = ...
    kPolyFlipEdge: int = ...
    kPolyFlipUV: int = ...
    kPolyHelix: int = ...
    kPolyHoleFace: int = ...
    kPolyLayoutUV: int = ...
    kPolyMapCut: int = ...
    kPolyMapDel: int = ...
    kPolyMapSew: int = ...
    kPolyMapSewMove: int = ...
    kPolyMappingManip: int = ...
    kPolyMergeEdge: int = ...
    kPolyMergeFacet: int = ...
    kPolyMergeUV: int = ...
    kPolyMergeVert: int = ...
    kPolyMesh: int = ...
    kPolyMirror: int = ...
    kPolyMirrorManipContainer: int = ...
    kPolyModifierManip: int = ...
    kPolyModifierManipContainer: int = ...
    kPolyMoveEdge: int = ...
    kPolyMoveFacet: int = ...
    kPolyMoveFacetUV: int = ...
    kPolyMoveUV: int = ...
    kPolyMoveUVManip: int = ...
    kPolyMoveVertex: int = ...
    kPolyMoveVertexManip: int = ...
    kPolyMoveVertexUV: int = ...
    kPolyNormal: int = ...
    kPolyNormalPerVertex: int = ...
    kPolyNormalizeUV: int = ...
    kPolyPassThru: int = ...
    kPolyPinUV: int = ...
    kPolyPipe: int = ...
    kPolyPlanProj: int = ...
    kPolyPlatonicSolid: int = ...
    kPolyPoke: int = ...
    kPolyPokeManip: int = ...
    kPolyPrimitive: int = ...
    kPolyPrimitiveMisc: int = ...
    kPolyPrism: int = ...
    kPolyProj: int = ...
    kPolyProjectCurve: int = ...
    kPolyProjectionManip: int = ...
    kPolyPyramid: int = ...
    kPolyQuad: int = ...
    kPolyReduce: int = ...
    kPolyRemesh: int = ...
    kPolySelectEditFeedbackManip: int = ...
    kPolySeparate: int = ...
    kPolySewEdge: int = ...
    kPolySmooth: int = ...
    kPolySmoothFacet: int = ...
    kPolySmoothProxy: int = ...
    kPolySoftEdge: int = ...
    kPolySphProj: int = ...
    kPolySphere: int = ...
    kPolySpinEdge: int = ...
    kPolySplit: int = ...
    kPolySplitEdge: int = ...
    kPolySplitRing: int = ...
    kPolySplitToolManip: int = ...
    kPolySplitVert: int = ...
    kPolyStraightenUVBorder: int = ...
    kPolySubdEdge: int = ...
    kPolySubdFacet: int = ...
    kPolyToSubdiv: int = ...
    kPolyToolFeedbackManip: int = ...
    kPolyToolFeedbackShape: int = ...
    kPolyTorus: int = ...
    kPolyTransfer: int = ...
    kPolyTriangulate: int = ...
    kPolyTweak: int = ...
    kPolyTweakUV: int = ...
    kPolyUVRectangle: int = ...
    kPolyUnite: int = ...
    kPolyVertexNormalManip: int = ...
    kPolyWedgeFace: int = ...
    kPoseInterpolatorManager: int = ...
    kPositionMarker: int = ...
    kPostProcessList: int = ...
    kPrecompExport: int = ...
    kPrimitive: int = ...
    kPrimitiveFalloff: int = ...
    kProjectCurve: int = ...
    kProjectTangent: int = ...
    kProjectTangentManip: int = ...
    kProjection: int = ...
    kProjectionManip: int = ...
    kProjectionMultiManip: int = ...
    kProjectionUVManip: int = ...
    kPropModManip: int = ...
    kPropMoveTriadManip: int = ...
    kProximityFalloff: int = ...
    kProximityPin: int = ...
    kProximityWrap: int = ...
    kProxy: int = ...
    kProxyManager: int = ...
    kPsdFileTexture: int = ...
    kQuadPtOnLineManip: int = ...
    kQuadShadingSwitch: int = ...
    kRBFsurface: int = ...
    kRPsolver: int = ...
    kRadial: int = ...
    kRadius: int = ...
    kRamp: int = ...
    kRampBackground: int = ...
    kRampShader: int = ...
    kRbfSrfManip: int = ...
    kReForm: int = ...
    kRebuildCurve: int = ...
    kRebuildSurface: int = ...
    kRecord: int = ...
    kReference: int = ...
    kReflect: int = ...
    kRemapColor: int = ...
    kRemapHsv: int = ...
    kRemapValue: int = ...
    kRenderBox: int = ...
    kRenderCone: int = ...
    kRenderGlobals: int = ...
    kRenderGlobalsList: int = ...
    kRenderLayer: int = ...
    kRenderLayerManager: int = ...
    kRenderPass: int = ...
    kRenderPassSet: int = ...
    kRenderQuality: int = ...
    kRenderRect: int = ...
    kRenderSetup: int = ...
    kRenderSphere: int = ...
    kRenderTarget: int = ...
    kRenderUtilityList: int = ...
    kRenderedImageSource: int = ...
    kRenderingList: int = ...
    kReorderUVSet: int = ...
    kResolution: int = ...
    kResultCurve: int = ...
    kResultCurveTimeToAngular: int = ...
    kResultCurveTimeToDistance: int = ...
    kResultCurveTimeToTime: int = ...
    kResultCurveTimeToUnitless: int = ...
    kReverse: int = ...
    kReverseCrvManip: int = ...
    kReverseCurve: int = ...
    kReverseCurveManip: int = ...
    kReverseSurface: int = ...
    kReverseSurfaceManip: int = ...
    kRevolve: int = ...
    kRevolveManip: int = ...
    kRevolvedPrimitive: int = ...
    kRevolvedPrimitiveManip: int = ...
    kRgbToHsv: int = ...
    kRigid: int = ...
    kRigidConstraint: int = ...
    kRigidDeform: int = ...
    kRigidSolver: int = ...
    kRock: int = ...
    kRotateBoxManip: int = ...
    kRotateLimitsManip: int = ...
    kRotateManip: int = ...
    kRotateUVManip2D: int = ...
    kRoundConstantRadius: int = ...
    kRoundConstantRadiusManip: int = ...
    kRoundRadiusCrvManip: int = ...
    kRoundRadiusManip: int = ...
    kSCsolver: int = ...
    kSPbirailSrf: int = ...
    kSamplerInfo: int = ...
    kScaleConstraint: int = ...
    kScaleLimitsManip: int = ...
    kScaleManip: int = ...
    kScalePointManip: int = ...
    kScaleUVManip2D: int = ...
    kScalingBoxManip: int = ...
    kScreenAlignedCircleManip: int = ...
    kScript: int = ...
    kScriptManip: int = ...
    kSculpt: int = ...
    kSectionManip: int = ...
    kSelectionItem: int = ...
    kSelectionList: int = ...
    kSelectionListData: int = ...
    kSelectionListOperator: int = ...
    kSequenceManager: int = ...
    kSequencer: int = ...
    kSet: int = ...
    kSetGroupComponent: int = ...
    kSetRange: int = ...
    kSfRevolveManip: int = ...
    kShaderGlow: int = ...
    kShaderList: int = ...
    kShadingEngine: int = ...
    kShadingMap: int = ...
    kShape: int = ...
    kShapeEditorManager: int = ...
    kShapeFragment: int = ...
    kShot: int = ...
    kShrinkWrapFilter: int = ...
    kSimpleVolumeShader: int = ...
    kSingleIndexedComponent: int = ...
    kSingleShadingSwitch: int = ...
    kSketchPlane: int = ...
    kSkin: int = ...
    kSkinBinding: int = ...
    kSkinClusterFilter: int = ...
    kSkinShader: int = ...
    kSl60: int = ...
    kSmear: int = ...
    kSmoothCurve: int = ...
    kSmoothTangentSrf: int = ...
    kSnapUVManip2D: int = ...
    kSnapshot: int = ...
    kSnapshotPath: int = ...
    kSnapshotShape: int = ...
    kSnow: int = ...
    kSoftMod: int = ...
    kSoftModFilter: int = ...
    kSoftModManip: int = ...
    kSolidFractal: int = ...
    kSolidify: int = ...
    kSphere: int = ...
    kSphereData: int = ...
    kSphericalProjectionManip: int = ...
    kSplineSolver: int = ...
    kSpotCylinderManip: int = ...
    kSpotLight: int = ...
    kSpotManip: int = ...
    kSpring: int = ...
    kSprite: int = ...
    kSquareSrf: int = ...
    kSquareSrfManip: int = ...
    kStandardSurface: int = ...
    kStateManip: int = ...
    kStencil: int = ...
    kStereoCameraMaster: int = ...
    kStitchAsNurbsShell: int = ...
    kStitchSrf: int = ...
    kStitchSrfManip: int = ...
    kStoryBoard: int = ...
    kStringArrayData: int = ...
    kStringData: int = ...
    kStringShadingSwitch: int = ...
    kStroke: int = ...
    kStrokeGlobals: int = ...
    kStucco: int = ...
    kStudioClearCoat: int = ...
    kStyleCurve: int = ...
    kSubCurve: int = ...
    kSubSurface: int = ...
    kSubVertexComponent: int = ...
    kSubdAddTopology: int = ...
    kSubdAutoProj: int = ...
    kSubdBlindData: int = ...
    kSubdBoolean: int = ...
    kSubdCleanTopology: int = ...
    kSubdCloseBorder: int = ...
    kSubdDelFace: int = ...
    kSubdExtrudeFace: int = ...
    kSubdHierBlind: int = ...
    kSubdLayoutUV: int = ...
    kSubdMapCut: int = ...
    kSubdMapSewMove: int = ...
    kSubdMappingManip: int = ...
    kSubdMergeVert: int = ...
    kSubdModifier: int = ...
    kSubdModifyEdge: int = ...
    kSubdMoveEdge: int = ...
    kSubdMoveFace: int = ...
    kSubdMoveVertex: int = ...
    kSubdPlanProj: int = ...
    kSubdProjectionManip: int = ...
    kSubdSplitFace: int = ...
    kSubdSubdivideFace: int = ...
    kSubdTweak: int = ...
    kSubdTweakUV: int = ...
    kSubdiv: int = ...
    kSubdivCVComponent: int = ...
    kSubdivCollapse: int = ...
    kSubdivCompId: int = ...
    kSubdivData: int = ...
    kSubdivEdgeComponent: int = ...
    kSubdivFaceComponent: int = ...
    kSubdivGeom: int = ...
    kSubdivMapComponent: int = ...
    kSubdivReverseFaces: int = ...
    kSubdivSurfaceVarGroup: int = ...
    kSubdivToNurbs: int = ...
    kSubdivToPoly: int = ...
    kSubsetFalloff: int = ...
    kSummaryObject: int = ...
    kSuper: int = ...
    kSurface: int = ...
    kSurfaceCVComponent: int = ...
    kSurfaceEPComponent: int = ...
    kSurfaceEdManip: int = ...
    kSurfaceFaceComponent: int = ...
    kSurfaceInfo: int = ...
    kSurfaceKnotComponent: int = ...
    kSurfaceLuminance: int = ...
    kSurfaceRangeComponent: int = ...
    kSurfaceShader: int = ...
    kSurfaceVarGroup: int = ...
    kSymmetryConstraint: int = ...
    kSymmetryLocator: int = ...
    kSymmetryMapCurve: int = ...
    kSymmetryMapVector: int = ...
    kTangentConstraint: int = ...
    kTension: int = ...
    kTexLattice: int = ...
    kTexLatticeDeformManip: int = ...
    kTexSmoothManip: int = ...
    kTexSmudgeUVManip: int = ...
    kTextButtonManip: int = ...
    kTextCurves: int = ...
    kTextManip: int = ...
    kTexture2d: int = ...
    kTexture3d: int = ...
    kTextureBakeSet: int = ...
    kTextureDeformer: int = ...
    kTextureDeformerHandle: int = ...
    kTextureEnv: int = ...
    kTextureList: int = ...
    kTextureManip3D: int = ...
    kThreadedDevice: int = ...
    kThreePointArcManip: int = ...
    kTime: int = ...
    kTimeAttribute: int = ...
    kTimeEditor: int = ...
    kTimeEditorAnimSource: int = ...
    kTimeEditorClip: int = ...
    kTimeEditorClipBase: int = ...
    kTimeEditorClipEvaluator: int = ...
    kTimeEditorInterpolator: int = ...
    kTimeEditorTracks: int = ...
    kTimeFunction: int = ...
    kTimeToUnitConversion: int = ...
    kTimeWarp: int = ...
    kToggleManip: int = ...
    kToggleOnLineManip: int = ...
    kToolContext: int = ...
    kToonLineAttributes: int = ...
    kTorus: int = ...
    kTowPointManip: int = ...
    kTowPointOnCurveManip: int = ...
    kTowPointOnSurfaceManip: int = ...
    kTrackInfoManager: int = ...
    kTransferAttributes: int = ...
    kTransferFalloff: int = ...
    kTransform: int = ...
    kTransformBoxManip: int = ...
    kTransformGeometry: int = ...
    kTranslateBoxManip: int = ...
    kTranslateLimitsManip: int = ...
    kTranslateManip: int = ...
    kTranslateManip2D: int = ...
    kTranslateUVManip: int = ...
    kTranslateUVManip2D: int = ...
    kTriadManip: int = ...
    kTrim: int = ...
    kTrimLocator: int = ...
    kTrimManip: int = ...
    kTrimWithBoundaries: int = ...
    kTriplanarProjectionManip: int = ...
    kTripleIndexedComponent: int = ...
    kTripleShadingSwitch: int = ...
    kTrsInsertManip: int = ...
    kTrsManip: int = ...
    kTrsTransManip: int = ...
    kTrsXformManip: int = ...
    kTurbulence: int = ...
    kTweak: int = ...
    kTwoPointArcManip: int = ...
    kTxSl: int = ...
    kTypedAttribute: int = ...
    kUInt64ArrayData: int = ...
    kUVManip2D: int = ...
    kUVPin: int = ...
    kUfeProxyTransform: int = ...
    kUint64SingleIndexedComponent: int = ...
    kUintArrayData: int = ...
    kUnderWorld: int = ...
    kUniform: int = ...
    kUniformFalloff: int = ...
    kUnitAttribute: int = ...
    kUnitConversion: int = ...
    kUnitToTimeConversion: int = ...
    kUnknown: int = ...
    kUnknownDag: int = ...
    kUnknownTransform: int = ...
    kUntrim: int = ...
    kUnused1: int = ...
    kUnused2: int = ...
    kUnused3: int = ...
    kUnused4: int = ...
    kUnused5: int = ...
    kUnused6: int = ...
    kUseBackground: int = ...
    kUvChooser: int = ...
    kVectorArrayData: int = ...
    kVectorProduct: int = ...
    kVertexBakeSet: int = ...
    kVertexWeightSet: int = ...
    kViewColorManager: int = ...
    kViewManip: int = ...
    kVolumeAxis: int = ...
    kVolumeBindManip: int = ...
    kVolumeFog: int = ...
    kVolumeLight: int = ...
    kVolumeNoise: int = ...
    kVolumeShader: int = ...
    kVortex: int = ...
    kWater: int = ...
    kWeightFunctionData: int = ...
    kWeightGeometryFilt: int = ...
    kWire: int = ...
    kWood: int = ...
    kWorld: int = ...
    kWrapFilter: int = ...
    kWriteToColorBuffer: int = ...
    kWriteToDepthBuffer: int = ...
    kWriteToFrameBuffer: int = ...
    kWriteToLabelBuffer: int = ...
    kWriteToVectorBuffer: int = ...
    kXformManip: int = ...
    kXsectionSubdivEdit: int = ...

class MFnBase:
    def hasObj(self: Self, type: int | MObject) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self: Self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self: Self, object: MObject) -> Self:
        """Attaches the function set to the specified Maya object."""
    def type(self: Self) -> int:
        """Returns the type of the function set."""

class MFnAttribute(MFnBase):
    def accepts(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this attribute can accept a connection of the given type."""
    def acceptsAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this attribute can accept a connection with the given attribute."""
    def addToCategory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds the attribute to a category"""
    @property
    def affectsAppearance(*args: Any, **kwargs: Any) -> Any:
        """Does the attribute affect how the node is drawn in Maya's viewport?"""
    @affectsAppearance.setter
    def affectsAppearance(*args: Any, **kwargs: Any) -> Any:
        """Does the attribute affect how the node is drawn in Maya's viewport?"""
    @property
    def affectsWorldSpace(*args: Any, **kwargs: Any) -> Any:
        """Does the attribute affect the node's worldSpace matrix?"""
    @affectsWorldSpace.setter
    def affectsWorldSpace(*args: Any, **kwargs: Any) -> Any:
        """Does the attribute affect the node's worldSpace matrix?"""
    @property
    def array(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute an array?"""
    @array.setter
    def array(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute an array?"""
    @property
    def cached(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute's value be cached in the datablock?"""
    @cached.setter
    def cached(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute's value be cached in the datablock?"""
    @property
    def channelBox(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute be displayed in the Channel Box?"""
    @channelBox.setter
    def channelBox(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute be displayed in the Channel Box?"""
    @property
    def connectable(*args: Any, **kwargs: Any) -> Any:
        """Can connections be made to the attribute?"""
    @connectable.setter
    def connectable(*args: Any, **kwargs: Any) -> Any:
        """Can connections be made to the attribute?"""
    @property
    def disconnectBehavior(*args: Any, **kwargs: Any) -> Any:
        """What should happen when the attribute loses an incoming connection?"""
    @disconnectBehavior.setter
    def disconnectBehavior(*args: Any, **kwargs: Any) -> Any:
        """What should happen when the attribute loses an incoming connection?"""
    @property
    def dynamic(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute a dynamic attribute?"""
    @dynamic.setter
    def dynamic(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute a dynamic attribute?"""
    @property
    def extension(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute an extension attribute?"""
    @extension.setter
    def extension(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute an extension attribute?"""
    def getAddAttrCmd(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""
    def hasCategory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Checks to see if the attribute has a given category"""
    @property
    def hidden(*args: Any, **kwargs: Any) -> Any:
        """If True the attribute will not be displayed in the Attribute Editor."""
    @hidden.setter
    def hidden(*args: Any, **kwargs: Any) -> Any:
        """If True the attribute will not be displayed in the Attribute Editor."""
    @property
    def indeterminant(*args: Any, **kwargs: Any) -> Any:
        """Hint to DG that this attribute may not always be used when computing the attributes which are dependent upon it."""
    @indeterminant.setter
    def indeterminant(*args: Any, **kwargs: Any) -> Any:
        """Hint to DG that this attribute may not always be used when computing the attributes which are dependent upon it."""
    @property
    def indexMatters(*args: Any, **kwargs: Any) -> Any:
        """If False, connectAttr -nextAvailable can be used with this attribute. If True then an explicit index must be provided."""
    @indexMatters.setter
    def indexMatters(*args: Any, **kwargs: Any) -> Any:
        """If False, connectAttr -nextAvailable can be used with this attribute. If True then an explicit index must be provided."""
    @property
    def internal(*args: Any, **kwargs: Any) -> Any:
        """Will the node handle the attribute's data storage itself, outside of the node's data block?"""
    @internal.setter
    def internal(*args: Any, **kwargs: Any) -> Any:
        """Will the node handle the attribute's data storage itself, outside of the node's data block?"""
    @property
    def isProxyAttribute(*args: Any, **kwargs: Any) -> Any:
        """Does the attribute is a proxy attribute?"""
    @isProxyAttribute.setter
    def isProxyAttribute(*args: Any, **kwargs: Any) -> Any:
        """Does the attribute is a proxy attribute?"""
    kDelete: int = ...
    kNothing: int = ...
    kReset: int = ...

    @property
    def keyable(*args: Any, **kwargs: Any) -> Any:
        """Can keys be set on the attribute?"""
    @keyable.setter
    def keyable(*args: Any, **kwargs: Any) -> Any:
        """Can keys be set on the attribute?"""
    @property
    def name(*args: Any, **kwargs: Any) -> Any:
        """Attribute's long name."""
    @name.setter
    def name(*args: Any, **kwargs: Any) -> Any:
        """Attribute's long name."""
    @property
    def parent(*args: Any, **kwargs: Any) -> Any:
        """Parent attribute. MObject::kNullObj if attr has no parent."""
    @parent.setter
    def parent(*args: Any, **kwargs: Any) -> Any:
        """Parent attribute. MObject::kNullObj if attr has no parent."""
    @property
    def readable(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute readable?"""
    @readable.setter
    def readable(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute readable?"""
    @property
    def renderSource(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute a render source?"""
    @renderSource.setter
    def renderSource(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute a render source?"""
    def setNiceNameOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""
    @property
    def shortName(*args: Any, **kwargs: Any) -> Any:
        """Attribute's short name."""
    @shortName.setter
    def shortName(*args: Any, **kwargs: Any) -> Any:
        """Attribute's short name."""
    @property
    def storable(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute's value be preserved when the node is written to file?"""
    @storable.setter
    def storable(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute's value be preserved when the node is written to file?"""
    @property
    def usedAsColor(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute be treated as a color in the UI?"""
    @usedAsColor.setter
    def usedAsColor(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute be treated as a color in the UI?"""
    @property
    def usedAsFilename(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute be treated as a file name in the UI?"""
    @usedAsFilename.setter
    def usedAsFilename(*args: Any, **kwargs: Any) -> Any:
        """Should the attribute be treated as a file name in the UI?"""
    @property
    def usesArrayDataBuilder(*args: Any, **kwargs: Any) -> Any:
        """Array attributes only: does the attribute create elements using MArrayDataBuilder?"""
    @usesArrayDataBuilder.setter
    def usesArrayDataBuilder(*args: Any, **kwargs: Any) -> Any:
        """Array attributes only: does the attribute create elements using MArrayDataBuilder?"""
    @property
    def worldSpace(*args: Any, **kwargs: Any) -> Any:
        """DAG nodes only: if the node is instanced, will the attribute have separate values for each instance?"""
    @worldSpace.setter
    def worldSpace(*args: Any, **kwargs: Any) -> Any:
        """DAG nodes only: if the node is instanced, will the attribute have separate values for each instance?"""
    @property
    def writable(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute writable?"""
    @writable.setter
    def writable(*args: Any, **kwargs: Any) -> Any:
        """Is the attribute writable?"""

class MFnDependencyNode(MFnBase):
    def absoluteName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""
    def addAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds a new dynamic attribute to the node."""
    def addExternalContentForFileAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds content info to the specified table from a file path attribute."""
    def affectsAnimation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the changes to the node may affect animation."""
    def allocateFlag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""
    def attribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an attribute of the node, given either its index or name."""
    def attributeClass(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the class of the specified attribute."""
    def attributeCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of attributes on the node."""
    def canBeWritten(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the node will be written to file."""
    def classification(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the classification string for the named node type."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new node of the given type."""
    def deallocateAllFlags(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deallocates all node flags which are currently allocated to the named plugin."""
    def deallocateFlag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""
    def dgCallbackIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""
    def dgCallbacks(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns DG timing information broken down by callback type."""
    def dgTimer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a specific DG timer metric for a given timer type."""
    def dgTimerOff(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Turns DG timing off for this node."""
    def dgTimerOn(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Turns DG timing on for this node."""
    def dgTimerQueryState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the current DG timer state for this node."""
    def dgTimerReset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Resets all DG timers for this node."""
    def findAlias(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute which has the given alias."""
    def findPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the given attribute."""
    def getAffectedAttributes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which are affected by the specified attribute."""
    def getAffectingAttributes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""
    def getAliasAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""
    def getAliasList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the node's attribute aliases."""
    def getConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns all the plugs which are connected to attributes of this node."""
    def getExternalContent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Gets the external content (files) that this node depends on."""
    def hasAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node has an attribute with the given name."""
    def hasUniqueName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node's name is unique."""
    @property
    def isDefaultNode(*args: Any, **kwargs: Any) -> Any:
        """True if this is a default node, created automatically by Maya."""
    @isDefaultNode.setter
    def isDefaultNode(*args: Any, **kwargs: Any) -> Any:
        """True if this is a default node, created automatically by Maya."""
    def isFlagSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the state of the specified node flag."""
    @property
    def isFromReferencedFile(*args: Any, **kwargs: Any) -> Any:
        """True if the node is from a referenced file, False if the node is part of the main scene."""
    @isFromReferencedFile.setter
    def isFromReferencedFile(*args: Any, **kwargs: Any) -> Any:
        """True if the node is from a referenced file, False if the node is part of the main scene."""
    @property
    def isLocked(*args: Any, **kwargs: Any) -> Any:
        """True if the node is locked against changes."""
    @isLocked.setter
    def isLocked(*args: Any, **kwargs: Any) -> Any:
        """True if the node is locked against changes."""
    def isNewAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""
    @property
    def isShared(*args: Any, **kwargs: Any) -> Any:
        """True if the node is shared."""
    @isShared.setter
    def isShared(*args: Any, **kwargs: Any) -> Any:
        """True if the node is shared."""
    def isTrackingEdits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""
    kExtensionAttr: int = ...
    kInvalidAttr: int = ...
    kLocalDynamicAttr: int = ...
    kNormalAttr: int = ...
    kTimerInvalidState: int = ...
    kTimerMetric_callback: int = ...
    kTimerMetric_callbackNotViaAPI: int = ...
    kTimerMetric_callbackViaAPI: int = ...
    kTimerMetric_compute: int = ...
    kTimerMetric_computeDuringCallback: int = ...
    kTimerMetric_computeNotDuringCallback: int = ...
    kTimerMetric_dirty: int = ...
    kTimerMetric_draw: int = ...
    kTimerMetric_fetch: int = ...
    kTimerMetrics: int = ...
    kTimerOff: int = ...
    kTimerOn: int = ...
    kTimerType_count: int = ...
    kTimerType_inclusive: int = ...
    kTimerType_self: int = ...
    kTimerTypes: int = ...
    kTimerUninitialized: int = ...

    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's name."""
    @property
    def namespace(*args: Any, **kwargs: Any) -> Any:
        """Name of the namespace which contains the node."""
    @namespace.setter
    def namespace(*args: Any, **kwargs: Any) -> Any:
        """Name of the namespace which contains the node."""
    @property
    def pluginName(*args: Any, **kwargs: Any) -> Any:
        """Name of the plugin which registered the node type, if any."""
    @pluginName.setter
    def pluginName(*args: Any, **kwargs: Any) -> Any:
        """Name of the plugin which registered the node type, if any."""
    def plugsAlias(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the alias for a plug's attribute."""
    def removeAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes a dynamic attribute from the node."""
    def reorderedAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the node's attribute, based on the order in which they are written to file."""
    def setAffectsAnimation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Specifies that modifications to a node could potentially affect the animation."""
    def setAlias(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds or removes an attribute alias."""
    def setDoNotWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Used to prevent the node from being written to file."""
    def setExternalContent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Changes the location of external content."""
    def setExternalContentForFileAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets content info in the specified attribute from the table."""
    def setFlag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the state of the specified node flag."""
    def setName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's name."""
    def setUuid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's UUID."""
    @property
    def typeId(*args: Any, **kwargs: Any) -> Any:
        """MTypeId for the node's type."""
    @typeId.setter
    def typeId(*args: Any, **kwargs: Any) -> Any:
        """MTypeId for the node's type."""
    @property
    def typeName(*args: Any, **kwargs: Any) -> Any:
        """Name of the node's type."""
    @typeName.setter
    def typeName(*args: Any, **kwargs: Any) -> Any:
        """Name of the node's type."""
    def uniqueName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""
    def userNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MPxNode object for a plugin node."""
    def uuid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's UUID."""

class MFnDagNode(MFnDependencyNode):
    def addChild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addChild(node, index=kNextPos, keepExistingParents=False) -> self

        Makes a node a child of this one.
        """
    @property
    def boundingBox(*args: Any, **kwargs: Any) -> Any:
        """Node's bounding box, in object space."""
    @boundingBox.setter
    def boundingBox(*args: Any, **kwargs: Any) -> Any:
        """Node's bounding box, in object space."""
    def child(self: Self, *args: Any, **kwargs: Any) -> Any:
        """child(index) -> MObject

        Returns the specified child of this node.
        """
    def childCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """childCount() -> int

        Returns the number of nodes which are children of this one.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(type, name=None, parent=MObject.kNullObj) -> MObject

        Creates a new DAG node of the specified type, with the given name.
        The type may be either a type name or a type ID. If no name is given
        then a unique name will be generated by combining the type name with
        an integer.

        If a parent is given then the new node will be parented under it and
        the functionset will be attached to the newly-created node. The
        newly-created node will be returned.

        If no parent is given and the new node is a transform, it will be
        parented under the world and the functionset will be attached to the
        newly-created transform. The newly-created transform will be returned.

        If no parent is given and the new node is not a transform then a
        transform node will be created under the world, the new node will be
        parented under it, and the functionset will be attached to the
        transform. The transform will be returned.
        """
    def dagPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dagPath() -> MDagPath

        Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path.
        """
    def dagRoot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dagRoot() -> MObject

        Returns the root node of the first path leading to this node.
        """
    def duplicate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """duplicate(instance=False, instanceLeaf=False) -> MObject

        Duplicates the DAG hierarchy rooted at the current node.
        """
    def fullPathName(self: Self) -> str:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def getAllPaths(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAllPaths() -> MDagPathArray

        Returns all of the DAG paths which lead to the object to which this function set is attached.
        """
    def getConnectedSetsAndMembers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedSetsAndMembers(instance, renderableSetsOnly) -> (MObjectArray, MObjectArray)

        Returns a tuple containing an array of sets and an array of the
        components of the DAG object which are in those sets. If the entire object is in a set, then the corresponding entry in the comps array will have no elements in it.
        """
    def getPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPath() -> MDagPath

        Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject.
        """
    def hasChild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasChild(node) -> bool

        Returns True if the specified node is a child of this one.
        """
    def hasParent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasParent(node) -> bool

        Returns True if the specified node is a parent of this one.
        """
    @property
    def inModel(*args: Any, **kwargs: Any) -> Any:
        """True if the node has been added to the model."""
    @inModel.setter
    def inModel(*args: Any, **kwargs: Any) -> Any:
        """True if the node has been added to the model."""
    @property
    def inUnderWorld(*args: Any, **kwargs: Any) -> Any:
        """True if this node is in the underworld of another node (e.g. a curve on surface is in the underworld of the surface)."""
    @inUnderWorld.setter
    def inUnderWorld(*args: Any, **kwargs: Any) -> Any:
        """True if this node is in the underworld of another node (e.g. a curve on surface is in the underworld of the surface)."""
    def instanceCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """instanceCount(indirect) -> int

        Returns the number of instances for this node.
        """
    def isChildOf(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isChildOf(node) -> bool

        Returns True if the specified node is a parent of this one.
        """
    @property
    def isInstanceable(*args: Any, **kwargs: Any) -> Any:
        """True if instancing is allowed for this node."""
    @isInstanceable.setter
    def isInstanceable(*args: Any, **kwargs: Any) -> Any:
        """True if instancing is allowed for this node."""
    def isInstanced(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isInstanced(indirect=True) -> bool

        Returns True if this node is instanced.
        """
    def isInstancedAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isInstancedAttribute(attr) -> bool

        Returns True if the specified attribute is an instanced attribute of this node.
        """
    @property
    def isIntermediateObject(*args: Any, **kwargs: Any) -> Any:
        """True if this node is just an intermediate in part of a larger calculation (e.g. input to a deformer)."""
    @isIntermediateObject.setter
    def isIntermediateObject(*args: Any, **kwargs: Any) -> Any:
        """True if this node is just an intermediate in part of a larger calculation (e.g. input to a deformer)."""
    def isParentOf(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isParentOf(node) -> bool

        Returns True if the specified node is a child of this one.
        """
    kNextPos: int = ...

    @property
    def objectColor(*args: Any, **kwargs: Any) -> Any:
        """Index from 0 to 7 indicating the color in which the node is to be drawn when inactive, assuming that it is drawable."""
    @objectColor.setter
    def objectColor(*args: Any, **kwargs: Any) -> Any:
        """Index from 0 to 7 indicating the color in which the node is to be drawn when inactive, assuming that it is drawable."""
    @property
    def objectColorRGB(*args: Any, **kwargs: Any) -> Any:
        """RGB value indicating the color in which the node is to be drawn when inactive, assuming that it is drawable."""
    @objectColorRGB.setter
    def objectColorRGB(*args: Any, **kwargs: Any) -> Any:
        """RGB value indicating the color in which the node is to be drawn when inactive, assuming that it is drawable."""
    @property
    def objectColorType(*args: Any, **kwargs: Any) -> Any:
        """Determines whether the default color, indexed object color, orRGB object color is used for this object."""
    @objectColorType.setter
    def objectColorType(*args: Any, **kwargs: Any) -> Any:
        """Determines whether the default color, indexed object color, orRGB object color is used for this object."""
    def parent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parent(index) -> MObject

        Returns the specified parent of this node.
        """
    def parentCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parentCount() -> int

        Returns the number of parents this node has.
        """
    def partialPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """partialPathName() -> string

        Returns the minimum path string necessary to uniquely identify the attached object.
        """
    def removeChild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeChild(node) -> self

        Removes the child, specified by MObject, reparenting it under the world.
        """
    def removeChildAt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeChildAt(index) -> self

        Removes the child, specified by index, reparenting it under the world.
        """
    def setObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setObject(MObject or MDagPath) -> self

        Attaches the function set to the specified node or DAG path.
        """
    def transformationMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """transformationMatrix() -> MMatrix

        Returns the object space transformation matrix for this DAG node.
        """
    @property
    def useObjectColor(*args: Any, **kwargs: Any) -> Any:
        """If True then the node will be drawn using its 'objectColor', otherwise it will be drawn using Maya's default color. Thismethod is deprecated, use objectColorType instead."""
    @useObjectColor.setter
    def useObjectColor(*args: Any, **kwargs: Any) -> Any:
        """If True then the node will be drawn using its 'objectColor', otherwise it will be drawn using Maya's default color. Thismethod is deprecated, use objectColorType instead."""

class MFnCamera(MFnDagNode):
    def aspectRatio(self: Self, *args: Any, **kwargs: Any) -> Any:
        """aspectRatio() -> float

        Returns the aspect ratio for the camera.
        """
    @property
    def cameraScale(*args: Any, **kwargs: Any) -> Any:
        """The camera scale."""
    @cameraScale.setter
    def cameraScale(*args: Any, **kwargs: Any) -> Any:
        """The camera scale."""
    @property
    def centerOfInterest(*args: Any, **kwargs: Any) -> Any:
        """The linear distance from the camera's eye point to the center of interest."""
    @centerOfInterest.setter
    def centerOfInterest(*args: Any, **kwargs: Any) -> Any:
        """The linear distance from the camera's eye point to the center of interest."""
    def centerOfInterestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """centerOfInterestPoint(space=kObject) -> MPoint

        Returns the center of interest point for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
    def computeDepthOfField(self: Self, *args: Any, **kwargs: Any) -> Any:
        """computeDepthOfField(nearLimit=None) -> self

        Compute the depth of field

        * nearLimit (float) - the near limit
        """
    def copyViewFrom(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyViewFrom(otherCamera) -> self

        Copy the camera settings related to the perspective from the given camera view.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * otherCamera (MDagPath) - Camera to copy view from
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(parent=None) -> MObject

        Creates a perspective camera. A parent can be specified for the new camera, otherwise a transform is created.

        The camera is positioned at (0, 0, 0), its center of interest at (0, 0, -1), which implies that the view-direction is pointing in the direction of the negative z-axis, and its up-direction along the positive Y axis.

        * parent (MObject) - The parent of the new camera
        """
    def eyePoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """eyePoint(space=kObject) -> MPoint

        Returns the eye point for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
    @property
    def fStop(*args: Any, **kwargs: Any) -> Any:
        """The f-stop value for the camera."""
    @fStop.setter
    def fStop(*args: Any, **kwargs: Any) -> Any:
        """The f-stop value for the camera."""
    @property
    def farClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """The distance to the far clipping plane."""
    @farClippingPlane.setter
    def farClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """The distance to the far clipping plane."""
    @property
    def farFocusDistance(*args: Any, **kwargs: Any) -> Any:
        """The farthest distance within the well-focus region"""
    @farFocusDistance.setter
    def farFocusDistance(*args: Any, **kwargs: Any) -> Any:
        """The farthest distance within the well-focus region"""
    @property
    def filmFit(*args: Any, **kwargs: Any) -> Any:
        """How the digital image is to be fitted to the film back.
        Valid values:
        * kFillFilmFit           The system calculates both horizontal and vertical fits and then applies the one that makes the digital image larger than the film back.
        * kHorizontalFilmFit     The digital image is made to fit the film back exactly in the horizontal direction. This then gives each pixel a horizontal size = (film back width) / (horizontal resolution). The pixel height is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size, resolution gives us a complete image. That image will match the film back exactly in width. It will almost never match in height, either being too tall or too short. By playing with the numbers you can get it pretty close though.
        * kVerticalFilmFit       The same idea as horizontal fit, only applied vertically. Thus the digital image will match the film back exactly in height, but miss in width.
        * kOverscanFilmFit       Over-scanning the film gate in the camera view allows us to choreograph action outside of the frustum from within the camera view without having to resort to a dolly or zoom. This feature is also essential for animating image planes.
        """
    @filmFit.setter
    def filmFit(*args: Any, **kwargs: Any) -> Any:
        """How the digital image is to be fitted to the film back.
        Valid values:
        * kFillFilmFit           The system calculates both horizontal and vertical fits and then applies the one that makes the digital image larger than the film back.
        * kHorizontalFilmFit     The digital image is made to fit the film back exactly in the horizontal direction. This then gives each pixel a horizontal size = (film back width) / (horizontal resolution). The pixel height is then = (pixel width) / (pixel aspect ratio). Now that the pixel has a size, resolution gives us a complete image. That image will match the film back exactly in width. It will almost never match in height, either being too tall or too short. By playing with the numbers you can get it pretty close though.
        * kVerticalFilmFit       The same idea as horizontal fit, only applied vertically. Thus the digital image will match the film back exactly in height, but miss in width.
        * kOverscanFilmFit       Over-scanning the film gate in the camera view allows us to choreograph action outside of the frustum from within the camera view without having to resort to a dolly or zoom. This feature is also essential for animating image planes.
        """
    @property
    def filmFitOffset(*args: Any, **kwargs: Any) -> Any:
        """The film fit offset for the camera."""
    @filmFitOffset.setter
    def filmFitOffset(*args: Any, **kwargs: Any) -> Any:
        """The film fit offset for the camera."""
    @property
    def filmRollOrder(*args: Any, **kwargs: Any) -> Any:
        """The order in which the film back rotation is applied with respect to the pivot point.
        Valid values:
        * kRotateTranslate      The film back is first rotated before it is translated by the pivot value.
        * kTranslateRotate      The film back is translated by the pivot before it is rotated.
        """
    @filmRollOrder.setter
    def filmRollOrder(*args: Any, **kwargs: Any) -> Any:
        """The order in which the film back rotation is applied with respect to the pivot point.
        Valid values:
        * kRotateTranslate      The film back is first rotated before it is translated by the pivot value.
        * kTranslateRotate      The film back is translated by the pivot before it is rotated.
        """
    @property
    def filmRollValue(*args: Any, **kwargs: Any) -> Any:
        """The film roll value for film back."""
    @filmRollValue.setter
    def filmRollValue(*args: Any, **kwargs: Any) -> Any:
        """The film roll value for film back."""
    @property
    def filmTranslateH(*args: Any, **kwargs: Any) -> Any:
        """The horizontal film translate value.  This value corresponds to the normalized viewport."""
    @filmTranslateH.setter
    def filmTranslateH(*args: Any, **kwargs: Any) -> Any:
        """The horizontal film translate value.  This value corresponds to the normalized viewport."""
    @property
    def filmTranslateV(*args: Any, **kwargs: Any) -> Any:
        """The vertical film translate value. This value corresponds to the normalized viewport, [-1,1]."""
    @filmTranslateV.setter
    def filmTranslateV(*args: Any, **kwargs: Any) -> Any:
        """The vertical film translate value. This value corresponds to the normalized viewport, [-1,1]."""
    @property
    def focalLength(*args: Any, **kwargs: Any) -> Any:
        """The focal length for the camera.
        This is the distance along the lens axis between the lens and the film plane when "focal distance" is infinitely large. This is an optical property of the lens. Specified in millimeters.
        """
    @focalLength.setter
    def focalLength(*args: Any, **kwargs: Any) -> Any:
        """The focal length for the camera.
        This is the distance along the lens axis between the lens and the film plane when "focal distance" is infinitely large. This is an optical property of the lens. Specified in millimeters.
        """
    @property
    def focusDistance(*args: Any, **kwargs: Any) -> Any:
        """The focus distance for the camera. This value sets the focus at a certain distance in front of the camera."""
    @focusDistance.setter
    def focusDistance(*args: Any, **kwargs: Any) -> Any:
        """The focus distance for the camera. This value sets the focus at a certain distance in front of the camera."""
    def getAspectRatioLimits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAspectRatioLimits() -> (float, float)

        Returns the minimum and maximum aspect ratio limits for the camera.
        """
    def getFilmApertureLimits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFilmApertureLimits() -> (float, float)

        Returns the maximum and minimum film aperture limits for the camera.
        """
    def getFilmFrustum(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFilmFrustum(distance, applyPanZoom=False) -> (float, float, float, float)

        Returns the film frustum for the camera (horizontal size, vertical size, horizontal offset and vertical offset). The frustum defines the projective transformation.

        * distance (float) - Specifies the focal length
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
    def getFilmFrustumCorners(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFilmFrustumCorners(distance, applyPanZoom=False) -> MPointArray

        Returns the film frustum for the camera. The frustum defines the projective transformation.

         element 0 is the bottom left
         element 1 is the top left
         element 2 is the top right
         element 3 is the bottom right

        * distance (float) - Specifies the focal length
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
    def getFocalLengthLimits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFocalLengthLimits() -> (float, float)

        Returns the maximum and minimum focal length limits for the camera.
        """
    def getPortFieldOfView(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPortFieldOfView(int, int) -> (float, float)

        Returns the horizontal and vertical field of view in radians from the given viewport width and height.

        * width (int) - width of viewport
        * height (int) - height of viewport
        """
    def getRenderingFrustum(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRenderingFrustum(windowAspect) -> (float, float, float, float)

        Returns the rendering frustum (left, right, bottom and top) for the camera.
        This is the frustum that the maya renderer uses.

        * windowAspect (float) - windowAspect
        """
    def getViewParameters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getViewParameters(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

        Returns the intermediate viewing frustum (apertureX, apertureY, offsetX and offsetY) parameters for the camera. The aperture and offset are used by getViewingFrustum() and getRenderingFrustum() to compute the extent (left, right, top, bottom) of the frustum in the following manner:

         left = focal_to_near * (-0.5*apertureX + offsetX)
         right = focal_to_near * (0.5*apertureX + offsetX)
         bottom = focal_to_near * (-0.5*apertureY + offsetY)
         top = focal_to_near * (0.5*apertureY + offsetY)

        Here, focal_to_near is equal to cameraScale if the camera is orthographic, or it is equal to ((nearClippingPlane / (focalLength * MM_TO_INCH)) * cameraScale) where MM_TO_INCH equals 0.03937.

        * windowAspect (float) - windowAspect
        * applyOverscan (bool) - specifies whether to apply overscan
        * applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
    def getViewingFrustum(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getViewingFrustum(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

        Returns the viewing frustum (left, right, bottom and top) for the camera.

        * windowAspect (float) - windowAspect
        * applyOverscan (bool) - specifies whether to apply overscan
        * applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """
    def hasSamePerspective(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasSamePerspective(otherCamera) -> bool

        Returns True if the camera has same perspective settings as the given camera.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * otherCamera (MDagPath) - Camera to compare perspective with
        """
    def horizontalFieldOfView(self: Self, *args: Any, **kwargs: Any) -> Any:
        """horizontalFieldOfView() -> float

        Returns the horizontal field of view for the camera.
        """
    @property
    def horizontalFilmAperture(*args: Any, **kwargs: Any) -> Any:
        """The horizontal film aperture for the camera."""
    @horizontalFilmAperture.setter
    def horizontalFilmAperture(*args: Any, **kwargs: Any) -> Any:
        """The horizontal film aperture for the camera."""
    @property
    def horizontalFilmOffset(*args: Any, **kwargs: Any) -> Any:
        """The horizontal offset of the film. Unit used is inches."""
    @horizontalFilmOffset.setter
    def horizontalFilmOffset(*args: Any, **kwargs: Any) -> Any:
        """The horizontal offset of the film. Unit used is inches."""
    @property
    def horizontalPan(*args: Any, **kwargs: Any) -> Any:
        """The camera 2D horizontal pan value. Unit is inches."""
    @horizontalPan.setter
    def horizontalPan(*args: Any, **kwargs: Any) -> Any:
        """The camera 2D horizontal pan value. Unit is inches."""
    @property
    def horizontalRollPivot(*args: Any, **kwargs: Any) -> Any:
        """The horizontal roll pivot for film back roll."""
    @horizontalRollPivot.setter
    def horizontalRollPivot(*args: Any, **kwargs: Any) -> Any:
        """The horizontal roll pivot for film back roll."""
    @property
    def horizontalShake(*args: Any, **kwargs: Any) -> Any:
        """The horizontal offset of the film due to the shake attribute. Unit used is inches."""
    @horizontalShake.setter
    def horizontalShake(*args: Any, **kwargs: Any) -> Any:
        """The horizontal offset of the film due to the shake attribute. Unit used is inches."""
    @property
    def isClippingPlanes(*args: Any, **kwargs: Any) -> Any:
        """Whether or not manual clipping planes are activated."""
    @isClippingPlanes.setter
    def isClippingPlanes(*args: Any, **kwargs: Any) -> Any:
        """Whether or not manual clipping planes are activated."""
    @property
    def isDepthOfField(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the depth of field calculation is performed for the camera."""
    @isDepthOfField.setter
    def isDepthOfField(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the depth of field calculation is performed for the camera."""
    @property
    def isDisplayFilmGate(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the film gate icons are displayed when looking through the camera."""
    @isDisplayFilmGate.setter
    def isDisplayFilmGate(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the film gate icons are displayed when looking through the camera."""
    @property
    def isDisplayGateMask(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the film gate is displayed shaded."""
    @isDisplayGateMask.setter
    def isDisplayGateMask(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the film gate is displayed shaded."""
    @property
    def isMotionBlur(*args: Any, **kwargs: Any) -> Any:
        """Wheter or not motion blur is on/off for the camera."""
    @isMotionBlur.setter
    def isMotionBlur(*args: Any, **kwargs: Any) -> Any:
        """Wheter or not motion blur is on/off for the camera."""
    def isOrtho(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isOrtho() -> bool

        Returns True if the camera is in orthographic mode.
        """
    @property
    def isVerticalLock(*args: Any, **kwargs: Any) -> Any:
        """Determines if vertical lock is turned on for the camera."""
    @isVerticalLock.setter
    def isVerticalLock(*args: Any, **kwargs: Any) -> Any:
        """Determines if vertical lock is turned on for the camera."""
    @property
    def lensSqueezeRatio(*args: Any, **kwargs: Any) -> Any:
        """The lens squeeze ratio for the camera"""
    @lensSqueezeRatio.setter
    def lensSqueezeRatio(*args: Any, **kwargs: Any) -> Any:
        """The lens squeeze ratio for the camera"""
    @property
    def nearClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """The distance to the near clipping plane."""
    @nearClippingPlane.setter
    def nearClippingPlane(*args: Any, **kwargs: Any) -> Any:
        """The distance to the near clipping plane."""
    @property
    def nearFocusDistance(*args: Any, **kwargs: Any) -> Any:
        """The nearest distance within the well-focus region"""
    @nearFocusDistance.setter
    def nearFocusDistance(*args: Any, **kwargs: Any) -> Any:
        """The nearest distance within the well-focus region"""
    @property
    def orthoWidth(*args: Any, **kwargs: Any) -> Any:
        """The orthographic projection width."""
    @orthoWidth.setter
    def orthoWidth(*args: Any, **kwargs: Any) -> Any:
        """The orthographic projection width."""
    @property
    def overscan(*args: Any, **kwargs: Any) -> Any:
        """The percent of overscan for this camera."""
    @overscan.setter
    def overscan(*args: Any, **kwargs: Any) -> Any:
        """The percent of overscan for this camera."""
    @property
    def panZoomEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera 2D pan/zoom enabled attribute.
        If this attribute is False, the 2D pan/zoom values are ignored by the camera.
        """
    @panZoomEnabled.setter
    def panZoomEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera 2D pan/zoom enabled attribute.
        If this attribute is False, the 2D pan/zoom values are ignored by the camera.
        """
    def postProjectionMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postProjectionMatrix(context=None) -> MFloatMatrix

        Returns the post projection matrix used to compute film roll on the film back plane.

        * context (MDGContext) - DG time-context to specify time of evaluation
        """
    @property
    def postScale(*args: Any, **kwargs: Any) -> Any:
        """The post projection matrix's post-scale value."""
    @postScale.setter
    def postScale(*args: Any, **kwargs: Any) -> Any:
        """The post projection matrix's post-scale value."""
    @property
    def preScale(*args: Any, **kwargs: Any) -> Any:
        """The post projection matrix's pre-scale value."""
    @preScale.setter
    def preScale(*args: Any, **kwargs: Any) -> Any:
        """The post projection matrix's pre-scale value."""
    def projectionMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """projectionMatrix(context=None) -> MFloatMatrix

        Returns the orthographic or perspective projection matrix for the camera.
        The projection matrix that maya's software renderer uses is almost identical to the OpenGL projection matrix. The difference is that maya uses a left hand coordinate system and so the entries [2][2] and [3][2] are negated.

        * context (MDGContext) - DG time-context to specify time of evaluation
        """
    @property
    def renderPanZoom(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera render 2D pan/zoom attribute.
        If this attribute is False, the 2D pan/zoom values will not affect the output render.
        """
    @renderPanZoom.setter
    def renderPanZoom(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera render 2D pan/zoom attribute.
        If this attribute is False, the 2D pan/zoom values will not affect the output render.
        """
    def rightDirection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rightDirection(space=kObject) -> MVector

        Returns the right direction vector for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """set(wsEyeLocation, wsViewDirection, wsUpDirection, horizFieldOfView, aspectRatio) -> self

        Convenience routine to set the camera viewing parameters. The specified values should be in world space where applicable.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * wsEyeLocation (MPoint) - Eye location to set in world space
        * wsViewDirection (MVector) - View direction to set in world space
        * wsUpDirection (MVector) - Up direction to set in world space
        * horizFieldOfView (float) - The horizontal field of view to set
        * aspectRatio (float) - The aspect ratio to set
        """
    def setAspectRatio(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAspectRatio(aspectRatio) -> self

        Set the aspect ratio of the View.  The aspect ratio is expressed as width/height.  This also modifies the entity's scale transformation to reflect the new aspect ratio.

        * aspectRatio (float) - The aspect ratio to be set
        """
    def setCenterOfInterestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCenterOfInterestPoint(centerOfInterest, space=kObject) -> self

        Positions the center-of-interest of the camera keeping the eye-point fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * centerOfInterest (MPoint) - Center of interest point to be set
        * space (int) - Specifies the coordinate system for this operation
        """
    def setEyePoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setEyePoint(eyeLocation, space=kObject) -> self

        Positions the eye-point of the camera keeping the center of interest fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * eyeLocation (MPoint) - The eye location to set
        * space (int) - Specifies the coordinate system for this operation
        """
    def setHorizontalFieldOfView(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHorizontalFieldOfView(fov) -> self

        Sets the horizontal field of view for the camera.

        * fov (float) - The horizontal field of view value to be set
        """
    def setIsOrtho(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIsOrtho(orthoState, useDist=None) -> self

        Switch the camera in and out of orthographic mode.  When the switch happens, the camera has to calculate a new fov or ortho width, each of which is based on the other and a set distance.  The caller can specify the distance; otherwise the center of interest is used.

        * orthoState (bool) - If True then the camera will be orthographic
        * useDist (float) - distance to use.
        """
    def setNearFarClippingPlanes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setNearFarClippingPlanes(near, far) -> self

        Set the distances to the Near and Far Clipping Planes.

        * near (float) - The near clipping plane value to be set
        * far (float) - The far clipping plane value to be set
        """
    def setVerticalFieldOfView(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setVerticalFieldOfView(fov) -> self

        Sets the vertical field of view for the camera.

        * fov (float) - The vertical field of view value to be set
        """
    @property
    def shakeEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera shake enabled attribute.
        If this attribute is False, the horizontalShake and verticalShake values are ignored by the camera.
        """
    @shakeEnabled.setter
    def shakeEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera shake enabled attribute.
        If this attribute is False, the horizontalShake and verticalShake values are ignored by the camera.
        """
    @property
    def shakeOverscan(*args: Any, **kwargs: Any) -> Any:
        """The camera shake overscan value. Unit is a multiplier to the film aperture."""
    @shakeOverscan.setter
    def shakeOverscan(*args: Any, **kwargs: Any) -> Any:
        """The camera shake overscan value. Unit is a multiplier to the film aperture."""
    @property
    def shakeOverscanEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera shake overscan attribute.
        If this attribute is False, the shakeOverscan value is ignored by the camera.
        """
    @shakeOverscanEnabled.setter
    def shakeOverscanEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the camera shake overscan attribute.
        If this attribute is False, the shakeOverscan value is ignored by the camera.
        """
    @property
    def shutterAngle(*args: Any, **kwargs: Any) -> Any:
        """The shutter angle which is one of the variables used to compute motion blur. The shutter angle is specified in radians."""
    @shutterAngle.setter
    def shutterAngle(*args: Any, **kwargs: Any) -> Any:
        """The shutter angle which is one of the variables used to compute motion blur. The shutter angle is specified in radians."""
    @property
    def stereoHIT(*args: Any, **kwargs: Any) -> Any:
        """The camera stereo horizontal image translation (stereo HIT) value.  Unit is inches."""
    @stereoHIT.setter
    def stereoHIT(*args: Any, **kwargs: Any) -> Any:
        """The camera stereo horizontal image translation (stereo HIT) value.  Unit is inches."""
    @property
    def stereoHITEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the stereo HIT enabled attribute.
        If this attribute is False, the stereoHIT value is ignored by the camera.
        """
    @stereoHITEnabled.setter
    def stereoHITEnabled(*args: Any, **kwargs: Any) -> Any:
        """The toggle value for the stereo HIT enabled attribute.
        If this attribute is False, the stereoHIT value is ignored by the camera.
        """
    @property
    def tumblePivot(*args: Any, **kwargs: Any) -> Any:
        """The tumble pivot value for the camera. The pivot value will be in world space coordinates unless usePivotAsLocalSpace is True in which case the pivot is a relative offset."""
    @tumblePivot.setter
    def tumblePivot(*args: Any, **kwargs: Any) -> Any:
        """The tumble pivot value for the camera. The pivot value will be in world space coordinates unless usePivotAsLocalSpace is True in which case the pivot is a relative offset."""
    def upDirection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """upDirection(space=kObject) -> MVector

        Returns the up direction vector for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """
    @property
    def usePivotAsLocalSpace(*args: Any, **kwargs: Any) -> Any:
        """The local axis tumble setting for this camera.True if using local space tumbling for this camera, or False if using the current global tumble setting in Maya."""
    @usePivotAsLocalSpace.setter
    def usePivotAsLocalSpace(*args: Any, **kwargs: Any) -> Any:
        """The local axis tumble setting for this camera.True if using local space tumbling for this camera, or False if using the current global tumble setting in Maya."""
    def verticalFieldOfView(self: Self, *args: Any, **kwargs: Any) -> Any:
        """verticalFieldOfView() -> float

        Returns the vertical field of view for the camera.
        """
    @property
    def verticalFilmAperture(*args: Any, **kwargs: Any) -> Any:
        """The vertical film aperture for the camera."""
    @verticalFilmAperture.setter
    def verticalFilmAperture(*args: Any, **kwargs: Any) -> Any:
        """The vertical film aperture for the camera."""
    @property
    def verticalFilmOffset(*args: Any, **kwargs: Any) -> Any:
        """The vertical offset of the film. Unit used is inches."""
    @verticalFilmOffset.setter
    def verticalFilmOffset(*args: Any, **kwargs: Any) -> Any:
        """The vertical offset of the film. Unit used is inches."""
    @property
    def verticalPan(*args: Any, **kwargs: Any) -> Any:
        """The camera 2D vertical pan value. Unit is inches."""
    @verticalPan.setter
    def verticalPan(*args: Any, **kwargs: Any) -> Any:
        """The camera 2D vertical pan value. Unit is inches."""
    @property
    def verticalRollPivot(*args: Any, **kwargs: Any) -> Any:
        """The vertical roll pivot for film back roll."""
    @verticalRollPivot.setter
    def verticalRollPivot(*args: Any, **kwargs: Any) -> Any:
        """The vertical roll pivot for film back roll."""
    @property
    def verticalShake(*args: Any, **kwargs: Any) -> Any:
        """The vertical film-based camera shake value. Unit used is inches."""
    @verticalShake.setter
    def verticalShake(*args: Any, **kwargs: Any) -> Any:
        """The vertical film-based camera shake value. Unit used is inches."""
    def viewDirection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewDirection(space=kObject) -> MVector

        Returns the view direction for the camera

        * space (int) - Specifies the coordinate system for this operation
        """
    @property
    def zoom(*args: Any, **kwargs: Any) -> Any:
        """The camera 2D zoom value, which is the percent over the film viewable frustum to display"""
    @zoom.setter
    def zoom(*args: Any, **kwargs: Any) -> Any:
        """The camera 2D zoom value, which is the percent over the film viewable frustum to display"""

class MFnComponent(MFnBase):
    @property
    def componentType(*args: Any, **kwargs: Any) -> Any:
        """Type of the component. (MFn Type constant)"""
    @componentType.setter
    def componentType(*args: Any, **kwargs: Any) -> Any:
        """Type of the component. (MFn Type constant)"""
    @property
    def elementCount(*args: Any, **kwargs: Any) -> Any:
        """Number of elements in the component."""
    @elementCount.setter
    def elementCount(*args: Any, **kwargs: Any) -> Any:
        """Number of elements in the component."""
    @property
    def hasWeights(*args: Any, **kwargs: Any) -> Any:
        """True if the component has weights associated with its elements."""
    @hasWeights.setter
    def hasWeights(*args: Any, **kwargs: Any) -> Any:
        """True if the component has weights associated with its elements."""
    @property
    def isComplete(*args: Any, **kwargs: Any) -> Any:
        """Marking a component as complete means that it represents a full set
        of indices from 0 to elementCount-1
        """
    @isComplete.setter
    def isComplete(*args: Any, **kwargs: Any) -> Any:
        """Marking a component as complete means that it represents a full set
        of indices from 0 to elementCount-1
        """
    @property
    def isEmpty(*args: Any, **kwargs: Any) -> Any:
        """True if the component contains no elements."""
    @isEmpty.setter
    def isEmpty(*args: Any, **kwargs: Any) -> Any:
        """True if the component contains no elements."""
    def isEqual(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isEqual(MObject other) -> bool

        Returns True if other refers to the same component as the
        one to which the function set is currently attached.
        """
    def weight(self: Self, *args: Any, **kwargs: Any) -> Any:
        """weight(index) -> MWeight

        Returns the weight associated with the specified element,
        where index can range from 0 to elementCount-1.
        """

class MFnData(MFnBase):
    kAny: int = ...
    kComponentList: int = ...
    kDoubleArray: int = ...
    kDynArrayAttrs: int = ...
    kDynSweptGeometry: int = ...
    kFalloffFunction: int = ...
    kFloatArray: int = ...
    kIntArray: int = ...
    kInvalid: int = ...
    kLast: int = ...
    kLattice: int = ...
    kMatrix: int = ...
    kMatrixArray: int = ...
    kMesh: int = ...
    kNId: int = ...
    kNObject: int = ...
    kNumeric: int = ...
    kNurbsCurve: int = ...
    kNurbsSurface: int = ...
    kPlugin: int = ...
    kPluginGeometry: int = ...
    kPointArray: int = ...
    kSphere: int = ...
    kString: int = ...
    kStringArray: int = ...
    kSubdSurface: int = ...
    kVectorArray: int = ...

class MFnComponentListData(MFnData):
    def add(self: Self, *args: Any, **kwargs: Any) -> Any:
        """add(MObject) -> self

        Adds the specified component to the end of the list.
        """
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Removes all of the components from the list.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new, empty component list, attaches it to the
        function set and returns an MObject which references it.
        """
    def get(self: Self, *args: Any, **kwargs: Any) -> Any:
        """get(index) -> MObject

        Returns a copy of the component at the specified index.
        Raises IndexError if the index is out of range.
        """
    def has(self: Self, *args: Any, **kwargs: Any) -> Any:
        """has(MObject) -> bool

        Returns True if the list contains the specified
        component, False otherwise.
        """
    def length(self: Self, *args: Any, **kwargs: Any) -> Any:
        """length() -> int

        Returns the number of components in the list.
        """
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(MObject) -> self
        remove(index) -> self

        Removes the specified component from the list.
        No exception is raised if the component is not in the list,
        raises IndexError if index is out of range
        """

class MFnCompoundAttribute(MFnAttribute):
    def addChild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a child attribute."""
    def child(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the attribute's children, specified by index."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new compound attribute, attaches it to the function set and returns it as an MObject."""
    def getAddAttrCmds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list of MEL 'addAttr' commands capable of recreating the attribute and all of its children."""
    def numChildren(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns number of child attributes currently parented under the compound attribute."""
    def removeChild(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove a child attribute."""

class MFnContainerNode(MFnDependencyNode):
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear()

        Delete all members of the container.
        """
    def getCurrentAsMObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentAsMObject() -> MObject

        Retrieve the current container node.
        """
    def getMembers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMembers() -> MObjectArray

        Return an array of the nodes included in this container.
        """
    def getParentContainer(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParentContainer() -> MObject

        Return the parent container, if there is one. Otherwise return an empty MObject.
        """
    def getPublishedNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPublishedNames(unboundOnly=bool) -> [MString]

        Return a list of published names on the container. Depending on the arguments, either all published names or only unbound published names will be returned.
        """
    def getPublishedNodes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPublishedNodes(publishNodeType=MPublishNodeType) -> ([MString] publishedNames, MObjectArray publishedNodes)

        Return a list of the published nodes of a given type. For any names that have assigned nodes, return the node at the corresponding array index. For any names that do not have assigned nodes, a NULL MObject will be at the corresponding array index.
        """
    def getPublishedPlugs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPublishedPlugs() -> (MPlugArray publishedPlugs, [MString] publishedNames)

        Return a tuple of plugs that have been published on this container and the names of those plugs.
        """
    def getRootTransform(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRootTransform() -> MObject

        Return the root transform, if there is one. Otherwise return an empty MObject.
        """
    def getSubcontainers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSubcontainers() -> MObjectArray

        Return an array of the container nodes included in this container.
        """
    def isCurrent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isCurrent() -> bool

        Return whether the container node managed by this function set is the current container.
        """
    def makeCurrent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """makeCurrent(isCurrent) -> self

        Set or clear whether the container managed by this function set is denoted as the
        the current container.  If the flag is true and the container is allowed to be
        current, then the current container is set to be the container.  Otherwise, if the
        container managed by the function set is the current container, then the current
        container is cleared.

        * isCurrent (True/False) - Specifies whether this container shall be current.
        """

class MFnDoubleArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MDoubleArray."""
    def copyTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new double array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MFnDoubleIndexedComponent(MFnComponent):
    def addElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElement(uIndex, vIndex) -> self
        addElement([uIndex, vIndex]) -> self

        Adds the element identified by (uIndex, vIndex) to the component.
        """
    def addElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElements(sequence of [uIndex, vIndex]) -> self

        Adds the specified elements to the component. Each item in the
        elements sequence is itself a sequence of two ints which are the U and
        V indices of an element to be added.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """
    def getCompleteData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCompleteData() -> (numU, numV)

        Returns a tuple containing the number of U and V indices in the complete
        component, or (0,0) if the component is not complete.
        """
    def getElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getElement(index) -> (uIndex, vIndex)

        Returns the index'th element of the component as a tuple containing the
        element's U and V indices.
        """
    def getElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getElements() -> list of (uIndex, vIndex)

        Returns all of the component's elements as a list of tuples with each
        tuple containing the U and V indices of a single element.
        """
    def setCompleteData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCompleteData(numU, numV) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numU and numV indicate the number of U and V indices in the complete
        component (i.e. the max U index is numU-1 and the max V index is numV-1).
        """

class MFnEnumAttribute(MFnAttribute):
    def addField(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add an item to the enumeration with a specified UI name and corresponding attribute value."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new enumeration attribute, attaches it to the function set and returns it as an MObject."""
    @property
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    @default.setter
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    def fieldName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the name of the enumeration item which has a given value."""
    def fieldValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the enumeration item which has a given name."""
    def getMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the maximum value of all the enumeration items."""
    def getMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the minimum value of all the enumeration items."""
    def setDefaultByName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set the default value using the name of an enumeration item. Equivalent to: attr.default = attr.fieldValue(name)"""

class MFnGenericAttribute(MFnAttribute):
    def addDataType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified Maya data type to the list of those accepted by the attribute."""
    def addNumericType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified numeric type to the list of those accepted by the attribute."""
    def addTypeId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified data typeId to the list of those accepted by the attribute."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new generic attribute, attaches it to the function set and returns it as an MObject."""
    def removeDataType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified Maya data type from the list of those accepted by the attribute."""
    def removeNumericType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified numeric type from the list of those accepted by the attribute."""
    def removeTypeId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified data typeId from the list of those accepted by the attribute."""

class MFnGeometryData(MFnData):
    def addComponentTag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addComponentTag(key) -> self

        Adds a componentTag with the given key to the object.
        """
    def addObjectGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addObjectGroup(id) -> self

        Adds an object group with the given id to the object.
        """
    def addObjectGroupComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addObjectGroupComponent(id, MObject component) -> self

        Adds the members of the given component to the object group
        with the given id.
        """
    def changeObjectGroupId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """changeObjectGroupId(sourceId, destId) -> self

        Changes the id of the object group with the given id to the new id.
        """
    def componentTagContents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentTagContents(key) -> MObject

        Returns a component which contains the members of the componentTag
        with the given key.
        """
    def componentTagExpressionSubsetState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentTagExpressionSubsetState(expr,ctg) -> MFnGeometryData::SubsetState type constant

        Returns the state of the contents of the resolved componentTag expression.
        """
    def componentTagType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentTagType(key) -> MFn Type constant

        Returns the type of the component that the componentTag with the
        given key contains.
        """
    def componentTags(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentTags() -> MObject

        Returns the componentTag keys contained in the object.
        """
    def copyObjectGroups(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyObjectGroups(MObject inGeom) -> self

        Copies the object groups from the given geometry data object.
        """
    def hasComponentTag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasComponentTag(key) -> bool

        Returns True if a componentTag with the given key exists.
        """
    def hasObjectGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasObjectGroup(id) -> self

        Returns True if an object group with the given id is
        contained in the data.
        """
    @property
    def isIdentity(*args: Any, **kwargs: Any) -> Any:
        """True if the matrix for the geometry is the identity."""
    @isIdentity.setter
    def isIdentity(*args: Any, **kwargs: Any) -> Any:
        """True if the matrix for the geometry is the identity."""
    @property
    def isNotIdentity(*args: Any, **kwargs: Any) -> Any:
        """True if the matrix for the geometry is not the identity."""
    @isNotIdentity.setter
    def isNotIdentity(*args: Any, **kwargs: Any) -> Any:
        """True if the matrix for the geometry is not the identity."""
    @property
    def matrix(*args: Any, **kwargs: Any) -> Any:
        """MMatrix used to convert the object into local space."""
    @matrix.setter
    def matrix(*args: Any, **kwargs: Any) -> Any:
        """MMatrix used to convert the object into local space."""
    def objectGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectGroup(index) -> int

        Returns the id of the index'th object group contained by the object.
        """
    def objectGroupComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectGroupComponent(id) -> MObject

        Returns a component which contains the members of the object group
        with the given id.
        """
    @property
    def objectGroupCount(*args: Any, **kwargs: Any) -> Any:
        """The number of object groups contained by the object."""
    @objectGroupCount.setter
    def objectGroupCount(*args: Any, **kwargs: Any) -> Any:
        """The number of object groups contained by the object."""
    def objectGroupSubsetState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectGroupSubsetState(id) -> MFnGeometryData::SubsetState type constant

        Returns the state of the group contents of the object group with the
        given id.
        """
    def objectGroupType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectGroupType(id) -> MFn Type constant

        Returns the type of the component that the object group with the
        given id contains.
        """
    def removeComponentTag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeComponentTag(key) -> self

        Removes a componentTag with the given key from the object.
        """
    def removeObjectGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeObjectGroup(id) -> self

        Removes an object group with the given id from the object.
        """
    def removeObjectGroupComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeObjectGroupComponent(id, MObject component) -> self

        Removes the members of the given component from the object group
        with the given id.
        """
    def renameComponentTag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renameComponentTag(key, newKey) -> self

        Renames a componentag with the given key the object.
        """
    def resolveComponentTagExpression(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resolveComponentTagExpression(key, ctg) -> MObject

        Returns a component which is the result of the resolved componentTag expression
        with the given key.
        """
    def setComponentTagContents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setComponentTagContents(key, MObject component) -> self

        Sets the members of the componentTag with the given key
        to be those in the given component.
        """
    def setObjectGroupComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setObjectGroupComponent(id, MObject component) -> self

        Sets the members of the object group with the given id
        to be only those in the given component.
        """

class MFnIntArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MIntArray."""
    def copyTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new int array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MFnLightDataAttribute(MFnAttribute):
    def child(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the attribute's children, specified by index."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new light data attribute, attaches it to the function set and returns it as an MObject."""
    @property
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default values for the light data attribute's child attributes."""
    @default.setter
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default values for the light data attribute's child attributes."""

class MFnMatrixArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MMatrixArray."""
    def copyTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MMatrix array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MFnMatrixAttribute(MFnAttribute):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new matrix attribute, attaches it to the function set and returns it as an MObject."""
    @property
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    @default.setter
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""

class MFnMatrixData(MFnData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new matrix data object."""
    def isTransformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attached object is an MTransformationMatrix, False if it is an MMatrix."""
    def matrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated matrix as an MMatrix."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the encapsulated matrix."""
    def transformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated matrix as an MTransformationMatrix."""

class MFnMesh(MFnDagNode):
    def addHoles(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addHoles(faceIndex, vertices, loopCounts, mergeVertices=True, pointTolerance=kPointTolerance) -> self

        Adds holes to a mesh polygon.
        loopCounts is an array of vertex counts.
        The first entry gives the count of vertices that make up the
        first hole to add to the polygon (using that many entries in vertexArray). The following
        entries in loopCounts give the count of vertices that make up each remaining hole,
        using the following entries in vertexArray.
        Therefore the sum of the entries of loopCounts should equal the total
        length of vertexArray.
        Note that holes should normally be specified with the opposite winding order
        to the exterior polygon.
        """
    def addPolygon(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPolygon(vertices, mergeVertices=True, pointTolerance=kPointTolerance, loopCounts=None) -> faceId

        Adds a new polygon to the mesh, returning the index of the new
        polygon. If mergeVertices is True and a new vertex is within
        pointTolerance of an existing one, then they are 'merged' by reusing
        the existing vertex and discarding the new one.

        loopCounts allows for polygons with holes. If supplied, it is an array of integer vertex
        counts. The first entry gives the count of vertices that make up the
        exterior of the polygon (using that many entries in vertexArray). The following
        entries in loopCounts give the count of vertices that make up each hole,
        using the following entries in vertexArray.
        Therefore the sum of the entries of loopCounts should equal the total
        length of vertexArray.
        Note that holes should normally be specified with the opposite winding order
        to the exterior polygon.
        """
    def allIntersections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allIntersections(raySource, rayDirection, space, maxParam,
            testBothDirections, faceIds=None, triIds=None, idsSorted=False,
            accelParams=None, tolerance=kIntersectTolerance, sortHits=False)
          -> (hitPoints, hitRayParams, hitFaces, hitTriangles, hitBary1s, hitBary2s)

        Finds all intersection of a ray starting at raySource and travelling
        in rayDirection with the mesh.

        If faceIds is specified, then only those faces will be considered
        for intersection. If both faceIds and triIds are given, then the
        triIds will be interpreted as face-relative and each pair of entries
        will be taken as a (face, triangle) pair to be considered for
        intersection. Thus, the face-triangle pair (10, 0) means the first
        triangle on face 10. If neither faceIds nor triIds is given, then
        all face-triangles in the mesh will be considered.

        The maxParam and testBothDirections flags can be used to control the
        radius of the search around the raySource point.

        The search proceeds by testing all applicable face-triangles looking
        for intersections. If the accelParams parameter is given then the
        mesh builds an intersection acceleration structure based on it. This
        acceleration structure is used to speed up the intersection
        operation, sometimes by a factor of several hundred over the non-
        accelerated case. Once created, the acceleration structure is cached
        and will be reused the next time this method (or anyIntersection()
        or allIntersections()) is called with an identically-configured
        MMeshIsectAccelParams object. If a different MMeshIsectAccelParams
        object is used, then the acceleration structure will be deleted and
        re-created according to the new settings. Once created, the
        acceleration structure will persist until either the object is
        destroyed (or rebuilt by a construction history operation), or the
        freeCachedIntersectionAccelerator() method is called. The
        cachedIntersectionAcceleratorInfo() and
        globalIntersectionAcceleratorsInfo() methods provide useful
        information about the resource usage of individual acceleration
        structures, and of all such structures in the system.
        If the ray hits the mesh, the details of the intersection points
        will be returned as a tuple containing the following:
        * hitPoints (MFloatPointArray) - coordinates of the points hit, in
          the space specified by the caller.* hitRayParams (MFloatArray) - parametric distances along the ray to
          the points hit.* hitFaces (MIntArray) - IDs of the faces hit
        * hitTriangles (MIntArray) - face-relative IDs of the triangles hit
        * hitBary1s (MFloatArray) - first barycentric coordinate of the
          points hit. If the vertices of the hitTriangle are (v1, v2, v3)
          then the barycentric coordinates are such that the hitPoint =
          (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3.* hitBary2s (MFloatArray) - second barycentric coordinate of the
          points hit.
        If no point was hit then the arrays will all be empty.
        """
    def anyIntersection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """anyIntersection(raySource, rayDirection, space, maxParam,
            testBothDirections, faceIds=None, triIds=None, idsSorted=False,
            accelParams=None, tolerance=kIntersectTolerance)
          -> (hitPoint, hitRayParam, hitFace, hitTriangle, hitBary1, hitBary2)

        Finds any intersection of a ray starting at raySource and travelling
        in rayDirection with the mesh.

        If faceIds is specified, then only those faces will be considered
        for intersection. If both faceIds and triIds are given, then the
        triIds will be interpreted as face-relative and each pair of entries
        will be taken as a (face, triangle) pair to be considered for
        intersection. Thus, the face-triangle pair (10, 0) means the first
        triangle on face 10. If neither faceIds nor triIds is given, then
        all face-triangles in the mesh will be considered.

        The maxParam and testBothDirections flags can be used to control the
        radius of the search around the raySource point.

        The search proceeds by testing all applicable face-triangles looking
        for intersections. If the accelParams parameter is given then the
        mesh builds an intersection acceleration structure based on it. This
        acceleration structure is used to speed up the intersection
        operation, sometimes by a factor of several hundred over the non-
        accelerated case. Once created, the acceleration structure is cached
        and will be reused the next time this method (or anyIntersection()
        or allIntersections()) is called with an identically-configured
        MMeshIsectAccelParams object. If a different MMeshIsectAccelParams
        object is used, then the acceleration structure will be deleted and
        re-created according to the new settings. Once created, the
        acceleration structure will persist until either the object is
        destroyed (or rebuilt by a construction history operation), or the
        freeCachedIntersectionAccelerator() method is called. The
        cachedIntersectionAcceleratorInfo() and
        globalIntersectionAcceleratorsInfo() methods provide useful
        information about the resource usage of individual acceleration
        structures, and of all such structures in the system.
        If the ray hits the mesh, the details of the intersection point
        will be returned as a tuple containing the following:
        * hitPoint (MFloatPoint) - coordinates of the point hit, in
          the space specified by the caller.* hitRayParam (float) - parametric distance along the ray to
          the point hit.* hitFace (int) - ID of the face hit
        * hitTriangle (int) - face-relative ID of the triangle hit
        * hitBary1 (float) - first barycentric coordinate of the
          point hit. If the vertices of the hitTriangle are (v1, v2, v3)
          then the barycentric coordinates are such that the hitPoint =
          (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3.* hitBary2 (float) - second barycentric coordinate of the point hit.
        If no point was hit then the arrays will all be empty.
        """
    def assignColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assignColor(faceId, vertexIndex, colorId, colorSet='') -> self

        Assigns a color from a colorSet to a specified vertex of a face.
        """
    def assignColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assignColors(colorIds, colorSet=') -> self

        Assigns colors to all of the mesh's face-vertices. The colorIds
        sequence must contain an entry for every vertex of every face, in
        face order, meaning that the entries for all the vertices of face 0
        come first, followed by the entries for the vertices of face 1, etc.
        """
    def assignUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assignUV(faceId, vertexIndex, uvId, uvSet='') -> self

        Assigns a UV coordinate from a uvSet to a specified vertex of a face.
        """
    def assignUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assignUVs(uvCounts, uvIds, uvSet='') -> self

        Assigns UV coordinates to the mesh's face-vertices.

        uvCounts contains the number of UVs to assign for each of the mesh's
        faces. That number must equal the number of vertices in the
        corresponding face or be 0 to indicate that no UVs will be assigned
        to that face.
        """
    def autoUniformGridParams(self: Self, *args: Any, **kwargs: Any) -> Any:
        """autoUniformGridParams() -> MMeshIsectAccelParams

        Creates an object which specifies a uniform voxel grid structure
        which can be used by the intersection routines to speed up their
        operation. The number of voxel cells to use will be determined
        automatically based on the density of triangles in the mesh. The
        grid acceleration structure will be cached with the mesh, so that
        if the same MMeshIsectAccelParams configuration is used on the next
        intersect call, the acceleration structure will not need to be rebuilt.
        """
    def booleanOp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """(Deprecated: Please use booleanOps instead) booleanOp(Boolean Operation constant, MFnMesh, MFnMesh) -> self

        Replaces this mesh's geometry with the result of a boolean operation
        on the two specified meshes.
        """
    def booleanOps(self: Self, *args: Any, **kwargs: Any) -> Any:
        """booleanOps(Boolean Operation constant, MObjectArray, bool) -> self

        Replaces this mesh's geometry with the result of a boolean operation
        on the specified meshes.
        """
    def cachedIntersectionAcceleratorInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cachedIntersectionAcceleratorInfo() -> string

        Retrieves a string that describes the intersection acceleration
        structure for this object, if any. The string will be of the
        following form:

          10x10x10 uniform grid, (build time 0.5s), (memory footprint 2000KB)

        It describes the configuration of the cached intersection
        accelerator, as well as how long it took to build it, and how much
        memory it is currently occupying. If the mesh has no cached
        intersection accelerator, the empty string is returned.
        """
    @property
    def checkSamePointTwice(*args: Any, **kwargs: Any) -> Any:
        """Controls whether polygons created or added through the functionset
        are checked for duplicate points.
        """
    @checkSamePointTwice.setter
    def checkSamePointTwice(*args: Any, **kwargs: Any) -> Any:
        """Controls whether polygons created or added through the functionset
        are checked for duplicate points.
        """
    def cleanupEdgeSmoothing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cleanupEdgeSmoothing() -> self

        Updates the mesh after setEdgeSmoothing has been done. This should
        be called only once, after all the desired edges have been had their
        smoothing set. If you don't call this method, the normals may not be
        correct, and the object will look odd in shaded mode.
        """
    def clearBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearBlindData(compType) -> self
        clearBlindData(compType, blindDataId, compId=None, attr='') -> self


        The first version deletes all blind data from all the mesh's
        components of the given type (an MFn Type constant).

        The second version deletes values of the specified blind data type
        from the mesh's components of a given type. If a component ID is
        provided then the data is only deleted from that component,
        otherwise it is deleted from all of the mesh's components of the
        specified type. If a blind data attribute name is provided then only
        data for that attribute is deleted, otherwise data for all of the
        blind data type's attributes is deleted.
        """
    def clearColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearColors(colorSet='') -> self

        Clears out all colors from a colorSet, and leaves behind an empty
        colorset. This method should be used if it is needed to shrink the
        actual size of the color set. In this case, the user should call
        clearColors(), setColors() and then assignColors() to rebuild the
        mapping info.

        When called on mesh data, the colors are removed. When called on a
        shape with no history, the colors are removed and the attributes are
        set on the shape. When called on a shape with history, the
        polyColorDel command is invoked and a polyColorDel node is created.

        If no colorSet is specified the mesh's current color set will be used.
        """
    def clearGlobalIntersectionAcceleratorInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearGlobalIntersectionAcceleratorInfo()

        Clears the 'total count', 'total build time', and 'peak memory'
        fields from the information string returned by
        globalIntersectionAcceleratorsInfo(). It will not cause information
        about currently existing accelerators to be lost.
        """
    def clearUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearUVs(uvSet='') -> self

        Clears out all uvs from a uvSet, and leaves behind an empty
        uvset. This method should be used if it is needed to shrink the
        actual size of the uv set. In this case, the user should call
        clearUVs(), setUVs() and then assignUVs() to rebuild the
        mapping info.

        When called on mesh data, the uvs are removed. When called on a
        shape with no history, the uvs are removed and the attributes are
        set on the shape. When called on a shape with history, the
        polyMapDel command is invoked and a polyMapDel node is created.

        If no uvSet is specified the mesh's current uv set will be used.
        """
    def closestIntersection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """closestIntersection(raySource, rayDirection, space, maxParam,
            testBothDirections, faceIds=None, triIds=None, idsSorted=False,
            accelParams=None, tolerance=kIntersectTolerance)
          -> (hitPoint, hitRayParam, hitFace, hitTriangle, hitBary1, hitBary2)

        Finds the closest intersection of a ray starting at raySource and
        travelling in rayDirection with the mesh.

        If faceIds is specified, then only those faces will be considered
        for intersection. If both faceIds and triIds are given, then the
        triIds will be interpreted as face-relative and each pair of entries
        will be taken as a (face, triangle) pair to be considered for
        intersection. Thus, the face-triangle pair (10, 0) means the first
        triangle on face 10. If neither faceIds nor triIds is given, then
        all face-triangles in the mesh will be considered.

        The maxParam and testBothDirections flags can be used to control the
        radius of the search around the raySource point.

        The search proceeds by testing all applicable face-triangles looking
        for intersections. If the accelParams parameter is given then the
        mesh builds an intersection acceleration structure based on it. This
        acceleration structure is used to speed up the intersection
        operation, sometimes by a factor of several hundred over the non-
        accelerated case. Once created, the acceleration structure is cached
        and will be reused the next time this method (or anyIntersection()
        or allIntersections()) is called with an identically-configured
        MMeshIsectAccelParams object. If a different MMeshIsectAccelParams
        object is used, then the acceleration structure will be deleted and
        re-created according to the new settings. Once created, the
        acceleration structure will persist until either the object is
        destroyed (or rebuilt by a construction history operation), or the
        freeCachedIntersectionAccelerator() method is called. The
        cachedIntersectionAcceleratorInfo() and
        globalIntersectionAcceleratorsInfo() methods provide useful
        information about the resource usage of individual acceleration
        structures, and of all such structures in the system.
        If the ray hits the mesh, the details of the intersection point
        will be returned as a tuple containing the following:
        * hitPoint (MFloatPoint) - coordinates of the point hit, in
          the space specified by the caller.* hitRayParam (float) - parametric distance along the ray to
          the point hit.* hitFace (int) - ID of the face hit
        * hitTriangle (int) - face-relative ID of the triangle hit
        * hitBary1 (float) - first barycentric coordinate of the
          point hit. If the vertices of the hitTriangle are (v1, v2, v3)
          then the barycentric coordinates are such that the hitPoint =
          (*hitBary1)*v1 + (*hitBary2)*v2 + (1-*hitBary1-*hitBary2)*v3.* hitBary2 (float) - second barycentric coordinate of the point hit.
        If no point was hit then the arrays will all be empty.
        """
    def collapseEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """collapseEdges(seq of int) -> self

        Collapses edges into vertices. The two vertices that create each
        given edge are replaced in turn by one vertex placed at the average
        of the two initial vertex.
        """
    def collapseFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """collapseFaces(seq of int) -> self

        Collapses faces into vertices. Adjacent faces will be collapsed
        together into a single vertex. Non-adjacent faces will be collapsed
        into their own, separate vertices.
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(MObject, parent=kNullObj) -> MObject

        Creates a new mesh with the same geometry as the source. Raises
        TypeError if the source is not a mesh node or mesh data object or it
        contains an empty mesh.

        If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create())
        then a mesh data object will be created and returned and the wrapper
        will be set to reference it.

        If the parent is a transform type node then a mesh node will be
        created and parented beneath it and the return value will be the
        mesh node.

        If the parent is any other type of node a TypeError will be raised.

        If no parent is provided then a transform node will be created and
        returned and a mesh node will be created and parented under the
        transform.
        """
    def copyInPlace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyInPlace(MObject) -> self

        Replaces the current mesh's geometry with that from the source.
        Raises TypeError if the source is not a mesh node or mesh data
        object or it contains an empty mesh.
        """
    def copyUVSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyUVSet(fromName, toName, modifier=None) -> string

        Copies the contents of one UV set into another.

        If the source UV set does not exist, or if it has the same name as
        the destination, then no copy will be made.

        If the destination UV set exists then its contents will be replace
        by a copy of the source UV set.

        If the destination UV set does not exist then a new UV set will be
        created and the source UV set will be copied into it. The name of
        the UV set will be that provided with a number appended to the end
        to ensure uniqueness.
        The final name of the destination UV set will be returned.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(vertices, polygonCounts, polygonConnects, uValues=None, vValues=None, parent=kNullObj) -> MObjectcreate(vertices, edges, edgeConnectsCount, edgeFaceConnects, edgeFaceDesc, storeDoubles=False, parent=kNullObj) -> MObjectcreate(vertices, edges, polygonCounts, polygonConnects, uValues=None, vValues=None, parent=kNullObj) -> MObject

        Creates a new polygonal mesh and sets this function set to operate
        on it. This method is meant to be as efficient as possible and thus
        assumes that all the given data is topologically correct.
        If edges are supplied, edges must be an integer array containingconsecutive sets of 3 integers (startVertex, endVertex, smooth) peredge. polygonConnects then references edges by index into the edgearray, where the ID == edge array index / 3.
        If UV values are supplied both parameters must be given and they
        must contain the same number of values, otherwise IndexError will be
        raised. Note that the UVs are simply stored in the mesh, not
        assigned to any vertices. To assign them use assignUVs().
        If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create())
        then a mesh data object will be created and returned and the wrapper
        will be set to reference it.
        If the parent is a transform type node then a mesh node will be
        created and parented beneath it and the return value will be the
        mesh node.
        If the parent is any other type of node a TypeError will be raised.

        If no parent is provided then a transform node will be created and
        returned and a mesh node will be created and parented under the
        transform.
        """
    def createBlindDataType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createBlindDataType(blindDataId, ((longName, shortName, typeName), ...)) -> self

        Create a new blind data type with the specified attributes.

        Each element of the attrs sequence is a tuple containing the long
        name, short name and type name of the attribute. Valid type names
        are 'int', 'float', 'double', 'boolean', 'string' or 'binary'.

        Raises RuntimeError if the blind data id is already in use or an
        invalid format was specified.
        """
    def createColorSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createColorSet(name, clamped, rep=kRGBA, modifier=None, instances=None) -> string

        Creates a new, empty color set for this mesh.

        If no name is provided 'colorSet#' will be used, where # is a number
        that makes the name unique for this mesh. If a name is provided but
        it conflicts with that of an existing color set then a number will
        be appended to the proposed name to make it unique.
        The return value is the final name used for the new color set.

        This method will only work when the functionset is attached to a
        mesh node, not mesh data.
        """
    def createInPlace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createInPlace(vertices, polygonCounts, polygonConnects) -> selfcreateInPlace(vertices, edges, polygonCounts, polygonConnects) -> self

        Replaces the existing polygonal mesh with a new one. This method is
        meant to be as efficient as possible and thus assumes that all the
        given data is topologically correct.

        If edges are supplied, edges must be an integer array containingconsecutive sets of 3 integers (startVertex, endVertex, smooth) peredge. polygonConnects then references edges by index into the edgearray, where the ID == edge array index / 3.
        The vertices may be given as a sequence of MFloatPoint's or a
        sequence of MPoint's, but not a mix of the two.
        """
    def createUVSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createUVSet(name, modifier=None, instances=None) -> string

        Creates a new, empty UV set for this mesh.

        If a UV set with proposed name already exists then a number will be
        appended to the proposed name to name it unique.

        If the proposed name is empty then a name of the form uvSet# will be
        used where '#' is a number chosen to ensure that the name is unique.

        The name used for the UV set will be returned.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
    def currentColorSetName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentColorSetName(instance=kInstanceUnspecified) -> string

        Get the name of the 'current' color set. The current color set is
        the one used for color operations when no color set is explicitly
        specified.
        On instanced meshes, color sets may be applied on a per-instance
        basis or may be shared across all instances. When the color sets are
        per-instance, the concept of the current color set has two levels of
        granularity. Namely, the current color set applies to one or more
        instances, plus there are other color sets in the same color set
        family that apply to different instances. The instance arguement is
        used to indicate that if this is a per-instance color set, you are
        interested in the name of the color set that applies to the
        specified instance. When the index is not specified, the current
        color set will be returned regardless of which instance it is for.
        If there is no current color set, then an empty string will be
        returned.
        """
    def currentUVSetName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentUVSetName(instance=kInstanceUnspecified) -> string

        Get the name of the 'current' uv set. The current uv set is
        the one used for uv operations when no uv set is explicitly
        specified.
        On instanced meshes, uv sets may be applied on a per-instance
        basis or may be shared across all instances. When the uv sets are
        per-instance, the concept of the current uv set has two levels of
        granularity. Namely, the current uv set applies to one or more
        instances, plus there are other uv sets in the same uv set
        family that apply to different instances. The instance arguement is
        used to indicate that if this is a per-instance uv set, you are
        interested in the name of the uv set that applies to the
        specified instance. When the index is not specified, the current
        uv set will be returned regardless of which instance it is for.
        If there is no current uv set, then an empty string will be
        returned.
        """
    def deleteColorSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteColorSet(colorSet, modifier=None, currentSelection=None) -> self

        Deletes a color set from the mesh.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
    def deleteEdge(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteEdge(edgeId, modifier=None) -> self

        Deletes the specified edge.
        """
    def deleteFace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteFace(faceId, modifier=None) -> self

        Deletes the specified face.
        """
    def deleteUVSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteUVSet(uvSet, modifier=None, currentSelection=None) -> self

        Deletes a uv set from the mesh.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """
    def deleteVertex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteVertex(vertexId, modifier=None) -> self

        Deletes the specified vertex.
        """
    @property
    def displayColors(*args: Any, **kwargs: Any) -> Any:
        """Determines if the mesh's colors are displayed. Attempting to turn
        color display on when the functionset is attached to mesh data (as
        opposed to a mesh node) will raise TypeError.
        """
    @displayColors.setter
    def displayColors(*args: Any, **kwargs: Any) -> Any:
        """Determines if the mesh's colors are displayed. Attempting to turn
        color display on when the functionset is attached to mesh data (as
        opposed to a mesh node) will raise TypeError.
        """
    def duplicateFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """duplicateFaces(faces, translation=None) -> self

        Duplicates a set of faces and detaches them from the rest of the
        mesh. The resulting mesh will contain one more independant piece of
        geometry.
        """
    def edgeBorderInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """edgeBorderInfo(edgeId, setId=0) -> MFnMesh::BorderInfo

        Returns if the specified edge is on geom/UV shell border or has shared/unshared UVs.
        """
    def extractFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """extractFaces(faces, translation=None) -> self

        Detaches a set of faces from the rest of the mesh. The resulting
        mesh will contain one more independant piece of geometry.
        """
    def extrudeEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """extrudeEdges(edges, extrusionCount=1, translation=None, extrudeTogether=True, thickness=0.0, offset=0.0) -> self

        Extrude the given edges along a vector. The resulting mesh will have
        extra parallelograms coming out of the given edges and going to the
        new extruded edges. The length of the new polygon is determined by
        the length of the vector. The extrusionCount parameter is the number
        of subsequent extrusions per edges and represents the number of
        polygons that will be created from each given edge to the extruded
        edges.
        The difference between using thickness or offset instead of providing
        a vector with the translation variable is that the translation will
        be applied to each vertex in the extrusion along its local direction.  This
        can result in vertices being moved the same distance, but the angles between
        the original components are not maintained so the overall shape is not the
        same.
        Both the thickness and offset variables will attempt to move the components
        a distance that will maintain angles between edges at the border of the
        extrusion.
        """
    def extrudeFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """extrudeFaces(faces, extrusionCount=1, translation=None, extrudeTogether=True, thickness=0.0, offset=0.0) -> self

        Extrude the given faces along a vector. The resulting mesh will have
        extra parallelograms coming out of the given faces and going to the
        new extruded faces. The length of the new polygon is determined by
        the length of the vector. The extrusionCount parameter is the number
        of subsequent extrusions per faces and represents the number of
        polygons that will be created from each given face to the extruded
        faces.
        The difference between using thickness or offset instead of providing
        a vector with the translation variable is that the translation will
        be applied to each vertex in the extrusion along its local direction.  This
        can result in vertices being moved the same distance, but the angles between
        the original components are not maintained so the overall shape is not the
        same.
        Both the thickness and offset variables will attempt to move the components
        a distance that will maintain angles between edges at the border of the
        extrusion.
        """
    def freeCachedIntersectionAccelerator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """freeCachedIntersectionAccelerator() -> self

        If the mesh has a cached intersection accelerator structure, then
        this routine forces it to be deleted. Ordinarily, these structures
        are cached so that series of calls to the closestIntersection(),
        allIntersections(), and anyIntersection() methods can reuse the same
        structure. Once the client is finished with these intersection
        operations, however, they are responsible for freeing the acceleration
        structure, which is what this method does.
        """
    def generateSmoothMesh(self: Self, *args: Any, **kwargs: Any) -> Any:
        """generateSmoothMesh(parent=kNullObj, options=None) -> MObject

        Creates a new polygonal mesh which is a smoothed version of the one
        to which the functionset is attached. If an options object is supplied
        it will be used to direct the smoothing operation, otherwise the
        mesh's Smooth Mesh Preview attributes will be used.

        If the parent is a kMeshData wrapper (e.g. from MFnMeshData.create())
        then a mesh data object will be created and returned.
        If the parent is a transform type node then a mesh node will be
        created and parented beneath it and the return value will be the
        mesh node.
        If the parent is any other type of node a TypeError will be raised.

        If no parent is provided then a transform node will be created and
        returned and a mesh node will be created and parented under the
        transform.

        Note that, unlike the create functions, this function does not set
        the functionset to operate on the new mesh, but leaves it attached
        to the original mesh.
        """
    def getAssignedUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAssignedUVs(uvSet='') -> (counts, uvIds)

        Returns a tuple containing all of the UV assignments for the specified
        UV set. The first element of the tuple is an array of counts giving
        the number of UVs assigned to each face of the mesh. The count will
        either be zero, indicating that that face's vertices do not have UVs
        assigned, or else it will equal the number of the face's vertices.
        The second element of the tuple is an array of UV IDs for all of the
        face-vertices which have UVs assigned.
        """
    def getAssociatedColorSetInstances(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedColorSetInstances(colorSet) -> MIntArray

        Returns the instance numbers associated with the specified Color set.
        If the color map is shared across all instances, an empty array will
        be returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
    def getAssociatedUVSetInstances(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedUVSetInstances(uvSet) -> MIntArray

        Returns the instance numbers associated with the specified UV set.
        If the uv map is shared across all instances, an empty array will be
        returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
    def getAssociatedUVSetTextures(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedUVSetTextures(uvSet) -> MObjectArray

        Returns the texture nodes which are using the specified UV set. If
        the texture has a 2d texture placement, the texture, and not the
        placement will be returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
    def getBinaryBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBinaryBlindData(compId, compType, blindDataId, attr) -> string
        getBinaryBlindData(compType, blindDataId, attr)
          -> (MIntArray, [string, string, ...])

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of 'binary'
        type.
        """
    def getBinormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBinormals(space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns the binormal vectors for all face-vertices.

        This method is not threadsafe.
        """
    def getBlindDataAttrNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBlindDataAttrNames(blindDataId) -> ((longName, shortName, typeName), ...)

        Returns a tuple listing the attributes of the given blind data type.
        Each element of the tuple is itself a tuple containing the long
        name, short name and type name of the attribute. Type names can be
        'int', 'float', 'double', 'boolean', 'string' or 'binary'.
        """
    def getBlindDataTypes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBlindDataTypes(MFn Type constant) -> MIntArray

        Returns all the blind data ID's associated with the given component
        type on this mesh.
        """
    def getBoolBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBoolBlindData(compId, compType, blindDataId, attr) -> bool
        getBoolBlindData(compType, blindDataId, attr) -> (MIntArray, MIntArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'boolean' type.
        """
    def getClosestNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getClosestNormal(MPoint, space=MSpace.kObject) -> (MVector, int)

        Returns a tuple containing the normal at the closest point on the
        mesh to the given point and the ID of the face in which that closest
        point lies.
        """
    def getClosestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getClosestPoint(MPoint, space=MSpace.kObject) -> (MPoint, int)

        Returns a tuple containing the closest point on the mesh to the
        given point and the ID of the face in which that closest point lies.

        This method is not threadsafe.
        """
    def getClosestPointAndNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getClosestPointAndNormal(MPoint, space=MSpace.kObject)
          -> (MPoint, MVector, int)

        Returns a tuple containing the closest point on the mesh to the
        given point, the normal at that point, and the ID of the face in
        which that point lies.

        This method is not threadsafe.
        """
    def getClosestUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getClosestUVs(u, v, uvSet='') -> MIntArray

        Returns the IDs of the UVs which are nearest in uv space to the
        given texture coordinate in the specified UV set. All these UVs
        locate at the same distance to the given coordinate.
        """
    def getColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorId, colorSet='') -> MColor

        Returns a color from a colorSet. Raises IndexError if the colorId is
        out of range.
        """
    def getColorIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndex(faceId, localVertexId, colorSet='') -> int

        Returns the index into the specified colorSet of the color used by a
        specific face-vertex. This can be used to index into the sequence
        returned by getColors().
        """
    def getColorRepresentation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorRepresentation(colorSet) -> Color Representation constant

        Returns the Color Representation used by the specified color set.
        """
    def getColorSetFamilyNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorSetFamilyNames() -> (string, ...)

        Returns the names of all of the color set families on this object. A
        color set family is a set of per-instance sets with the same name
        with each individual set applying to one or more instances. A set
        which is shared across all instances will be the sole member of its
        family.

        Given a color set family name, getColorSetsInFamily() may be used to
        determine the names of the associated individual sets.
        """
    def getColorSetNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorSetNames() -> (string, ...)

        Returns the names of all the color sets on this object.
        """
    def getColorSetsInFamily(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorSetsInFamily(familyName) -> (string, ...)

        Returns the names of all of the color sets that belong to the
        specified family. Per-instance sets will have multiple sets in a
        family, with each individual set applying to one or more instances.
        A set which is shared across all instances will be the sole member
        of its family and will share the same name as its family.
        """
    def getColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColors(colorSet='') -> MColorArray

        Returns all of the colors in a colorSet. If no colorSet is specified
        then the default colorSet is used.

        Use the index returned by getColorIndex() to access the returned
        array.
        """
    def getConnectedShaders(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedShaders(instance) -> (MObjectArray, MIntArray)

        Returns a tuple containing an array of shaders (sets) and an array
        of ints mapping the mesh's polygons onto those shaders. For each
        polygon in the mesh there will be corresponding value in the second
        array. If it is -1 that means that the polygon is not assigned to a
        shader, otherwise it indicates the index into the first array of the
        shader to which that polygon is assigned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """
    def getCreaseEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCreaseEdges() -> (MUintArray, MDoubleArray)

        Returns a tuple containing two arrays. The first contains the mesh-
        relative/global IDs of the mesh's creased edges and the second
        contains the associated crease data.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned
        by Pixar(R).
        """
    def getCreaseVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCreaseVertices() -> (MUintArray, MDoubleArray)

        Returns a tuple containing two arrays. The first contains the mesh-
        relative/global IDs of the mesh's creased vertices and the second
        contains the associated crease data.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned
        by Pixar(R).
        """
    def getDoubleBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDoubleBlindData(compId, compType, blindDataId, attr) -> float
        getDoubleBlindData(compType, blindDataId, attr) -> (MIntArray, MDoubleArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'double' type.
        """
    def getEdgeVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEdgeVertices(edgeId) -> (int, int)

        Returns a tuple containing the mesh-relative/global IDs of the
        edge's two vertices. The indices can be used to refer to the
        elements in the array returned by the getPoints() method.
        """
    def getFaceAndVertexIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceAndVertexIndices(faceVertexIndex, localVertex=True) -> (int, int)

        Returns a tuple containg the faceId and vertexIndex represented by
        the given face-vertex index. This is the reverse of the operation
        performed by getFaceVertexIndex().

        If localVertex is True then the returned vertexIndex is the face-
        relative/local index, otherwise it is the mesh-relative/global index.
        """
    def getFaceNormalIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceNormalIds(faceId) -> MIntArray

        Returns the IDs of the normals for all the vertices of a given face.
        These IDs can be used to index into the arrays returned by getNormals().
        """
    def getFaceUVSetNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceUVSetNames(faceId) -> (string, ...)

        Returns the names of all of the uv sets mapped to the specified face.

        This method is not threadsafe.
        """
    def getFaceVertexBinormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexBinormal(faceId, vertexId, space=MSpace.kObject, uvSet='') -> MVector

        Returns the binormal vector at a given face vertex.

        This method is not threadsafe.
        """
    def getFaceVertexBinormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexBinormals(faceId, space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns all the per-vertex-per-face binormals for a given face.

        This method is not threadsafe.
        """
    def getFaceVertexColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexColors(colorSet='', defaultUnsetColor=None) -> MColorArray

        Returns colors for all the mesh's face-vertices.

        The colors are returned in face order: e.g. F0V0, F0V1.. F0Vn, F1V0,
        etc... Use the index returned by getFaceVertexIndex() if you wish to
        index directly into the returned color array.

        If no face has color for that vertex, the entry returned will be
        defaultUnsetColor. If a color was set for some but not all the faces
        for that vertex, the ones where the color has not been explicitly set
        will return (0,0,0). If a vertex has shared color, the same value
        will be set for all its vertes/faces.

        If the colorSet is not specified, the default color set will be used.
        If the defaultUnsetColor is not given, then (-1, -1, -1, -1) will be
        used.
        """
    def getFaceVertexIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexIndex(faceId, vertexIndex, localVertex=True) -> int

        Returns the index for a specific face-vertex into an array of face-
        vertex values, such as those returned by getFaceVertexBinormals(),
        getFaceVertexColors(), getFaceVertexNormals(), etc.

        The values in the target arrays are presumed to be in face order:
        F0V0, F0V1.. F0Vn, F1V0, etc...
        If localVertex is True then vertexIndex must be a face-relative/local
        index. If localVertex is False then vertexIndex must be a mesh-
        relative/global index.

        The opposite operation is performed by the getFaceAndVertexIndices()
        method.
        """
    def getFaceVertexNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexNormal(faceId, vertexId, space=MSpace.kObject) -> MVector

        Returns the per-vertex-per-face normal for a given face and vertex.

        This method is not threadsafe.
        """
    def getFaceVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexNormals(faceId, space=MSpace.kObject) -> MFloatVectorArray

        Returns the normals for a given face.

        This method is not threadsafe.
        """
    def getFaceVertexTangent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexTangent(faceId, vertexId, space=MSpace.kObject, uvSet='') -> MVector

        Return the normalized tangent vector at a given face vertex.

        The tangent is defined as the surface tangent of the polygon running
        in the U direction defined by the uv map.
        This method is not threadsafe.
        """
    def getFaceVertexTangents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexTangents(faceId, space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns all the per-vertex-per-face tangents for a given face.

        The tangent is defined as the surface tangent of the polygon running
        in the U direction defined by the uv map.

        This method is not threadsafe.
        """
    def getFloatBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFloatBlindData(compId, compType, blindDataId, attr) -> float
        getFloatBlindData(compType, blindDataId, attr) -> (MIntArray, MFloatArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'float' type.
        """
    def getFloatPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFloatPoints(space=MSpace.kObject) -> MFloatPointArray

        Returns an MFloatPointArray containing the mesh's vertices.
        """
    def getHoles(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getHoles() -> ((face, (v1, v2, ...)), (face, (v1, v2, ...)), ...)

        Returns a tuple describing the holes in the mesh. Each element of the
        tuple is itself a tuple. The first element of the sub-tuple is the
        integer ID of the face in which the hole occurs. The second element
        of the sub-tuple is another tuple containing the mesh-relative/global
        IDs of the vertices which make up the hole.

        Take the following return value as an example:

            ((3, (7, 2, 6)), (5, (11, 10, 3, 4)))

        This says that the mesh has two holes. The first hole is in face 3
        and consists of vertices 7, 2 and 6. The second hole is in face 5 and
        consists of vertices 11, 10, 3 and 4.
        """
    def getIntBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getIntBlindData(compId, compType, blindDataId, attr) -> int
        getIntBlindData(compType, blindDataId, attr) -> (MIntArray, MIntArray)

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of
        'int' type.
        """
    def getInvisibleFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getInvisibleFaces() -> MUintArray

        Returns the invisible faces of the mesh. Invisible faces are like
        lightweight holes in that they are not rendered but do not require
        additional geometry the way that holes do. They have the advantage
        over holes that if the mesh is smoothed then their edges will be
        smoothed as well, while holes will retain their hard edges.

        Invisible faces can be set using the setInvisibleFaces() method or
        the polyHole command.
        """
    def getMeshShellsIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMeshShellsIds(compType) -> (int, MIntArray)

        Returns a tuple containing describing how the specified component type items
        are grouped into shells. The first element of the tuple is the number
        of distinct shells. The second element of the tuple is an array of
        shell indices, one per component, indicating which shell that component is part of.
        """
    def getNormalIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormalIds() -> (MIntArray, MIntArray)

        Returns the normal IDs for all of the mesh's polygons as a tuple of
        two int arrays. The first array contains the number of vertices for
        each polygon and the second contains the normal IDs for each polygon-
        vertex. These IDs can be used to index into the array returned by
        getNormals().
        """
    def getNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormals(space=MSpace.kObject) -> MFloatVectorArray

        Returns a copy of the mesh's normals. The normals are the per-polygon
        per-vertex normals. To find the normal for a particular vertex-face,
        use getFaceNormalIds() to get the index into the array.

        This method is not threadsafe.
        """
    def getPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPoint(vertexId, space=MSpace.kObject) -> MPoint

        Returns the position of specified vertex.
        """
    def getPointAtUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtUV(faceId, u, v, space=MSpace.kObject, uvSet='', tolerance=0.0) -> MPoint

        Returns the position of the point at the give UV value in the
        specified face.

        This method is not threadsafe.
        """
    def getPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPoints(space=MSpace.kObject) -> MPointArray

        Returns a copy of the mesh's vertex positions as an MPointArray.
        """
    def getPointsAtUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPointsAtUV(u, v, space=MSpace.kObject, uvSet='', tolerance=0.001) -> (MIntArray, MPointArray)

        Returns the polygon ids and positions of points at the given UV position on the mesh.
        """
    def getPolygonNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonNormal(polygonId, space=MSpace.kObject) -> MVector

        Returns the per-polygon normal for the given polygon.

        This method is not threadsafe.
        """
    def getPolygonTriangleVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonTriangleVertices(polygonId, triangleId) -> (int, int, int)

        Returns the mesh-relative/global IDs of the 3 vertices of the
        specified triangle of the specified polygon. These IDs can be used
        to index into the arrays returned by getPoints() and getFloatPoints().
        """
    def getPolygonUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonUV(polygonId, vertexId, uvSet='') -> (float, float)

        Returns a tuple containing the U and V values at a specified vertex
        of a specified polygon.

        This method is not threadsafe.
        """
    def getPolygonUVid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonUVid(polygonId, vertexId, uvSet='') -> int

        Returns the ID of the UV at a specified vertex of a specified polygon.

        This method is not threadsafe.
        """
    def getPolygonVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonVertices(polygonId) -> MIntArray

        Returns the mesh-relative/global vertex IDs the specified polygon.
        These IDs can be used to index into the arrays returned by getPoints()
        and getFloatPoints().
        """
    def getSmoothMeshDisplayOptions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSmoothMeshDisplayOptions() -> MMeshSmoothOptions

        Returns the options currently in use when smoothing the mesh for display.
        """
    def getStringBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getStringBlindData(compId, compType, blindDataId, attr) -> string
        getStringBlindData(compType, blindDataId, attr)
          -> (MIntArray, [string, string, ...])

        The first version returns the value of the specified blind data
        attribute from the specified mesh component.

        The second version returns a tuple containing an array of component
        IDs and an array of values for the specified blind data attribute
        for all of the mesh's components of the specified type.

        Both versions raise RuntimeError if the attribute is not of 'string'
        type.
        """
    def getTangentId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTangentId(faceId, vertexId) -> int

        Returns the ID of the tangent for a given face and vertex.
        """
    def getTangents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTangents(space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Return the tangent vectors for all face vertices. The tangent is
        defined as the surface tangent of the polygon running in the U
        direction defined by the uv map.

        This method is not threadsafe.
        """
    def getTriangleOffsets(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTriangleOffsets() -> (MIntArray, MIntArray)

        Returns the number of triangles for every polygon face and the
        offset into the vertex indices array for each triangle vertex (see getVertices()).
        The triangleVertices array holds each vertex for each triangle in sequence,
        so it has three times as many elements as there are triangles.
        (i.e. three times the sum of the elements of the triangleCounts array)
        """
    def getTriangles(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTriangles() -> (MIntArray, MIntArray)

        Returns a tuple describing the mesh's triangulation. The first
        element of the tuple is an array giving the number of triangles for
        each of the mesh's polygons. The second tuple gives the ids of the
        vertices of all the triangles.
        """
    def getUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvId, uvSet='') -> (float, float)

        Returns a tuple containing the u and v values of the specified UV.
        """
    def getUVAtPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVAtPoint(point, space=MSpace.kObject, uvSet='') -> (float, float, int)

        Returns a tuple containing the u and v coordinates of the point on
        the mesh closest to the given point, and the ID of the face
        containing that closest point.

        This method is not threadsafe.
        """
    def getUVBorderEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVBorderEdges(setId) -> MIntArray

        Retrieves the edge indices for edges lying on a UV border.
        """
    def getUVSetFamilyNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetFamilyNames() -> (string, ...)

        Returns the names of all of the uv set families on this object. A
        uv set family is a set of per-instance sets with the same name
        with each individual set applying to one or more instances. A set
        which is shared across all instances will be the sole member of its
        family.

        Given a uv set family name, getUVSetsInFamily() may be used to
        determine the names of the associated individual sets.
        """
    def getUVSetNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetNames() -> (string, ...)

        Returns the names of all the uv sets on this object.
        """
    def getUVSetsInFamily(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetsInFamily(familyName) -> (string, ...)

        Returns the names of all of the uv sets that belong to the
        specified family. Per-instance sets will have multiple sets in a
        family, with each individual set applying to one or more instances.
        A set which is shared across all instances will be the sole member
        of its family and will share the same name as its family.
        """
    def getUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVs(uvSet='') -> (MFloatArray, MFloatArray)

        Returns a tuple containing an array of U values and an array of V
        values, representing all of the UVs for the given UV set.
        """
    def getUvShellsIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUvShellsIds(uvSet='') -> (int, MIntArray)

        Returns a tuple containing describing how the specified UV set's UVs
        are grouped into shells. The first element of the tuple is the number
        of distinct shells. The second element of the tuple is an array of
        shell indices, one per uv, indicating which shell that uv is part of.
        """
    def getVertexColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getVertexColors(colorSet='', defaultUnsetColor=None) -> MColorArray

        Gets colors for all vertices of the given colorSet. If no face has
        color for that vertex, the entry returned will be defaultUnsetColor.
        If a color was set for some or all the faces for that vertex, an
        average of those vertex/face values where the color has been set will
        be returned.

        If the colorSet is not specified, the default color set will be used.
        If the defaultUnsetColor is not given, then (-1, -1, -1, -1) will be
        used.
        """
    def getVertexNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getVertexNormal(vertexId, angleWeighted, space=MSpace.kObject) -> MVector

        Returns the normal at the given vertex. The returned normal is a
        single per-vertex normal, so unshared normals at a vertex will be
        averaged.

        If angleWeighted is set to true, the normals are computed by an
        average of surrounding face normals weighted by the angle subtended
        by the face at the vertex. If angleWeighted is set to false, a simple
        average of surround face normals is returned.

        The simple average evaluation is significantly faster than the angle-
        weighted average.

        This method is not threadsafe.
        """
    def getVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getVertexNormals(angleWeighted, space=MSpace.kObject) -> MFloatVectorArray

        Returns all the vertex normals. The returned normals are per-vertex
        normals, so unshared normals at a vertex will be averaged.

        If angleWeighted is set to True, the normals are computed by an
        average of surrounding face normals weighted by the angle subtended
        by the face at the vertex. If angleWeighted is set to false, a simple
        average of surround face normals is returned.

        The simple average evaluation is significantly faster than the angle-
        weighted average.

        This method is not threadsafe.
        """
    def getVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getVertices() -> (MIntArray, MIntArray)

        Returns the mesh-relative/global vertex IDs for all of the mesh's
        polygons as a tuple of two int arrays. The first array contains the
        number of vertices for each polygon and the second contains the mesh-
        relative IDs for each polygon-vertex. These IDs can be used to index
        into the arrays returned by getPoints() and getFloatPoints().
        """
    def globalIntersectionAcceleratorsInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """globalIntersectionAcceleratorsInfo() -> string

        Returns a string that describes the system-wide resource usage for
        cached mesh intersection accelerators. The string will be of the
        following form:
          total 10 accelerators created (2 currently active - total current memory = 10000KB), total build time = 10.2s, peak memory = 14567.1KB

        This means that:

        * a total of 10 intersection accelerators have been created as
          instructed by calls to closestIntersection(), allIntersections(),
          or anyIntersection() with non-NULL accelParams values. Thesen  structures are destroyed and re-created when intersection requests
          with differing acceleration parameters are passed in for the same
          mesh, so it is useful to see this value, which is the total count
          of how many have been created. In this case, 8 of the 10 created
          have been destroyed, either automatically or via calls to the
          freeCachedIntersectionAccelerator() method

        * the total memory footprint for the 2 accelerators currently in
          existence is 10,000KB

        * the total build time for all 10 structures that have been created
          is 10.2 seconds
        * the peak of total memory usage for all accelerators in the system
          was 14567.1KB
        Calling clearGlobalIntersectionAcceleratorInfo() will clear the
        'total count', 'total build time', and 'peak memory' fields from
        this information. It will not cause information about currently
        existing accelerators to be lost.
        """
    def hasAlphaChannels(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasAlphaChannels(colorSet) -> bool

        Returns True if the color set has an alpha channel.
        """
    def hasBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasBlindData(compType, compId=None, blindDataId=None) -> bool

        Returns true if any component of the given type on this mesh has
        blind data. If a component ID is provided then only that particular
        component is checked. If a blind data ID is provided then only blind
        data of that type is checked.
        """
    def hasColorChannels(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasColorChannels(colorSet) -> bool

        Returns True if the color set has RGB channels.
        """
    def intersectFaceAtUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """intersectFaceAtUV(u, v, uvSet='') -> int

        Returns the IDs of the UVs on this surface which are nearest
        in uv space to the given uv set and coordinate.All these UVs
        locate at the same distance to the given coordinate.

        This method is not threadsafe.
        """
    def isBlindDataTypeUsed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isBlindDataTypeUsed(blindDataId) -> bool

        Returns True if the blind data type is already in use anywhere in the scene.
        """
    def isColorClamped(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isColorClamped(colorSet) -> bool

        Returns True if the color sets RGBA components are clamped to the
        range 0 to 1.
        """
    def isColorSetPerInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isColorSetPerInstance(colorSet) -> bool

        Returns True if the color set is per-instance, and False if it is
        shared across all instances.
        """
    def isEdgeSmooth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isEdgeSmooth(edgeId) -> bool

        Returns True if the edge is smooth, False if it is hard.
        """
    def isNormalLocked(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isNormalLocked(normalId) -> bool

        Returns True if the normal is locked, False otherwise.
        """
    def isPolygonConvex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPolygonConvex(faceId) -> bool

        Returns True if the polygon is convex, False if it is concave.
        """
    def isPolygonUVReversed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPolygonUVReversed(faceId) -> bool

        Returns True if the texture coordinates (uv's) for specified polygon are
        reversed (clockwise), False if they are not reversed (counter clockwise).
        """
    def isRightHandedTangent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isRightHandedTangent(tangentId, uvSet='') -> bool

        Returns True if the normal, tangent, and binormal form a right handed
        coordinate system, False otherwise.
        """
    def isUVSetPerInstance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isUVSetPerInstance(uvSet) -> bool

        Returns True if the UV set is per-instance, and False if it is shared
        across all instances.
        """
    kGeomBorder: int = ...
    kInstanceUnspecified: int = ...
    kIntersectTolerance: float = ...
    kPointTolerance: float = ...
    kUVBorder: int = ...

    def lockFaceVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lockFaceVertexNormals(seq of faceIds, seq of vertIds) -> self

        Locks the normals for the given face/vertex pairs.
        """
    def lockVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """lockVertexNormals(sequence of vertIds) -> self

        Locks the shared normals for the specified vertices.
        """
    @property
    def numColorSets(*args: Any, **kwargs: Any) -> Any:
        """Number of color sets."""
    @numColorSets.setter
    def numColorSets(*args: Any, **kwargs: Any) -> Any:
        """Number of color sets."""
    def numColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numColors(colorSet='') -> int

        Returns the number of colors in the given color set. If no color set
        is specified then the mesh's current color set will be used.
        """
    @property
    def numEdges(*args: Any, **kwargs: Any) -> Any:
        """Number of edges."""
    @numEdges.setter
    def numEdges(*args: Any, **kwargs: Any) -> Any:
        """Number of edges."""
    @property
    def numFaceVertices(*args: Any, **kwargs: Any) -> Any:
        """Total number of vertices within faces. Shared vertices are counted
        for each face which uses them.
        """
    @numFaceVertices.setter
    def numFaceVertices(*args: Any, **kwargs: Any) -> Any:
        """Total number of vertices within faces. Shared vertices are counted
        for each face which uses them.
        """
    @property
    def numNormals(*args: Any, **kwargs: Any) -> Any:
        """Number of per-polygon per-vertex normals."""
    @numNormals.setter
    def numNormals(*args: Any, **kwargs: Any) -> Any:
        """Number of per-polygon per-vertex normals."""
    @property
    def numPolygons(*args: Any, **kwargs: Any) -> Any:
        """Number of polygons (faces)."""
    @numPolygons.setter
    def numPolygons(*args: Any, **kwargs: Any) -> Any:
        """Number of polygons (faces)."""
    @property
    def numUVSets(*args: Any, **kwargs: Any) -> Any:
        """Number of UV (texture coordinate) sets."""
    @numUVSets.setter
    def numUVSets(*args: Any, **kwargs: Any) -> Any:
        """Number of UV (texture coordinate) sets."""
    def numUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numUVs(uvSet='') -> int

        Returns the number of UVs (texture coordinates) in the given UV set.
        If no UV set is specified then the mesh's current UV set will be used.
        """
    @property
    def numVertices(*args: Any, **kwargs: Any) -> Any:
        """Number of distinct vertices. Shared vertices are only counted once."""
    @numVertices.setter
    def numVertices(*args: Any, **kwargs: Any) -> Any:
        """Number of distinct vertices. Shared vertices are only counted once."""
    def onBoundary(self: Self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary(faceId) -> bool

        Returns true if the face is on the border of the mesh, meaning that
        one or more of its edges is a border edge.
        """
    def polygonVertexCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """polygonVertexCount(faceId) -> int

        Returns the number of vertices in the given polygon. Raises
        ValueError if the polygon ID is invalid.
        """
    def removeFaceColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeFaceColors(seq of faceIds) -> self

        Removes colors from all vertices of the specified faces.
        """
    def removeFaceVertexColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeFaceVertexColors(seq of faceIds, seq of vertexIds) -> self

        Removes colors from the specified face/vertex pairs.
        """
    def removeVertexColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeVertexColors(seq of vertexIds) -> self

        Removes colors from the specified vertices in all of the faces which
        share those vertices.
        """
    def renameUVSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renameUVSet(origName, newName, modifier=None) -> self

        Renames a UV set. The set must exist and the new name cannot be the
        same as that of an existing set.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """
    def setBinaryBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setBinaryBlindData(compId, compType, blindDataId, attr, data) -> self
        setBinaryBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'binary' blind data attribute
        on a single component of the mesh. The data must be a single string.

        The second version sets the value of a 'binary' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        strings then it must provide a value for each component in compIds.
        If it is a single string then all of the specified components will
        have their blind data set to that value.
        """
    def setBoolBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setBoolBlindData(compId, compType, blindDataId, attr, data) -> self
        setBoolBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'boolean' blind data attribute
        on a single component of the mesh. The data must be a single boolean.

        The second version sets the value of a 'boolean' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        booleans then it must provide a value for each component in compIds.
        If it is a single boolean then all of the specified components will
        have their blind data set to that value.
        """
    def setColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setColor(colorId, MColor, colorSet='', rep=kRGBA) -> self

        Sets a color in the specified colorSet. If no colorSet is given the
        current colorSet will be used. If the colorId is greater than or
        equal to numColors() then the colorSet will be grown to accommodate
        the specified color.
        """
    def setColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setColors(seq of MColor, colorSet='', rep=kRGBA) -> self

        Sets all the colors of the specified colorSet. If no colorSet is
        given the current colorSet will be used. After using this method to
        set the color values, you can call assignColors() to assign the
        corresponding color ids to the geometry.

        The color sequence must be at least as large as the current color set
        size. You can determine the color set size by calling numColors() for
        the default color set, or numColors(colorSet) for a named color set.
        If the sequence is larger than the color set size, then the color set
        for this mesh will be expanded to accommodate the new color values.

        In order to shrink the colorSet you have to clear its existing
        colors. E.g: clearColors(), setColors( ... ), assignColors()
        """
    def setCreaseEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCreaseEdges(edgeIds, seq of float) -> self


        Sets the specified edges of the mesh as crease edges.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned by
        Pixar(R).
        """
    def setCreaseVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCreaseVertices(edgeIds, seq of float) -> self


        Sets the specified edges of the mesh as crease edges.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned by
        Pixar(R).
        """
    def setCurrentColorSetName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCurrentColorSetName(colorSet, modifier=None, currentSelection=None) -> self

        Sets the 'current' color set for this object. The current color set
        is the one used when no color set name is specified for a color
        operation. If the specified color set does not exist then the current
        color set will not be changed.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.

        This method may change the current selection. If the 'currentSelection'
        (MSelectionList) parameter is provided then the current selection
        will be saved to it prior to the change. This is useful for
        supporting full undo of the change.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """
    def setCurrentUVSetName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCurrentUVSetName(uvSet, modifier=None, currentSelection=None) -> self

        Sets the 'current' uv set for this object. The current uv set is the
        one used when no uv set name is specified for a uv operation. If the
        specified uv set does not exist then the current uv set will not be
        changed.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.

        This method may change the current selection. If the 'currentSelection'
        (MSelectionList) parameter is provided then the current selection
        will be saved to it prior to the change. This is useful for
        supporting full undo of the change.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """
    def setDoubleBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDoubleBlindData(compId, compType, blindDataId, attr, data) -> self
        setDoubleBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'double' blind data attribute
        on a single component of the mesh. The data must be a single float.

        The second version sets the value of a 'double' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        floats then it must provide a value for each component in compIds.
        If it is a single float then all of the specified components will
        have their blind data set to that value.
        """
    def setEdgeSmoothing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setEdgeSmoothing(edgeId, smooth=True) -> self

        Sets the specified edge to be hard or smooth. You must use the
        cleanupEdgeSmoothing() method after all the desired edges on your
        mesh have had setEdgeSmoothing() done. Use the updateSurface() method
        to indicate the mesh needs to be redrawn.
        """
    def setEdgeSmoothings(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setEdgeSmoothings(edgeIds, smooths) -> self

        Sets the specified edges to be hard or smooth. You must use the
        cleanupEdgeSmoothing() method after all the desired edges on your
        mesh have had setEdgeSmoothings() done. Use the updateSurface() method
        to indicate the mesh needs to be redrawn.
        """
    def setFaceColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFaceColor(color, faceId, rep=kRGBA) -> self

        Sets the face-vertex color for all vertices on this face.
        """
    def setFaceColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFaceColors(colors, faceIds, rep=kRGBA) -> self

        Sets the colors of the specified faces. For each face in the faceIds
        sequence the corresponding color from the colors sequence will be
        applied to all of its vertices.
        """
    def setFaceVertexColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexColor(color, faceId, vertexId, modifier=None, rep=kRGBA) -> self

        Sets a face-specific normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
    def setFaceVertexColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexColors(colors, faceIds, vertexIds, modifier=None, rep=kRGBA) -> self

        Sets the colors of the specified face/vertex pairs.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
    def setFaceVertexNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexNormal(normal, faceId, vertexId, space=MSpace.kObject, modifier=None) -> self

        Sets a face-specific normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
    def setFaceVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexNormal(normals, faceIds, vertexIds, space=MSpace.kObject) -> self

        Sets normals for the given face/vertex pairs.
        """
    def setFloatBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFloatBlindData(compId, compType, blindDataId, attr, data) -> self
        setFloatBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'float' blind data attribute
        on a single component of the mesh. The data must be a single float.

        The second version sets the value of a 'float' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        floats then it must provide a value for each component in compIds.
        If it is a single float then all of the specified components will
        have their blind data set to that value.
        """
    def setIntBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIntBlindData(compId, compType, blindDataId, attr, data) -> self
        setIntBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'int' blind data attribute
        on a single component of the mesh. The data must be a single int.

        The second version sets the value of a 'int' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        ints then it must provide a value for each component in compIds.
        If it is a single int then all of the specified components will
        have their blind data set to that value.
        """
    def setInvisibleFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setInvisibleFaces(faceIds, makeVisible=False) -> self

        Sets the specified faces of the mesh to be visible or invisible. See
        the getInvisibleFaces() method for a description of invisible faces.
        """
    def setIsColorClamped(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIsColorClamped(colorSet, clamped) -> self

        Sets whether the color set's RGBA components should be clamped to the
        range 0 to 1.
        """
    def setNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setNormals(normals, space=MSpace.kObject) -> self

        Sets the mesh's normals (user normals).
        """
    def setPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(vertexId, MPoint, space=MSpace.kObject) -> self

        Sets the position of specified vertex.

        Note that if you modify the position of a vertex for a mesh node (as
        opposed to mesh data), a tweak will be created. If you have a node
        with no history, the first time that a tweak is created, the
        underlying pointers under the MFnMesh object may change. You will
        need to call syncObject() to make sure that the object is valid.
        Subsequent calls to setPoint() on the same object do not require a
        syncObject() call.
        """
    def setPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPoints(points, space=MSpace.kObject) -> self

        Sets the positions of the mesh's vertices. The positions may be
        given as a sequence of MFloatPoint's or a sequence of MPoint's, but
        not a mix of the two.
        """
    def setSmoothMeshDisplayOptions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSmoothMeshDisplayOptions(MMeshSmoothOptions) -> self

        Sets the options to use when smoothing the mesh for display.
        """
    def setSomeColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSomeColors(colorIds, colors, colorSet='', rep=kRGBA) -> self

        Sets specific colors in a colorSet.

        If the largest colorId in the sequence is larger than numColors()
        then the colorSet will be grown to accommodate the new color values.
        If you have added new colorIds, you can call assignColors to assign
        the colorIds to the geometry. If you are modifying existing colors,
        they will already be referenced by the existing mesh data.
        """
    def setSomeUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSomeUVs(uvIds, uValues, vValues, uvSet='') -> self

        Sets the specified texture coordinates (uv's) for this mesh. The uv
        value sequences and the uvIds sequence must all be of equal size. If
        the largest uvId in the array is larger than numUVs() then the uv
        list for this mesh will be grown to accommodate the new uv values.
        If a named uv set is given, the array will be grown when the largest
        uvId is larger than numUVs(uvSet).

        If you have added new uvIds, you must call one of the assignUV
        methods to assign the uvIds to the geometry. If you are modifying
        existing UVs, you do not need to call one of the assignUV methods.
        """
    def setStringBlindData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setStringBlindData(compId, compType, blindDataId, attr, data) -> self
        setStringBlindData(seq of compId, compType, blindDataId, attr, data) -> self

        The first version sets the value of a 'string' blind data attribute
        on a single component of the mesh. The data must be a single string.

        The second version sets the value of a 'string' blind data attribute
        on multiple components of the mesh. If the data is a sequence of
        strings then it must provide a value for each component in compIds.
        If it is a single string then all of the specified components will
        have their blind data set to that value.
        """
    def setUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUV(uvId, u, v, uvSet='') -> self

        Sets the specified texture coordinate.

        The uvId is the element in the uv list that will be set. If the uvId
        is greater than or equal to numUVs() then the uv list will be grown
        to accommodate the specified uv. If the UV being added is new, thenyou must call one of the assignUV methods in order to update the
        geometry.
        """
    def setUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUVs(uValues, vValues, uvSet='') -> self

        Sets all of the texture coordinates (uv's) for this mesh. The uv
        value sequences must be of equal size and must be at least as large
        as the current UV set size. You can determine the UV set size by
        calling numUVs() for the default UV set, or numUVs(uvSet) for a
        named UV set.

        If the sequences are larger than the UV set size, then the uv list
        for this mesh will be grown to accommodate the new uv values.

        After using this method to set the UV values, you must call one of
        the assignUV methods to assign the corresponding UV ids to the
        geometry.

        In order to shrink the uvs array, do the following: clearUVs(),
        setUVs(...), assignUVs(). These steps will let you to create an
        array of uvs which is smaller than the original one.
        """
    def setVertexColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setVertexColor(color, vertexId, modifier=None, rep=kRGBA) -> self

        Sets the color for a vertex in all the faces which share it.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
    def setVertexColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setVertexColors(colors, vertexIds, modifier=None, rep=kRGBA) -> self

        Sets the colors of the specified vertices. For each vertex in the
        vertexIds sequence, the corresponding color from the colors sequence
        will be applied to the vertex in all of the faces which share it.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
    def setVertexNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setVertexNormal(normal, vertexId, space=MSpace.kObject, modifier=None) -> self

        Sets the shared normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """
    def setVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setVertexNormal(normals, vertexIds, space=MSpace.kObject) -> self

        Sets the shared normals for the given vertices.
        """
    def sortIntersectionFaceTriIds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sortIntersectionFaceTriIds(faceIds, triIds=none) -> self

        Convenience routine for sorting faceIds or face/triangle ids before
        passing them into the closestIntersection(), allIntersections(), or
        anyIntersection() methods. When using an acceleration structure with
        an intersection operation it is essential that any faceId or
        faceId/triId arrays be sorted properly to ensure optimal performance.

        Both arguments must be MIntArray's.
        """
    def split(self: Self, *args: Any, **kwargs: Any) -> Any:
        """split(((kOnEdge, int, float), (kInternalPoint, MFloatPoint), ...)) -> self

        Each tuple in the placements sequence consists of a Split Placement
        constant followed by one or two parameters.

        If the Split Placement is kOnEdge then the tuple will contain two
        more elements giving the int id of the edge to split, and a float
        value between 0 and 1 indicating how far along the edge to do the
        split. The same edge cannot be split more than once per call.

        If the Split Placement is kInternalPoint then the tuple will contain
        just one more element giving an MFloatPoint within the face.

        All splits must begin and end on an edge meaning that the first and
        last tuples in the placements sequence must be kOnEdge placements.
        """
    def subdivideEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """subdivideEdges(edges, numDivisions) -> self

        Subdivides edges at regular intervals. For example, if numDivisions
        is 2 then two equally-spaced vertices will be added to each of the
        specified edges: one 1/3 of the way along the edge and a second 2/3
        of the way along the edge.
        """
    def subdivideFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """subdivideFaces(faces, numDivisions) -> self

        Subdivides each specified face into a grid of smaller faces.
        Triangles are subdivided into a grid of smaller triangles and quads
        are subdivided into a grid of smaller quads. Faces with more than
        four edges are ignored.

        The numDivisions parameter tells how many times to subdivide each
        edge of the face. Internal points and edges are introduced as needed
        to create a grid of smaller faces.
        """
    def syncObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """syncObject() -> self

        If a non-api operation happens that many have changed the
        underlying Maya object attached to this functionset, calling this
        method will make sure that the functionset picks up those changes.
        In particular this call should be used after calling mel commands
        which might affect the mesh. Note that this only applies when the
        functionset is attached to a mesh node. If it's attached to mesh
        data the it is not necessary to call this method.
        """
    def uniformGridParams(self: Self, *args: Any, **kwargs: Any) -> Any:
        """uniformGridParams(xDiv, yDiv, zDiv) -> MMeshIsectAccelParams

        Creates an object which specifies a uniform voxel grid structure
        which can be used by the intersection routines to speed up their
        operation. This object specifies the number of voxel cells to be
        used in the x, y, and z dimensions. The grid acceleration structure
        will be cached with the mesh, so that if the same MMeshIsectAccelParams
        configuration is used on the next intersect call, the acceleration
        structure will not need to be rebuilt.
        """
    def unlockFaceVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unlockFaceVertexNormals(seq of faceIds, seq of vertIds) -> self

        Unlocks the normals for the given face/vertex pairs.
        """
    def unlockVertexNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unlockVertexNormals(sequence of vertIds) -> self

        Unlocks the shared normals for the specified vertices.
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signal that this polygonal mesh has changed and needs to be redrawn.
        """

class MFnMeshData(MFnGeometryData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new mesh data object, attaches it to this function set
        and returns an MObject which references it.
        """

class MFnMessageAttribute(MFnAttribute):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new message attribute, attaches it to the function set and returns it as an MObject."""

class MFnNumericAttribute(MFnAttribute):
    def child(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the specified child attribute of the parent attribute currently attached to the function set."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new simple or compound numeric attribute, attaches it to the function set and returns it in an MObject."""
    def createAddr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new address attribute, attaches it to the function set and returns it in an MObject."""
    def createColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new color attribute, attaches it to the function set and returns it in an MObject."""
    def createPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new 3D point attribute, attaches it to the function set and returns it in an MObject."""
    @property
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    @default.setter
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    def getMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard maximum value(s)."""
    def getMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard minimum value(s)."""
    def getSoftMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft maximum value."""
    def getSoftMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft minimum value."""
    def hasMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a hard maximum value has been specified for the attribute."""
    def hasMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a hard minimum value has been specified for the attribute."""
    def hasSoftMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a soft maximum value has been specified for the attribute."""
    def hasSoftMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a soft minimum value has been specified for the attribute."""
    def numericType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the numeric type of the attribute currently attached to the function set."""
    def setMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard maximum value(s)."""
    def setMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard minimum value(s)."""
    def setSoftMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft maximum value."""
    def setSoftMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft minimum value."""

class MFnNumericData(MFnData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new numeric data object."""
    def getData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the attached data object's data."""
    def numericType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of data in the attached data object."""
    def setData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the data in the attached data object."""

class MFnNurbsCurve(MFnDagNode):
    def area(self: Self, *args: Any, **kwargs: Any) -> Any:
        """area(tolerance=kPointTolerance) -> float

        Returns the area bounded by the curve. The curve must be closed and
        planar. A value of 0.0 will be returned if area cannot be determined.

        * tolerance (float) - Amount of error allowed in the calculation
        """
    def closestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """closestPoint(testPoint, guess=None, tolerance=kPointTolerance,
            space=kObject) -> (MPoint, float)

        Returns a tuple containing the point on the curve which is closest
        to 'testPoint', and the parameter value at which that point occurs.

        * testPoint (MPoint) - point to get closest to
        * guess      (float) - a guess as to roughly where on the curve the
                               closest point will be. If the guess is in the
                               correct span than it can significantly speed
                               up the search. If not then it may slow down
                               the search a bit. If no guess is supplied
                               then the search will begin at the start of
                               the curve.
        * tolerance  (float) - maximum allowed distance between the curve
                               and the returned point.
        * space (MSpace constant) - coordinate space to use for the points
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source, parent=MObject.kNullObj) -> MObject

        Returns a new NURBS curve which is a copy of 'source' and resets
        the functionset to operate on it.

        * parent (MObject)
                     - the parent/owner of the new curve. If it's a NURBS
                       curve data wrapper (MFn.kNurbsCurveData) then the
                       created curve will be returned as a geometry object
                       (MFn.kNurbsCurveGeom) owned by the wrapper. If
                       'parent' is a DAG node then the new curve will be
                       returned as nurbsCurve node parented under it. If
                       'parent' is not provided then a new top-level
                       transform will be created with the new curve parented
                       beneath it as a nurbsCurve node. In this last case it
                       will be the transform node which is returned.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(cvs, knots, degree, form, is2D, rational, parent=kNullObj)
            -> self
        create(subCurves, parent=kNullObj) -> self

        Returns a newly created curve and resets the functionset to operate
        on it. The first version creates the curve based on the control
        vertices and knots provided while the second creates the curve as a
        copy of the provided subCurves, all joined together.

        * cvs (MPointArray or seq of MPoint)
                     - positions of the control vertices
        * knots (MDoubleArray seq of float)
                     - parameter values of the knots. There must be
                       (# spans + 2*degree - 1) knots provided and they must
                       appear in non-decreasing order.
        * degree (int) - degree of the curve to create
        * form (int) - one of kOpen, kClosed or kPeriodic
        * is2d (bool)- if True the Z-coordinates of 'cvs' will be ignored,
                       giving a curve in the local XY plane.
        * rational (bool)
                     - set True if you want the new curve to be rational
        * parent (MObject)
                     - the parent/owner of the new curve. If it's a NURBS
                       curve data wrapper (MFn.kNurbsCurveData) then the
                       created curve will be returned as a geometry object
                       (MFn.kNurbsCurveGeom) owned by the wrapper. If
                       'parent' is a DAG node then the new curve will be
                       returned as nurbsCurve node parented under it. If
                       'parent' is not provided then a new top-level
                       transform will be created with the new curve parented
                       beneath it as a nurbsCurve node. In this last case it
                       will be the transform node which is returned.
        * subCurves (MObjectArray or seq of MObject)
                     - array of curves from which the new curve will be built
                       The curves must all be in the same direction, must not
                       intersect themselves or each other, the start of each
                       curve in the array must be coincident with the end of
                       the previous curve in the array, and the curves must be
                       be at least C0 continuous (i.e. tangent breaks are okay).
        """
    def createWithEditPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createWithEditPoints(eps, degree, form, is2D, rational, uniform,
            parent=kNullObj) -> MObject

        Returns a new curve based on the given edit points (i.e. points
        which lie on the curve) and resets the functionset to operate on it.

        * eps (MPointArray or seq of MPoint)
                     - positions of the edit points
        * degree (int) - degree of the curve to create
        * form (int) - one of kOpen, kClosed or kPeriodic
        * is2d (bool)- if True the Z-coordinates of 'eps' will be ignored,
                       giving a curve in the local XY plane.
        * rational (bool)
                     - set True if you want the new curve to be rational
        * uniform (bool)
                     - if True then parameter values of the knots will be
                       uniformly spaced, otherwise they will be based on
                       chord length.
        * parent (MObject)
                     - the parent/owner of the new curve. If it's a NURBS
                       curve data wrapper (MFn.kNurbsCurveData) then the
                       created curve will be returned as a geometry object
                       (MFn.kNurbsCurveGeom) owned by the wrapper. If
                       'parent' is a DAG node then the new curve will be
                       returned as nurbsCurve node parented under it. If
                       'parent' is not provided then a new top-level
                       transform will be created with the new curve parented
                       beneath it as a nurbsCurve node. In this last case it
                       will be the transform node which is returned.
        """
    def cvPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvPosition(index, space=kObject) -> MPoint

        Returns the position of a single control vertex.

        * index (int) - index of the CV to return
        * space (int) - an MSpace constant giving the coordinate space in
                        which the point is given
        """
    def cvPositions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvPositions(space=kObject) -> MPointArray

        Returns the positions of all of the curve's control vertices.

        * space (int) - an MSpace constant giving the coordinate space in
                        which the point is given
        """
    def cvs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvs(startIndex[, endIndex]) -> MObject

        Returns a CV or a range of CVs as a component. MItCurveCV can be
        used to examine or modify the CVs in the component. Any modifications
        made to them will affect the curve. After all modifications are done,
        updateCurve() should be called to have the curve recalculate its
        cached geometry.

        * startIndex (int) - start of the range of CVs to return.
        * endIndex   (int) - end of the range of CVs to return. If not
                             provided then only the CV specified by
                             startIndex will be returned.
        """
    @property
    def degree(*args: Any, **kwargs: Any) -> Any:
        """The degree of the curve or 0 if the degree cannot be determined."""
    @degree.setter
    def degree(*args: Any, **kwargs: Any) -> Any:
        """The degree of the curve or 0 if the degree cannot be determined."""
    def distanceToPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """distanceToPoint(point, space=kObject) -> float

        Returns the distance from the given point to the point on the curve
        which is closest to it.

        * point (MPoint) - the point to calculate the distance to
        * space (int)    - an MSpace constant giving the coordinate space in
                           which the point is given
        """
    def findLengthFromParam(self: Self, *args: Any, **kwargs: Any) -> Any:
        """findLengthFromParam(param) -> float

        Returns the length along the curve corresponding to a given
        parameter value on the curve. If the length cannot be found for
        the given parameter value then a length of zero is returned.

        * param (float) - parameter value on the curve
        """
    def findParamFromLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """findParamFromLength(length, tolerance=kFindParamTolerance) -> float

        Returns the parameter value corresponding to a given length along
        the curve. If the parameter value cannot be determined then the value
        for the end point of the curve is returned.

        * length (float) - distance along the curve
        * tolerance (float) - search tolerance
        """
    @property
    def form(*args: Any, **kwargs: Any) -> Any:
        """The form of the curve: kOpen, kClosed, kPeriodic or kInvalid"""
    @form.setter
    def form(*args: Any, **kwargs: Any) -> Any:
        """The form of the curve: kOpen, kClosed, kPeriodic or kInvalid"""
    def getDerivativesAtParam(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDerivativesAtParam(param, space=kObject) -> (MPoint, MVector[, MVector])

        Evaluates the curve at the given parameter value, returning a tuple
        containing the position and first derivative at that value. If 'dUU'
        is True then the returned tuple will include the second derivative
        as well as its third element.

        * param (float) - parameter value at which to do the evaluation
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the point is given
        * dUU    (bool) - if True include the second derivative in the result.
        """
    def getParamAtPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParamAtPoint(point, tolerance=kPointTolerance, space=kObject) -> float

        Returns the parameter value corresponding to the given point on the
        curve.

        * point    (MPoint) - point on curve.
        * tolerance (float) - max distance 'point' can be from the curve and
                              still be considered to lie on it.
        * space       (int) - an MSpace constant giving the coordinate space
                              in which the point is given
        """
    def getPointAtParam(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtParam(param, space=kObject) -> MPoint

        Returns the point on the curve at the given parameter value.

        * param (float) - parameter value at which to find the point
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the point should be returned
        """
    @property
    def hasHistoryOnCreate(*args: Any, **kwargs: Any) -> Any:
        """True if the curve was created with history."""
    @hasHistoryOnCreate.setter
    def hasHistoryOnCreate(*args: Any, **kwargs: Any) -> Any:
        """True if the curve was created with history."""
    def isParamOnCurve(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isParamOnCurve(param) -> bool

        Returns True if the given parameter value lies on the curve (i.e. is
        within the curve's knot domain), False otherwise.

        * param (float) - parameter value to test
        """
    @property
    def isPlanar(*args: Any, **kwargs: Any) -> Any:
        """True if the curve is planar."""
    @isPlanar.setter
    def isPlanar(*args: Any, **kwargs: Any) -> Any:
        """True if the curve is planar."""
    def isPointOnCurve(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPointOnCurve(point, tolerance=kPointTolerance, space=kObject) -> bool

        Returns True if the given point lies on the curve, False otherwise.

        * point    (MPoint) - point to test.
        * tolerance (float) - max distance 'point' can be from the curve and
                              still be considered to lie on it.
        * space       (int) - an MSpace constant giving the coordinate space
                              in which the point is given
        """
    kFindParamTolerance: float = ...
    kPointTolerance: float = ...

    def knot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """knot(index) -> float

        Returns the parameter value of a single knot.

        * index (int) - index of the knot to return. These range from 0 to
                        (numKnots - 1)
        """
    @property
    def knotDomain(*args: Any, **kwargs: Any) -> Any:
        """A tuple containing a pair of floats corresponding to the maximum and
        minimum parameter values for this curve.
        """
    @knotDomain.setter
    def knotDomain(*args: Any, **kwargs: Any) -> Any:
        """A tuple containing a pair of floats corresponding to the maximum and
        minimum parameter values for this curve.
        """
    def knots(self: Self, *args: Any, **kwargs: Any) -> Any:
        """knots() -> MDoubleArray

        Returns the parameter values for all of the curve's knots.
        """
    def length(self: Self, *args: Any, **kwargs: Any) -> Any:
        """length(tolerance=kPointTolerance) -> float

        Returns the arc length of this curve or 0.0 if it cannot be computed.

        * tolerance (float) - max error allowed in the calculation.
        """
    def makeMultipleEndKnots(self: Self, *args: Any, **kwargs: Any) -> Any:
        """makeMultipleEndKnots() -> self

        Sets the curve's end knots to have full multiplicity. This ensures
        that the end points interpolate the first and last CVs (i.e. lie
        directly on them). It can also be used to convert a periodic curve
        to a closed curve.
        """
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """normal(param, space=kObject) -> MVector

        Returns the normal at the given parameter value on the curve. For
        degree 1 curves the normal is the vector at right angles to the
        curve that lies in the average plane of the curve. For higher degrees
        the normal is defined by the local curvature at the parameter.

        * param (float) - parameter value at which to find the normal
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the normal should be returned
        """
    @property
    def numCVs(*args: Any, **kwargs: Any) -> Any:
        """Number of CVs in the curve or 0 if the number of CVs cannot be
        determined.
        """
    @numCVs.setter
    def numCVs(*args: Any, **kwargs: Any) -> Any:
        """Number of CVs in the curve or 0 if the number of CVs cannot be
        determined.
        """
    @property
    def numKnots(*args: Any, **kwargs: Any) -> Any:
        """Number of knots in the curve or 0 if the number of knots cannot be
        determined.
        """
    @numKnots.setter
    def numKnots(*args: Any, **kwargs: Any) -> Any:
        """Number of knots in the curve or 0 if the number of knots cannot be
        determined.
        """
    @property
    def numSpans(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the curve or 0 if the number of spans cannot be
        determined.
        """
    @numSpans.setter
    def numSpans(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the curve or 0 if the number of spans cannot be
        determined.
        """
    @property
    def planeNormal(*args: Any, **kwargs: Any) -> Any:
        """MVector of the normal to the plane of the curve, if the curve is
        planar, or None if the curve is not planar.
        """
    @planeNormal.setter
    def planeNormal(*args: Any, **kwargs: Any) -> Any:
        """MVector of the normal to the plane of the curve, if the curve is
        planar, or None if the curve is not planar.
        """
    def removeKnot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeKnot(param, removeAll=False) -> self

        Removes one or more knots at the given parameter value.

        If there are multiple knots at the parameter value then 'removeAll'
        determines which ones will be removed. If it is True then they will
        all be removed. If it is False then all but one will be removed.

        * param     (float) - parameter of the knot
        * removeAll  (bool) - how to handle multiple knots at the same param
        """
    def reverse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reverse() -> self

        Reverses the direction of the curve.
        """
    def setCVPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCVPosition(index, point, space=kObject) -> self

        Sets the position of a single control vertex of the curve.

        * index    (int) - index of the cv
        * point (MPoint) - new position for the cv
        * space    (int) - an MSpace constant giving the coordinate space
                           in which the point is given
        """
    def setCVPositions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCVPositions(points, space=kObject) -> self

        Sets the positions of all of the curve's control vertices.

        * points (MPointArray or seq of MPoint)
                       - the points to be set. The array/sequence must
                         contain exactly the same number of points as the
                         curve has control vertices.
        * space  (int) - an MSpace constant giving the coordinate space
                         in which the points are given
        """
    def setKnot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setKnot(index, param) -> self

        Sets the parameter value of a single knot.
        * index   (int) - index of the knot
        * param (float) - new parameter value for the knot
        """
    def setKnots(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setKnots(params, startIndex, endIndex) -> self

        Sets the parameter values of a contiguous group of knots.

        * params (MDoubleArray of seq of float)
                           - the parameter values to set, one per knot in
                             the range
        * startIndex (int) - first knot in the range to be set
        * endIndex   (int) - last knot in the range to be set
        """
    def tangent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """tangent(param, space=kObject) -> MVector

        Returns the normalized tangent vector at the given parameter value
        on the curve.

        * param (float) - parameter value at which to find the tangent
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the tangent should be returned
        """
    def updateCurve(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateCurve() -> self

        Tells the shape node which represents the curve in the scene, if
        any, that the curve has changed and needs to be redrawn.
        """

class MFnNurbsCurveData(MFnGeometryData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new nurbs curve data object, attaches it to this function set
        and returns an MObject which references it.
        """

class MFnNurbsSurface(MFnDagNode):
    def area(self: Self, *args: Any, **kwargs: Any) -> Any:
        """area(space=kObject, tolerance=kPointTolerance) -> float

        Returns the surface's area, or 0.0 if the area cannot be determined.
        """
    def assignUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assignUV(patchId, cornerIndex, uvId) -> self

        Maps a texture coordinate (uv) to a the specified corner of a patch.

        Note that API methods that modify uv data will work correctly when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * patchId     (int) - Patch to map to.
        * cornerIndex (int) - Corner of the patch to map to.
        * uvId        (int) - Index into the uv list of the UV to map.
        """
    def assignUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assignUVs(uvCounts, uvIds) -> self

        Maps all texture coordinates for the surface. setUV() and setUVs()
        are used to create the texture coordinate table for the surface.
        After the table is created, this method is used to map those values
        to each patch on a per-corner basis.

        The uvCounts array should contain the number of uvs per patch.
        Since uvs are mapped per-patch per-corner, the entries in this array
        should match the corner counts for each patch in the surface.
        If an entry in this array is '0' then the corresponding patch will
        not be mapped.

        The sum of all the entries in the uvCounts array must be equal to
        the size of the uvIds array or this method will fail.

        The uvIds array should contain the UV indices that will be mapped to
        each patch-corner in the surface. The entries in this array specify
        which uvs in the surface's uv table are mapped to each patch-corner.
        Each entry in the uvIds array must be less than numUVs().
        The size of the uvIds array is equivalent to adding up all of the
        entries in the uvCounts array, so for a cube with all patches mapped
        there would be 24 entries.

        Note that API methods that modify uv data will work correctly when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * uvCounts (MIntArray or seq of int)
                     - UV counts for each patch in the surface.
        * uvIds    (MIntArray or seq of int)
                     - UV indices to be mapped to each patch-corner.
        """
    def boundaryType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """boundaryType(region, boundary) -> int

        Returns the type of the specified boundary. The surface must be a
        trimmed surface. Valid boundary types are:

            kInner           - an inner (clockwise) boundary
            kOuter           - an outser (counter clockwise) boundary
            kSegment         - a curve on a patch
            kClosedSegment   - a closed curve on a patch
            kInvalidBoundary - an invalid boundary type

        * region (int)   - Region containing the boundary
        * boundary (int) - Index of the boundary within the region.
        """
    def clearUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearUVs() -> self

        Clears out all texture coordinates for the nurbsSurface, and leaves
        behind an empty UVset.

        This method should be used if it is needed to shrink the size of the
        UV table. In this case, the user should call clearUVs, setUVs and
        then assignUVs to rebuild the mapping info.

        When called on a dataNurbsSurface the UVs are removed. When called
        on a shape with no history, the UVs are removed and the attributes
        are set on the shape. When called on a shape with history, the
        polyDelMap command is invoked and a polyMapDel node is created.
        """
    def closestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """closestPoint(testPoint, uStart=None, vStart=None,
            ignoreTrimBoundaries=False, tolerance=kPointTolerance,
            space=kObject) -> (MPoint, float, float)

        Returns the closest point on the surface to the specified test point
        The return value is a tuple containing the position of the point and
        and its U and V texture parameters.

        Performance can be greatly increased by supplying starting U and V
        parameter values which are reasonably close to the final point.
        Specifying these values will invoke a special algorithm which will
        begin to search for the closest point at the given parameter value,
        and will check the local surface to see which direction will bring
        it closer to the given point. It then offsets in this direction and
        repeats the process, iteratively traversing the surface until it
        finds the closest point.
        This algorithm will fail if it encounters a seam before reaching
        the closest point, or if it finds a local closest point, such as a
        bulge on a mesh where an offset in any direction will take it
        further from the given point, even if that is not the true closest
        point on the mesh. For this reason it is advisable to avoid using
        this option unless absolutely sure that the initial point will be
        a good enough approximation to the final point that these
        conditions will not occur.

        * testPoint (MPoint) - Position of the point to be checked
        * uStart     (float) - Initial guess of a U parameter near where the
                               where the closest point is expected to be.
        * vStart     (float) - Initial guess of a V parameter near where the
                               where the closest point is expected to be.
        * ignoreTrimBoundaries (bool)
                             - For trimmed surfaces, if this is true the
                               trim curves will be ignored and the entire
                               untrimmed surface searched.
        * tolerance  (float) - How close to the surface must a point be to
                               be considered 'on' the surface.
        * space        (int) - an MSpace constant giving the coordinate
                               space which 'testPoint' is in. The returned
                               point will be in the same space.
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source, parent=kNullObj) -> MObject

        Returns a new NURBS surface, which is a copy of the source surface,
        and sets the functionset to operate on it.

        * source (MObject)- The surface to copy.
        * parent (MObject)- The parent/owner of the new surface. If it's a
                            NURBS surface data wrapper (MFn.kNurbsSurfaceData)
                            then the created surface will be returned as a
                            geometry object (MFn.kNurbsSurfaceGeom) owned by
                            the wrapper. If 'parent' is a DAG node then the
                            new surface will be returned as nurbsSurface node
                            parented under it. If 'parent' is not provided
                            then a new top-level transform will be created
                            with the new surface parented beneath it as a
                            nurbsSurface node. In this last case it will be
                            the transform node which is returned.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(cvs, uKnots, vKnots, uDegree, vDegree, uForm, vForm,
            rational, parent=kNullObj) -> MObject

        Returns a new NURBS surface created from the specified data and sets
        the function set to operate on it.

        * cvs (MPointArray or seq of MPoint)
                          - The control vertices.
        * uKnots (MDoubleArray or seq of float)
                          - Parameter values for the knots in the U direction.
        * vKnots (MDoubleArray or seq of float)
                          - Parameter values for the knots in the V direction.
        * uDegree   (int) - Degree of the basis functions in the U direction.
        * vDegree   (int) - Degree of the basis functions in the V direction.
        * uForm     (int) - A Form constant (kOpen, kClosed, kPeriodic) giving
                            the surface's form in the U direction.
        * vForm     (int) - A Form constant (kOpen, kClosed, kPeriodic) giving
                            the surface's form in the V direction.
        * rational (bool) - Create as rational (True) or non-rational (False)
                            surface.
        * parent (MObject)- The parent/owner of the new surface. If it's a
                            NURBS surface data wrapper (MFn.kNurbsSurfaceData)
                            then the created surface will be returned as a
                            geometry object (MFn.kNurbsSurfaceGeom) owned by
                            the wrapper. If 'parent' is a DAG node then the
                            new surface will be returned as nurbsSurface node
                            parented under it. If 'parent' is not provided
                            then a new top-level transform will be created
                            with the new surface parented beneath it as a
                            nurbsSurface node. In this last case it will be
                            the transform node which is returned.
        """
    def cv(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cv(uIndex, vIndex) -> MObject

        Returns a component for the specified control vertex.

        * uIndex (int) - U index of the CV.
        * vIndex (int) - V index of the CV.
        """
    def cvPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvPosition(uIndex, vIndex, space=kObject) -> MPoint

        Returns the position of the specified control vertex.

        * uIndex (int) - U index of the CV.
        * vIndex (int) - V index of the CV.
        * space  (int) - an MSpace constant giving the coordinate
                         space which the point should be returned.
        """
    def cvPositions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvPositions(space=kObject) -> MPointArray

        Returns the positions of all the surface's control vertices.

        * space  (int) - an MSpace constant giving the coordinate
                         space which the points should be returned.
        """
    def cvsInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvsInU(startUIndex, endUIndex, vIndex) -> MObject

        Returns a component for a set of control vertices in the U direction.

        * startUIndex (int) - U index of the first CV to return.
        * endUIndex   (int) - U index of the last CV to return.
        * vIndex      (int) - V index for all of the returned CVs.
        """
    def cvsInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cvsInV(startVIndex, endVIndex, uIndex) -> MObject

        Returns a component for a set of control vertices in the V direction.

        * startVIndex (int) - V index of the first CV to return.
        * endVIndex   (int) - V index of the last CV to return.
        * uIndex      (int) - U index for all of the returned CVs.
        """
    @property
    def dataObject(*args: Any, **kwargs: Any) -> Any:
        """If the functionset was created using an MFn.kNurbsSurfaceData object
        then this attribute will contain an MObject which references that
        data object. Otherwise it will contain MObject.kNullObj.
        """
    @dataObject.setter
    def dataObject(*args: Any, **kwargs: Any) -> Any:
        """If the functionset was created using an MFn.kNurbsSurfaceData object
        then this attribute will contain an MObject which references that
        data object. Otherwise it will contain MObject.kNullObj.
        """
    @property
    def degreeInU(*args: Any, **kwargs: Any) -> Any:
        """The degree of the surface in the U direction or 0 if the degree
        cannot be determined.
        """
    @degreeInU.setter
    def degreeInU(*args: Any, **kwargs: Any) -> Any:
        """The degree of the surface in the U direction or 0 if the degree
        cannot be determined.
        """
    @property
    def degreeInV(*args: Any, **kwargs: Any) -> Any:
        """The degree of the surface in the V direction or 0 if the degree
        cannot be determined.
        """
    @degreeInV.setter
    def degreeInV(*args: Any, **kwargs: Any) -> Any:
        """The degree of the surface in the V direction or 0 if the degree
        cannot be determined.
        """
    def distanceToPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """distanceToPoint(point, space=kObject) -> float

        Returns the distance from the given point to the closest point on
        the surface.

        * point (MPoint) - Point to calculate distance to.
        * space  (int)   - An MSpace constant giving the coordinate space in
                           which the point has been specified.
        """
    def edge(self: Self, *args: Any, **kwargs: Any) -> Any:
        """edge(region, boundary, edge, paramEdge=False) -> MObjectArray

        Return the specified edge of a trim boundary.

        For each region of a trimmed surface there may be several boundary
        curves: an outer curve and possibly several inner boundary curves
        (which define holes). These boundary curves are made up of one or
        more curves called edges.

        The edge is returned as an MObjectArray as it may consist of more
        than one curve. The returned edge, or trim curve, can be a 2D parameter
        edge or a 3D edge curve. Note that for closed surfaces some of the
        3d edges may be 0 length in which case an empty MObjectArray is
        returned. An example of this is the poles of a sphere.

        * region     (int) - Index of trimmed region containing the edge.
        * boundary   (int) - Index of boundary within trimmed region.
        * edge       (int) - Index of the edge within the boundary.
        * paramEdge (bool) - If True a 2D parameter edge is returned,
                             otherwise a 3D edge is returned.
        """
    @property
    def formInU(*args: Any, **kwargs: Any) -> Any:
        """Form of the surface in the U direction. Can be one of kOpen,
        kClosed, kPeriodic or kInvalid.
        """
    @formInU.setter
    def formInU(*args: Any, **kwargs: Any) -> Any:
        """Form of the surface in the U direction. Can be one of kOpen,
        kClosed, kPeriodic or kInvalid.
        """
    @property
    def formInV(*args: Any, **kwargs: Any) -> Any:
        """Form of the surface in the V direction. Can be one of kOpen,
        kClosed, kPeriodic or kInvalid.
        """
    @formInV.setter
    def formInV(*args: Any, **kwargs: Any) -> Any:
        """Form of the surface in the V direction. Can be one of kOpen,
        kClosed, kPeriodic or kInvalid.
        """
    def getAssignedUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAssignedUVs() -> (MIntArray, MIntArray)

        Returns the indices of all UVs which have been mapped to the surface.
        The return value is a tuple with an array containing the number
        of UVs for each patch in the surface, and a second array containing
        the indices of the UVs mapped to each corner of those patches. This
        is the same format as the arrays taken by the assignUVs() method.
        """
    def getConnectedShaders(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedShaders(instanceNumber) -> (MObjectArray, MIntArray)

        Returns a tuple containing an array of all the shaders (sets)
        connected to the specified instance of this surface, and an array of
        patch/shader assignments. The second array will hold, for each patch
        in the surface, an index into the first array. If a patch does not
        have a shader assigned to it, the value of the index will be -1.
        The shader objects can be derived from the sets returned.

        Note: This method will only work with a MFnNurbsSurface function set
              which has been initialized with an MFn::kNurbsSurface.

        See also getConnectedSetsAndMembers.

        * instanceNumber (int) - Determines which instance of the surface to
                                 query. This will be zero if there is only
                                 one instance.
        """
    def getDerivativesAtParam(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDerivativesAtParam(uParam, vParam, space=kObject, secondOrder=False)
            -> (MPoint, MVector, MVector)
            -> (MPoint, MVector, MVector, MVector, MVector, MVector)

        Evaluates the surface at the given (u,v) coordinates, returning a
        tuple containing the position at that point, the first derivative
        vector in U, and the first derivative vector in V. If 'secondOrder'
        is True then the tuple will also contain three additional vectors:
        the second order partial derivative with respect to U (dUU), the
        second order partial derivative with respect to V (dVV), and the
        second order partial derivative with respect to U then V (dUV).
        None of the vectors will be normalized.

        * uParam (float) - U parameter value at which to do the evaluation.
        * vParam (float) - V parameter value at which to do the evaluation.
        * space    (int) - An MSpace constant giving the coordinate space in
                           which to perform the calculation.
        * secondOrder (bool)
                         - If True, second order derivatives will be included
                           in the result. Note that this will increase
                           computation time.
        """
    def getParamAtPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getParamAtPoint(point, ignoreTrimBoundaries, tolerance=kPointTolerance,
            space=kObject) -> (float, float)

        Returns a tuple containing the parameter values corresponding to the
        given point on the surface (or underlying surface).

        * point    (MPoint) - Location of the parameter to obtain.
        * ignoreTrimBoundaries (bool)
                            - For trimmed surfaces, if this is true the
                              trim curves will be ignored and the entire
                              untrimmed surface searched.
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation.
        """
    def getPatchUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPatchUV(patchId, cornerIndex) -> (float, float)

        Returns a tuple containing the texture texture coordinate for a
        corner of a patch. Since texture coordinates (UVs) are stored
        per-patch per-corner you must specify both the patch and the corner
        that the u and v values are mapped to.
        * patchId (int)     - Patch of interest.
        * cornerIndex (int) - Corner of interest.
        """
    def getPatchUVid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPatchUVid(patchId, cornerIndex) -> int

        Returns the id of the texture coordinate for a single corner of a patch.

        * patchId (int)     - Patch of interest.
        * cornerIndex (int) - Corner of interest.
        """
    def getPatchUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPatchUVs(patchId) -> (MFloatArray, MFloatArray)

        Returns a tuple containing the values of the texture coordinates on
        all corners of the specified patch. The tuple contains an array of U
        coordinates and an array of V coordinates, both the same length.

        * patchId (int)     - Patch of interest.
        """
    def getPointAtParam(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtParam(uParam, vParam, space=kObject) -> MPoint"""
    def getUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvId) -> (float, float)

        Returns a tuple containing the U and V values for the a texture coordinate

        * uvId (int) - Id of the texture coordinate of intest.
        """
    def getUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVs() -> (MFloatArray, MFloatArray)

        Returns all of the surface's texture coordinates as a tuple containing
        an array of U values and an array of V values.
        """
    @property
    def hasHistoryOnCreate(*args: Any, **kwargs: Any) -> Any:
        """True if the surface was created with history."""
    @hasHistoryOnCreate.setter
    def hasHistoryOnCreate(*args: Any, **kwargs: Any) -> Any:
        """True if the surface was created with history."""
    def intersect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """intersect(rayStart, rayDir, tolerance=kPointTolerance, space=kObject,
            distance=False, exactHit=False, all=False)
            -> (MPoint, float, float[, float][, bool])
            -> (MPointArray, MDoubleArray, MDoubleArray[, MDoubleArray][, bool])
            -> None

        Returns the closest point of intersection of a ray with the surface
        as a tuple containing the point of intersection and the U and V
        parameters at that point.
        * rayStart (MPoint) - Starting point for the ray.
        * rayDir  (MVector) - Direction of the ray
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation.* distance   (bool) - If True the distance from 'rayStart' to the
                              point of intersection will be appended to the
                              returned tuple.
        * exactHit   (bool) - If True then a boolean value indicating if the
                              point of intersection was an exact hit will be
                              appended to the returned tuple.
        * all        (bool) - If True then all points of intersection will
                              be returned. In this case the point of
                              intersection, U and V parameters, and distance
                              (if requested) will all be returned as arrays.
        """
    @property
    def isBezier(*args: Any, **kwargs: Any) -> Any:
        """True if the knot spacing gives a Bezier surface."""
    @isBezier.setter
    def isBezier(*args: Any, **kwargs: Any) -> Any:
        """True if the knot spacing gives a Bezier surface."""
    def isFlipNorm(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isFlipNorm(region) -> bool

        Checks whether the normal for the specified region is flipped
        This method is only valid for trimmed surfaces.

        region (int) - Region to check.
        """
    @property
    def isFoldedOnBispan(*args: Any, **kwargs: Any) -> Any:
        """True if surface contains are any folds or creases on bispan
        boundaries, including trimmed regions.
        """
    @isFoldedOnBispan.setter
    def isFoldedOnBispan(*args: Any, **kwargs: Any) -> Any:
        """True if surface contains are any folds or creases on bispan
        boundaries, including trimmed regions.
        """
    def isKnotU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isKnotU(param) -> bool

        Checks if the specified parameter value is a knot value in the U
        direction.

        * param (float) - Parameter value to check.
        """
    def isKnotV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isKnotV(param) -> bool

        Checks if the specified parameter value is a knot value in the V
        direction.

        * param (float) - Parameter value to check.
        """
    def isParamOnSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isParamOnSurface(uParam, vParam) -> bool

        Checks if the specified parameter point is on this surface.

        * uParam (float) - U parameter value.
        * vParam (float) - V parameter value.
        """
    def isPointInTrimmedRegion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPointInTrimmedRegion(uParam, vParam) -> bool

        Checks if the given point is in a trimmed away region of a trimmed
        surface. A trimmed away region is the part of the surface that is
        cut away as a result of a trim operation.

        * uParam (float) - U parameter of the point to check.
        * vParam (float) - V parameter of the point to check.
        """
    def isPointOnSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPointOnSurface(point, tolerance=kPointTolerance, space=kObject) -> bool

        Checks if the given point is on this surface.

        * point    (MPoint) - Point to check.
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation
        """
    @property
    def isTrimmedSurface(*args: Any, **kwargs: Any) -> Any:
        """True if the surface is a trimmed surface."""
    @isTrimmedSurface.setter
    def isTrimmedSurface(*args: Any, **kwargs: Any) -> Any:
        """True if the surface is a trimmed surface."""
    @property
    def isUniform(*args: Any, **kwargs: Any) -> Any:
        """True if the knot spacing is uniform."""
    @isUniform.setter
    def isUniform(*args: Any, **kwargs: Any) -> Any:
        """True if the knot spacing is uniform."""
    kPointTolerance: float = ...

    @property
    def knotDomainInU(*args: Any, **kwargs: Any) -> Any:
        """A tuple containing a pair of floats corresponding to the maximum and
        minimum U parameter values for this surface.
        """
    @knotDomainInU.setter
    def knotDomainInU(*args: Any, **kwargs: Any) -> Any:
        """A tuple containing a pair of floats corresponding to the maximum and
        minimum U parameter values for this surface.
        """
    @property
    def knotDomainInV(*args: Any, **kwargs: Any) -> Any:
        """A tuple containing a pair of floats corresponding to the maximum and
        minimum V parameter values for this surface.
        """
    @knotDomainInV.setter
    def knotDomainInV(*args: Any, **kwargs: Any) -> Any:
        """A tuple containing a pair of floats corresponding to the maximum and
        minimum V parameter values for this surface.
        """
    def knotInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """knotInU(index) -> float

        Returns the knot value at the specified U index. U knots are indexed
        from 0 to numKnotsInU-1.
        * index (int) - Index of the U knot to return.
        """
    def knotInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """knotInV(index) -> float

        Returns the knot value at the specified V index. V knots are indexed
        from 0 to numKnotsInV-1.
        * index (int) - Index of the V knot to return.
        """
    def knotsInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """knotsInU() -> MDoubleArray

        Returns all of the surface's knots in the U direction.
        """
    def knotsInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """knotsInV() -> MDoubleArray

        Returns all of the surface's knots in the V direction.
        """
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """normal(uParam, vParam, space=kObject) -> MVector

        Returns the normal at the given parameter value on the surface.

        * uParam (float) - U parameter at which to obtain normal.
        * vParam (float) - V parameter at which to obtain normal.
        * space    (int) - An MSpace constant giving the coordinate space
                           in which to perform the operation
        """
    def numBoundaries(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numBoundaries(region) -> unsigned int

        Returns the number of boundaries for the specified region. The
        surface must be a trimmed surface.

        For each region there may be several boundary curves, an outer curve
        and possibly several inner boundary curves which define holes. These
        boundary curves are made up of one or more curves called edges.

        * region (int) - Region of interest.
        """
    @property
    def numCVsInU(*args: Any, **kwargs: Any) -> Any:
        """Number of CVs in the surface in the U direction or 0 if the number
        of CVs cannot be determined.
        """
    @numCVsInU.setter
    def numCVsInU(*args: Any, **kwargs: Any) -> Any:
        """Number of CVs in the surface in the U direction or 0 if the number
        of CVs cannot be determined.
        """
    @property
    def numCVsInV(*args: Any, **kwargs: Any) -> Any:
        """Number of CVs in the surface in the V direction or 0 if the number
        of CVs cannot be determined.
        """
    @numCVsInV.setter
    def numCVsInV(*args: Any, **kwargs: Any) -> Any:
        """Number of CVs in the surface in the V direction or 0 if the number
        of CVs cannot be determined.
        """
    def numEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numEdges(region, boundary) -> unsigned int

        Returns the number of edges for the specified trim boundary.
        For each region there may be several boundary curves, an outer curve
        and possibly several inner boundary curves which define holes. These
        boundary curves are made up of one or more curves called edges.

        * region   (int) - Region of interest.
        * boundary (int) - Boundary of interest
        """
    @property
    def numKnotsInU(*args: Any, **kwargs: Any) -> Any:
        """Number of knots in the surface in the U direction or 0 if the number
        of knots cannot be determined.
        """
    @numKnotsInU.setter
    def numKnotsInU(*args: Any, **kwargs: Any) -> Any:
        """Number of knots in the surface in the U direction or 0 if the number
        of knots cannot be determined.
        """
    @property
    def numKnotsInV(*args: Any, **kwargs: Any) -> Any:
        """Number of knots in the surface in the V direction or 0 if the number
        of knots cannot be determined.
        """
    @numKnotsInV.setter
    def numKnotsInV(*args: Any, **kwargs: Any) -> Any:
        """Number of knots in the surface in the V direction or 0 if the number
        of knots cannot be determined.
        """
    @property
    def numNonZeroSpansInU(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the U direction which are non-zero (i.e. their
        max param value is greater than their min param value).
        """
    @numNonZeroSpansInU.setter
    def numNonZeroSpansInU(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the U direction which are non-zero (i.e. their
        max param value is greater than their min param value).
        """
    @property
    def numNonZeroSpansInV(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the V direction which are non-zero (i.e. their
        max param value is greater than their min param value).
        """
    @numNonZeroSpansInV.setter
    def numNonZeroSpansInV(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the V direction which are non-zero (i.e. their
        max param value is greater than their min param value).
        """
    @property
    def numPatches(*args: Any, **kwargs: Any) -> Any:
        """Number of non-zero patches on the surface."""
    @numPatches.setter
    def numPatches(*args: Any, **kwargs: Any) -> Any:
        """Number of non-zero patches on the surface."""
    @property
    def numPatchesInU(*args: Any, **kwargs: Any) -> Any:
        """Number of non-zero patches in the U direction."""
    @numPatchesInU.setter
    def numPatchesInU(*args: Any, **kwargs: Any) -> Any:
        """Number of non-zero patches in the U direction."""
    @property
    def numPatchesInV(*args: Any, **kwargs: Any) -> Any:
        """Number of non-zero patches in the V direction."""
    @numPatchesInV.setter
    def numPatchesInV(*args: Any, **kwargs: Any) -> Any:
        """Number of non-zero patches in the V direction."""
    @property
    def numRegions(*args: Any, **kwargs: Any) -> Any:
        """Number of trimmed regions for this surface or 0 if the surface is
        not a trimmed surface.
        """
    @numRegions.setter
    def numRegions(*args: Any, **kwargs: Any) -> Any:
        """Number of trimmed regions for this surface or 0 if the surface is
        not a trimmed surface.
        """
    @property
    def numSpansInU(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the U direction, including zero-length spans."""
    @numSpansInU.setter
    def numSpansInU(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the U direction, including zero-length spans."""
    @property
    def numSpansInV(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the V direction, including zero-length spans."""
    @numSpansInV.setter
    def numSpansInV(*args: Any, **kwargs: Any) -> Any:
        """Number of spans in the V direction, including zero-length spans."""
    @property
    def numUVs(*args: Any, **kwargs: Any) -> Any:
        """Number of texture (uv) coordinates for this surface. The uvs are
        stored in a list which is referenced by patches requiring textures
        on a per-patch per-patchCorner basis. This attribute contains the
        number of elements in this list.
        """
    @numUVs.setter
    def numUVs(*args: Any, **kwargs: Any) -> Any:
        """Number of texture (uv) coordinates for this surface. The uvs are
        stored in a list which is referenced by patches requiring textures
        on a per-patch per-patchCorner basis. This attribute contains the
        number of elements in this list.
        """
    def projectCurve(self: Self, *args: Any, **kwargs: Any) -> Any:
        """projectCurve(curve[, direction], keepHistory=False) -> self

        Projects the given curve onto the surface, creating a curve on surface.

        * direction (MVector) - Direction of projection. If not supplied
                                then surface normals will be used.
        * keepHistory  (bool) - Determines whether the construction history
                                of the projection should be retained.
        """
    def removeKnotInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeKnotInU(param, removeAll=False) -> self

        Removes one or more U knots at the specified parameter value from
        from the surface.

        * param    (float) - U parameter value of the knot to remove.
        * removeAll (bool) - If True and there are multiple knots at the
                             parameter value then they will all be removed.
                             Otherwise, all but one will be removed.
        """
    def removeKnotInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeKnotInV(param, removeAll=False) -> self

        Removes one or more V knots at the specified parameter value from
        from the surface.

        * param    (float) - V parameter value of the knot to remove.
        * removeAll (bool) - If True and there are multiple knots at the
                             parameter value then they will all be removed.
                             Otherwise, all but one will be removed.
        """
    def removeOneKnotInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeOneKnotInU(param) -> self

        Removes one U knot at the specified parameter value. If there are
        multiple knots at that the value the others are retained.

        * param (float) - U parameter value of the knot to remove.
        """
    def removeOneKnotInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeOneKnotInV(param) -> self

        Removes one V knot at the specified parameter value. If there are
        multiple knots at that the value the others are retained.

        * param (float) - V parameter value of the knot to remove.
        """
    def setCVPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCVPosition(uIndex, vIndex, point, space=kObject) -> self"""
    def setCVPositions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCVPositions(points, space=kObject) -> self

        Set the positions of all of the surface's CVs.
        (numCVsInU * numCVsInV) points must be provided. Converting from
        U and V indices to array indices is done by:

                array index = numCVsInV * U index + V index

        To keep this method as fast as possible, no checking of the data is
        performed beyond ensuring that the total number of CVs passed in is
        correct. It is up to the caller to ensure that the CVs provide a
        valid surface, for example by ensuring that overlapping CVs in
        periodic surfaces have the same positions.

        * points (MPointArray or seq of MPoint)
                       - Positions of the CVs.
        * space  (int) - An MSpace constant giving the coordinate space
                         in which to perform the operation
        """
    def setKnotInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setKnotInU(index, param) -> self

        Sets the value of an existing U knot. U knots are indexed from 0 to
        numKnotsInU-1. Note that this method does not insert a new knot, it
        simply changes the value of an existing knot.

        If a knot value is set that breaks the non-decreasing requirement
        for the knot array, the knot value will be changed and an exception
        raised.

        * index   (int) - U index of the knot to set.
        * param (float) - New parameter value for the knot.
        """
    def setKnotInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setKnotInV(index, param) -> self

        Sets the value of an existing V knot. V knots are indexed from 0 to
        numKnotsInV-1. Note that this method does not insert a new knot, it
        simply changes the value of an existing knot.

        If a knot value is set that breaks the non-decreasing requirement
        for the knot array, the knot value will be changed and an exception
        raised.

        * index   (int) - V index of the knot to set.
        * param (float) - New parameter value for the knot.
        """
    def setKnotsInU(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setKnotsInU(params, startIndex, endIndex) -> self

        Sets the values of a range of U knots.

        * params     (MDoubleArray or seq of float)
                           - Parameter values to set at the knots. One value
                             per knot in the range.
        * startIndex (int) - Index of the first U knot to set.
        * endIndex   (int) - Index of the last U knot to set.
        """
    def setKnotsInV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setKnotsInV(params, startIndex, endIndex) -> self

        Sets the values of a range of V knots.

        * params     (MDoubleArray or seq of float)
                           - Parameter values to set at the knots. One value
                             per knot in the range.
        * startIndex (int) - Index of the first V knot to set.
        * endIndex   (int) - Index of the last V knot to set.
        """
    def setUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUV(uvId, u, v) -> self

        Sets a single texture coordinate. If 'uvId' is greater than or equal
        to numUVs then the surface's uv list will be grown to accommodate it.

        Note that API methods that modify uv data work correctly either when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * uvId (int) - Index of the element in the surface's uv list to set.
        * u  (float) - U value to set the uv to.
        * v  (float) - V value to set the uv to.
        """
    def setUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUVs(uList, vList) -> self

        Sets all of the texture coordinates (uvs) for this surface. The
        arrays must be of equal length and must be at least of length numUVs.
        If the arrays are larger than numUVs then the uv list for this surface
        will be grown to accommodate the new uv values.

        After using this method to set the UV values, you can call
        assignUVs to assign the corresponding UVids to the geometry.

        Note that API methods that modify uv data work correctly either when
        called through a plug-in node that is in the history of the shape,
        or when used on a surface shape that does not have history.
        Modifying uvs directly on a shape with history will result in the
        modifications getting over-written by the next evaluation of the
        history attached to the shape.

        * uList (MFloatArray or seq of float) - U values to set
        * vList (MFloatArray or seq of float) - V values to set
        """
    def tangents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """tangents(uParam, vParam, space=kObject) -> (MVector, MVector)

        Returns the tangents in the U and V directions at a given parameter
        value on the surface. The returned tangent vectors are normalized.

        This method does not fail if the given parameter lies within a
        trimmed away region of a trimmed surface. Use isPointInTrimmedRegion()
        to determine if the uv point lies within such a region.

        * uParam (float) - U parameter value at which to obtain the tangents.
        * vParam (float) - V parameter value at which to obtain the tangents.
        * space    (int) - An MSpace constant giving the coordinate space
                           in which to perform the operation
        """
    def trim(self: Self, *args: Any, **kwargs: Any) -> Any:
        """trim(regionsToKeepU, regionsToKeepV, keepHistory=False) -> self

        Trims the surface to its curves on surface. Regions which are kept
        are specified by passing in arrays of u,v parameters.

        This method will create a new trimmed surface in the DAG. The surface
        attached to this function set will remain unchanged.

        * regionsToKeepU (MDoubleArray or seq of float)
                                - U parameters of points within the regions
                                  to be kept.
        * regionsToKeepV (MDoubleArray or seq of float)
                                - V parameters of points within the regions
                                  to be kept.
        * keepHistory    (bool) - Determines whether the construction history
                                  of the operation should be retained.
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signals that this surface has changed and needs to be recalculated.

        This method is useful when a large number of CVs for the surface are
        being modified. Instead of updating the surface every time a CV is
        changed it is more efficient to call this method once after all the
        updates are complete.
        """

class MFnNurbsSurfaceData(MFnGeometryData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new nurbs surface data object, attaches it to this function set
        and returns an MObject which references it.
        """

class MFnPlugin(MFnBase):
    def apiVersion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the API version required by the plug-in."""
    def deregisterAttributePatternFactory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined attribute pattern factory type from Maya."""
    def deregisterCommand(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined command from Maya."""
    def deregisterContextCommand(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined context command from Maya."""
    def deregisterData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined data type from Maya."""
    def deregisterDragAndDropBehavior(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined drag and drop behavior from Maya."""
    def deregisterNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined dependency node from Maya."""
    def findPlugin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an MObject corresponding to the named plugin."""
    def loadPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the full path name of the file from which the plug-in was loaded."""
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the plug-in's name."""
    def registerAttributePatternFactory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new attribute pattern factory type with Maya."""
    def registerCommand(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new command with Maya."""
    def registerContextCommand(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new context command with Maya.  Once registered, the context
        can be used to create a new tool that can be used in a manner
        identical to built-in Maya tools.
        """
    def registerData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new data type with Maya."""
    def registerDragAndDropBehavior(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new drag and drop behavior with Maya.
        Once registered, the new behavior can be used to finish connections between node drag and drops from the hyperGraph/hyperShade to other nodes or Maya UI.
        """
    def registerNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new dependency node with Maya."""
    def registerShape(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Register a new user defined shape node with Maya.
        To deregister the shape node use the MFnPlugin.deregisterNode().
        """
    def setName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set the plug-in's name."""
    def vendor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the plug-in's vendor string."""
    @property
    def version(*args: Any, **kwargs: Any) -> Any:
        """Plug-in version string."""
    @version.setter
    def version(*args: Any, **kwargs: Any) -> Any:
        """Plug-in version string."""

class MFnPluginData(MFnData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(id) -> MObject

        Create an instance of the specified user defined data type and attach it to this functionset.

        * id (MTypeId) - the unique MTypeId of the user defined data class derived from MPxData.
        """
    def data(self: Self, *args: Any, **kwargs: Any) -> Any:
        """data() -> MPxData

        Return the user defined data held in this instance
        """
    def typeId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Return the unique MTypeId of the user defined data that is held by this instance
        """

class MFnPointArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MPointArray."""
    def copyTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MPoint array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MFnReference(MFnDependencyNode):
    def associatedNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """associatedNamespace(bool shortName) -> MString

        Returns the namespace associated with this reference.
        """
    def containsNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """containsNode(MObject) -> bool

        Returns true if the specified node is from this reference or one of its child references. The containsNodeExactly method can be used to test membership without including the child references.
        """
    def containsNodeExactly(self: Self, *args: Any, **kwargs: Any) -> Any:
        """containsNodeExactly(MObject) -> bool

        Returns true if the specified node is from this reference. Membership in child references is not checked. The containsNode method may be used to test membership in a reference and its child references.
        """
    def fileName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

        Returns the name of file associated with this reference.
        """
    def ignoreReferenceEdits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """ignoreReferenceEdits() -> bool

        Indicates whether reference edits will be tracked and logged or not.
        """
    def isExportEditsFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isExportEditsFile() -> bool

        Returns true if the reference is an export edits file. An export edits file is a file of type '.editMA' or '.editMB' which was created using Maya's offline file functionality.
        """
    def isLoaded(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isLoaded() -> bool

        Returns true if the reference is loaded.
        """
    def isLocked(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isLocked() -> bool

        Returns true if the reference is locked or if the referenced file was saved as locked.
        """
    def isValidReference(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isValidReference() -> bool

        Returns true if the reference is an valid file reference.
        """
    def nodes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """nodes() -> MObjectArray

        Returns an array of the nodes associated with this reference.
        """
    def parentAssembly(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parentAssembly() -> MObject

        Returns the parent assembly node that contains this reference. See MFnAssembly documentation for more details.
        """
    def parentFileName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parentFileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

        Returns the name of parent file associated with this reference.
        """
    def parentReference(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parentReference() -> MObject

        Returns the reference node associated with the parent reference.
        """
    def setIgnoreReferenceEdits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIgnoreReferenceEdits(bool) -> None

        Specify whether reference edits should be tracked and logged or not.
        This should be treated as a temporary state and should be enabled
        around a batch of operations where reference edits should be ignored.
        Restore the previous value when the batch of operations is complete.
        """

class MFnSet(MFnDependencyNode):
    def addMember(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addMember( object ) -> self

        Add a new object to the set.

        The added object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """
    def addMembers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addMembers( MSelectionList ) -> self

        Add a list of new objects to the set.
        """
    def annotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """annotation() -> string

        Returns the annotation string for this set.  This allows a description of the set to be stored with it.
        """
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Removes all elements from this set.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(members, restriction=kNone) -> MObject

        Creates a new set dependency node and puts it in the dependency graph.

        * members (MSelectionList) - list of members for new set
        * restriction (MFnSet.Restriction) - restriction applied to members
        """
    def getIntersection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getIntersection( otherSet ) -> MSelectionList

        This method calculates the intersection of two sets.  The result will be the intersection of this set and the set passed into the method.

        * otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set
        """
    def getMemberPaths(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMemberPaths( shading ) -> MDagPathArray

        Get the members of this set as an array of dagPaths.

        This will usually return the same dagPaths as will be contained in the getMembersmethod. If the shading flag is set to true, the list will consist only of dagPathsthat are affected by this set for the purposes of material assignments.

        * shading (bool) -  whether the list should only contain members of this set used for shading purposes.
        """
    def getMembers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMembers( flatten ) -> MSelectionList

        Get the members of this set as a selection list.  This information is providedas a selection list so that all of the path information is retained forDAG nodes.

        It is possible to ask for the returned list to be flattened.  This means thatall sets that exist inside this set will be expanded into a list of theircontents.

        * flatten (bool) - whether to flatten the returned list
        """
    def getUnion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUnion( otherSet ) -> MSelectionList

        This method calculates the union of two sets.  The result will be the union of this set and the set passed into the method.

        * otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set
        """
    def hasRestrictions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasRestrictions() -> bool

        Returns true if this function set has restrictions on the type of objects that it may contain.
        """
    def intersectsWith(self: Self, *args: Any, **kwargs: Any) -> Any:
        """intersectsWith( otherSet ) -> self

        Returns true if this set intersects with the given set.  An intersection occurs if there are any common members between the two sets.
        """
    def isMember(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isMember( object ) -> bool

        Returns true if the given object is a member of this set.

        The object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """
    def removeMember(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeMember( object ) -> self

        Remove an object from the set.

        The removed object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """
    def removeMembers(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeMembers( MSelectionList ) -> self

        Remove items of the selection list from the set.
        """
    def restriction(self: Self, *args: Any, **kwargs: Any) -> Any:
        """restriction() -> MFnSet.Restriction

        Returns the type of membership restriction that this set has.
        """
    def setAnnotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAnnotation( annotation ) -> self

        Sets the annotation string for this set.  This allows a description of the set to be stored with it.
        """

class MFnSingleIndexedComponent(MFnComponent):
    def addElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElement(int element) -> self

        Adds the specified element to the component.
        """
    def addElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElements([int]) -> self
        addElements(MIntArray) -> self

        Adds the specified elements to the component.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """
    def element(self: Self, *args: Any, **kwargs: Any) -> Any:
        """element(index) -> int

        Returns the index'th element of the component.
        """
    @property
    def elementMax(*args: Any, **kwargs: Any) -> Any:
        """Biggest element plus 1 in the component."""
    @elementMax.setter
    def elementMax(*args: Any, **kwargs: Any) -> Any:
        """Biggest element plus 1 in the component."""
    def getCompleteData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCompleteData() -> int

        Returns the number of elements in the complete component, or 0 if the component is not complete.
        """
    def getElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getElements() -> MIntArray

        Returns all of the component's elements.
        """
    def setCompleteData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCompleteData(numElements) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numElements indicates the number of elements in the complete component.
        """

class MFnStringArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as a list of unicode objects."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new string array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MFnStringData(MFnData):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new string data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the encapsulated string."""
    def string(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated string as a unicode object."""

class MFnTransform(MFnDagNode):
    def clearRestPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Clears the transform's rest position matrix."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new transform node and attaches it to the function set."""
    def enableLimit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Enables or disables a specified limit type."""
    def isLimited(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified limit type is enabled."""
    kRotateMaxX: int = ...
    kRotateMaxY: int = ...
    kRotateMaxZ: int = ...
    kRotateMinX: int = ...
    kRotateMinY: int = ...
    kRotateMinZ: int = ...
    kShearMaxYZ: int = ...
    kShearMinYZ: int = ...
    kTranslateMaxX: int = ...
    kTranslateMaxY: int = ...
    kTranslateMaxZ: int = ...
    kTranslateMinX: int = ...
    kTranslateMinY: int = ...
    kTranslateMinZ: int = ...

    def limitValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the specified limit."""
    def resetFromRestPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Resets the transform from its rest position matrix."""
    def restPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rest position matrix."""
    def rotateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""
    def rotateByComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def rotateOrientation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MQuaternion which orients the local rotation space."""
    def rotatePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotate pivot."""
    def rotatePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotate pivot translation."""
    def rotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def rotationComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""
    def rotationOrder(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""
    def scale(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""
    def scaleBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""
    def scalePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's scale pivot."""
    def scalePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's scale pivot translation."""
    def setLimit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the specified limit."""
    def setRestPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rest position matrix."""
    def setRotateOrientation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the MQuaternion which orients the local rotation space."""
    def setRotatePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotate pivot."""
    def setRotatePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotate pivot translation."""
    def setRotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""
    def setRotationComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""
    def setRotationOrder(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation order."""
    def setScale(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale components."""
    def setScalePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale pivot."""
    def setScalePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale pivot translation."""
    def setShear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's shear."""
    def setTransformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""
    def setTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's translation."""
    def shear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""
    def shearBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transform's shear components by a sequence of three floats."""
    def transformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation matrix represented by this transform."""
    def translateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds an MVector to the transform's translation."""
    def translation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's translation as an MVector."""

class MFnTripleIndexedComponent(MFnComponent):
    def addElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElement(sIndex, tIndex, uIndex) -> self
        addElement([sIndex, tIndex, uIndex]) -> self

        Adds the element identified by (sIndex, tIndex, uIndex) to the component.
        """
    def addElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addElements(sequence of [sIndex, tIndex, uIndex]) -> self

        Adds the specified elements to the component. Each item in the
        elements sequence is itself a sequence of three ints which are the
        S, T and U indices of an element to be added.
        """
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """
    def getCompleteData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCompleteData() -> (numS, numT, numU)

        Returns a tuple containing the number of S, T and U indices in
        the complete component, or (0,0,0) if the component is not complete.
        """
    def getElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getElement(index) -> (sIndex, tIndex, uIndex)

        Returns the index'th element of the component as a tuple containing the
        element's S, T and U indices.
        """
    def getElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getElements() -> list of (sIndex, tIndex, uIndex)

        Returns all of the component's elements as a list of tuples with each
        tuple containing the S, T and U indices of a single element.
        """
    def setCompleteData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCompleteData(numS, numT, numU) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numS, numT and numU indicate the number of S, T and U indices
        in the complete component (i.e. the max S index is numS-1, the max T
        index is numT-1 and the max U index is numU-1).
        """

class MFnTypedAttribute(MFnAttribute):
    def attrType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of data handled by the attribute."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new type attribute, attaches it to the function set and returns it as an MObject."""
    @property
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    @default.setter
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""

class MFnUInt64ArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MUint64Array."""
    def copyTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MUint64 array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MFnUnitAttribute(MFnAttribute):
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new unit attribute, attaches it to the function set and returns it as an MObject."""
    @property
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    @default.setter
    def default(*args: Any, **kwargs: Any) -> Any:
        """Default value"""
    def getMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def getMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def getSoftMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def getSoftMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""
    def hasMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a hard maximum value."""
    def hasMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a hard minimum value."""
    def hasSoftMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a soft maximum value."""
    def hasSoftMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a soft minimum value."""
    kLast: int = ...
    kTime: int = ...

    def setMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard maximum value."""
    def setMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard minimum value."""
    def setSoftMax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft maximum value."""
    def setSoftMin(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft minimum value."""
    def unitType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of data handled by the attribute."""

class MFnVectorArrayData(MFnData):
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MVectorArray."""
    def copyTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MVector array data object."""
    def set(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""

class MGlobal:
    def addToModel(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addToModel(MObject, MObject) -> None

        This method is used to add new dag objects to the model.  If no parent node
        is specified, then the node is added under the world.  When a node is
        added under the world, then a transform node is automatically created as
        a parent.  This assumes that the node being added is not already a
        transform node.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter will be returned.
        """
    def addToModelAt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addToModelAt(MObject, MVector, double[3], double[3], rotateOrder=MTransformationMatrix.kXYZ) -> None

        Adds the specified dag object to the DAG and transform the object
        by the specified arguments.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter
        will be returned.
        """
    def animSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """animSelectionMask() -> MSelectionMask

        Returns the animation selection mask.
        """
    def apiVersion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """apiVersion() -> int

        Returns a number describing the version of the Maya API at runtime.
        """
    def className(self: Self, *args: Any, **kwargs: Any) -> Any:
        """className() -> string

        Returns the name of this class.
        """
    def clearSelectionList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clearSelectionList() -> None

        Removes all items from the active selection list.
        """
    def closeErrorLog(self: Self, *args: Any, **kwargs: Any) -> Any:
        """closeErrorLog() -> None

        This method closes the API error log file.  If error logging is currently
        enabled this method disables it.
        The error log is time and date stamped before it is closed.
        After the log is closed the error log path name is reset to the default
        path name.
        If the error log file is already closed, then no action is taken.

        Note that if a log is reopened after it is closed, all information previously
        logged to it is lost.
        """
    def componentSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentSelectionMask() -> MSelectionMask

        Returns the component selection mask.
        """
    def currentToolContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentToolContext() -> MObject

        Returns the current tool context as an MObject.
        """
    def defaultErrorLogPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """defaultErrorLogPathName() -> string

        Determines the default path name of the error log file.
        Returns an empty string on failure.
        """
    def deleteNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteNode(MObject) -> None

        Delete the given dag node or dependency graph node.
        """
    def disableStow(self: Self, *args: Any, **kwargs: Any) -> Any:
        """disableStow() -> bool

        This method is used to query if the disabling of Stowing (hiding)
        and Unstowing (showing) windows is active.
        """
    def displayError(self: Self, *args: Any, **kwargs: Any) -> Any:
        """displayError(msg) -> None

        Display an error in the script editor.
        """
    def displayInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """displayInfo(msg) -> None

        Display an informational message in the script editor.
        """
    def displayWarning(self: Self, *args: Any, **kwargs: Any) -> Any:
        """displayWarning(msg) -> None

        Display a warning in the script editor.
        """
    def doErrorLogEntry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """doErrorLogEntry(string) -> bool

        Logs an entry in the currently open log file.  It is not necessary for error
        logging to be enabled, but a log file must be open.
        A newline is appended to each log entry.
        """
    def errorLogPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """errorLogPathName() -> string

        Determines the path name of the current error log file.
        Returns the null stringon failure.
        """
    def errorLoggingIsOn(self: Self, *args: Any, **kwargs: Any) -> Any:
        """errorLoggingIsOn() -> bool

        This method determines whether or not API errors are being logged.
        """
    def executeCommandOnIdle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """executeCommandOnIdle(string, bool displayEnabled=False) -> None

        Sets a MEL command to execute on the next idle event. Since the command
        will likely not be executed until some time after control is returned to
        caller, there is no access to the command results.

        This method is thread safe and can be called from a thread other than
        Maya's main thread. However, that thread must still be part of the Maya
        process. Calling this method from a completely separate process will
        not work and may lead to unpredictable behaviour.
        """
    def executeCommandStringResult(self: Self, *args: Any, **kwargs: Any) -> Any:
        """executeCommandStringResult(string, bool displayEnabled=False, bool undoEnabled=False) -> string or [string, string, ...]

        Executes a MEL command that returns a string or an array of strings
        result from the command engine depending on the number of return values.
        Optionally allows display of the command in the Command Window to be
        enabled or disabled.  Defaults to disabled.  Optionally allows undo
        for the command to be enabled or disabled.  Defaults to disabled.

        Note: This is not thread safe; you may use executeCommandOnIdle instead
        """
    def getAbsolutePathToResources(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAbsolutePathToResources() -> string

        Return the absolute path of Maya's "Resources" fold on the system,
        including the "Resources" folder itself.
        """
    def getActiveSelectionList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getActiveSelectionList(orderedSelectionIfAvailable=False) -> MSelectionList

        Return an MSelectionList containing the nodes, components and
        plugs currently selected in Maya. If orderedSelectionIfAvailable
        is True, and tracking is enabled, will return the selected items
        in the order that they were selected.
        """
    def getAssociatedSets(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedSets(MSelectionList) -> list

        This utility method finds all the sets that the items in
        the given selection list are members of.
        """
    def getFunctionSetList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFunctionSetList(MObject) -> (string, string, ...)

        Returns a tuple of strings that represent the type of each function
        set that will accept this object.
        """
    def getHiliteList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getHiliteList() -> MSelectionList

        Returns a copy of the hilite list.  The hilite list contains all DAG objects
        that are hilited for component selection mode.  (e.g. when the user right clicks
        over a Mesh object and chooses the "vertex" option the Mesh line drawing changes
        color and the mesh is added to the hiliteList.)
        """
    def getLiveList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getLiveList() -> MSelectionList

        Returns a copy of the live list. When a user performs a
        "Modify->Make Live" in the user interface the currently selected
        objects are added to the live list.
        """
    def getPreselectionHiliteList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPreselectionHiliteList() -> MSelectionList

        Gets the objects for which Maya is displaying a preselection
        highlight in the viewports.
        """
    def getRichSelection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRichSelection(defaultToActiveSelection=True) -> MRichSelection

        Returns the current rich selection (usually the active selection with
        any soft selection and symmetry applied). If no rich selection exists
        and 'defaultToActiveSelection' is True, the current active selection
        will be returned instead.
        """
    def getSelectionListByName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionListByName(name) -> MSelectionList

        Returns an MSelectionList with all of the objects that match the
        specified name. The name may use the same type of regular expressions
        as can be used in MEL commands. For example, the pattern 'pCube*' will
        match all occurrences of objects whose names begin with 'pCube'.
        """
    def initOptionVar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """initOptionVar(string name, int, string category) -> bool
        initOptionVar(string name, double, string category) -> bool
        initOptionVar(string name, string, string category) -> bool


        This method is used to initialize an option variable value of int, bool, string type.
        This method will create the option var if it doesn't exist and set the default value
        and category.
        """
    def isRedoing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isRedoing() -> bool

        true if Maya is currently in the middle of a redo.
        """
    def isSelected(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isSelected(MObject) -> bool

        Determines whether the given object is on the active selection list.
        """
    def isUndoing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isUndoing() -> bool

        true if Maya is currently in the middle of an undo.
        """
    def isYAxisUp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isYAxisUp() -> bool

        This method returns true if, currently, the Y-axis is UP.
        """
    def isZAxisUp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isZAxisUp() -> bool

        This method returns true if, currently, the Z-axis is UP.
        """
    kAddToHeadOfList: int = ...
    kAddToList: int = ...
    kBaseUIMode: int = ...
    kBatch: int = ...
    kInteractive: int = ...
    kLibraryApp: int = ...
    kRemoveFromList: int = ...
    kReplaceList: int = ...
    kSelectComponentMode: int = ...
    kSelectLeafMode: int = ...
    kSelectObjectMode: int = ...
    kSelectRootMode: int = ...
    kSelectTemplateMode: int = ...
    kSurfaceSelectMethod: int = ...
    kWireframeSelectMethod: int = ...
    kXORWithList: int = ...

    def mayaFeatureSet(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mayaFeatureSet() -> int

        Returns an enumerated type specifying if Maya API has unlimited set of features.
          kComplete  Running Maya version with all features available.
          kRestricted  Running Maya version with some features limited in availability.
        """
    def mayaName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mayaName() -> string

        Returns a string containing name of running application.
        """
    def mayaState(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mayaState() -> int

        Returns an enumerated type specifying the way in which Maya was invoked.
          kInteractive  Running with a UI
          kBatch  Running without a UI
          kLibraryApp  Running as a standalone (MLibrary) application.
          kBaseUIMode  Running with UI enabled but Maya's std UI scripts not run.
        """
    def mayaVersion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """mayaVersion() -> string

        Returns a string describing this version of Maya.
        """
    def miscSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """miscSelectionMask() -> MSelectionMask

        Returns the miscellaneous selection mask.
        """
    def objectSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """objectSelectionMask() -> MSelectionMask

        Returns the object selection mask.
        """
    def optionVarDoubleValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """optionVarDoubleValue(string) -> double

        This method is used to get the option variable value of type double
        """
    def optionVarExists(self: Self, *args: Any, **kwargs: Any) -> Any:
        """optionVarExists(string) -> bool

        This method is used to check if the option variable exists
        """
    def optionVarIntValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """optionVarIntValue(string) -> int

        This method is used to get the option variable value of int type
        """
    def optionVarStringValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """optionVarStringValue(string) -> MString

        This method is used to get the option variable value of type string
        """
    def removeFromModel(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeFromModel(MObject) -> None

        Removes the specified dag node from the scene.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter
        will be returned.

        Note that this method doesn't delete the dag node which means
        the node must be added back to scene by calling either
        MGlobal::addToModel() or MGlobal::addToModelAt() in later
        calls, otherwise the dag node is leaked. To delete the dag node,
        call MGlobal::deleteNode() instead.
        """
    def removeOptionVar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeOptionVar(string) -> None

        This method is used to remove the option variable
        """
    def resetToDefaultErrorLogPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resetToDefaultErrorLogPathName() -> None

        Closes the current log file if it is open, and then resets the log path to
        the default path.
        Logging is disabled and the log file speicified by the default path is not opened.
        If logging is disabled, it remains disabled.
        Use startErrorLogging() to enable logging to the default log file.
        If the current path is the default path, no action is taken,
        but an invalid parameter error is returned.

        Note that if the default log is reopened after it is closed, all information
        previously logged to it is lost.
        """
    def selectByName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectByName(string, listAdjustment=kReplaceList) -> None

        Puts objects that match the give name on the active selection list.
        """
    def selectCommand(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectCommand(MSelectionList, listAdjustment=kReplaceList) -> None

        Set the active selection list, by calling the built in Maya select
        command.  This differs from setActiveSelectionList in that in this
        version Maya takes over the selection list you give it and will be
        responsible for maintaing the necessary information required for
        undo, redo, and journaling.
        """
    def selectFromScreen(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectFromScreen(short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None
        selectFromScreen(short, short, short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None

        Perform click-pick type selection on the dag. If an object intersects
        the click point then it is selected according to listAdjustment.
        """
    def selectionMethod(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectionMethod() -> int

        Determines the selection method that should be used in the currently active
        viewport.  This is useful as input to the "selectFromScreen" functions.
        """
    def selectionMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """selectionMode() -> int

        Get current selection mode:
          kSelectObjectMode     Objects are selected as a whole. Components are not directly accessible.
          kSelectComponentMode  Components such as vertices are selectable in this mode.
          kSelectRootMode       Selecting the child in a hierarchy will also select its root DAG node.
          kSelectLeafMode       Selecting the child in a hierarchy will result only in that child being selected.
          kSelectTemplateMode   Templated objects are selectable in this mode.
        """
    def setActiveSelectionList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setActiveSelectionList(MSelectionList, listAdjustment=kReplaceList) -> None

        Set the active selection list.
        The selection items on the given list will update the contents of the active selection
        list as indicated by the listAdjustment parameter.
        Valid listAdjustment values are:
          kReplaceList      #Totally replace the list with the given items.
          kXORWithList      #Items already in the list will be removed. New items will be appended to the end of the list.
          kAddToList        #Add the items to the end of the list.
          kRemoveFromList   #Remove the items from the list.
          kAddToHeadOfList  #Add the items to the beginning of the list.
        """
    def setAnimSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAnimSelectionMask(mask) -> selfsetAnimSelectionMask(type) -> self

        Set the animation selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
    def setComponentSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setComponentSelectionMask(mask) -> selfsetComponentSelectionMask(type) -> self

        Set the component selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
    def setDisableStow(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDisableStow(bool) -> None

        This method is used to make the visiblity of all Maya windows unchangable.
        If set to true, it disables any attempts to change the visiblity of any window.
        In addition, all popup windows will be supressed.
        """
    def setDisplayCVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDisplayCVs(MSelectionList, bool) -> None

        Controls drawing of control points in the specified selection list.

        The selection items on the given list will be marked for drawing. This
        overrides Maya's current draw list and allow, for example, the drawing
        of control points without being in vertex selection mode.
        """
    def setErrorLogPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setErrorLogPathName(string) -> None

        Determines the default path name of the error log file.
        Returns an empty string on failure.
        """
    def setHiliteList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHiliteList(MSelectionList) -> None

        Sets the current hilite list. The current selection list is unchanged.
        """
    def setMiscSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMiscSelectionMask(mask) -> selfsetMiscSelectionMask(type) -> self

        Set the miscellaneous selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
    def setObjectSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setObjectSelectionMask(mask) -> selfsetObjectSelectionMask(type) -> self

        Set the object selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """
    def setOptionVarValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setOptionVarValue(string, int) -> bool
        setOptionVarValue(string name, double) -> bool
        setOptionVarValue(string name, string) -> bool


        This method is used to set the option variable value of int, bool, string type
        """
    def setPreselectionHiliteList(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPreselectionHiliteList(MSelectionList) -> None

        Sets the objects for which Maya will display a preselection
        highlight in the viewports.

        The objects/components in the list will be drawn in Maya's
        preselection highlight style on the next viewport refresh
        (if preselection highlighting is enabled in the preferences).

        If preselection highlighting is not enabled, Maya will still
        store the list.
        """
    def setRichSelection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRichSelection(MRichSelection) -> None

        Set the current rich selection.
        """
    def setSelectionMode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSelectionMode(int) -> None

        Set the current selection mode.
        See selectionMode() for a list of valid modes.
        """
    def setTrackSelectionOrderEnabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setTrackSelectionOrderEnabled() -> None

        Set whether Maya should maintain an active selection list which
        maintains object and component selection order.
        """
    def setYAxisUp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setYAxisUp() -> None

        This method sets the flag to identify which axis is Up, and
        rotates the ground plane around around the X-axis 90 degrees to get
        the Y-Up from Z-Up.
        """
    def setZAxisUp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setZAxisUp() -> None

        This method sets the flag to identify which axis is Up, and
        rotates the ground plane around around the X-axis 90 degrees to get
        the Y-Up from Y-Up.
        """
    def sourceFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """sourceFile(string) -> None

        Causes the MEL command engine to open the named file and execute
        the contents of the file as a MEL script.  If the provided fileName
        is a Unix absolute pathname, then that file is opened.  If a relative
        pathname is provided, the directories indicated by the environment
        variable, MAYA_SCRIPT_PATH, will be searched for a matching filename.
        """
    def startErrorLogging(self: Self, *args: Any, **kwargs: Any) -> Any:
        """startErrorLogging() -> None
        startErrorLogging(string)

        This method enables output to the API error log file specified by the path.
        If another error log file is already open this method time and date stamps
        the log, and closes it.
        The new error log is time and date stamped when it is opened.

        If the new path name is the same as the current path name, this method ensures
        that logging is enabled, but no other action is taken.
        """
    def stopErrorLogging(self: Self, *args: Any, **kwargs: Any) -> Any:
        """stopErrorLogging() -> None

        This method disables output to the API error log but does not close the log file.
        """
    def trackSelectionOrderEnabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """trackSelectionOrderEnabled() -> bool

        Returns whether the selection order is currerntly being tracked.
        """
    def unselect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unselect(MObject) -> None
        unselect(MDagPath, MObject) -> None

        Remove the given object/components from the active selection list.
        If components is null then the object will be unselected, otherwise
        the components will be unselected.

        Perform marquee type selection on the dag.  If an object intersects the
        selection rectangle, it is selected according to listAdjustment.
        """
    def unselectByName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """unselectByName(string) -> None

        Removes objects matching the pattern from the active selection list.
        """
    def upAxis(self: Self, *args: Any, **kwargs: Any) -> Any:
        """upAxis() -> MVector

        This method returns the model's current up axis.
        """
    def viewFrame(self: Self, *args: Any, **kwargs: Any) -> Any:
        """viewFrame(double) -> None
        viewFrame(MTime) -> None

        Sets the global time to the specified time.  This function is optimized
        for sequential time values that are monotonically increasing.  While
        one can set the time randomly with this function, a significant
        performance hit will be incurred.
        """

class MImage:
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(width, height, channels=4, type=kByte) -> self

        Create a new MImage object. Allocates memory for an RGBA array of pixels
        of the given size. If an object was already in memory, it is released first.

        * width (unsigned int) - the desired image's width in pixels.
        * height (unsigned int) - the desired image's height in pixels.
        * channels (unsigned int) - the desired number of channels per pixel.
        * type (int) - the desired pixel format (kByte or kFloat, see MImage.pixelType() description for details.)
        """
    def depth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """depth() -> int

        Get the color depth (in bytes) of the currently opened image.
        """
    def depthMap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """depthMap() -> long

        Returns a long containing a C++ 'float' pointer which points to the depth data.
        """
    def filter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """filter(sourceFormat, targetFormat, scale=1.0, offset=1.0) -> self

        Modify the content of the image by applying a filter.
        The dimension of the image remains the same; only the RGBA components get affected.

        * sourceFormat (MImageFilterFormat) - the format of the source image.
        * targetFormat (MImageFilterFormat) - the format of the resulting image.* scale (float) - vary depending on the source/target format.
        * offset (float) - vary depending on the source/target format.

        The scale argument for this filter can vary from -256.0 to 256.0, although typical values range from 1.0 to 10.0.
        The offset argument is currently ignored and should be left to the default value of 0.0.
        """
    def filterExists(self: Self, *args: Any, **kwargs: Any) -> Any:
        """filterExists(sourceFormat, targetFormat) -> bool

        Return whether or not a given source format can be directly converted to a given target format.

        * sourceFormat (MImageFilterFormat) - the format of the source image.
        * targetFormat (MImageFilterFormat) - the format of the resulting image.
        """
    def floatPixels(self: Self, *args: Any, **kwargs: Any) -> Any:
        """floatPixels() -> long

        Returns a long containing a C++ 'float' pointer which points to the pixel data.
        This data is uncompressed and tightly packed, of size (width * height * depth * sizeof( float)) bytes.
        """
    def getDepthMapRange(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDepthMapRange() -> [minValue, maxValue]

        Compute the minimum and maximum depth values (range) for any stored depth buffer.
        """
    def getDepthMapSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDepthMapSize() -> [width, height]

        Returns the size of the depth map buffer.
        """
    def getSize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSize() -> [width, height]

        Get the width and height of the currently opened image.
        """
    def haveDepth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """haveDepth() -> bool

        Returns True if this instance of MImage contains a depth map.
        """
    def isRGBA(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isRGBA() -> bool

        Query flag which indicates whether the pixel information is in RGBA sequence or BGRA sequence.
        If no pixel data exists, then False will be returned.
        """
    kByte: int = ...
    kFloat: int = ...
    kHeightFieldBumpFormat: int = ...
    kNoFormat: int = ...
    kNormalMapBumpFormat: int = ...
    kUnknown: int = ...
    kUnknownFormat: int = ...

    def pixelType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pixelType() -> int

        Get the current pixel format of the image:  kUnknown    Format not known or invalid.
          kByte       One byte per channel, ranging from 0 to 255.
          kFloat      One float per channel, ranging from 0.0 to 1.0.
        """
    def pixels(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pixels() -> long

        Returns a long containing a C++ 'unsigned char' pointer which points to the pixel data.
        This data is uncompressed and tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.
        """
    def readDepthMap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """readDepthMap(pathname) -> self

        Reads the depth map from the specified file and place the result into the depth map array of this MImage instance.
        """
    def readFromFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """readFromFile(pathname, type=kByte) -> self

        Attempt to identify and open the specified image file.

        * pathname (string) - the full path of the image file that should be opened.
        * type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type.
        """
    def readFromTextureNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """readFromTextureNode(fileTextureObject, type=kByte) -> self

        Attempt to read the content of the given file texture node.


        * fileTextureObject (MObject) - an object that refers to the file texture node that should be read.
        * type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type.
        """
    def release(self: Self, *args: Any, **kwargs: Any) -> Any:
        """release() -> self

        Release the current image. If there is no current image, the call is ignored.
        """
    def resize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resize(width, height, preserveAspectRatio=True) -> self

        Resize the currently opened image to the specified dimension, or to the closest
        width/height that is preserves the original aspect ratio.* width (unsigned int) - the desired image's width in pixels.
        * height (unsigned int) - the desired image's height in pixels.
        * preserveAspectRatio (bool) - specifies whether the aspect ratio should be preserved or not.
                 If this flag is set, the given width and height are interpreted as the maximum dimensions allowable.
        """
    def setDepthMap(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDepthMap(depth, width, heigth) -> self

        Specifies the depth map resolution and data.

        * depth (float*) - float buffer that contains depth values.
        * width (unsigned int) - the width of the depth buffer.
        * height (unsigned int) - the height of the depth buffer.

        * depth (MFloatArray) - float array that contains depth values.
        * width (unsigned int) - the width of the depth buffer.
        * height (unsigned int) - the height of the depth buffer.
        """
    def setFloatPixels(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFloatPixels(pixels, width, height, channels=4) -> self

        Copy the uncompressed pixels array passed in into the MImage.
        This array is tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

        * pixels (float*) - the variable containing a block of pixels.
        * width (unsigned int) - the variable that will be set to the image's width in pixels.
        * height (unsigned int) - the variable that will be set to the image's height in pixels.
        * channels (unsigned int) - the number of channels per pixel.
        """
    def setPixels(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPixels(pixels, width, height) -> self

        Copy the uncompressed pixels array passed in into the MImage.
        This array is tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

        * pixels (unsigned char*) - the variable containing a block of pixels.
        * width (unsigned int) - the variable that will be set to the image's width in pixels.
        * height (unsigned int) - the variable that will be set to the image's height in pixels.
        """
    def setRGBA(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRGBA(bool) -> self

        Sets a flag to indicate that pixel information is in RGBA sequence or BGRA sequence.
        Pixel data must have been allocated before this call is made.
        """
    def verticalFlip(self: Self, *args: Any, **kwargs: Any) -> Any:
        """verticalFlip() -> bool

        Flips the image vertically.
        """
    def writeToFile(self: Self, *args: Any, **kwargs: Any) -> Any:
        """writeToFile(pathname, outputFormat=iff) -> self

        Save the content of this image in a file. By default, the file is saved in IFF format.
        Optionally, the file can also be converted in a variety of image formats.
        """
    def writeToFileWithDepth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """writeToFileWithDepth(pathname, outputFormat=iff, writeDepth=False) -> self

        Save the content of this image in a file. By default, the file is saved in IFF format.
        Optionally, the file can also be converted in a variety of image formats.
        If the writeDepth parameter is True then any depth information stored in MImage will be written to file.
        """

class MInt64Array:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MIntArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MItCurveCV:
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Returns the current CV in the iteration as an MObject.
        """
    def hasHistoryOnCreate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasHistoryOnCreate() -> bool

        This method determines if the shape was created with history.

        If the object that this iterator is attached to is not a shape then this method will fail.
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current edge in the iteration.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the edges have been traversed yet.
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next edge in the iteration.
        """
    def position(self: Self, *args: Any, **kwargs: Any) -> Any:
        """position() -> MPoint

        Returns the position of the current CV.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(curve) -> self
        reset(curve, component=None) -> self

        Reset the iterator to the first CV of the curve.

        Reset the iterator to the first CV of the specified curve

        * curve (MObject) - The curve for the iteration

        Reset the iterator with the given curve and component.
        If component is None then the iteration will be for all CVs in the curve.

        * curve (MDagPath) - The curve to iterate over
        * component (MObject) - The CVs of the curve to iterate over
        """
    def setPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPosition(point, space=kObject) -> self

        Sets the position of the current CV, in the given transformation

        space.

        * point       (MPoint) - The new position for the specified vertex
        * space (MSpace constant) - The transformation space
        """
    def translateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """translateBy(vector, space=kObject) -> self

        Translate the current CV by the amount specified
        by the given vector.

        * vector (MVector) - The amount of translation
        * space (int) - The Transformation space
        """
    def updateCurve(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateCurve() -> self

        This method is used to signal the curve that it has been changed and needs to redraw itself.

        When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified.
        """

class MItDag:
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Retrieves DAG node to which the iterator points.
        """
    def depth(self: Self, *args: Any, **kwargs: Any) -> Any:
        """depth() -> integer

        Returns the height or depth of the current node in the DAG relative to the
        root node.  The root node has a depth of zero.
        """
    def fullPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """fullPathName() -> MString

        Return a string representing the full path from the root of the dag to this object.
        """
    def getAllPaths(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAllPaths() -> MDagPathArray

        Determines all DAG Paths to current item in the iteration.
        """
    def getPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPath() -> MDagPath

        Determines a DAG Path to the current item in the iteration.
        """
    def instanceCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """instanceCount(total) -> Integer

        Determines the number of times the current item (DAG node) in the iteration
        is instanced.

        If total is False the number of direct instances is returned, which
        is the same as the node's parent count.

        If total is True the total number of instances is returned, including
        indirect instances resulting from instancing higher up the DAG hierarchy
        (i.e. one or more of the node's ancestors also has multiple instances).
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates end of iteration path.
        """
    def isInstanced(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isInstanced(indirect = True) -> Bool

        Determines whether the current item (DAG node) in the iteration is directly
        or indirectly instanced.

        If indirect instance flag is False, the result is True if and only if the
        Node itself is multiply instanced (node.parentCount > 1).

        If the indirect flag is True, the result is True if and only if the Node
        itself is multiply instanced (node.parentCount > 1) or if the Node is not
        multiply instanced, but it has a directly instanced parent
        (node.parentCount()=1 and parent.parentCount >1).

        * indirect (Bool) -Indirect instance flag, defaults to True.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    kBreadthFirst: int = ...
    kDepthFirst: int = ...
    kInvalidType: int = ...

    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Moves to the next node matching the filter in the graph.
        """
    def partialPathName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """partialPathName() -> MString

        Return a string representing the partial path from the root of the
        dag to this object.

        The partial path is the minimum path that is still unique. This string
        may contain wildcards.
        """
    def prune(self: Self, *args: Any, **kwargs: Any) -> Any:
        """prune() -> self

        Prunes iteration tree at current node.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(rootObject, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
        reset(rootPath, traversalType = MItDag.kDepthFirst, filterType = MFn.kInvalid) -> self
        reset(dagInfoObject, rootObject OR rootPath, traversalType = MItDag.kDepthFirst) -> self


        Resets the iterator.
        When used without parameters, the iterator is reset to the previous traversal setting.
        If a dagInfoObject is used, then the type of the provided rootObject or rootPath must
        match dagInfoObject.objectType.

           rootObject (MObject) - Root node to begin the next traversal.
           rootPath (MDagPath) - Root path to to begin the next traversal. Useful with instances.
           dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           traversalType (MItDag.TraversalType) - Enumerated type that determines the direction of the traversal, defaults to kDepthFirst.
           filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid
        """
    def root(self: Self, *args: Any, **kwargs: Any) -> Any:
        """root() -> MObject

        Returns the root (start node) of the current traversal.
        The constructor sets the root of traversal to the world node.
        The root can be changed by the reset() method.
        """
    def traversalType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """traversalType() -> MItDag.TraversalType

        Returns the direction of the traversal.
        """
    @property
    def traverseUnderWorld(*args: Any, **kwargs: Any) -> Any:
        """Specifies whether underworld traversal is turned on (Bool)."""
    @traverseUnderWorld.setter
    def traverseUnderWorld(*args: Any, **kwargs: Any) -> Any:
        """Specifies whether underworld traversal is turned on (Bool)."""

class MItDependencyGraph:
    @property
    def currentDirection(*args: Any, **kwargs: Any) -> Any:
        """Direction of the iteration through the graph (MItDependencyGraph.Direction)."""
    @currentDirection.setter
    def currentDirection(*args: Any, **kwargs: Any) -> Any:
        """Direction of the iteration through the graph (MItDependencyGraph.Direction)."""
    @property
    def currentFilter(*args: Any, **kwargs: Any) -> Any:
        """Current node type filter (MFn.Type) ."""
    @currentFilter.setter
    def currentFilter(*args: Any, **kwargs: Any) -> Any:
        """Current node type filter (MFn.Type) ."""
    @property
    def currentLevel(*args: Any, **kwargs: Any) -> Any:
        """Level of the iteration through the graph (MItDependencyGraph.Level)."""
    @currentLevel.setter
    def currentLevel(*args: Any, **kwargs: Any) -> Any:
        """Level of the iteration through the graph (MItDependencyGraph.Level)."""
    def currentNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentNode() -> MObject

        Retrieves the current node of the iteration.  Results in a null object on
        failure or if the node is of a unrecognized type.
        """
    def currentNodeHasUnknownType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentNodeHasUnknownType() -> Bool

        Indicates whether or not the current node has an unrecognised
        type.  This is useful if an unexpected failure is encountered
        in the next() or currentNode() methods.
        """
    def currentPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentPlug() -> MPlug

        Retrieves the current plug of the iteration.  Results in a null
        plug on failure.
        """
    @property
    def currentRelationship(*args: Any, **kwargs: Any) -> Any:
        """Relationship mode of the iteration through the graph (MItDependencyGraph.Relationship)."""
    @currentRelationship.setter
    def currentRelationship(*args: Any, **kwargs: Any) -> Any:
        """Relationship mode of the iteration through the graph (MItDependencyGraph.Relationship)."""
    @property
    def currentTraversal(*args: Any, **kwargs: Any) -> Any:
        """Traversal mode of the iteration through the graph (MItDependencyGraph.Traversal)."""
    @currentTraversal.setter
    def currentTraversal(*args: Any, **kwargs: Any) -> Any:
        """Traversal mode of the iteration through the graph (MItDependencyGraph.Traversal)."""
    def getNodePath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNodePath() -> MObjectArray

        Retrieves the direct path from the current node to the root
        node.  Path does not include the current node.
        State of the provided array is undefined if this method fails.
        """
    def getNodesVisited(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNodesVisited() -> MObjectArray

        Retrieves all nodes visited during the iteration.
        State of the provided array is undefined if this method fails.
        """
    def getPlugPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPlugPath() -> MPlugArray

        Retrieves the direct path from the current plug to the root
        plug, with the current plug in element 0 of the array and the root
        plug in the final element of the array.

        Once the iterator is done (i.e. isDone() returns True) there is no
        longer a current plug and this method will return an empty array.

        If this method fails the state of the returned array is undefined.
        """
    def getPlugsVisited(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPlugsVisited() -> MPlugArray

        Retrieves all plugs visited during the iteration.
        State of the provided array is undefined if this method fails.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates whether or not all nodes or plugs have been iterated over
        in accordance with the direction, traversal, level, relationship and filter.
        If a valid filter is set, the iterator only visits those nodes that match
        the filter.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    kBreadthFirst: int = ...
    kConnectedTo: int = ...
    kDependsOn: int = ...
    kDepthFirst: int = ...
    kDownstream: int = ...
    kEvaluationGraph: int = ...
    kNodeLevel: int = ...
    kPlugLevel: int = ...
    kUpstream: int = ...

    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Iterates to the next node or plug in accordance with the
        direction, traversal, level, relationship and filter.  If a valid filter is
        set, the iterator only visits those nodes that match the
        filter.  When filtering is enabled nodes that have unknown type
        are treated as non-matching nodes.  With filtering disabled,
        iteration to a node with an unknown type is treated as a
        failure.  An attempt to iterate when there is nothing left to
        iterate over has no effect.
        """
    @property
    def nodeDepth(*args: Any, **kwargs: Any) -> Any:
        """Depth of the iteration through the graph (int)."""
    @nodeDepth.setter
    def nodeDepth(*args: Any, **kwargs: Any) -> Any:
        """Depth of the iteration through the graph (int)."""
    def previousPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """previousPlug() -> MPlug

        Retrieves the previous plug of the iteration.  Results in a
        null plug on failure.  Null plug may also indicate that the
        current plug is the root plug.
        """
    def prune(self: Self, *args: Any, **kwargs: Any) -> Any:
        """prune() -> self

        Prunes the search path at the current plug.  Iterator will not
        visit any of the plugs connected to the pruned plug.
        """
    @property
    def pruningOnFilter(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the iteration path is pruned automatically at nodes or plugs which do not match the filter (Bool)."""
    @pruningOnFilter.setter
    def pruningOnFilter(*args: Any, **kwargs: Any) -> Any:
        """Whether or not the iteration path is pruned automatically at nodes or plugs which do not match the filter (Bool)."""
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Clears iterator data and resets the iterator to the root node
        or plug.  If a valid filter is enabled, the iterator
        automatically advances to the next node after the root node
        that matches the filter.  If no matching node is found an
        exception is thrown.
        """
    def resetFilter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resetFilter() -> self

        Resets the node or plug filter to default, MFn.kInvalid
        (filter disabled).  Disables pruning on the filter (default).
        Resets the iterator.
        """
    def resetTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """resetTo(rootObject, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
        resetTo(rootPlug, filter = MFn.kInvalid, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self
        resetTo(infoObject, rootObject OR rootPlug, direction = MItDependencyGraph.kDownstream, traversal = MItDependencyGraph.kDepthFirst, level = MItDependencyGraph.kNodeLevel, relationship = MItDependencyGraph.kDependsOn) -> self


        Clears iterator data and re-initializes the iterator.  If a
        valid filter is provided, the iterator automatically advances
        to the next node after the root node that matches the filter.
        If no matching node is found an exception is thrown.


           rootObject (MObject) - Root node to begin the next traversal.
           rootPlug (MPlug) - Root plug to to begin the next traversal.
           infoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           filter (MFn.Type) - Function set type, defaults to MFn.kInvalid
           direction (MItDependencyGraph.Direction) - Primary direction of iteration, defaults to MItDependencyGraph.kDownstream
           traversal (MItDependencyGraph.Traversal) - Order of traversal, defaults to MItDependencyGraph.kDepthFirst
           level (MItDependencyGraph.Level) - Level of detail of the iteration, defaults to MItDependencyGraph.kNodeLevel
           relationship (MItDependencyGraph.Relationship) - Relationship mode of the iteration, defaults to MItDependencyGraph.kDependsOn
        """
    def rootNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rootNode() -> MObject

        Retrieves the root node of the iteration.
        """
    def rootPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rootPlug() -> MPlug

        Retrieves the root plug of the iteration.
        """
    @property
    def traversingOverWorldSpaceDependents(*args: Any, **kwargs: Any) -> Any:
        """Whether the iterator is set to traverse world-space attribute dependencies (Bool)."""
    @traversingOverWorldSpaceDependents.setter
    def traversingOverWorldSpaceDependents(*args: Any, **kwargs: Any) -> Any:
        """Whether the iterator is set to traverse world-space attribute dependencies (Bool)."""

class MItDependencyNodes:
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates end of the iteration.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Moves to the next node matching the filter.  If the filter
        is set to kInvalid, this method advances to the next
        DG node without doing any filtering.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(filterType = MFn.kInvalid) -> self
        reset(dagInfoObject) -> self


        Resets the iterator.


           dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid.
        """
    def thisNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """thisNode() -> MObject

        Retrieves the dependency node to which the iterator points.
        """

class MItGeometry:
    def allPositions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """allPositions() -> MStatus

        Return the position of all the points/CVs/vertices.  This
        operation is faster than using the iterator to get values one by
        one, but uses more memory as it requires an array to hold all the
        values to be returned.
        """
    def component(self: Self, *args: Any, **kwargs: Any) -> Any:
        """component() -> MObject

            DEPRECATED in 2019, use currentItem instead.
        This method returns the current component in the iteration.
        """
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int


        Return the number of items in this iteration. This number will
        always be at least as large as the number of items, however in
        some cases it may be larger. It is useful if allocating space in
        an array to hold the results, since it will always be of
        sufficient size. If the exact number of items is required, use the
        exactCount method instead. The exactCount method is however
        significantly slower than this method.
        """
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        This method returns the current component in the iteration.
        """
    def exactCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """exactCount() -> int


        Return the exact number of items in this iteration. This method is
        significantly slower than the count() method, so use if only if
        the precise number is required.
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int


        This method returns the index of the current point/CV/vertex
        component in the iteration.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates end of the iteration.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next component in the iteration.
        If the iterator is already at the last component then this
        method has no effect. Use isDone to determine if the iterator
        is at the last component.
        """
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """normal() -> MVector

        Return the normal of the current point/CV/vertex component.
        """
    def position(self: Self, *args: Any, **kwargs: Any) -> Any:
        """position() -> MPoint

        Return the position of the current point/CV/vertex component.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self


        Resets the iterator.
        """
    def setAllPositions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAllPositions() -> MStatus

        Set the position of all the points/CVs/vertices at once. This
        operation is faster than using the iterator to set values one by
        one, but uses more memory as it requires an array to hold all the
        values to be set.
        """
    def setPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPosition() -> MStatus

        Set the position of the current point/CV/vertex.
        """
    def weight(self: Self, *args: Any, **kwargs: Any) -> Any:
        """weight() -> MWeight

        Return the weight of the current point/CV/vertex component.
        """

class MItMeshEdge:
    def center(self: Self, *args: Any, **kwargs: Any) -> Any:
        """center(space=kObject) -> MPoint

        Returns the center point of the edge, in the given transformation space.

        * space (MSpace constant) - The  transformation space
        """
    def connectedToEdge(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connectedToEdge(index) -> bool

        Determines whether the given edge is connected to the current edge.

        * index (int) - Index of edge to check.
        """
    def connectedToFace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connectedToFace(index) -> bool

        Determines whether the given face contains the current edge.

        * index (int) - Index of face to check.
        """
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Return the number of edges in the iteration
        """
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Returns the current edge in the iteration as a component.

        Components are used to specify one or more edges and are useful in operating on groups of non-contiguous edges for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
    def geomChanged(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Resets the geom pointer in the MItMeshEdge. If you're using MFnMesh to
        update Normals or Color per vertex while iterating, you must call geomChanged
        on the iterator immediately after the MFnMesh call to make sure that your
        geometry is up to date. A crash may result if this method is not called.
        A similar approach must be taken for updating upstream vertex tweaks
        with an MPlug. After the update, call this method.
        """
    def getConnectedEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedEdges() -> MIntArray

        Returns the indices of edges connected to the current edge.
        """
    def getConnectedFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedFaces() -> MIntArray

        Returns the indices of the faces connected to the current edge.
        Normally a boundary edge will only have one face connected to it and
        an internal edge will have two, but if the mesh has manifold geometry
        then the edge may have three or more faces connected to it.
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current edge in the iteration.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the edges have been traversed yet.
        """
    @property
    def isSmooth(*args: Any, **kwargs: Any) -> Any:
        """True if the edge is smooth, False if it is hard."""
    @isSmooth.setter
    def isSmooth(*args: Any, **kwargs: Any) -> Any:
        """True if the edge is smooth, False if it is hard."""
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def length(self: Self, *args: Any, **kwargs: Any) -> Any:
        """length(space=kObject) -> float

        Returns the length of the edge, in the given transformation space.

        * space (MSpace constant) - The  transformation space
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next edge in the iteration.
        """
    def numConnectedEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedEdges() -> int

        Returns the number of edges connected to the current edge.
        """
    def numConnectedFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedFaces() -> int

        Returns the number of faces connected to the current edge.
        """
    def onBoundary(self: Self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary() -> bool

        Determines if the current edge is a border edge.
        """
    def point(self: Self, *args: Any, **kwargs: Any) -> Any:
        """point(whichVertex, space=kObject) -> MPoint

        Returns the position of one of the current edge's vertices, int the
        given transformation space.

        * whichVertex    (0 or 1) - Which of the edge's two vertices to return
        * space (MSpace constant) - The transformation space
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(mesh) -> self
        reset(mesh, component=None) -> self

        Reset the iterator to the first edge of the mesh.

        Reset the iterator to the first edge of the specified mesh

        * mesh (MObject) - The polygon for the iteration

        Reset the iterator with the given mesh and component.
        If component is None then the iteration will be for all edges in the mesh.

        * mesh (MDagPath) - The mesh to iterate over
        * component (MObject) - The edges of the mesh to iterate over
        """
    def setIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(index) -> int

        Sets the index of the current edge to be accessed. The current edge
        will no longer be in sync with any previous iteration.

        Returns the index of the edge which was current before the change.


        * index (int) - The index of desired edge to access.
        """
    def setPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(point, whichVertex, space=kObject) -> self

        Sets the position of one of the current edge's vertices, in the given
        transformation space.

        * point       (MPoint) - The new position for the specified vertex
        * whichVertex (0 or 1) - Which of the edge's 2 vertices to set.
        * space (MSpace constant) - The transformation space
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Tells Maya that mesh has been changed and needs to redraw itself.
        """
    def vertexId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexId(whichVertex) -> int

        Returns the global index (as opposed to face-relative index) of one of
        the edge's vertices.

        * whichVertex (0 or 1) - Which of the edge's 2 vertices to use.
        """

class MItMeshFaceVertex:
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Returns the current faceVertex as a double-indexed component.
        """
    def faceId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """faceId() -> int

        Returns the current face index.
        """
    def faceVertexId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """faceVertexId() -> int

        Returns the relative index of the vertex within the current face. This
        index together with the faceId can be used for a fast access to get
        various info stored per vertex (normals, uvs, colors).
        """
    def geomChanged(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Resets the geom pointer in the MItMeshFaceVertex. If you're using
        MFnMesh to update Normals or Color per vertex while iterating, you
        must call geomChanged on the iterator immediately after the MFnMesh
        call to make sure that your geometry is up to date. A crash may result
        if this method is not called. A similar approach must be taken for
        updating upstream vertex tweaks with an MPlug. After the update, call
        this method.
        """
    def getBinormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getBinormal(space=MSpace.kObject, uvSet='') -> MVector

        Returns the face vertex binormal associated with the UV set.
        """
    def getColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorSetName='') -> MColor

        Returns a color of the current face vertex.
        """
    def getColorIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndex(colorSetName='') -> int

        Return a color index of the current face vertex.
        """
    def getNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormal(space=MSpace.kObject) -> MVector

        Returns the face vertex normal.
        """
    def getTangent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTangent(space=MSpace.kObject, uvSet='') -> MVector

        Returns the face vertex tangent associated with the given UV set. The
        tangent is defined as the surface tangent of the polygon running in
        the U direction.
        """
    def getUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvSet='') -> (float, float)

        Returns the texture coordinate for the current face vertex.
        """
    def getUVIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndex(uvSet='') -> int

        Returns the index of the texture coordinate for the current face
        vertex. This index refers to an element of the mesh's texture
        coordinate array as returned by MFnMesh::getUVs().
        """
    def hasColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasColor() -> bool

        Returns whether the current face vertex has a color-per-vertex set.
        """
    def hasUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUVs(uvSet='') -> bool

        Returns whether the current face vertex has UVs mapped in the given
        set.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the face vertices have been traversed.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next face vertex in the iteration.
        """
    def normalId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """normalId() -> int

        Returns the normal index for the specified vertex. This index refers
        to an element in the normal array returned by MFnMesh::getNormals().
        These normals are per-face per-vertex normals.
        """
    def position(self: Self, *args: Any, **kwargs: Any) -> Any:
        """position(space=MSpace.kObject) -> MPoint

        Returns the position of the current face vertex.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(mesh) -> self
        reset(mesh, component=None) -> self

        Reset the iterator to the first face vertex of the mesh.

        Reset the iterator to the first face vertex of the specified mesh.

        * mesh (MObject) - The mesh for the iteration

        Reset the iterator with the given mesh and component.
        If component is None then the iteration will be for all face vertices in the mesh.

        * mesh (MDagPath) - The mesh to iterate over
        * component (MObject) - The faces of the mesh to iterate over
        """
    def setIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(faceId, faceVertexId) -> (oldFaceId, oldFaceVertexId)

        Sets the index of the current face vertex to be accessed. The current
        face vertex will no longer be in sync with any previous iteration.

        Returns the indices of the old face and vertex.


        * faceId (int) - Index of desired face to access.
        * faceVertexId (int) - Face-relative index of desired vertex to access.
        * oldFaceId (int) - Index of the face which was current before the change.
        * oldFaceVertexId (int) - Face-relative index of the vertex which was current before the change.
        """
    def tangentId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """tangentId() -> int

        Returns the tangent index for the current face vertex. This index
        refers to an element in the array returned by MFnMesh::getTangents.
        These tangents are per-face per-vertex.
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Tells Maya that mesh has been changed and needs to redraw itself.
        """
    def vertexId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexId() -> int

        Returns the global (as opposed to face-relative) index of the
        current vertex.
        """

class MItMeshPolygon:
    def center(self: Self, *args: Any, **kwargs: Any) -> Any:
        """center(space=kObject) -> MPoint

        Return the position of the center of the current polygon

        * space (int) - The coordinate system for this operation
        """
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Return the number of polygons in the iteration
        """
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Get the current polygon in the iteration as a component.

        Components are used to specify one or more polygons and are usefull in operating on groups of non-contiguous polygons for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
    def geomChanged(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Reset the geom pointer in the MItMeshPolygon. This is now being handled automatically inside the iterator, and users should no longer need to call this method directly to sync up the iterator to changes made by MFnMesh
        """
    def getArea(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getArea(space=kObject) -> float

        This method gets the area of the face

        * space (int) - World Space or Object Space
        """
    def getColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorSetName=None) -> MColor
        getColor(vertexIndex) -> MColor

        This method gets the color of the specified vertex in this face

        * index (int) - The face-relative vertex index on this face

        Or the average color of the all the vertices in this face

        * colorSetName (string) - Name of the color set.
        """
    def getColorIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndex(vertexIndex, colorSetName=None) -> int

        This method returns the colorIndex for a vertex of the current face.

        * vertexIndex (int) - Face-relative index of vertex.
        * colorSetName (string) - Name of the color set.
        """
    def getColorIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndices(colorSetName=None) -> MIntArray

        This method returns the colorIndices for each vertex on the face.

        * colorSetName (string) - Name of the color set.
        """
    def getColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColors(colorSetName=None) -> MColorArray

        This method gets the color of the each vertex in the current face.

        * colorSetName (string) - Name of the color set.
        """
    def getConnectedEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedEdges() -> MIntArray

        This method gets the indices of the edges connected to the vertices of the current face, but DOES not include the edges contained in the current face
        """
    def getConnectedFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedFaces() -> MIntArray

        This method gets the indices of the faces connected to the current face.
        """
    def getConnectedVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedVertices() -> MIntArray

        This method gets the object-relative indices of the vertices surrounding the vertices of the current face, but does not include the vertices of the current face
        """
    def getEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getEdges() -> MIntArray

        This method gets the indices of the edges contained in the current face.
        """
    def getNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormal(space=kObject) -> MVector
        getNormal(vertexIndex, [space=]kObject) -> MVector

        Return the face normal of the current polygon.

        * space (int) - The transformation space. The keyword 'space' has to be explicitly stated. If not present, the argument will be identified as a 'vertexIndex' argument, and the second form of this function will be used instead.

        Returns the vertex-face normal for the vertex in the current polygon.

        * index (int) - face-relative vertex index of the vertex whose normal to retrieve
        * space (int) - The transformation space. Defaults to kObject, the keyword 'space' is optional as well.
        """
    def getNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormals(space=kObject) -> MVectorArray

        Returns the normals for all vertices in the current face

        * space (int) - The transformation space
        """
    def getPointAtUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtUV(uvPoint, space=kObject, uvSet=None, tolerance=0) -> MPoint

        Return the position of the point at the given UV value in the current polygon.

        * uvPoint ([float, float]) - The UV value to try to locate
        * space (int) - The coordinate system for this operation
        * uvSet (string) - UV set to work with
        * tolerance (float) - tolerance value to compare float data type
        """
    def getPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPoints(space=kObject) -> MPointArray

        Retrieves the positions of the vertices on the current face/polygon that the iterator is pointing to. Vertex positions will be inserted into the given array and will be indexed using face-relative vertex IDs (ie. ordered from 0 to (vertexCount of the face) - 1), which should not be confused with the vertexIDs of each vertex in relation to the entire mesh object.

        * space (int) - The coordinate system for this operation
        """
    def getTriangle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTriangle(localTriIndex, space=kObject) -> [MPointArray, MIntArray]

        Get the vertices and vertex positions of the given triangle in the current face's triangulation.

        * localTriIndex (int) - Local index of the desired triangle in this face
        * space (int) - World Space or Object Space
        """
    def getTriangles(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getTriangles(space=kObject) -> [MPointArray, MIntArray]

        Get the vertices and vertex positions of all the triangles in the current face's triangulation

        * space (int) - World Space or Object Space
        """
    def getUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUV(vertexId, uvSet=None) -> [float, float]

        Return the texture coordinate for the given vertex.

        * vertex (int) - The face-relative vertex index to get UV for
        * uvSet (string) - UV set to work with
        """
    def getUVArea(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVArea(uvSet=None) -> float

        This method gets the UV area of the face

        * uvSet (string) - UV set to work with
        """
    def getUVAtPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVAtPoint(pt, space=kObject, uvSet=None) -> [float, float]

        Find the point closest to the given point in the current polygon, and return the UV value at that point.

        * pt (MPoint) - The point to try to get UV for
        * space (int) - The coordinate system for this operation
        * uvSet (string) - UV set to work with
        """
    def getUVIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndex(vertex, uvSet=None) -> int

        Returns the index of the texture coordinate for the given vertex.
        This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

        * vertex (int) - The face-relative vertex index of the current polygon
        * uvSet (string) - UV set to work with
        """
    def getUVIndexAndValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndexAndValue(vertex, uvSet=None) -> [int, float, float]

        Return the index and value of the texture coordinate for the given vertex. This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

        * vertex (int) - The face-relative vertex index of the current polygon
        * uvSet (string) - UV set to work with
        """
    def getUVSetNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetNames() -> list of strings

        This method is used to find the UV set names mapped to the current face
        """
    def getUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVs(uvSet=None) -> [MFloatArray, MFloatArray]

        Return the all the texture coordinates for the vertices of this face (in local vertex order).

        * uvSet (string) - UV set to work with
        """
    def getVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getVertices() -> MIntArray

        This method gets the indices of the vertices of the current face
        """
    def hasColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasColor() -> bool
        hasColor(localVertexIndex) -> bool

        This method determines whether the current face has color-per-vertex set for any or the given vertex

        * localVertexIndex (int) - face-relative vertex index to check for color on
        """
    def hasUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasUVs(uvSet=None) -> bool

        Tests whether this face has UV's mapped or not (either all the vertices for a face should have UV's, or none of them do, so the UV count for a face is either 0, or equal to the number of vertices).

        * uvSet (string) - UV set to work with
        """
    def hasValidTriangulation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasValidTriangulation() -> bool

        This method checks if the face has a valid triangulation. If it doesn't, then the face was bad geometry: it may gave degenerate points or cross over itself.
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current polygon
        """
    def isConnectedToEdge(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isConnectedToEdge(index) -> bool

        This method determines whether the given face is adjacent to the current face

        * index (int) - Index of the face to be tested for
        """
    def isConnectedToFace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isConnectedToFace(index) -> bool

        This method determines whether the given face is adjacent to the current face

        * index (int) - Index of the face to be tested for
        """
    def isConnectedToVertex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isConnectedToVertex(index) -> bool

        This method determines whether the given vertex shares an edge with a vertex in the current face

        * index (int) - Index of the face to be tested for
        """
    def isConvex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isConvex() -> bool

        This method checks if the face is convex.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the polygons have been traversed yet.
        """
    def isHoled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isHoled() -> bool

        This method checks if the face has any holes.
        """
    def isLamina(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isLamina() -> bool

        This method checks if the face is a lamina (the face is folded over onto itself).
        """
    def isPlanar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPlanar() -> bool

        This method checks if the face is planar
        """
    def isStarlike(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isStarlike() -> bool

        This method checks if the face is starlike. That is, a line from the centre to any vertex lies entirely within the face.
        """
    def isUVReversed(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isUVReversed(faceId) -> bool

        Returns True if the texture coordinates (uv's) for the face are
        reversed (clockwise), False if they are not reversed (counter clockwise).
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next polygon in the iteration.
        """
    def normalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """normalIndex(vertex) -> int

        Returns the normal index for the specified vertex.
        This index refers to an element in the normal array returned by MFnMesh.getNormals.  These normals are per-polygon per-vertex normals. See the MFnMesh description for more information on normals.

        * localVertexIndex (int) - The face-relative index of the vertex to examine for the current polygon
        """
    def numColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numColors(colorSetName=None) -> int

        This method checks for the number of colors on vertices in this face

        * colorSetName (string) - Name of the color set.
        """
    def numConnectedEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedEdges() -> int

        This method checks for the number of connected edges on the vertices of this face
        """
    def numConnectedFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedFaces() -> int

        This method checks for the number of connected faces
        """
    def numTriangles(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numTriangles() -> int

        This Method checks for the number of triangles in this face in the current triangulation
        """
    def onBoundary(self: Self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary() -> bool

        This method determines whether the current face is on a boundary
        """
    def point(self: Self, *args: Any, **kwargs: Any) -> Any:
        """point(index, space=kObject) -> MPoint

        Return the position of the vertex at index in the current polygon.

        * index (int) - The face-relative index of the vertex in the current polygon
        * space (int) - The coordinate system for this operation
        """
    def polygonVertexCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """polygonVertexCount() -> int

        Return the number of vertices for the current polygon
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(polyObject) -> self
        reset(polyObject, component=None) -> self

        Reset the iterator to the first polygon

        Reset the iterator to the first polygon in the supplied surface

        * polyObject (MObject) - The polygon for the iteration

        Reset the iterator with the given surface and component.
        If component is None then the iteration will be for all polygons in the given surface.

        * polyObject (MDagPath) - The surface (mesh) to iterate over
        * component (MObject) - The polygons (faces) of the polyObject to iterate over
        """
    def setIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(index) -> int

        This method sets the index of the current face to be accessed.
        The current face will no longer be in sync with any previous iteration.
        Returns the index of the current face in the iteration

        * index (int) - The index of desired face to access.
        """
    def setPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(point, index, space=kObject) -> self

        Set the vertex at the given index in the current polygon.

        * point (MPoint) - The new position for the vertex
        * index (int) - The face-relative index of the vertex in the current polygon
        * space (int) - The coordinate system for this operation
        """
    def setPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPoints(pointArray, space=kObject) -> self

        Sets new locations for vertices of the current polygon that the iterator is pointing to.

        * pointArray (MPointArray) - The new positions for the vertices.
        * space (int) - The coordinate system for this operation.
        """
    def setUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUV(vertexId, uvPoint, uvSet=None) -> self

        Modify the UV value for the given vertex in the current face.
        If the face is not already mapped, this method will fail.

        * vertexId (int) - face-relative index of the vertex to set UV for.
        * uvPoint ([float, float]) - The UV values to set it to
        * uvSet (string) - UV set to work with
        """
    def setUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUVs(uArray, vArray, uvSet=None) -> self

        Modify the UV value for all vertices in the current face.
        If the face has not already been mapped, this method will fail.

        * uArray (MFloatArray) - All the U values - in local face order
        * vArray (MFloatArray) - The corresponding V values
        * uvSet (string) - UV set to work with
        """
    def tangentIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """tangentIndex(localVertexIndex) -> int

        Returns the tangent (or binormal) index for the specified vertex.
        This index refers to an element in the normal array returned by MFnMesh.getTangents. These tangent or binormals are per-polygon per-vertex.
        See the MFnMesh description for more information on tangents and binormals.

        * localVertexIndex(int) - The face-relative index of the vertex to examine for the current polygon
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signal that this polygonal surface has changed and needs to redraw itself.
        """
    def vertexIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexIndex(index) -> int

        Returns the object-relative index of the specified vertex of the current polygon.
        The index returned may be used to refer to an element in the vertex list returned by MFnMesh.getPoints.

        * index (int) - The face-relative index of the vertex in the polygon
        """
    def zeroArea(self: Self, *args: Any, **kwargs: Any) -> Any:
        """zeroArea() -> bool

        This method checks if its a zero area face
        """
    def zeroUVArea(self: Self, *args: Any, **kwargs: Any) -> Any:
        """zeroUVArea(uvSet=None) -> bool

        This method checks if the UV area of the face is zero

        * uvSet (string) - UV set to work with
        """

class MItMeshVertex:
    def connectedToEdge(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connectedToEdge(index) -> bool

        This method determines whether the given edge contains the current vertex

        * index (int) - Index of edge to check.
        """
    def connectedToFace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connectedToFace(index) -> bool

        This method determines whether the given face contains the current vertex

        * index (int) - Index of face to check.
        """
    def count(self: Self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Return the number of vertices in the iteration
        """
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Get the current vertex in the iteration as a component.

        Components are used to specify one or more vertices and are usefull in operating on groups of non-contiguous vertices for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
    def geomChanged(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Reset the geom pointer in the MItMeshVertex. If you're using MFnMesh to
        update Normals or Color per vertex while iterating, you must call geomChanged
        on the iteratior immediately after the MFnMesh call to make sure that your
        geometry is up to date. A crash may result if this method is not called.
        A similar approach must be taken for updating upstream vertex tweaks
        with an MPlug. After the update, call this method.
        """
    def getColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorSetName=None) -> MColor
        getColor(faceIndex, colorSetName=None) -> MColor

        This method gets the average color of the vertex

        * colorSetName (string) - Name of the color set.

        This method gets the color of the current vertex in the specified face

        * index (int) - The face to get the color for this vertex for* colorSetName (string) - Name of the color set.
        """
    def getColorIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndices(colorSetName=None) -> MIntArray

        This method returns the colorIndices into the color array see MFnMesh::getColors()
        of the current vertex.

        * colorSetName (string) - Name of the color set.
        """
    def getColors(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getColors(colorSetName=None) -> MColorArray

        This method gets the colors of the current vertex for each face it
        belongs to. If no colors are assigned to the vertex at all, the
        return values will be (-1 -1 -1 1). If some but not all of the
        vertex/face colors have been explicitly set, the ones that have not
        been set will be (0, 0, 0, 1).

        * colorSetName (string) - Name of the color set.
        """
    def getConnectedEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedEdges() -> MIntArray

        This method gets the indices of the edges contained in the current vertex.
        """
    def getConnectedFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedFaces() -> MIntArray

        This method gets the indices of the faces connected to the current vertex.
        """
    def getConnectedVertices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedVertices() -> MIntArray

        This method gets the indices of the vertices surrounding the current vertex.
        """
    def getNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormal(space=kObject) -> MVector
        getNormal(faceIndex, space=kObject) -> MVector

        Return the normal or averaged normal if unshared of the current vertex.

        * space (int) - The transformation space

        Return the normal of the current vertex in the specified face.

        * faceIndex (int) - face index to get normal for
        * space (int) - The transformation space
        """
    def getNormalIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormalIndices() -> MIntArray

        This method returns the normal indices of the face/vertex associated
        with the current vertex.
        """
    def getNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNormals(space=kObject) -> MVectorArray

        Return the normals of the current vertex for all faces

        * space (int) - The transformation space
        """
    def getOppositeVertex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getOppositeVertex(edgeId) -> int

        This method gets the other vertex of the given edge

        * edgeId (int) - The edge to get the other vertex for
        """
    def getUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvSet=None) -> [float, float]getUV(faceId, uvSet=None) -> [float, float]

        Get the shared UV value at this vertex.

        * uvSet (string) - Name of the uv set to work with.

        Get the UV value for the give facen at the current vertex.

        * faceId (int) - Index of the required face
        * uvSet (string) - Name of the uv set to work with
        """
    def getUVIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndices(uvSet=None) -> MIntArray

        This method returns the uv indices into the normal array see MFnMesh::getUVs()
        of the current vertex.

        * uvSet (string) - Name of the uv set.
        """
    def getUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUVs(uvSet=None) -> [MFloatArray, MFloatArray, MIntArray]

        Get the UV values for all mapped faces at the current vertex.
        If at least one face was mapped the method will succeed.

        * uvSet (string) - Name of the uv set to work with
        """
    def hasColor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasColor() -> bool
        hasColor(index) -> bool

        This method determines whether the current Vertex has a color set
        for one or more faces.

        * index (int) - Index of face to check
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current vertex in the vertex list for this
        polygonal object.
        Polygonal objects contain a list of vertices. Faces and edges are
        specified as indicies from this list, in this way vertices can
        be shared amoung faces and edges.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the vertices have been traversed yet.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next edge in the iteration.
        """
    def numConnectedEdges(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedEdges() -> int

        This Method checks for the number of connected Edges on this vertex
        """
    def numConnectedFaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedFaces() -> int

        This Method checks for the number of Connected Faces
        """
    def numUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """numUVs(uvSet=None) -> int

        This method returns the number of unique UVs mapped on this vertex

        * uvSet (string) - Name of the uv set to work with
        """
    def onBoundary(self: Self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary() -> bool

        This method determines whether the current vertex is on a Boundary
        """
    def position(self: Self, *args: Any, **kwargs: Any) -> Any:
        """position(space=kObject) -> MPoint

        Return the position of the current vertex in the specified space.
        Object space ignores all transformations for the polygon, world space
        includes all such transformations.

        * space (int) - The  transformation space
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(polyObject) -> self
        reset(polyObject, component=None) -> self

        Reset the iterator to the first polygon

        Reset the iterator to the first polygon in the supplied polygon

        * polyObject (MObject) - The polygon for the iteration

        Reset the iterator with the given surface and component.
        If component is None then the iteration will be for all vertices in the given polygon.

        * polyObject (MDagPath) - The surface (mesh) to iterate over
        * component (MObject) - The vertices of the polyObject to iterate over
        """
    def setIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(index) -> int

        This method sets the index of the current vertex to be accessed.
        The current vertex will no longer be in sync with any previous iteration.

        * index (int) - The index of desired vertex to access.
        """
    def setPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPosition(point, space=kObject) -> self

        Set the position of the current vertex in the given space.

        * point (MPoint) - The new position for the current vertex
        * space (int) - The Transformation space
        """
    def setUV(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUV(uvPoint, uvSet=None) -> selfsetUV(faceId, uvPoint, uvSet=None) -> self

        Set the shared UV value at this vertex

        * uvPoint ([float, float]) - The UV values to set
        * uvSet (string) - Name of the UV set to work with

        Set the UV value for the given face at the current vertex

        * faceId (int) - Index of required face
        * uvPoint ([float, float]) - The UV values to set
        * uvSet (string) - Name of the UV set to work with
        """
    def setUVs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUVs(uArray, vArray, faceIds, uvSet=None) -> self

        Set the UV value for the specified faces at the current vertex.
        If the face is not already mapped, the value will not be set.
        If at least ne face was previously mapped, the method should succeed.
        If no faces were mapped, the method will fail.

        * uArray (MFloatArray) - All the U values - in local face order
        * vArray (MFloatArray) - The corresponding V values
        * faceIds (MIntArray) - The corresponding face Ids
        * uvSet (string) - UV set to work with
        """
    def translateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """translateBy(vector, space=kObject) -> self

        Translate the current vertex by the amount specified
        by the given vector.

        * vector (MVector) - The amount of translation
        * space (int) - The Transformation space
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signal that this polygonal surface has changed and needs to redraw itself.
        """

class MItSelectionList:
    def getComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getComponent() -> (MDagPath, MObject)

        This method retrieves the dag path and the component of the current selection item.
        """
    def getDagPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDagPath() -> MDagPath

        This method retrieves the dag path of the current selection item.
        """
    def getDependNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDependNode() -> MObject

        This method retrieves the dependency node of the current selection itemRaises kFailure if there is no dependency node associated with the current item
        """
    def getPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPlug() -> MPlug

        This method retrieves the plug of the current selection item.
        """
    def getStrings(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getStrings() -> list of strings

        Get the string representation of the current item in the selection list.
        It is possible that it will require more than one string to represent the item (the item may contain groups of CVs for example)
        """
    def hasComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasComponents() -> bool

        Returns whether or not the current selection item has components.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Specifies whether or not there is anything more to iterator over.
        """
    def itemType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """itemType() -> int

        Returns the current selection item type.

          kDagSelectionItem    selection item is in the DAG
          kAnimSelectionItem   selection item is a keyset
          kDNselectionItem     selection item is a dependency node
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    kAnimSelectionItem: int = ...
    kDNselectionItem: int = ...
    kDagSelectionItem: int = ...
    kPlugSelectionItem: int = ...
    kUnknownItem: int = ...

    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next item. If components are selected then advance to next component.

        If a filter is specified then the next item will be one that matches the filter.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Reset the iterator.
        If a filter has been specified then the current item will be the first selected item that matches the filter.
        """
    def setFilter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFilter(filter) -> self

        Apply a filter to the iteration.
        Selection items not matching the filter type will be excluded from the iteration.
        """

class MItSurfaceCV:
    def currentItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Get the current CV in the iteration as a component.

        Components are used to specify one or more CVs and are useful in operating on groups of non-contiguous CVs for a curve or surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """
    def hasHistoryOnCreate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasHistoryOnCreate() -> bool

        This method determines if the shape was created with history.

        If the object that this iterator is attached to is not a shape then this method will raise.
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Get the index of the current CV as it appears in CV array for this surface.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Returns True if the iteration is finished, i.e. there are no more CVs to iterate on.
        """
    def isRowDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isRowDone() -> bool

        Returns True if the current row has no more CVs to iterate over.
        The row can be in the U or V direction depending on what value of useURows has been set in the constructor.
        """
    def iter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """
    def iternext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next CV in the iteration.
        If the iterator is already at the last CV then this method has no effect. Use isDone() to determine if the iterator is at the last CV.
        """
    def nextRow(self: Self, *args: Any, **kwargs: Any) -> Any:
        """nextRow() -> self

        Advance to the next row in the iteration.
        The row can be in the U or V direction depending on what value of useURows has been set in the constructor.
        """
    def position(self: Self, *args: Any, **kwargs: Any) -> Any:
        """position(space=kObject) -> MPoint

        Returns the position of the current CV in the iteration in the specified space.

        * space (int) - The coordinate space in which the CV is set
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(surface, useURows=True) -> self
        reset(surface, component, useURows=True) -> self

        Reset the iterator to the first CV.

        Or
        Reset the iterator to iterate over all CVs on the specified surface.

        * surface (MObject) - The surface for the iteration
        * useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.

        Or
        Reset the iterator to iterate over the CVs of the given surface that are specified in the given component. If the component is NULL then the iteration will be over all CVs on the surface.

        * surface (MDagPath) - The surface for the iteration
        * component (MObject) - A group of CVs to be iterated on
        * useURows (bool) - If True then the iterator will iterate in the U direction, otherwise it will be in the V direction.
        """
    def setPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPosition(point, space=kObject) -> self

        Set the position of the current CV in the iteration to the specified point.

        * point (MPoint) - The new position for the current CV in the iteration
        * space (int) - The coordinate space in which the CV is set
        """
    def translateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """translateBy(vector, space=kObject) -> self

        Move the current CV in the iteration by the sepcified vector.

        * vector (MVector) - The translation vector
        * space (int) - The coordinate space in which the CV is set
        """
    def updateSurface(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        This method is used to signal the surface that it has been changed and needs to redraw itself.

        When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified.
        """
    def uvIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """uvIndices() -> (indexU, indexV)

        Get the u and v index of the current CV.
        """

class MIteratorType:
    @property
    def filterList(*args: Any, **kwargs: Any) -> Any:
        """Filter list (MIntArray containing MFn.Type)."""
    @filterList.setter
    def filterList(*args: Any, **kwargs: Any) -> Any:
        """Filter list (MIntArray containing MFn.Type)."""
    @property
    def filterListEnabled(*args: Any, **kwargs: Any) -> Any:
        """Whether the we are using a single filter on the iterator or a filter list (Boolean)."""
    @filterListEnabled.setter
    def filterListEnabled(*args: Any, **kwargs: Any) -> Any:
        """Whether the we are using a single filter on the iterator or a filter list (Boolean)."""
    @property
    def filterType(*args: Any, **kwargs: Any) -> Any:
        """Filter type (MFn.Type)."""
    @filterType.setter
    def filterType(*args: Any, **kwargs: Any) -> Any:
        """Filter type (MFn.Type)."""
    kMDagPathObject: int = ...
    kMObject: int = ...
    kMPlugObject: int = ...

    @property
    def objectType(*args: Any, **kwargs: Any) -> Any:
        """Object type (MIteratorType.objFilterType)."""
    @objectType.setter
    def objectType(*args: Any, **kwargs: Any) -> Any:
        """Object type (MIteratorType.objFilterType)."""

class MLockMessage(MMessage):
    kAddAttr: int = ...
    kChildReorder: int = ...
    kCreateChildInstance: int = ...
    kCreateNodeInstance: int = ...
    kCreateParentInstance: int = ...
    kLast: int = ...
    kLastDAG: int = ...
    kLastPlug: int = ...
    kLockAttr: int = ...
    kLockNode: int = ...
    kPlugAttrValChange: int = ...
    kPlugConnect: int = ...
    kPlugDisconnect: int = ...
    kPlugRemoveAttr: int = ...
    kPlugRenameAttr: int = ...
    kRemoveAttr: int = ...
    kRenameAttr: int = ...
    kReparent: int = ...
    kUnlockAttr: int = ...
    kUnlockNode: int = ...

    def setNodeLockDAGQueryCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setNodeLockDAGQueryCallback(dagPath, function, clientData=None) -> id

        This methods registers a callback that is invoked in any situation
        involving a locking condition on DAG level changes.  When called,
        the API user can make a decision on how to handle the given locking
        situation. The programmer can either accept the default action, or
        they can deny the default action. The decision is returned through a
        decision variable which is passed to the callback function.

        The callback function takes the following parameters:
         * dagPath - The DAG path that the event occurred on.
         * otherPath - The other path involved, e.g. the new parent.
         * clientData - User defined data passed to the callback function.
         * eventType - Description of the event.
        And return True to accept the default behavior and False to
        reject it.

         The meanings of the dagPath and otherPath parameters for each
        eventType, and default actions associated with those event types, are
        as follows:

        kGroup
         * dagPath - Path of the node to be grouped.
         * otherPath - Path of the group node.
         * default actions - If dagPath
           is locked then the default action is to not allow the grouping.
           If dagPath is unlocked then dagPath
           can be grouped with otherPath.

        kUnGroup
         * dagPath - Path of the node attempted to ungroup.
         * otherPath - Path of the group node.
         * default actions - If dagPath is locked then
           the default action is to not allow the ungrouping. If dagPath
           is unlocked then dagPath can be ungrouped from otherPath.

        kReparent
         * dagPath - Path of the node which is being reparented.
         * otherPath - Path of the new parent, if any. When
           reparenting to the world, otherPath will be invalid.
         * default actions - If dagPath is locked then
           the default action is to not allow the reparenting. If dagPath
           is unlocked then dagPath can be parented to otherPath.

        kChildReorder
         * dagPath - Path of the child node to be reordered.
         * otherPath - Path of the parent node.
         * default actions - If dagPath is locked then
           the default action is to not allow the reordering. If dagPath
           is unlocked then dagPath can be reordered on otherPath.

        kCreateNodeInstance
         * dagPath - Path of the node which is being instanced.
         * otherPath - Invalid Path.
         * default actions - If dagPath is locked then
           the default action is to not allow the instance to be created.
           If dagPath is unlocked then dagPath can be instanced.

        kCreateChildInstance
         * dagPath - Path of the node whose child is being
           instanced.
         * otherPath - Path of the child node.
         * default actions - If dagPath is locked then
           the default action is to not allow the instance to be created.
           If dagPath is unlocked then dagPath can be instanced.

         * dagPath (MDagPath) - The path to attach the callback.
         * function - the callback function (see below for the description)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def setNodeLockQueryCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setNodeLockQueryCallback(node, function, clientData=None) -> id

        This methods registers a callback that is invoked in any locking
        condition on node properties, e.g. name, lock status, etc. When
        called, the API user can make a decision on how to handle the given
        locking situation. The programmer can either accept the default
        action, or they can deny the default action. The decision is returned
        through a decision variable which is passed to the callback function.

        The callback function takes the following parameters:
           * node - The node that triggered the callback.
           * aux - Any auxiliary data that may be needed, e.g.
             the attribute about to be added.
           * clientData - User defined data passed to the
             callback function.
           * eventType - Description of the event.
        And return True to accept the default behavior and False to
        reject it.

        The meanings of the node and aux parameters for each
        eventType, and default actions associated with those event types, are
        as follows:

        kRename
           * node - The node that the user is attempting to rename.
           * aux - MObject.kNullObj
           * default actions - If node is locked then the
             default action is to not allow the rename. Otherwise,
             if node is unlocked then node can be renamed.

        kDelete   * node - The node that the user is attempting to delete.
           * aux - MObject.kNullObj
           * default actions - If node is locked then the
             default action is to not allow the delete. If node is unlocked
             then the node can be deleted.

        kLockNode   * node - The node that the user is attempting to lock.
           * aux - MObject.kNullObj
           * default actions - If node is unlocked then the
             default action is to ALLOW the node to be locked. The callback
             is not invoked when the user tries to unlock an already unlocked
             node.

        kUnlockNode   * node - The node that the user is attempting to unlock.
           * aux - MObject.kNullObj
           * default actions - If node is locked then the
             default action is to ALLOW the unlock. The callback is not invoked
             when the user tries to unlock an already unlocked node.

        kAddAttr   * node - The node that is having an attribute added.
           * aux - MObject of the attribute to be added. Note:
             the attribute does not belong to the node yet. You can only
             access the attribute information using MFnAttribute.
           * default actions - If node is locked then the default
             action is to not allow to the addition of aux. If node
             is unlocked then aux can be added to the node.

        kRemoveAttr
           * node - The node that is having an attribute removed.
           * aux - The attribute to be removed. In certain
             situations the user is allowed to do a global delete,
             e.g. "deleteAttr -at AttrName [nodes]". In these cases the plug is not
             created until checks have been performed; so aux ==
             MObject.kNullObj
           * default actions - If node is locked then the default
             action is to not allow the attribute removal. If node is
             unlocked then aux can be removed.

        kRenameAttr
           * node - The node that is having an attribute renamed.
           * aux - The attribute.
           * default actions - If node is locked then the default
             action is to not allow the rename. If node is unlocked then
             aux can be renamed.

        kUnlockAttr
           * node - The node that is having an attribute unlocked.
           * aux - The attribute to be unlocked.
           * default actions - If node is locked then the default
             action is to not allow the unlock. If node is unlocked then
             aux attribute can be unlocked.

        kLockAttr
           * node - The node that is having an attribute locked.
           * aux - The attribute to be locked.
           * default actions - If node is locked then the default
             action is to not allow the locking of aux. If node is
             unlocked then aux can be locked.

         * node (MObject) - The node to register the callback for.
         * function - the callback function (see below for description)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def setPlugLockQueryCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPlugLockQueryCallback(plug, function, clientData=None) -> id

        This method registers a callback that is invoked in any locking
        condition on a plug, e.g. plug unlock, plug lock, connections, etc.
        When the callback is invoked, the API programmer can make a decision on
        how to handle the given locking situation. The programmer can either
        accept the default action, or they can deny the default action.
        The decision is made through the decision variable described above.

        The callback function takes the following parameters:
           * plug - The plug that triggered the callback.
           * otherPlug - The other plug involved in the callback.
             This is only valid during connect and disconnect events.
             clientData - User defined data passed to the
             callback function.
           * eventType - Description of the event.
        And return True to accept the default behavior and False to
        reject it.

        The meanings of the plug and otherPlug parameters for each
        eventType, and default actions associated with those event types, are
        as follows:

        kPlugLockAttr
           * plug - The plug that the user is attempting to lock.
           * otherPlug - None.
           * default actions - If plug is unlocked then the
             default action is to allow the plug to be locked.

        kPlugUnlockAttr
           * plug - The plug that the user is attempting to unlock.
           * otherPlug - None.
           * default actions - If plug is locked then the
             default action is to allow the plug to be unlocked.

        kPlugAttrValChange
           * plug - The plug that the user is attempting to change.
           * otherPlug - None.
           * default actions - If plug is locked then the
             default action is to not allow plug to change. If plug is
             unlocked then plug can change.

        kPlugRemoveAttr
           * plug - The plug that the user is attempting to remove.
           * otherPlug - None.
           * default actions - If plug is locked then the
             default action is to not allow removal. Otherwise, if plug is
             unlocked then plug can be removed.

        kPlugRenameAttr
           * plug - The plug that the user is attempting to rename.
           * otherPlug - None.
           * default actions - If plug is locked then the default
             action is to not allow the rename. Otherwise, if plug is
             unlocked then plug can be renamed.

        kPlugConnect
           * plug - The plug that is to be connected (incoming
             connection).
           * otherPlug - The source plug of the connection being made.
           * default actions - If plug is locked then the
             connection is DENIED. If plug is unlocked then otherPlug can
             be connected to plug.

        kPlugDisconnect
           * plug - The plug that it is having an incoming connection broken.
           * otherPlug - The source plug of the connection being made.
           * default actions - If plug is locked then the
             default action is to DENY the connection from being broken. If
             plug is unlocked then otherPlug can be disconnected from
             plug.

         * plug (MPlug) - the plug to attach the callback
         * function - the callback function (see below for description)
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MMatrix:
    def adjoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's adjoint."""
    def det3x3(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""
    def det4x4(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns this matrix's determinant."""
    def getElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix element for the specified row and column."""
    def homogenize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing the homogenized version of this matrix."""
    def inverse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's inverse."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two matrices, within a tolerance."""
    def isSingular(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this matrix is singular."""
    kIdentity: MMatrix = ...
    kTolerance: float = ...

    def setElement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the matrix element for the specified row and column."""
    def setToIdentity(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the identity."""
    def setToProduct(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the product of the two matrices passed in."""
    def transpose(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's transpose."""

class MMatrixArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MMeshIntersector:
    def create(self: Self, *args: Any, **kwargs: Any) -> Any:
        """create(mesh, matrix) -> self

        Creates the internal data required by the intersector. It is a
        compute-heavy operation and should only be called when necessary.

        mesh (MObject)   - the mesh to be used
        matrix (MMatrix) - transformation to use to bring points into the
        mesh's object space.faceIds (list) - the faces of the mesh to be passed to the intersector
        """
    def getClosestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getClosestPoint(referencePoint, maxDistance=sys.float_info.max) -> MPointOnMesh

        Finds the closest point within 'maxDistance' of the reference point
        (MPoint) which lies on the surface of the mesh. The reference point
        will first be transformed by the matrix passed in the create() call,
        so if, for example, you want to specify reference points in world
        space then the matrix passed to create() should provide the mapping
        from world space to the mesh's object space.

        Returns an MPointOnMesh object if a closest point is found, or None
        if no closest point is found (e.g. referencePoint is not within
        maxDistance of the mesh).

        Raises ValueError if create() has not yet been called for this
        intersector.
        """
    @property
    def isCreated(*args: Any, **kwargs: Any) -> Any:
        """True if the intersector has been created, False otherwise."""
    @isCreated.setter
    def isCreated(*args: Any, **kwargs: Any) -> Any:
        """True if the intersector has been created, False otherwise."""

class MMeshIsectAccelParams:
    pass

class MMeshSmoothOptions:
    @property
    def boundaryRule(*args: Any, **kwargs: Any) -> Any:
        """Determines how boundary edges and vertices are creased."""
    @boundaryRule.setter
    def boundaryRule(*args: Any, **kwargs: Any) -> Any:
        """Determines how boundary edges and vertices are creased."""
    @property
    def divisions(*args: Any, **kwargs: Any) -> Any:
        """Number of subdivisions used in smoothing."""
    @divisions.setter
    def divisions(*args: Any, **kwargs: Any) -> Any:
        """Number of subdivisions used in smoothing."""
    kCatmullClark: int = ...
    kCreaseAll: int = ...
    kCreaseEdge: int = ...
    kInvalid: int = ...
    kInvalidSubdivision: int = ...
    kLast: int = ...
    kLastSubdivision: int = ...
    kLegacy: int = ...
    kOpenSubdivCatmullClarkAdaptive: int = ...
    kOpenSubdivCatmullClarkUniform: int = ...

    @property
    def keepBorderEdge(*args: Any, **kwargs: Any) -> Any:
        """If True, border edges will not be smoothed."""
    @keepBorderEdge.setter
    def keepBorderEdge(*args: Any, **kwargs: Any) -> Any:
        """If True, border edges will not be smoothed."""
    @property
    def keepHardEdge(*args: Any, **kwargs: Any) -> Any:
        """If True, hard edges will not be smoothed."""
    @keepHardEdge.setter
    def keepHardEdge(*args: Any, **kwargs: Any) -> Any:
        """If True, hard edges will not be smoothed."""
    @property
    def propEdgeHardness(*args: Any, **kwargs: Any) -> Any:
        """If True, the hardness of edges in the base cage will be propagated to the edges of the smoothed mesh which derive from them."""
    @propEdgeHardness.setter
    def propEdgeHardness(*args: Any, **kwargs: Any) -> Any:
        """If True, the hardness of edges in the base cage will be propagated to the edges of the smoothed mesh which derive from them."""
    @property
    def smoothUVs(*args: Any, **kwargs: Any) -> Any:
        """If True, UVs will be smoothed as well as geometry. If False, only geometry will be smoothed."""
    @smoothUVs.setter
    def smoothUVs(*args: Any, **kwargs: Any) -> Any:
        """If True, UVs will be smoothed as well as geometry. If False, only geometry will be smoothed."""
    @property
    def smoothness(*args: Any, **kwargs: Any) -> Any:
        """The degree of smoothness desired. Ranges from 0.0 (hard) to 1.0 (fully smoothed)."""
    @smoothness.setter
    def smoothness(*args: Any, **kwargs: Any) -> Any:
        """The degree of smoothness desired. Ranges from 0.0 (hard) to 1.0 (fully smoothed)."""
    @property
    def subdivisionType(*args: Any, **kwargs: Any) -> Any:
        """Determines subdivision algorithm used for mesh smoothing."""
    @subdivisionType.setter
    def subdivisionType(*args: Any, **kwargs: Any) -> Any:
        """Determines subdivision algorithm used for mesh smoothing."""

class MModelMessage(MMessage):
    def addAfterDuplicateCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAfterDuplicateCallback(function, clientData=None) -> id

        This method registers a callback that is called after a duplicate
        command is made. The callback will be called after everything is
        duplicated.

         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addBeforeDuplicateCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addBeforeDuplicateCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a duplicate
        command is made. The callback will be called before anything is
        duplicated.

         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCallback(message, function, clientData=None) -> id

        Adds a new callback for the specified model message.


         * message (Message constant, see class doc for a list) - the model
           message that will trigger the callback
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeAddedToModelCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeAddedToModelCallback(dagNode, function, clientData=None) -> id

        This method registers a callback that is called when a dag node is about
        to be added to the Maya model.

         * dagNode (MObject) - Node that should acquire the callback
         * function - callable which will be passed a MObject indicating
           the node being added to the model and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeRemovedFromModelCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeRemovedFromModelCallback(dagNode, function, clientData=None) -> id

        This method registers a callback that is called when the
        specified dag node is being removed from the Maya model.

         * dagNode (MObject) - Node that should acquire the callback
         * function - callable which will be passed a MObject indicating
           the node being removed to the model and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MNamespace:
    def addNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNamespace(MString name, MString parent=None)

        Create the namespace 'name'. If the `parent' namespace is given
        the new namespace will be a child of `parent', otherwise the new
        namespace will be a child of the current namespace.
        The new namespace is added, but not made current. To make the
        new namespace be current use MNamespace.setCurrentNamespace().
        Note that adding a namespace changes the scene, so any code that calls
        this method needs to handle undo.

             name    The new namespace to create. A qualified or unqualified
                     name may be used. If a qualified name is used and one or
                     more of the higher level namespaces do not already exist,
                     they will be created automatically. For example, if the new
                     name is 'a:b:c' and 'a' does not yet exist, then it will be
                     created automatically and 'b' automatically created beneath
                     it and finally 'c' will be created beneath 'b'.
                     If the supplied name contains invalid characters it will first
                     be modified as per the validateName() method.
             parent  The fully qualified name of the namespace under which
                     the new one is to be created. If not provided then the
                     current namespace will be used. If the name of the new
                     namespace is absolute (i.e. begins with a colon, ':a:b:c')
                     then the 'parent' parameter will be ignored and the new namespace
                     will be created under the root namespace.
        """
    def currentNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """currentNamespace() -> MString

        Get the name of the current namespace. This name is returned
        as an absolute namepath (i.e. fully qualfied from the root
        namespace downwards, ':a:b:c').
        """
    def getNamespaceFromName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNamespaceFromName(MString fullName) -> MString

        Get namespace from a full name.
        For example, given a full name: 'a:b:c:d:ball' this method
        would return: 'a:b:c:d'.
        """
    def getNamespaceObjects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNamespaceObjects(MString parentNamespace, bool recurse=False) -> MObjectArray

        Return an array of MObjects representing the object contained within
        the specified namespace. To query the current namespace, call this
        method in this way:
        """
    def getNamespaces(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getNamespaces(MString parentNamespace=None, bool recurse=False) -> [MString]

        Return a list of all namespaces in the current namespace.
        Notes:
            1)  Names returned are always absolute (e.g. :a:b:sphere).
            2)  The list returned is just the child namespaces (and
                descendents if `recurse' is true). It thus never contains
                the root namespace in the list returned.

                   parentNamespace  the namespace to query.
                   recurse          optional parameter to control whether all
                                    namespaces or just top-level namespaces
                                    are returned. A value of false (the
                                    default if unspecified) causes only the
                                    top-level namespaces to be returned. If
                                    true, all namespaces will be listed.
        """
    def makeNamepathAbsolute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """makeNamepathAbsolute(MString fullName) -> MString

        Make a namepath which is relative to the root into an absolute
        namepath. For example, given the namepath 'a:sphere' this method
        returns ':a:sphere'. It also culls out duplicate and trailing
        separators, e.g. 'a:b::c:' will return ':a:b:c'.
        """
    def moveNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """moveNamespace(MString src, MString dst, bool force=False)

        Move the contents of the namespace 'src' into the namespace 'dst'.
        Note that moving namespace contents changes the scene, so any code
        that calls this method needs to handle undo.

                  src       source namespace from which objects will be moved.
                  dst       destination namespace to which objects will be moved.
                  force     optional parameter which if true forces the move
                            even if name clashes occur, in which case nodes are
                            renamed to ensure uniqueness. If false, the move
                            will not happen if there are clashes. The default
                            value is false.
        """
    def namespaceExists(self: Self, *args: Any, **kwargs: Any) -> Any:
        """namespaceExists(MString name) -> bool

        Check if a given namespace exists.
        """
    def parentNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """parentNamespace() -> MString

        Get the name of the current namespace's parent. This name is returned
        as an absolute namepath (i.e. fully qualfied from the root namespace
        downwards, ':a:b'). If the root namespace is
        current, this method returns an error.
        """
    def relativeNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """relativeNames() -> bool

        Query Maya's current 'relative name lookup' state. Relative name
        lookup causes lookups to be relative to the current namespace.
        By default, relative name lookup in Maya is off, which causes
        name lookups to be relative to the root namespace. For example,
        if you have the object :a:b:sphere, and the current namespace is
        ':a:b', in relative name lookup mode you can issue a command like

            setAttr sphere.translateX 10;

        If relative name lookup is off, you need to specify the full
        namepath, e.g.

            setAttr a:b:sphere.translateX 10;
        """
    def removeNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeNamespace(MString name, bool removeContents=False)

        Remove the specified namespace.
        Note that removing a namespace changes the scene, so any code
        that calls this method needs to handle undo.
        """
    def renameNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renameNamespace(MString oldName, MString newName, MString parent=None)

        Rename the specified namespace to a new name with optional parent name.
        Note that removing a namespace changes the scene, so any code
        that calls this method needs to handle undo.
        """
    def rootNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """rootNamespace() -> MString

        Get the name of the root namespace. This name is an absolute
        namepath (i.e. prefixed by a ':').
        """
    def setCurrentNamespace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCurrentNamespace(MString name) -> MString

        Set the specified namespace to be the current namespace. The 'name'
        parameter you specify is relative to whatever namespace is current,
        but any namespace can be specified by passing an absolute name (e.g. :a:b:c).
        Note that making a namespace current changes the scene, so any code
        that calls this method needs to handle undo.

        To make the root namespace become current, use:
            MNamespace.setCurrentNamespace(MNamespace.rootNamespace())
        """
    def setRelativeNames(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRelativeNames(bool newState)

        Set relative name lookup mode.

        Note that turning on or off relativeNames mode can change the scene,
        so any code that calls this method needs to handle undo.
        See MNamespace.relativeNames() for details on relative name lookup.

        Note: relative name lookup mode is intended for bracketing user
        code which needs to be namespace-independent. Leaving relative
        name lookup enabled outside of your specific code could cause
        functionality such as 3rd-party plugins that assume absolute
        name lookup to fail.

           newState         true to turn on relative name lookup, false to
                            turn it off. Maya's default setting is false.
        """
    def stripNamespaceFromName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """stripNamespaceFromName(MString fullName) -> MString

        Strips the namespace from a full name.
        For example, given a full name: 'a:b:c:d:ball' this method
        would return: 'ball'.
        """
    def validateName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """validateName(MString name) -> MString

        Convert the specified name to a validated name which
        contains no illegal characters.
        The leading illegal characters will be removed and
        other illegal characters will be converted to '_'.

        For example, name '@name@space@' will be converted to 'name_space_'.

        If the entire name consists solely of illegal characters,
        e.g. '123' which contains only leading digits, then the
        returned string will be empty.
        """

class MNodeCacheDisablingInfo:
    def getCacheDisabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCacheDisabled() -> bool

        Return True if the cache should be disabled because of this node.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset()

        Resets the disabling info to an enabled state.
        """
    def setCacheDisabled(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setCacheDisabled(bool)

        Set if the cache should be disabled because of this node.
        """
    def setMitigation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMitigation(mitigation)

        Sets the mitigation to fix the reason for disabling Cached Playback.
        """
    def setReason(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setReason(reason)

        Sets the reason for disabling Cached Playback.
        """

class MNodeCacheSetupInfo:
    def getPreference(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPreference(PreferenceFlag) -> bool

        Get a preference flag for this node.
        """
    def getRequirement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRequirement(RequirementFlag) -> bool

        Get a requirement flag for this node.
        """
    kLastPreference: int = ...
    kLastRequirement: int = ...
    kSimulationSupport: int = ...
    kWantToCacheByDefault: int = ...

    def setPreference(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPreference(PreferenceFlag, bool)

        Set a preference flag for this node.
        """
    def setRequirement(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setRequirement(RequirementFlag, bool)

        Set a requirement flag for this node.
        """

class MNodeClass:
    def addExtensionAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds an extension attribute to the node class. An extension attribute is a class-level attribute which has been added dynamically to a node class. Because it is added at the class level, all nodes of that class will have the given attribute, and will only store the attribute's value if it differs from the default. Returns the type of the object at the end of the path."""
    def attribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """If passed an int: Returns the node class's i'th attribute. Raises IndexError if index is out of bounds.  If passed a string, Returns the node class's attribute having the given name. Returns MObject.kNullObj if the class does not have an attribute with that name."""
    @property
    def attributeCount(*args: Any, **kwargs: Any) -> Any:
        """Number of attributes the node class has. Includes extension attributes, since those are applied to the entire node class, but not dynamic attributes, since those are only applied to individual nodes."""
    @attributeCount.setter
    def attributeCount(*args: Any, **kwargs: Any) -> Any:
        """Number of attributes the node class has. Includes extension attributes, since those are applied to the entire node class, but not dynamic attributes, since those are only applied to individual nodes."""
    @property
    def classification(*args: Any, **kwargs: Any) -> Any:
        """This is a string that is used in dependency nodes that are also shaders to provide more detailed type information to the rendering system."""
    @classification.setter
    def classification(*args: Any, **kwargs: Any) -> Any:
        """This is a string that is used in dependency nodes that are also shaders to provide more detailed type information to the rendering system."""
    def getAttributes(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an MObjectArray array containing all of the node class's attributes."""
    def hasAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node class has an attribute of the given name, False otherwise."""
    @property
    def pluginName(*args: Any, **kwargs: Any) -> Any:
        """File path of the plug-in in which the node class is defined. The empty string is returned for Maya's built-in node types."""
    @pluginName.setter
    def pluginName(*args: Any, **kwargs: Any) -> Any:
        """File path of the plug-in in which the node class is defined. The empty string is returned for Maya's built-in node types."""
    def removeExtensionAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes an extension attribute from the node class. Raises ValueError if attr is not an extension attribute of this node class."""
    def removeExtensionAttributeIfUnset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes an extension attribute from the node class, but only if there are no nodes in the graph with non-default values for this attribute. Returns True if the attribute was removed, False otherwise. Raises ValueError if attr is not an extension attribute of this node class."""
    @property
    def typeId(*args: Any, **kwargs: Any) -> Any:
        """Type ID for the node class."""
    @typeId.setter
    def typeId(*args: Any, **kwargs: Any) -> Any:
        """Type ID for the node class."""
    @property
    def typeName(*args: Any, **kwargs: Any) -> Any:
        """Name of the node class. This is the name that is given to the createNode command to create nodes of this type."""
    @typeName.setter
    def typeName(*args: Any, **kwargs: Any) -> Any:
        """Name of the node class. This is the name that is given to the createNode command to create nodes of this type."""

class MNodeMessage(MMessage):
    def addAttributeAddedOrRemovedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAttributeAddedOrRemovedCallback(node, function, clientData=None) -> id

        Registers callbacks for attribute add/removed messages.
        This is a more specific version of addAttributeChanged as only attribute
        added and attribute removed messages will trigger the callback.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed an AttributeMessage constant (see
           class doc for a list) containing the kind of attribute change triggering
           the callback, a MObject indicating the node's plug where the connection
           changed and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addAttributeChangedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAttributeChangedCallback(node, function, clientData=None) -> id

        This method registers a callback for attribute changed messages.
        See the AttributeChanged enum for a list of all possible messages
        that will trigger the callback.

        Note: Attribute Changed messages will not be generated
        while Maya is either in playback or scrubbing modes. If you need to
        do something during playback or scrubbing you will have to register
        a callback for the timeChanged message which is the only
        message that is sent during those modes.

        The callback function will be passed the type of attribute message
        that has occurred, the plug(s) for the attributes, and any client
        data that the user wishes to pass in.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed an AttributeMessage constant (see
           class doc for a list) containing the kind of attribute change triggering
           the callback, a MObject indicating the node's plug where the connection
           changed, a MObject indicating the plug opposite the node's plug where the
           connection changed and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addKeyableChangeOverride(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addKeyableChangeOverride(plug, function, clientData=None) -> id

        This method registers a callback that is invoked by any class that
        changes the keyable state of an attribute.  When the callback is
        invoked, the API programmer can make a decision on how to handle
        the given keyable change event.  The programmer can either accept
        the keyable state change by returning True
        or reject it by returning False.

        Note: you can only attach one callback keyable change override
        callback per attribute.  It is an error to attach more than one
        callback to the same attribute.

         * plug (MPlug) - The plug to which to attach the callback.
         * function - callable which will be passed a MPlug indicating the plug that
           has triggered the callback, the clientData object, and a KeyableChangeMsg
           constant (see class doc for a list) containing the kind of Keyable change
           the callback, a MObject indicating the node's plug where the connection.
           User can return True to accept the keyable state change or False to reject it.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNameChangedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNameChangedCallback(node, function, clientData=None) -> id

        Registers a callback for name changed messages.

         * node (MObject) - the node. If this is a NULL MObject then the callback
           applies to all node name changes.
         * function - callable which will be passed a MObject indicating the node whose
           name's changed, a string containing the previous name of the node and the
           clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeAboutToDeleteCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeAboutToDeleteCallback(node, function, clientData=None) -> id

        Registers a callback which will get called when a node is about to
        be deleted.

        The callback will be passed the MDGModifer that will be used to
        delete the node. This modifier can be used to do any DG modifications,
        such as disconnections, before the node is deleted.  These operations are
        also stored and performed when the deletion operation is undone or redone.

        The callback registered with this method will only get called when the
        deletion operation is first performed. Undos and redos will be handled solely
        through the MDGModifier which was passed to the callback on the original
        deletion. If you also wish to receive notification of deletion events
        when they are redone, you should register an additional callback using
        addNodePreRemovalCallback().

        When a node is deleted Maya automatically breaks all connections to that
        node. This process takes place after the callback has been called. This
        means that if you use the passed-in MDGModifier to break any
        connections to the node you must be sure to call the modifier's doIt() method
        before returning from the callback. Otherwise Maya will see that the connections
        still exist and try to delete them again, which can lead to errors.

        Note that it uses the passed-in MDGModifier to perform all the disconnections and
        connections. This ensures that if the deletion is undone or redone then all of
        the connections will be restored correctly.

        After it is done breaking connections, the callback calls the
        modifier's doIt() method to commit those disconnections. As noted
        above, this is necessary to ensure that Maya doesn't see the
        connections and try to break them again later on.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node that
           will be deleted, a MDGModifier indicating the DG modifier used to delete the
           node and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeDestroyedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeDestroyedCallback(node, function, clientData=None) -> id

        Registers a callback which will get called when a node's destructor is
        called.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """
    def addNodeDirtyCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeDirtyCallback(node, function, clientData=None) -> id

        Registers a callback for node dirty messages.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that has  become dirty and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodeDirtyPlugCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodeDirtyPlugCallback(node, function, clientData=None) -> id

        Registers a callback for node dirty messages.  This callback provides
        the plug on the node that was dirtied.  Only provides dirty information
        on input plugs.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that has  become dirty, a MPlug indicating the plug on the node that has
           become dirty and the clientData object * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addNodePreRemovalCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addNodePreRemovalCallback(node, function, clientData=None) -> id

        Registers a callback which will get called before a node is deleted.
        This callback is called before connections on the node are removed.
        Unlike the aboutToDelete callback, this callback will be invoked whenever
        the node is deleted, even during a redo.

        Pre-removal and aboutToDelete callbacks serve different purposes.  If DG
        changes need to be made when a node is deleted, the aboutToDelete callback
        should be used to add undoable operations to an MDGModifier to perform
        these changes.  When the desired actions cannot be accomplished using the
        MDGModifier passed to the aboutToDelete callback, this callback can be
        used to receive notification of the deletion event, even during redo.

        Note that this callback method should not perform any DG operations.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that is being deleted and the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """
    def addUuidChangedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUuidChangedCallback(node, function, clientData=None) -> id

        Registers a callback for UUID changed messages.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that is being modified, a MUuid containing the previous UUID of the node
           and the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """
    kAttributeAdded: int = ...
    kAttributeArrayAdded: int = ...
    kAttributeArrayRemoved: int = ...
    kAttributeEval: int = ...
    kAttributeKeyable: int = ...
    kAttributeLocked: int = ...
    kAttributeRemoved: int = ...
    kAttributeRenamed: int = ...
    kAttributeSet: int = ...
    kAttributeUnkeyable: int = ...
    kAttributeUnlocked: int = ...
    kIncomingDirection: int = ...
    kKeyChangeLast: int = ...
    kLast: int = ...
    kOtherPlugSet: int = ...

class MObject:
    def apiType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the function set type for the object."""
    @property
    def apiTypeStr(*args: Any, **kwargs: Any) -> Any:
        """(readonly) String containing the object's type name."""
    @apiTypeStr.setter
    def apiTypeStr(*args: Any, **kwargs: Any) -> Any:
        """(readonly) String containing the object's type name."""
    def hasFn(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Tests whether object is compatible with the specified function set."""
    def isNull(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Tests whether there is an internal Maya object."""
    kNullObj: MObject = ...

class MObjectArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MObjectHandle:
    def assign(self: Self, *args: Any, **kwargs: Any) -> Any:
        """assign(source) -> self

        Assigns this MObjectHandle to an instance of another MObjectHandle, or to a MObject instance.

        * source (MObject/MObjectHandle) - other instance to assign from.
        """
    def hashCode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hashCode() -> int

        Returns a hash code for the internal Maya object referenced by the MObject within this MObjectHandle. If the MObject is null or no longer alive then 0 will be returned, otherwise the hash code is guaranteed to be non-zero
        """
    def isAlive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isAlive() -> bool

        Returns the live state of the associated MObject. An object can still be 'alive' but not 'valid' (eg. a deleted object that resides in the undo queue).
        """
    def isValid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isValid() -> bool

        Returns the validity of the associated MObject.
        """
    def object(self: Self, *args: Any, **kwargs: Any) -> Any:
        """object() -> MObject

        Returns the MObject associated with this handle. The returned MObject will be MObject.kNullObj if the object is invalid.
        """

class MObjectSetMessage(MMessage):
    def addSetMembersModifiedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addSetMembersModifiedCallback(node, function, clientData=None) -> id

        Registers callbacks for set modified messages.

         * node (MObject) - the set that has triggered a setModified event
         * function (MMessage::MNodeFunction) - the callback function
         * function - callable which will be passed a MObject indicating the
           set that has triggered a setModified event and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MPlane:
    def distance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """distance() -> float

        Returns the distance of the plane along the normal.
        """
    def distanceToPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """distanceToPoint(point, signed=False) -> float

        Returns the distance from the plane to the specified point.

        * point (MVector) - The point from which to calculate the distance
        * signed (bool) - Whether to return a signed or unsigned distance
        """
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """normal() -> MVector

        Returns the normal of the plane.
        """
    def setPlane(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPlane(a, b, c, d) -> self
        setPlane(n, d) -> self

        Set the equation of the plane.

        From values : ax + by + cz + d = 0
        * a (float) - The plane equation's x coefficent
        * b (float) - The plane equation's y coefficent
        * c (float) - The plane equation's z coefficent
        * d (float) - The plane equation's constant distance term

        From a normal and offset
        * n (MVector) - The plane's normal
        * d (float) - The offset of the plane along the normal
        """

class MPlug:
    def array(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the array of plugs of which this plug is an element."""
    def asBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a boolean."""
    def asChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a single-byte integer."""
    def asDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a double-precision float."""
    def asFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a single-precision float."""
    def asInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a regular integer."""
    def asMAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as an MAngle."""
    def asMDataHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieve the current value of the attribute this plug references."""
    def asMDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as an MDistance."""
    def asMObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as as an MObject containing a direct reference to the plug's data."""
    def asMTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as an MTime."""
    def asShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a short integer."""
    def asString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a string."""
    def attribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute currently referenced by this plug."""
    def child(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the specified child attribute of this plug."""
    def connectedTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an array of plugs which are connected to this one."""
    def connectionByPhysicalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the index'th connected element of this plug."""
    def constructHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Constructs a data handle for the plug."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Copies one plug to another."""
    def destinations(self: Self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a source, return the destination plugs connected to it.
        If this plug is not a source, a null plug is returned.
        This method will produce the networked version of the connected plug.
        """
    def destinationsWithConversions(self: Self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a source, return the destination plugs connected to it.
        This method is very similar to the destinations() method.  The only difference is that the destinations() method skips over any unit conversion node connected to this source, and returns the destination of the unit conversion node.
        destinationsWithConversionNode() does not skip over unit conversion nodes, and returns the destination plug on a unit conversion node, if present.
        Note that the behavior of connectedTo() is identical to destinationsWithConversions(), that is, do not skip over unit conversion nodes.
        """
    def destructHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Destroys a data handle previously constructed using constructHandle()."""
    def elementByLogicalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the element of this plug array having the specified logical index."""
    def elementByPhysicalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the element of this plug array having the specified physical index."""
    def evaluateNumElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Like numElements() but evaluates all connected elements first to ensure that they are included in the count."""
    def getExistingArrayAttributeIndices(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns an array of all the plug's logical indices which are currently in use."""
    def getSetAttrCmds(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list of strings containing the setAttr commands (in MEL syntax) for this plug and all of its descendents."""
    @property
    def info(*args: Any, **kwargs: Any) -> Any:
        """Description of the plug for debugging purposes, in the form node:attr1.attr2[].attr3..."""
    @info.setter
    def info(*args: Any, **kwargs: Any) -> Any:
        """Description of the plug for debugging purposes, in the form node:attr1.attr2[].attr3..."""
    @property
    def isArray(*args: Any, **kwargs: Any) -> Any:
        """True if plug is an array of plugs."""
    @isArray.setter
    def isArray(*args: Any, **kwargs: Any) -> Any:
        """True if plug is an array of plugs."""
    @property
    def isCaching(*args: Any, **kwargs: Any) -> Any:
        """True if plug's value is being cached."""
    @isCaching.setter
    def isCaching(*args: Any, **kwargs: Any) -> Any:
        """True if plug's value is being cached."""
    @property
    def isChannelBox(*args: Any, **kwargs: Any) -> Any:
        """True if plug will appear in Maya's Channel Box."""
    @isChannelBox.setter
    def isChannelBox(*args: Any, **kwargs: Any) -> Any:
        """True if plug will appear in Maya's Channel Box."""
    @property
    def isChild(*args: Any, **kwargs: Any) -> Any:
        """True if plug is a child of a compound parent."""
    @isChild.setter
    def isChild(*args: Any, **kwargs: Any) -> Any:
        """True if plug is a child of a compound parent."""
    @property
    def isCompound(*args: Any, **kwargs: Any) -> Any:
        """True if plug is compound parent with children."""
    @isCompound.setter
    def isCompound(*args: Any, **kwargs: Any) -> Any:
        """True if plug is compound parent with children."""
    @property
    def isConnected(*args: Any, **kwargs: Any) -> Any:
        """True if plug has any connections."""
    @isConnected.setter
    def isConnected(*args: Any, **kwargs: Any) -> Any:
        """True if plug has any connections."""
    def isDefaultValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a value indicating if the plug's value is equivalent to the plug's default value."""
    @property
    def isDestination(*args: Any, **kwargs: Any) -> Any:
        """True if plug is the destination of a connection."""
    @isDestination.setter
    def isDestination(*args: Any, **kwargs: Any) -> Any:
        """True if plug is the destination of a connection."""
    @property
    def isDynamic(*args: Any, **kwargs: Any) -> Any:
        """True if plug is for a dynamic attribute."""
    @isDynamic.setter
    def isDynamic(*args: Any, **kwargs: Any) -> Any:
        """True if plug is for a dynamic attribute."""
    @property
    def isElement(*args: Any, **kwargs: Any) -> Any:
        """True if plug is an element of an array of plugs."""
    @isElement.setter
    def isElement(*args: Any, **kwargs: Any) -> Any:
        """True if plug is an element of an array of plugs."""
    def isFreeToChange(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a value indicating if the plug's value can be changed, after taking into account the effects of locking and connections."""
    @property
    def isFromReferencedFile(*args: Any, **kwargs: Any) -> Any:
        """True if plug is part of a connection from a referenced file."""
    @isFromReferencedFile.setter
    def isFromReferencedFile(*args: Any, **kwargs: Any) -> Any:
        """True if plug is part of a connection from a referenced file."""
    @property
    def isIgnoredWhenRendering(*args: Any, **kwargs: Any) -> Any:
        """True if connetions to plug are ignored during rendering."""
    @isIgnoredWhenRendering.setter
    def isIgnoredWhenRendering(*args: Any, **kwargs: Any) -> Any:
        """True if connetions to plug are ignored during rendering."""
    @property
    def isKeyable(*args: Any, **kwargs: Any) -> Any:
        """True if keys can be set on plug from Maya's UI."""
    @isKeyable.setter
    def isKeyable(*args: Any, **kwargs: Any) -> Any:
        """True if keys can be set on plug from Maya's UI."""
    @property
    def isLocked(*args: Any, **kwargs: Any) -> Any:
        """True if plug is locked against changes."""
    @isLocked.setter
    def isLocked(*args: Any, **kwargs: Any) -> Any:
        """True if plug is locked against changes."""
    @property
    def isNetworked(*args: Any, **kwargs: Any) -> Any:
        """True if plug is networked."""
    @isNetworked.setter
    def isNetworked(*args: Any, **kwargs: Any) -> Any:
        """True if plug is networked."""
    @property
    def isNull(*args: Any, **kwargs: Any) -> Any:
        """True if plug does not reference an attribute."""
    @isNull.setter
    def isNull(*args: Any, **kwargs: Any) -> Any:
        """True if plug does not reference an attribute."""
    @property
    def isProcedural(*args: Any, **kwargs: Any) -> Any:
        """True if plug is procedural."""
    @isProcedural.setter
    def isProcedural(*args: Any, **kwargs: Any) -> Any:
        """True if plug is procedural."""
    @property
    def isProxy(*args: Any, **kwargs: Any) -> Any:
        """True if plug is a proxy plug."""
    @isProxy.setter
    def isProxy(*args: Any, **kwargs: Any) -> Any:
        """True if plug is a proxy plug."""
    @property
    def isSource(*args: Any, **kwargs: Any) -> Any:
        """True if plug is the source of a connection."""
    @isSource.setter
    def isSource(*args: Any, **kwargs: Any) -> Any:
        """True if plug is the source of a connection."""
    kAll: int = ...
    kChanged: int = ...
    kChildrenNotFreeToChange: int = ...
    kFreeToChange: int = ...
    kLastAttrSelector: int = ...
    kNonDefault: int = ...
    kNotFreeToChange: int = ...

    def logicalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns this plug's logical index within its parent array."""
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the name of the plug."""
    def node(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node that this plug belongs to."""
    def numChildren(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of children this plug has."""
    def numConnectedChildren(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of this plug's children which have connections."""
    def numConnectedElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of this plug's elements which have connections."""
    def numElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of the plug's logical indices which are currently in use. Connected elements which have not yet been evaluated may not yet fully exist and may be excluded from the count."""
    def parent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the parent of this plug."""
    def partialName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the name of the plug, formatted according to various criteria."""
    def proxied(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the proxied plug for this plug."""
    def selectAncestorLogicalIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Changes the logical index of the specified attribute in the plug's path."""
    def setAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Switches the plug to reference the given attribute of the same node as the previously referenced attribute."""
    def setBool(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a boolean."""
    def setChar(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a single-byte integer."""
    def setDouble(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a double-precision float."""
    def setFloat(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a single-precision float."""
    def setInt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a regular integer."""
    def setMAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MAngle."""
    def setMDataHandle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a data handle."""
    def setMDistance(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MDistance."""
    def setMObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MObject."""
    def setMPxData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value using custom plug-in data."""
    def setMTime(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MTime."""
    def setNumElements(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Pre-allocates space for count elements in an array of plugs."""
    def setShort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a short integer."""
    def setString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a string."""
    def source(self: Self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a destination, return the source plug connected to it.
        If this plug is not a destination, a null plug is returned.
        This method will produce the networked version of the connectedplug.
        """
    def sourceWithConversion(self: Self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a destination, return the source plug connected to it.
        This method is very similar to the source() method.  The only difference is that the source() method skips over any unit conversionnode connected to this destination, and returns the source of the unit conversion node.
        sourceWithConversion() does not skip over unitconversion nodes, and returns the source plug on a unit conversionnode, if present.
        Note that the behavior of connectedTo() is identical to sourceWithConversion(), that is, do not skip over unit conversion nodes.
        """

class MPlugArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MPoint:
    def cartesianize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to cartesian form."""
    def distanceTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return distance between this point and another."""
    def homogenize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to homogenous form."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two points, within a tolerance."""
    kOrigin: MPoint = ...
    kTolerance: float = ...

    def rationalize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to rational form."""
    @property
    def w(*args: Any, **kwargs: Any) -> Any:
        """W coordinate"""
    @w.setter
    def w(*args: Any, **kwargs: Any) -> Any:
        """W coordinate"""
    @property
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @x.setter
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @property
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @y.setter
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @property
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""
    @z.setter
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""

class MPointArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MPointOnMesh:
    @property
    def barycentricCoords(*args: Any, **kwargs: Any) -> Any:
        """(float, float) Tuple containing the barycentric coordinates of the
        point. If the triangle has vertices (A, B, C) then barycentric
        coordinates of (u, v) mean that the 3D position of the point is
        u*A + v*B + (1 - u - v)*C. The barycentric coordinates are
        particularly useful when interpolating attributes from one mesh to
        another.
        """
    @barycentricCoords.setter
    def barycentricCoords(*args: Any, **kwargs: Any) -> Any:
        """(float, float) Tuple containing the barycentric coordinates of the
        point. If the triangle has vertices (A, B, C) then barycentric
        coordinates of (u, v) mean that the 3D position of the point is
        u*A + v*B + (1 - u - v)*C. The barycentric coordinates are
        particularly useful when interpolating attributes from one mesh to
        another.
        """
    @property
    def face(*args: Any, **kwargs: Any) -> Any:
        """(int) Mesh-global index of the face containing the point."""
    @face.setter
    def face(*args: Any, **kwargs: Any) -> Any:
        """(int) Mesh-global index of the face containing the point."""
    @property
    def normal(*args: Any, **kwargs: Any) -> Any:
        """(MFloatVector) Surface normal vector at the point."""
    @normal.setter
    def normal(*args: Any, **kwargs: Any) -> Any:
        """(MFloatVector) Surface normal vector at the point."""
    @property
    def point(*args: Any, **kwargs: Any) -> Any:
        """(MFloatPoint) 3D position of the point."""
    @point.setter
    def point(*args: Any, **kwargs: Any) -> Any:
        """(MFloatPoint) 3D position of the point."""
    @property
    def triangle(*args: Any, **kwargs: Any) -> Any:
        """(int) Face-local index of the triangle containing the point."""
    @triangle.setter
    def triangle(*args: Any, **kwargs: Any) -> Any:
        """(int) Face-local index of the triangle containing the point."""

class MPolyMessage(MMessage):
    def addPolyComponentIdChangedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPolyComponentIdChangedCallback(node, (wantVertIds, wantEdgeIds, wantFaceIds), function, clientData=None) -> id

        This method registers a callback that should be called whenever a poly
        component id is modified.
        Currently, there are some cases where the component ids for a polygonal
        mesh can be modified without generating a callback or without generating a
        correct mapping.  These cases are outlined below.

        - Polygonal mesh has construction history enabled, and there is more than
                 one topology changing operation in the history.  In this case, the
                 callback is only called when the component ID mapping changes for the
                 most recent operation, and performs the mapping with respect to the
                 input and output meshes for this operation node.
        - Polygonal mesh has construction history enabled, and the most recent
                 topology changing operation is no longer the most recent operation.
                 In this case, no id remapping callbacks will be invoked when the
                 attributes on the operation node are changed in the history.
        - When undo is used to revert a topology changing operation, the callback
                 will not be invoked.  The MEventMessage class can be used to get
                 notification when undo is performed.


        Component id mapping should always work correctly when construction history
        is off.  It should also work correctly when construction history is on and
        only the most recent operation is permitted to be adjusted (eg. changing
        the distance parameter for a merge vertex node, when merge vertices was the
        most recent operation.)  In either case, undo will not produce a poly
        message callback.

         * node (MObject) - the node the callback function should listen to
         *(wantVertIds, wantEdgeIds, wantFaceIds) - tuple of 3 booleans specifying
           what arrays should be provided to the callback function when it is
           invoked: (vertex indices, edge indices, face indices).
         * function - callable which will be passed a tuple and the clientData object.
           The tuple will contain three MUintArrays which are, respectively, the vertex,
           edge and face ids of the modified components. Only the arrays which were requested
           when the callback was registered will contain data, the others will be empty.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addPolyTopologyChangedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addPolyTopologyChangedCallback(node, function, clientData=None) -> id

        This method registers a callback that will be called when a node impacting
        the topology of a meshShape is modified. Because the callback is invoked
        before the mesh has evaluated, the new topology data cannot be
        queried at the time the callback is received. If you want to receive a
        callback at a time when the new mesh data can be queried, use the
        following technique:

        - Use this method to register a topology-changed callback.
        - In the topology-changed callback, add an MNodeMessage.addAttributeChangedCallback on the mesh shape.
        - In the attribute-changed callback, check the inputs for an MNodeMessage.kAttributeEval message received by the "outMesh" plug of the mesh.
        - Once you have received the eval message on that plug, the attribute-changed callback can be removed and the mesh topology can be queried.

         * node (MObject) - the node the callback function should listen to
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MPxAttributePatternFactory:
    pass

class MPxCommand:
    def appendToResult(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Append a value to the result to be returned by the command."""
    def clearResult(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Clears the command's result."""
    @property
    def commandString(*args: Any, **kwargs: Any) -> Any:
        """Command string to be echoed to the user."""
    @commandString.setter
    def commandString(*args: Any, **kwargs: Any) -> Any:
        """Command string to be echoed to the user."""
    def currentResult(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the command's current result."""
    def currentResultType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the current result."""
    def displayError(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Display an error message."""
    def displayInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Display an informational message."""
    def displayWarning(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Display a warning message."""
    def doIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to execute the command."""
    def hasSyntax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to determine if the command provides an MSyntax object describing its syntax."""
    @property
    def historyOn(*args: Any, **kwargs: Any) -> Any:
        """Determines if construction history is on for the command."""
    @historyOn.setter
    def historyOn(*args: Any, **kwargs: Any) -> Any:
        """Determines if construction history is on for the command."""
    def isCurrentResultArray(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the command's current result is an array of values."""
    def isUndoable(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to determine if the command supports undo."""
    kDouble: int = ...
    kLong: int = ...
    kNoArg: int = ...
    kString: int = ...

    def redoIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to redo a previously undone command."""
    def setResult(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set the value of the result to be returned by the command."""
    def syntax(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the command's MSyntax object, if it has one."""
    def undoIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to undo a previously executed command."""

class MPxData:
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(src) -> self

        This method initializes an instance of an MPxData derived class from another existing instance.  This method can be thought of as the second half of a copy constructor for the class.  The default constructor has already been called for the instance, and this method is used to set the private data by copying the values from an existing instance.
        This method must be implemented by the derived class.

        * src (MPxData) - The object from which to copy the private data
        """
    kData: int = ...
    kGeometryData: int = ...
    kLast: int = ...

    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the custom data type.
        This method must be implemented by the derived class.
        """
    def readASCII(self: Self, *args: Any, **kwargs: Any) -> Any:
        """readASCII(argList, endOfTheLastParsedElement) -> int

        Creates Data in Data Block as specified by input from ASCII file record.
        Returns the new last argument parsed by this method.

        * argList (MArgList) - List of arguments read from ASCII record* endOfTheLastParsedElement (int) - points to last argument already parsed.
        """
    def readBinary(self: Self, *args: Any, **kwargs: Any) -> Any:
        """readBinary(in, length) -> int

        Creates Data in Data Block as specified by binary data from the given stream.
        Returns the numbers of data bytes processed or -1 in case of error.

        * in (bytearray) - Input stream
        * length (int) - Length in bytes of binary data to be read.
        """
    def typeId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Determines the type id of the Data object.
        This method must be implemented by the derived class.
        """
    def writeASCII(self: Self, *args: Any, **kwargs: Any) -> Any:
        """writeASCII() -> string

        Encodes Data in accordance with the ASCII file format and returns as string.
        """
    def writeBinary(self: Self, *args: Any, **kwargs: Any) -> Any:
        """writeBinary() -> bytearray

        Encodes Data in accordance with the binary file format and returns as bytearray.
        """

class MPxGeometryData(MPxData):
    def deleteComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteComponent(compList) -> bool

        This method should be overridden if this data is to support component deletion. For user defined shapes (MPxSurfaceShape) which support components, this method must be overridden if component deletion is to be supported when the shape has history.

        Returns True if the deletion was successfull, False otherwise.

        * compList (MObjectArray) - a list of components that are to be deleted
        """
    def deleteComponentsFromGroups(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteComponentsFromGroups(compList, groupIdArray, groupComponentArray) -> bool

        This method should be overridden to modify the groups that flows along with the geometry, as part of the data, based on the components being deleted. It should intelligently update the groups based on what gets deleted. The class MFnGeometryData can be used to access and modify grouping information for data.

        Returns True if the deletion was successfull, False otherwise.

        The groupIdArray and groupComponentArray should contain the updated grouping information after the deletion has occurred.

        * compList (MObjectArray) - a list of components that are to be deleted
        * groupIdArray [OUT] (MIntArray) - array of group id's
        * groupComponentArray (MObjectArray) - array of updated components, one for each group id
        """
    def getMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getMatrix(matrix) -> bool

        Gets the matrix associated to MPxGeometryData and retursn True if is identity

        * matrix [OUT] (MMatrix) - the returned matrix that takes a point from local object space to world space.
        """
    def iterator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iterator(componentList, component, useComponents, world=None) -> MPxGeometryIterator

        Associates a control point based geometry iterator with this data.
        This method is used in conjunction with MPxSurfaceShape and should be overridden if your shape is to support maya's deformations.

        The useComponents argument specifies whether the iteration is over the given componentList or the component.

        Returns an iterator for your geometry.

        * componentList (MObjectArray) - a list of components that are to be iterated over.
        * component (MObject) - a component to be iterator over.
        * useComponents (bool) - if True then componentList is to be iterated over, otherwise the iteration is on component.
        * world (bool) - specifies whether the iteration is for world space data.
        """
    @property
    def matrix(*args: Any, **kwargs: Any) -> Any:
        """The matrix associated to MPxGeometryData."""
    @matrix.setter
    def matrix(*args: Any, **kwargs: Any) -> Any:
        """The matrix associated to MPxGeometryData."""
    def smartCopy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """smartCopy(srcGeom) -> self

        This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

        This method is used to prvoide maya with an efficient way to copy the source data into the memory of this data with as little memory allocation as possible.

        This method is not mandatory and only needs to be overridden to improve performance of deformations on shapes.

        * srcGeom (MPxGeometryData) - the data to be copied
        """
    def updateCompleteVertexGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """updateCompleteVertexGroup(component) -> bool

        This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

        This method should make sure that complete vertex group data is up-to-date.
        If the given component is not complete (i.e. it represents all elements of your geometry) then you must mark is as complete using the methods of MFnComponent and return true if the component was updated, false if it was already complete.

        This method is used by deformers when deforming the "whole" object and not just selected components.

        Returns true if the component was updated, false if it was already complete.

        * component (MObject) - the component to test
        """

class MPxGeometryIterator:
    def component(self: Self, *args: Any, **kwargs: Any) -> Any:
        """component() -> MObject

        Returns a component for the current item in the iteration.
        """
    @property
    def currentPoint(*args: Any, **kwargs: Any) -> Any:
        """The current index of the iteration.
        This value is used when iterating over all elements of your geometry, i.e. when there are no components specified.
        """
    @currentPoint.setter
    def currentPoint(*args: Any, **kwargs: Any) -> Any:
        """The current index of the iteration.
        This value is used when iterating over all elements of your geometry, i.e. when there are no components specified.
        """
    def geometry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geometry() -> long/object

        Returns the user geometry that this iterator is iterating over.
        """
    def hasNormals(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasNormals() -> bool

        Returns whether the underlying geometry has normals.
        """
    def hasPoints(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasPoints() -> bool

        Returns whether the underlying geometry has point data.
        """
    def index(self: Self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns a unique index for the current item in the iteration.
        If the iteration is over the whole geometry then this index is the same as current point. If the iteration is over some elements of the geometry specified by a component then this index is the index in your geometry.
        """
    def indexUnsimplified(self: Self, *args: Any, **kwargs: Any) -> Any:
        """indexUnsimplified() -> int

        Returns a unique index for the current item in the iteration.
        Rather than being the iterator index this is the index for the actual item when simplification is skipping items. This index will be equal to index() if no simplification, otherwise it will be larger.
        """
    def isDone(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Returns whether all the items have been traversed yet.
        """
    def iteratorCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """iteratorCount() -> int

        Returns an estimate of how many items will be iterated over.
        """
    @property
    def maxPoints(*args: Any, **kwargs: Any) -> Any:
        """The largest index that will be iterated over.
        This value is used when iterating over all elements of your geometry, i.e. when there are no components specified.
        """
    @maxPoints.setter
    def maxPoints(*args: Any, **kwargs: Any) -> Any:
        """The largest index that will be iterated over.
        This value is used when iterating over all elements of your geometry, i.e. when there are no components specified.
        """
    def next(self: Self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next component.
        """
    def point(self: Self, *args: Any, **kwargs: Any) -> Any:
        """point() -> MPoint

        Returns the current component's positional data.
        """
    def reset(self: Self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Resets the iterator to the start of the components so that another pass over them may be made.
        """
    def setObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setObject(shape) -> self

        Optional method to set a shape object to iterate over to allow tweaking of the shape's history (input geometry).

        * shape (MPxSurfaceShape) - a user defined shape object.
        """
    def setPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(point) -> self

        Sets the current component's positional data.

        * point (MPoint) - the new positional value to set.
        """
    def setPointGetNext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPointGetNext(point) -> int

        Sets the current component's positional data, and returns the next index value.

        * point (MPoint) - the positional value to set.
        """

class MPxNode:
    def addAttribute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addAttribute(attr) -> None

        This method adds a new attribute to a user defined node type during the type's initialization.

        This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into  MFnPlugin.registerNode(). The attributes must first be created using one of the MFnAttribute classes, and can then be added using this method.

        For compound attributes, the proper way to use this method is by calling it with the parent attribute. If a compound attribute is passed, this method will add all of its children.
        NOTE: A failure will occur if you attempt to call addAttribute() on the children of a compound attribute.

        * attr (MObject) - new attribute to add.
        """
    def addExternalContentForFileAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addExternalContentForFileAttr(table, attr) -> bool

        This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute.

        The method will not overwrite existing items, i.e. items with the same key. (attribute name).  In this context, overwriting an item means the caller has called this function twice with the same attribute, or that two separate but identically named attributes were used.  If replacing an entry is the desired effect, it is the caller's responsibility to erase the previous item first.

        * table [OUT] (MExternalContentInfoTable) - table The table in which the new entry will be added.
        * attr (MObject) - The attribute for which the plug value will be queried for a location.

        Returns True if an item was sucessfully added to the table.  False if the attribute does not describe a non-empty location, or an item with the same key was already present in the table.
        """
    def attributeAffects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """attributeAffects(whenChanges, isAffected) -> None

        This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail.

        This method must be called for every attribute dependency when initializing the node's attributes.  The attributes must first be added using the MPxNode.addAttribute() method.  Failing to call this method will cause the node not to update when its inputs change. If there are no calls to this method in a node's initialization, then the compute method will never be called.

        This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into MFnPlugin.registerNode().  As a result, it does not work with dynamic attributes. For an alternate solution which handles dynamic as well as non-dynamic attributes refer to MPxNode.setDependentsDirty.()

        * whenChanges (MObject) - input attribute - MObject that points to an input attribute that has already been added.
        * isAffected (MObject) - affected output attribute - MObject that points to an output attribute that has already been added.
        """
    def compute(self: Self, *args: Any, **kwargs: Any) -> Any:
        """compute(plug, dataBlock) -> self

        This method should be overridden in user defined nodes.

        Recompute the given output based on the nodes inputs.  The plug represents the data value that needs to be recomputed, and the data block holds the storage for all of the node's attributes.

        The MDataBlock will provide smart handles for reading and writing this node's attribute values.  Only these values should be used when performing computations.

        When evaluating the dependency graph, Maya will first call the compute method for this node.  If the plug that is provided to the compute indicates that that the attribute was defined by the Maya parent node, the compute method should return None.  When this occurs, Maya will call the internal Maya node from which the user-defined node is derived to compute the plug's value. Returning any othervalue (including self) will tell Maya that this node successfully computed theplug. Raising an exception will tell Maya that this node failed at computingthe plug. Note that in most cases, Maya ignores node compute failures.

        In other words, the compute method should return None to get the Maya parent class to compute the plug. It should return self (or any other value) to indicate that the plug was computed successfully.

        This means that a user defined node does not need to be concerned with computing inherited output attributes.  However, if desired, these can be safely recomputed by this method to change the behaviour of the node.

        * plug (MPlug) - plug representing the attribute that needs to be recomputed.
        * block (MDataBlock) - data block containing storage for the node's attributes.
        """
    def configCache(self: Self, *args: Any, **kwargs: Any) -> Any:
        """configCache(evalNode, schema) -> None

        Defines the node's behavior when participating in Cached Playback.

        This method will be called at EM partitioning time, after rules evaluation.

        * evalNode (MEvaluationNode)  - This node's evaluation node, contains animated plug information
        * schema (MCacheSchema)       - Specification about what attributes to cache
        """
    def connectionBroken(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connectionBroken( plug, otherPlug, asSrc) -> self

        This method gets called when connections are broken with attributes of this node.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """
    def connectionMade(self: Self, *args: Any, **kwargs: Any) -> Any:
        """connectionMade(plug, otherPlug, asSrc) -> self

        This method gets called when connections are made to attributes of this node.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """
    def copyInternalData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copyInternalData(node) -> self

        This method is overriden by nodes that store attribute data in some internal format.

        On duplication this method is called on the duplicated node with the node being duplicated passed as the parameter.  Overriding this method gives your node a chance to duplicate any internal data you've been storing and manipulating outside of normal attribute data.

        * node (MPxNode) - the node that is being duplicated.
        """
    def dependsOn(self: Self, *args: Any, **kwargs: Any) -> Any:
        """dependsOn( plug, otherPlug) -> bool/None

        This method may be overridden by the user defined node. It should only be required to override this on rare occasions.

        This method determines whether a specific attribute depends on another attribute.

        You should return None to specify that Maya should determines the dependency (default).

        This is mainly to define dependency of dynamic attributes, since attributeAffects does not work with dynamic attributes.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        """
    def doNotWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """doNotWrite() -> bool

        use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out.
        """
    def existWithoutInConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """existWithoutInConnections() -> bool

        Determines whether or not this node can exist without input connections.

        If a node connected to this node is deleted resulting in no more input
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        Returns true if this node can exist without input connections, false otherwise
        """
    def existWithoutOutConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """existWithoutOutConnections() -> bool

        Determines whether or not this node can exist without output connections.

        If a node connected to this node is deleted resulting in no more output
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        Returns true if this node can exist without output connections, false otherwise
        """
    def forceCache(self: Self, *args: Any, **kwargs: Any) -> Any:
        """forceCache(ctx=MDGContext::current()) -> MDataBlock

        Get the datablock for this node. If there is no datablock then one will be created.
        NOTE: This should be used only in places where fast access to the datablock outside of a compute is critical such as the transformUsing method of MPxSurfaceShape.

        * ctx (MDGContext) - The context in which the datablock will be retrieved.
        """
    def getCacheSetup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getCacheSetup(evalNode, disablingInfo, setupInfo, objectArray) -> None

        Provide node-specific setup info for the Cached Playback system.

        This method will be called at EM partitioning time.  It works in one of two ways.
        - It can state that the node supports Cached Playback and background evaluation.  In this case it can use the cacheSetupInfo to configure preferences and requirements
        - It can state that this node cannot work with Cached Playback enabled and will  therefore cause Cached Playback to be disabled.  In this case it can use the disablingInfo to provide additional info about why Cached Playback is disabled.

        In case the answer depends on the value of attributes (for example, a node can have multiple modes, some of them working with caching and some of them not), the node can add the attributes to the monitored attribute list so they can be monitored in case the value changes.

        By default, this method states that Cached Playback is supported, but does not request to be cached by default.

        Note that regardless of the preferences expressed by a node, Caching Rules can always override the preferences from this method.  Caching Rules always have the last world.  This method simply indicates the built-in Evaluation Cache rule used by Maya's default Caching Modes that this node is to be cached.  Other rules can ignore or override this behavior.

        * evalNode (MEvaluationNode)              - This node's evaluation node, contains animated plug information
        * disablingInfo (MNodeCacheDisablingInfo) - Information about why the node disables Cached Playback to be reported to the user
        * cacheSetupInfo (MNodeCacheSetupInfo)    - Preferences and requirements this node has for Cached Playback
        * monitoredAttributes (MObjectArray)      - Attributes impacting the behavior of this method that will be monitored for change
        """
    def getExternalContent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getExternalContent(table) -> self

        The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details.

        Keys used to add items to this table will be the same that get passed to setExternalContent through its MExternalContentLocationTable parameter to perform a batched change of content location.

        When implementing getExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also add their external content to the table.

        The default implementation does nothing.

        * table [OUT] (MExternalContentInfoTable) - Content information table that this method must populate.
        """
    def getFilesToArchive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFilesToArchive(shortName=False, unresolvedName=False, markCouldBeImageSequence=False) -> list of strings

        Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command.

        Only include files that exist.

        If shortName is True, return just the filename portion of the path. Otherwise, return a full path.

        If unresolvedName is True, return the path before any resolution has been done (i.e leave it as a relative path, include unexpanded environment variables,  tildes, ".."s etc). Otherwise, resolve the file	path and return an absolute path (to resolve with standard Maya path resolution, use MFileObject.resolvedFullName()).

        * shortName (bool) - If True, only add the filename of the path.
        * unresolvedName (bool) - If True, add paths before any resolution, rather than absolute paths.
        * markCouldBeImageSequence (bool) - If True, append an asterisk after any file path that could be an image sequence (note: only used by maya.exe -archive).
        """
    def getInternalValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getInternalValue(plug, dataHandle) -> bool

        This method is overridden by nodes that store attribute data in some internal format.

        The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

        When internal attribute values are queried via getAttr or MPlug.getValue() this method is called.

        All internal data should respect the current context, which may be obtained from MDGContext::current()

        * plug (MPlug) - the attribute that is being queried.
        * dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
        """
    def getInternalValueInContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getInternalValueInContext(plug, dataHandle, ctx) -> bool [OBSOLETE]

        This method is obsolete. Override MPxNode.getInternalValue instead.

        * plug (MPlug) - the attribute that is being queried.
        * dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
        * ctx (MDGContext) - the context the method is being evaluated in.
        """
    def hasInvalidationRangeTransformation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasInvalidationRangeTransformation() -> bool

        Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method
        """
    def inheritAttributesFrom(self: Self, *args: Any, **kwargs: Any) -> Any:
        """inheritAttributesFrom(parentClassName) -> None

        This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node.

        This method will only work during the static initialization method of the user defined node class and must be called before any other attributes have been added.  The initialization method is the one that is passed into  MFnPlugin.registerNode().

        A plugin node may only inherit attributes from one other class of plugin node. Attempting to call this method multiple times within a node's initialization method will result in an error.

        Both node classes must be registered using the same MPxNode type, listed in MPxNode.type().

        * parentClassName (string) - class of node to inherit attributes from.
        """
    def internalArrayCount(self: Self, *args: Any, **kwargs: Any) -> Any:
        """internalArrayCount(plug) -> int
        internalArrayCount(plug, ctx) -> int  [OBSOLETE]

        This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock. This method is used by Maya to determine the non-sparse count of array elements during file IO. If the internal array is stored sparsely, you should return the maximum index of the array plus one. If the internal array is non-sparse then return the length of the array.

        This method does not need to be implemented for attributes that are stored in the datablock since Maya will use the datablock size.

        If this method is overridden, it should return -1 for attributes which it does not handle. Maya will use the datablock size to determine the array length when -1 is returned.

        All internal data should respect the current context, which may be obtained from MDGContext.current()

        * plug (MPlug) - the array plug.
        * ctx (MDGContext) - the context, default to MDGContext.current().
        """
    def isAbstractClass(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isAbstractClass() -> bool

        Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command.

        It is not necessary to override this method.
        """
    def isPassiveOutput(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isPassiveOutput(plug) -> bool

        This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user.

        * plug (MPlug) - plug representing output in question.
        """
    kAssembly: int = ...
    kBlendShape: int = ...
    kCameraSetNode: int = ...
    kClientDeviceNode: int = ...
    kConstraintNode: int = ...
    kDeformerNode: int = ...
    kDependNode: int = ...
    kEmitterNode: int = ...
    kEvaluatedDirectly: int = ...
    kEvaluatedIndirectly: int = ...
    kFieldNode: int = ...
    kFluidEmitterNode: int = ...
    kGeometryFilter: int = ...
    kHardwareShader: int = ...
    kHwShaderNode: int = ...
    kIkSolverNode: int = ...
    kImagePlaneNode: int = ...
    kLast: int = ...
    kLeaveDirty: int = ...
    kLocatorNode: int = ...
    kManipContainer: int = ...
    kManipulatorNode: int = ...
    kMotionPathNode: int = ...
    kObjectSet: int = ...
    kParticleAttributeMapperNode: int = ...
    kPostEvaluationTypeLast: int = ...
    kSkinCluster: int = ...
    kSpringNode: int = ...
    kSurfaceShape: int = ...
    kThreadedDeviceNode: int = ...
    kTransformNode: int = ...

    def legalConnection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """legalConnection(plug, otherPlug, asSrc) -> bool/None

        This method allows you to check for legal connections being made to attributes of this node.

        You should return None to specify that maya should handle this connection if you are unable to determine if it is legal.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """
    def legalDisconnection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """legalDisconnection(plug, otherPlug, arsSrc) -> bool/None

        This method allows you to check for legal disconnections being made to attributes of this node.

        You should return None to specify that maya should handle this disconnection if you are unable to determine if it is legal.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (boool) - is this plug a source of the connection.
        """
    def name(self: Self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL.

        It is not necessary to override this method.

        Returns the name of the node
        """
    def passThroughToMany(self: Self, *args: Any, **kwargs: Any) -> Any:
        """passThroughToMany(plug, plugArray) -> bool

        This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes.

        If this method is not implemented or returns False, the base class Maya implementation of this method calls passThroughToOne and returns the results of that call.

        * plug (MPlug) - the plug.
        * plugArray (MPlugArray) - the corresponding plugs.
        """
    def passThroughToOne(self: Self, *args: Any, **kwargs: Any) -> Any:
        """passThroughToOne(plug) -> plug

        This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:

        - When this node is deleted, the delete command will rewire the source of the input attribute to the destination of the output attribute if the source and destination are connected to nodes that are not deleted.
        - History traversal algorithms such as the bakePartialHistory command use this method to direct its traversal through a shape's construction history.
        - The base class Maya implementation of passThroughToAll will call this method if passThroughToAll returns False.

        * plug (MPlug) - the plug.
        """
    def postConstructor(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postConstructor() -> self

        Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object.
        The association between the these two objects is not made until after the MPxNode constructor is called. This implies that no MPxNode member function can be called from the MPxNode constructor.
        The postConstructor will get called immediately after the constructor when it is safe to call any MPxNode member function.
        """
    def postEvaluation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postEvaluation(context, evalNode, evalType) -> None

        Clean up node's internal state after threaded evaluation.

        After the evaluation graph execution, each node gets a chance to restore / update its internal states.For example, resetting draw state.

        This code has to be thread safe, non - blocking and work only on data owned by the node.

        This call will most likely happen from a worker thread.

        * context (MDGContext) - Context in which the evaluation is happening.
                                 This should be respected and only internal state
                                 information pertaining to it should be modified.
        * evaluationNode (MEvaluationNode) - Evaluation node which contains
                                             information about the dirty plugs the
                                             dirty plugs that were evaluated for this
                                             context.
        * evalType (PostEvaluationType)
          * kEvaluatedIndirectly : The node's compute function handled evaluation.
          * kEvaluatedDirectly   : Evaluation was performed externally and the results injected
                                   back into the node.  This would happen in situations such as
                                   extracting values from an external cache.The node needs to
                                   update any additional internal state based on the new values.
          * kLeaveDirty          : Evaluation was performed without updating this node. Internal
                                   state should be updated to reflect that the node is dirty.
        """
    def preEvaluation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """preEvaluation(context, evalNode) -> None

        Prepare a node's internal state for threaded evaluation.

        During the evaluation graph execution each node gets a chance to reset its internal states just before being evaluated.

        This code has to be thread safe, non - blocking and work only on data owned by the node.

        The timing of this callback is at the discretion of evaluation graph dependencies and individual evaluators.This means, it should be used purely to prepare this node for evaluation and no particular order should be assumed.

        This call will most likely happen from a worker thread.

        * context (MDGContext) - Context in which the evaluation is happening.
                                 This should be respected and only internal state
                                 information pertaining to it should be modified.
        * evaluationNode (MEvaluationNode) - Evaluation node which contains
                                             information about the dirty plugs that
                                             are about to be evaluated for the context.
                                             Should be only used to query information.
        """
    def setDependentsDirty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDependentsDirty(plug, plugArray) -> self

        This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:



        - Allows attributeAffects-style relationships to be handled for dynamically-added attributes. Since MPxNode.attributeAffects() can only be used with non-dynamic attributes, use of this method allows a way for all attributes of a node to affect one another, both dynamic and non-dynamic.

        - Provides more flexible relationships than what is available with MPxNode.attributeAffects(). For example, you may wish to not dirty plugs when the current frame is one. However, as the routine is called during dirty propagation, there are restrictions on what can be done within the routine, most importantly you must not cause any dependency graph computation. For details, see the IMPORTANT NOTE below.



        This method is designed to work harmoniously with MPxNode.attributeAffects() on the same node. Alternately, you can do all affects relationships within a yourNode.setDependentsDirty() implementation.

        The body of a user-implemented setDependentsDirty() implementation might look like the following example, which causes the plug called "B" to be set dirty whever plug "A" is changed, i.e. A affects B.

        * plug (MPlug) - plug which is being set dirty by Maya.
        * plugArray the programmer should add any plugs which they want to set dirty to this list.
        """
    def setDoNotWrite(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDoNotWrite(bool) -> self

        Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out.

        NOTES:
        1. Plug-in "requires" information will be written out with the model when saved.  But a subsequent reload and resave of the file will cause these to go away.
        2. If this node is a DAG and has a parent or children, the "do not write" flag of the parent or children will not be set. It is the developer's responsibility to ensure that the resulting scene file is capable of being read in without errors due to unwritten nodes.
        """
    def setExistWithoutInConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setExistWithoutInConnections(bool) -> bool

        This method specifies whether or not the node can exist without input
        connections.

        If a node connected to this node is deleted resulting in no more input
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        * flag (bool) true if this node can exist without input connections, false otherwise
        """
    def setExistWithoutOutConnections(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setExistWithoutOutConnections(bool) -> bool

        This method specifies whether or not the node can exist without
        output connections.

        If a node connected to this node is deleted resulting in no more output
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        * flag (bool) true if this node can exist without output connections, false otherwise
        """
    def setExternalContent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setExternalContent(table) -> self

        This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts.

        The keys in the map must be the same as the ones provided by the node in getExternalContent.  The values are the new locations.

        When implementing setExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also set their external content.

        The default implementation does nothing.

        * table Key->location table with new content locations.
        """
    def setExternalContentForFileAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setExternalContentForFileAttr(attr, table) -> bool

        This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name.

        The method will not write to the plug if the attribute is not found in the  table.

        * attr (MObject) - The attribute of the plug we want to write to.
        * table (MExternalContentLocationTable) - A table which may hold or not the value for a given plug.

        Returns True if the plug was successfully written to. False if no entry in the table was named after the attribute or if no plug was found.
        """
    def setInternalValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setInternalValue(plug, dataHandle) -> bool


        This method is overriden by nodes that store attribute data in some internal format.

        The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

        When internal attribute values are set via setAttr or MPlug.setValue() this method is called.

        Another use for this method is to impose attribute limits.

        All internal data should respect the current context, which may be obtained from MDGContext::current()

        * plug (MPlug) - the attribute that is being set.
        * dataHandle (MDataHandle) - the dataHandle containing the value to set.
        """
    def setInternalValueInContext(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setInternalValueInContext(plug, dataHandle, ctx) -> bool  [OBSOLETE]

        This method is obsolete. Override MPxNode.setInternalValue instead.

        * plug (MPlug) - the attribute that is being set.
        * dataHandle (MDataHandle) - the dataHandle containing the value to set.
        * ctx (MDGContext) - the context the method is being evaluated in.
        """
    def setMPSafe(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMPSafe(bool) -> self

        This method is obsolete. Override MPxNode.setSchedulingType instead.

        Set a flag to specify if a user defined shading node is safe for multi-processor rendering. For a shading node to be MP safe, it cannot access any shared global data and should only use attributes in the datablock to get input data and store output data.

        NOTE: This should be called from the postConstructor() method for shading node plug-ins only. If a shading node is non-safe, then it will only be useful during single processor rendering.
        """
    def shouldSave(self: Self, *args: Any, **kwargs: Any) -> Any:
        """shouldSave(plug) -> bool/None

        This method may be overridden by the user defined node.  It should only be required to override this on rare occasions.

        This method determines whether a specific attribute of this node should be written out during a file save.  The default behavior is to only write the value if it differs from the default and is not being supplied by a connection.  This behavior should be sufficient in most cases.
        This method is not called for ramp attributes since they should always be written.

        * plug (MPlug) - plug representing the attribute to be saved.
        """
    def thisMObject(self: Self, *args: Any, **kwargs: Any) -> Any:
        """thisMObject() -> MObject

        Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes.
        """
    def transformInvalidationRange(self: Self, *args: Any, **kwargs: Any) -> Any:
        """transformInvalidationRange(plug, timeRange) -> timeRange

        Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... )

        * source (MPlug)     - The source plug in this node where the dirty propagation comes from
        * input (MTimeRange) - The incoming invalidation range


        Returns The output invalidation range for all the dependents of plug 'source'

        WARNING: You cannot do any evaluation in this function, because it can be called in dirty-propagation
        WARNING: Do *not* call MPxNode::transformInvalidationRange from your override method
        NOTE: If a plugin node have invalidation-range-transformation *conditionally* Only transform the invalidation range when attribute 'enableIRT' is set The plugin should call MPxNode::transformInvalidationRange to signal it does not perform any IRT.
        """
    def type(self: Self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Returns the type of node that this is.  This is used to differentiate user defined nodes that are derived off different MPx base classes.

        It is not necessary to override this method.

          kDependNode                    Custom node derived from MPxNode
          kLocatorNode                   Custom locator derived from MPxLocatorNode
          kDeformerNode                  Custom deformer derived from MPxDeformerNode
          kManipContainer                Custom container derived from MPxManipContainer
          kSurfaceShape                  Custom shape derived from MPxSurfaceShape
          kFieldNode                     Custom field derived from MPxFieldNode
          kEmitterNode                   Custom emitter derived from MPxEmitterNode
          kSpringNode                    Custom spring derived from MPxSpringNode
          kIkSolverNode                  Custom IK solver derived from MPxIkSolverNode
          kHardwareShader                Custom shader derived from MPxHardwareShader
          kHwShaderNode                  Custom shader derived from MPxHwShaderNode
          kTransformNode                 Custom transform derived from MPxTransform
          kObjectSet                     Custom set derived from MPxObjectSet
          kFluidEmitterNode              Custom fluid emitter derived from MpxFluidEmitterNode
          kImagePlaneNode                Custom image plane derived from MPxImagePlane
          kParticleAttributeMapperNode   Custom particle attribute mapper derived from MPxParticleAttributeMapperNode
          kCameraSetNode                 Custom director derived from MPxCameraSet
          kConstraintNode                Custom constraint derived from MPxConstraint
          kManipulatorNode               Custom manipulator derived from MPxManipulatorNode
          kClientDeviceNode              Custom threaded device derived from MPxThreadedDeviceNode
          kThreadedDeviceNode            Custom threaded device node
          kAssembly                      Custom assembly derived from MPxAssembly
          kSkinCluster					Custom deformer derived from MPxSkinCluster
          kGeometryFilter				Custom deformer derived from MPxGeometryFilter
                 kBlendShape					Custom deformer derived from MPxBlendShape
        """
    def typeId(self: Self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Returns the TYPEID of this node.
        """
    def typeName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """typeName() -> string

        Returns the type name of this node.  The type name identifies the node type to the ASCII file format
        """

class MPxSurfaceShape(MPxNode):
    def acceptsGeometryIterator(self: Self, *args: Any, **kwargs: Any) -> Any:
        """acceptsGeometryIterator(component, writeable=True, forReadOnly=False) -> bool
        acceptsGeometryIterator(writeable=True) -> boolboundingBox() -> MBoundingBox

        Returns True if the shape can supply a component iterator.
        This methods should be overridden to return True. The default is to return False.

        * component (MObject) - the component to test
        * writeable (bool) - is this component type writable by an iterator
        * forReadOnly (bool) - is this component type readable by an iterator
        """
    def activeComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """activeComponents() -> MObjectArray

        Returns a list of active (selected) components for the shape.
        """
    def boundingBox(self: Self, *args: Any, **kwargs: Any) -> Any:
        """boundingBox() -> MBoundingBox

        This method should be overridden to return a bounding box for the shape.
        If this method is overridden, then MPxSurfaceShape.isBounded() should also be overridden to return True.
        """
    boundingBoxCenterX: MObject = ...
    boundingBoxCenterY: MObject = ...
    boundingBoxCenterZ: MObject = ...

    def cachedShapeAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """cachedShapeAttr() -> MObject

        Returns the attribute containing the shape's cached geometry, if it has one.
        """
    def canMakeLive(self: Self, *args: Any, **kwargs: Any) -> Any:
        """canMakeLive() -> bool

        This method is used by Maya to determine whether a surface can be made live. It can be overridden to return True if you wish to allow your surface to be made live. If you return True, you will also need to implement both closestPoint() overloads. The default is to return False.
        """
    center: MObject = ...

    def childChanged(self: Self, *args: Any, **kwargs: Any) -> Any:
        """childChanged(state=kObjectChanged) -> self

        This method can be used to trigger the shape to recalculate its bounding box.

        * state (int) - the type of change that has occurred

        Valid state:
          kObjectChanged         Object geometry changed. Internal caches need to be updated.
          kBoundingBoxChanged    Object geometry is unchanged but its bounding box has changed.
                                 This might happen if the object was moved or an offset changed.
        """
    def closestPoint(self: Self, *args: Any, **kwargs: Any) -> Any:
        """closestPoint(toThisPoint, theClosestPoint, tolerance=MPoint.kTolerance) -> self
        closestPoint(raySource, rayDirection, theClosestPoint, theClosestNormal, findClosestOnMiss, tolerance=MPoint.kTolerance) -> bool

        This methods are respectively used by Maya in functions (such as select) that require closest point information from your surface and for snapping queries when your surface is live.

        For selection:
        If you've overridden canMakeLive() to return True, this method is also used by Maya for some snapping queries when your surface is live.

        * toThisPoint (MPoint) - the point to test against.
        * theClosestPoint [OUT] (MPoint) - the closest point on your surface.
        * tolerance (float) - tolerance to use in your calculations.


        For snapping:
        If you override this method, you should set theClosestPoint to the closest point on your surface intersected by the ray defined by raySource and rayDirection. You should also populate the theClosestNormal parameter with the surface normal at that intersection point.

        If no intersection is found and findClosestOnMiss is True, you should still provide a point on your surface closest to the ray defined by raySource and rayDirection. When used for live snapping, this allows the user to click and drag outside the bounds	of a live surface and still have it snap to the nearest point on it within the viewport. Note, performing a pure 3D closest point of approach test in this situation may not give the most natural result for live mesh snapping.
        To provide behavior that matches Maya, you can project your surface onto the plane defined by the ray, then perform your calculations. This will account for view perspective and give accurate live snap points along the silhouette of the surface.

        If findClosestOnMiss is False, you should not provide a point and normal when the ray misses.
        Should return True if theClosestPoint and theClosestNormal have been set, False otherwise.
        canMakeLive() must also be overridden to return True.

        * raySource (MPoint) - the origin of the ray to test against
        * rayDirection (MVector) - the direction of the ray to test against
        * theClosestPoint [OUT] (MPoint) - the closest point on your surface
        * theClosestNormal [OUT] (MVector) - the normal at the closest point on your surface
        * findClosestOnMiss (bool) - when True, you should calculate theClosestPoint and theClosestNormal even if the ray misses your surface.
        * tolerance (float) - tolerance to use in your calculations
        """
    def componentToPlugs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """componentToPlugs(component, selectionList) -> self

        Converts the given component into a selection list of plugs.
        This method is used to associate a shapes components into the corresponding attributes (plugs) within the shape. For example, it gets called by the translate manipulator to determine which attributes should be driven by the manipulator, and by the setKeyframe command to determine where to connect animCurves for components.

        This method should be overridden if the shape supports components that can be selected and moved in Maya.

        * component (MObject) - the component to be converted
        * list (MSelectionList) - a selection list where the plug should be added
        """
    def convertToTweakNodePlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """convertToTweakNodePlug(plug) -> bool

        Check if a tweak node is connected to this node. If it is, then reset the supplied plug to contain the controlPoints attribute on the tweak node.
        Returns True if a tweak node was found, False if the plug was unchanged

        * plug (MPlug) - plug which will be set to point to the associated tweak node plug if a tweak node is connected
        """
    def createFullRenderGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createFullRenderGroup() -> MObject

        Returns a component containing all of renderable elements in the shape.
        This method is used to create a component containing every renderable element in the object.

        This method is supposed to return non-null object only if the dag object contains renderable components. Type of the return component should is the same as the one returned by MPxSurfaceShape::renderGroupComponentType().
        """
    def createFullVertexGroup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """createFullVertexGroup() -> MObject

        Returns a component containing all of the vertices in the shape.
        This method is used to create a component containing every vertex/CV in the object.

        This method is supposed to return non-null object only if the dag object contains vertices/CVs (control points), so derived classes that do should override this method.
        """
    def deleteComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteComponents(componentList, undoInfo) -> bool

        Returns True if this method was successful, False otherwise.
        This method should be overridden if the shape is to support deletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component can be stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.

        * componentList (MObjectArray) - List of components to be deleted
        * undoInfo (MDoubleArray) - Values used for undo purposes
        """
    def excludeAsPluginShape(self: Self, *args: Any, **kwargs: Any) -> Any:
        """excludeAsPluginShape() -> bool

        A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape. By overriding excludeAsPluginShape() to return False, you can change that behaviour so that this shape is still displayed even when the display of "Plugin Shapes" is disabled.
        The default implementation returns True.
        Returns True to have this shape obey the "Plugin Shapes" settings in the viewport's "Show" menu; False to have it ignore that setting.
        """
    def geometryData(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geometryData() -> MObject

        Returns the geometry data of the shape. The geometry data must be derived from the MPxGeometryData class.

        The data is used by Maya to add, edit and query component grouping (set) information for the shape. This set information is stored and managed by Maya's shape base class, geometryShape.
        """
    def geometryIteratorSetup(self: Self, *args: Any, **kwargs: Any) -> Any:
        """geometryIteratorSetup(componentList, components, forReadOnly=False) -> MPxGeometryIterator

        This method should be overridden by the user to return a geometry iterator compatible with the user's geometry.
        A geometry iterator is used for iterating over the components of a shape, such as the vertices of a mesh, in a generic manner.

        The components to be iterated over are passed to this function in on of two ways, as a list of components, or as a single component.
        Only one of these arguments is used at any particular time.

        * componentList (MObjectArray) - a list of components to be iterated over
        * components (MObject) - the components to be iterated over
        * forReadOnly (bool) - specifies whether the iterator is for read-only
        """
    def getComponentSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getComponentSelectionMask() -> MSelectionMask

        Returns the selection mask of the shape.
        This routine must be overridden if the shape is to support interactive component selection in Viewport 2.0 and should provide information about the selection mask of the shape component.
        """
    def getShapeSelectionMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getShapeSelectionMask() -> MSelectionMask

        Returns the selection mask of the shape.
        This routine must be overridden if the shape is to support interactive object selection in Viewport 2.0 and should provide information about the selection mask of the shape.
        """
    def getWorldMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getWorldMatrix(block, instanceGeom) -> MMatrix

        Returns MMatrix which takes a point from local object space to world space.

        * block (MDataBlock) - a MDataBlock
        * instanceGeom (int) - the instance this MPxSurfaceShape corresponds to
        """
    def hasActiveComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasActiveComponents() -> bool

        This method is used to determine whether or not the shape has active (selected) components.
        """
    instObjGroups: MObject = ...
    intermediateObject: MObject = ...
    inverseMatrix: MObject = ...

    def isBounded(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isBounded() -> bool

        This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient.
        Returns a boolean value indicating whether a bounding box routine has been supplied
        """
    @property
    def isRenderable(*args: Any, **kwargs: Any) -> Any:
        """Specifies whether the shape is a renderable shape.
        Making a shape renderable allows the shape to have shading group assignments.
        """
    @isRenderable.setter
    def isRenderable(*args: Any, **kwargs: Any) -> Any:
        """Specifies whether the shape is a renderable shape.
        Making a shape renderable allows the shape to have shading group assignments.
        """
    isTemplated: MObject = ...

    def localShapeInAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """localShapeInAttr() -> MObject

        Returns the attribute containing the shape's input geometry in local space.

        This method will be called by Maya to determine if the shape has construction history and must be overridden if the shape is to support deformers.
        """
    def localShapeOutAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """localShapeOutAttr() -> MObject

        Returns the attribute containing the shape's output geometry in local space.

        This method must be overridden if the shape is to support deformers.
        """
    mControlPoints: MObject = ...
    mControlValueX: MObject = ...
    mControlValueY: MObject = ...
    mControlValueZ: MObject = ...
    mHasHistoryOnCreate: MObject = ...

    def match(self: Self, *args: Any, **kwargs: Any) -> Any:
        """match(mask, componentList) -> bool

        This method is used to check for matches between a selection type (or mask) and a given component. If your shape has components representing attributes then this method is used to match up your components with selection masks.

        This is used by sets and deformers to make sure that the selected components fall into the "vertex only" category. This is useful when you want to make sure that only a particular component can be deformed.

        * mask (MSelectionMask) - the selection mask to test against
        * componentList (MObjectArray) - a list of components to be tested
        """
    def matchComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """matchComponent(item, spec, list) -> int

        This method is used to convert the string representation of a component into a component object and to validate that the indices.

        This method should be overridden if the shape has components.

        * item (MSelectionList) - DAG selection item for the object being matched
        * spec (MAttributeSpecArray) - attribute specification object
        * list (MSelectionList) - list to add components to

        List of valid component match result:
          kMatchOk                       The component was matched without error.
          kMatchNone                     No component was matched.
          kMatchTooMany                  Not used.
          kMatchInvalidName              One of the names in the attribute specification was not valid.
          kMatchInvalidAttribute         Not used.
          kMatchInvalidAttributeIndex    The attribute specification contained an index for a non-array attribute.
          kMatchInvalidAttributeRange    An attribute index was out of range.
          kMatchInvalidAttributeDim      The attribute specification provided the wrong number of dimensions for an attribute.
        """
    matrix: MObject = ...

    def newControlPointComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """newControlPointComponent() -> MObject

        The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent) in order to support rigid skinning binds.

        This method can be overridden to support other types of components such as MFnDoubleIndexedComponent and MFnTripleIndexedComponent	and should return a new component of that type.  The types allowed are those listed in the create() method docs for each MFn*IndexedComponent.
        """
    nodeBoundingBox: MObject = ...
    nodeBoundingBoxMax: MObject = ...
    nodeBoundingBoxMaxX: MObject = ...
    nodeBoundingBoxMaxZ: MObject = ...
    nodeBoundingBoxMin: MObject = ...
    nodeBoundingBoxMinX: MObject = ...
    nodeBoundingBoxMinY: MObject = ...
    nodeBoundingBoxMinZ: MObject = ...
    nodeBoundingBoxSize: MObject = ...
    nodeBoundingBoxSizeX: MObject = ...
    nodeBoundingBoxSizeY: MObject = ...
    nodeBoundingBoxSizeZ: MObject = ...
    objectColor: MObject = ...
    objectGroupColor: MObject = ...
    objectGroupId: MObject = ...
    objectGroups: MObject = ...
    objectGrpCompList: MObject = ...
    parentInverseMatrix: MObject = ...
    parentMatrix: MObject = ...

    def pointAtParm(self: Self, *args: Any, **kwargs: Any) -> Any:
        """pointAtParm(atThisParm, evaluatedPoint) -> bool

        This method is used by Maya in functions (such as select) that require point at parameter values. This only makes sense for parametric surfaces such as NURBS.
        Returns True if a point was found, False otherwise

        * atThisParm (MPoint) - the parameter to check
        * evaluatedPoint [OUT] (MPoint) - the surface point
        """
    def renderGroupComponentType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """renderGroupComponentType() -> int

        This method is used to return the type of renderable components for this shape. It should return a type among MFn::kMeshPolygonComponent, MFn::kSubdivFaceComponent and MFn::kSurfaceFaceComponent, which is used in the creation of per-face/patch shader assignment.

        Returns the type of renderable components for this shape.
        See MFnSet.addMember()
        """
    def transformUsing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """transformUsing(matrix, componentList, cachingMode=None, pointCache=None) -> self

        Transform the given components using the specified transformation matrix.
        This method should be overridden if the shape supports components that can be transformed using maya's move, scale, and rotate tools.

        * matrix (MMatrix) - the matrix representing the transformation that is to be applied to the components
        * componentList (MObjectArray) - a list of components to be transformed. If the list is empty, it indicates that every point in the geometry should be transformed.
        * cachingMode (int) - whether the points should be cached in the pointCache argument, or restored from the pointCache
        * pointCache (MPointArray) - used to store for undo and restore points during undo

        List of valid caching modes:
          kNoPointCaching             No point caching.
          kSavePoints                 Points should be saved for undo in the point cache.
          kRestorePoints              Points should be restored from the point cache.
          kUpdatePoints               Transform and update the points in the point cache.
          kTransformOriginalPoints    Transform using use the original pre-transformation values stored in the pointCache.
        """
    def tweakUsing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """tweakUsing(matrix, componentList, cachingMode, pointCache, handle) -> self

        Transform the given components using the specified transformation matrix.
        This method should be overridden if the shape supports components that can be transformed using maya's move, scale, and rotate tools. This method is called when the shape has history & connected to a tweak node. The most common reason why the shape would be connected to a tweak node is if it is being deformed. When a shape is connected to a tweak node, transformations applied to the points are placed in the tweak node rather than in the shape itself.

        * matrix (MMatrix) - the matrix representing the transformation that is to be applied to the components
        * componentList (MObjectArray) - a list of components to be tranformed. If the list is empty, it indicates that every point in the geometry should be transformed.
        * cachingMode (int) - whether the points should be cached in the pointCache argument, or restored from the pointCache
        * pointCache (MPointArray) - used to store for undo and restore points during undo
        * handle (MArrayDataHandle) - array data handle where the tweaks are stored

        See transformUsing() for a list of valid caching mode
        """
    def undeleteComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """undeleteComponents(componentList, undoInfo) -> bool

        This method should be overridden if the shape is to support undeletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component is stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.
        Returns True if this method was successful, False otherwise

        * componentList (MObjectArray) - List of components that were deleted
        * undoInfo (MDoubleArray) - Values used for undo purposes
        """
    useObjectColor: MObject = ...

    def vertexOffsetDirection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """vertexOffsetDirection(component, direction, mode, normalize) -> bool

        This method should be overridden if the shape supports components that can be moved in the direction of the normal or UV's using the move vertex normal tool.

        This method should calculate the offset direction for a vertex components. The direction vector array is an array of offsets corresponding to the elements in the component. The mode argument specifies the type of movement that is being performed.

        The default for this method is to return False, i.e. no support for move normal tool.
        Returns True if the shape supports the current mode, False if the shape cannot do the requested vertex move

        * component (MObject)
        * direction (MVectorArray)
        * mode (int) - The type of vertex movement
        * normalize (bool) - specifies whether the offset vectors should be normalized

        List of valid types:
          kNormal       Move in normal direction.
          kUTangent     Move in u tangent direction.
          kVTangent     Move in v tangent direction.
          kUVNTriad     Calculate u, v, and normal offsets.
        """
    visibility: MObject = ...

    def weightedTransformUsing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """weightedTransformUsing(xform, space, componentList, cachingMode, pointCache, freezePlane) -> self

        Transform the given components with interpolation using the specified transformation matrix.

        If not overridden, then a default implementation will be used to perform the transformation and interpolation.
        The default implementation calls setPoint() for each transformed point.

        * xform (MTransformationMatrix) - the matrix representing the transformation that is to be applied to the components.
        * space (MMatrix) - the matrix representing the transformation space to perform the interpolated transformation. A value of None indicates it should be ignored.
        * componentList (MObjectArray) - a list of components to be transformed and their weights. This list will not be empty.* cachingMode (int) - whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using use the original values in the pointCache.
        * pointCache (MPointArray) - used to store for undo and restore points during undo
        * freezePlane (MPlane) - used for symmetric transformation of components. A value of None indicates it is not used and there is no symmetric transformation.

        See transformUsing() for a list of valid caching mode
        """
    def weightedTweakUsing(self: Self, *args: Any, **kwargs: Any) -> Any:
        """weightedTweakUsing(xform, space, componentList, cachingMode, pointCache, freezePlane, handle) -> self

        Transform the given components with interpolation using the specified transformation matrix.
        This method is called for transforming components using maya's move, scale, and rotate tools when the shape has history and is connected to a tweak node. The most common reason why the shape would be connected to a tweak node is if it is being deformed. When a shape is connected to a tweak node, transformations applied to the points are placed in the tweak node rather than in the shape itself.

        If not overridden, then a default implementation will be used to perform the transformation and interpolation.
        The default implementation calls setPoint() for each transformed point.

        * xform (MTransformationMatrix) - the matrix representing the transformation that is to be applied to the components
        * space (MMatrix) - the matrix representing the transformation space to perform the interpolated transformation. A value of None indicates it should be ignored.
        * componentList (MObjectArray) - a list of components to be transformed and their weights. This list will not be empty.
        * cachingMode (int) - whether the points should be added/updated in the pointCache, restored from the pointCache, or transform using the original values in the pointCache.
        * pointCache (MPointArray) - used to store for undo and restore points during undo
        * freezePlane (MPlane) - used for symmetric transformation of components. A value of None indicates it is not used and there is no symmetric transformation.
        * handle (MArrayDataHandle) - array data handle where the tweaks are stored

        See transformUsing() for a list of valid caching mode
        """
    worldInverseMatrix: MObject = ...
    worldMatrix: MObject = ...

    def worldShapeOutAttr(self: Self, *args: Any, **kwargs: Any) -> Any:
        """worldShapeOutAttr() -> MObject

        Returns the attribute containing the shape's output geometry in world space.

        This method must be overridden if the shape is to support deformers.
        """

class MQuaternion:
    def asAxisAngle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as a tuple containing an axis vector and an angle in radians about that axis."""
    def asEulerRotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent MEulerRotation."""
    def asMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent rotation matrix."""
    def conjugate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the conjugate of this quaternion (i.e. x, y and z components negated)."""
    def conjugateIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place conjugation (i.e. negates the x, y and z components)."""
    def exp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the exponent of this one."""
    def inverse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the inverse of this one."""
    def invertIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place inversion."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the distance between the two quaternions (in quaternion space) is less than or equal to the given tolerance."""
    kIdentity: MQuaternion = ...
    kTolerance: float = ...

    def log(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the natural log of this one."""
    def negateIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place negation of the x, y, z and w components."""
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the normalized version of this one (i.e. scaled to unit length)."""
    def normalizeIt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """In-place normalization (i.e. scales the quaternion to unit length)."""
    def setToXAxis(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the X-axis."""
    def setToYAxis(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Y-axis."""
    def setToZAxis(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Z-axis."""
    def setValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set the value of this quaternion to that of the specified MQuaternion, MEulerRotation, MMatrix or MVector and angle."""
    def slerp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the quaternion at a given interpolation value along the shortest path between two quaternions."""
    def squad(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the quaternion at a given interpolation value along a cubic curve segment in quaternion space."""
    def squadPt(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion representing an intermediate point which when used with squad() will produce a C1 continuous spline."""
    @property
    def w(*args: Any, **kwargs: Any) -> Any:
        """Real component"""
    @w.setter
    def w(*args: Any, **kwargs: Any) -> Any:
        """Real component"""
    @property
    def x(*args: Any, **kwargs: Any) -> Any:
        """Imaginary X component"""
    @x.setter
    def x(*args: Any, **kwargs: Any) -> Any:
        """Imaginary X component"""
    @property
    def y(*args: Any, **kwargs: Any) -> Any:
        """Imaginary Y component"""
    @y.setter
    def y(*args: Any, **kwargs: Any) -> Any:
        """Imaginary Y component"""
    @property
    def z(*args: Any, **kwargs: Any) -> Any:
        """Imaginary Z component"""
    @z.setter
    def z(*args: Any, **kwargs: Any) -> Any:
        """Imaginary Z component"""

class MRampAttribute:
    def addEntries(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds entries to the ramp."""
    def createColorRamp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates and returns a new color ramp attribute."""
    def createCurveRamp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates and returns a new curve ramp attribute."""
    def createRamp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Creates and returns a new color or curve ramp attribute initialized with values."""
    def deleteEntries(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Removes from the ramp those entries with the specified indices."""
    def getEntries(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a tuple containing all of the entries in the ramp."""
    def getValueAtPosition(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the entry at the given position."""
    def hasIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return true if an entry is defined at this index."""
    @property
    def isColorRamp(*args: Any, **kwargs: Any) -> Any:
        """True if the attribute is a color ramp."""
    @isColorRamp.setter
    def isColorRamp(*args: Any, **kwargs: Any) -> Any:
        """True if the attribute is a color ramp."""
    @property
    def isCurveRamp(*args: Any, **kwargs: Any) -> Any:
        """True if the attribute is a curve ramp."""
    @isCurveRamp.setter
    def isCurveRamp(*args: Any, **kwargs: Any) -> Any:
        """True if the attribute is a curve ramp."""
    kLinear: int = ...
    kNone: int = ...
    kSmooth: int = ...
    kSpline: int = ...

    def numEntries(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of entries in the ramp."""
    def pack(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Change the indices numbering by re-ordering them from 0."""
    def setInterpolationAtIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the interpolation of the entry at the given index."""
    def setPositionAtIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the position of the entry at the given index."""
    def setRamp(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set this ramp with one or multiple entries. Current entries are removed before adding the new one(s)."""
    def setValueAtIndex(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the entry at the given index."""
    def sort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sort the ramp by position. Indices are also re-ordered during sort."""

class MRichSelection:
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self


        Empties the rich selection.
        """
    def getRawSymmetryMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getRawSymmetryMatrix() -> (MMatrix, space)

        Returns a tuple containing the raw symmetry matrix to use for the
        symmetric components of the rich selection, and the transformation
        space used by the matrix (see MSpace). The caller is responsible for
        handling any necessary transformation space conversions.
        """
    def getSelection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSelection() -> MSelectionList

        Returns a copy of the non-symmetry component of the rich selection.
        """
    def getSymmetry(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSymmetry() -> MSelectionList

        Returns a copy of the symmetry component of the rich selection.
        """
    def getSymmetryMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSymmetryMatrix(MDagPath, space) -> MMatrix

        Returns the symmetry matrix to use for the symmetric component of
        the specified DAG object. The matrix will already be converted to
        use the specified transformation space (see MSpace).
        """
    def getSymmetryPlane(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSymmetryPlane(MDagPath, space) -> MPlane

        Returns the plane of symmetry, in the specified transformation space
        (see MSpace). This can be used to enforce seam weights in tools that
        support symmetry. Note that the direction of the plane carries no
        significance. Specifically, having a positive offset from the plane
        does not imply a point is part of the non-symmetric selection.
        """
    def setSelection(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setSelection(MSelectionList) -> self

        Sets the non-symmetry component of the rich selection.
        """

class MSceneMessage(MMessage):
    def addCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCallback(message, function, clientData=None) -> id

        Adds a new callback for the specified scene message.
        If a 'before' message is sent, the corresponding 'after' message
        will be as well.
        Callbacks can be added to the following Message constant with this function: kSceneUpdate
         kBeforeNew
         kAfterNew
         kBeforeImport
         kAfterImport
         kBeforeOpen
         kAfterOpen
         kBeforeFileRead
         kAfterFileRead
         kAfterSceneReadAndRecordEdits
         kBeforeExport
         kExportStarted
         kAfterExport
         kBeforeSave
         kAfterSave
         kBeforeCreateReference
         kBeforeCreateReferenceAndRecordEdits
         kAfterCreateReference
         kAfterCreateReferenceAndRecordEdits
         kBeforeRemoveReference
         kAfterRemoveReference
         kBeforeImportReference
         kAfterImportReference
         kBeforeExportReference
         kAfterExportReference
         kBeforeUnloadReference
         kAfterUnloadReference
         kBeforeLoadReference
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReference
         kAfterLoadReferenceAndRecordEdits
         kBeforeSoftwareRender
         kAfterSoftwareRender
         kBeforeSoftwareFrameRender
         kAfterSoftwareFrameRender
         kSoftwareRenderInterrupted
         kMayaInitialized
         kMayaExiting

        Note that for referencing, the creation of the reference (i.e. creation of
        the reference node and associated structures) is separate from the loading
        of the reference itself (i.e. read the nodes from file).

        The kBeforeCreateReference message will be sent when a reference is created.
        So it will happen for both loaded and unloaded references. But the
        kBeforeLoadReference message will only be sent when the file is read from disk.

        When opening a file with a loaded reference, the callback order is as follows:
         kBeforeCreateReference
         kBeforeCreateReferenceAndRecordEdits
         kBeforeCreateReferenceAndRecordEdits
         kAfterCreateReferenceAndRecordEdits

         kBeforeLoadReference
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReference
         kAfterLoadReferenceAndRecordEdits

        By default, edits to referenced objects will not be recorded during the execution
        of file I/O callbacks. A specific set of callbacks are provided that will enable
        the recording of reference edits during their execution as follows:
         kAfterSceneReadAndRecordEdits
         kBeforeCreateReferenceAndRecordEdits
         kAfterCreateReferenceAndRecordEdits
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReferenceAndRecordEdits

        The kExportStarted callback is sent after the kBeforeExport callback, once Maya
        has actually started to process the exported data. One important difference between
        the two callbacks is that the fileInfo command affects the exported scene when used
        in the kExportStarted callback, but affects the current scene in memory when used
        in the kBeforeExport callback.

         * message - the Message constant that will trigger the callback
         * function - callable which will be passed the clientData object
         * clientData - user data that will be passed to the callback function
        """
    def addCheckCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCheckCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message.
        The callback will have the ability to abort the current operation
        by returning False.

        Callbacks can be added to the following messages with this function:
         kBeforeNewCheck
         kBeforeImportCheck
         kBeforeOpenCheck
         kBeforeExportCheck
         kBeforeSaveCheck
         kBeforeCreateReferenceCheck
         kBeforeLoadReferenceCheck

         * message - the scene message that will trigger the callback
         * function - callable which will be passed the clientData object,
           return False to abort the current operation.
         * clientData - user data that will be passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addCheckFileCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCheckFileCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message. This
        callback has the option to abort the current operation by returning
        False. The file parameter stores the target file for the current
        file IO operation, by modifying this file parameter the target file
        will be changed as well.

        Callbacks can be added to the following messages with this function:
         kBeforeImportCheck
         kBeforeOpenCheck
         kBeforeExportCheck
         kBeforeCreateReferenceCheck
         kBeforeLoadReferenceCheck

         * message - the scene message that will trigger the callback
         * function - callable which will be passed a MFileObject indicating the
           file object that will be acted on by the current file IO operation, any
           modifications to it will be passed back to Maya and change the file being
           acted on, and the clientData object.
           return False to abort the current operation.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addCheckReferenceCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addCheckReferenceCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message.
        The callback will have the ability to abort the current operation
        by returning False.

        Callbacks can be added to the following Message constant with this function:
         BeforeLoadReferenceCheck

         * message - the scene Message constant that will trigger the callback
         * function - callable which will be passed a MObject indicating the
           reference node, a MFileObject indicating the resolved file path of the
           referenced file, and the clientData object
           return False to abort the current operation
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addConnectionFailedCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addConnectionFailedCallback(function, clientData=None) -> id

        This method registers a callback that is called when a connection was
        unable to be made.
        Currently, the callback is only triggered during the reading of files (.ma or .mb)
        or of edits files (.editMA or .editMB files created by Maya's offline file support).
        The most common reasons why a connection would fail are:
        - inability to find the specified node or attribute names, or
        - a conflicting existing connection

         * function - callable which will be passed a MPlug indicating the
           source plug of the connection (or None if it could not be found),
           a MPlug indicating destination plug of the connection (or None if
           it could not be found), a string containing the name used to look up
           the source plug, a string containing the name used to look up the
           destination plug and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addReferenceCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addReferenceCallback(message, function, clientData=None) -> id

        This function adds a new callback for the specified scene message.

        Callbacks can be added to the following messages with this function:
         kBeforeRemoveReference
         kBeforeImportReference
         kBeforeUnloadReference
         kAfterUnloadReference
         kBeforeLoadReference
         kAfterLoadReference
         kAfterCreateReference
         kAfterCreateReferenceAndRecordEdits
         kBeforeLoadReferenceAndRecordEdits
         kAfterLoadReferenceAndRecordEdits

         * message - the scene Message constant that will trigger the callback
         * function - callable which will be passed a MObject indicating the
           reference node, a MFileObject indicating he resolved file path of the
           referenced file and the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def addStringArrayCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addStringArrayCallback(message, function, clientData=None) -> id

        Adds a new callback which takes a string array argument, in addition to
        the usual clientData.

        The Message constants which can be used with this method and the contents
        of the string array passed to their callbacks are as follows:
         kBeforePluginLoad - path to plug-in file
         kAfterPluginLoad - path to plug-in file, name of plug-in
         kBeforePluginUnload - name of plug-in
         kAfterPluginUnload - name of plug-in, path to plug-in file

                To allow for future expansion callbacks should not rely on the number
        of array elements being exactly as given above. While there will not
        be fewer elements than given above, there may in future be more.

         * message - the scene Message constant that will trigger the callback
         * function - callable which will be passed a list of strings and the
           clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    kAfterCreateReference: int = ...
    kAfterCreateReferenceAndRecordEdits: int = ...
    kAfterExport: int = ...
    kAfterExportReference: int = ...
    kAfterFileRead: int = ...
    kAfterImport: int = ...
    kAfterImportReference: int = ...
    kAfterLoadReference: int = ...
    kAfterLoadReferenceAndRecordEdits: int = ...
    kAfterOpen: int = ...
    kAfterPluginLoad: int = ...
    kAfterPluginUnload: int = ...
    kAfterReference: int = ...
    kAfterRemoveReference: int = ...
    kAfterSave: int = ...
    kAfterSceneReadAndRecordEdits: int = ...
    kAfterSoftwareFrameRender: int = ...
    kAfterSoftwareRender: int = ...
    kAfterUnloadReference: int = ...
    kBeforeCreateReference: int = ...
    kBeforeCreateReferenceAndRecordEdits: int = ...
    kBeforeCreateReferenceCheck: int = ...
    kBeforeExport: int = ...
    kBeforeExportCheck: int = ...
    kBeforeExportReference: int = ...
    kBeforeFileRead: int = ...
    kBeforeImport: int = ...
    kBeforeImportCheck: int = ...
    kBeforeImportReference: int = ...
    kBeforeLoadReference: int = ...
    kBeforeLoadReferenceAndRecordEdits: int = ...
    kBeforeLoadReferenceCheck: int = ...
    kBeforeNewCheck: int = ...
    kBeforeOpen: int = ...
    kBeforeOpenCheck: int = ...
    kBeforePluginLoad: int = ...
    kBeforePluginUnload: int = ...
    kBeforeReference: int = ...
    kBeforeReferenceCheck: int = ...
    kBeforeRemoveReference: int = ...
    kBeforeSave: int = ...
    kBeforeSaveCheck: int = ...
    kBeforeSoftwareFrameRender: int = ...
    kBeforeSoftwareRender: int = ...
    kBeforeUnloadReference: int = ...
    kExportStarted: int = ...
    kLast: int = ...
    kMayaExiting: int = ...
    kMayaInitialized: int = ...
    kSoftwareRenderInterrupted: int = ...

class MSelectionList:
    def add(self: Self, *args: Any, **kwargs: Any) -> Any:
        """add(pattern, searchChildNamespaces=False) -> self
        add(item, mergeWithExisting=True) -> self


        The first version adds to the list any nodes, DAG paths, components
        or plugs which match the given the pattern string.

        The second version adds the specific item to the list, where the
        item can be a plug (MPlug), a node (MObject), a DAG path (MDagPath)
        or a component (tuple of (MDagPath, MObject) ).
        """
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Empties the selection list.
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(src) -> self

        Replaces the contents of the selection list with a copy of those from src (MSelectionList).
        """
    def getComponent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getComponent(index) -> (MDagPath, MObject)

        Returns the index'th item of the list as a component, represented by
        a tuple containing an MDagPath and an MObject. If the item is just a
        DAG path without a component then MObject.kNullObj will be returned
        in the second element of the tuple. Raises TypeError if the item is
        neither a DAG path nor a component. Raises IndexError if index is
        out of range.
        """
    def getDagPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDagPath(index) -> MDagPath

        Returns the DAG path associated with the index'th item of the list.
        Raises TypeError if the item is neither a DAG path nor a component.
        Raises IndexError if index is out of range.
        """
    def getDependNode(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDependNode(index) -> MObject

        Returns the node associated with the index'th item, whether it be a
        dependency node, DAG path, component or plug.
        Raises kFailure if there is no dependency node associated with the current item.
        Raises IndexError if index is out of range.
        """
    def getPlug(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPlug(index) -> MPluggetPlug(index, convertComponents) -> MPlug

        Returns the index'th item of the list as a plug. Raises TypeError if
        the item is not a plug. Raises IndexError if index is out of range.
        If convertComponents is True then components in the selection list that have a corresponding plug will return that instead.
        Note: This only works if the component selection can be converted into a single plug - single component or all components selected.
        """
    def getSelectionStrings(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionStrings(index=None) -> (string, string, ...)

        Returns a tuple containing the string representation of the
        specified item. For nodes, DAG paths, plugs and contiguous
        components the tuple will only contain a single string, but for non-
        contiguous components there will be a separate string for each
        distinct block of contiguous elements. If index is not specified
        then the string representations of all the items in the selection
        list are returned. Raises IndexError if index is out of bounds.
        """
    def hasItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasItem(item) -> bool

        Returns True if the given item is on the selection list. For a
        component this means that all of the elements of the component must
        be on the list. A component is passed as a tuple containing the
        MDagPath of the DAG node and an MObject containing the component.
        """
    def hasItemPartly(self: Self, *args: Any, **kwargs: Any) -> Any:
        """hasItemPartly(dagPath, component) -> bool

        Returns True if at least one of the component's elements is on the
        selection list. Raises TypeError if dagPath is invalid or component
        does not contain a component.
        """
    def intersect(self: Self, *args: Any, **kwargs: Any) -> Any:
        """intersect(other, expandToLeaves=False) -> self

        Modify this list to contain the intersection of itself and the given list.
        """
    def isEmpty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isEmpty() -> bool

        Returns True if the selection list is empty.
        """
    kMergeNormal: int = ...
    kRemoveFromList: int = ...
    kXORWithList: int = ...

    def length(self: Self, *args: Any, **kwargs: Any) -> Any:
        """length() -> int

        Returns the number of items on the selection list.
        """
    def merge(self: Self, *args: Any, **kwargs: Any) -> Any:
        """merge(other, strategy=kMergeNormal) -> self
        merge(dagPath, component, strategy=kMergeNormal) -> self

        The first version merges the items from another selection list in
        with those already on the list, using the given strategy.

        The second version merges the specified component with those already
        on the list.
        """
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """remove(index) -> self

        Removes the index'th item from the list. Raises IndexError if the
        index is out of range.
        """
    def replace(self: Self, *args: Any, **kwargs: Any) -> Any:
        """replace(index, newItem) -> self

        Replaces the index'th item on the list with a new item. A component
        is passed as a tuple containing the MDagPath of the DAG node and an
        MObject containing the component. Raises IndexError if the index is
        out of range.
        """
    def toggle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """toggle(dagPath, component) -> self

        Removes from the list those elements of the given component which
        are already on it and adds those which are not.
        """

class MSelectionMask:
    def addMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addMask(selType) -> self

        Add the specified selection type to this mask.

        * selType (int) - the selection type to add.

        Valid selection types:
          kSelectHandles
          kSelectLocalAxis
          kSelectIkHandles
          kSelectIkEndEffectors
          kSelectJoints
          kSelectLights
          kSelectCameras
          kSelectLattices
          kSelectClusters
          kSelectSculpts
          kSelectNurbsCurves
          kSelectNurbsSurfaces
          kSelectMeshes
          kSelectSubdiv
          kSelectSketchPlanes
          kSelectParticleShapes
          kSelectEmitters
          kSelectFields
          kSelectSprings
          kSelectRigidBodies
          kSelectRigidConstraints
          kSelectCollisionModels
          kSelectXYZLocators
          kSelectOrientationLocators
          kSelectUVLocators
          kSelectTextures
          kSelectCurves
          kSelectSurfaces
          kSelectLocators
          kSelectObjectsMask
          kSelectCVs
          kSelectHulls
          kSelectEditPoints
          kSelectMeshVerts
          kSelectMeshEdges
          kSelectMeshFreeEdges
          kSelectMeshFaces
          kSelectSubdivMeshPoints
          kSelectSubdivMeshEdges
          kSelectSubdivMeshFaces
          kSelectMeshUVs
          kSelectVertices
          kSelectEdges
          kSelectFacets
          kSelectMeshLines
          kSelectMeshComponents
          kSelectCurveParmPoints
          kSelectCurveKnots
          kSelectSurfaceParmPoints
          kSelectSurfaceKnots
          kSelectSurfaceRange
          kSelectSurfaceEdge
          kSelectIsoparms
          kSelectCurvesOnSurfaces
          kSelectPPStrokes
          kSelectLatticePoints
          kSelectParticles
          kSelectJointPivots
          kSelectScalePivots
          kSelectRotatePivots
          kSelectPivots
          kSelectComponentsMask
          kSelectAnimCurves
          kSelectAnimKeyframes
          kSelectAnimInTangents
          kSelectAnimOutTangents
          kSelectAnimMask
          kSelectAnimAny
          kSelectTemplates
          kSelectManipulators
          kSelectGuideLines
          kSelectPointsForGravity
          kSelectPointsOnCurvesForGravity
          kSelectPointsOnSurfacesForGravity
          kSelectObjectGroups
          kSelectSubdivMeshMaps
          kSelectFluids
          kSelectHairSystems
          kSelectFollicles
          kSelectNCloths
          kSelectNRigids
          kSelectDynamicConstraints
          kSelectNParticles
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source selection mask.

        * source (MSelectionMask) - The source selection mask to copy from
        """
    def deregisterSelectionType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterSelectionType(selTypeName) -> bool

        Unregisters a previously registered selection type.

        * selTypeName (string) - Name of the selection type.
        """
    def getSelectionTypePriority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionTypePriority(selTypeName) -> int

        Gets the selection priority corresponding to a given selection type.

        * selTypeName (string) - Name of the selection type.
        """
    def intersects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """intersects(mask) -> bool
        intersects(selType) -> bool

        Returns True if the specified selection mask or selection type is contained within this selection mask.

        * mask (MSelectionMask) - the selection mask to test.
        * selType (int) - the selection type to test.  See addMask() for a list of valid selection masks.
        """
    kSelectAnimAny: int = ...
    kSelectAnimCurves: int = ...
    kSelectAnimInTangents: int = ...
    kSelectAnimKeyframes: int = ...
    kSelectAnimMask: int = ...
    kSelectAnimOutTangents: int = ...
    kSelectCVs: int = ...
    kSelectCameras: int = ...
    kSelectClusters: int = ...
    kSelectCollisionModels: int = ...
    kSelectComponentsMask: int = ...
    kSelectCurveKnots: int = ...
    kSelectCurveParmPoints: int = ...
    kSelectCurves: int = ...
    kSelectCurvesOnSurfaces: int = ...
    kSelectDynamicConstraints: int = ...
    kSelectEdges: int = ...
    kSelectEditPoints: int = ...
    kSelectEmitters: int = ...
    kSelectFacets: int = ...
    kSelectFields: int = ...
    kSelectFluids: int = ...
    kSelectFollicles: int = ...
    kSelectGuideLines: int = ...
    kSelectHairSystems: int = ...
    kSelectHandles: int = ...
    kSelectHulls: int = ...
    kSelectIkEndEffectors: int = ...
    kSelectIkHandles: int = ...
    kSelectIsoparms: int = ...
    kSelectJointPivots: int = ...
    kSelectJoints: int = ...
    kSelectLatticePoints: int = ...
    kSelectLattices: int = ...
    kSelectLights: int = ...
    kSelectLocalAxis: int = ...
    kSelectLocators: int = ...
    kSelectManipulators: int = ...
    kSelectMeshComponents: int = ...
    kSelectMeshEdges: int = ...
    kSelectMeshFaces: int = ...
    kSelectMeshFreeEdges: int = ...
    kSelectMeshLines: int = ...
    kSelectMeshUVs: int = ...
    kSelectMeshVerts: int = ...
    kSelectMeshes: int = ...
    kSelectNCloths: int = ...
    kSelectNParticles: int = ...
    kSelectNRigids: int = ...
    kSelectNurbsCurves: int = ...
    kSelectNurbsSurfaces: int = ...
    kSelectObjectGroups: int = ...
    kSelectObjectsMask: int = ...
    kSelectOrientationLocators: int = ...
    kSelectPPStrokes: int = ...
    kSelectParticleShapes: int = ...
    kSelectParticles: int = ...
    kSelectPivots: int = ...
    kSelectPointsForGravity: int = ...
    kSelectPointsOnCurvesForGravity: int = ...
    kSelectPointsOnSurfacesForGravity: int = ...
    kSelectRigidBodies: int = ...
    kSelectRigidConstraints: int = ...
    kSelectRotatePivots: int = ...
    kSelectScalePivots: int = ...
    kSelectSculpts: int = ...
    kSelectSelectHandles: int = ...
    kSelectSketchPlanes: int = ...
    kSelectSprings: int = ...
    kSelectSubdiv: int = ...
    kSelectSubdivMeshEdges: int = ...
    kSelectSubdivMeshFaces: int = ...
    kSelectSubdivMeshMaps: int = ...
    kSelectSubdivMeshPoints: int = ...
    kSelectSurfaceEdge: int = ...
    kSelectSurfaceKnots: int = ...
    kSelectSurfaceParmPoints: int = ...
    kSelectSurfaceRange: int = ...
    kSelectSurfaces: int = ...
    kSelectTemplates: int = ...
    kSelectTextures: int = ...
    kSelectUVLocators: int = ...
    kSelectVertices: int = ...
    kSelectXYZLocators: int = ...

    def registerSelectionType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerSelectionType(selTypeName, priority=0) -> bool

        Registers a new selection type. It is perfectly legal for 2 plug-ins to register the same selection type.
        Currently we use the registration count. The selection type is deleted only when deregisterSelectionType() as been called the same number of times as this function - registerSelectionType().

        When registerSelectionType() is invoked and the selection type already exists, we neither enable it nor change its priority, just add its registration count by 1.
        The reason is the user might has modified these values after loading the plug-in that has register the selection type the first time.

        * selTypeName (string) - Name of the selection type.
        * priority (int) - Priority of the selection type.
        """
    def setMask(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setMask(mask) -> self
        setMask(selType) -> self

        Sets the selection mask to the specified selection mask or selection type.

        * mask (MSelectionMask) - the selection mask to be set.
        * selType (int) - the selection type to be set.  See addMask() for a list of valid selection masks.
        """

class MSpace:
    kInvalid: int = ...
    kLast: int = ...
    kObject: int = ...
    kPostTransform: int = ...
    kPreTransform: int = ...
    kTransform: int = ...
    kWorld: int = ...

class MSyntax:
    def addArg(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a command argument."""
    def addFlag(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a flag and its arguments."""
    @property
    def enableEdit(*args: Any, **kwargs: Any) -> Any:
        """Enable support for the -edit flag."""
    @enableEdit.setter
    def enableEdit(*args: Any, **kwargs: Any) -> Any:
        """Enable support for the -edit flag."""
    @property
    def enableQuery(*args: Any, **kwargs: Any) -> Any:
        """Enable support for the -query flag."""
    @enableQuery.setter
    def enableQuery(*args: Any, **kwargs: Any) -> Any:
        """Enable support for the -query flag."""
    kAngle: int = ...
    kBoolean: int = ...
    kDistance: int = ...
    kDouble: int = ...
    kInvalidArgType: int = ...
    kInvalidObjectFormat: int = ...
    kLastArgType: int = ...
    kLastObjectFormat: int = ...
    kLong: int = ...
    kNoArg: int = ...
    kNone: int = ...
    kSelectionItem: int = ...
    kSelectionList: int = ...
    kString: int = ...
    kStringObjects: int = ...
    kTime: int = ...
    kUnsigned: int = ...

    def makeFlagMultiUse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set whether a flag may be used multiple times on the command line."""
    def makeFlagQueryWithFullArgs(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set whether a flag requires its args when queried."""
    def maxObjects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the maximum number of objects which can be passed to the command."""
    def minObjects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the minimum number of objects which can be passed to the command."""
    def setMaxObjects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the maximum number of objects which can be passed to the command."""
    def setMinObjects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the minimum number of objects which can be passed to the command."""
    def setObjectType(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Set the type and number of objects to be passed to the command."""
    def useSelectionAsDefault(self: Self, *args: Any, **kwargs: Any) -> Any:
        """If set to True then when no objects are provided on the command-line Maya will pass the current selection instead."""

class MTime:
    def asUnits(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the time value, converted to the specified units."""
    k100FPS: int = ...
    k10FPS: int = ...
    k1200FPS: int = ...
    k120FPS: int = ...
    k125FPS: int = ...
    k12FPS: int = ...
    k1500FPS: int = ...
    k150FPS: int = ...
    k15FPS: int = ...
    k16FPS: int = ...
    k2000FPS: int = ...
    k200FPS: int = ...
    k20FPS: int = ...
    k23_976FPS: int = ...
    k240FPS: int = ...
    k24FPS: int = ...
    k250FPS: int = ...
    k25FPS: int = ...
    k29_97DF: int = ...
    k29_97FPS: int = ...
    k2FPS: int = ...
    k3000FPS: int = ...
    k300FPS: int = ...
    k30FPS: int = ...
    k375FPS: int = ...
    k3FPS: int = ...
    k400FPS: int = ...
    k40FPS: int = ...
    k44100FPS: int = ...
    k47_952FPS: int = ...
    k48000FPS: int = ...
    k48FPS: int = ...
    k4FPS: int = ...
    k500FPS: int = ...
    k50FPS: int = ...
    k59_94FPS: int = ...
    k5FPS: int = ...
    k6000FPS: int = ...
    k600FPS: int = ...
    k60FPS: int = ...
    k6FPS: int = ...
    k750FPS: int = ...
    k75FPS: int = ...
    k80FPS: int = ...
    k8FPS: int = ...
    k90FPS: int = ...
    kFilm: int = ...
    kGames: int = ...
    kHours: int = ...
    kInvalid: int = ...
    kLast: int = ...
    kMilliseconds: int = ...
    kMinutes: int = ...
    kNTSCField: int = ...
    kNTSCFrame: int = ...
    kPALField: int = ...
    kPALFrame: int = ...
    kSeconds: int = ...
    kShowScan: int = ...
    kUserDef: int = ...

    def setUIUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Change the units used to display time in Maya's UI."""
    def ticksPerSecond(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of ticks per second, the smallest unit of time available."""
    def uiUnit(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Return the units used to display time in Maya's UI."""
    @property
    def unit(*args: Any, **kwargs: Any) -> Any:
        """Time units currently in use."""
    @unit.setter
    def unit(*args: Any, **kwargs: Any) -> Any:
        """Time units currently in use."""
    @property
    def value(*args: Any, **kwargs: Any) -> Any:
        """Value of the time in the current units."""
    @value.setter
    def value(*args: Any, **kwargs: Any) -> Any:
        """Value of the time in the current units."""

class MTimeArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MTimeRange:
    def contains(self: Self, *args: Any, **kwargs: Any) -> Any:
        """contains(MTime) -> boolcontains(MTime, MTime) -> bool

        Checks if the given time point or interval is contained in this time range.
        """
    def empty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """empty() -> bool

        Checks if this time range is an empty set
        """
    def intersects(self: Self, *args: Any, **kwargs: Any) -> Any:
        """intersects(MTime, MTime) -> bool

        Checks if the given interval intersects with this time range.
        """

class MTimerMessage(MMessage):
    def addTimerCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addTimerCallback(period, function, clientData=None) -> id

        This method registers a callback which is called repeatedly with a
        specified period of time between calls. Each time the timer fires the
        callback will be placed on the idle queue for execution in the next
        idle cycle. If the timer fires again, before the previous invocation
        has completed execution, the new firing will be skipped.

        If the execution time of the callback exceeds half of its period then
        the next timeout will be skipped to give Maya time to process other tasks.

        The maximum resolution for this callback is about 1ms.  The response
        is, however, not guaranteed because while multitasking, the OS may
        delay for an unspecified length of time before returning control to
        Maya.

         * period (float) - the period at which the callback will be
        executed (Measured in seconds)
         * function - callable which will be passed a float indicating
           the elapsed time since this function was last called, a float
           indicating the execution time of this function the last time
           it was called, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

class MTransformationMatrix:
    def asMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Interpolates between the identity transformation and that currently in the object, returning the result as an MMatrix."""
    def asMatrixInverse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the inverse of the matrix representing the transformation."""
    def asRotateMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix which takes points from object space to the space immediately following the scale/shear/rotation transformations."""
    def asScaleMatrix(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix which takes points from object space to the space immediately following scale and shear transformations."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if this transformation's matrix is within tolerance of another's matrix."""
    kIdentity: MTransformationMatrix = ...
    kInvalid: int = ...
    kLast: int = ...
    kTolerance: float = ...
    kXYZ: int = ...
    kXZY: int = ...
    kYXZ: int = ...
    kYZX: int = ...
    kZXY: int = ...
    kZYX: int = ...

    def reorderRotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Reorders the transformation's rotate component to give the same overall rotation but using a new order or rotations."""
    def rotateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transformation's rotation component."""
    def rotateByComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transformation's rotation component."""
    def rotatePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's rotate pivot component."""
    def rotatePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's rotate pivot translation component."""
    def rotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's rotation component as either an Euler rotation or a quaternion."""
    def rotationComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the four components of the transformation's rotate component."""
    def rotationOrder(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the order of rotations when the transformation's rotate component is expressed as an euler rotation."""
    def rotationOrientation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a quaternion which orients the local rotation space."""
    def scale(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transformation's scale components."""
    def scaleBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transformation's scale components by the three floats in the provided sequence."""
    def scalePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's scale pivot component."""
    def scalePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's scale pivot translation component."""
    def setRotatePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate pivot component."""
    def setRotatePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate pivot translation component."""
    def setRotation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotation component."""
    def setRotationComponents(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate component from the four values in the provided sequence."""
    def setRotationOrientation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets a quaternion which orients the local rotation space."""
    def setScale(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's scale components to the three floats in the provided sequence."""
    def setScalePivot(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's scale pivot component."""
    def setScalePivotTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's scale pivot translation component."""
    def setShear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's shear component."""
    def setToRotationAxis(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate component to be a given axis vector and angle in radians."""
    def setTranslation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's translation component."""
    def shear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transformation's shear components."""
    def shearBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transformation's shear components by the three floats in the provided sequence."""
    def translateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Adds a vector to the transformation's translation component."""
    def translation(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's translation component as a vector."""

class MTypeId:
    def id(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type id as a long."""

class MURI:
    def addQueryItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addQueryItem(key, value) -> self

        Add a key/value pair to the query string of the URI.
        """
    def asString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asString() -> string

        Returns the string representation of the URI.
        """
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clears the contents of the MURI object.
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy method. Assigns the value of one MURI to another.

        * source (MURI) - Existing MURI object to copy.
        """
    def getAllQueryItemKeys(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAllQueryItemKeys() -> array

        Returns an array containing the keys from all query string pairs.
        """
    def getAllQueryItemValues(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAllQueryItemValues(key) -> array

        Returns an array containing the values from all query string pairs which have a given key.
        """
    def getAuthority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getAuthority() -> string

        Returns the authority component of the URI.
        """
    def getDirectory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getDirectory() -> string

        Returns just the file directory portion of the URI, without the file name.
        """
    def getFileName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFileName(bool includeExtension=True) -> string

        Returns just the file name portion of the URI, with or without the extension.
        """
    def getFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getFragment() -> string

        Returns the fragment component of the URI.
        """
    def getHost(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getHost() -> string

        Returns the host component of the URI.
        """
    def getPassword(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPassword() -> string

        Returns the password component of the URI.
        """
    def getPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPath() -> string

        Returns the path component of the URI.
        """
    def getPort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getPort() -> int

        Returns the port component of the URI, or -1 if the port is not defined.
        """
    def getQueryItemValue(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getQueryItemValue(key) -> string

        Returns the value from the first query string pair in the URI which has a given key.
        """
    def getQueryPairDelimiter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getQueryPairDelimiter() -> string

        Returns the character used to delimit between key-value pairs in the query string of the URI.
        """
    def getQueryValueDelimiter(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getQueryValueDelimiter() -> string

        Returns the character used to delimit keys and values in the query string of the URI.
        """
    def getScheme(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getScheme() -> string

        Returns the scheme of the URI.
        """
    def getUserInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUserInfo() -> string

        Returns the user info component of the URI.
        """
    def getUserName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """getUserName() -> string

        Returns the user name component of the URI.
        """
    def isEmpty(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isEmpty() -> bool

        Determines if the URI does not contain any data.
        """
    def isValid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isValid() -> bool

        Determines if the URI is valid.
        """
    def isValidURI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isValidURI(uri) -> bool

        Determines if a string value represents a valid URI.
        """
    def removeAllQueryItems(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeAllQueryItems(int) -> self

        Removes all query string pairs having a given key from the URI.
        """
    def removeQueryItem(self: Self, *args: Any, **kwargs: Any) -> Any:
        """removeQueryItem(int) -> self

        Removes the first query string pair with a given key from the URI.
        """
    def setAuthority(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setAuthority(string) -> self

        Set the authority portion of the URI.
        """
    def setDirectory(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDirectory(string) -> self

        Sets just the directory portion of the URI (i.e. not including the filename).
        """
    def setFileName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFileName(string) -> self

        Sets just the filename portion of the URI (i.e. not including the directory).
        """
    def setFragment(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setFragment(string) -> self

        Sets the fragment component of the URI.
        """
    def setHost(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setHost(string) -> self

        Set the host component of the URI.
        """
    def setPassword(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPassword(string) -> self

        Sets the password part of the user info component.
        """
    def setPath(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPath(string) -> self

        Sets the path component of the URI.
        """
    def setPort(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setPort(int) -> self

        Set the port component of the URI.
        """
    def setQueryDelimiters(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setQueryDelimiters(valueDelimiter, pairDelimiter) -> self

        Sets the delimiter characters used in the query string of the URI.
        """
    def setScheme(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setScheme(string) -> self

        Sets the scheme component of the URI.
        """
    def setURI(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setURI(uri) -> self

        Initialize the MURI from a string value.
        """
    def setUserInfo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUserInfo(string) -> self

        Decomposes the userInfo string to fill out the userInfo-related component values.
        """
    def setUserName(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setUserName(string) -> self

        Sets the user name part of the user info component.
        """

class MUint64Array:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MUintArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MUserData:
    def deleteAfterUse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deleteAfterUse() -> bool

        Returns whether or not this user data should be deleted immediately after use instead of being
        maintained until the internal owning object is deleted.

            DEPRECATED in 2022, deleteAfterUse is deprecated.
        """
    def setDeleteAfterUse(self: Self, *args: Any, **kwargs: Any) -> Any:
        """setDeleteAfterUse(bool) -> self

        Sets whether or not this user data should be deleted immediately after use instead of being
        maintained until the internal owning object is deleted.

        Setting this to false may allow the data to be reused in some situations.
        For example, if the MUserData returned by an MPxDrawOverride instance's prepareForDraw() method has
        its delete-after-use set to false, then Maya will retain the data between draws of that object,
        passing it back to the instance for reuse on subsequent draws.

            DEPRECATED in 2022, deleteAfterUse is deprecated.
        """

class MUserEventMessage(MMessage):
    def addUserEventCallback(self: Self, *args: Any, **kwargs: Any) -> Any:
        """addUserEventCallback(eventName, function, clientData=None) -> id

        This method registers a callback for user-defined messages.

        The parameter clientData will be passed to callbacks registered for this
        event whenever the event is triggered.  To override the data that is passed
        to the callback whenever the event is posted, you can supply a clientData
        pointer to postUserEvent()..

         * eventName (string) - the event name to register the callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """
    def deregisterUserEvent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """deregisterUserEvent(eventName)

        Removes the event type with the given event name.  If callbacks have been
        registered with this event type, they will become invalid after a
        successful call to this method.

         * eventName (string) - the name of the new event to deregister.
        """
    def isUserEvent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """isUserEvent(eventName) -> bool

        Checks if an event type exists with the given event name.

         * eventName (string) - the name of the new event to check.
        """
    def postUserEvent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """postUserEvent(eventName, clientData=None)

        Notifies all callbacks attached to the given event type of the occurence
        of the event.

        If clientData is specified, this data will be passed to all callbacks that
        receive the event.  If clientData is None (the default), the clientData
        registered with addUserEventCallback will be passed to the callbacks.


         * eventName (string) - the name of the new event.
         * clientData - User defined data.
        """
    def registerUserEvent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """registerUserEvent(eventName)

        Adds a new event type with the given string identifier.  The string
        identifier can then be used in all other MUserEventMessage methods to operate
        on the new event type.

         * eventName (string) - the name of the new event to register.  Any
           non-empty string may be used as an event name.
        """

class MUuid:
    def asString(self: Self, *args: Any, **kwargs: Any) -> Any:
        """asString() -> string

        Return the UUID as a string.
        """
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy method. Assigns the value of one MUuid to another.

        * source (MUuid) - Existing MUuid object to copy.
        """
    def generate(self: Self, *args: Any, **kwargs: Any) -> Any:
        """generate() -> self

        Generate a new UUID.
        """
    def valid(self: Self, *args: Any, **kwargs: Any) -> Any:
        """valid() -> bool

        Return whether the UUID is valid.
        """

class MVector:
    def angle(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angle, in radians, between this vector and another."""
    def isEquivalent(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within a given tolerance of being equal."""
    def isParallel(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within the given tolerance of being parallel."""
    kOneVector: MVector = ...
    kTolerance: float = ...
    kWaxis: int = ...
    kXaxis: int = ...
    kXaxisVector: MVector = ...
    kXnegAxisVector: MVector = ...
    kYaxis: int = ...
    kYaxisVector: MVector = ...
    kYnegAxisVector: MVector = ...
    kZaxis: int = ...
    kZaxisVector: MVector = ...
    kZeroVector: MVector = ...
    kZnegAxisVector: MVector = ...

    def length(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the magnitude of this vector."""
    def normal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector containing the normalized version of this one."""
    def normalize(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Normalizes this vector in-place and returns a new reference to it."""
    def rotateBy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the vector resulting from rotating this one by the given amount."""
    def rotateTo(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns the quaternion which will rotate this vector into another."""
    def transformAsNormal(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix's inverse and then normalizing the result."""
    @property
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @x.setter
    def x(*args: Any, **kwargs: Any) -> Any:
        """X coordinate"""
    @property
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @y.setter
    def y(*args: Any, **kwargs: Any) -> Any:
        """Y coordinate"""
    @property
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""
    @z.setter
    def z(*args: Any, **kwargs: Any) -> Any:
        """Z coordinate"""

class MVectorArray:
    def append(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Add a value to the end of the array."""
    def clear(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove all elements from the array."""
    def copy(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Replace the array contents with that of another or of a compatible Python sequence."""
    def insert(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Insert a new value into the array at the given index."""
    def remove(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Remove an element from the array."""
    def setLength(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Grow or shrink the array to contain a specific number of elements."""
    @property
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""
    @sizeIncrement.setter
    def sizeIncrement(*args: Any, **kwargs: Any) -> Any:
        """Number of elements by which to grow the array when necessary."""

class MWeight:
    @property
    def influence(*args: Any, **kwargs: Any) -> Any:
        """Controls how much of a given operation is applied to the entity
        associated with this weight structure. A value of 1 means the full
         effect should be applied. A value of 0 means the operation should
        not affect the entity at all.
        """
    @influence.setter
    def influence(*args: Any, **kwargs: Any) -> Any:
        """Controls how much of a given operation is applied to the entity
        associated with this weight structure. A value of 1 means the full
         effect should be applied. A value of 0 means the operation should
        not affect the entity at all.
        """
    @property
    def seam(*args: Any, **kwargs: Any) -> Any:
        """Indicates how close the entity associated with this weight is to the
        plane of reflection (the seam), and hence, how strongly it should be
        associated with the seam. A value of 0 means the entity is free to move
        independent of the seam. A value of 1 means the entity is full on the
        seam, and should ideally maintain it's distance relative to the plane of
        symmetry. This value is only relevant when symmetry is enabled.
        """
    @seam.setter
    def seam(*args: Any, **kwargs: Any) -> Any:
        """Indicates how close the entity associated with this weight is to the
        plane of reflection (the seam), and hence, how strongly it should be
        associated with the seam. A value of 0 means the entity is free to move
        independent of the seam. A value of 1 means the entity is full on the
        seam, and should ideally maintain it's distance relative to the plane of
        symmetry. This value is only relevant when symmetry is enabled.
        """
