from __future__ import annotations

from typing import *

Unknown = Any

class MAngle(object):
    """Manipulate angular data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def asAngMinutes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to minutes of arc."""

    def asAngSeconds(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to seconds of arc."""

    def asDegrees(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to degrees."""

    def asRadians(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to radians."""

    def asUnits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular value, converted to the specified units."""

    def internalToUI(self, *args: Any, **kwargs: Any) -> Any:
        """Converts a value from Maya's internal units to the units used in the UI."""

    def internalUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angular unit used internally by Maya."""

    kAngMinutes: int = 3
    kAngSeconds: int = 4
    kDegrees: int = 2
    kInvalid: int = 0
    kLast: int = 5
    kRadians: int = 1
    def setUIUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the angular unit used in Maya's UI."""

    def uiToInternal(self, *args: Any, **kwargs: Any) -> Any:
        """Converts a value from the units used in the UI to Maya's internal units."""

    def uiUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the units used to display angles in Maya's UI."""

    unit: getset_descriptor = <attribute 'unit' of 'OpenMaya.MAngle' objects>
    value: getset_descriptor = <attribute 'value' of 'OpenMaya.MAngle' objects>

class MArgDatabase(MArgParser):
    """Command argument list parser which extends MArgParser with the
    ability to return arguments and objects as MSelectionLists
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def commandArgumentMSelectionList(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMSelectionList(argIndex) -> MSelectionList

        Returns the specified command argument as an MSelectionList.
        """

    def flagArgumentMSelectionList(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMSelectionList(flagName, argIndex) -> MSelectionList

        Returns the specified argument of the specified single-use flag as
        an MSelectionList.
        """

    def getObjectList(self, *args: Any, **kwargs: Any) -> Any:
        """getObjectList() -> MSelectionList

        If the command's MSyntax has set the object format to kSelectionList
        then this method will return the objects passed to the command as an
        MSelectionList. If any other object format is set then an empty
        selection list will be returned.
        """


class MArgList(object):
    """Argument list for passing to commands."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addArg(self, *args: Any, **kwargs: Any) -> Any:
        """addArg(arg) -> self , 'arg' is a numeric value, MAngle, MDistance,
        MTime, MPoint or        MVector.

        Add an argument to the end of the arg list.
        """

    def asAngle(self, *args: Any, **kwargs: Any) -> Any:
        """asAngle(index) -> MAngle

        Return an argument as an MAngle.
        """

    def asBool(self, *args: Any, **kwargs: Any) -> Any:
        """asBool(index) -> bool

        Return an argument as a boolean.
        """

    def asDistance(self, *args: Any, **kwargs: Any) -> Any:
        """asDistance(index) -> MDistance

        Return an argument as an MDistance.
        """

    def asDouble(self, *args: Any, **kwargs: Any) -> Any:
        """asDouble(index) -> float

        Alias for asFloat().
        """

    def asDoubleArray(self, *args: Any, **kwargs: Any) -> Any:
        """asDoubleArray(index) -> MDoubleArray

        Return a sequence of arguments as an MDoubleArray.
        """

    def asFloat(self, *args: Any, **kwargs: Any) -> Any:
        """asFloat(index) -> float

        Return an argument as a float.
        """

    def asInt(self, *args: Any, **kwargs: Any) -> Any:
        """asInt(index) -> int

        Return an argument as an integer.
        """

    def asIntArray(self, *args: Any, **kwargs: Any) -> Any:
        """asIntArray(index) -> MIntArray

        Return a sequence of arguments as an MIntArray.
        """

    def asMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """asMatrix(index) -> MMatrix

        Return a sequence of arguments as an MMatrix.
        """

    def asPoint(self, *args: Any, **kwargs: Any) -> Any:
        """asPoint(index) -> MPoint

        Return a sequence of arguments as an MPoint.
        """

    def asString(self, *args: Any, **kwargs: Any) -> Any:
        """asString(index) -> string

        Return an argument as a string.
        """

    def asStringArray(self, *args: Any, **kwargs: Any) -> Any:
        """asStringArray(index) -> list of strings

        Return a sequence of arguments as a list of strings.
        """

    def asTime(self, *args: Any, **kwargs: Any) -> Any:
        """asTime(index) -> MTime

        Return an argument as an MTime.
        """

    def asVector(self, *args: Any, **kwargs: Any) -> Any:
        """asVector(index) -> MVector

        Return a sequence of arguments as an MVector.
        """

    def flagIndex(self, *args: Any, **kwargs: Any) -> Any:
        """flagIndex(shortFlag, longFlag=None) -> int

        Return index of first occurrence of specified flag.
        """

    kInvalidArgIndex: int = -1
    def lastArgUsed(self, *args: Any, **kwargs: Any) -> Any:
        """lastArgUsed() -> int

        Return index of last argument used by the most recent as*() method.
        """


class MArgParser(object):
    """Command argument list parser."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def commandArgumentBool(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentBool(argIndex) -> bool

        Returns the specified command argument as a bool.
        """

    def commandArgumentDouble(self, *args: Any, **kwargs: Any) -> Any:
        """Alias for commandArgumentFloat()."""

    def commandArgumentFloat(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentFloat(argIndex) -> float

        Returns the specified command argument as a float.
        """

    def commandArgumentInt(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentInt(argIndex) -> int

        Returns the specified command argument as an int.
        """

    def commandArgumentMAngle(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMAngle(argIndex) -> MAngle

        Returns the specified command argument as an MAngle.
        """

    def commandArgumentMDistance(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMDistance(argIndex) -> MDistance

        Returns the specified command argument as an MDistance.
        """

    def commandArgumentMTime(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentMTime(argIndex) -> MTime

        Returns the specified command argument as an MTime.
        """

    def commandArgumentString(self, *args: Any, **kwargs: Any) -> Any:
        """commandArgumentString(argIndex) -> unicode string

        Returns the specified command argument as a string.
        """

    def flagArgumentBool(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentBool(flagName, argIndex) -> bool

        Returns the specified argument of the specified single-use flag as
        a bool.
        """

    def flagArgumentDouble(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentDouble(flagName, argIndex) -> float

        Alias for flagArgumentFloat().
        """

    def flagArgumentFloat(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentFloat(flagName, argIndex) -> float

        Returns the specified argument of the specified single-use flag as
        a float.
        """

    def flagArgumentInt(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentInt(flagName, argIndex) -> int

        Returns the specified argument of the specified single-use flag as
        an int.
        """

    def flagArgumentMAngle(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMAngle(flagName, argIndex) -> MAngle

        Returns the specified argument of the specified single-use flag as
        an MAngle.
        """

    def flagArgumentMDistance(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMDistance(flagName, argIndex) -> MDistance

        Returns the specified argument of the specified single-use flag as
        an MDistance.
        """

    def flagArgumentMTime(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentMTime(flagName, argIndex) -> MTime

        Returns the specified argument of the specified single-use flag as
        an MTime.
        """

    def flagArgumentString(self, *args: Any, **kwargs: Any) -> Any:
        """flagArgumentString(flagName, argIndex) -> string

        Returns the specified argument of the specified single-use flag as
        a string.
        """

    def getFlagArgumentList(self, *args: Any, **kwargs: Any) -> Any:
        """getFlagArgumentList(flagName, occurrence) -> MArgList

        Returns the arguments for the specified occurrence of the given
        multi-use flag as an MArgList. Raises RuntimeError if the flag has
        not been enabled for multi-use. Raises IndexError if occurrence is
        out of range.
        """

    def getFlagArgumentPosition(self, *args: Any, **kwargs: Any) -> Any:
        """getFlagArgumentPosition(flagName, occurrence) -> int

        Returns the position in the argument list of the specified occurrence
        of the given flag. Raises IndexError if occurrence is out of range.
        """

    def getObjectStrings(self, *args: Any, **kwargs: Any) -> Any:
        """getObjectStrings() -> tuple of unicode strings

        If the command's MSyntax has set the object format to kStringObjects
        then this method will return the objects passed to the command as a
        tuple of strings. If any other object format is set then an empty
        tuple will be returned.
        """

    isEdit: getset_descriptor = <attribute 'isEdit' of 'OpenMaya.MArgParser' objects>
    def isFlagSet(self, *args: Any, **kwargs: Any) -> Any:
        """isFlagSet(flagName) -> bool

        Returns True if the given flag appears on the command line.
        """

    isQuery: getset_descriptor = <attribute 'isQuery' of 'OpenMaya.MArgParser' objects>
    def numberOfFlagUses(self, *args: Any, **kwargs: Any) -> Any:
        """numberOfFlagUses(flagName) -> int

        Returns the number of times that the flag appears on the command
        line.
        """

    numberOfFlagsUsed: getset_descriptor = <attribute 'numberOfFlagsUsed' of 'OpenMaya.MArgParser' objects>

class MArrayDataBuilder(object):
    """Array builder for arrays in data blocks."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addElement(self, *args: Any, **kwargs: Any) -> Any:
        """addElement(index) -> MDataHandle

        Adds a new element to the array at the given index.

        * index (int) - the index at which we wish to add the new element

        Returns The handle for the new element
        """

    def addElementArray(self, *args: Any, **kwargs: Any) -> Any:
        """addElementArray(index) -> MArrayDataHandle

        Adds a new element to the array at the given index.  The added element is also an array.

        * index (int) - the index at which we wish to add the new element

        Returns The handle for the new array element
        """

    def addLast(self, *args: Any, **kwargs: Any) -> Any:
        """addLast() -> MDataHandle

        Adds a new element to the end of the array.  The index of the element will be the current highest index + 1.

        Returns The handle for the new element
        """

    def addLastArray(self, *args: Any, **kwargs: Any) -> Any:
        """addLastArray() -> MArrayDataHandle

        Adds a new element to the end of the array.  The added element is also an array.  The index of the element will the current highest index + 1.

        Returns The handle for the new array element
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source builder.

        * source (MArrayDataBuilder) - The source object to copy from
        """

    def growArray(self, *args: Any, **kwargs: Any) -> Any:
        """growArray(amount) -> self

        Grows the array storage by the given amount.

        * amount (int) - the amount to grow the array by
        """

    def removeElement(self, *args: Any, **kwargs: Any) -> Any:
        """removeElement(index) -> self

        Removes the specified element from the array

        * index (int) - the element of the array to remove
        """

    def setGrowSize(self, *args: Any, **kwargs: Any) -> Any:
        """setGrowSize(size) -> self

        Sets the grow size of the array.  As elements are added to the array, the builder will allocate memory in chunks.  This method tells the builder how many elements to allocate each time it grows the array.

        * size (int) - the number of elements to allocate when growing the array
        """


class MArrayDataHandle(object):
    """Data block handle for array data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def builder(self, *args: Any, **kwargs: Any) -> Any:
        """builder() -> MArrayDataBuilder

        Returns a builder for this handle's array so that it can be expanded.

        This method will raise an exception if the current array does not support array data builders. This can be changed in a node's initialize routine using the usesArrayDataBuilder attribute in MFnAttribute.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source array.

        * source (MArrayDataHandle) - The source object to copy from
        """

    def elementLogicalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """elementLogicalIndex() -> int

        Returns the index that we are currently at in the array.  It is possible for the index to be invalid, in which case the return status will report an error.  These may be sparse arrays so the element index returned will be a logical index.

        Raises an exception if there is no current element (e.g. if there are no elements).
        """

    def inputArrayValue(self, *args: Any, **kwargs: Any) -> Any:
        """inputArrayValue() -> MArrayDataHandle

        Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """

    def inputValue(self, *args: Any, **kwargs: Any) -> Any:
        """inputValue() -> MDataHandle

        Gets a handle into this data block for the current array element.  The data represented by the handle will be valid.  If the data is from an dirty connection, then the connection will be evaluated.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Specifies whether or not there are more elements to iterate over.
        """

    def jumpToLogicalElement(self, *args: Any, **kwargs: Any) -> Any:
        """jumpToLogicalElement(index) -> self

        Jump to a specific logical element in the array.
        Since the logical array is sparse its indices may not be consecutive and a binary search is used internally to find the element.
        Thus when iterating through the elements of the array it is much faster to do so using physical indices.

        * index (int) - the logical index to jump to
        """

    def jumpToPhysicalElement(self, *args: Any, **kwargs: Any) -> Any:
        """jumpToPhysicalElement(position) -> self

        Jump to a specific physical element in the array.
        Since physical elements are contiguous no search is required.

        * position (int) - the array position to jump to
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> bool

        Advance to the next element in the array.
        Return True if there was a next element and False if there wasn't.
        """

    def outputArrayValue(self, *args: Any, **kwargs: Any) -> Any:
        """outputArrayValue() -> MArrayDataHandle

        Gets a handle into this data block for the current array element.  This method should be used when the array elements are also arrays. The array's elements are not evaluated and may no longer be valid. Therefore, this handle should only be used for writing over the data.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """

    def outputValue(self, *args: Any, **kwargs: Any) -> Any:
        """outputValue() -> MDataHandle

        Gets a handle into this data block for the current array element. The element is not evaluated so its data may not be valid. Therefore, this handle should only be used for writing over the data.

        This method can also be used to retrieve handles to individual elements of  non-datablock array handles, such as those returned by MPlug.getValue() and MPlug.asMDataHandle().
        """

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """set(builder) -> self

        Sets the data for this array from the data in the builder object

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().

        * builder (MArrayDataBuilder) - the builder object
        """

    def setAllClean(self, *args: Any, **kwargs: Any) -> Any:
        """setAllClean() -> self

        Marks every element of the array attribute represented by the handle as clean.  This method should be used if a compute function is asked to compute a single element of a multi, but instead calculates all the elements.  Calling <i>setAllClean</i> in this situation will prevent further calls to the node's compute method for the other elements of the multi.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle()
        """

    def setClean(self, *args: Any, **kwargs: Any) -> Any:
        """setClean() -> self

        Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.

        Do not use with an MArrayDataHandle which was returned by MPlug.asMDataHandle().
        """


class MAttributeIndex(object):
    """The index information for an attribute specification."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source index.

        * source (MAttributeIndex) - The source index to copy from
        """

    def getLower(self, *args: Any, **kwargs: Any) -> Any:
        """getLower() -> int/float

        Returns the lower bound of the index.
        """

    def getUpper(self, *args: Any, **kwargs: Any) -> Any:
        """getUpper() -> int/float

        Returns the upper bound of the index.
        """

    def getValue(self, *args: Any, **kwargs: Any) -> Any:
        """getValue() -> int/float

        Returns the current value of the index.
        Raises an exception if the index is a range.
        """

    def hasLowerBound(self, *args: Any, **kwargs: Any) -> Any:
        """hasLowerBound() -> bool

        Returns True if a lower bound is specified.
        """

    def hasRange(self, *args: Any, **kwargs: Any) -> Any:
        """hasRange() -> bool

        Returns True if a range was specified.
        """

    def hasUpperBound(self, *args: Any, **kwargs: Any) -> Any:
        """hasUpperBound() -> bool

        Returns True if an upper bound is specified.
        """

    def hasValidRange(self, *args: Any, **kwargs: Any) -> Any:
        """hasValidRange() -> bool

        Returns True if upper bound is greater than lower bound.
        """

    def isBounded(self, *args: Any, **kwargs: Any) -> Any:
        """isBounded() -> bool

        Returns True if the index is bounded.
        """

    kFloat: int = 1
    kInteger: int = 0
    def setLower(self, *args: Any, **kwargs: Any) -> Any:
        """setLower(value) -> self

        Sets the lower bound of the index.
        """

    def setType(self, *args: Any, **kwargs: Any) -> Any:
        """setType(type) -> self

        Sets the type of attribute index.
        See type() for a list of valid index types.

        * type (int) - the index type to set
        """

    def setUpper(self, *args: Any, **kwargs: Any) -> Any:
        """setUpper(value) -> self

        Sets the upper bound of the index.
        """

    def setValue(self, *args: Any, **kwargs: Any) -> Any:
        """setValue(value) -> self

        Sets the value of the index.

        Remark: calling this method with an integer value will change its type to kInteger, and subsequently calling with a float value will change it to kFloat.
        """

    def type(self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Returns the type of attribute index.

        Valid index types:
          kInteger      Integer index (e.g. mesh.cp[5])
          kFloat                Floating-poing index (e.g. curve.u[1.3])
        """


class MAttributePattern(object):
    """Manipulate attribute structure patterns."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def addRootAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Add the given root attribute to this pattern."""

    def attrPattern(self, *args: Any, **kwargs: Any) -> Any:
        """Return the specified pattern indexed from the global list."""

    def attrPatternCount(self, *args: Any, **kwargs: Any) -> Any:
        """Return the global number of patterns created."""

    def findPattern(self, *args: Any, **kwargs: Any) -> Any:
        """Return a pattern with the given name, None if not found."""

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Return the name of the attribute pattern."""

    def removeRootAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Return the nth or passed-in root attribute from this pattern."""

    def rootAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Return the nth root attribute in this pattern."""

    def rootAttrCount(self, *args: Any, **kwargs: Any) -> Any:
        """Return the number of root attributes in this pattern."""


class MAttributeSpec(object):
    """Class that encapsulates component/attribute information for generating selection items."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source specification.

        * source (MAttributeSpec) - The source specification to copy from
        """

    dimensions: getset_descriptor = <attribute 'dimensions' of 'OpenMaya.MAttributeSpec' objects>
    name: getset_descriptor = <attribute 'name' of 'OpenMaya.MAttributeSpec' objects>

class MAttributeSpecArray(object):
    """Array of MAttributeSpec values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MAttributeSpecArray' objects>

class MBoundingBox(object):
    """3D axis-aligned bounding box."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    center: getset_descriptor = <attribute 'center' of 'OpenMaya.MBoundingBox' objects>
    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """Empties the bounding box, setting its corners to (0, 0, 0)."""

    def contains(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a point lies within the bounding box."""

    depth: getset_descriptor = <attribute 'depth' of 'OpenMaya.MBoundingBox' objects>
    def expand(self, *args: Any, **kwargs: Any) -> Any:
        """Expands the bounding box to include a point or other bounding box."""

    height: getset_descriptor = <attribute 'height' of 'OpenMaya.MBoundingBox' objects>
    def intersects(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if any part of a given bounding box lies within this one."""

    max: getset_descriptor = <attribute 'max' of 'OpenMaya.MBoundingBox' objects>
    min: getset_descriptor = <attribute 'min' of 'OpenMaya.MBoundingBox' objects>
    def transformUsing(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the bounding box's corners by a matrix."""

    width: getset_descriptor = <attribute 'width' of 'OpenMaya.MBoundingBox' objects>

class MCacheSchema(object):
    """Defines a node's cached data when participant in EM Cached Playback.
    Can be used to query or modify the attributes being cached.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def add(self, *args: Any, **kwargs: Any) -> Any:
        """add(attribute) -> self

        Force the attribute to be cached

        this method allows you to cache input attributes or other animatedattributes that are not fully understood by EM

        * attribute (MObject) - Attribute to cache
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset()

        Reset this schema to the minimal.
        """


class MCallbackIdArray(object):
    """Array of MCallbackId values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MCallbackIdArray' objects>

class MCameraMessage(MMessage):
    """Class used to register callbacks for Camera Manipulation Begin and End related messages."""
    def addBeginManipulationCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addBeginManipulationCallback(node, function, clientData=None) -> id

        Registers callbacks for camera manipulation beginning messages.

         * node (MObject) - The node to register the callback for.
         * function (MMessage::MNodeFunction) - the callback function
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addEndManipulationCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addEndManipulationCallback(node, function, clientData=None) -> id

        Registers callbacks for camera manipulation ending messages.

         * node (MObject) - The node to register the callback for.
         * function (MMessage::MNodeFunction) - the callback function
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class MColor(object):
    """Manipulate color data."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __itruediv__(self, value) -> Any:
        """Return self/=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rtruediv__(self, value) -> Any:
        """Return value/self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __truediv__(self, value) -> Any:
        """Return self/value."""

    a: getset_descriptor = <attribute 'a' of 'OpenMaya.MColor' objects>
    b: getset_descriptor = <attribute 'b' of 'OpenMaya.MColor' objects>
    g: getset_descriptor = <attribute 'g' of 'OpenMaya.MColor' objects>
    def getColor(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the color's components, in the specified color model."""

    kByte: int = 1
    kCMY: int = 2
    kCMYK: int = 3
    kFloat: int = 0
    kHSV: int = 1
    kOpaqueBlack: MColor = (0, 0, 0, 1)
    kRGB: int = 0
    kShort: int = 2
    r: getset_descriptor = <attribute 'r' of 'OpenMaya.MColor' objects>
    def setColor(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the color's components and color model."""


class MColorArray(object):
    """Array of MColor values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MColorArray' objects>

class MCommandMessage(MMessage):
    """Class used to register callbacks for command related messages.

    The class also provides the following MessageType constants which
    describe the different types of output messages:
      kHistory              #Command history
      kDisplay              #String to display unmodified
      kInfo         #General information
      kWarning              #Warning message
      kError                #Error message
      kResult               #Result from a command execution in the command window
      kStackTrace   #Stack trace
    """
    def addCommandCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addCommandOutputCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addCommandOutputCallback(function, clientData=None) -> id

        This method registers a callback for whenever commands generate
        output such as that which is printed into the command window.

         * function - callable which will be passed a string containing the
           MEL command being executed, a MessageType constant (see class docs
           for a list) indicating the message type and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addCommandOutputFilterCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addProcCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    kError: int = 4
    kResult: int = 5
    kStackTrace: int = 6
    kWarning: int = 3

class MConditionMessage(MMessage):
    """Class used to register callbacks for condition related messages."""
    def addConditionCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def getConditionNames(self, *args: Any, **kwargs: Any) -> Any:
        """getConditionNames() -> (string, string, ...)

        This method returns the list of available condition names.

         * return: tuple of available condition names.
        """

    def getConditionState(self, *args: Any, **kwargs: Any) -> Any:
        """getConditionState(name) -> bool

        This method returns the current state of a condition.

         * name (string) - the name of the condition.


         * return: The current state of the condition.
        """


class MContainerMessage(MMessage):
    """Class used to register callbacks for container related messages."""
    def addBoundAttrCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addBoundAttrCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an attribute
        is bound or unbound on a container.

         * function - callable which will be passed a Node (the container)
           ,a string indicating the name of the bound attr, and
           the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addPublishAttrCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addPublishAttrCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an attribute
        is published or unpublished from a container.

         * function - callable which will be passed a Node (the container)
           ,a string indicating the name of the published attr, and
           the clientData object.
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class MDAGDrawOverrideInfo(object):
    """A data structure to store the per path draw override information."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    displayType: getset_descriptor = <attribute 'displayType' of 'OpenMaya.MDAGDrawOverrideInfo' objects>
    enableShading: getset_descriptor = <attribute 'enableShading' of 'OpenMaya.MDAGDrawOverrideInfo' objects>
    enableTexturing: getset_descriptor = <attribute 'enableTexturing' of 'OpenMaya.MDAGDrawOverrideInfo' objects>
    enableVisible: getset_descriptor = <attribute 'enableVisible' of 'OpenMaya.MDAGDrawOverrideInfo' objects>
    kDisplayTypeNormal: int = 0
    kDisplayTypeReference: int = 1
    kDisplayTypeTemplate: int = 2
    kLODBoundingBox: int = 1
    kLODFull: int = 0
    lod: getset_descriptor = <attribute 'lod' of 'OpenMaya.MDAGDrawOverrideInfo' objects>
    overrideEnabled: getset_descriptor = <attribute 'overrideEnabled' of 'OpenMaya.MDAGDrawOverrideInfo' objects>
    playbackVisible: getset_descriptor = <attribute 'playbackVisible' of 'OpenMaya.MDAGDrawOverrideInfo' objects>

class MDGContext(object):
    """Dependency graph context."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source context.

        * source (MDGContext) - The source object to copy from
        """

    def current(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the current context being used for evaluation."""

    def getTime(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the time at which this context is set to evaluate."""

    def isCurrent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the context is currently being used for evaluation. Returns False if some other context is being used for evaluation."""

    def isNormal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the context is set to evaluate normally. Returns False if the context is set to evaluate at a specific time."""

    kNormal: MDGContext = <OpenMaya.MDGContext object at 0x00000218A9670BF0>
    def makeCurrent(self, *args: Any, **kwargs: Any) -> Any:
        """Makes this context the new current one being used for evaluation. Returns the previous evaluation context."""


class MDGMessage(MMessage):
    """Class used to register callbacks for Dependency Graph related messages."""
    def addConnectionCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addDelayedTimeChangeCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addDelayedTimeChangeCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph, but after the time changed callback.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addDelayedTimeChangeRunupCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addDelayedTimeChangeRunupCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph, but after the other time changed callbacks
        which can be used to invoke a dynamics solve or runup if needed

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addForceUpdateCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addForceUpdateCallback(function, clientData=None) -> id

        This method registers a callback that is called after the time
        changes and after all nodes have been evaluated in the
        dependency graph.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addNodeAddedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addNodeChangeUuidCheckCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addNodeRemovedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addPreConnectionCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addTimeChangeCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addTimeChangeCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever the time
        changes in the dependency graph.

         * function - callable which will be passed a MTime object indicating
           the new time and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class MDGModifier(object):
    """Used to change the structure of the dependency graph."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """addAttribute(MObject node, MObject attribute) -> self

        Adds an operation to the modifier to add a new dynamic attribute to the
        given dependency node. If the attribute is a compound its children will
        be added as well, so only the parent needs to be added using this method.
        """

    def addExtensionAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """addExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

        Adds an operation to the modifier to add a new extension attribute to
        the given node class. If the attribute is a compound its children will be
        added as well, so only the parent needs to be added using this method.
        """

    def commandToExecute(self, *args: Any, **kwargs: Any) -> Any:
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

    def connect(self, *args: Any, **kwargs: Any) -> Any:
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

    def createNode(self, *args: Any, **kwargs: Any) -> Any:
        """createNode(typeName) -> MObject
        createNode(MTypeId typeId) -> MObject

        Adds an operation to the modifier to create a node of the given type.
        The new node is created and returned but will not be added to the
        Dependency Graph until the modifier's doIt() method is called. Raises
        TypeError if the named node type does not exist or if it is a DAG node
        type.
        """

    def deleteNode(self, *args: Any, **kwargs: Any) -> Any:
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

    def disconnect(self, *args: Any, **kwargs: Any) -> Any:
        """disconnect(MPlug source, MPlug dest) -> self
        disconnect(MObject sourceNode, MObject sourceAttr,
                   MObject destNode,   MObject destAttr) -> self

        Adds an operation to the modifier that breaks a connection between two
        plugs in the dependency graph.
        Plugs can either be specified with node and attribute MObjects or with
        MPlugs.
        """

    def doIt(self, *args: Any, **kwargs: Any) -> Any:
        """doIt() -> self

        Executes the modifier's operations. If doIt() is called multiple times
        in a row, without any intervening calls to undoIt(), then only the
        operations which were added since the previous doIt() call will be
        executed. If undoIt() has been called then the next call to doIt() will
        do all operations.
        """

    def linkExtensionAttributeToPlugin(self, *args: Any, **kwargs: Any) -> Any:
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

    def newPlugValue(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValue(MPlug plug, MObject value) -> self

        Adds an operation to the modifier to set the value of a plug, where
        value is an MObject data wrapper, such as created by the various
        MFn*Data classes.
        """

    def newPlugValueBool(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueBool(MPlug plug, bool value) -> self

        Adds an operation to the modifier to set a value onto a bool plug.
        """

    def newPlugValueChar(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueChar(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto a char (single
        byte signed integer) plug.
        """

    def newPlugValueDouble(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueDouble(MPlug plug, float value) -> self

        Adds an operation to the modifier to set a value onto a double-precision
        float plug.
        """

    def newPlugValueFloat(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueFloat(MPlug plug, float value) -> self

        Adds an operation to the modifier to set a value onto a single-precision
        float plug.
        """

    def newPlugValueInt(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueInt(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto an int plug.
        """

    def newPlugValueMAngle(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueMAngle(MPlug plug, MAngle value) -> self

        Adds an operation to the modifier to set a value onto an angle plug.
        """

    def newPlugValueMDistance(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueMDistance(MPlug plug, MDistance value) -> self

        Adds an operation to the modifier to set a value onto a distance plug.
        """

    def newPlugValueMTime(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueMTime(MPlug plug, MTime value) -> self

        Adds an operation to the modifier to set a value onto a time plug.
        """

    def newPlugValueShort(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueShort(MPlug plug, int value) -> self

        Adds an operation to the modifier to set a value onto a short
        integer plug.
        """

    def newPlugValueString(self, *args: Any, **kwargs: Any) -> Any:
        """newPlugValueString(MPlug plug, string value) -> self

        Adds an operation to the modifier to set a value onto a string plug.
        """

    def pythonCommandToExecute(self, *args: Any, **kwargs: Any) -> Any:
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

    def removeAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """removeAttribute(MObject node, MObject attribute) -> self

        Adds an operation to the modifier to remove a dynamic attribute from the
        given dependency node. If the attribute is a compound its children will
        be removed as well, so only the parent needs to be removed using this
        method. The attribute MObject passed in will be set to kNullObj. There
        should be no function sets attached to the attribute at the time of the
        call as their behaviour may become unpredictable.
        """

    def removeExtensionAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """removeExtensionAttribute(MNodeClass nodeClass, MObject attribute) -> self

        Adds an operation to the modifier to remove an extension attribute from
        the given node class. If the attribute is a compound its children will
        be removed as well, so only the parent needs to be removed using this
        method. The attribute MObject passed in will be set to kNullObj. There
        should be no function sets attached to the attribute at the time of the
        call as their behaviour may become unpredictable.
        """

    def removeExtensionAttributeIfUnset(self, *args: Any, **kwargs: Any) -> Any:
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

    def removeMultiInstance(self, *args: Any, **kwargs: Any) -> Any:
        """removeMultiInstance(MPlug plug, bool breakConnections) -> self

        Adds an operation to the modifier to remove an element of a multi (array) plug.
        """

    def renameAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """renameAttribute(MObject node, MObject attribute, 
        string newShortName, string newShortName) -> self

        Adds an operation to the modifer that renames a dynamic attribute on the given dependency node.
        """

    def renameNode(self, *args: Any, **kwargs: Any) -> Any:
        """renameNode(MObject node, string newName) -> self

        Adds an operation to the modifer to rename a node.
        """

    def setNodeLockState(self, *args: Any, **kwargs: Any) -> Any:
        """setNodeLockState(MObject node, bool newState) -> self

        Adds an operation to the modifier to set the lockState of a node.
        """

    def undoIt(self, *args: Any, **kwargs: Any) -> Any:
        """undoIt() -> self

        Undoes all of the operations that have been given to this modifier. It
        is only valid to call this method after the doIt() method has been
        called.
        """

    def unlinkExtensionAttributeFromPlugin(self, *args: Any, **kwargs: Any) -> Any:
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
    """Class used to register callbacks for Dag related messages.

    The class also provides the following DagMessage constants which describe the different types of DAG operations:
      kParentAdded
      kParentRemoved
      kChildAdded
      kChildRemoved
      kChildReordered
      kInstanceAdded
      kInstanceRemoved
      kInvalidMsg
    """
    def addAllDagChangesCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addAllDagChangesDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addChildAddedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addChildAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        added in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addChildAddedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addChildAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        added to the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addChildRemovedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addChildRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        removed in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addChildRemovedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addChildRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        removed from the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addChildReorderedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addChildReorderedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a child is
        reordered in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addChildReorderedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addChildReorderedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a child of
        the specified DAG node is reordered

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addDagCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addDagDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addInstanceAddedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever any node in the DAG
        is instanced.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addInstanceAddedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever the specified node
        is instanced

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addInstanceRemovedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever an instance of any DAG
        node is removed or deleted.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addInstanceRemovedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addInstanceRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever an instance of the specified
        node is removed.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addMatrixModifiedCallback(self, *args: Any, **kwargs: Any) -> Any:
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
          kScaleX               kScaleY                 kScaleZ
          kShearXY              kShearXZ                kShearYZ
          kRotateX              kRotateY                kRotateZ
          kTranslateX   kTranslateY             kTranslateZ
          kScalePivotX  kScalePivotY    kScalePivotZ
          kRotatePivotX kRotatePivotY   kRotatePivotZ
          kScaleTransX  kScaleTransY    kScaleTransZ
          kRotateTransX kRotateTransY   kRotateTransZ
          kRotateOrientX        kRotateOrientY  kRotateOrientZ
          kRotateOrder
        Composite flags
          kAll
          kScale                = kScaleX        | kScaleY        | kScaleZ
          kShear                = kShearXY       | kShearXZ       | kShearYZ
          kRotation             = kRotateX       | kRotateY       | kRotateZ
          kTranslation          = kTranslateX    | kTranslateY    | kTranslateZ
          kScalePivot           = kScalePivotX   | kScalePivotY   | kScalePivotZ
          kRotatePivot          = kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
          kScalePivotTrans      = kScaleTransX   | kScaleTransY   | kScaleTransZ
          kRotatePivotTrans     = kRotateTransX  | kRotateTransY  | kRotateTransZ
          kRotateOrient         = kRotateOrientX | kRotateOrientY | kRotateOrientZ

         * return: Identifier used for removing the callback.
        """

    def addParentAddedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addParentAddedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        added in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addParentAddedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addParentAddedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        added to the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addParentRemovedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addParentRemovedCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        removed in the DAG.

         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addParentRemovedDagPathCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addParentRemovedDagPathCallback(node, function, clientData=None) -> id

        This method registers a callback that is called whenever a parent is
        removed from the specified DAG node.

         * node (MDagPath) - the DAG node to register the callback for
         * function - callable which will be passed a MDagPath to the parent,
           a MDagPath to the child, and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addWorldMatrixModifiedCallback(self, *args: Any, **kwargs: Any) -> Any:
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
          kScaleX               kScaleY                 kScaleZ
          kShearXY              kShearXZ                kShearYZ
          kRotateX              kRotateY                kRotateZ
          kTranslateX   kTranslateY             kTranslateZ
          kScalePivotX  kScalePivotY    kScalePivotZ
          kRotatePivotX kRotatePivotY   kRotatePivotZ
          kScaleTransX  kScaleTransY    kScaleTransZ
          kRotateTransX kRotateTransY   kRotateTransZ
          kRotateOrientX        kRotateOrientY  kRotateOrientZ
          kRotateOrder
        Composite flags
          kAll
          kScale                = kScaleX        | kScaleY        | kScaleZ
          kShear                = kShearXY       | kShearXZ       | kShearYZ
          kRotation             = kRotateX       | kRotateY       | kRotateZ
          kTranslation          = kTranslateX    | kTranslateY    | kTranslateZ
          kScalePivot           = kScalePivotX   | kScalePivotY   | kScalePivotZ
          kRotatePivot          = kRotatePivotX  | kRotatePivotY  | kRotatePivotZ
          kScalePivotTrans      = kScaleTransX   | kScaleTransY   | kScaleTransZ
          kRotatePivotTrans     = kRotateTransX  | kRotateTransY  | kRotateTransZ
          kRotateOrient         = kRotateOrientX | kRotateOrientY | kRotateOrientZ

         * return: Identifier used for removing the callback.
        """

    kAll: int = 268435455
    kChildRemoved: int = 3
    kChildReordered: int = 4
    kInstanceAdded: int = 5
    kInstanceRemoved: int = 6
    kInvalidMsg: int = -1
    kLast: int = 7
    kRotateOrder: int = 134217728
    kRotateOrient: int = 117440512
    kRotateOrientX: int = 16777216
    kRotateOrientY: int = 33554432
    kRotateOrientZ: int = 67108864
    kRotatePivot: int = 229376
    kRotatePivotTrans: int = 14680064
    kRotatePivotX: int = 32768
    kRotatePivotY: int = 65536
    kRotatePivotZ: int = 131072
    kRotateTransX: int = 2097152
    kRotateTransY: int = 4194304
    kRotateTransZ: int = 8388608
    kRotateX: int = 64
    kRotateY: int = 128
    kRotateZ: int = 256
    kRotation: int = 448
    kScale: int = 7
    kScalePivot: int = 28672
    kScalePivotTrans: int = 1835008
    kScalePivotX: int = 4096
    kScalePivotY: int = 8192
    kScalePivotZ: int = 16384
    kScaleTransX: int = 262144
    kScaleTransY: int = 524288
    kScaleTransZ: int = 1048576
    kScaleZ: int = 4
    kShear: int = 56
    kShearXY: int = 8
    kShearXZ: int = 16
    kShearYZ: int = 32
    kTranslateX: int = 512
    kTranslateY: int = 1024
    kTranslateZ: int = 2048
    kTranslation: int = 3584

class MDagModifier(MDGModifier):
    """Used to change the structure of the DAG"""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def createNode(self, *args: Any, **kwargs: Any) -> Any:
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

    def reparentNode(self, *args: Any, **kwargs: Any) -> Any:
        """reparentNode(MObject node, newParent=MObject.kNullObj) -> self

        Adds an operation to the modifier to reparent a DAG node under a
        specified parent.

        If no parent is provided then the DAG node will be reparented under the
        world, so long as it is a transform type. If it is not a transform type
        then the doIt() will raise a RuntimeError.
        """


class MDagPath(object):
    """Path to a DAG node from the top of the DAG."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def apiType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the object at the end of the path."""

    def child(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the specified child of the object at the end of the path."""

    def childCount(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of objects parented directly beneath the object at the end of the path."""

    def exclusiveMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix for all transforms in the path, excluding the end object."""

    def exclusiveMatrixInverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the inverse of exclusiveMatrix()."""

    def extendToShape(self, *args: Any, **kwargs: Any) -> Any:
        """Extends the path to the specified shape node parented directly beneath the transform at the current end of the path."""

    def fullPathName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a string representation of the path from the DAG root to the path's last node."""

    def getAPathTo(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the first path found to the given node."""

    def getAllPathsTo(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all paths to the given node."""

    def getDisplayStatus(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the display status for this path."""

    def getDrawOverrideInfo(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the draw override information for this path."""

    def getPath(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the specified sub-path of this path."""

    def hasFn(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the object at the end of the path supports the given function set."""

    def inclusiveMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix for all transforms in the path, including the end object, if it is a transform."""

    def inclusiveMatrixInverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the inverse of inclusiveMatrix()."""

    def instanceNumber(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the instance number of this path to the object at the end."""

    def isInstanced(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the object at the end of the path can be reached by more than one path."""

    def isTemplated(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the DAG Node at the end of the path is templated."""

    def isValid(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this is a valid path."""

    def isVisible(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the DAG Node at the end of the path is visible."""

    def length(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of nodes on the path, not including the DAG's root node."""

    def matchTransform(self, *args: Any, **kwargs: Any) -> Any:
        """Do some new stuff."""

    def node(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the DAG node at the end of the path."""

    def numberOfShapesDirectlyBelow(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of shape nodes parented directly beneath the transform at the end of the path."""

    def partialPathName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the minimum string representation which will uniquely identify the path."""

    def pathCount(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of sub-paths which make up this path."""

    def pop(self, *args: Any, **kwargs: Any) -> Any:
        """Removes objects from the end of the path."""

    def push(self, *args: Any, **kwargs: Any) -> Any:
        """Extends the path to the specified child object, which must be parented directly beneath the object currently at the end of the path."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the current path held by this object with another."""

    def transform(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the last transform node on the path."""


class MDagPathArray(object):
    """Array of MDagPath values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MDagPathArray' objects>

class MDataBlock(object):
    """Dependency node data block."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def context(self, *args: Any, **kwargs: Any) -> Any:
        """context() -> MDGContext

        Returns a copy of the dependecy graph context for which this data block was created. The context is used to specify how a dependency node is going to be evaluated.
        """

    def inputArrayValue(self, *args: Any, **kwargs: Any) -> Any:
        """inputArrayValue(plug) -> MArrayDataHandle
        inputArrayValue(attribute) -> MArrayDataHandle

        Gets an array handle to this data block for the given plug/attribute's data.  This is only valid if the given plug has array data.  The data represented by the handle will be valid.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned.  If the plug has not been set to a particular value, then the default value will be returned.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute whose data you wish to access
        """

    def inputValue(self, *args: Any, **kwargs: Any) -> Any:
        """inputValue(plug) -> MDataHandle
        inputValue(attribute) -> MDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  The data represented by the handle is guaranteed to be valid for reading.  If the data is from a dirty connection, then the connection will be evaluated.  If no connection is present, then the value that the plug has been set to will be returned. If the plug has not been set to a particular value, then the default value will be returned.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
        """

    def isClean(self, *args: Any, **kwargs: Any) -> Any:
        """isClean(plug) -> bool
        isClean(attribute) -> bool

        Queries the dependency graph to see whether the given plug/attribute is clean.

        * plug (MPlug) - the plug that is to be query
         OR
        * attribute (MObject) - the attribute that is to be query.
        """

    def outputArrayValue(self, *args: Any, **kwargs: Any) -> Any:
        """outputArrayValue(plug) -> MArrayDataHandle
        outputArrayValue(attribute) -> MArrayDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  No dependency graph evaluations will be done, and therefore the data is not guaranteed to be valid (i.e. it may be dirty).  Typically, this method is used to get the handle during compute in order to write output data to it.

        Another usage of this method is to access an input array attribute without evaluating any of its array elements. One can then use MArrayDataHandle.jumpToElement() to get to the particular element of interest, and evaluate its value using MArrayDataHandle.inputValue().

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute whose data you wish to access
        """

    def outputValue(self, *args: Any, **kwargs: Any) -> Any:
        """outputValue(plug) -> MDataHandle
        outputValue(attribute) -> MDataHandle

        Gets a handle to this data block for the given plug/attribute's data.  The data is not guaranteed to be valid.  No dependency graph evaluations will be done. Therefore, this handle should be used only for writing.

        * plug (MPlug) - the plug whose data you wish to access
         OR
        * attribute (MObject) - the attribute of the node that you want to access
        """

    def setClean(self, *args: Any, **kwargs: Any) -> Any:
        """setClean(plug) -> self
        setClean(attribute) -> self

        Tells the dependency graph that the given plug/attribute has been updated and is now clean.  This should be called after the data in the plug has been recalculated from the inputs of the node.

        * plug (MPlug) - the plug that is to be marked clean
         OR
        * attribute (MObject) - the attribute that is to be marked clean
        """

    def setContext(self, *args: Any, **kwargs: Any) -> Any:
        """setContext(ctx) -> self

        Set the dependency graph context for this data block. The context is used to specify how a dependency node is going to be evaluated, thus replacing the context for the given datablock. This does not modify the dirty state of the datablock so that they apply to the new context.

        This function should not be used for timed evaluation.

        * ctx (MDGContext) - the dependency graph context
        """


class MDataHandle(object):
    """Data handle for information contained in a data block."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def acceptedTypeIds(self, *args: Any, **kwargs: Any) -> Any:
        """acceptedTypeIds() -> array of MTypeIds

        This method returns an array of MTypeIds.
        """

    def asAddr(self, *args: Any, **kwargs: Any) -> Any:
        """asAddr() -> long

        Returns the data represented by this handle in the data block.
        """

    def asAngle(self, *args: Any, **kwargs: Any) -> Any:
        """asAngle() -> MAngle

        Returns the data represented by this handle in the data block.
        """

    def asBool(self, *args: Any, **kwargs: Any) -> Any:
        """asBool() -> bool

        Returns the data represented by this handle in the data block.
        """

    def asChar(self, *args: Any, **kwargs: Any) -> Any:
        """asChar() -> int

        Returns the data represented by this handle in the data block.
        """

    def asDistance(self, *args: Any, **kwargs: Any) -> Any:
        """asDistance() -> MDistance

        Returns the data represented by this handle in the data block.
        """

    def asDouble(self, *args: Any, **kwargs: Any) -> Any:
        """asDouble() -> float

        Returns the data represented by this handle in the data block.
        """

    def asDouble2(self, *args: Any, **kwargs: Any) -> Any:
        """asDouble2() -> [float, float]

        Returns the data represented by this handle in the data block.
        """

    def asDouble3(self, *args: Any, **kwargs: Any) -> Any:
        """asDouble3() -> [float, float, float]

        Returns the data represented by this handle in the data block.
        """

    def asDouble4(self, *args: Any, **kwargs: Any) -> Any:
        """asDouble4() -> [float, float, float, float]

        Returns the data represented by this handle in the data block.
        """

    def asFloat(self, *args: Any, **kwargs: Any) -> Any:
        """asFloat() -> float

        Returns the data represented by this handle in the data block.
        """

    def asFloat2(self, *args: Any, **kwargs: Any) -> Any:
        """asFloat2() -> [float, float]

        Returns the data represented by this handle in the data block.
        """

    def asFloat3(self, *args: Any, **kwargs: Any) -> Any:
        """asFloat3() -> [float, float, float]

        Returns the data represented by this handle in the data block.
        """

    def asFloatMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """asFloatMatrix() -> MFloatMatrix

        Returns the data represented by this handle in the data block.
        """

    def asFloatVector(self, *args: Any, **kwargs: Any) -> Any:
        """asFloatVector() -> MFloatVector

        Returns the data represented by this handle in the data block.
        """

    def asGenericBool(self, *args: Any, **kwargs: Any) -> Any:
        """asGenericBool() -> bool

        Returns the generic data represented by this handle in the data block.
        """

    def asGenericChar(self, *args: Any, **kwargs: Any) -> Any:
        """asGenericChar() -> int

        Returns the generic data represented by this handle in the data block.
        """

    def asGenericDouble(self, *args: Any, **kwargs: Any) -> Any:
        """asGenericDouble() -> float

        Returns the generic data represented by this handle in the data block.
        """

    def asGenericFloat(self, *args: Any, **kwargs: Any) -> Any:
        """asGenericFloat() -> float

        Returns the generic data represented by this handle in the data block.
        """

    def asGenericInt(self, *args: Any, **kwargs: Any) -> Any:
        """asGenericInt() -> int

        Returns the generic data represented by this handle in the data block.
        """

    def asGenericShort(self, *args: Any, **kwargs: Any) -> Any:
        """asGenericShort() -> int

        Returns the generic data represented by this handle in the data block.
        """

    def asInt(self, *args: Any, **kwargs: Any) -> Any:
        """asInt() -> int

        Returns the data represented by this handle in the data block.
        """

    def asInt2(self, *args: Any, **kwargs: Any) -> Any:
        """asInt2() -> [int, int]

        Returns the data represented by this handle in the data block.
        """

    def asInt3(self, *args: Any, **kwargs: Any) -> Any:
        """asInt3() -> [int, int, int]

        Returns the data represented by this handle in the data block.
        """

    def asMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """asMatrix() -> MMatrix

        Returns the data represented by this handle in the data block.This method is only valid for attributes created using the MFnMatrixAttribute function set.
        """

    def asMesh(self, *args: Any, **kwargs: Any) -> Any:
        """asMesh() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set and iterators.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the mesh function set and iterators.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """

    def asMeshTransformed(self, *args: Any, **kwargs: Any) -> Any:
        """asMeshTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the mesh function set (MFnMesh) or any of the mesh iterators.

        If the incoming mesh comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the mesh that is returned will be the mesh as it exists in world space.

        The mesh that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """

    def asNurbsCurve(self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsCurve() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The curve returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix. This means that world space operations may be performed on this object using the nurbs curve function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """

    def asNurbsCurveTransformed(self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsCurveTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs curve function set (MFnNurbsCurve) or the nurbs curve CV iterator (MItCurveCV).

        If the incoming curve comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the curve that is returned will be the curve as it exists in world space.

        The curve that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """

    def asNurbsSurface(self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsSurface() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space transformation matrix.  This means that world space operations may be performed on this object using the nurbs surface function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """

    def asNurbsSurfaceTransformed(self, *args: Any, **kwargs: Any) -> Any:
        """asNurbsSurfaceTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the nurbs surface function set (MFnNurbsSurface) or the nurbs surface CV iterator (MItSurfaceCV).

        If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

        The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """

    def asPluginData(self, *args: Any, **kwargs: Any) -> Any:
        """asPluginData() -> MPxData

        Returns the data represented by this handle in the data block.  The object is returned as plugin data.  This should be used to access data types defined by plugins.
        """

    def asShort(self, *args: Any, **kwargs: Any) -> Any:
        """asShort() -> int

        Returns the data represented by this handle in the data block.
        """

    def asShort2(self, *args: Any, **kwargs: Any) -> Any:
        """asShort2() -> [int, int]

        Returns the data represented by this handle in the data block.
        """

    def asShort3(self, *args: Any, **kwargs: Any) -> Any:
        """asShort3() -> [int, int, int]

        Returns the data represented by this handle in the data block.
        """

    def asString(self, *args: Any, **kwargs: Any) -> Any:
        """asString() -> MString

        Returns the data represented by this handle in the data block.
        """

    def asSubdSurface(self, *args: Any, **kwargs: Any) -> Any:
        """asSubdSurface() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set and iterator.  Even though this method does not return a reference to an MObject, modifications to the MObject instance will update the contents of the handle in the data block.  The method MDataHandle.setClean() should be called after the data block has been modified.

        The subdivision surface returned by this method will be in local space even if the connection is supplying world space geometry.  This occurs mostly for efficiency reasons.  In the case of a world space geometry connection, the MObject returned by this method will also contain the world space   transformation matrix. This means that world space operations may be performed on this object using the subdivision surface function set and iterator.

        It is possible to get the matrix that defines the local to world transformation for this geometry using the MDataHandle.geometryTransformMatrix() method.
        """

    def asSubdSurfaceTransformed(self, *args: Any, **kwargs: Any) -> Any:
        """asSubdSurfaceTransformed() -> MObject

        Returns the data represented by this handle in the data block.  The object returned by this call may be used directly with the subdivision surface function set (MFnSubdSurface) or the subdivision surface iterators (MItSubdVertex, MItSubdFace, MItSubdEdge).

        If the incoming surface comes with world space transformation data, then it will be applied to the data that is returned.  In other words, the surface that is returned will be the surface as it exists in world space.

        The surface that is returned from this method should not be modified.  This method is only provided to make it easier to take world space geometry as input.
        """

    def asTime(self, *args: Any, **kwargs: Any) -> Any:
        """asTime() -> MTime

        Returns the data represented by this handle in the data block.
        """

    def asUChar(self, *args: Any, **kwargs: Any) -> Any:
        """asUChar() -> int

        Returns the data represented by this handle in the data block.
        """

    def asVector(self, *args: Any, **kwargs: Any) -> Any:
        """asVector() -> MVector

        Returns the data represented by this handle in the data block.
        """

    def child(self, *args: Any, **kwargs: Any) -> Any:
        """child(MPlug) -> MDataHandle
        child(MObject) -> MDataHandle

        Get a handle to a child of this handle.  This is used if you have a handle to a compound attribute.
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(src) -> self

        Copies the attribute from the src attribute to the attribute referenced by this handle.  This is the only method which can completely copy a compound attribute from one handle to another.  The construct outputHandle.set (inputHandle.data()) will not work for compound or multi attributes.

        * src (MDataHandle) - the handle to the attribute to copy.
        """

    def copyWritable(self, *args: Any, **kwargs: Any) -> Any:
        """copyWritable(src) -> self

        Copies the attribute from the <i>src</i> attribute to the attribute referenced by this handle.  When the copy is made it ensures that the data in this handle is writable. That is, if the src handle has a writable copy of the data then it will be duplicated, otherwise this handle will claim the writer status for the data.

        * src (MDataHandle) - the handle to the attribute to copy.
        """

    def data(self, *args: Any, **kwargs: Any) -> Any:
        """data() -> MObject

        Returns the data object from this handle.  The object returned should be used with the appropriate data function set.  This method is not valid for simple numeric types.
        """

    def datablock(self, *args: Any, **kwargs: Any) -> Any:
        """datablock() -> MDataBlock

        Returns a reference to the datablock assigned to this data handle.
        """

    def geometryTransformMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """geometryTransformMatrix() -> MMatrix

        This method returns a reference to the local-to-world transformation matrix that can accompany a geometry data object.  Only use this method on handles to geometry data (curves, surfaces, and meshes).

        If no local-to-world transformation information has been provided then this will be an identity matrix.
        """

    def isGeneric(self, *args: Any, **kwargs: Any) -> Any:
        """isGeneric() -> [bool, isNumeric, isNull]

        Returns True if this handle is for generic data.  There are 2 forms of generic data.  The first is for simple data and is used if the isNumeric parameter returns True.  In this case, the asGeneric*() and setGeneric*() methods of this class are used to query and set values.
        The second form of generic data is for more complex attribute types.  As a result the type of the object must be checked and an appropriate attribute function set initialized with the object.Returns isNumeric True if this handle is for simple generic numeric data.
        Returns isNull True if this handle is not set.
        """

    def isNumeric(self, *args: Any, **kwargs: Any) -> Any:
        """isNumeric() -> bool

        Returns True if this handle is for simple numeric data. That means that the numeric data is directly accessible through the non-generic as*() and set*() methods of this handle. For example, depending on handle initialization, the asBool() may be called but the asGenericBool() should not be called.
        """

    def numericType(self, *args: Any, **kwargs: Any) -> Any:
        """numericType() -> int

        Returns the type of data represented by this handle.  This method is only valid for data handles of simple numeric types.
        """

    def set2Double(self, *args: Any, **kwargs: Any) -> Any:
        """set2Double(float, float) -> self

        Set the data that this handle represents in the data block.
        """

    def set2Float(self, *args: Any, **kwargs: Any) -> Any:
        """set2Float(float, float) -> self

        Set the data that this handle represents in the data block.
        """

    def set2Int(self, *args: Any, **kwargs: Any) -> Any:
        """set2Int(int, int) -> self

        Set the data that this handle represents in the data block.
        """

    def set2Short(self, *args: Any, **kwargs: Any) -> Any:
        """set2Short(int, int) -> self

        Set the data that this handle represents in the data block.
        """

    def set3Double(self, *args: Any, **kwargs: Any) -> Any:
        """set3Double(float, float, float) -> self

        Set the data that this handle represents in the data block.
        """

    def set3Float(self, *args: Any, **kwargs: Any) -> Any:
        """set3Float(float, float, float) -> self

        Set the data that this handle represents in the data block.
        """

    def set3Int(self, *args: Any, **kwargs: Any) -> Any:
        """set3Int(int, int, int) -> self

        Set the data that this handle represents in the data block.
        """

    def set3Short(self, *args: Any, **kwargs: Any) -> Any:
        """set3Short(int, int, int) -> self

        Set the data that this handle represents in the data block.
        """

    def set4Double(self, *args: Any, **kwargs: Any) -> Any:
        """set4Double(float, float, float, float) -> self

        Set the data that this handle represents in the data block.
        """

    def setBool(self, *args: Any, **kwargs: Any) -> Any:
        """setBool(bool) -> self

        Set the data that this handle represents in the data block.
        """

    def setChar(self, *args: Any, **kwargs: Any) -> Any:
        """setChar(int) -> self

        Set the data that this handle represents in the data block.
        """

    def setClean(self, *args: Any, **kwargs: Any) -> Any:
        """setClean() -> self

        Marks the data that is represented by this handle as being clean.  This should be done after recalculating the data from the inputs.
        """

    def setDouble(self, *args: Any, **kwargs: Any) -> Any:
        """setDouble(float) -> self

        Set the data that this handle represents in the data block.
        """

    def setFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setFloat(float) -> self

        Set the data that this handle represents in the data block.
        """

    def setGenericBool(self, *args: Any, **kwargs: Any) -> Any:
        """setGenericBool(bool, force) -> self

        Set the data that this handle represents in the data block.
        """

    def setGenericChar(self, *args: Any, **kwargs: Any) -> Any:
        """setGenericChar(int, force) -> self

        Set the data that this handle represents in the data block.
        """

    def setGenericDouble(self, *args: Any, **kwargs: Any) -> Any:
        """setGenericDouble(float, force) -> self

        Set the data that this handle represents in the data block.
        """

    def setGenericFloat(self, *args: Any, **kwargs: Any) -> Any:
        """setGenericFloat(float, force) -> self

        Set the data that this handle represents in the data block.
        """

    def setGenericInt(self, *args: Any, **kwargs: Any) -> Any:
        """setGenericInt(int, force) -> self

        Set the data that this handle represents in the data block.
        """

    def setGenericShort(self, *args: Any, **kwargs: Any) -> Any:
        """setGenericShort(int, force) -> self

        Set the data that this handle represents in the data block.
        """

    def setInt(self, *args: Any, **kwargs: Any) -> Any:
        """setInt(int) -> self

        Set the data that this handle represents in the data block.
        """

    def setMAngle(self, *args: Any, **kwargs: Any) -> Any:
        """setMAngle(MAngle) -> self

        Set the data that this handle represents in the data block.
        """

    def setMDistance(self, *args: Any, **kwargs: Any) -> Any:
        """setMDistance(MDistance) -> self

        Set the data that this handle represents in the data block.
        """

    def setMFloatMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """setMFloatMatrix(MFloatMatrix) -> self

        Set the data that this handle represents in the data block.
        """

    def setMFloatVector(self, *args: Any, **kwargs: Any) -> Any:
        """setMFloatVector(MFloatVector) -> self

        Set the data that this handle represents in the data block.
        """

    def setMMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """setMMatrix(MMatrix) -> self

        Set the data that this handle represents in the data block.
        """

    def setMObject(self, *args: Any, **kwargs: Any) -> Any:
        """setMObject(MObject) -> self

        Set the data that this handle represents in the data block.  This method assumes that the MObject is a dependency graph data object.  These objects can be created using the appropriate MFn..Data function set.
        Note that this method cannot be used to copy compound or multi attributes from one handle to another via the construct outputHandle.set (inputHandle.data()).
        To copy these user defined attributes, the method MDataHandle.copy() must be used.
        """

    def setMPxData(self, *args: Any, **kwargs: Any) -> Any:
        """setMPxData(MPxData) -> self

        Set the data that this handle represents in the data block.  This method takes a pointer to a user defined data object.  The data block will become the new owner of the data object that you pass in.  Do not delete it.
        """

    def setMTime(self, *args: Any, **kwargs: Any) -> Any:
        """setMTime(MTime) -> self

        Set the data that this handle represents in the data block.
        """

    def setMVector(self, *args: Any, **kwargs: Any) -> Any:
        """setMVector(MVector) -> self

        Set the data that this handle represents in the data block.
        """

    def setShort(self, *args: Any, **kwargs: Any) -> Any:
        """setShort(int) -> self

        Set the data that this handle represents in the data block.
        """

    def setString(self, *args: Any, **kwargs: Any) -> Any:
        """setString(string) -> self

        Set the data that this handle represents in the data block.
        """

    def type(self, *args: Any, **kwargs: Any) -> Any:
        """type() -> int

        Returns the type of data represented by this handle.
        """

    def typeId(self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Returns the type of data represented by this handle as a type id.  A type id is a four character code that is used to identify the data type.
        If no data exists for this handle, the type id will be 0x0.
        """


class MDistance(object):
    """Manipulate distance data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def asCentimeters(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to centimeters."""

    def asFeet(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to feet."""

    def asInches(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to inches."""

    def asKilometers(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to kilometers."""

    def asMeters(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to meters."""

    def asMiles(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to miles."""

    def asMillimeters(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to millimeters."""

    def asUnits(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to the specified units."""

    def asYards(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance value, converted to yards."""

    def internalToUI(self, *args: Any, **kwargs: Any) -> Any:
        """Convert a value from Maya's internal units to the units used in the UI."""

    def internalUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Return the distance unit used internally by Maya."""

    kCentimeters: int = 6
    kFeet: int = 2
    kInches: int = 1
    kInvalid: int = 0
    kKilometers: int = 7
    kLast: int = 9
    kMeters: int = 8
    kMiles: int = 4
    kMillimeters: int = 5
    kYards: int = 3
    def setUIUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Change the units used to display distances in Maya's UI."""

    def uiToInternal(self, *args: Any, **kwargs: Any) -> Any:
        """Convert a value from the units used in the UI to Maya's internal units."""

    def uiUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Return the units used to display distances in Maya's UI."""

    unit: getset_descriptor = <attribute 'unit' of 'OpenMaya.MDistance' objects>
    value: getset_descriptor = <attribute 'value' of 'OpenMaya.MDistance' objects>

class MDoubleArray(object):
    """Array of double values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MDoubleArray' objects>

class MEulerRotation(object):
    """X, Y and Z rotations, applied in a specified order."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __neg__(self) -> Any:
        """-self"""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def alternateSolution(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation which is not simply a multiple."""

    def asMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent matrix."""

    def asQuaternion(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent quaternion."""

    def asVector(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the X, Y and Z rotations as a vector."""

    def bound(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new MEulerRotation having this rotation, but with each rotation component bound within +/- PI."""

    def boundIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place bounding of each rotation component to lie wthin +/- PI."""

    def closestCut(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation which is full spin multiples of this one and comes closest to target."""

    def closestSolution(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the equivalent rotation which comes closest to a target."""

    def computeAlternateSolution(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation which is not simply a multiple."""

    def computeBound(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an equivalent rotation with each rotation component bound within +/- PI."""

    def computeClosestCut(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation which is full spin multiples of the src and comes closest to target."""

    def computeClosestSolution(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the equivalent rotation which comes closest to a target."""

    def decompose(self, *args: Any, **kwargs: Any) -> Any:
        """Extracts a rotation from a matrix."""

    def incrementalRotateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Increase this rotation by a given angle around the specified axis. The update is done in series of small increments to avoid flipping."""

    def inverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new MEulerRotation containing the inverse rotation of this one and reversed rotation order."""

    def invertIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place inversion of the rotation. Rotation order is also reversed."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if this rotation has the same order as another and their X, Y and Z components are within a tolerance of each other."""

    def isZero(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the X, Y and Z components are each within a tolerance of 0.0."""

    kIdentity: MEulerRotation = (0, 0, 0, kXYZ)
    kTolerance: float = 1e-10
    kXYZ: int = 0
    kXZY: int = 3
    kYXZ: int = 4
    kYZX: int = 1
    kZXY: int = 2
    kZYX: int = 5
    order: getset_descriptor = <attribute 'order' of 'OpenMaya.MEulerRotation' objects>
    def reorder(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new MEulerRotation having this rotation, reordered to use the given rotation order."""

    def reorderIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place reordering to use the given rotation order."""

    def setToAlternateSolution(self, *args: Any, **kwargs: Any) -> Any:
        """Replace this rotation with an alternate solution."""

    def setToClosestCut(self, *args: Any, **kwargs: Any) -> Any:
        """Replace this rotation with the closest cut to a target."""

    def setToClosestSolution(self, *args: Any, **kwargs: Any) -> Any:
        """Replace this rotation with the closest solution to a target."""

    def setValue(self, *args: Any, **kwargs: Any) -> Any:
        """Set the rotation."""

    x: getset_descriptor = <attribute 'x' of 'OpenMaya.MEulerRotation' objects>
    y: getset_descriptor = <attribute 'y' of 'OpenMaya.MEulerRotation' objects>
    z: getset_descriptor = <attribute 'z' of 'OpenMaya.MEulerRotation' objects>

class MEvaluationNode(object):
    """A class providing access to Evaluation Manager node information."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def datablock(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the datablock for this node."""

    def dependencyNode(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the dependency node this evaluation node represents."""

    def dirtyPlug(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the top-most plug for the specified attribute if the attribute has dirty plugs. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to access a networked plug which is going to be dirty and computed."""

    def dirtyPlugExists(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the specified attribute has a dirty plug. This call should be made from MPxNode::preEvaluation() and MPxNode::postEvaluation() to verify which plugs are going to be dirty and computed."""

    def iterator(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an iterator at the beginning of the dirty plug list."""


class MEvaluationNodeIterator(object):
    """A class providing access to the Evaluation Manager node dirty plug list."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """Checks to see if the iterator has reached the end of the iteration."""

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """Advances the iterator to the next position in the dirty plug list."""

    def plug(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the dirty plug at the current iterator position. Returns an empty plug if the iterator is illegal."""

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """Resets the iterator to the first position in the dirty plug list."""


class MEventMessage(MMessage):
    """Class used to register callbacks for event related messages.

    The first parameter passed to the add callback method is the name
    of the event that will trigger the callback.  The list of
    available event names can be retrieved by calling the
    getEventNames method or by using the -listEvents flag on the
    scriptJob command.
    The addEventCallback method returns an id which is used to remove the
    callback.

    To remove a callback use OpenMaya.MMessage.removeCallback.

    All callbacks that are registered by a plug-in must be removed by
    that plug-in when it is unloaded.  Failure to do so will result in
    a fatal error.

    Idle event callbacks should be removed immediately after running.
    Otherwise they will continue to use up CPU resources. They will also
    prevent idleVeryLow event callbacks from running - which are required
    for Maya to function properly.
    """
    def addEventCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def getEventNames(self, *args: Any, **kwargs: Any) -> Any:
        """getEventNames() -> (string, string, ...)

        This method returns the list of available event names.

         * return: tuple of available event names.
        """


class MExternalContentInfoTable(object):
    """This is a table of all the external content for a given node."""
    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addResolvedEntry(self, *args: Any, **kwargs: Any) -> Any:
        """addResolvedEntry(key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles) -> self

        Add an entry in the table.

        * key (string) - An arbitrary string defined by the caller. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.
        * unresolvedLocation (string) - Path as stored in the node (i.e. without any token replacement performed).
        * resolvedLocation (string) - Full path to the content if it exists at the time of creation of this object.
        * contextNodeFullName (string) - The fullname of the URI owner (node) if it applies, an empty string otherwise.
        * roles (list of strings) - An enumeration of all roles this content plays in the context of the node. The actual strings are not rigidly defined as of this writing. This is mostly for offline browsing of the content info: to assist in sorting content by role.  A better content type system may be introduced later on to        formalize this.
        """

    def addUnresolvedEntry(self, *args: Any, **kwargs: Any) -> Any:
        """addUnresolvedEntry(key, unresolvedLocation, contextNodeFullName, roles=None) -> self

        Add an entry in the table. The resolved location will be inferred from the application's built-in file resolving for the specified file type. This will automatically add entries into the roles vector that correspond to the search rules for this file type.

        * key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * unresolvedLocation (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * contextNodeFullName (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        * roles (list of strings) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        """

    def getEntry(self, *args: Any, **kwargs: Any) -> Any:
        """getEntry(index) -> [key, unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

        Retrieves external content entry based on its position in the table.

        * index (unsigned int) - Position of the entry to retrieve information from.
        """

    def getInfo(self, *args: Any, **kwargs: Any) -> Any:
        """getInfo(key) -> [unresolvedLocation, resolvedLocation, contextNodeFullName, roles]

        Retrieves external content information based on its key.

        * key (string) - See documentation of MExternalContentInfoTable.addResolvedEntry().
        """


class MExternalContentLocationTable(object):
    """This is a table of the all the external content locations for a given node."""
    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addEntry(self, *args: Any, **kwargs: Any) -> Any:
        """addEntry(key, location) -> self

        Adds an external content location and its key to the table.

        * key (string) - An arbitrary string defined by the node. This will typically be an attribute name for situations where the content location is stored verbatim in a plug's value.* location (string) - Full path to the content referenced by the key.
        """

    def getEntry(self, *args: Any, **kwargs: Any) -> Any:
        """getEntry(index) -> [key, location]

        Retrieves external content entry based on its position in the table.

        * index (unsigned int) - Position of the entry to retrieve information from.
        """

    def getLocation(self, *args: Any, **kwargs: Any) -> Any:
        """getLocation(key) -> string

        Retrieves an entry's location based on the associated key.

        * key (string) - See documentation of MExternalContentLocationTable.addEntry().
        """


class MFileObject(object):
    """Manipulate filenames and search paths."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source file object.

        * source (MFileObject) - The source file object to copy from
        """

    def exists(self, *args: Any, **kwargs: Any) -> Any:
        """exists(index=None) -> bool

        Checks to see if the file exists and is readable.
        If index is None tests for the fullName file, else tests the file constructed from the indicated portion of the path element and filename element.

        * index (int) - Index of the path element to be used in searching for the file.
        """

    def expandedFullName(self, *args: Any, **kwargs: Any) -> Any:
        """expandedFullName() -> string

        Returns the pathname of a file constructed from the unresolved file object values. The file name will consist of the the expanded raw path and raw name elements.
        All variables in the path element are expanded, and the first path (the part before the first separator (':') in the path) is prepended to the filename element to construct the fullName.

        After expanding environment variables Maya may perform additional modifications to the full file name in order to resolve it to a valid location on disk. This resolved full file name can be accessed through resolvedFullName().
        """

    def expandedPath(self, *args: Any, **kwargs: Any) -> Any:
        """expandedPath() -> string

        Returns the raw path element of the unresolved file object with all environment variables expanded. In the case that the path expands to multiple paths, the first expanded path will be returned.

        After expanding environment variables Maya may perform additional modifications to the path in order to resolve it to a valid location on disk. This resolved path can be accessed through resolvedPath().
        """

    def fullName(self, *args: Any, **kwargs: Any) -> Any:
        """fullName(index) -> string

        Returns the pathname of a file constructed from the indicated portion of the path element and filename element.
        All variables in the path element are expanded, and the indicated path portion is prepended to the filename element to construct the fullName.

        * index (int) - the index of the desired path portion.
        """

    def getResolvedFullName(self, *args: Any, **kwargs: Any) -> Any:
        """getResolvedFullName(rawFullName) -> string

        Returns the full path to the resolved file, or an empty string if the resolution was unsuccessful.

        * rawFullName (string) - The fully specified unresolved path.
        """

    def getResolvedFullNameAndExistsStatus(self, *args: Any, **kwargs: Any) -> Any:
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

    def isAbsolutePath(self, *args: Any, **kwargs: Any) -> Any:
        """isAbsolutePath(fileName) -> bool

        Checks a file path string and determines if it represents an absolute file path. An absolute path can uniquely identify a directory or file.

        * fileName (string) - the string used to check if it is absolute
        """

    def isSet(self, *args: Any, **kwargs: Any) -> Any:
        """isSet() -> bool

        Checks to see if both file and path elements of the file object have been set.
        """

    kBaseName: int = 32
    kDirMap: int = 4
    kExact: int = 2
    kInputFile: int = 54
    kInputReference: int = 62
    kNone: int = 1
    kReferenceMappings: int = 8
    kRelative: int = 16
    kStrict: int = 6
    def overrideResolvedFullName(self, *args: Any, **kwargs: Any) -> Any:
        """overrideResolvedFullName(fullFileName, reresolveType=False) -> self

        Normally when a raw file name is set, Maya will perform a series of operations on it in an attempt to resolve it to a valid file name. This final resolved file name can be accessed through the resolvedName(), resolvedPath(), and resolvedFullFileName() methods and can be quite different from the originally specified raw file name.

        This method will override the normal Maya path resolution process and explicitly set the resolved file name. This path does not have to be a valid file path, but if any '/' characters appear in the given name then the resolved path element of the file object is set to everything in name up to, but not including the last '/'. The resolved filename is set to the part of name after the final '/'.

        Once the resolved file name is set, it is only guaranteed to be retained in the file object so long as the raw file path is not updated. Once the rawPath, rawName or rawFullName are set, the normal Maya path resolution process will be re-invoked and the resolved path and filename will be updated.

        - fullFileName (string) - the string used to override the path and filename.- reresolveType (bool) - if Maya should re-resolve the file type/translator.
        """

    def path(self, *args: Any, **kwargs: Any) -> Any:
        """path(index) -> string

        Returns the indicated portion of the path element of the file object.  All variables in the path element are expanded, and the portion indicated by the argument is extracted and returned.

        * index (int) - the index of the desired path portion.
        """

    def pathCount(self, *args: Any, **kwargs: Any) -> Any:
        """pathCount() -> int

        Returns the number of paths in the path element of the file object.
        This will be equal to one more than the number of ':' characters specified of the rawPath attribute.
        """

    def rawFullName(self, *args: Any, **kwargs: Any) -> Any:
        """rawFullName() -> string

        Returns the unresolved full file name (path plus filename) of the MFileObject with all environment variables unexpanded.

        This method differs from expandedFullName() in that it returns the unexpanded instead of expanded values.
        """

    def rawName(self, *args: Any, **kwargs: Any) -> Any:
        """rawName() -> string

        Returns the unresolved filename element of the MFileObject.
        """

    def rawPath(self, *args: Any, **kwargs: Any) -> Any:
        """rawPath() -> string

        Returns the path element of the MFileObject with all environment variables unexpanded.
        """

    def rawURI(self, *args: Any, **kwargs: Any) -> Any:
        """rawURI() -> MURI

        Returns the unresolved URI of the MFileObject, if any.

        This will be empty if the MFileObject was not resolved from a URI.
        """

    resolveMethod: getset_descriptor = <attribute 'resolveMethod' of 'OpenMaya.MFileObject' objects>
    def resolvedFullName(self, *args: Any, **kwargs: Any) -> Any:
        """resolvedFullName() -> string

        Returns the first pathname of a file constructed from the path and filename elements.  All variables in the path element are expanded, and the first path (the part before the first ':' in the path) is prepended to the filename element. After expanding all environment     variables Maya may then perform additional modifications, such  as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.

        The resolution is performed using the ResolveMethod of the file object.
        By default, this will be set to kNone. While this is suitable in many situations, it may not be appropriate if the file is expected to exist.
        Refer to getResolvedFullNameAndExistsStatus() for more information about how the  resolution mode is used.

        Failure to resolve the path according to the specifications of the file object will result in an empty return value.
        """

    def resolvedName(self, *args: Any, **kwargs: Any) -> Any:
        """resolvedName() -> string

        Returns the resolved filename element of the file object.
        """

    def resolvedPath(self, *args: Any, **kwargs: Any) -> Any:
        """resolvedPath() -> string

        Returns the resolved path element of the file object. In order to build the resolved path, Maya first expands all environment variables and then may perform additional modifications, such as prepending directories to a relative path name, in order to resolve the path to a valid location on disk.
        """

    def setRawFullName(self, *args: Any, **kwargs: Any) -> Any:
        """setRawFullName(fullFileName) -> self

        This method combines the functions of the setRawName and setRawPath methods in that it sets both the path and filename from the given name.

        If any '/' characters appear in the given name then the path element of the MFileObject is set to everything in name up to, but not including the last '/'.  The filename is set to the part of name after the final '/'.

        If no '/' characters appear in the given name then the path element is set to "." and the filename is set to the given name.

        Note that if the specified fullFileName is relative, contains environment variables, or does not exist, the full names returned by resolvedFullName() and expandedFullName() may not match the fullFileName. See the description of resolvedFullName() and expandedFullName() for more information.

        Also note that for URI-based file paths (e.g. "arrow:uri_path_to_file"),  setRawFullName will not call setRawName and setRawPath (raw name and path will remain empty). Use resolvedName and resolvedPath to retrieve the resolved file path, or rawFullName to retrieve the unresolved file path.

        * fullFileName (string) - The string used to initialize the path and filename.
        """

    def setRawName(self, *args: Any, **kwargs: Any) -> Any:
        """setRawName(fileName) -> self

        Set the unresolved filename element of the MFileObject instance.  This name should not contain any '/' characters, it should indicate simply the name of a file.  The directories in which this name will be searched for are specified by setRawPath.

        * fileName (string) - The filename to set.
        """

    def setRawPath(self, *args: Any, **kwargs: Any) -> Any:
        """setRawPath(pathName) -> self

        Set the unresolved path element of the MFileObject instance.  This should contain a list of directories, each separated by a single ':' character.  The pathnames can contain Unix environment variables in the form $VARNAME.  These will be expanded when paths to actual filenames are constructed.

        Note that if the specified pathName is relative, contains environment variables, or does not exist, the paths returned by resolvedPath() and expandedPath() may not match the rawPath. See the description of resolvedPath() and expandedPath() for more information.

        * pathName (string) - The path string.
        """

    def setRawURI(self, *args: Any, **kwargs: Any) -> Any:
        """setRawURI(uri) -> self

        Set the unresolved URI of the MFileObject instance.

        * uri (string or MURI) - The unresolved URI.
        """


class MFloatArray(object):
    """Array of float values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MFloatArray' objects>

class MFloatMatrix(object):
    """4x4 matrix with single-precision elements."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def adjoint(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's adjoint."""

    def det3x3(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""

    def det4x4(self, *args: Any, **kwargs: Any) -> Any:
        """Returns this matrix's determinant."""

    def getElement(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix element for the specified row and column."""

    def homogenize(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing the homogenized version of this matrix."""

    def inverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's inverse."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two matrices, within a tolerance."""

    kTolerance: float = 9.999999747378752e-06
    def setElement(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the matrix element for the specified row and column."""

    def setToIdentity(self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the identity."""

    def setToProduct(self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the product of the two matrices passed in."""

    def transpose(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's transpose."""


class MFloatPoint(object):
    """3D point with single-precision coordinates."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __rtruediv__(self, value) -> Any:
        """Return value/self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def __truediv__(self, value) -> Any:
        """Return self/value."""

    def cartesianize(self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to cartesian form."""

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        """Return distance between this point and another."""

    def homogenize(self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to homogenous form."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two points, within a tolerance."""

    kOrigin: MFloatPoint = (0, 0, 0, 1)
    kTolerance: float = 9.999999747378752e-06
    def rationalize(self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to rational form."""

    w: getset_descriptor = <attribute 'w' of 'OpenMaya.MFloatPoint' objects>
    x: getset_descriptor = <attribute 'x' of 'OpenMaya.MFloatPoint' objects>
    y: getset_descriptor = <attribute 'y' of 'OpenMaya.MFloatPoint' objects>
    z: getset_descriptor = <attribute 'z' of 'OpenMaya.MFloatPoint' objects>

class MFloatPointArray(object):
    """Array of MFloatPoint values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MFloatPointArray' objects>

class MFloatVector(object):
    """3D vector with single-precision coordinates."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __itruediv__(self, value) -> Any:
        """Return self/=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __neg__(self) -> Any:
        """-self"""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __rtruediv__(self, value) -> Any:
        """Return value/self."""

    def __rxor__(self, value) -> Any:
        """Return value^self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def __truediv__(self, value) -> Any:
        """Return self/value."""

    def __xor__(self, value) -> Any:
        """Return self^value."""

    def angle(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angle, in radians, between this vector and another."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within a given tolerance of being equal."""

    def isParallel(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within the given tolerance of being parallel."""

    kOneVector: MFloatVector = (1, 1, 1)
    kTolerance: float = 9.999999747378752e-06
    kXaxisVector: MFloatVector = (1, 0, 0)
    kXnegAxisVector: MFloatVector = (-1, 0, 0)
    kYaxisVector: MFloatVector = (0, 1, 0)
    kYnegAxisVector: MFloatVector = (0, -1, 0)
    kZaxisVector: MFloatVector = (0, 0, 1)
    kZeroVector: MFloatVector = (0, 0, 0)
    kZnegAxisVector: MFloatVector = (0, 0, -1)
    def length(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the magnitude of this vector."""

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector containing the normalized version of this one."""

    def normalize(self, *args: Any, **kwargs: Any) -> Any:
        """Normalizes this vector in-place and returns a new reference to it."""

    def transformAsNormal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix and then normalizing the result."""

    x: getset_descriptor = <attribute 'x' of 'OpenMaya.MFloatVector' objects>
    y: getset_descriptor = <attribute 'y' of 'OpenMaya.MFloatVector' objects>
    z: getset_descriptor = <attribute 'z' of 'OpenMaya.MFloatVector' objects>

class MFloatVectorArray(object):
    """Array of MFloatVector values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MFloatVectorArray' objects>

class MFn(object):
    """Static class providing constants for all API types."""
    kAISEnvFacade: int = 977
    kAddDoubleLinear: int = 5
    kAdskMaterial: int = 1067
    kAffect: int = 6
    kAimConstraint: int = 111
    kAimMatrix: int = 1139
    kAir: int = 257
    kAlignCurve: int = 41
    kAlignManip: int = 912
    kAlignSurface: int = 42
    kAmbientLight: int = 303
    kAngle: int = 270
    kAngleBetween: int = 21
    kAnimBlend: int = 794
    kAnimBlendInOut: int = 795
    kAnimCurve: int = 7
    kAnimCurveTimeToAngular: int = 8
    kAnimCurveTimeToDistance: int = 9
    kAnimCurveTimeToTime: int = 10
    kAnimCurveTimeToUnitless: int = 11
    kAnimCurveUnitlessToAngular: int = 12
    kAnimCurveUnitlessToDistance: int = 13
    kAnimCurveUnitlessToTime: int = 14
    kAnimCurveUnitlessToUnitless: int = 15
    kAnimLayer: int = 1020
    kAnisotropy: int = 622
    kAnnotation: int = 271
    kAnyGeometryVarGroup: int = 115
    kArcLength: int = 273
    kAreaLight: int = 305
    kArrayMapper: int = 528
    kArrowManip: int = 123
    kArubaTesselate: int = 1132
    kAssembly: int = 1081
    kAsset: int = 1018
    kAttachCurve: int = 43
    kAttachSurface: int = 44
    kAttribute: int = 565
    kAttribute2Double: int = 747
    kAttribute2Float: int = 748
    kAttribute2Int: int = 750
    kAttribute2Short: int = 749
    kAttribute3Double: int = 751
    kAttribute3Float: int = 752
    kAttribute3Int: int = 754
    kAttribute3Short: int = 753
    kAttribute4Double: int = 880
    kAudio: int = 22
    kAverageCurveManip: int = 149
    kAvgCurves: int = 45
    kAvgNurbsSurfacePoints: int = 47
    kAvgSurfacePoints: int = 46
    kAxesActionManip: int = 124
    kBackground: int = 23
    kBallProjectionManip: int = 125
    kBarnDoorManip: int = 150
    kBase: int = 1
    kBaseLattice: int = 249
    kBendLattice: int = 335
    kBevel: int = 48
    kBevelManip: int = 151
    kBevelPlus: int = 899
    kBezierCurve: int = 1054
    kBezierCurveData: int = 1055
    kBezierCurveToNurbs: int = 1057
    kBinaryData: int = 746
    kBirailSrf: int = 49
    kBlend: int = 27
    kBlendColorSet: int = 739
    kBlendColors: int = 31
    kBlendDevice: int = 30
    kBlendFalloff: int = 1141
    kBlendManip: int = 152
    kBlendMatrix: int = 1137
    kBlendNodeAdditiveRotation: int = 1033
    kBlendNodeAdditiveScale: int = 1032
    kBlendNodeBase: int = 1021
    kBlendNodeBoolean: int = 1022
    kBlendNodeDouble: int = 1023
    kBlendNodeDoubleAngle: int = 1024
    kBlendNodeDoubleLinear: int = 1025
    kBlendNodeEnum: int = 1026
    kBlendNodeFloat: int = 1027
    kBlendNodeFloatAngle: int = 1028
    kBlendNodeFloatLinear: int = 1029
    kBlendNodeInt16: int = 1030
    kBlendNodeInt32: int = 1031
    kBlendNodeTime: int = 1052
    kBlendShape: int = 336
    kBlendTwoAttr: int = 28
    kBlendWeighted: int = 29
    kBlindData: int = 756
    kBlindDataTemplate: int = 757
    kBlinn: int = 373
    kBlinnMaterial: int = 389
    kBoundary: int = 53
    kBox: int = 867
    kBoxData: int = 866
    kBrownian: int = 508
    kBrush: int = 765
    kBulge: int = 497
    kBulgeLattice: int = 338
    kBump: int = 32
    kBump3d: int = 33
    kButtonManip: int = 153
    kCacheBase: int = 999
    kCacheBlend: int = 1000
    kCacheFile: int = 987
    kCacheTrack: int = 1001
    kCacheableNode: int = 996
    kCaddyManipBase: int = 1110
    kCamera: int = 250
    kCameraManip: int = 154
    kCameraPlaneManip: int = 143
    kCameraSet: int = 1011
    kCameraView: int = 34
    kCenterManip: int = 134
    kChainToSpline: int = 35
    kCharacter: int = 688
    kCharacterMap: int = 803
    kCharacterMappingData: int = 742
    kCharacterOffset: int = 689
    kChecker: int = 498
    kChoice: int = 36
    kChooser: int = 772
    kCircle: int = 54
    kCircleManip: int = 126
    kCirclePointManip: int = 231
    kCircleSweepManip: int = 128
    kClampColor: int = 39
    kClientDevice: int = 1077
    kClip: int = 809
    kClipGhostShape: int = 1082
    kClipLibrary: int = 780
    kClipScheduler: int = 779
    kClipToGhostData: int = 1083
    kCloseCurve: int = 55
    kCloseSurface: int = 57
    kClosestPointOnMesh: int = 989
    kClosestPointOnSurface: int = 56
    kCloth: int = 499
    kCloud: int = 509
    kCluster: int = 251
    kClusterFilter: int = 347
    kClusterFlexor: int = 300
    kCoiManip: int = 155
    kCollision: int = 253
    kColorBackground: int = 24
    kColorMgtGlobals: int = 1101
    kColorProfile: int = 1066
    kCombinationShape: int = 337
    kCommCornerManip: int = 613
    kCommCornerOperManip: int = 614
    kCommEdgeOperManip: int = 611
    kCommEdgePtManip: int = 610
    kCommEdgeSegmentManip: int = 612
    kComponent: int = 535
    kComponentFalloff: int = 1144
    kComponentListData: int = 583
    kComponentManip: int = 674
    kComponentMatch: int = 1149
    kComposeMatrix: int = 1136
    kCompoundAttribute: int = 575
    kConcentricProjectionManip: int = 129
    kCondition: int = 37
    kCone: int = 96
    kConstraint: int = 932
    kContainer: int = 1013
    kContainerBase: int = 1068
    kContourProjectionManip: int = 1115
    kContrast: int = 38
    kControl: int = 486
    kControllerTag: int = 1128
    kCopyColorSet: int = 738
    kCopyUVSet: int = 807
    kCpManip: int = 156
    kCrater: int = 510
    kCreaseSet: int = 1090
    kCreate: int = 40
    kCreateBPManip: int = 837
    kCreateBezierManip: int = 1053
    kCreateCVManip: int = 157
    kCreateColorSet: int = 736
    kCreateEPManip: int = 158
    kCreateSectionManip: int = 824
    kCreateUVSet: int = 808
    kCrossSectionEditManip: int = 825
    kCrossSectionManager: int = 823
    kCubicProjectionManip: int = 130
    kCurve: int = 266
    kCurveCVComponent: int = 536
    kCurveCurveIntersect: int = 641
    kCurveEPComponent: int = 537
    kCurveEdManip: int = 159
    kCurveFromMeshCoM: int = 934
    kCurveFromMeshEdge: int = 640
    kCurveFromSubdivEdge: int = 836
    kCurveFromSubdivFace: int = 842
    kCurveFromSurface: int = 58
    kCurveFromSurfaceBnd: int = 59
    kCurveFromSurfaceCoS: int = 60
    kCurveFromSurfaceIso: int = 61
    kCurveInfo: int = 62
    kCurveKnotComponent: int = 538
    kCurveNormalizerAngle: int = 1003
    kCurveNormalizerLinear: int = 1004
    kCurveParamComponent: int = 539
    kCurveSegmentManip: int = 160
    kCurveVarGroup: int = 116
    kCustomEvaluatorClusterNode: int = 1130
    kCylinder: int = 98
    kCylindricalProjectionManip: int = 131
    kDOF: int = 323
    kDPbirailSrf: int = 50
    kDagContainer: int = 1069
    kDagNode: int = 107
    kDagPose: int = 690
    kDagSelectionItem: int = 562
    kData: int = 582
    kData2Double: int = 593
    kData2Float: int = 594
    kData2Int: int = 595
    kData2Short: int = 596
    kData3Double: int = 597
    kData3Float: int = 598
    kData3Int: int = 599
    kData3Short: int = 600
    kData4Double: int = 881
    kDblTrsManip: int = 190
    kDecayRegionCapComponent: int = 548
    kDecayRegionComponent: int = 549
    kDecomposeMatrix: int = 1135
    kDefaultLightList: int = 317
    kDeformBend: int = 625
    kDeformBendManip: int = 631
    kDeformFlare: int = 628
    kDeformFlareManip: int = 634
    kDeformFunc: int = 624
    kDeformSine: int = 629
    kDeformSineManip: int = 635
    kDeformSquash: int = 627
    kDeformSquashManip: int = 633
    kDeformTwist: int = 626
    kDeformTwistManip: int = 632
    kDeformWave: int = 630
    kDeformWaveManip: int = 636
    kDeleteColorSet: int = 737
    kDeleteComponent: int = 318
    kDeleteUVSet: int = 800
    kDeltaMush: int = 350
    kDependencyNode: int = 4
    kDetachCurve: int = 63
    kDetachSurface: int = 64
    kDiffuseMaterial: int = 387
    kDimension: int = 269
    kDimensionManip: int = 232
    kDirectedDisc: int = 276
    kDirectionManip: int = 161
    kDirectionalLight: int = 308
    kDiscManip: int = 132
    kDiskCache: int = 863
    kDispatchCompute: int = 319
    kDisplacementShader: int = 321
    kDisplayLayer: int = 733
    kDisplayLayerManager: int = 734
    kDistance: int = 272
    kDistanceBetween: int = 322
    kDistanceManip: int = 638
    kDofManip: int = 162
    kDoubleAngleAttribute: int = 567
    kDoubleArrayData: int = 584
    kDoubleIndexedComponent: int = 714
    kDoubleLinearAttribute: int = 569
    kDoubleShadingSwitch: int = 619
    kDrag: int = 258
    kDropOffFunction: int = 826
    kDropoffLocator: int = 282
    kDropoffManip: int = 163
    kDummy: int = 254
    kDummyConnectable: int = 324
    kDynAirManip: int = 724
    kDynArrayAttrsData: int = 729
    kDynAttenuationManip: int = 728
    kDynBase: int = 720
    kDynBaseFieldManip: int = 723
    kDynEmitterManip: int = 721
    kDynFieldsManip: int = 722
    kDynGlobals: int = 769
    kDynNewtonManip: int = 725
    kDynParticleSetComponent: int = 560
    kDynSpreadManip: int = 727
    kDynSweptGeometryData: int = 743
    kDynTurbulenceManip: int = 726
    kDynamicConstraint: int = 993
    kDynamicsController: int = 325
    kEdgeComponent: int = 545
    kEditCurve: int = 821
    kEditCurveManip: int = 822
    kEditMetadata: int = 1089
    kEditsManager: int = 1097
    kEmitter: int = 255
    kEnableManip: int = 136
    kEnumAttribute: int = 572
    kEnvBall: int = 491
    kEnvChrome: int = 493
    kEnvCube: int = 492
    kEnvFacade: int = 976
    kEnvFogMaterial: int = 381
    kEnvFogShape: int = 278
    kEnvSky: int = 494
    kEnvSphere: int = 495
    kExplodeNurbsShell: int = 692
    kExpression: int = 327
    kExtendCurve: int = 65
    kExtendCurveDistanceManip: int = 164
    kExtendSurface: int = 66
    kExtendSurfaceDistanceManip: int = 716
    kExtract: int = 328
    kExtrude: int = 67
    kExtrudeManip: int = 165
    kFFD: int = 339
    kFFblendSrf: int = 68
    kFFfilletSrf: int = 69
    kFacade: int = 974
    kFalloffEval: int = 1148
    kFfdDualBase: int = 340
    kField: int = 256
    kFileBackground: int = 25
    kFileTexture: int = 500
    kFilletCurve: int = 70
    kFilter: int = 329
    kFilterClosestSample: int = 330
    kFilterEuler: int = 331
    kFilterSimplify: int = 332
    kFitBspline: int = 71
    kFixedLineManip: int = 233
    kFlexor: int = 299
    kFloatAngleAttribute: int = 568
    kFloatArrayData: int = 1037
    kFloatLinearAttribute: int = 570
    kFloatMatrixAttribute: int = 579
    kFloatVectorArrayData: int = 1014
    kFlow: int = 72
    kFluid: int = 914
    kFluidData: int = 916
    kFluidEmitter: int = 920
    kFluidGeom: int = 915
    kFluidTexture2D: int = 909
    kFluidTexture3D: int = 908
    kFollicle: int = 935
    kForceUpdateManip: int = 695
    kFosterParent: int = 1092
    kFourByFourMatrix: int = 775
    kFractal: int = 501
    kFreePointManip: int = 133
    kFreePointTriadManip: int = 137
    kGammaCorrect: int = 333
    kGenericAttribute: int = 576
    kGeoConnectable: int = 326
    kGeoConnector: int = 922
    kGeomBind: int = 1100
    kGeometric: int = 265
    kGeometryConstraint: int = 113
    kGeometryData: int = 712
    kGeometryFilt: int = 334
    kGeometryOnLineManip: int = 142
    kGeometryVarGroup: int = 114
    kGlobalCacheControls: int = 862
    kGlobalStitch: int = 701
    kGranite: int = 511
    kGravity: int = 259
    kGreasePencilSequence: int = 1088
    kGreasePlane: int = 1086
    kGreasePlaneRenderShape: int = 1087
    kGrid: int = 502
    kGroundPlane: int = 290
    kGroupId: int = 356
    kGroupParts: int = 357
    kGuide: int = 358
    kGuideLine: int = 301
    kHairConstraint: int = 940
    kHairSystem: int = 936
    kHairTubeShader: int = 947
    kHandleRotateManip: int = 216
    kHardenPointCurve: int = 73
    kHardwareReflectionMap: int = 886
    kHardwareRenderGlobals: int = 527
    kHardwareRenderingGlobals: int = 1071
    kHeightField: int = 921
    kHikEffector: int = 961
    kHikFKJoint: int = 963
    kHikFloorContactMarker: int = 983
    kHikGroundPlane: int = 984
    kHikHandle: int = 965
    kHikIKEffector: int = 962
    kHikSolver: int = 964
    kHistorySwitch: int = 988
    kHsvToRgb: int = 359
    kHwShaderNode: int = 889
    kHyperGraphInfo: int = 360
    kHyperLayout: int = 361
    kHyperLayoutDG: int = 1005
    kHyperView: int = 362
    kIkEffector: int = 119
    kIkHandle: int = 120
    kIkRPManip: int = 167
    kIkSolver: int = 363
    kIkSplineManip: int = 166
    kIkSystem: int = 369
    kIllustratorCurve: int = 74
    kImageAdd: int = 659
    kImageBlur: int = 665
    kImageColorCorrect: int = 664
    kImageData: int = 653
    kImageDepth: int = 667
    kImageDiff: int = 660
    kImageDisplay: int = 668
    kImageFilter: int = 666
    kImageLoad: int = 654
    kImageMotionBlur: int = 670
    kImageMultiply: int = 661
    kImageNetDest: int = 657
    kImageNetSrc: int = 656
    kImageOver: int = 662
    kImagePlane: int = 370
    kImageRender: int = 658
    kImageSave: int = 655
    kImageSource: int = 791
    kImageUnder: int = 663
    kImageView: int = 669
    kImplicitCone: int = 894
    kImplicitSphere: int = 895
    kInsertKnotCrv: int = 75
    kInsertKnotSrf: int = 76
    kInstancer: int = 762
    kInt64ArrayData: int = 814
    kIntArrayData: int = 585
    kIntersectSurface: int = 77
    kInvalid: int = 0
    kIsoparmComponent: int = 540
    kIsoparmManip: int = 146
    kItemList: int = 564
    kJiggleDeformer: int = 861
    kJoint: int = 121
    kJointCluster: int = 349
    kJointClusterManip: int = 168
    kJointTranslateManip: int = 229
    kKeyframeDelta: int = 949
    kKeyframeDeltaAddRemove: int = 952
    kKeyframeDeltaBlockAddRemove: int = 953
    kKeyframeDeltaBreakdown: int = 957
    kKeyframeDeltaInfType: int = 954
    kKeyframeDeltaMove: int = 950
    kKeyframeDeltaScale: int = 951
    kKeyframeDeltaTangent: int = 955
    kKeyframeDeltaWeighted: int = 956
    kKeyframeRegionManip: int = 1002
    kKeyingGroup: int = 687
    kLambert: int = 371
    kLambertMaterial: int = 388
    kLattice: int = 279
    kLatticeComponent: int = 546
    kLatticeData: int = 587
    kLatticeGeom: int = 280
    kLayeredShader: int = 376
    kLayeredTexture: int = 804
    kLeastSquares: int = 379
    kLeather: int = 512
    kLight: int = 302
    kLightDataAttribute: int = 577
    kLightFogMaterial: int = 380
    kLightInfo: int = 378
    kLightLink: int = 768
    kLightList: int = 382
    kLightManip: int = 169
    kLightProjectionGeometry: int = 234
    kLightSource: int = 383
    kLightSourceMaterial: int = 391
    kLimitManip: int = 135
    kLineArrowManip: int = 235
    kLineManip: int = 147
    kLineModifier: int = 978
    kLinearLight: int = 306
    kLocator: int = 281
    kLodGroup: int = 773
    kLodThresholds: int = 771
    kLookAt: int = 112
    kLuminance: int = 384
    kMCsolver: int = 364
    kMPbirailSrf: int = 51
    kMakeGroup: int = 385
    kMandelbrot: int = 1084
    kMandelbrot3D: int = 1085
    kManip2DContainer: int = 192
    kManipContainer: int = 148
    kManipulator: int = 230
    kManipulator2D: int = 205
    kManipulator3D: int = 122
    kMarble: int = 513
    kMarker: int = 283
    kMarkerManip: int = 210
    kMaterial: int = 386
    kMaterialFacade: int = 975
    kMaterialInfo: int = 392
    kMaterialTemplate: int = 393
    kMatrixAdd: int = 394
    kMatrixArrayData: int = 603
    kMatrixAttribute: int = 578
    kMatrixData: int = 588
    kMatrixFloatData: int = 672
    kMatrixHold: int = 395
    kMatrixMult: int = 396
    kMatrixPass: int = 397
    kMatrixWtAdd: int = 398
    kMembrane: int = 1038
    kMentalRayTexture: int = 942
    kMergeVertsToolManip: int = 1039
    kMesh: int = 296
    kMeshComponent: int = 550
    kMeshData: int = 589
    kMeshEdgeComponent: int = 551
    kMeshFaceVertComponent: int = 555
    kMeshFrEdgeComponent: int = 553
    kMeshGeom: int = 297
    kMeshMapComponent: int = 817
    kMeshPolygonComponent: int = 552
    kMeshVarGroup: int = 117
    kMeshVertComponent: int = 554
    kMeshVtxFaceComponent: int = 745
    kMessageAttribute: int = 580
    kMidModifier: int = 399
    kMidModifierWithMatrix: int = 400
    kModel: int = 3
    kModifyEdgeBaseManip: int = 838
    kModifyEdgeCrvManip: int = 829
    kModifyEdgeManip: int = 830
    kMorph: int = 352
    kMotionPath: int = 445
    kMotionPathManip: int = 170
    kMountain: int = 503
    kMoveUVShellManip2D: int = 710
    kMoveVertexManip: int = 763
    kMultDoubleLinear: int = 774
    kMultiSubVertexComponent: int = 558
    kMultilisterLight: int = 447
    kMultiplyDivide: int = 448
    kMute: int = 931
    kNBase: int = 998
    kNCloth: int = 1007
    kNComponent: int = 994
    kNId: int = 1036
    kNIdData: int = 1035
    kNLE: int = 1095
    kNObject: int = 1016
    kNObjectData: int = 1015
    kNParticle: int = 1008
    kNRigid: int = 1009
    kNamedObject: int = 2
    kNearestPointOnCurve: int = 1065
    kNewton: int = 260
    kNodeGraphEditorBookmarkInfo: int = 1118
    kNodeGraphEditorBookmarks: int = 1117
    kNodeGraphEditorInfo: int = 1116
    kNoise: int = 879
    kNonAmbientLight: int = 304
    kNonDagSelectionItem: int = 563
    kNonExtendedLight: int = 307
    kNonLinear: int = 623
    kNormalConstraint: int = 238
    kNucleus: int = 997
    kNumericAttribute: int = 566
    kNumericData: int = 592
    kNurbsBoolean: int = 693
    kNurbsCircular2PtArc: int = 643
    kNurbsCircular3PtArc: int = 642
    kNurbsCube: int = 80
    kNurbsCurve: int = 267
    kNurbsCurveData: int = 591
    kNurbsCurveGeom: int = 268
    kNurbsCurveToBezier: int = 1056
    kNurbsPlane: int = 79
    kNurbsSquare: int = 621
    kNurbsSurface: int = 294
    kNurbsSurfaceData: int = 590
    kNurbsSurfaceGeom: int = 295
    kNurbsTesselate: int = 78
    kNurbsToSubdiv: int = 760
    kObjectAttrFilter: int = 680
    kObjectBinFilter: int = 943
    kObjectFilter: int = 676
    kObjectMultiFilter: int = 677
    kObjectNameFilter: int = 678
    kObjectRenderFilter: int = 681
    kObjectScriptFilter: int = 682
    kObjectTypeFilter: int = 679
    kOcean: int = 875
    kOceanDeformer: int = 1126
    kOceanShader: int = 898
    kOffsetCos: int = 81
    kOffsetCosManip: int = 171
    kOffsetCurve: int = 82
    kOffsetCurveManip: int = 172
    kOffsetSurface: int = 644
    kOffsetSurfaceManip: int = 652
    kOldGeometryConstraint: int = 449
    kOpaqueAttribute: int = 1150
    kOpticalFX: int = 450
    kOrientConstraint: int = 239
    kOrientationComponent: int = 556
    kOrientationLocator: int = 286
    kOrientationMarker: int = 284
    kOrthoGrid: int = 291
    kPASolver: int = 365
    kPairBlend: int = 927
    kParamDimension: int = 275
    kParentConstraint: int = 242
    kParticle: int = 311
    kParticleAgeMapper: int = 451
    kParticleCloud: int = 452
    kParticleColorMapper: int = 453
    kParticleIncandecenceMapper: int = 454
    kParticleSamplerInfo: int = 806
    kParticleTransparencyMapper: int = 455
    kPartition: int = 456
    kPassContributionMap: int = 787
    kPfxGeometry: int = 945
    kPfxHair: int = 946
    kPfxToon: int = 971
    kPhong: int = 374
    kPhongExplorer: int = 375
    kPhongMaterial: int = 390
    kPickMatrix: int = 1138
    kPivotComponent: int = 541
    kPivotManip2D: int = 191
    kPlace2dTexture: int = 457
    kPlace3dTexture: int = 458
    kPlanarProjectionManip: int = 207
    kPlanarTrimSrf: int = 83
    kPlane: int = 288
    kPlugin: int = 581
    kPluginBlendShape: int = 1121
    kPluginCameraSet: int = 1012
    kPluginClientDevice: int = 1078
    kPluginConstraintNode: int = 1017
    kPluginData: int = 601
    kPluginDeformerNode: int = 615
    kPluginDependNode: int = 459
    kPluginEmitterNode: int = 731
    kPluginFieldNode: int = 730
    kPluginGeometryData: int = 767
    kPluginGeometryFilter: int = 1120
    kPluginHardwareShader: int = 890
    kPluginHwShaderNode: int = 891
    kPluginIkSolver: int = 761
    kPluginImagePlaneNode: int = 1006
    kPluginLocatorNode: int = 460
    kPluginManipContainer: int = 696
    kPluginManipulatorNode: int = 1034
    kPluginMotionPathNode: int = 446
    kPluginObjectSet: int = 924
    kPluginParticleAttributeMapperNode: int = 1010
    kPluginShape: int = 711
    kPluginSkinCluster: int = 1119
    kPluginSpringNode: int = 732
    kPluginThreadedDevice: int = 1079
    kPluginTransformNode: int = 913
    kPlusMinusAverage: int = 461
    kPointArrayData: int = 602
    kPointConstraint: int = 240
    kPointLight: int = 309
    kPointManip: int = 236
    kPointMatrixMult: int = 462
    kPointOnCurveInfo: int = 84
    kPointOnCurveManip: int = 208
    kPointOnLineManip: int = 211
    kPointOnPolyConstraint: int = 1060
    kPointOnSurfaceInfo: int = 85
    kPointOnSurfaceManip: int = 212
    kPoleVectorConstraint: int = 243
    kPolyAppend: int = 403
    kPolyAppendVertex: int = 796
    kPolyArrow: int = 979
    kPolyAutoProj: int = 851
    kPolyAutoProjManip: int = 967
    kPolyAverageVertex: int = 850
    kPolyBevel: int = 401
    kPolyBevel2: int = 1098
    kPolyBevel3: int = 1102
    kPolyBlindData: int = 758
    kPolyBoolOp: int = 617
    kPolyBridgeEdge: int = 995
    kPolyCBoolOp: int = 1099
    kPolyCaddyManip: int = 1111
    kPolyChipOff: int = 404
    kPolyCircularize: int = 1131
    kPolyClean: int = 1124
    kPolyCloseBorder: int = 405
    kPolyCollapseEdge: int = 406
    kPolyCollapseF: int = 407
    kPolyColorDel: int = 741
    kPolyColorMod: int = 740
    kPolyColorPerVertex: int = 735
    kPolyComponentData: int = 985
    kPolyCone: int = 437
    kPolyConnectComponents: int = 1061
    kPolyContourProj: int = 1114
    kPolyCreaseEdge: int = 959
    kPolyCreateFacet: int = 443
    kPolyCreateToolManip: int = 140
    kPolyCreator: int = 435
    kPolyCube: int = 438
    kPolyCut: int = 901
    kPolyCutManip: int = 905
    kPolyCutManipContainer: int = 904
    kPolyCylProj: int = 408
    kPolyCylinder: int = 439
    kPolyDelEdge: int = 409
    kPolyDelFacet: int = 410
    kPolyDelVertex: int = 411
    kPolyDuplicateEdge: int = 973
    kPolyEdgeToCurve: int = 1019
    kPolyEditEdgeFlow: int = 1091
    kPolyExtrudeEdge: int = 793
    kPolyExtrudeFacet: int = 412
    kPolyExtrudeManip: int = 1074
    kPolyExtrudeManipContainer: int = 1075
    kPolyExtrudeVertex: int = 926
    kPolyFlipEdge: int = 792
    kPolyFlipUV: int = 888
    kPolyHelix: int = 986
    kPolyHoleFace: int = 1059
    kPolyLayoutUV: int = 852
    kPolyMapCut: int = 413
    kPolyMapDel: int = 414
    kPolyMapSew: int = 415
    kPolyMapSewMove: int = 853
    kPolyMappingManip: int = 194
    kPolyMergeEdge: int = 416
    kPolyMergeFacet: int = 417
    kPolyMergeUV: int = 910
    kPolyMergeVert: int = 698
    kPolyMesh: int = 440
    kPolyMirror: int = 958
    kPolyMirrorManipContainer: int = 906
    kPolyModifierManip: int = 195
    kPolyModifierManipContainer: int = 1112
    kPolyMoveEdge: int = 418
    kPolyMoveFacet: int = 419
    kPolyMoveFacetUV: int = 420
    kPolyMoveUV: int = 421
    kPolyMoveUVManip: int = 193
    kPolyMoveVertex: int = 422
    kPolyMoveVertexManip: int = 196
    kPolyMoveVertexUV: int = 423
    kPolyNormal: int = 424
    kPolyNormalPerVertex: int = 759
    kPolyNormalizeUV: int = 887
    kPolyPassThru: int = 1122
    kPolyPinUV: int = 960
    kPolyPipe: int = 982
    kPolyPlanProj: int = 425
    kPolyPlatonicSolid: int = 981
    kPolyPoke: int = 902
    kPolyPokeManip: int = 907
    kPolyPrimitive: int = 436
    kPolyPrimitiveMisc: int = 980
    kPolyPrism: int = 968
    kPolyProj: int = 426
    kPolyProjectCurve: int = 1072
    kPolyProjectionManip: int = 174
    kPolyPyramid: int = 969
    kPolyQuad: int = 427
    kPolyReduce: int = 770
    kPolyRemesh: int = 1113
    kPolySelectEditFeedbackManip: int = 1042
    kPolySeparate: int = 463
    kPolySewEdge: int = 697
    kPolySmooth: int = 428
    kPolySmoothFacet: int = 699
    kPolySmoothProxy: int = 944
    kPolySoftEdge: int = 429
    kPolySphProj: int = 430
    kPolySphere: int = 441
    kPolySpinEdge: int = 1058
    kPolySplit: int = 431
    kPolySplitEdge: int = 815
    kPolySplitRing: int = 970
    kPolySplitToolManip: int = 141
    kPolySplitVert: int = 810
    kPolyStraightenUVBorder: int = 911
    kPolySubdEdge: int = 432
    kPolySubdFacet: int = 433
    kPolyToSubdiv: int = 685
    kPolyToolFeedbackManip: int = 1041
    kPolyToolFeedbackShape: int = 312
    kPolyTorus: int = 442
    kPolyTransfer: int = 849
    kPolyTriangulate: int = 434
    kPolyTweak: int = 402
    kPolyTweakUV: int = 709
    kPolyUVRectangle: int = 1070
    kPolyUnite: int = 444
    kPolyVertexNormalManip: int = 197
    kPolyWedgeFace: int = 903
    kPoseInterpolatorManager: int = 1127
    kPositionMarker: int = 285
    kPostProcessList: int = 464
    kPrecompExport: int = 788
    kPrimitive: int = 86
    kPrimitiveFalloff: int = 1140
    kProjectCurve: int = 87
    kProjectTangent: int = 88
    kProjectTangentManip: int = 177
    kProjection: int = 465
    kProjectionManip: int = 173
    kProjectionMultiManip: int = 176
    kProjectionUVManip: int = 175
    kPropModManip: int = 178
    kPropMoveTriadManip: int = 138
    kProximityFalloff: int = 1145
    kProximityPin: int = 991
    kProximityWrap: int = 354
    kProxy: int = 108
    kProxyManager: int = 966
    kPsdFileTexture: int = 948
    kQuadPtOnLineManip: int = 179
    kQuadShadingSwitch: int = 925
    kRBFsurface: int = 89
    kRPsolver: int = 367
    kRadial: int = 261
    kRadius: int = 274
    kRamp: int = 504
    kRampBackground: int = 26
    kRampShader: int = 896
    kRbfSrfManip: int = 180
    kReForm: int = 1129
    kRebuildCurve: int = 90
    kRebuildSurface: int = 91
    kRecord: int = 466
    kReference: int = 755
    kReflect: int = 372
    kRemapColor: int = 938
    kRemapHsv: int = 939
    kRemapValue: int = 937
    kRenderBox: int = 868
    kRenderCone: int = 97
    kRenderGlobals: int = 523
    kRenderGlobalsList: int = 524
    kRenderLayer: int = 785
    kRenderLayerManager: int = 786
    kRenderPass: int = 783
    kRenderPassSet: int = 784
    kRenderQuality: int = 525
    kRenderRect: int = 277
    kRenderSetup: int = 522
    kRenderSphere: int = 298
    kRenderTarget: int = 789
    kRenderUtilityList: int = 467
    kRenderedImageSource: int = 790
    kRenderingList: int = 1073
    kReorderUVSet: int = 1133
    kResolution: int = 526
    kResultCurve: int = 16
    kResultCurveTimeToAngular: int = 17
    kResultCurveTimeToDistance: int = 18
    kResultCurveTimeToTime: int = 19
    kResultCurveTimeToUnitless: int = 20
    kReverse: int = 468
    kReverseCrvManip: int = 182
    kReverseCurve: int = 92
    kReverseCurveManip: int = 181
    kReverseSurface: int = 93
    kReverseSurfaceManip: int = 183
    kRevolve: int = 94
    kRevolveManip: int = 184
    kRevolvedPrimitive: int = 95
    kRevolvedPrimitiveManip: int = 185
    kRgbToHsv: int = 469
    kRigid: int = 314
    kRigidConstraint: int = 313
    kRigidDeform: int = 341
    kRigidSolver: int = 470
    kRock: int = 514
    kRotateBoxManip: int = 214
    kRotateLimitsManip: int = 217
    kRotateManip: int = 215
    kRotateUVManip2D: int = 707
    kRoundConstantRadius: int = 645
    kRoundConstantRadiusManip: int = 648
    kRoundRadiusCrvManip: int = 647
    kRoundRadiusManip: int = 646
    kSCsolver: int = 366
    kSPbirailSrf: int = 52
    kSamplerInfo: int = 478
    kScaleConstraint: int = 244
    kScaleLimitsManip: int = 218
    kScaleManip: int = 219
    kScalePointManip: int = 831
    kScaleUVManip2D: int = 708
    kScalingBoxManip: int = 220
    kScreenAlignedCircleManip: int = 127
    kScript: int = 639
    kScriptManip: int = 221
    kSculpt: int = 342
    kSectionManip: int = 818
    kSelectionItem: int = 561
    kSelectionList: int = 608
    kSelectionListData: int = 675
    kSelectionListOperator: int = 683
    kSequenceManager: int = 1049
    kSequencer: int = 1050
    kSet: int = 471
    kSetGroupComponent: int = 559
    kSetRange: int = 474
    kSfRevolveManip: int = 841
    kShaderGlow: int = 475
    kShaderList: int = 476
    kShadingEngine: int = 320
    kShadingMap: int = 477
    kShape: int = 248
    kShapeEditorManager: int = 1125
    kShapeFragment: int = 479
    kShot: int = 1051
    kShrinkWrapFilter: int = 1096
    kSimpleVolumeShader: int = 480
    kSingleIndexedComponent: int = 713
    kSingleShadingSwitch: int = 618
    kSketchPlane: int = 289
    kSkin: int = 100
    kSkinBinding: int = 1062
    kSkinClusterFilter: int = 686
    kSkinShader: int = 673
    kSl60: int = 481
    kSmear: int = 917
    kSmoothCurve: int = 700
    kSmoothTangentSrf: int = 782
    kSnapUVManip2D: int = 1093
    kSnapshot: int = 482
    kSnapshotPath: int = 923
    kSnapshotShape: int = 859
    kSnow: int = 515
    kSoftMod: int = 252
    kSoftModFilter: int = 348
    kSoftModManip: int = 637
    kSolidFractal: int = 516
    kSolidify: int = 353
    kSphere: int = 99
    kSphereData: int = 604
    kSphericalProjectionManip: int = 222
    kSplineSolver: int = 368
    kSpotCylinderManip: int = 187
    kSpotLight: int = 310
    kSpotManip: int = 186
    kSpring: int = 315
    kSprite: int = 292
    kSquareSrf: int = 717
    kSquareSrfManip: int = 718
    kStandardSurface: int = 377
    kStateManip: int = 145
    kStencil: int = 505
    kStereoCameraMaster: int = 1048
    kStitchAsNurbsShell: int = 691
    kStitchSrf: int = 101
    kStitchSrfManip: int = 694
    kStoryBoard: int = 483
    kStringArrayData: int = 606
    kStringData: int = 605
    kStringShadingSwitch: int = 918
    kStroke: int = 764
    kStrokeGlobals: int = 766
    kStucco: int = 517
    kStudioClearCoat: int = 919
    kStyleCurve: int = 900
    kSubCurve: int = 102
    kSubSurface: int = 781
    kSubVertexComponent: int = 557
    kSubdAddTopology: int = 892
    kSubdAutoProj: int = 877
    kSubdBlindData: int = 802
    kSubdBoolean: int = 827
    kSubdCleanTopology: int = 893
    kSubdCloseBorder: int = 864
    kSubdDelFace: int = 858
    kSubdExtrudeFace: int = 839
    kSubdHierBlind: int = 801
    kSubdLayoutUV: int = 873
    kSubdMapCut: int = 872
    kSubdMapSewMove: int = 874
    kSubdMappingManip: int = 885
    kSubdMergeVert: int = 865
    kSubdModifier: int = 854
    kSubdModifyEdge: int = 828
    kSubdMoveEdge: int = 856
    kSubdMoveFace: int = 857
    kSubdMoveVertex: int = 855
    kSubdPlanProj: int = 882
    kSubdProjectionManip: int = 884
    kSubdSplitFace: int = 869
    kSubdSubdivideFace: int = 878
    kSubdTweak: int = 883
    kSubdTweakUV: int = 871
    kSubdiv: int = 684
    kSubdivCVComponent: int = 702
    kSubdivCollapse: int = 805
    kSubdivCompId: int = 798
    kSubdivData: int = 811
    kSubdivEdgeComponent: int = 703
    kSubdivFaceComponent: int = 704
    kSubdivGeom: int = 812
    kSubdivMapComponent: int = 860
    kSubdivReverseFaces: int = 816
    kSubdivSurfaceVarGroup: int = 840
    kSubdivToNurbs: int = 820
    kSubdivToPoly: int = 719
    kSubsetFalloff: int = 1146
    kSummaryObject: int = 484
    kSuper: int = 485
    kSurface: int = 293
    kSurfaceCVComponent: int = 542
    kSurfaceEPComponent: int = 543
    kSurfaceEdManip: int = 777
    kSurfaceFaceComponent: int = 778
    kSurfaceInfo: int = 103
    kSurfaceKnotComponent: int = 544
    kSurfaceLuminance: int = 487
    kSurfaceRangeComponent: int = 547
    kSurfaceShader: int = 488
    kSurfaceVarGroup: int = 118
    kSymmetryConstraint: int = 241
    kSymmetryLocator: int = 833
    kSymmetryMapCurve: int = 835
    kSymmetryMapVector: int = 834
    kTangentConstraint: int = 245
    kTension: int = 351
    kTexLattice: int = 200
    kTexLatticeDeformManip: int = 199
    kTexSmoothManip: int = 201
    kTexSmudgeUVManip: int = 198
    kTextButtonManip: int = 651
    kTextCurves: int = 104
    kTextManip: int = 928
    kTexture2d: int = 496
    kTexture3d: int = 507
    kTextureBakeSet: int = 472
    kTextureDeformer: int = 343
    kTextureDeformerHandle: int = 344
    kTextureEnv: int = 490
    kTextureList: int = 489
    kTextureManip3D: int = 223
    kThreadedDevice: int = 1076
    kThreePointArcManip: int = 649
    kTime: int = 520
    kTimeAttribute: int = 571
    kTimeEditor: int = 1106
    kTimeEditorAnimSource: int = 1109
    kTimeEditorClip: int = 1105
    kTimeEditorClipBase: int = 1103
    kTimeEditorClipEvaluator: int = 1104
    kTimeEditorInterpolator: int = 1108
    kTimeEditorTracks: int = 1107
    kTimeFunction: int = 941
    kTimeToUnitConversion: int = 521
    kTimeWarp: int = 1080
    kToggleManip: int = 224
    kToggleOnLineManip: int = 144
    kToolContext: int = 1094
    kToonLineAttributes: int = 972
    kTorus: int = 616
    kTowPointManip: int = 139
    kTowPointOnCurveManip: int = 209
    kTowPointOnSurfaceManip: int = 776
    kTrackInfoManager: int = 1123
    kTransferAttributes: int = 992
    kTransferFalloff: int = 1143
    kTransform: int = 110
    kTransformBoxManip: int = 832
    kTransformGeometry: int = 609
    kTranslateBoxManip: int = 225
    kTranslateLimitsManip: int = 226
    kTranslateManip: int = 227
    kTranslateManip2D: int = 206
    kTranslateUVManip: int = 213
    kTranslateUVManip2D: int = 706
    kTriadManip: int = 237
    kTrim: int = 105
    kTrimLocator: int = 287
    kTrimManip: int = 228
    kTrimWithBoundaries: int = 933
    kTriplanarProjectionManip: int = 188
    kTripleIndexedComponent: int = 715
    kTripleShadingSwitch: int = 620
    kTrsInsertManip: int = 203
    kTrsManip: int = 189
    kTrsTransManip: int = 202
    kTrsXformManip: int = 204
    kTurbulence: int = 262
    kTweak: int = 345
    kTwoPointArcManip: int = 650
    kTxSl: int = 518
    kTypedAttribute: int = 574
    kUInt64ArrayData: int = 813
    kUVManip2D: int = 705
    kUVPin: int = 990
    kUfeProxyTransform: int = 1134
    kUint64SingleIndexedComponent: int = 1040
    kUintArrayData: int = 586
    kUnderWorld: int = 109
    kUniform: int = 263
    kUniformFalloff: int = 1142
    kUnitAttribute: int = 573
    kUnitConversion: int = 529
    kUnitToTimeConversion: int = 530
    kUnknown: int = 532
    kUnknownDag: int = 316
    kUnknownTransform: int = 246
    kUntrim: int = 106
    kUnused1: int = 843
    kUnused2: int = 844
    kUnused3: int = 845
    kUnused4: int = 846
    kUnused5: int = 847
    kUnused6: int = 848
    kUseBackground: int = 531
    kUvChooser: int = 797
    kVectorArrayData: int = 607
    kVectorProduct: int = 533
    kVertexBakeSet: int = 473
    kVertexWeightSet: int = 1064
    kViewColorManager: int = 671
    kViewManip: int = 929
    kVolumeAxis: int = 799
    kVolumeBindManip: int = 1063
    kVolumeFog: int = 870
    kVolumeLight: int = 897
    kVolumeNoise: int = 876
    kVolumeShader: int = 534
    kVortex: int = 264
    kWater: int = 506
    kWeightFunctionData: int = 1147
    kWeightGeometryFilt: int = 346
    kWire: int = 355
    kWood: int = 519
    kWorld: int = 247
    kWrapFilter: int = 744
    kWriteToColorBuffer: int = 1044
    kWriteToDepthBuffer: int = 1046
    kWriteToFrameBuffer: int = 1043
    kWriteToLabelBuffer: int = 1047
    kWriteToVectorBuffer: int = 1045
    kXformManip: int = 930
    kXsectionSubdivEdit: int = 819

class MFnAttribute(MFnBase):
    """Base class for attribute functionsets."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def accepts(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this attribute can accept a connection of the given type."""

    def acceptsAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this attribute can accept a connection with the given attribute."""

    def addToCategory(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the attribute to a category"""

    affectsAppearance: getset_descriptor = <attribute 'affectsAppearance' of 'OpenMaya.MFnAttribute' objects>
    affectsWorldSpace: getset_descriptor = <attribute 'affectsWorldSpace' of 'OpenMaya.MFnAttribute' objects>
    array: getset_descriptor = <attribute 'array' of 'OpenMaya.MFnAttribute' objects>
    cached: getset_descriptor = <attribute 'cached' of 'OpenMaya.MFnAttribute' objects>
    channelBox: getset_descriptor = <attribute 'channelBox' of 'OpenMaya.MFnAttribute' objects>
    connectable: getset_descriptor = <attribute 'connectable' of 'OpenMaya.MFnAttribute' objects>
    disconnectBehavior: getset_descriptor = <attribute 'disconnectBehavior' of 'OpenMaya.MFnAttribute' objects>
    dynamic: getset_descriptor = <attribute 'dynamic' of 'OpenMaya.MFnAttribute' objects>
    extension: getset_descriptor = <attribute 'extension' of 'OpenMaya.MFnAttribute' objects>
    def getAddAttrCmd(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a string containing a MEL 'addAttr' command capable of recreating the attribute."""

    def hasCategory(self, *args: Any, **kwargs: Any) -> Any:
        """Checks to see if the attribute has a given category"""

    hidden: getset_descriptor = <attribute 'hidden' of 'OpenMaya.MFnAttribute' objects>
    indeterminant: getset_descriptor = <attribute 'indeterminant' of 'OpenMaya.MFnAttribute' objects>
    indexMatters: getset_descriptor = <attribute 'indexMatters' of 'OpenMaya.MFnAttribute' objects>
    internal: getset_descriptor = <attribute 'internal' of 'OpenMaya.MFnAttribute' objects>
    isProxyAttribute: getset_descriptor = <attribute 'isProxyAttribute' of 'OpenMaya.MFnAttribute' objects>
    kDelete: int = 0
    kNothing: int = 2
    kReset: int = 1
    keyable: getset_descriptor = <attribute 'keyable' of 'OpenMaya.MFnAttribute' objects>
    name: getset_descriptor = <attribute 'name' of 'OpenMaya.MFnAttribute' objects>
    parent: getset_descriptor = <attribute 'parent' of 'OpenMaya.MFnAttribute' objects>
    readable: getset_descriptor = <attribute 'readable' of 'OpenMaya.MFnAttribute' objects>
    renderSource: getset_descriptor = <attribute 'renderSource' of 'OpenMaya.MFnAttribute' objects>
    def setNiceNameOverride(self, *args: Any, **kwargs: Any) -> Any:
        """Sets a nice UI name for this attribute rather than using the default derived from it's long name."""

    shortName: getset_descriptor = <attribute 'shortName' of 'OpenMaya.MFnAttribute' objects>
    storable: getset_descriptor = <attribute 'storable' of 'OpenMaya.MFnAttribute' objects>
    usedAsColor: getset_descriptor = <attribute 'usedAsColor' of 'OpenMaya.MFnAttribute' objects>
    usedAsFilename: getset_descriptor = <attribute 'usedAsFilename' of 'OpenMaya.MFnAttribute' objects>
    usesArrayDataBuilder: getset_descriptor = <attribute 'usesArrayDataBuilder' of 'OpenMaya.MFnAttribute' objects>
    worldSpace: getset_descriptor = <attribute 'worldSpace' of 'OpenMaya.MFnAttribute' objects>
    writable: getset_descriptor = <attribute 'writable' of 'OpenMaya.MFnAttribute' objects>

class MFnBase(object):
    """Base class for function sets."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def hasObj(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the function set is compatible with the specified Maya object."""

    def object(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""

    def setObject(self, *args: Any, **kwargs: Any) -> Any:
        """Attaches the function set to the specified Maya object."""

    def type(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the function set."""


class MFnCamera(MFnDagNode):
    """Function set for cameras."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def aspectRatio(self, *args: Any, **kwargs: Any) -> Any:
        """aspectRatio() -> float

        Returns the aspect ratio for the camera.
        """

    cameraScale: getset_descriptor = <attribute 'cameraScale' of 'OpenMaya.MFnCamera' objects>
    centerOfInterest: getset_descriptor = <attribute 'centerOfInterest' of 'OpenMaya.MFnCamera' objects>
    def centerOfInterestPoint(self, *args: Any, **kwargs: Any) -> Any:
        """centerOfInterestPoint(space=kObject) -> MPoint

        Returns the center of interest point for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """

    def computeDepthOfField(self, *args: Any, **kwargs: Any) -> Any:
        """computeDepthOfField(nearLimit=None) -> self

        Compute the depth of field

        * nearLimit (float) - the near limit
        """

    def copyViewFrom(self, *args: Any, **kwargs: Any) -> Any:
        """copyViewFrom(otherCamera) -> self

        Copy the camera settings related to the perspective from the given camera view.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * otherCamera (MDagPath) - Camera to copy view from
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(parent=None) -> MObject

        Creates a perspective camera. A parent can be specified for the new camera, otherwise a transform is created.

        The camera is positioned at (0, 0, 0), its center of interest at (0, 0, -1), which implies that the view-direction is pointing in the direction of the negative z-axis, and its up-direction along the positive Y axis.

        * parent (MObject) - The parent of the new camera
        """

    def eyePoint(self, *args: Any, **kwargs: Any) -> Any:
        """eyePoint(space=kObject) -> MPoint

        Returns the eye point for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """

    fStop: getset_descriptor = <attribute 'fStop' of 'OpenMaya.MFnCamera' objects>
    farClippingPlane: getset_descriptor = <attribute 'farClippingPlane' of 'OpenMaya.MFnCamera' objects>
    farFocusDistance: getset_descriptor = <attribute 'farFocusDistance' of 'OpenMaya.MFnCamera' objects>
    filmFit: getset_descriptor = <attribute 'filmFit' of 'OpenMaya.MFnCamera' objects>
    filmFitOffset: getset_descriptor = <attribute 'filmFitOffset' of 'OpenMaya.MFnCamera' objects>
    filmRollOrder: getset_descriptor = <attribute 'filmRollOrder' of 'OpenMaya.MFnCamera' objects>
    filmRollValue: getset_descriptor = <attribute 'filmRollValue' of 'OpenMaya.MFnCamera' objects>
    filmTranslateH: getset_descriptor = <attribute 'filmTranslateH' of 'OpenMaya.MFnCamera' objects>
    filmTranslateV: getset_descriptor = <attribute 'filmTranslateV' of 'OpenMaya.MFnCamera' objects>
    focalLength: getset_descriptor = <attribute 'focalLength' of 'OpenMaya.MFnCamera' objects>
    focusDistance: getset_descriptor = <attribute 'focusDistance' of 'OpenMaya.MFnCamera' objects>
    def getAspectRatioLimits(self, *args: Any, **kwargs: Any) -> Any:
        """getAspectRatioLimits() -> (float, float)

        Returns the minimum and maximum aspect ratio limits for the camera.
        """

    def getFilmApertureLimits(self, *args: Any, **kwargs: Any) -> Any:
        """getFilmApertureLimits() -> (float, float)

        Returns the maximum and minimum film aperture limits for the camera.
        """

    def getFilmFrustum(self, *args: Any, **kwargs: Any) -> Any:
        """getFilmFrustum(distance, applyPanZoom=False) -> (float, float, float, float)

        Returns the film frustum for the camera (horizontal size, vertical size, horizontal offset and vertical offset). The frustum defines the projective transformation.

        * distance (float) - Specifies the focal length
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """

    def getFilmFrustumCorners(self, *args: Any, **kwargs: Any) -> Any:
        """getFilmFrustumCorners(distance, applyPanZoom=False) -> MPointArray

        Returns the film frustum for the camera. The frustum defines the projective transformation.

         element 0 is the bottom left
         element 1 is the top left
         element 2 is the top right
         element 3 is the bottom right

        * distance (float) - Specifies the focal length
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """

    def getFocalLengthLimits(self, *args: Any, **kwargs: Any) -> Any:
        """getFocalLengthLimits() -> (float, float)

        Returns the maximum and minimum focal length limits for the camera.
        """

    def getPortFieldOfView(self, *args: Any, **kwargs: Any) -> Any:
        """getPortFieldOfView(int, int) -> (float, float)

        Returns the horizontal and vertical field of view in radians from the given viewport width and height.

        * width (int) - width of viewport
        * height (int) - height of viewport
        """

    def getRenderingFrustum(self, *args: Any, **kwargs: Any) -> Any:
        """getRenderingFrustum(windowAspect) -> (float, float, float, float)

        Returns the rendering frustum (left, right, bottom and top) for the camera.
        This is the frustum that the maya renderer uses.

        * windowAspect (float) - windowAspect
        """

    def getViewParameters(self, *args: Any, **kwargs: Any) -> Any:
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

    def getViewingFrustum(self, *args: Any, **kwargs: Any) -> Any:
        """getViewingFrustum(windowAspect, applyOverscan=False, applySqueeze=False, applyPanZoom=False) -> (float, float, float, float)

        Returns the viewing frustum (left, right, bottom and top) for the camera.

        * windowAspect (float) - windowAspect
        * applyOverscan (bool) - specifies whether to apply overscan
        * applySqueeze (bool) - specifies whether to apply the lens squeeze ratio of the camera
        * applyPanZoom (bool) - specifies whether to apply 2D pan/zoom
        """

    def hasSamePerspective(self, *args: Any, **kwargs: Any) -> Any:
        """hasSamePerspective(otherCamera) -> bool

        Returns True if the camera has same perspective settings as the given camera.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * otherCamera (MDagPath) - Camera to compare perspective with
        """

    def horizontalFieldOfView(self, *args: Any, **kwargs: Any) -> Any:
        """horizontalFieldOfView() -> float

        Returns the horizontal field of view for the camera.
        """

    horizontalFilmAperture: getset_descriptor = <attribute 'horizontalFilmAperture' of 'OpenMaya.MFnCamera' objects>
    horizontalFilmOffset: getset_descriptor = <attribute 'horizontalFilmOffset' of 'OpenMaya.MFnCamera' objects>
    horizontalPan: getset_descriptor = <attribute 'horizontalPan' of 'OpenMaya.MFnCamera' objects>
    horizontalRollPivot: getset_descriptor = <attribute 'horizontalRollPivot' of 'OpenMaya.MFnCamera' objects>
    horizontalShake: getset_descriptor = <attribute 'horizontalShake' of 'OpenMaya.MFnCamera' objects>
    isClippingPlanes: getset_descriptor = <attribute 'isClippingPlanes' of 'OpenMaya.MFnCamera' objects>
    isDepthOfField: getset_descriptor = <attribute 'isDepthOfField' of 'OpenMaya.MFnCamera' objects>
    isDisplayFilmGate: getset_descriptor = <attribute 'isDisplayFilmGate' of 'OpenMaya.MFnCamera' objects>
    isDisplayGateMask: getset_descriptor = <attribute 'isDisplayGateMask' of 'OpenMaya.MFnCamera' objects>
    isMotionBlur: getset_descriptor = <attribute 'isMotionBlur' of 'OpenMaya.MFnCamera' objects>
    def isOrtho(self, *args: Any, **kwargs: Any) -> Any:
        """isOrtho() -> bool

        Returns True if the camera is in orthographic mode.
        """

    isVerticalLock: getset_descriptor = <attribute 'isVerticalLock' of 'OpenMaya.MFnCamera' objects>
    lensSqueezeRatio: getset_descriptor = <attribute 'lensSqueezeRatio' of 'OpenMaya.MFnCamera' objects>
    nearClippingPlane: getset_descriptor = <attribute 'nearClippingPlane' of 'OpenMaya.MFnCamera' objects>
    nearFocusDistance: getset_descriptor = <attribute 'nearFocusDistance' of 'OpenMaya.MFnCamera' objects>
    orthoWidth: getset_descriptor = <attribute 'orthoWidth' of 'OpenMaya.MFnCamera' objects>
    overscan: getset_descriptor = <attribute 'overscan' of 'OpenMaya.MFnCamera' objects>
    panZoomEnabled: getset_descriptor = <attribute 'panZoomEnabled' of 'OpenMaya.MFnCamera' objects>
    def postProjectionMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """postProjectionMatrix(context=None) -> MFloatMatrix

        Returns the post projection matrix used to compute film roll on the film back plane.

        * context (MDGContext) - DG time-context to specify time of evaluation
        """

    postScale: getset_descriptor = <attribute 'postScale' of 'OpenMaya.MFnCamera' objects>
    preScale: getset_descriptor = <attribute 'preScale' of 'OpenMaya.MFnCamera' objects>
    def projectionMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """projectionMatrix(context=None) -> MFloatMatrix

        Returns the orthographic or perspective projection matrix for the camera.
        The projection matrix that maya's software renderer uses is almost identical to the OpenGL projection matrix. The difference is that maya uses a left hand coordinate system and so the entries [2][2] and [3][2] are negated.

        * context (MDGContext) - DG time-context to specify time of evaluation
        """

    renderPanZoom: getset_descriptor = <attribute 'renderPanZoom' of 'OpenMaya.MFnCamera' objects>
    def rightDirection(self, *args: Any, **kwargs: Any) -> Any:
        """rightDirection(space=kObject) -> MVector

        Returns the right direction vector for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """set(wsEyeLocation, wsViewDirection, wsUpDirection, horizFieldOfView, aspectRatio) -> self

        Convenience routine to set the camera viewing parameters. The specified values should be in world space where applicable.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * wsEyeLocation (MPoint) - Eye location to set in world space
        * wsViewDirection (MVector) - View direction to set in world space
        * wsUpDirection (MVector) - Up direction to set in world space
        * horizFieldOfView (float) - The horizontal field of view to set
        * aspectRatio (float) - The aspect ratio to set
        """

    def setAspectRatio(self, *args: Any, **kwargs: Any) -> Any:
        """setAspectRatio(aspectRatio) -> self

        Set the aspect ratio of the View.  The aspect ratio is expressed as width/height.  This also modifies the entity's scale transformation to reflect the new aspect ratio.

        * aspectRatio (float) - The aspect ratio to be set
        """

    def setCenterOfInterestPoint(self, *args: Any, **kwargs: Any) -> Any:
        """setCenterOfInterestPoint(centerOfInterest, space=kObject) -> self

        Positions the center-of-interest of the camera keeping the eye-point fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * centerOfInterest (MPoint) - Center of interest point to be set
        * space (int) - Specifies the coordinate system for this operation
        """

    def setEyePoint(self, *args: Any, **kwargs: Any) -> Any:
        """setEyePoint(eyeLocation, space=kObject) -> self

        Positions the eye-point of the camera keeping the center of interest fixed in space. This method changed the orientation and translation of the camera's transform attributes as well as the center-of-interest distance.

        This method will only work when the world space information for the camera is available, i.e. when the function set has been initialized with a DAG path.

        * eyeLocation (MPoint) - The eye location to set
        * space (int) - Specifies the coordinate system for this operation
        """

    def setHorizontalFieldOfView(self, *args: Any, **kwargs: Any) -> Any:
        """setHorizontalFieldOfView(fov) -> self

        Sets the horizontal field of view for the camera.

        * fov (float) - The horizontal field of view value to be set
        """

    def setIsOrtho(self, *args: Any, **kwargs: Any) -> Any:
        """setIsOrtho(orthoState, useDist=None) -> self

        Switch the camera in and out of orthographic mode.  When the switch happens, the camera has to calculate a new fov or ortho width, each of which is based on the other and a set distance.  The caller can specify the distance; otherwise the center of interest is used.

        * orthoState (bool) - If True then the camera will be orthographic
        * useDist (float) - distance to use.
        """

    def setNearFarClippingPlanes(self, *args: Any, **kwargs: Any) -> Any:
        """setNearFarClippingPlanes(near, far) -> self

        Set the distances to the Near and Far Clipping Planes.

        * near (float) - The near clipping plane value to be set
        * far (float) - The far clipping plane value to be set
        """

    def setVerticalFieldOfView(self, *args: Any, **kwargs: Any) -> Any:
        """setVerticalFieldOfView(fov) -> self

        Sets the vertical field of view for the camera.

        * fov (float) - The vertical field of view value to be set
        """

    shakeEnabled: getset_descriptor = <attribute 'shakeEnabled' of 'OpenMaya.MFnCamera' objects>
    shakeOverscan: getset_descriptor = <attribute 'shakeOverscan' of 'OpenMaya.MFnCamera' objects>
    shakeOverscanEnabled: getset_descriptor = <attribute 'shakeOverscanEnabled' of 'OpenMaya.MFnCamera' objects>
    shutterAngle: getset_descriptor = <attribute 'shutterAngle' of 'OpenMaya.MFnCamera' objects>
    stereoHIT: getset_descriptor = <attribute 'stereoHIT' of 'OpenMaya.MFnCamera' objects>
    stereoHITEnabled: getset_descriptor = <attribute 'stereoHITEnabled' of 'OpenMaya.MFnCamera' objects>
    tumblePivot: getset_descriptor = <attribute 'tumblePivot' of 'OpenMaya.MFnCamera' objects>
    def upDirection(self, *args: Any, **kwargs: Any) -> Any:
        """upDirection(space=kObject) -> MVector

        Returns the up direction vector for the camera.

        * space (int) - Specifies the coordinate system for this operation
        """

    usePivotAsLocalSpace: getset_descriptor = <attribute 'usePivotAsLocalSpace' of 'OpenMaya.MFnCamera' objects>
    def verticalFieldOfView(self, *args: Any, **kwargs: Any) -> Any:
        """verticalFieldOfView() -> float

        Returns the vertical field of view for the camera.
        """

    verticalFilmAperture: getset_descriptor = <attribute 'verticalFilmAperture' of 'OpenMaya.MFnCamera' objects>
    verticalFilmOffset: getset_descriptor = <attribute 'verticalFilmOffset' of 'OpenMaya.MFnCamera' objects>
    verticalPan: getset_descriptor = <attribute 'verticalPan' of 'OpenMaya.MFnCamera' objects>
    verticalRollPivot: getset_descriptor = <attribute 'verticalRollPivot' of 'OpenMaya.MFnCamera' objects>
    verticalShake: getset_descriptor = <attribute 'verticalShake' of 'OpenMaya.MFnCamera' objects>
    def viewDirection(self, *args: Any, **kwargs: Any) -> Any:
        """viewDirection(space=kObject) -> MVector

        Returns the view direction for the camera

        * space (int) - Specifies the coordinate system for this operation
        """

    zoom: getset_descriptor = <attribute 'zoom' of 'OpenMaya.MFnCamera' objects>

class MFnComponent(MFnBase):
    """This is the base class for all function sets which deal with
    component objects.

    __init__()
    Initializes a new, empty MFnComponent object
    __init__(MObject component)
    Initializes a new MFnComponent function set, attached to the specified component.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    componentType: getset_descriptor = <attribute 'componentType' of 'OpenMaya.MFnComponent' objects>
    elementCount: getset_descriptor = <attribute 'elementCount' of 'OpenMaya.MFnComponent' objects>
    hasWeights: getset_descriptor = <attribute 'hasWeights' of 'OpenMaya.MFnComponent' objects>
    isComplete: getset_descriptor = <attribute 'isComplete' of 'OpenMaya.MFnComponent' objects>
    isEmpty: getset_descriptor = <attribute 'isEmpty' of 'OpenMaya.MFnComponent' objects>
    def isEqual(self, *args: Any, **kwargs: Any) -> Any:
        """isEqual(MObject other) -> bool

        Returns True if other refers to the same component as the
        one to which the function set is currently attached.
        """

    def weight(self, *args: Any, **kwargs: Any) -> Any:
        """weight(index) -> MWeight

        Returns the weight associated with the specified element,
        where index can range from 0 to elementCount-1.
        """


class MFnComponentListData(MFnData):
    """MFnComponentListData allows the creation and manipulation of component list
    (represented as MObjects) data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnComponentListData object.

    __init__(MObject)
    Initializes a new MFnComponentListData function set, attached
    to the specified object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def add(self, *args: Any, **kwargs: Any) -> Any:
        """add(MObject) -> self

        Adds the specified component to the end of the list.
        """

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Removes all of the components from the list.
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new, empty component list, attaches it to the
        function set and returns an MObject which references it.
        """

    def get(self, *args: Any, **kwargs: Any) -> Any:
        """get(index) -> MObject

        Returns a copy of the component at the specified index.
        Raises IndexError if the index is out of range.
        """

    def has(self, *args: Any, **kwargs: Any) -> Any:
        """has(MObject) -> bool

        Returns True if the list contains the specified
        component, False otherwise.
        """

    def length(self, *args: Any, **kwargs: Any) -> Any:
        """length() -> int

        Returns the number of components in the list.
        """

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove(MObject) -> self
        remove(index) -> self

        Removes the specified component from the list.
        No exception is raised if the component is not in the list,
        raises IndexError if index is out of range
        """


class MFnCompoundAttribute(MFnAttribute):
    """Functionset for creating and working with compound attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addChild(self, *args: Any, **kwargs: Any) -> Any:
        """Add a child attribute."""

    def child(self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the attribute's children, specified by index."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new compound attribute, attaches it to the function set and returns it as an MObject."""

    def getAddAttrCmds(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list of MEL 'addAttr' commands capable of recreating the attribute and all of its children."""

    def numChildren(self, *args: Any, **kwargs: Any) -> Any:
        """Returns number of child attributes currently parented under the compound attribute."""

    def removeChild(self, *args: Any, **kwargs: Any) -> Any:
        """Remove a child attribute."""


class MFnContainerNode(MFnDependencyNode):
    """Function set for containers."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear()

        Delete all members of the container.
        """

    def getCurrentAsMObject(self, *args: Any, **kwargs: Any) -> Any:
        """getCurrentAsMObject() -> MObject

        Retrieve the current container node.
        """

    def getMembers(self, *args: Any, **kwargs: Any) -> Any:
        """getMembers() -> MObjectArray

        Return an array of the nodes included in this container.
        """

    def getParentContainer(self, *args: Any, **kwargs: Any) -> Any:
        """getParentContainer() -> MObject

        Return the parent container, if there is one. Otherwise return an empty MObject.
        """

    def getPublishedNames(self, *args: Any, **kwargs: Any) -> Any:
        """getPublishedNames(unboundOnly=bool) -> [MString]

        Return a list of published names on the container. Depending on the arguments, either all published names or only unbound published names will be returned.
        """

    def getPublishedNodes(self, *args: Any, **kwargs: Any) -> Any:
        """getPublishedNodes(publishNodeType=MPublishNodeType) -> ([MString] publishedNames, MObjectArray publishedNodes)

        Return a list of the published nodes of a given type. For any names that have assigned nodes, return the node at the corresponding array index. For any names that do not have assigned nodes, a NULL MObject will be at the corresponding array index.
        """

    def getPublishedPlugs(self, *args: Any, **kwargs: Any) -> Any:
        """getPublishedPlugs() -> (MPlugArray publishedPlugs, [MString] publishedNames)

        Return a tuple of plugs that have been published on this container and the names of those plugs.
        """

    def getRootTransform(self, *args: Any, **kwargs: Any) -> Any:
        """getRootTransform() -> MObject

        Return the root transform, if there is one. Otherwise return an empty MObject.
        """

    def getSubcontainers(self, *args: Any, **kwargs: Any) -> Any:
        """getSubcontainers() -> MObjectArray

        Return an array of the container nodes included in this container.
        """

    def isCurrent(self, *args: Any, **kwargs: Any) -> Any:
        """isCurrent() -> bool

        Return whether the container node managed by this function set is the current container.
        """

    def makeCurrent(self, *args: Any, **kwargs: Any) -> Any:
        """makeCurrent(isCurrent) -> self

        Set or clear whether the container managed by this function set is denoted as the
        the current container.  If the flag is true and the container is allowed to be
        current, then the current container is set to be the container.  Otherwise, if the
        container managed by the function set is the current container, then the current
        container is cleared.

        * isCurrent (True/False) - Specifies whether this container shall be current.
        """


class MFnDagNode(MFnDependencyNode):
    """Function set for operating on DAG nodes.

    __init__()
    Initializes a new, empty MFnDagNode functionset.

    __init__(MObject)
    Initializes a new MFnDagNode functionset and attaches it to a
    DAG node.

    __init__(MDagPath)
    Initializes a new MFnDagNode functionset and attaches it to a
    DAG path.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addChild(self, *args: Any, **kwargs: Any) -> Any:
        """addChild(node, index=kNextPos, keepExistingParents=False) -> self

        Makes a node a child of this one.
        """

    boundingBox: getset_descriptor = <attribute 'boundingBox' of 'OpenMaya.MFnDagNode' objects>
    def child(self, *args: Any, **kwargs: Any) -> Any:
        """child(index) -> MObject

        Returns the specified child of this node.
        """

    def childCount(self, *args: Any, **kwargs: Any) -> Any:
        """childCount() -> int

        Returns the number of nodes which are children of this one.
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
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

    def dagPath(self, *args: Any, **kwargs: Any) -> Any:
        """dagPath() -> MDagPath

        Returns the DAG path to which this function set is attached. Raises a TypeError if the function set is attached to an MObject rather than a path.
        """

    def dagRoot(self, *args: Any, **kwargs: Any) -> Any:
        """dagRoot() -> MObject

        Returns the root node of the first path leading to this node.
        """

    def duplicate(self, *args: Any, **kwargs: Any) -> Any:
        """duplicate(instance=False, instanceLeaf=False) -> MObject

        Duplicates the DAG hierarchy rooted at the current node.
        """

    def fullPathName(self, *args: Any, **kwargs: Any) -> Any:
        """fullPathName() -> string

        Returns the full path of the attached object, from the root of the DAG on down.
        """

    def getAllPaths(self, *args: Any, **kwargs: Any) -> Any:
        """getAllPaths() -> MDagPathArray

        Returns all of the DAG paths which lead to the object to which this function set is attached.
        """

    def getConnectedSetsAndMembers(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedSetsAndMembers(instance, renderableSetsOnly) -> (MObjectArray, MObjectArray)

        Returns a tuple containing an array of sets and an array of the
        components of the DAG object which are in those sets. If the entire object is in a set, then the corresponding entry in the comps array will have no elements in it.
        """

    def getPath(self, *args: Any, **kwargs: Any) -> Any:
        """getPath() -> MDagPath

        Returns the DAG path to which this function set is attached, or the first path to the node if the function set is attached to an MObject.
        """

    def hasChild(self, *args: Any, **kwargs: Any) -> Any:
        """hasChild(node) -> bool

        Returns True if the specified node is a child of this one.
        """

    def hasParent(self, *args: Any, **kwargs: Any) -> Any:
        """hasParent(node) -> bool

        Returns True if the specified node is a parent of this one.
        """

    inModel: getset_descriptor = <attribute 'inModel' of 'OpenMaya.MFnDagNode' objects>
    inUnderWorld: getset_descriptor = <attribute 'inUnderWorld' of 'OpenMaya.MFnDagNode' objects>
    def instanceCount(self, *args: Any, **kwargs: Any) -> Any:
        """instanceCount(indirect) -> int

        Returns the number of instances for this node.
        """

    def isChildOf(self, *args: Any, **kwargs: Any) -> Any:
        """isChildOf(node) -> bool

        Returns True if the specified node is a parent of this one.
        """

    isInstanceable: getset_descriptor = <attribute 'isInstanceable' of 'OpenMaya.MFnDagNode' objects>
    def isInstanced(self, *args: Any, **kwargs: Any) -> Any:
        """isInstanced(indirect=True) -> bool

        Returns True if this node is instanced.
        """

    def isInstancedAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """isInstancedAttribute(attr) -> bool

        Returns True if the specified attribute is an instanced attribute of this node.
        """

    isIntermediateObject: getset_descriptor = <attribute 'isIntermediateObject' of 'OpenMaya.MFnDagNode' objects>
    def isParentOf(self, *args: Any, **kwargs: Any) -> Any:
        """isParentOf(node) -> bool

        Returns True if the specified node is a child of this one.
        """

    kNextPos: int = 255
    objectColor: getset_descriptor = <attribute 'objectColor' of 'OpenMaya.MFnDagNode' objects>
    objectColorRGB: getset_descriptor = <attribute 'objectColorRGB' of 'OpenMaya.MFnDagNode' objects>
    objectColorType: getset_descriptor = <attribute 'objectColorType' of 'OpenMaya.MFnDagNode' objects>
    def parent(self, *args: Any, **kwargs: Any) -> Any:
        """parent(index) -> MObject

        Returns the specified parent of this node.
        """

    def parentCount(self, *args: Any, **kwargs: Any) -> Any:
        """parentCount() -> int

        Returns the number of parents this node has.
        """

    def partialPathName(self, *args: Any, **kwargs: Any) -> Any:
        """partialPathName() -> string

        Returns the minimum path string necessary to uniquely identify the attached object.
        """

    def removeChild(self, *args: Any, **kwargs: Any) -> Any:
        """removeChild(node) -> self

        Removes the child, specified by MObject, reparenting it under the world.
        """

    def removeChildAt(self, *args: Any, **kwargs: Any) -> Any:
        """removeChildAt(index) -> self

        Removes the child, specified by index, reparenting it under the world.
        """

    def setObject(self, *args: Any, **kwargs: Any) -> Any:
        """setObject(MObject or MDagPath) -> self

        Attaches the function set to the specified node or DAG path.
        """

    def transformationMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """transformationMatrix() -> MMatrix

        Returns the object space transformation matrix for this DAG node.
        """

    useObjectColor: getset_descriptor = <attribute 'useObjectColor' of 'OpenMaya.MFnDagNode' objects>

class MFnData(MFnBase):
    """Base class for dependency graph data function sets."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    kAny: int = 24
    kComponentList: int = 13
    kDoubleArray: int = 7
    kDynArrayAttrs: int = 19
    kDynSweptGeometry: int = 20
    kFalloffFunction: int = 25
    kFloatArray: int = 8
    kIntArray: int = 9
    kInvalid: int = 0
    kLast: int = 26
    kLattice: int = 15
    kMatrix: int = 5
    kMatrixArray: int = 12
    kMesh: int = 14
    kNId: int = 23
    kNObject: int = 22
    kNumeric: int = 1
    kNurbsCurve: int = 16
    kNurbsSurface: int = 17
    kPlugin: int = 2
    kPluginGeometry: int = 3
    kPointArray: int = 10
    kSphere: int = 18
    kString: int = 4
    kStringArray: int = 6
    kSubdSurface: int = 21
    kVectorArray: int = 11

class MFnDependencyNode(MFnBase):
    """Function set for operating on dependency nodes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def absoluteName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the absolute name of this node.  The absolute name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself.  Regardless of relative name mode, absoluteName() will always return a full namespace path prefixed with a leading colon (the root namespace).  If the underlying node is a DAG node, then absoluteName() does not guarantee uniqueness, that is, two dependency nodes could have the same absoluteName().  In cases like this the uniqueName() method will guarantee that the name uniquely identifies the node."""

    def addAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Adds a new dynamic attribute to the node."""

    def addExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Adds content info to the specified table from a file path attribute."""

    def affectsAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the changes to the node may affect animation."""

    def allocateFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Allocates a flag on all nodes for use by the named plugin and returns the flag's index."""

    def attribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an attribute of the node, given either its index or name."""

    def attributeClass(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the class of the specified attribute."""

    def attributeCount(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of attributes on the node."""

    def canBeWritten(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the node will be written to file."""

    def classification(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the classification string for the named node type."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new node of the given type."""

    def deallocateAllFlags(self, *args: Any, **kwargs: Any) -> Any:
        """Deallocates all node flags which are currently allocated to the named plugin."""

    def deallocateFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Deallocates the specified node flag, which was previously allocated by the named plugin using allocateFlag()."""

    def dgCallbackIds(self, *args: Any, **kwargs: Any) -> Any:
        """Returns DG timing information for a specific callback type, broken down by callbackId."""

    def dgCallbacks(self, *args: Any, **kwargs: Any) -> Any:
        """Returns DG timing information broken down by callback type."""

    def dgTimer(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a specific DG timer metric for a given timer type."""

    def dgTimerOff(self, *args: Any, **kwargs: Any) -> Any:
        """Turns DG timing off for this node."""

    def dgTimerOn(self, *args: Any, **kwargs: Any) -> Any:
        """Turns DG timing on for this node."""

    def dgTimerQueryState(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the current DG timer state for this node."""

    def dgTimerReset(self, *args: Any, **kwargs: Any) -> Any:
        """Resets all DG timers for this node."""

    def findAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute which has the given alias."""

    def findPlug(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the given attribute."""

    def getAffectedAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which are affected by the specified attribute."""

    def getAffectingAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the attributes which affect the specified attribute."""

    def getAliasAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's alias attribute, which is a special attribute used to store information about the node's attribute aliases."""

    def getAliasList(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all of the node's attribute aliases."""

    def getConnections(self, *args: Any, **kwargs: Any) -> Any:
        """Returns all the plugs which are connected to attributes of this node."""

    def getExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Gets the external content (files) that this node depends on."""

    def hasAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node has an attribute with the given name."""

    def hasUniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node's name is unique."""

    isDefaultNode: getset_descriptor = <attribute 'isDefaultNode' of 'OpenMaya.MFnDependencyNode' objects>
    def isFlagSet(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the state of the specified node flag."""

    isFromReferencedFile: getset_descriptor = <attribute 'isFromReferencedFile' of 'OpenMaya.MFnDependencyNode' objects>
    isLocked: getset_descriptor = <attribute 'isLocked' of 'OpenMaya.MFnDependencyNode' objects>
    def isNewAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified attribute was added in the current scene, and not by by one of its referenced files."""

    isShared: getset_descriptor = <attribute 'isShared' of 'OpenMaya.MFnDependencyNode' objects>
    def isTrackingEdits(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node is referenced or in an assembly that is tracking edits."""

    kExtensionAttr: int = 3
    kInvalidAttr: int = 4
    kLocalDynamicAttr: int = 1
    kNormalAttr: int = 2
    kTimerInvalidState: int = 3
    kTimerMetric_callback: int = 0
    kTimerMetric_callbackNotViaAPI: int = 6
    kTimerMetric_callbackViaAPI: int = 5
    kTimerMetric_compute: int = 1
    kTimerMetric_computeDuringCallback: int = 7
    kTimerMetric_computeNotDuringCallback: int = 8
    kTimerMetric_dirty: int = 2
    kTimerMetric_draw: int = 3
    kTimerMetric_fetch: int = 4
    kTimerMetrics: int = 9
    kTimerOff: int = 0
    kTimerOn: int = 1
    kTimerType_count: int = 2
    kTimerType_inclusive: int = 1
    kTimerType_self: int = 0
    kTimerTypes: int = 3
    kTimerUninitialized: int = 2
    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's name."""

    namespace: getset_descriptor = <attribute 'namespace' of 'OpenMaya.MFnDependencyNode' objects>
    pluginName: getset_descriptor = <attribute 'pluginName' of 'OpenMaya.MFnDependencyNode' objects>
    def plugsAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the alias for a plug's attribute."""

    def removeAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Removes a dynamic attribute from the node."""

    def reorderedAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the node's attribute, based on the order in which they are written to file."""

    def setAffectsAnimation(self, *args: Any, **kwargs: Any) -> Any:
        """Specifies that modifications to a node could potentially affect the animation."""

    def setAlias(self, *args: Any, **kwargs: Any) -> Any:
        """Adds or removes an attribute alias."""

    def setDoNotWrite(self, *args: Any, **kwargs: Any) -> Any:
        """Used to prevent the node from being written to file."""

    def setExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """Changes the location of external content."""

    def setExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """Sets content info in the specified attribute from the table."""

    def setFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the state of the specified node flag."""

    def setName(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's name."""

    def setUuid(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the node's UUID."""

    typeId: getset_descriptor = <attribute 'typeId' of 'OpenMaya.MFnDependencyNode' objects>
    typeName: getset_descriptor = <attribute 'typeName' of 'OpenMaya.MFnDependencyNode' objects>
    def uniqueName(self, *args: Any, **kwargs: Any) -> Any:
        """For a DAG node, the unique name of a node is the full namespace path starting at (and including) the root namespace, down to (and including) the node itself. For a non-DAG node, the uniqueName is just its name."""

    def userNode(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MPxNode object for a plugin node."""

    def uuid(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node's UUID."""


class MFnDisplayLayer(MFnDependencyNode):
    """Function set display layer.

    __init__()
    Initializes a new, empty MFnDisplayLayer object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def add(self, *args: Any, **kwargs: Any) -> Any:
        """add(item) -> status
        Adds the item to the display layer, where item can be a Ufe path string
        (MString) or a Maya path (MDagPath).
        """

    def contains(self, *args: Any, **kwargs: Any) -> Any:
        """contains(item) -> bool
        Returns true if the item is in the display layer, where item can be a Ufe
        path string (MString) or a Maya path (MDagPath).
        """

    def containsAncestorInclusive(self, *args: Any, **kwargs: Any) -> Any:
        """containsAncestorInclusive(item) -> status
        Returns true if the item or one of its ancestors is in the display layer,
         where item can be a Ufe path string (MString) or a Maya path (MDagPath).
        """

    def getMembers(self, *args: Any, **kwargs: Any) -> Any:
        """getMembers(members) -> status
        Get the members of the display layer
        """

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove(item) -> status
        Removes the item to the display layer, where item can be a Ufe path string
        (MString) or a Maya path (MDagPath).
        """


class MFnDisplayLayerManager(MFnDependencyNode):
    """Function set display layer.

    __init__()
    Initializes a new, empty MFnDisplayLayerManager object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def currentDisplayLayerManager(self, *args: Any, **kwargs: Any) -> Any:
        """currentDisplayLayerManager() -> MObject
        Get the current display layer manager
        """

    def getAllDisplayLayers(self, *args: Any, **kwargs: Any) -> Any:
        """getAllDisplayLayers() -> object array
        Get all the display layers managed by the display layer manager
        (MString) or a Maya path (MDagPath).
        """

    def getAncestorLayersInclusive(self, *args: Any, **kwargs: Any) -> Any:
        """getAncestorLayersInclusive(item) -> status
        Finds the layers the item and it's ancestors are in, where item can be a Ufe
        path string (MString) or a Maya object (MObject).
        """

    def getLayer(self, *args: Any, **kwargs: Any) -> Any:
        """getLayer(item) -> status
        Finds the layer the item is in, where item can be a Ufe
        path string (MString) or a Maya object (MObject).
        """


class MFnDoubleArrayData(MFnData):
    """Function set for node data consisting of an array of doubles."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MDoubleArray."""

    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new double array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MFnDoubleIndexedComponent(MFnComponent):
    """This function set allows you to create, edit, and query double indexed
    components. Double indexed components store 2 dimensional index values.

    __init__()
    Initializes a new, empty MFnDoubleIndexedComponent object

    __init__(MObject component)
    Initializes a new MFnDoubleIndexedComponent function set, attached
    to the specified component.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addElement(self, *args: Any, **kwargs: Any) -> Any:
        """addElement(uIndex, vIndex) -> self
        addElement([uIndex, vIndex]) -> self

        Adds the element identified by (uIndex, vIndex) to the component.
        """

    def addElements(self, *args: Any, **kwargs: Any) -> Any:
        """addElements(sequence of [uIndex, vIndex]) -> self

        Adds the specified elements to the component. Each item in the
        elements sequence is itself a sequence of two ints which are the U and
        V indices of an element to be added.
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """

    def getCompleteData(self, *args: Any, **kwargs: Any) -> Any:
        """getCompleteData() -> (numU, numV)

        Returns a tuple containing the number of U and V indices in the complete
        component, or (0,0) if the component is not complete.
        """

    def getElement(self, *args: Any, **kwargs: Any) -> Any:
        """getElement(index) -> (uIndex, vIndex)

        Returns the index'th element of the component as a tuple containing the
        element's U and V indices.
        """

    def getElements(self, *args: Any, **kwargs: Any) -> Any:
        """getElements() -> list of (uIndex, vIndex)

        Returns all of the component's elements as a list of tuples with each
        tuple containing the U and V indices of a single element.
        """

    def setCompleteData(self, *args: Any, **kwargs: Any) -> Any:
        """setCompleteData(numU, numV) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numU and numV indicate the number of U and V indices in the complete
        component (i.e. the max U index is numU-1 and the max V index is numV-1).
        """


class MFnEnumAttribute(MFnAttribute):
    """Functionset for creating and working with enumeration attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addField(self, *args: Any, **kwargs: Any) -> Any:
        """Add an item to the enumeration with a specified UI name and corresponding attribute value."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new enumeration attribute, attaches it to the function set and returns it as an MObject."""

    default: getset_descriptor = <attribute 'default' of 'OpenMaya.MFnEnumAttribute' objects>
    def fieldName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the name of the enumeration item which has a given value."""

    def fieldValue(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the enumeration item which has a given name."""

    def getMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the maximum value of all the enumeration items."""

    def getMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the minimum value of all the enumeration items."""

    def setDefaultByName(self, *args: Any, **kwargs: Any) -> Any:
        """Set the default value using the name of an enumeration item. Equivalent to: attr.default = attr.fieldValue(name)"""


class MFnGenericAttribute(MFnAttribute):
    """Functionset for creating and working with attributes which can accept several different types of data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addDataType(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified Maya data type to the list of those accepted by the attribute."""

    def addNumericType(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified numeric type to the list of those accepted by the attribute."""

    def addTypeId(self, *args: Any, **kwargs: Any) -> Any:
        """Adds the specified data typeId to the list of those accepted by the attribute."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new generic attribute, attaches it to the function set and returns it as an MObject."""

    def removeDataType(self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified Maya data type from the list of those accepted by the attribute."""

    def removeNumericType(self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified numeric type from the list of those accepted by the attribute."""

    def removeTypeId(self, *args: Any, **kwargs: Any) -> Any:
        """Removes the specified data typeId from the list of those accepted by the attribute."""


class MFnGeometryData(MFnData):
    """This class is the function set for geometry data.

    Geometry data adds matrix and grouping (set) information to regular
    data and is used to pass geometry types such as mesh, lattice, and
    NURBS shape data through DG connections.

    __init__()
    Initializes a new, empty MFnGeometryData object

    __init__(MObject)
    Initializes a new MFnGeometryData function set, attached
    to the specified object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addComponentTag(self, *args: Any, **kwargs: Any) -> Any:
        """addComponentTag(key) -> self

        Adds a componentTag with the given key to the object.
        """

    def addObjectGroup(self, *args: Any, **kwargs: Any) -> Any:
        """addObjectGroup(id) -> self

        Adds an object group with the given id to the object.
        """

    def addObjectGroupComponent(self, *args: Any, **kwargs: Any) -> Any:
        """addObjectGroupComponent(id, MObject component) -> self

        Adds the members of the given component to the object group
        with the given id.
        """

    def changeObjectGroupId(self, *args: Any, **kwargs: Any) -> Any:
        """changeObjectGroupId(sourceId, destId) -> self

        Changes the id of the object group with the given id to the new id.
        """

    def componentTagContents(self, *args: Any, **kwargs: Any) -> Any:
        """componentTagContents(key) -> MObject

        Returns a component which contains the members of the componentTag
        with the given key.
        """

    def componentTagExpressionSubsetState(self, *args: Any, **kwargs: Any) -> Any:
        """componentTagExpressionSubsetState(expr,ctg) -> MFnGeometryData::SubsetState type constant

        Returns the state of the contents of the resolved componentTag expression.
        """

    def componentTagType(self, *args: Any, **kwargs: Any) -> Any:
        """componentTagType(key) -> MFn Type constant

        Returns the type of the component that the componentTag with the
        given key contains.
        """

    def componentTags(self, *args: Any, **kwargs: Any) -> Any:
        """componentTags() -> MObject

        Returns the componentTag keys contained in the object.
        """

    def copyObjectGroups(self, *args: Any, **kwargs: Any) -> Any:
        """copyObjectGroups(MObject inGeom) -> self

        Copies the object groups from the given geometry data object.
        """

    def hasComponentTag(self, *args: Any, **kwargs: Any) -> Any:
        """hasComponentTag(key) -> bool

        Returns True if a componentTag with the given key exists.
        """

    def hasObjectGroup(self, *args: Any, **kwargs: Any) -> Any:
        """hasObjectGroup(id) -> self

        Returns True if an object group with the given id is
        contained in the data.
        """

    isIdentity: getset_descriptor = <attribute 'isIdentity' of 'OpenMaya.MFnGeometryData' objects>
    isNotIdentity: getset_descriptor = <attribute 'isNotIdentity' of 'OpenMaya.MFnGeometryData' objects>
    matrix: getset_descriptor = <attribute 'matrix' of 'OpenMaya.MFnGeometryData' objects>
    def objectGroup(self, *args: Any, **kwargs: Any) -> Any:
        """objectGroup(index) -> int

        Returns the id of the index'th object group contained by the object.
        """

    def objectGroupComponent(self, *args: Any, **kwargs: Any) -> Any:
        """objectGroupComponent(id) -> MObject

        Returns a component which contains the members of the object group
        with the given id.
        """

    objectGroupCount: getset_descriptor = <attribute 'objectGroupCount' of 'OpenMaya.MFnGeometryData' objects>
    def objectGroupSubsetState(self, *args: Any, **kwargs: Any) -> Any:
        """objectGroupSubsetState(id) -> MFnGeometryData::SubsetState type constant

        Returns the state of the group contents of the object group with the
        given id.
        """

    def objectGroupType(self, *args: Any, **kwargs: Any) -> Any:
        """objectGroupType(id) -> MFn Type constant

        Returns the type of the component that the object group with the
        given id contains.
        """

    def removeComponentTag(self, *args: Any, **kwargs: Any) -> Any:
        """removeComponentTag(key) -> self

        Removes a componentTag with the given key from the object.
        """

    def removeObjectGroup(self, *args: Any, **kwargs: Any) -> Any:
        """removeObjectGroup(id) -> self

        Removes an object group with the given id from the object.
        """

    def removeObjectGroupComponent(self, *args: Any, **kwargs: Any) -> Any:
        """removeObjectGroupComponent(id, MObject component) -> self

        Removes the members of the given component from the object group
        with the given id.
        """

    def renameComponentTag(self, *args: Any, **kwargs: Any) -> Any:
        """renameComponentTag(key, newKey) -> self

        Renames a componentag with the given key the object.
        """

    def resolveComponentTagExpression(self, *args: Any, **kwargs: Any) -> Any:
        """resolveComponentTagExpression(key, ctg) -> MObject

        Returns a component which is the result of the resolved componentTag expression
        with the given key.
        """

    def setComponentTagContents(self, *args: Any, **kwargs: Any) -> Any:
        """setComponentTagContents(key, MObject component) -> self

        Sets the members of the componentTag with the given key
        to be those in the given component.
        """

    def setObjectGroupComponent(self, *args: Any, **kwargs: Any) -> Any:
        """setObjectGroupComponent(id, MObject component) -> self

        Sets the members of the object group with the given id
        to be only those in the given component.
        """


class MFnIntArrayData(MFnData):
    """Function set for node data consisting of an array of ints."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MIntArray."""

    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new int array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MFnLightDataAttribute(MFnAttribute):
    """Functionset for creating and working with light data attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def child(self, *args: Any, **kwargs: Any) -> Any:
        """Returns one of the attribute's children, specified by index."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new light data attribute, attaches it to the function set and returns it as an MObject."""

    default: getset_descriptor = <attribute 'default' of 'OpenMaya.MFnLightDataAttribute' objects>

class MFnMatrixArrayData(MFnData):
    """Function set for node data consisting of an array of MMatrix."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MMatrixArray."""

    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MMatrix array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MFnMatrixAttribute(MFnAttribute):
    """Functionset for creating and working with matrix attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new matrix attribute, attaches it to the function set and returns it as an MObject."""

    default: getset_descriptor = <attribute 'default' of 'OpenMaya.MFnMatrixAttribute' objects>

class MFnMatrixData(MFnData):
    """Function set for matrix node data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new matrix data object."""

    def isTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attached object is an MTransformationMatrix, False if it is an MMatrix."""

    def matrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated matrix as an MMatrix."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the encapsulated matrix."""

    def transformation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated matrix as an MTransformationMatrix."""


class MFnMesh(MFnDagNode):
    """Function set for operation on meshes (polygonal surfaces).

    __init__()
    Initializes a new, empty MFnMesh object.

    __init__(MDagPath path)
    Initializes a new MFnMesh object and attaches it to the DAG path
    of a mesh node.

    __init__(MObject nodeOrData)
    Initializes a new MFnMesh object and attaches it to a mesh
    node or mesh data object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addHoles(self, *args: Any, **kwargs: Any) -> Any:
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

    def addPolygon(self, *args: Any, **kwargs: Any) -> Any:
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

    def allIntersections(self, *args: Any, **kwargs: Any) -> Any:
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

    def anyIntersection(self, *args: Any, **kwargs: Any) -> Any:
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

    def assignColor(self, *args: Any, **kwargs: Any) -> Any:
        """assignColor(faceId, vertexIndex, colorId, colorSet='') -> self

        Assigns a color from a colorSet to a specified vertex of a face.
        """

    def assignColors(self, *args: Any, **kwargs: Any) -> Any:
        """assignColors(colorIds, colorSet=') -> self

        Assigns colors to all of the mesh's face-vertices. The colorIds
        sequence must contain an entry for every vertex of every face, in
        face order, meaning that the entries for all the vertices of face 0
        come first, followed by the entries for the vertices of face 1, etc.
        """

    def assignUV(self, *args: Any, **kwargs: Any) -> Any:
        """assignUV(faceId, vertexIndex, uvId, uvSet='') -> self

        Assigns a UV coordinate from a uvSet to a specified vertex of a face.
        """

    def assignUVs(self, *args: Any, **kwargs: Any) -> Any:
        """assignUVs(uvCounts, uvIds, uvSet='') -> self

        Assigns UV coordinates to the mesh's face-vertices.

        uvCounts contains the number of UVs to assign for each of the mesh's
        faces. That number must equal the number of vertices in the
        corresponding face or be 0 to indicate that no UVs will be assigned
        to that face.
        """

    def autoUniformGridParams(self, *args: Any, **kwargs: Any) -> Any:
        """autoUniformGridParams() -> MMeshIsectAccelParams

        Creates an object which specifies a uniform voxel grid structure
        which can be used by the intersection routines to speed up their
        operation. The number of voxel cells to use will be determined
        automatically based on the density of triangles in the mesh. The
        grid acceleration structure will be cached with the mesh, so that
        if the same MMeshIsectAccelParams configuration is used on the next
        intersect call, the acceleration structure will not need to be rebuilt.
        """

    def booleanOp(self, *args: Any, **kwargs: Any) -> Any:
        """(Deprecated: Please use booleanOps instead) booleanOp(Boolean Operation constant, MFnMesh, MFnMesh) -> self

        Replaces this mesh's geometry with the result of a boolean operation
        on the two specified meshes.
        """

    def booleanOps(self, *args: Any, **kwargs: Any) -> Any:
        """booleanOps(Boolean Operation constant, MObjectArray, bool) -> self

        Replaces this mesh's geometry with the result of a boolean operation
        on the specified meshes.
        """

    def cachedIntersectionAcceleratorInfo(self, *args: Any, **kwargs: Any) -> Any:
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

    checkSamePointTwice: getset_descriptor = <attribute 'checkSamePointTwice' of 'OpenMaya.MFnMesh' objects>
    def cleanupEdgeSmoothing(self, *args: Any, **kwargs: Any) -> Any:
        """cleanupEdgeSmoothing() -> self

        Updates the mesh after setEdgeSmoothing has been done. This should
        be called only once, after all the desired edges have been had their
        smoothing set. If you don't call this method, the normals may not be
        correct, and the object will look odd in shaded mode.
        """

    def clearBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def clearColors(self, *args: Any, **kwargs: Any) -> Any:
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

    def clearGlobalIntersectionAcceleratorInfo(self, *args: Any, **kwargs: Any) -> Any:
        """clearGlobalIntersectionAcceleratorInfo()

        Clears the 'total count', 'total build time', and 'peak memory'
        fields from the information string returned by
        globalIntersectionAcceleratorsInfo(). It will not cause information
        about currently existing accelerators to be lost.
        """

    def clearUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def closestIntersection(self, *args: Any, **kwargs: Any) -> Any:
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

    def collapseEdges(self, *args: Any, **kwargs: Any) -> Any:
        """collapseEdges(seq of int) -> self

        Collapses edges into vertices. The two vertices that create each
        given edge are replaced in turn by one vertex placed at the average
        of the two initial vertex.
        """

    def collapseFaces(self, *args: Any, **kwargs: Any) -> Any:
        """collapseFaces(seq of int) -> self

        Collapses faces into vertices. Adjacent faces will be collapsed
        together into a single vertex. Non-adjacent faces will be collapsed
        into their own, separate vertices.
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
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

    def copyInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """copyInPlace(MObject) -> self

        Replaces the current mesh's geometry with that from the source.
        Raises TypeError if the source is not a mesh node or mesh data
        object or it contains an empty mesh.
        """

    def copyUVSet(self, *args: Any, **kwargs: Any) -> Any:
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

    def create(self, *args: Any, **kwargs: Any) -> Any:
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

    def createBlindDataType(self, *args: Any, **kwargs: Any) -> Any:
        """createBlindDataType(blindDataId, ((longName, shortName, typeName), ...)) -> self

        Create a new blind data type with the specified attributes.

        Each element of the attrs sequence is a tuple containing the long
        name, short name and type name of the attribute. Valid type names
        are 'int', 'float', 'double', 'boolean', 'string' or 'binary'.

        Raises RuntimeError if the blind data id is already in use or an
        invalid format was specified.
        """

    def createColorSet(self, *args: Any, **kwargs: Any) -> Any:
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

    def createInPlace(self, *args: Any, **kwargs: Any) -> Any:
        """createInPlace(vertices, polygonCounts, polygonConnects) -> selfcreateInPlace(vertices, edges, polygonCounts, polygonConnects) -> self

        Replaces the existing polygonal mesh with a new one. This method is
        meant to be as efficient as possible and thus assumes that all the
        given data is topologically correct.

        If edges are supplied, edges must be an integer array containingconsecutive sets of 3 integers (startVertex, endVertex, smooth) peredge. polygonConnects then references edges by index into the edgearray, where the ID == edge array index / 3.
        The vertices may be given as a sequence of MFloatPoint's or a
        sequence of MPoint's, but not a mix of the two.
        """

    def createUVSet(self, *args: Any, **kwargs: Any) -> Any:
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

    def currentColorSetName(self, *args: Any, **kwargs: Any) -> Any:
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

    def currentUVSetName(self, *args: Any, **kwargs: Any) -> Any:
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

    def deleteColorSet(self, *args: Any, **kwargs: Any) -> Any:
        """deleteColorSet(colorSet, modifier=None, currentSelection=None) -> self

        Deletes a color set from the mesh.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """

    def deleteEdge(self, *args: Any, **kwargs: Any) -> Any:
        """deleteEdge(edgeId, modifier=None) -> self

        Deletes the specified edge.
        """

    def deleteFace(self, *args: Any, **kwargs: Any) -> Any:
        """deleteFace(faceId, modifier=None) -> self

        Deletes the specified face.
        """

    def deleteUVSet(self, *args: Any, **kwargs: Any) -> Any:
        """deleteUVSet(uvSet, modifier=None, currentSelection=None) -> self

        Deletes a uv set from the mesh.

        This method is only valid for functionsets which are attached to
        mesh nodes, not mesh data.
        """

    def deleteVertex(self, *args: Any, **kwargs: Any) -> Any:
        """deleteVertex(vertexId, modifier=None) -> self

        Deletes the specified vertex.
        """

    displayColors: getset_descriptor = <attribute 'displayColors' of 'OpenMaya.MFnMesh' objects>
    def duplicateFaces(self, *args: Any, **kwargs: Any) -> Any:
        """duplicateFaces(faces, translation=None) -> self

        Duplicates a set of faces and detaches them from the rest of the
        mesh. The resulting mesh will contain one more independant piece of
        geometry.
        """

    def edgeBorderInfo(self, *args: Any, **kwargs: Any) -> Any:
        """edgeBorderInfo(edgeId, setId=0) -> MFnMesh::BorderInfo

        Returns if the specified edge is on geom/UV shell border or has shared/unshared UVs.
        """

    def extractFaces(self, *args: Any, **kwargs: Any) -> Any:
        """extractFaces(faces, translation=None) -> self

        Detaches a set of faces from the rest of the mesh. The resulting
        mesh will contain one more independant piece of geometry.
        """

    def extrudeEdges(self, *args: Any, **kwargs: Any) -> Any:
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

    def extrudeFaces(self, *args: Any, **kwargs: Any) -> Any:
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

    def freeCachedIntersectionAccelerator(self, *args: Any, **kwargs: Any) -> Any:
        """freeCachedIntersectionAccelerator() -> self

        If the mesh has a cached intersection accelerator structure, then
        this routine forces it to be deleted. Ordinarily, these structures
        are cached so that series of calls to the closestIntersection(),
        allIntersections(), and anyIntersection() methods can reuse the same
        structure. Once the client is finished with these intersection
        operations, however, they are responsible for freeing the acceleration
        structure, which is what this method does.
        """

    def generateSmoothMesh(self, *args: Any, **kwargs: Any) -> Any:
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

    def getAssignedUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getAssignedUVs(uvSet='') -> (counts, uvIds)

        Returns a tuple containing all of the UV assignments for the specified
        UV set. The first element of the tuple is an array of counts giving
        the number of UVs assigned to each face of the mesh. The count will
        either be zero, indicating that that face's vertices do not have UVs
        assigned, or else it will equal the number of the face's vertices.
        The second element of the tuple is an array of UV IDs for all of the
        face-vertices which have UVs assigned.
        """

    def getAssociatedColorSetInstances(self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedColorSetInstances(colorSet) -> MIntArray

        Returns the instance numbers associated with the specified Color set.
        If the color map is shared across all instances, an empty array will
        be returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """

    def getAssociatedUVSetInstances(self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedUVSetInstances(uvSet) -> MIntArray

        Returns the instance numbers associated with the specified UV set.
        If the uv map is shared across all instances, an empty array will be
        returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """

    def getAssociatedUVSetTextures(self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedUVSetTextures(uvSet) -> MObjectArray

        Returns the texture nodes which are using the specified UV set. If
        the texture has a 2d texture placement, the texture, and not the
        placement will be returned.

        This method will only work if the functionset is attached to a mesh
        node. It will raise RuntimeError if the functionset is attached to
        mesh data.
        """

    def getBinaryBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def getBinormals(self, *args: Any, **kwargs: Any) -> Any:
        """getBinormals(space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns the binormal vectors for all face-vertices.

        This method is not threadsafe.
        """

    def getBlindDataAttrNames(self, *args: Any, **kwargs: Any) -> Any:
        """getBlindDataAttrNames(blindDataId) -> ((longName, shortName, typeName), ...)

        Returns a tuple listing the attributes of the given blind data type.
        Each element of the tuple is itself a tuple containing the long
        name, short name and type name of the attribute. Type names can be
        'int', 'float', 'double', 'boolean', 'string' or 'binary'.
        """

    def getBlindDataTypes(self, *args: Any, **kwargs: Any) -> Any:
        """getBlindDataTypes(MFn Type constant) -> MIntArray

        Returns all the blind data ID's associated with the given component
        type on this mesh.
        """

    def getBoolBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def getClosestNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getClosestNormal(MPoint, space=MSpace.kObject) -> (MVector, int)

        Returns a tuple containing the normal at the closest point on the
        mesh to the given point and the ID of the face in which that closest
        point lies.
        """

    def getClosestPoint(self, *args: Any, **kwargs: Any) -> Any:
        """getClosestPoint(MPoint, space=MSpace.kObject) -> (MPoint, int)

        Returns a tuple containing the closest point on the mesh to the
        given point and the ID of the face in which that closest point lies.

        This method is not threadsafe.
        """

    def getClosestPointAndNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getClosestPointAndNormal(MPoint, space=MSpace.kObject)
          -> (MPoint, MVector, int)

        Returns a tuple containing the closest point on the mesh to the
        given point, the normal at that point, and the ID of the face in
        which that point lies.

        This method is not threadsafe.
        """

    def getClosestUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getClosestUVs(u, v, uvSet='') -> MIntArray

        Returns the IDs of the UVs which are nearest in uv space to the
        given texture coordinate in the specified UV set. All these UVs
        locate at the same distance to the given coordinate.
        """

    def getColor(self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorId, colorSet='') -> MColor

        Returns a color from a colorSet. Raises IndexError if the colorId is
        out of range.
        """

    def getColorIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndex(faceId, localVertexId, colorSet='') -> int

        Returns the index into the specified colorSet of the color used by a
        specific face-vertex. This can be used to index into the sequence
        returned by getColors().
        """

    def getColorRepresentation(self, *args: Any, **kwargs: Any) -> Any:
        """getColorRepresentation(colorSet) -> Color Representation constant

        Returns the Color Representation used by the specified color set.
        """

    def getColorSetFamilyNames(self, *args: Any, **kwargs: Any) -> Any:
        """getColorSetFamilyNames() -> (string, ...)

        Returns the names of all of the color set families on this object. A
        color set family is a set of per-instance sets with the same name
        with each individual set applying to one or more instances. A set
        which is shared across all instances will be the sole member of its
        family.

        Given a color set family name, getColorSetsInFamily() may be used to
        determine the names of the associated individual sets.
        """

    def getColorSetNames(self, *args: Any, **kwargs: Any) -> Any:
        """getColorSetNames() -> (string, ...)

        Returns the names of all the color sets on this object.
        """

    def getColorSetsInFamily(self, *args: Any, **kwargs: Any) -> Any:
        """getColorSetsInFamily(familyName) -> (string, ...)

        Returns the names of all of the color sets that belong to the
        specified family. Per-instance sets will have multiple sets in a
        family, with each individual set applying to one or more instances.
        A set which is shared across all instances will be the sole member
        of its family and will share the same name as its family.
        """

    def getColors(self, *args: Any, **kwargs: Any) -> Any:
        """getColors(colorSet='') -> MColorArray

        Returns all of the colors in a colorSet. If no colorSet is specified
        then the default colorSet is used.

        Use the index returned by getColorIndex() to access the returned
        array.
        """

    def getConnectedShaders(self, *args: Any, **kwargs: Any) -> Any:
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

    def getCreaseEdges(self, *args: Any, **kwargs: Any) -> Any:
        """getCreaseEdges() -> (MUintArray, MDoubleArray)

        Returns a tuple containing two arrays. The first contains the mesh-
        relative/global IDs of the mesh's creased edges and the second
        contains the associated crease data.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned
        by Pixar(R).
        """

    def getCreaseVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getCreaseVertices() -> (MUintArray, MDoubleArray)

        Returns a tuple containing two arrays. The first contains the mesh-
        relative/global IDs of the mesh's creased vertices and the second
        contains the associated crease data.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned
        by Pixar(R).
        """

    def getDoubleBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def getEdgeVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getEdgeVertices(edgeId) -> (int, int)

        Returns a tuple containing the mesh-relative/global IDs of the
        edge's two vertices. The indices can be used to refer to the
        elements in the array returned by the getPoints() method.
        """

    def getFaceAndVertexIndices(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceAndVertexIndices(faceVertexIndex, localVertex=True) -> (int, int)

        Returns a tuple containg the faceId and vertexIndex represented by
        the given face-vertex index. This is the reverse of the operation
        performed by getFaceVertexIndex().

        If localVertex is True then the returned vertexIndex is the face-
        relative/local index, otherwise it is the mesh-relative/global index.
        """

    def getFaceNormalIds(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceNormalIds(faceId) -> MIntArray

        Returns the IDs of the normals for all the vertices of a given face.
        These IDs can be used to index into the arrays returned by getNormals().
        """

    def getFaceUVSetNames(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceUVSetNames(faceId) -> (string, ...)

        Returns the names of all of the uv sets mapped to the specified face.

        This method is not threadsafe. 
        """

    def getFaceVertexBinormal(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexBinormal(faceId, vertexId, space=MSpace.kObject, uvSet='') -> MVector

        Returns the binormal vector at a given face vertex.

        This method is not threadsafe.
        """

    def getFaceVertexBinormals(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexBinormals(faceId, space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns all the per-vertex-per-face binormals for a given face.

        This method is not threadsafe.
        """

    def getFaceVertexColors(self, *args: Any, **kwargs: Any) -> Any:
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

    def getFaceVertexIndex(self, *args: Any, **kwargs: Any) -> Any:
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

    def getFaceVertexNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexNormal(faceId, vertexId, space=MSpace.kObject) -> MVector

        Returns the per-vertex-per-face normal for a given face and vertex.

        This method is not threadsafe.
        """

    def getFaceVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexNormals(faceId, space=MSpace.kObject) -> MFloatVectorArray

        Returns the normals for a given face.

        This method is not threadsafe.
        """

    def getFaceVertexTangent(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexTangent(faceId, vertexId, space=MSpace.kObject, uvSet='') -> MVector

        Return the normalized tangent vector at a given face vertex.

        The tangent is defined as the surface tangent of the polygon running
        in the U direction defined by the uv map.
        This method is not threadsafe.
        """

    def getFaceVertexTangents(self, *args: Any, **kwargs: Any) -> Any:
        """getFaceVertexTangents(faceId, space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Returns all the per-vertex-per-face tangents for a given face.

        The tangent is defined as the surface tangent of the polygon running
        in the U direction defined by the uv map.

        This method is not threadsafe.
        """

    def getFloatBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def getFloatPoints(self, *args: Any, **kwargs: Any) -> Any:
        """getFloatPoints(space=MSpace.kObject) -> MFloatPointArray

        Returns an MFloatPointArray containing the mesh's vertices.
        """

    def getHoles(self, *args: Any, **kwargs: Any) -> Any:
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

    def getIntBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def getInvisibleFaces(self, *args: Any, **kwargs: Any) -> Any:
        """getInvisibleFaces() -> MUintArray

        Returns the invisible faces of the mesh. Invisible faces are like
        lightweight holes in that they are not rendered but do not require
        additional geometry the way that holes do. They have the advantage
        over holes that if the mesh is smoothed then their edges will be
        smoothed as well, while holes will retain their hard edges.

        Invisible faces can be set using the setInvisibleFaces() method or
        the polyHole command.
        """

    def getMeshShellsIds(self, *args: Any, **kwargs: Any) -> Any:
        """getMeshShellsIds(compType) -> (int, MIntArray)

        Returns a tuple containing describing how the specified component type items
        are grouped into shells. The first element of the tuple is the number
        of distinct shells. The second element of the tuple is an array of
        shell indices, one per component, indicating which shell that component is part of.
        """

    def getNormalIds(self, *args: Any, **kwargs: Any) -> Any:
        """getNormalIds() -> (MIntArray, MIntArray)

        Returns the normal IDs for all of the mesh's polygons as a tuple of
        two int arrays. The first array contains the number of vertices for
        each polygon and the second contains the normal IDs for each polygon-
        vertex. These IDs can be used to index into the array returned by
        getNormals().
        """

    def getNormals(self, *args: Any, **kwargs: Any) -> Any:
        """getNormals(space=MSpace.kObject) -> MFloatVectorArray

        Returns a copy of the mesh's normals. The normals are the per-polygon
        per-vertex normals. To find the normal for a particular vertex-face,
        use getFaceNormalIds() to get the index into the array.

        This method is not threadsafe.
        """

    def getPoint(self, *args: Any, **kwargs: Any) -> Any:
        """getPoint(vertexId, space=MSpace.kObject) -> MPoint

        Returns the position of specified vertex.
        """

    def getPointAtUV(self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtUV(faceId, u, v, space=MSpace.kObject, uvSet='', tolerance=0.0) -> MPoint

        Returns the position of the point at the give UV value in the
        specified face.

        This method is not threadsafe.
        """

    def getPoints(self, *args: Any, **kwargs: Any) -> Any:
        """getPoints(space=MSpace.kObject) -> MPointArray

        Returns a copy of the mesh's vertex positions as an MPointArray.
        """

    def getPointsAtUV(self, *args: Any, **kwargs: Any) -> Any:
        """getPointsAtUV(u, v, space=MSpace.kObject, uvSet='', tolerance=0.001) -> (MIntArray, MPointArray)

        Returns the polygon ids and positions of points at the given UV position on the mesh.
        """

    def getPolygonNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonNormal(polygonId, space=MSpace.kObject) -> MVector

        Returns the per-polygon normal for the given polygon.

        This method is not threadsafe.
        """

    def getPolygonTriangleVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonTriangleVertices(polygonId, triangleId) -> (int, int, int)

        Returns the mesh-relative/global IDs of the 3 vertices of the
        specified triangle of the specified polygon. These IDs can be used
        to index into the arrays returned by getPoints() and getFloatPoints().
        """

    def getPolygonUV(self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonUV(polygonId, vertexId, uvSet='') -> (float, float)

        Returns a tuple containing the U and V values at a specified vertex
        of a specified polygon.

        This method is not threadsafe.
        """

    def getPolygonUVid(self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonUVid(polygonId, vertexId, uvSet='') -> int

        Returns the ID of the UV at a specified vertex of a specified polygon.

        This method is not threadsafe.
        """

    def getPolygonVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getPolygonVertices(polygonId) -> MIntArray

        Returns the mesh-relative/global vertex IDs the specified polygon.
        These IDs can be used to index into the arrays returned by getPoints()
        and getFloatPoints().
        """

    def getSmoothMeshDisplayOptions(self, *args: Any, **kwargs: Any) -> Any:
        """getSmoothMeshDisplayOptions() -> MMeshSmoothOptions

        Returns the options currently in use when smoothing the mesh for display.
        """

    def getStringBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def getTangentId(self, *args: Any, **kwargs: Any) -> Any:
        """getTangentId(faceId, vertexId) -> int

        Returns the ID of the tangent for a given face and vertex.
        """

    def getTangents(self, *args: Any, **kwargs: Any) -> Any:
        """getTangents(space=MSpace.kObject, uvSet='') -> MFloatVectorArray

        Return the tangent vectors for all face vertices. The tangent is
        defined as the surface tangent of the polygon running in the U
        direction defined by the uv map.

        This method is not threadsafe.
        """

    def getTriangleOffsets(self, *args: Any, **kwargs: Any) -> Any:
        """getTriangleOffsets() -> (MIntArray, MIntArray)

        Returns the number of triangles for every polygon face and the
        offset into the vertex indices array for each triangle vertex (see getVertices()).
        The triangleVertices array holds each vertex for each triangle in sequence,
        so it has three times as many elements as there are triangles.
        (i.e. three times the sum of the elements of the triangleCounts array)
        """

    def getTriangles(self, *args: Any, **kwargs: Any) -> Any:
        """getTriangles() -> (MIntArray, MIntArray)

        Returns a tuple describing the mesh's triangulation. The first
        element of the tuple is an array giving the number of triangles for
        each of the mesh's polygons. The second tuple gives the ids of the
        vertices of all the triangles.
        """

    def getUV(self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvId, uvSet='') -> (float, float)

        Returns a tuple containing the u and v values of the specified UV.
        """

    def getUVAtPoint(self, *args: Any, **kwargs: Any) -> Any:
        """getUVAtPoint(point, space=MSpace.kObject, uvSet='') -> (float, float, int)

        Returns a tuple containing the u and v coordinates of the point on
        the mesh closest to the given point, and the ID of the face
        containing that closest point.

        This method is not threadsafe.
        """

    def getUVBorderEdges(self, *args: Any, **kwargs: Any) -> Any:
        """getUVBorderEdges(setId) -> MIntArray

        Retrieves the edge indices for edges lying on a UV border.
        """

    def getUVSetFamilyNames(self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetFamilyNames() -> (string, ...)

        Returns the names of all of the uv set families on this object. A
        uv set family is a set of per-instance sets with the same name
        with each individual set applying to one or more instances. A set
        which is shared across all instances will be the sole member of its
        family.

        Given a uv set family name, getUVSetsInFamily() may be used to
        determine the names of the associated individual sets.
        """

    def getUVSetNames(self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetNames() -> (string, ...)

        Returns the names of all the uv sets on this object.
        """

    def getUVSetsInFamily(self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetsInFamily(familyName) -> (string, ...)

        Returns the names of all of the uv sets that belong to the
        specified family. Per-instance sets will have multiple sets in a
        family, with each individual set applying to one or more instances.
        A set which is shared across all instances will be the sole member
        of its family and will share the same name as its family.
        """

    def getUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getUVs(uvSet='') -> (MFloatArray, MFloatArray)

        Returns a tuple containing an array of U values and an array of V
        values, representing all of the UVs for the given UV set.
        """

    def getUvShellsIds(self, *args: Any, **kwargs: Any) -> Any:
        """getUvShellsIds(uvSet='') -> (int, MIntArray)

        Returns a tuple containing describing how the specified UV set's UVs
        are grouped into shells. The first element of the tuple is the number
        of distinct shells. The second element of the tuple is an array of
        shell indices, one per uv, indicating which shell that uv is part of.
        """

    def getVertexColors(self, *args: Any, **kwargs: Any) -> Any:
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

    def getVertexNormal(self, *args: Any, **kwargs: Any) -> Any:
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

    def getVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
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

    def getVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getVertices() -> (MIntArray, MIntArray)

        Returns the mesh-relative/global vertex IDs for all of the mesh's
        polygons as a tuple of two int arrays. The first array contains the
        number of vertices for each polygon and the second contains the mesh-
        relative IDs for each polygon-vertex. These IDs can be used to index
        into the arrays returned by getPoints() and getFloatPoints().
        """

    def globalIntersectionAcceleratorsInfo(self, *args: Any, **kwargs: Any) -> Any:
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

    def hasAlphaChannels(self, *args: Any, **kwargs: Any) -> Any:
        """hasAlphaChannels(colorSet) -> bool

        Returns True if the color set has an alpha channel.
        """

    def hasBlindData(self, *args: Any, **kwargs: Any) -> Any:
        """hasBlindData(compType, compId=None, blindDataId=None) -> bool

        Returns true if any component of the given type on this mesh has
        blind data. If a component ID is provided then only that particular
        component is checked. If a blind data ID is provided then only blind
        data of that type is checked. 
        """

    def hasColorChannels(self, *args: Any, **kwargs: Any) -> Any:
        """hasColorChannels(colorSet) -> bool

        Returns True if the color set has RGB channels.
        """

    def intersectFaceAtUV(self, *args: Any, **kwargs: Any) -> Any:
        """intersectFaceAtUV(u, v, uvSet='') -> int

        Returns the IDs of the UVs on this surface which are nearest
        in uv space to the given uv set and coordinate.All these UVs
        locate at the same distance to the given coordinate.

        This method is not threadsafe.
        """

    def isBlindDataTypeUsed(self, *args: Any, **kwargs: Any) -> Any:
        """isBlindDataTypeUsed(blindDataId) -> bool

        Returns True if the blind data type is already in use anywhere in the scene.
        """

    def isColorClamped(self, *args: Any, **kwargs: Any) -> Any:
        """isColorClamped(colorSet) -> bool

        Returns True if the color sets RGBA components are clamped to the
        range 0 to 1.
        """

    def isColorSetPerInstance(self, *args: Any, **kwargs: Any) -> Any:
        """isColorSetPerInstance(colorSet) -> bool

        Returns True if the color set is per-instance, and False if it is
        shared across all instances.
        """

    def isEdgeSmooth(self, *args: Any, **kwargs: Any) -> Any:
        """isEdgeSmooth(edgeId) -> bool

        Returns True if the edge is smooth, False if it is hard.
        """

    def isNormalLocked(self, *args: Any, **kwargs: Any) -> Any:
        """isNormalLocked(normalId) -> bool

        Returns True if the normal is locked, False otherwise.
        """

    def isPolygonConvex(self, *args: Any, **kwargs: Any) -> Any:
        """isPolygonConvex(faceId) -> bool

        Returns True if the polygon is convex, False if it is concave.
        """

    def isPolygonUVReversed(self, *args: Any, **kwargs: Any) -> Any:
        """isPolygonUVReversed(faceId) -> bool

        Returns True if the texture coordinates (uv's) for specified polygon are
        reversed (clockwise), False if they are not reversed (counter clockwise).
        """

    def isRightHandedTangent(self, *args: Any, **kwargs: Any) -> Any:
        """isRightHandedTangent(tangentId, uvSet='') -> bool

        Returns True if the normal, tangent, and binormal form a right handed
        coordinate system, False otherwise.
        """

    def isUVSetPerInstance(self, *args: Any, **kwargs: Any) -> Any:
        """isUVSetPerInstance(uvSet) -> bool

        Returns True if the UV set is per-instance, and False if it is shared
        across all instances.
        """

    kGeomBorder: int = -2
    kInstanceUnspecified: int = -1
    kIntersectTolerance: float = 1e-06
    kPointTolerance: float = 1e-10
    kUVBorder: int = -1
    def lockFaceVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """lockFaceVertexNormals(seq of faceIds, seq of vertIds) -> self

        Locks the normals for the given face/vertex pairs.
        """

    def lockVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """lockVertexNormals(sequence of vertIds) -> self

        Locks the shared normals for the specified vertices.
        """

    numColorSets: getset_descriptor = <attribute 'numColorSets' of 'OpenMaya.MFnMesh' objects>
    def numColors(self, *args: Any, **kwargs: Any) -> Any:
        """numColors(colorSet='') -> int

        Returns the number of colors in the given color set. If no color set
        is specified then the mesh's current color set will be used.
        """

    numEdges: getset_descriptor = <attribute 'numEdges' of 'OpenMaya.MFnMesh' objects>
    numFaceVertices: getset_descriptor = <attribute 'numFaceVertices' of 'OpenMaya.MFnMesh' objects>
    numNormals: getset_descriptor = <attribute 'numNormals' of 'OpenMaya.MFnMesh' objects>
    numPolygons: getset_descriptor = <attribute 'numPolygons' of 'OpenMaya.MFnMesh' objects>
    numUVSets: getset_descriptor = <attribute 'numUVSets' of 'OpenMaya.MFnMesh' objects>
    def numUVs(self, *args: Any, **kwargs: Any) -> Any:
        """numUVs(uvSet='') -> int

        Returns the number of UVs (texture coordinates) in the given UV set.
        If no UV set is specified then the mesh's current UV set will be used.
        """

    numVertices: getset_descriptor = <attribute 'numVertices' of 'OpenMaya.MFnMesh' objects>
    def onBoundary(self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary(faceId) -> bool

        Returns true if the face is on the border of the mesh, meaning that
        one or more of its edges is a border edge.
        """

    def polygonVertexCount(self, *args: Any, **kwargs: Any) -> Any:
        """polygonVertexCount(faceId) -> int

        Returns the number of vertices in the given polygon. Raises
        ValueError if the polygon ID is invalid.
        """

    def removeFaceColors(self, *args: Any, **kwargs: Any) -> Any:
        """removeFaceColors(seq of faceIds) -> self

        Removes colors from all vertices of the specified faces.
        """

    def removeFaceVertexColors(self, *args: Any, **kwargs: Any) -> Any:
        """removeFaceVertexColors(seq of faceIds, seq of vertexIds) -> self

        Removes colors from the specified face/vertex pairs.
        """

    def removeVertexColors(self, *args: Any, **kwargs: Any) -> Any:
        """removeVertexColors(seq of vertexIds) -> self

        Removes colors from the specified vertices in all of the faces which
        share those vertices.
        """

    def renameUVSet(self, *args: Any, **kwargs: Any) -> Any:
        """renameUVSet(origName, newName, modifier=None) -> self

        Renames a UV set. The set must exist and the new name cannot be the
        same as that of an existing set.

        This method is only valid for functionsets which are attached to mesh
        nodes, not mesh data.
        """

    def setBinaryBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def setBoolBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def setColor(self, *args: Any, **kwargs: Any) -> Any:
        """setColor(colorId, MColor, colorSet='', rep=kRGBA) -> self

        Sets a color in the specified colorSet. If no colorSet is given the
        current colorSet will be used. If the colorId is greater than or
        equal to numColors() then the colorSet will be grown to accommodate
        the specified color.
        """

    def setColors(self, *args: Any, **kwargs: Any) -> Any:
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

    def setCreaseEdges(self, *args: Any, **kwargs: Any) -> Any:
        """setCreaseEdges(edgeIds, seq of float) -> self


        Sets the specified edges of the mesh as crease edges.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned by
        Pixar(R).
        """

    def setCreaseVertices(self, *args: Any, **kwargs: Any) -> Any:
        """setCreaseVertices(edgeIds, seq of float) -> self


        Sets the specified edges of the mesh as crease edges.

        Please note that to make effective use of the creasing variable in
        software outside of Maya may require a license under patents owned by
        Pixar(R).
        """

    def setCurrentColorSetName(self, *args: Any, **kwargs: Any) -> Any:
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

    def setCurrentUVSetName(self, *args: Any, **kwargs: Any) -> Any:
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

    def setDoubleBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def setEdgeSmoothing(self, *args: Any, **kwargs: Any) -> Any:
        """setEdgeSmoothing(edgeId, smooth=True) -> self

        Sets the specified edge to be hard or smooth. You must use the
        cleanupEdgeSmoothing() method after all the desired edges on your
        mesh have had setEdgeSmoothing() done. Use the updateSurface() method
        to indicate the mesh needs to be redrawn.
        """

    def setEdgeSmoothings(self, *args: Any, **kwargs: Any) -> Any:
        """setEdgeSmoothings(edgeIds, smooths) -> self

        Sets the specified edges to be hard or smooth. You must use the
        cleanupEdgeSmoothing() method after all the desired edges on your
        mesh have had setEdgeSmoothings() done. Use the updateSurface() method
        to indicate the mesh needs to be redrawn.
        """

    def setFaceColor(self, *args: Any, **kwargs: Any) -> Any:
        """setFaceColor(color, faceId, rep=kRGBA) -> self

        Sets the face-vertex color for all vertices on this face.
        """

    def setFaceColors(self, *args: Any, **kwargs: Any) -> Any:
        """setFaceColors(colors, faceIds, rep=kRGBA) -> self

        Sets the colors of the specified faces. For each face in the faceIds
        sequence the corresponding color from the colors sequence will be
        applied to all of its vertices.
        """

    def setFaceVertexColor(self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexColor(color, faceId, vertexId, modifier=None, rep=kRGBA) -> self

        Sets a face-specific normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """

    def setFaceVertexColors(self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexColors(colors, faceIds, vertexIds, modifier=None, rep=kRGBA) -> self

        Sets the colors of the specified face/vertex pairs.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """

    def setFaceVertexNormal(self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexNormal(normal, faceId, vertexId, space=MSpace.kObject, modifier=None) -> self

        Sets a face-specific normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """

    def setFaceVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """setFaceVertexNormal(normals, faceIds, vertexIds, space=MSpace.kObject) -> self

        Sets normals for the given face/vertex pairs.
        """

    def setFloatBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def setIntBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def setInvisibleFaces(self, *args: Any, **kwargs: Any) -> Any:
        """setInvisibleFaces(faceIds, makeVisible=False) -> self

        Sets the specified faces of the mesh to be visible or invisible. See
        the getInvisibleFaces() method for a description of invisible faces.
        """

    def setIsColorClamped(self, *args: Any, **kwargs: Any) -> Any:
        """setIsColorClamped(colorSet, clamped) -> self

        Sets whether the color set's RGBA components should be clamped to the
        range 0 to 1.
        """

    def setNormals(self, *args: Any, **kwargs: Any) -> Any:
        """setNormals(normals, space=MSpace.kObject) -> self

        Sets the mesh's normals (user normals).
        """

    def setPoint(self, *args: Any, **kwargs: Any) -> Any:
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

    def setPoints(self, *args: Any, **kwargs: Any) -> Any:
        """setPoints(points, space=MSpace.kObject) -> self

        Sets the positions of the mesh's vertices. The positions may be
        given as a sequence of MFloatPoint's or a sequence of MPoint's, but
        not a mix of the two.
        """

    def setSmoothMeshDisplayOptions(self, *args: Any, **kwargs: Any) -> Any:
        """setSmoothMeshDisplayOptions(MMeshSmoothOptions) -> self

        Sets the options to use when smoothing the mesh for display.
        """

    def setSomeColors(self, *args: Any, **kwargs: Any) -> Any:
        """setSomeColors(colorIds, colors, colorSet='', rep=kRGBA) -> self

        Sets specific colors in a colorSet.

        If the largest colorId in the sequence is larger than numColors()
        then the colorSet will be grown to accommodate the new color values.
        If you have added new colorIds, you can call assignColors to assign
        the colorIds to the geometry. If you are modifying existing colors,
        they will already be referenced by the existing mesh data.
        """

    def setSomeUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def setStringBlindData(self, *args: Any, **kwargs: Any) -> Any:
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

    def setUV(self, *args: Any, **kwargs: Any) -> Any:
        """setUV(uvId, u, v, uvSet='') -> self

        Sets the specified texture coordinate.

        The uvId is the element in the uv list that will be set. If the uvId
        is greater than or equal to numUVs() then the uv list will be grown
        to accommodate the specified uv. If the UV being added is new, thenyou must call one of the assignUV methods in order to update the
        geometry.
        """

    def setUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def setVertexColor(self, *args: Any, **kwargs: Any) -> Any:
        """setVertexColor(color, vertexId, modifier=None, rep=kRGBA) -> self

        Sets the color for a vertex in all the faces which share it.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """

    def setVertexColors(self, *args: Any, **kwargs: Any) -> Any:
        """setVertexColors(colors, vertexIds, modifier=None, rep=kRGBA) -> self

        Sets the colors of the specified vertices. For each vertex in the
        vertexIds sequence, the corresponding color from the colors sequence
        will be applied to the vertex in all of the faces which share it.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """

    def setVertexNormal(self, *args: Any, **kwargs: Any) -> Any:
        """setVertexNormal(normal, vertexId, space=MSpace.kObject, modifier=None) -> self

        Sets the shared normal at a vertex.

        If 'modifier' (MDGModifier) is provided then the operation will be
        added to the modifier and will not take effect until the modifier's
        doIt() is called. Otherwise it will take effect immediately.
        """

    def setVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """setVertexNormal(normals, vertexIds, space=MSpace.kObject) -> self

        Sets the shared normals for the given vertices.
        """

    def sortIntersectionFaceTriIds(self, *args: Any, **kwargs: Any) -> Any:
        """sortIntersectionFaceTriIds(faceIds, triIds=none) -> self

        Convenience routine for sorting faceIds or face/triangle ids before
        passing them into the closestIntersection(), allIntersections(), or
        anyIntersection() methods. When using an acceleration structure with
        an intersection operation it is essential that any faceId or
        faceId/triId arrays be sorted properly to ensure optimal performance.

        Both arguments must be MIntArray's.
        """

    def split(self, *args: Any, **kwargs: Any) -> Any:
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

    def subdivideEdges(self, *args: Any, **kwargs: Any) -> Any:
        """subdivideEdges(edges, numDivisions) -> self

        Subdivides edges at regular intervals. For example, if numDivisions
        is 2 then two equally-spaced vertices will be added to each of the
        specified edges: one 1/3 of the way along the edge and a second 2/3
        of the way along the edge.
        """

    def subdivideFaces(self, *args: Any, **kwargs: Any) -> Any:
        """subdivideFaces(faces, numDivisions) -> self

        Subdivides each specified face into a grid of smaller faces.
        Triangles are subdivided into a grid of smaller triangles and quads
        are subdivided into a grid of smaller quads. Faces with more than
        four edges are ignored.

        The numDivisions parameter tells how many times to subdivide each
        edge of the face. Internal points and edges are introduced as needed
        to create a grid of smaller faces.
        """

    def syncObject(self, *args: Any, **kwargs: Any) -> Any:
        """syncObject() -> self

        If a non-api operation happens that many have changed the
        underlying Maya object attached to this functionset, calling this
        method will make sure that the functionset picks up those changes.
        In particular this call should be used after calling mel commands
        which might affect the mesh. Note that this only applies when the
        functionset is attached to a mesh node. If it's attached to mesh
        data the it is not necessary to call this method.
        """

    def uniformGridParams(self, *args: Any, **kwargs: Any) -> Any:
        """uniformGridParams(xDiv, yDiv, zDiv) -> MMeshIsectAccelParams

        Creates an object which specifies a uniform voxel grid structure
        which can be used by the intersection routines to speed up their
        operation. This object specifies the number of voxel cells to be
        used in the x, y, and z dimensions. The grid acceleration structure
        will be cached with the mesh, so that if the same MMeshIsectAccelParams
        configuration is used on the next intersect call, the acceleration
        structure will not need to be rebuilt.
        """

    def unlockFaceVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """unlockFaceVertexNormals(seq of faceIds, seq of vertIds) -> self

        Unlocks the normals for the given face/vertex pairs.
        """

    def unlockVertexNormals(self, *args: Any, **kwargs: Any) -> Any:
        """unlockVertexNormals(sequence of vertIds) -> self

        Unlocks the shared normals for the specified vertices.
        """

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signal that this polygonal mesh has changed and needs to be redrawn.
        """


class MFnMeshData(MFnGeometryData):
    """MFnMeshData allows the creation and manipulation of Mesh
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnMeshData object

    __init__(MObject)
    Initializes a new MFnMeshData function set, attached
    to the specified object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new mesh data object, attaches it to this function set
        and returns an MObject which references it.
        """


class MFnMessageAttribute(MFnAttribute):
    """Functionset for creating and working with message attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new message attribute, attaches it to the function set and returns it as an MObject."""


class MFnNumericAttribute(MFnAttribute):
    """Functionset for creating and working with numeric attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def child(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the specified child attribute of the parent attribute currently attached to the function set."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new simple or compound numeric attribute, attaches it to the function set and returns it in an MObject."""

    def createAddr(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new address attribute, attaches it to the function set and returns it in an MObject."""

    def createColor(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new color attribute, attaches it to the function set and returns it in an MObject."""

    def createPoint(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new 3D point attribute, attaches it to the function set and returns it in an MObject."""

    default: getset_descriptor = <attribute 'default' of 'OpenMaya.MFnNumericAttribute' objects>
    def getMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard maximum value(s)."""

    def getMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard minimum value(s)."""

    def getSoftMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft maximum value."""

    def getSoftMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft minimum value."""

    def hasMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a hard maximum value has been specified for the attribute."""

    def hasMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a hard minimum value has been specified for the attribute."""

    def hasSoftMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a soft maximum value has been specified for the attribute."""

    def hasSoftMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if a soft minimum value has been specified for the attribute."""

    def numericType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the numeric type of the attribute currently attached to the function set."""

    def setMax(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard maximum value(s)."""

    def setMin(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard minimum value(s)."""

    def setSoftMax(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft maximum value."""

    def setSoftMin(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft minimum value."""


class MFnNumericData(MFnData):
    """Function set for non-simple numeric node data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new numeric data object."""

    def getData(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the attached data object's data."""

    def numericType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of data in the attached data object."""

    def setData(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the data in the attached data object."""


class MFnNurbsCurve(MFnDagNode):
    """NURBS (Non-Uniform Rational B-Spline) curve function set.

    The shape of a NURBS curve is defined by an array of CVs
    (control vertices), an array of knot values, a degree, and a
    form.  There are 3 possible 'forms' for the curve: open,
    closed and periodic.

    The open and closed forms are quite similar, and in fact a
    closed curve will become an open curve if either the first
    or last CV is moved so that they are no longer coincident.
    To create an open or closed curve of degree N with M spans,
    you must provide M+N CVs.  This implies that for a degree N
    curve, you must specify at least N+1 CVs to get a curve with
    a single span.

    The number of knots required for a curve is M + 2N - 1. If
    you want the curve to start exactly at the first CV and end
    exactly at the last CV, then the knot vector must be
    structured to have degree N 'multiplicity' at the beginning
    and end.  This means that the first N knots must be
    identical, and the last N knots must be identical.

    A periodic curve is a special case of a closed curve.
    Instead of having just the first and last CVs coincident,
    the last N CVs in the curve must overlap the first N CVs.
    This results in a curve with no tangent break at the seam
    where the ends meet.  The last N CVs in a periodic curve are
    permanently bound to the first N CVs, and Maya will not
    allow those last N CVs to be repositioned.  If one or more
    of the first N CVs of the curve are repositioned, the
    overlapping CV's will remain bound, and will also be moved.

    In order to create a periodic curve, you must specify at
    least 2N+1 CVs, so that that last N can overlap the first N
    and you still have 1 non-overlapping CV left.  The number of
    CVs required to create a periodic curve is still N+M (with a
    lower limit of 2N+1), but you must ensure that the positions
    of the last N CVs are identical to the positions of the
    first N.

    You still need M + 2N - 1 knots for a periodic curve, but
    the knot values required are more restrictive than for open
    or closed curves because of the overlap at the ends, The
    difference between the first N pairs of knots values should
    be equal to the difference between the last N pairs.
    Additionally there can be no knot multiplicity at the ends
    of the curve, because that would compromise the tangent
    continuity property. So an example knot sequence could begin
    with knots at { -(N-2), -(N-1), ... , 0}.

    Note that some third party applications use a different
    format for knots, where the number of knots required for a
    curve is M+2N+1 rather than M+2N-1 as used in Maya. Both
    knot representations are equivalent mathematically. To
    convert from one of these external representations into the
    Maya representation, simply omit the first and last knots
    from the external representation when creating the Maya
    representation. To convert from the Maya representation into
    the external representation, add two new knots at the
    beginning and end of the Maya knot sequence. The value of
    these new knots depends on the existing knot sequence. For a
    knot sequence with multiple end knots, simply duplicate the
    existing first and last knots once more, for example:

    Maya representation: {0,0,0,...,N,N,N}
    External representation: {0,0,0,0,...,N,N,N,N}

    For a knot sequence with uniform end knots, create the new
    knots offset at an interval equal to the existing first and
    last knot intervals, for example:

    Maya representation: {0,1,2,...,N,N+1,N+2}
    External representation: {-1,0,1,2,...,N,N+1,N+2,N+3}
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def area(self, *args: Any, **kwargs: Any) -> Any:
        """area(tolerance=kPointTolerance) -> float

        Returns the area bounded by the curve. The curve must be closed and
        planar. A value of 0.0 will be returned if area cannot be determined.

        * tolerance (float) - Amount of error allowed in the calculation
        """

    def closestPoint(self, *args: Any, **kwargs: Any) -> Any:
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

    def copy(self, *args: Any, **kwargs: Any) -> Any:
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

    def create(self, *args: Any, **kwargs: Any) -> Any:
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

    def createWithEditPoints(self, *args: Any, **kwargs: Any) -> Any:
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

    def cvPosition(self, *args: Any, **kwargs: Any) -> Any:
        """cvPosition(index, space=kObject) -> MPoint

        Returns the position of a single control vertex.

        * index (int) - index of the CV to return
        * space (int) - an MSpace constant giving the coordinate space in
                        which the point is given
        """

    def cvPositions(self, *args: Any, **kwargs: Any) -> Any:
        """cvPositions(space=kObject) -> MPointArray

        Returns the positions of all of the curve's control vertices.

        * space (int) - an MSpace constant giving the coordinate space in
                        which the point is given
        """

    def cvs(self, *args: Any, **kwargs: Any) -> Any:
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

    degree: getset_descriptor = <attribute 'degree' of 'OpenMaya.MFnNurbsCurve' objects>
    def distanceToPoint(self, *args: Any, **kwargs: Any) -> Any:
        """distanceToPoint(point, space=kObject) -> float

        Returns the distance from the given point to the point on the curve
        which is closest to it.

        * point (MPoint) - the point to calculate the distance to
        * space (int)    - an MSpace constant giving the coordinate space in
                           which the point is given
        """

    def findLengthFromParam(self, *args: Any, **kwargs: Any) -> Any:
        """findLengthFromParam(param) -> float

        Returns the length along the curve corresponding to a given
        parameter value on the curve. If the length cannot be found for
        the given parameter value then a length of zero is returned.

        * param (float) - parameter value on the curve
        """

    def findParamFromLength(self, *args: Any, **kwargs: Any) -> Any:
        """findParamFromLength(length, tolerance=kFindParamTolerance) -> float

        Returns the parameter value corresponding to a given length along
        the curve. If the parameter value cannot be determined then the value
        for the end point of the curve is returned.

        * length (float) - distance along the curve
        * tolerance (float) - search tolerance
        """

    form: getset_descriptor = <attribute 'form' of 'OpenMaya.MFnNurbsCurve' objects>
    def getDerivativesAtParam(self, *args: Any, **kwargs: Any) -> Any:
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

    def getParamAtPoint(self, *args: Any, **kwargs: Any) -> Any:
        """getParamAtPoint(point, tolerance=kPointTolerance, space=kObject) -> float

        Returns the parameter value corresponding to the given point on the
        curve.

        * point    (MPoint) - point on curve.
        * tolerance (float) - max distance 'point' can be from the curve and
                              still be considered to lie on it.
        * space       (int) - an MSpace constant giving the coordinate space
                              in which the point is given
        """

    def getPointAtParam(self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtParam(param, space=kObject) -> MPoint

        Returns the point on the curve at the given parameter value.

        * param (float) - parameter value at which to find the point
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the point should be returned
        """

    hasHistoryOnCreate: getset_descriptor = <attribute 'hasHistoryOnCreate' of 'OpenMaya.MFnNurbsCurve' objects>
    def isParamOnCurve(self, *args: Any, **kwargs: Any) -> Any:
        """isParamOnCurve(param) -> bool

        Returns True if the given parameter value lies on the curve (i.e. is
        within the curve's knot domain), False otherwise.

        * param (float) - parameter value to test
        """

    isPlanar: getset_descriptor = <attribute 'isPlanar' of 'OpenMaya.MFnNurbsCurve' objects>
    def isPointOnCurve(self, *args: Any, **kwargs: Any) -> Any:
        """isPointOnCurve(point, tolerance=kPointTolerance, space=kObject) -> bool

        Returns True if the given point lies on the curve, False otherwise.

        * point    (MPoint) - point to test.
        * tolerance (float) - max distance 'point' can be from the curve and
                              still be considered to lie on it.
        * space       (int) - an MSpace constant giving the coordinate space
                              in which the point is given
        """

    kFindParamTolerance: float = 1e-06
    kPointTolerance: float = 0.001
    def knot(self, *args: Any, **kwargs: Any) -> Any:
        """knot(index) -> float

        Returns the parameter value of a single knot.

        * index (int) - index of the knot to return. These range from 0 to
                        (numKnots - 1)
        """

    knotDomain: getset_descriptor = <attribute 'knotDomain' of 'OpenMaya.MFnNurbsCurve' objects>
    def knots(self, *args: Any, **kwargs: Any) -> Any:
        """knots() -> MDoubleArray

        Returns the parameter values for all of the curve's knots.
        """

    def length(self, *args: Any, **kwargs: Any) -> Any:
        """length(tolerance=kPointTolerance) -> float

        Returns the arc length of this curve or 0.0 if it cannot be computed.

        * tolerance (float) - max error allowed in the calculation.
        """

    def makeMultipleEndKnots(self, *args: Any, **kwargs: Any) -> Any:
        """makeMultipleEndKnots() -> self

        Sets the curve's end knots to have full multiplicity. This ensures
        that the end points interpolate the first and last CVs (i.e. lie
        directly on them). It can also be used to convert a periodic curve
        to a closed curve.
        """

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """normal(param, space=kObject) -> MVector

        Returns the normal at the given parameter value on the curve. For
        degree 1 curves the normal is the vector at right angles to the
        curve that lies in the average plane of the curve. For higher degrees
        the normal is defined by the local curvature at the parameter.

        * param (float) - parameter value at which to find the normal
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the normal should be returned
        """

    numCVs: getset_descriptor = <attribute 'numCVs' of 'OpenMaya.MFnNurbsCurve' objects>
    numKnots: getset_descriptor = <attribute 'numKnots' of 'OpenMaya.MFnNurbsCurve' objects>
    numSpans: getset_descriptor = <attribute 'numSpans' of 'OpenMaya.MFnNurbsCurve' objects>
    planeNormal: getset_descriptor = <attribute 'planeNormal' of 'OpenMaya.MFnNurbsCurve' objects>
    def removeKnot(self, *args: Any, **kwargs: Any) -> Any:
        """removeKnot(param, removeAll=False) -> self

        Removes one or more knots at the given parameter value.

        If there are multiple knots at the parameter value then 'removeAll'
        determines which ones will be removed. If it is True then they will
        all be removed. If it is False then all but one will be removed.

        * param     (float) - parameter of the knot
        * removeAll  (bool) - how to handle multiple knots at the same param
        """

    def reverse(self, *args: Any, **kwargs: Any) -> Any:
        """reverse() -> self

        Reverses the direction of the curve.
        """

    def setCVPosition(self, *args: Any, **kwargs: Any) -> Any:
        """setCVPosition(index, point, space=kObject) -> self

        Sets the position of a single control vertex of the curve.

        * index    (int) - index of the cv
        * point (MPoint) - new position for the cv
        * space    (int) - an MSpace constant giving the coordinate space
                           in which the point is given
        """

    def setCVPositions(self, *args: Any, **kwargs: Any) -> Any:
        """setCVPositions(points, space=kObject) -> self

        Sets the positions of all of the curve's control vertices.

        * points (MPointArray or seq of MPoint)
                       - the points to be set. The array/sequence must
                         contain exactly the same number of points as the
                         curve has control vertices.
        * space  (int) - an MSpace constant giving the coordinate space
                         in which the points are given
        """

    def setKnot(self, *args: Any, **kwargs: Any) -> Any:
        """setKnot(index, param) -> self

        Sets the parameter value of a single knot.
        * index   (int) - index of the knot
        * param (float) - new parameter value for the knot
        """

    def setKnots(self, *args: Any, **kwargs: Any) -> Any:
        """setKnots(params, startIndex, endIndex) -> self

        Sets the parameter values of a contiguous group of knots.

        * params (MDoubleArray of seq of float)
                           - the parameter values to set, one per knot in
                             the range
        * startIndex (int) - first knot in the range to be set
        * endIndex   (int) - last knot in the range to be set
        """

    def tangent(self, *args: Any, **kwargs: Any) -> Any:
        """tangent(param, space=kObject) -> MVector

        Returns the normalized tangent vector at the given parameter value
        on the curve.

        * param (float) - parameter value at which to find the tangent
        * space   (int) - an MSpace constant giving the coordinate space in
                          which the tangent should be returned
        """

    def updateCurve(self, *args: Any, **kwargs: Any) -> Any:
        """updateCurve() -> self

        Tells the shape node which represents the curve in the scene, if
        any, that the curve has changed and needs to be redrawn.
        """


class MFnNurbsCurveData(MFnGeometryData):
    """MFnNurbsCurveData allows the creation and manipulation of Nurbs Curve
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnNurbsCurveData object

    __init__(MObject)
    Initializes a new MFnNurbsCurveData function set, attached
    to the specified object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new nurbs curve data object, attaches it to this function set
        and returns an MObject which references it.
        """


class MFnNurbsSurface(MFnDagNode):
    """NURBS (Non-Uniform Rational B-Spline) surface function set.

    The shape of a NURBS surface is defined by an array of CVs
    (control vertices), an array of knot values in the U direction
    and an array of knot values in the V direction, a degree in U
    and in V, and a form in U and in V.

    The U and V knot vectors for NURBS surfaces are of size
    (spansInU + 2*degreeInU -1) and (spansInV + 2*degreeInV -1).
    Note: spans = numCVs - degree.

    There are 3 possible forms for the surface in the U and V
    directions: open, closed and periodic. These forms are described
    below. Note that the descriptions below apply to both the U and
    V directions.

    The open and closed forms are quite similar, and in fact a
    closed surface will become an open surface if either the first
    or last CV is moved so that they are no longer coincident. To
    create an open or closed surface, of degree N, with M spans, you
    must provide M+N CVs. This implies that for a degree N surface,
    you must specify at least N+1 CVs to get a surface with a single
    span.

    The number of knots required for the surface is M + 2N - 1.  If
    you want the surface to start exactly at the first CV and end
    exactly at the last CV, then the knot vector must be structured
    to have degree N multiplicity at the beginning and end. This
    means that the first N knots must be identical, and the last N
    knots must be identical.

    A periodic surface is a special case of a closed surface.
    Instead of having just the first and last CVs coincident, the
    last N CVs in the surface, where N is equal to the degree,
    overlap the first N CVs. This results in a surface with no
    tangent break where the ends meet. The last N CVs in a periodic
    surface are permanently bound to the first N CVs, and Maya will
    not allow those last N CVs to be repositioned. If one or more
    of the first N CVs of the surface are repositioned, the
    overlapping CV's will remain bound, and will also be moved.

    In order to create a periodic surface, you must specify at least
    2N+1 CVs, so that that last N can overlap the first N and you
    still have 1 non-overlapping CV left.  The number of CVs
    required to create a periodic surface is still N+M (with a
    lower limit of 2N+1), but you must ensure that the positions
    of the last N CVs are identical to the positions of the
    first N.

    You still need M + 2N - 1 knots for a periodic surface, but
    the knot values required are more restrictive than for open
    or closed surfaces because of the overlap of the last N CVs.
    The first N knots should be specified at the beginning of
    the knot array as values { -(N-1), -(N-2), ... 0 } in order
    to implement the overlap.  Additionally there can be no knot
    multiplicity at the end of the surface, because that would
    compromise the tangent continuity property.

    Note that some third party applications use a different
    format for knots, where the number of knots required for a
    surface is M+2N+1 rather than M+2N-1 as used in Maya. Both
    knot representations are equivalent mathematically. To
    convert from one of these external representations into the
    Maya representation, simply omit the first and last knots
    from the external representation when creating the Maya
    representation. To convert from the Maya representation into
    the external representation, add two new knots at the
    beginning and end of the Maya knot sequence. The value of
    these new knots depends on the existing knot sequence. For a
    knot sequence with multiple end knots, simply duplicate the
    existing first and last knots once more, for example:

    Maya representation: {0,0,0,...,N,N,N}
    External representation: {0,0,0,0,...,N,N,N,N}

    For a knot sequence with uniform end knots, create the new
    knots offset at an interval equal to the existing first and
    last knot intervals, for example:

    Maya representation: {0,1,2,...,N,N+1,N+2}
    External representation: {-1,0,1,2,...,N,N+1,N+2,N+3}
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def area(self, *args: Any, **kwargs: Any) -> Any:
        """area(space=kObject, tolerance=kPointTolerance) -> float

        Returns the surface's area, or 0.0 if the area cannot be determined.
        """

    def assignUV(self, *args: Any, **kwargs: Any) -> Any:
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

    def assignUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def boundaryType(self, *args: Any, **kwargs: Any) -> Any:
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

    def clearUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def closestPoint(self, *args: Any, **kwargs: Any) -> Any:
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

    def copy(self, *args: Any, **kwargs: Any) -> Any:
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

    def create(self, *args: Any, **kwargs: Any) -> Any:
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

    def cv(self, *args: Any, **kwargs: Any) -> Any:
        """cv(uIndex, vIndex) -> MObject

        Returns a component for the specified control vertex.

        * uIndex (int) - U index of the CV.
        * vIndex (int) - V index of the CV.
        """

    def cvPosition(self, *args: Any, **kwargs: Any) -> Any:
        """cvPosition(uIndex, vIndex, space=kObject) -> MPoint

        Returns the position of the specified control vertex.

        * uIndex (int) - U index of the CV.
        * vIndex (int) - V index of the CV.
        * space  (int) - an MSpace constant giving the coordinate
                         space which the point should be returned.
        """

    def cvPositions(self, *args: Any, **kwargs: Any) -> Any:
        """cvPositions(space=kObject) -> MPointArray

        Returns the positions of all the surface's control vertices.

        * space  (int) - an MSpace constant giving the coordinate
                         space which the points should be returned.
        """

    def cvsInU(self, *args: Any, **kwargs: Any) -> Any:
        """cvsInU(startUIndex, endUIndex, vIndex) -> MObject

        Returns a component for a set of control vertices in the U direction.

        * startUIndex (int) - U index of the first CV to return.
        * endUIndex   (int) - U index of the last CV to return.
        * vIndex      (int) - V index for all of the returned CVs.
        """

    def cvsInV(self, *args: Any, **kwargs: Any) -> Any:
        """cvsInV(startVIndex, endVIndex, uIndex) -> MObject

        Returns a component for a set of control vertices in the V direction.

        * startVIndex (int) - V index of the first CV to return.
        * endVIndex   (int) - V index of the last CV to return.
        * uIndex      (int) - U index for all of the returned CVs.
        """

    dataObject: getset_descriptor = <attribute 'dataObject' of 'OpenMaya.MFnNurbsSurface' objects>
    degreeInU: getset_descriptor = <attribute 'degreeInU' of 'OpenMaya.MFnNurbsSurface' objects>
    degreeInV: getset_descriptor = <attribute 'degreeInV' of 'OpenMaya.MFnNurbsSurface' objects>
    def distanceToPoint(self, *args: Any, **kwargs: Any) -> Any:
        """distanceToPoint(point, space=kObject) -> float

        Returns the distance from the given point to the closest point on
        the surface.

        * point (MPoint) - Point to calculate distance to.
        * space  (int)   - An MSpace constant giving the coordinate space in
                           which the point has been specified.
        """

    def edge(self, *args: Any, **kwargs: Any) -> Any:
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

    formInU: getset_descriptor = <attribute 'formInU' of 'OpenMaya.MFnNurbsSurface' objects>
    formInV: getset_descriptor = <attribute 'formInV' of 'OpenMaya.MFnNurbsSurface' objects>
    def getAssignedUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getAssignedUVs() -> (MIntArray, MIntArray)

        Returns the indices of all UVs which have been mapped to the surface.
        The return value is a tuple with an array containing the number
        of UVs for each patch in the surface, and a second array containing
        the indices of the UVs mapped to each corner of those patches. This
        is the same format as the arrays taken by the assignUVs() method.
        """

    def getConnectedShaders(self, *args: Any, **kwargs: Any) -> Any:
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

    def getDerivativesAtParam(self, *args: Any, **kwargs: Any) -> Any:
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

    def getParamAtPoint(self, *args: Any, **kwargs: Any) -> Any:
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

    def getPatchUV(self, *args: Any, **kwargs: Any) -> Any:
        """getPatchUV(patchId, cornerIndex) -> (float, float)

        Returns a tuple containing the texture texture coordinate for a
        corner of a patch. Since texture coordinates (UVs) are stored
        per-patch per-corner you must specify both the patch and the corner
        that the u and v values are mapped to.
        * patchId (int)     - Patch of interest.
        * cornerIndex (int) - Corner of interest.
        """

    def getPatchUVid(self, *args: Any, **kwargs: Any) -> Any:
        """getPatchUVid(patchId, cornerIndex) -> int

        Returns the id of the texture coordinate for a single corner of a patch.

        * patchId (int)     - Patch of interest.
        * cornerIndex (int) - Corner of interest.
        """

    def getPatchUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getPatchUVs(patchId) -> (MFloatArray, MFloatArray)

        Returns a tuple containing the values of the texture coordinates on
        all corners of the specified patch. The tuple contains an array of U
        coordinates and an array of V coordinates, both the same length.

        * patchId (int)     - Patch of interest.
        """

    def getPointAtParam(self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtParam(uParam, vParam, space=kObject) -> MPoint"""

    def getUV(self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvId) -> (float, float)

        Returns a tuple containing the U and V values for the a texture coordinate

        * uvId (int) - Id of the texture coordinate of intest.
        """

    def getUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getUVs() -> (MFloatArray, MFloatArray)

        Returns all of the surface's texture coordinates as a tuple containing
        an array of U values and an array of V values.
        """

    hasHistoryOnCreate: getset_descriptor = <attribute 'hasHistoryOnCreate' of 'OpenMaya.MFnNurbsSurface' objects>
    def intersect(self, *args: Any, **kwargs: Any) -> Any:
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

    isBezier: getset_descriptor = <attribute 'isBezier' of 'OpenMaya.MFnNurbsSurface' objects>
    def isFlipNorm(self, *args: Any, **kwargs: Any) -> Any:
        """isFlipNorm(region) -> bool

        Checks whether the normal for the specified region is flipped
        This method is only valid for trimmed surfaces.

        region (int) - Region to check.
        """

    isFoldedOnBispan: getset_descriptor = <attribute 'isFoldedOnBispan' of 'OpenMaya.MFnNurbsSurface' objects>
    def isKnotU(self, *args: Any, **kwargs: Any) -> Any:
        """isKnotU(param) -> bool

        Checks if the specified parameter value is a knot value in the U
        direction.

        * param (float) - Parameter value to check.
        """

    def isKnotV(self, *args: Any, **kwargs: Any) -> Any:
        """isKnotV(param) -> bool

        Checks if the specified parameter value is a knot value in the V
        direction.

        * param (float) - Parameter value to check.
        """

    def isParamOnSurface(self, *args: Any, **kwargs: Any) -> Any:
        """isParamOnSurface(uParam, vParam) -> bool

        Checks if the specified parameter point is on this surface.

        * uParam (float) - U parameter value.
        * vParam (float) - V parameter value.
        """

    def isPointInTrimmedRegion(self, *args: Any, **kwargs: Any) -> Any:
        """isPointInTrimmedRegion(uParam, vParam) -> bool

        Checks if the given point is in a trimmed away region of a trimmed
        surface. A trimmed away region is the part of the surface that is
        cut away as a result of a trim operation.

        * uParam (float) - U parameter of the point to check.
        * vParam (float) - V parameter of the point to check.
        """

    def isPointOnSurface(self, *args: Any, **kwargs: Any) -> Any:
        """isPointOnSurface(point, tolerance=kPointTolerance, space=kObject) -> bool

        Checks if the given point is on this surface.

        * point    (MPoint) - Point to check.
        * tolerance (float) - Accuracy to be used in the operation.
        * space       (int) - An MSpace constant giving the coordinate space
                              in which to perform the operation
        """

    isTrimmedSurface: getset_descriptor = <attribute 'isTrimmedSurface' of 'OpenMaya.MFnNurbsSurface' objects>
    isUniform: getset_descriptor = <attribute 'isUniform' of 'OpenMaya.MFnNurbsSurface' objects>
    kPointTolerance: float = 0.001
    knotDomainInU: getset_descriptor = <attribute 'knotDomainInU' of 'OpenMaya.MFnNurbsSurface' objects>
    knotDomainInV: getset_descriptor = <attribute 'knotDomainInV' of 'OpenMaya.MFnNurbsSurface' objects>
    def knotInU(self, *args: Any, **kwargs: Any) -> Any:
        """knotInU(index) -> float

        Returns the knot value at the specified U index. U knots are indexed
        from 0 to numKnotsInU-1.
        * index (int) - Index of the U knot to return.
        """

    def knotInV(self, *args: Any, **kwargs: Any) -> Any:
        """knotInV(index) -> float

        Returns the knot value at the specified V index. V knots are indexed
        from 0 to numKnotsInV-1.
        * index (int) - Index of the V knot to return.
        """

    def knotsInU(self, *args: Any, **kwargs: Any) -> Any:
        """knotsInU() -> MDoubleArray

        Returns all of the surface's knots in the U direction.
        """

    def knotsInV(self, *args: Any, **kwargs: Any) -> Any:
        """knotsInV() -> MDoubleArray

        Returns all of the surface's knots in the V direction.
        """

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """normal(uParam, vParam, space=kObject) -> MVector

        Returns the normal at the given parameter value on the surface.

        * uParam (float) - U parameter at which to obtain normal.
        * vParam (float) - V parameter at which to obtain normal.
        * space    (int) - An MSpace constant giving the coordinate space
                           in which to perform the operation
        """

    def numBoundaries(self, *args: Any, **kwargs: Any) -> Any:
        """numBoundaries(region) -> unsigned int

        Returns the number of boundaries for the specified region. The
        surface must be a trimmed surface.

        For each region there may be several boundary curves, an outer curve
        and possibly several inner boundary curves which define holes. These
        boundary curves are made up of one or more curves called edges.

        * region (int) - Region of interest.
        """

    numCVsInU: getset_descriptor = <attribute 'numCVsInU' of 'OpenMaya.MFnNurbsSurface' objects>
    numCVsInV: getset_descriptor = <attribute 'numCVsInV' of 'OpenMaya.MFnNurbsSurface' objects>
    def numEdges(self, *args: Any, **kwargs: Any) -> Any:
        """numEdges(region, boundary) -> unsigned int

        Returns the number of edges for the specified trim boundary.
        For each region there may be several boundary curves, an outer curve
        and possibly several inner boundary curves which define holes. These
        boundary curves are made up of one or more curves called edges.

        * region   (int) - Region of interest.
        * boundary (int) - Boundary of interest
        """

    numKnotsInU: getset_descriptor = <attribute 'numKnotsInU' of 'OpenMaya.MFnNurbsSurface' objects>
    numKnotsInV: getset_descriptor = <attribute 'numKnotsInV' of 'OpenMaya.MFnNurbsSurface' objects>
    numNonZeroSpansInU: getset_descriptor = <attribute 'numNonZeroSpansInU' of 'OpenMaya.MFnNurbsSurface' objects>
    numNonZeroSpansInV: getset_descriptor = <attribute 'numNonZeroSpansInV' of 'OpenMaya.MFnNurbsSurface' objects>
    numPatches: getset_descriptor = <attribute 'numPatches' of 'OpenMaya.MFnNurbsSurface' objects>
    numPatchesInU: getset_descriptor = <attribute 'numPatchesInU' of 'OpenMaya.MFnNurbsSurface' objects>
    numPatchesInV: getset_descriptor = <attribute 'numPatchesInV' of 'OpenMaya.MFnNurbsSurface' objects>
    numRegions: getset_descriptor = <attribute 'numRegions' of 'OpenMaya.MFnNurbsSurface' objects>
    numSpansInU: getset_descriptor = <attribute 'numSpansInU' of 'OpenMaya.MFnNurbsSurface' objects>
    numSpansInV: getset_descriptor = <attribute 'numSpansInV' of 'OpenMaya.MFnNurbsSurface' objects>
    numUVs: getset_descriptor = <attribute 'numUVs' of 'OpenMaya.MFnNurbsSurface' objects>
    def projectCurve(self, *args: Any, **kwargs: Any) -> Any:
        """projectCurve(curve[, direction], keepHistory=False) -> self

        Projects the given curve onto the surface, creating a curve on surface.

        * direction (MVector) - Direction of projection. If not supplied
                                then surface normals will be used.
        * keepHistory  (bool) - Determines whether the construction history
                                of the projection should be retained.
        """

    def removeKnotInU(self, *args: Any, **kwargs: Any) -> Any:
        """removeKnotInU(param, removeAll=False) -> self

        Removes one or more U knots at the specified parameter value from
        from the surface.

        * param    (float) - U parameter value of the knot to remove.
        * removeAll (bool) - If True and there are multiple knots at the
                             parameter value then they will all be removed.
                             Otherwise, all but one will be removed.
        """

    def removeKnotInV(self, *args: Any, **kwargs: Any) -> Any:
        """removeKnotInV(param, removeAll=False) -> self

        Removes one or more V knots at the specified parameter value from
        from the surface.

        * param    (float) - V parameter value of the knot to remove.
        * removeAll (bool) - If True and there are multiple knots at the
                             parameter value then they will all be removed.
                             Otherwise, all but one will be removed.
        """

    def removeOneKnotInU(self, *args: Any, **kwargs: Any) -> Any:
        """removeOneKnotInU(param) -> self

        Removes one U knot at the specified parameter value. If there are
        multiple knots at that the value the others are retained.

        * param (float) - U parameter value of the knot to remove.
        """

    def removeOneKnotInV(self, *args: Any, **kwargs: Any) -> Any:
        """removeOneKnotInV(param) -> self

        Removes one V knot at the specified parameter value. If there are
        multiple knots at that the value the others are retained.

        * param (float) - V parameter value of the knot to remove.
        """

    def setCVPosition(self, *args: Any, **kwargs: Any) -> Any:
        """setCVPosition(uIndex, vIndex, point, space=kObject) -> self"""

    def setCVPositions(self, *args: Any, **kwargs: Any) -> Any:
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

    def setKnotInU(self, *args: Any, **kwargs: Any) -> Any:
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

    def setKnotInV(self, *args: Any, **kwargs: Any) -> Any:
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

    def setKnotsInU(self, *args: Any, **kwargs: Any) -> Any:
        """setKnotsInU(params, startIndex, endIndex) -> self

        Sets the values of a range of U knots.

        * params     (MDoubleArray or seq of float)
                           - Parameter values to set at the knots. One value
                             per knot in the range.
        * startIndex (int) - Index of the first U knot to set.
        * endIndex   (int) - Index of the last U knot to set.
        """

    def setKnotsInV(self, *args: Any, **kwargs: Any) -> Any:
        """setKnotsInV(params, startIndex, endIndex) -> self

        Sets the values of a range of V knots.

        * params     (MDoubleArray or seq of float)
                           - Parameter values to set at the knots. One value
                             per knot in the range.
        * startIndex (int) - Index of the first V knot to set.
        * endIndex   (int) - Index of the last V knot to set.
        """

    def setUV(self, *args: Any, **kwargs: Any) -> Any:
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

    def setUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def tangents(self, *args: Any, **kwargs: Any) -> Any:
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

    def trim(self, *args: Any, **kwargs: Any) -> Any:
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

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signals that this surface has changed and needs to be recalculated.

        This method is useful when a large number of CVs for the surface are
        being modified. Instead of updating the surface every time a CV is
        changed it is more efficient to call this method once after all the
        updates are complete.
        """


class MFnNurbsSurfaceData(MFnGeometryData):
    """MFnNurbsSurfaceData allows the creation and manipulation of Nurbs Surface
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnNurbsSurfaceData object

    __init__(MObject)
    Initializes a new MFnNurbsSurfaceData function set, attached
    to the specified object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create() -> MObject

        Creates a new nurbs surface data object, attaches it to this function set
        and returns an MObject which references it.
        """


class MFnPlugin(MFnBase):
    """Register and deregister plug-in services with Maya."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def apiVersion(self, *args: Any, **kwargs: Any) -> Any:
        """Return the API version required by the plug-in."""

    def deregisterAttributePatternFactory(self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined attribute pattern factory type from Maya."""

    def deregisterCommand(self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined command from Maya."""

    def deregisterContextCommand(self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined context command from Maya."""

    def deregisterData(self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined data type from Maya."""

    def deregisterDragAndDropBehavior(self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined drag and drop behavior from Maya."""

    def deregisterNode(self, *args: Any, **kwargs: Any) -> Any:
        """Deregister a user defined dependency node from Maya."""

    def findPlugin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an MObject corresponding to the named plugin."""

    def loadPath(self, *args: Any, **kwargs: Any) -> Any:
        """Return the full path name of the file from which the plug-in was loaded."""

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Return the plug-in's name."""

    def registerAttributePatternFactory(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new attribute pattern factory type with Maya."""

    def registerCommand(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new command with Maya."""

    def registerContextCommand(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new context command with Maya.  Once registered, the context
        can be used to create a new tool that can be used in a manner
        identical to built-in Maya tools.
        """

    def registerData(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new data type with Maya."""

    def registerDragAndDropBehavior(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new drag and drop behavior with Maya.
        Once registered, the new behavior can be used to finish connections between node drag and drops from the hyperGraph/hyperShade to other nodes or Maya UI.
        """

    def registerNode(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new dependency node with Maya."""

    def registerShape(self, *args: Any, **kwargs: Any) -> Any:
        """Register a new user defined shape node with Maya.
        To deregister the shape node use the MFnPlugin.deregisterNode().
        """

    def setName(self, *args: Any, **kwargs: Any) -> Any:
        """Set the plug-in's name."""

    def vendor(self, *args: Any, **kwargs: Any) -> Any:
        """Return the plug-in's vendor string."""

    version: getset_descriptor = <attribute 'version' of 'OpenMaya.MFnPlugin' objects>

class MFnPluginData(MFnData):
    """MFnPluginData allows the creation and manipulation of plugin
    data objects for use in the dependency graph.

    __init__()
    Initializes a new, empty MFnPluginData object

    __init__(MObject)
    Initializes a new MFnPluginData function set, attached
    to the specified object.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(id) -> MObject

        Create an instance of the specified user defined data type and attach it to this functionset.

        * id (MTypeId) - the unique MTypeId of the user defined data class derived from MPxData.
        """

    def data(self, *args: Any, **kwargs: Any) -> Any:
        """data() -> MPxData

        Return the user defined data held in this instance
        """

    def typeId(self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Return the unique MTypeId of the user defined data that is held by this instance
        """


class MFnPointArrayData(MFnData):
    """Function set for node data consisting of an array of MPoints."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MPointArray."""

    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MPoint array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MFnReference(MFnDependencyNode):
    """Function set for reference nodes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def associatedNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """associatedNamespace(bool shortName) -> MString

        Returns the namespace associated with this reference.
        """

    def containsNode(self, *args: Any, **kwargs: Any) -> Any:
        """containsNode(MObject) -> bool

        Returns true if the specified node is from this reference or one of its child references. The containsNodeExactly method can be used to test membership without including the child references.
        """

    def containsNodeExactly(self, *args: Any, **kwargs: Any) -> Any:
        """containsNodeExactly(MObject) -> bool

        Returns true if the specified node is from this reference. Membership in child references is not checked. The containsNode method may be used to test membership in a reference and its child references.
        """

    def fileName(self, *args: Any, **kwargs: Any) -> Any:
        """fileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

        Returns the name of file associated with this reference.
        """

    def ignoreReferenceEdits(self, *args: Any, **kwargs: Any) -> Any:
        """ignoreReferenceEdits() -> bool

        Indicates whether reference edits will be tracked and logged or not.
        """

    def isExportEditsFile(self, *args: Any, **kwargs: Any) -> Any:
        """isExportEditsFile() -> bool

        Returns true if the reference is an export edits file. An export edits file is a file of type '.editMA' or '.editMB' which was created using Maya's offline file functionality.
        """

    def isLoaded(self, *args: Any, **kwargs: Any) -> Any:
        """isLoaded() -> bool

        Returns true if the reference is loaded.
        """

    def isLocked(self, *args: Any, **kwargs: Any) -> Any:
        """isLocked() -> bool

        Returns true if the reference is locked or if the referenced file was saved as locked.
        """

    def isValidReference(self, *args: Any, **kwargs: Any) -> Any:
        """isValidReference() -> bool

        Returns true if the reference is an valid file reference.
        """

    def nodes(self, *args: Any, **kwargs: Any) -> Any:
        """nodes() -> MObjectArray

        Returns an array of the nodes associated with this reference.
        """

    def parentAssembly(self, *args: Any, **kwargs: Any) -> Any:
        """parentAssembly() -> MObject

        Returns the parent assembly node that contains this reference. See MFnAssembly documentation for more details.
        """

    def parentFileName(self, *args: Any, **kwargs: Any) -> Any:
        """parentFileName(bool resolvedName, bool includePath, bool includeCopyNumber) -> MString

        Returns the name of parent file associated with this reference.
        """

    def parentReference(self, *args: Any, **kwargs: Any) -> Any:
        """parentReference() -> MObject

        Returns the reference node associated with the parent reference.
        """

    def setIgnoreReferenceEdits(self, *args: Any, **kwargs: Any) -> Any:
        """setIgnoreReferenceEdits(bool) -> None

        Specify whether reference edits should be tracked and logged or not.
        This should be treated as a temporary state and should be enabled 
        around a batch of operations where reference edits should be ignored.
        Restore the previous value when the batch of operations is complete.
        """


class MFnSet(MFnDependencyNode):
    """Function set for sets."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addMember(self, *args: Any, **kwargs: Any) -> Any:
        """addMember( object ) -> self

        Add a new object to the set.

        The added object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """

    def addMembers(self, *args: Any, **kwargs: Any) -> Any:
        """addMembers( MSelectionList ) -> self

        Add a list of new objects to the set.
        """

    def annotation(self, *args: Any, **kwargs: Any) -> Any:
        """annotation() -> string

        Returns the annotation string for this set.  This allows a description of the set to be stored with it.
        """

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Removes all elements from this set.
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(members, restriction=kNone) -> MObject

        Creates a new set dependency node and puts it in the dependency graph.

        * members (MSelectionList) - list of members for new set
        * restriction (MFnSet.Restriction) - restriction applied to members
        """

    def getIntersection(self, *args: Any, **kwargs: Any) -> Any:
        """getIntersection( otherSet ) -> MSelectionList

        This method calculates the intersection of two sets.  The result will be the intersection of this set and the set passed into the method.

        * otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set
        """

    def getMemberPaths(self, *args: Any, **kwargs: Any) -> Any:
        """getMemberPaths( shading ) -> MDagPathArray

        Get the members of this set as an array of dagPaths.

        This will usually return the same dagPaths as will be contained in the getMembersmethod. If the shading flag is set to true, the list will consist only of dagPathsthat are affected by this set for the purposes of material assignments.

        * shading (bool) -  whether the list should only contain members of this set used for shading purposes.
        """

    def getMembers(self, *args: Any, **kwargs: Any) -> Any:
        """getMembers( flatten ) -> MSelectionList

        Get the members of this set as a selection list.  This information is providedas a selection list so that all of the path information is retained forDAG nodes.

        It is possible to ask for the returned list to be flattened.  This means thatall sets that exist inside this set will be expanded into a list of theircontents.

        * flatten (bool) - whether to flatten the returned list
        """

    def getUnion(self, *args: Any, **kwargs: Any) -> Any:
        """getUnion( otherSet ) -> MSelectionList

        This method calculates the union of two sets.  The result will be the union of this set and the set passed into the method.

        * otherSet (MObject or MObjectArray or list of sets) - set(s) to find union of with this set
        """

    def hasRestrictions(self, *args: Any, **kwargs: Any) -> Any:
        """hasRestrictions() -> bool

        Returns true if this function set has restrictions on the type of objects that it may contain.
        """

    def intersectsWith(self, *args: Any, **kwargs: Any) -> Any:
        """intersectsWith( otherSet ) -> self

        Returns true if this set intersects with the given set.  An intersection occurs if there are any common members between the two sets.
        """

    def isMember(self, *args: Any, **kwargs: Any) -> Any:
        """isMember( object ) -> bool

        Returns true if the given object is a member of this set.

        The object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """

    def removeMember(self, *args: Any, **kwargs: Any) -> Any:
        """removeMember( object ) -> self

        Remove an object from the set.

        The removed object may be an MObject, an (MDagPath, MObject) tuple, or an MPlug.
        """

    def removeMembers(self, *args: Any, **kwargs: Any) -> Any:
        """removeMembers( MSelectionList ) -> self

        Remove items of the selection list from the set.
        """

    def restriction(self, *args: Any, **kwargs: Any) -> Any:
        """restriction() -> MFnSet.Restriction

        Returns the type of membership restriction that this set has.
        """

    def setAnnotation(self, *args: Any, **kwargs: Any) -> Any:
        """setAnnotation( annotation ) -> self

        Sets the annotation string for this set.  This allows a description of the set to be stored with it.
        """


class MFnSingleIndexedComponent(MFnComponent):
    """This function set allows you to create, edit, and query single indexed components.
    Single indexed components store 1 dimensional index values.

    __init__()
    Initializes a new, empty MFnSingleIndexedComponent object

    __init__(MObject component)
    Initializes a new MFnSingleIndexedComponent function set, attached to the specified component.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addElement(self, *args: Any, **kwargs: Any) -> Any:
        """addElement(int element) -> self

        Adds the specified element to the component.
        """

    def addElements(self, *args: Any, **kwargs: Any) -> Any:
        """addElements([int]) -> self
        addElements(MIntArray) -> self

        Adds the specified elements to the component.
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """

    def element(self, *args: Any, **kwargs: Any) -> Any:
        """element(index) -> int

        Returns the index'th element of the component.
        """

    elementMax: getset_descriptor = <attribute 'elementMax' of 'OpenMaya.MFnSingleIndexedComponent' objects>
    def getCompleteData(self, *args: Any, **kwargs: Any) -> Any:
        """getCompleteData() -> int

        Returns the number of elements in the complete component, or 0 if the component is not complete.
        """

    def getElements(self, *args: Any, **kwargs: Any) -> Any:
        """getElements() -> MIntArray

        Returns all of the component's elements.
        """

    def setCompleteData(self, *args: Any, **kwargs: Any) -> Any:
        """setCompleteData(numElements) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numElements indicates the number of elements in the complete component.
        """


class MFnStringArrayData(MFnData):
    """Function set for node data consisting of an array of string."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as a list of unicode objects."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new string array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MFnStringData(MFnData):
    """Function set for string node data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new string data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the encapsulated string."""

    def string(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated string as a unicode object."""


class MFnTransform(MFnDagNode):
    """Function set for operating on transform nodes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def clearRestPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Clears the transform's rest position matrix."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new transform node and attaches it to the function set."""

    def enableLimit(self, *args: Any, **kwargs: Any) -> Any:
        """Enables or disables a specified limit type."""

    def isLimited(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the specified limit type is enabled."""

    kRotateMaxX: int = 13
    kRotateMaxY: int = 15
    kRotateMaxZ: int = 17
    kRotateMinX: int = 12
    kRotateMinY: int = 14
    kRotateMinZ: int = 16
    kShearMaxYZ: int = 11
    kShearMinYZ: int = 10
    kTranslateMaxX: int = 19
    kTranslateMaxY: int = 21
    kTranslateMaxZ: int = 23
    kTranslateMinX: int = 18
    kTranslateMinY: int = 20
    kTranslateMinZ: int = 22
    def limitValue(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the specified limit."""

    def resetFromRestPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Resets the transform from its rest position matrix."""

    def restPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rest position matrix."""

    def rotateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds an MEulerRotation or MQuaternion to the transform's rotation."""

    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""

    def rotateOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the MQuaternion which orients the local rotation space."""

    def rotatePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotate pivot."""

    def rotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotate pivot translation."""

    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""

    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's rotation as the individual components of an MEulerRotation or MQuaternion."""

    def rotationOrder(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the order of rotations when the transform's rotation is expressed as an MEulerRotation."""

    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's XYZ scale components."""

    def scaleBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transform's XYZ scale components by a sequence of three floats."""

    def scalePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's scale pivot."""

    def scalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's scale pivot translation."""

    def setLimit(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the specified limit."""

    def setRestPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rest position matrix."""

    def setRotateOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the MQuaternion which orients the local rotation space."""

    def setRotatePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotate pivot."""

    def setRotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotate pivot translation."""

    def setRotation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using an MEulerRotation or MQuaternion."""

    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation using the individual components of an MEulerRotation or MQuaternion."""

    def setRotationOrder(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's rotation order."""

    def setScale(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale components."""

    def setScalePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale pivot."""

    def setScalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's scale pivot translation."""

    def setShear(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's shear."""

    def setTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's attribute values to represent the given transformation matrix."""

    def setTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transform's translation."""

    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transform's shear components."""

    def shearBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transform's shear components by a sequence of three floats."""

    def transformation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation matrix represented by this transform."""

    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds an MVector to the transform's translation."""

    def translation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transform's translation as an MVector."""


class MFnTripleIndexedComponent(MFnComponent):
    """This function set allows you to create, edit, and query triple indexed
    components. Triple indexed components store 3 dimensional index values.

    __init__()
    Initializes a new, empty MFnTripleIndexedComponent object

    __init__(MObject component)
    Initializes a new MFnTripleIndexedComponent function set, attached
    to the specified component.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addElement(self, *args: Any, **kwargs: Any) -> Any:
        """addElement(sIndex, tIndex, uIndex) -> self
        addElement([sIndex, tIndex, uIndex]) -> self

        Adds the element identified by (sIndex, tIndex, uIndex) to the component.
        """

    def addElements(self, *args: Any, **kwargs: Any) -> Any:
        """addElements(sequence of [sIndex, tIndex, uIndex]) -> self

        Adds the specified elements to the component. Each item in the
        elements sequence is itself a sequence of three ints which are the
        S, T and U indices of an element to be added.
        """

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(MFn Type constant) -> MObject

        Creates a new, empty component, attaches it to the function set and
        returns an MObject which references it.
        """

    def getCompleteData(self, *args: Any, **kwargs: Any) -> Any:
        """getCompleteData() -> (numS, numT, numU)

        Returns a tuple containing the number of S, T and U indices in
        the complete component, or (0,0,0) if the component is not complete.
        """

    def getElement(self, *args: Any, **kwargs: Any) -> Any:
        """getElement(index) -> (sIndex, tIndex, uIndex)

        Returns the index'th element of the component as a tuple containing the
        element's S, T and U indices.
        """

    def getElements(self, *args: Any, **kwargs: Any) -> Any:
        """getElements() -> list of (sIndex, tIndex, uIndex)

        Returns all of the component's elements as a list of tuples with each
        tuple containing the S, T and U indices of a single element.
        """

    def setCompleteData(self, *args: Any, **kwargs: Any) -> Any:
        """setCompleteData(numS, numT, numU) -> self

        Marks the component as complete (i.e. contains all possible elements).
        numS, numT and numU indicate the number of S, T and U indices
        in the complete component (i.e. the max S index is numS-1, the max T
        index is numT-1 and the max U index is numU-1).
        """


class MFnTypedAttribute(MFnAttribute):
    """Functionset for creating and working typed attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def attrType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of data handled by the attribute."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new type attribute, attaches it to the function set and returns it as an MObject."""

    default: getset_descriptor = <attribute 'default' of 'OpenMaya.MFnTypedAttribute' objects>

class MFnUInt64ArrayData(MFnData):
    """Function set for node data consisting of an array of MUint64."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MUint64Array."""

    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MUint64 array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MFnUnitAttribute(MFnAttribute):
    """Functionset for creating and working with angle, distance and time attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new unit attribute, attaches it to the function set and returns it as an MObject."""

    default: getset_descriptor = <attribute 'default' of 'OpenMaya.MFnUnitAttribute' objects>
    def getMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""

    def getMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's hard minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""

    def getSoftMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft maximum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""

    def getSoftMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute's soft minimum value. Returned MAngle and MDistance are always in radians and centimeters, respectively"""

    def hasMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a hard maximum value."""

    def hasMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a hard minimum value."""

    def hasSoftMax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a soft maximum value."""

    def hasSoftMin(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the attribute has a soft minimum value."""

    kLast: int = 4
    kTime: int = 3
    def setMax(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard maximum value."""

    def setMin(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's hard minimum value."""

    def setSoftMax(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft maximum value."""

    def setSoftMin(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the attribute's soft minimum value."""

    def unitType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of data handled by the attribute."""


class MFnVectorArrayData(MFnData):
    """Function set for node data consisting of an array of MVectors."""
    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the encapsulated array as an MVectorArray."""

    def copyTo(self, *args: Any, **kwargs: Any) -> Any:
        """Replaces the elements of an array with those in the encapsulated array."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Creates a new MVector array data object."""

    def set(self, *args: Any, **kwargs: Any) -> Any:
        """Sets values in the encapsulated array."""


class MGlobal(object):
    """Static class providing common API global functions."""
    def addToModel(self, *args: Any, **kwargs: Any) -> Any:
        """addToModel(MObject, MObject) -> None

        This method is used to add new dag objects to the model.  If no parent node
        is specified, then the node is added under the world.  When a node is
        added under the world, then a transform node is automatically created as
        a parent.  This assumes that the node being added is not already a
        transform node.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter will be returned.
        """

    def addToModelAt(self, *args: Any, **kwargs: Any) -> Any:
        """addToModelAt(MObject, MVector, double[3], double[3], rotateOrder=MTransformationMatrix.kXYZ) -> None

        Adds the specified dag object to the DAG and transform the object
        by the specified arguments.
        This method is only valid for dag nodes. If the specified
        object is not of type MFn::kDagNode then MS::kInvalidParameter
        will be returned.
        """

    def animSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """animSelectionMask() -> MSelectionMask

        Returns the animation selection mask.
        """

    def apiVersion(self, *args: Any, **kwargs: Any) -> Any:
        """apiVersion() -> int

        Returns a number describing the version of the Maya API at runtime.
        """

    def className(self, *args: Any, **kwargs: Any) -> Any:
        """className() -> string

        Returns the name of this class.
        """

    def clearSelectionList(self, *args: Any, **kwargs: Any) -> Any:
        """clearSelectionList() -> None

        Removes all items from the active selection list.
        """

    def closeErrorLog(self, *args: Any, **kwargs: Any) -> Any:
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

    def componentSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """componentSelectionMask() -> MSelectionMask

        Returns the component selection mask.
        """

    def currentToolContext(self, *args: Any, **kwargs: Any) -> Any:
        """currentToolContext() -> MObject

        Returns the current tool context as an MObject.
        """

    def defaultErrorLogPathName(self, *args: Any, **kwargs: Any) -> Any:
        """defaultErrorLogPathName() -> string

        Determines the default path name of the error log file.
        Returns an empty string on failure.
        """

    def deleteNode(self, *args: Any, **kwargs: Any) -> Any:
        """deleteNode(MObject) -> None

        Delete the given dag node or dependency graph node.
        """

    def disableStow(self, *args: Any, **kwargs: Any) -> Any:
        """disableStow() -> bool

        This method is used to query if the disabling of Stowing (hiding) 
        and Unstowing (showing) windows is active.
        """

    def displayError(self, *args: Any, **kwargs: Any) -> Any:
        """displayError(msg) -> None

        Display an error in the script editor.
        """

    def displayInfo(self, *args: Any, **kwargs: Any) -> Any:
        """displayInfo(msg) -> None

        Display an informational message in the script editor.
        """

    def displayWarning(self, *args: Any, **kwargs: Any) -> Any:
        """displayWarning(msg) -> None

        Display a warning in the script editor.
        """

    def doErrorLogEntry(self, *args: Any, **kwargs: Any) -> Any:
        """doErrorLogEntry(string) -> bool

        Logs an entry in the currently open log file.  It is not necessary for error
        logging to be enabled, but a log file must be open.
        A newline is appended to each log entry.
        """

    def errorLogPathName(self, *args: Any, **kwargs: Any) -> Any:
        """errorLogPathName() -> string

        Determines the path name of the current error log file.
        Returns the null stringon failure.
        """

    def errorLoggingIsOn(self, *args: Any, **kwargs: Any) -> Any:
        """errorLoggingIsOn() -> bool

        This method determines whether or not API errors are being logged.
        """

    def executeCommandOnIdle(self, *args: Any, **kwargs: Any) -> Any:
        """executeCommandOnIdle(string, bool displayEnabled=False) -> None

        Sets a MEL command to execute on the next idle event. Since the command
        will likely not be executed until some time after control is returned to
        caller, there is no access to the command results.

        This method is thread safe and can be called from a thread other than
        Maya's main thread. However, that thread must still be part of the Maya
        process. Calling this method from a completely separate process will
        not work and may lead to unpredictable behaviour.
        """

    def executeCommandStringResult(self, *args: Any, **kwargs: Any) -> Any:
        """executeCommandStringResult(string, bool displayEnabled=False, bool undoEnabled=False) -> string or [string, string, ...]

        Executes a MEL command that returns a string or an array of strings 
        result from the command engine depending on the number of return values.
        Optionally allows display of the command in the Command Window to be 
        enabled or disabled.  Defaults to disabled.  Optionally allows undo 
        for the command to be enabled or disabled.  Defaults to disabled.

        Note: This is not thread safe; you may use executeCommandOnIdle instead
        """

    def getAbsolutePathToResources(self, *args: Any, **kwargs: Any) -> Any:
        """getAbsolutePathToResources() -> string

        Return the absolute path of Maya's "Resources" fold on the system,
        including the "Resources" folder itself.
        """

    def getActiveSelectionList(self, *args: Any, **kwargs: Any) -> Any:
        """getActiveSelectionList(orderedSelectionIfAvailable=False) -> MSelectionList

        Return an MSelectionList containing the nodes, components and
        plugs currently selected in Maya. If orderedSelectionIfAvailable
        is True, and tracking is enabled, will return the selected items
        in the order that they were selected.
        """

    def getAssociatedSets(self, *args: Any, **kwargs: Any) -> Any:
        """getAssociatedSets(MSelectionList) -> list

        This utility method finds all the sets that the items in
        the given selection list are members of.
        """

    def getFunctionSetList(self, *args: Any, **kwargs: Any) -> Any:
        """getFunctionSetList(MObject) -> (string, string, ...)

        Returns a tuple of strings that represent the type of each function
        set that will accept this object.
        """

    def getHiliteList(self, *args: Any, **kwargs: Any) -> Any:
        """getHiliteList() -> MSelectionList

        Returns a copy of the hilite list.  The hilite list contains all DAG objects
        that are hilited for component selection mode.  (e.g. when the user right clicks
        over a Mesh object and chooses the "vertex" option the Mesh line drawing changes
        color and the mesh is added to the hiliteList.)
        """

    def getLiveList(self, *args: Any, **kwargs: Any) -> Any:
        """getLiveList() -> MSelectionList

        Returns a copy of the live list. When a user performs a
        "Modify->Make Live" in the user interface the currently selected
        objects are added to the live list.
        """

    def getPreselectionHiliteList(self, *args: Any, **kwargs: Any) -> Any:
        """getPreselectionHiliteList() -> MSelectionList

        Gets the objects for which Maya is displaying a preselection
        highlight in the viewports.
        """

    def getRichSelection(self, *args: Any, **kwargs: Any) -> Any:
        """getRichSelection(defaultToActiveSelection=True) -> MRichSelection

        Returns the current rich selection (usually the active selection with
        any soft selection and symmetry applied). If no rich selection exists
        and 'defaultToActiveSelection' is True, the current active selection
        will be returned instead.
        """

    def getSelectionListByName(self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionListByName(name) -> MSelectionList

        Returns an MSelectionList with all of the objects that match the
        specified name. The name may use the same type of regular expressions
        as can be used in MEL commands. For example, the pattern 'pCube*' will
        match all occurrences of objects whose names begin with 'pCube'.
        """

    def initOptionVar(self, *args: Any, **kwargs: Any) -> Any:
        """initOptionVar(string name, int, string category) -> bool
        initOptionVar(string name, double, string category) -> bool
        initOptionVar(string name, string, string category) -> bool


        This method is used to initialize an option variable value of int, bool, string type.
        This method will create the option var if it doesn't exist and set the default value
        and category.
        """

    def isRedoing(self, *args: Any, **kwargs: Any) -> Any:
        """isRedoing() -> bool

        true if Maya is currently in the middle of a redo.
        """

    def isSelected(self, *args: Any, **kwargs: Any) -> Any:
        """isSelected(MObject) -> bool

        Determines whether the given object is on the active selection list.
        """

    def isUndoing(self, *args: Any, **kwargs: Any) -> Any:
        """isUndoing() -> bool

        true if Maya is currently in the middle of an undo.
        """

    def isYAxisUp(self, *args: Any, **kwargs: Any) -> Any:
        """isYAxisUp() -> bool

        This method returns true if, currently, the Y-axis is UP.
        """

    def isZAxisUp(self, *args: Any, **kwargs: Any) -> Any:
        """isZAxisUp() -> bool

        This method returns true if, currently, the Z-axis is UP.
        """

    kAddToHeadOfList: int = 4
    kAddToList: int = 2
    kBaseUIMode: int = 3
    kBatch: int = 1
    kInteractive: int = 0
    kLibraryApp: int = 2
    kRemoveFromList: int = 3
    kReplaceList: int = 0
    kSelectComponentMode: int = 1
    kSelectLeafMode: int = 3
    kSelectObjectMode: int = 0
    kSelectRootMode: int = 2
    kSelectTemplateMode: int = 4
    kSurfaceSelectMethod: int = 0
    kWireframeSelectMethod: int = 1
    kXORWithList: int = 1
    def mayaFeatureSet(self, *args: Any, **kwargs: Any) -> Any:
        """mayaFeatureSet() -> int

        Returns an enumerated type specifying if Maya API has unlimited set of features.
          kComplete  Running Maya version with all features available.
          kRestricted  Running Maya version with some features limited in availability.
        """

    def mayaName(self, *args: Any, **kwargs: Any) -> Any:
        """mayaName() -> string

        Returns a string containing name of running application.
        """

    def mayaState(self, *args: Any, **kwargs: Any) -> Any:
        """mayaState() -> int

        Returns an enumerated type specifying the way in which Maya was invoked.
          kInteractive  Running with a UI
          kBatch  Running without a UI
          kLibraryApp  Running as a standalone (MLibrary) application.
          kBaseUIMode  Running with UI enabled but Maya's std UI scripts not run.
        """

    def mayaVersion(self, *args: Any, **kwargs: Any) -> Any:
        """mayaVersion() -> string

        Returns a string describing this version of Maya.
        """

    def miscSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """miscSelectionMask() -> MSelectionMask

        Returns the miscellaneous selection mask.
        """

    def objectSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """objectSelectionMask() -> MSelectionMask

        Returns the object selection mask.
        """

    def optionVarDoubleValue(self, *args: Any, **kwargs: Any) -> Any:
        """optionVarDoubleValue(string) -> double

        This method is used to get the option variable value of type double
        """

    def optionVarExists(self, *args: Any, **kwargs: Any) -> Any:
        """optionVarExists(string) -> bool

        This method is used to check if the option variable exists
        """

    def optionVarIntValue(self, *args: Any, **kwargs: Any) -> Any:
        """optionVarIntValue(string) -> int

        This method is used to get the option variable value of int type
        """

    def optionVarStringValue(self, *args: Any, **kwargs: Any) -> Any:
        """optionVarStringValue(string) -> MString

        This method is used to get the option variable value of type string
        """

    def removeFromModel(self, *args: Any, **kwargs: Any) -> Any:
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

    def removeOptionVar(self, *args: Any, **kwargs: Any) -> Any:
        """removeOptionVar(string) -> None

        This method is used to remove the option variable
        """

    def resetToDefaultErrorLogPathName(self, *args: Any, **kwargs: Any) -> Any:
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

    def selectByName(self, *args: Any, **kwargs: Any) -> Any:
        """selectByName(string, listAdjustment=kReplaceList) -> None

        Puts objects that match the give name on the active selection list.
        """

    def selectCommand(self, *args: Any, **kwargs: Any) -> Any:
        """selectCommand(MSelectionList, listAdjustment=kReplaceList) -> None

        Set the active selection list, by calling the built in Maya select
        command.  This differs from setActiveSelectionList in that in this
        version Maya takes over the selection list you give it and will be
        responsible for maintaing the necessary information required for
        undo, redo, and journaling.
        """

    def selectFromScreen(self, *args: Any, **kwargs: Any) -> Any:
        """selectFromScreen(short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None
        selectFromScreen(short, short, short, short, listAdjustment=kAddToList, selectMethod=kWireframeSelectMethod) -> None

        Perform click-pick type selection on the dag. If an object intersects
        the click point then it is selected according to listAdjustment.
        """

    def selectionMethod(self, *args: Any, **kwargs: Any) -> Any:
        """selectionMethod() -> int

        Determines the selection method that should be used in the currently active
        viewport.  This is useful as input to the "selectFromScreen" functions.
        """

    def selectionMode(self, *args: Any, **kwargs: Any) -> Any:
        """selectionMode() -> int

        Get current selection mode:
          kSelectObjectMode     Objects are selected as a whole. Components are not directly accessible.
          kSelectComponentMode  Components such as vertices are selectable in this mode.
          kSelectRootMode       Selecting the child in a hierarchy will also select its root DAG node.
          kSelectLeafMode       Selecting the child in a hierarchy will result only in that child being selected.
          kSelectTemplateMode   Templated objects are selectable in this mode.
        """

    def setActiveSelectionList(self, *args: Any, **kwargs: Any) -> Any:
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

    def setAnimSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """setAnimSelectionMask(mask) -> selfsetAnimSelectionMask(type) -> self

        Set the animation selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """

    def setComponentSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """setComponentSelectionMask(mask) -> selfsetComponentSelectionMask(type) -> self

        Set the component selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """

    def setDisableStow(self, *args: Any, **kwargs: Any) -> Any:
        """setDisableStow(bool) -> None

        This method is used to make the visiblity of all Maya windows unchangable.
        If set to true, it disables any attempts to change the visiblity of any window.
        In addition, all popup windows will be supressed.
        """

    def setDisplayCVs(self, *args: Any, **kwargs: Any) -> Any:
        """setDisplayCVs(MSelectionList, bool) -> None

        Controls drawing of control points in the specified selection list.

        The selection items on the given list will be marked for drawing. This
        overrides Maya's current draw list and allow, for example, the drawing
        of control points without being in vertex selection mode.
        """

    def setErrorLogPathName(self, *args: Any, **kwargs: Any) -> Any:
        """setErrorLogPathName(string) -> None

        Determines the default path name of the error log file.
        Returns an empty string on failure.
        """

    def setHiliteList(self, *args: Any, **kwargs: Any) -> Any:
        """setHiliteList(MSelectionList) -> None

        Sets the current hilite list. The current selection list is unchanged.
        """

    def setMiscSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """setMiscSelectionMask(mask) -> selfsetMiscSelectionMask(type) -> self

        Set the miscellaneous selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """

    def setObjectSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """setObjectSelectionMask(mask) -> selfsetObjectSelectionMask(type) -> self

        Set the object selection mask to the supplied value.

        * mask (MSelectionMask) - The selection mask.
        * type (int) - The selection type (see MSelectionMask.addMask() for a list of values).
        """

    def setOptionVarValue(self, *args: Any, **kwargs: Any) -> Any:
        """setOptionVarValue(string, int) -> bool
        setOptionVarValue(string name, double) -> bool
        setOptionVarValue(string name, string) -> bool


        This method is used to set the option variable value of int, bool, string type
        """

    def setPreselectionHiliteList(self, *args: Any, **kwargs: Any) -> Any:
        """setPreselectionHiliteList(MSelectionList) -> None

        Sets the objects for which Maya will display a preselection
        highlight in the viewports.

        The objects/components in the list will be drawn in Maya's
        preselection highlight style on the next viewport refresh
        (if preselection highlighting is enabled in the preferences).

        If preselection highlighting is not enabled, Maya will still
        store the list.
        """

    def setRichSelection(self, *args: Any, **kwargs: Any) -> Any:
        """setRichSelection(MRichSelection) -> None

        Set the current rich selection.
        """

    def setSelectionMode(self, *args: Any, **kwargs: Any) -> Any:
        """setSelectionMode(int) -> None

        Set the current selection mode.
        See selectionMode() for a list of valid modes.
        """

    def setTrackSelectionOrderEnabled(self, *args: Any, **kwargs: Any) -> Any:
        """setTrackSelectionOrderEnabled() -> None

        Set whether Maya should maintain an active selection list which
        maintains object and component selection order.
        """

    def setYAxisUp(self, *args: Any, **kwargs: Any) -> Any:
        """setYAxisUp() -> None

        This method sets the flag to identify which axis is Up, and
        rotates the ground plane around around the X-axis 90 degrees to get
        the Y-Up from Z-Up.
        """

    def setZAxisUp(self, *args: Any, **kwargs: Any) -> Any:
        """setZAxisUp() -> None

        This method sets the flag to identify which axis is Up, and
        rotates the ground plane around around the X-axis 90 degrees to get
        the Y-Up from Y-Up.
        """

    def sourceFile(self, *args: Any, **kwargs: Any) -> Any:
        """sourceFile(string) -> None

        Causes the MEL command engine to open the named file and execute
        the contents of the file as a MEL script.  If the provided fileName
        is a Unix absolute pathname, then that file is opened.  If a relative
        pathname is provided, the directories indicated by the environment
        variable, MAYA_SCRIPT_PATH, will be searched for a matching filename.
        """

    def startErrorLogging(self, *args: Any, **kwargs: Any) -> Any:
        """startErrorLogging() -> None
        startErrorLogging(string)

        This method enables output to the API error log file specified by the path.
        If another error log file is already open this method time and date stamps
        the log, and closes it.
        The new error log is time and date stamped when it is opened.

        If the new path name is the same as the current path name, this method ensures
        that logging is enabled, but no other action is taken.
        """

    def stopErrorLogging(self, *args: Any, **kwargs: Any) -> Any:
        """stopErrorLogging() -> None

        This method disables output to the API error log but does not close the log file.
        """

    def trackSelectionOrderEnabled(self, *args: Any, **kwargs: Any) -> Any:
        """trackSelectionOrderEnabled() -> bool

        Returns whether the selection order is currerntly being tracked.
        """

    def unselect(self, *args: Any, **kwargs: Any) -> Any:
        """unselect(MObject) -> None
        unselect(MDagPath, MObject) -> None

        Remove the given object/components from the active selection list.
        If components is null then the object will be unselected, otherwise
        the components will be unselected.

        Perform marquee type selection on the dag.  If an object intersects the
        selection rectangle, it is selected according to listAdjustment.
        """

    def unselectByName(self, *args: Any, **kwargs: Any) -> Any:
        """unselectByName(string) -> None

        Removes objects matching the pattern from the active selection list.
        """

    def upAxis(self, *args: Any, **kwargs: Any) -> Any:
        """upAxis() -> MVector

        This method returns the model's current up axis.
        """

    def viewFrame(self, *args: Any, **kwargs: Any) -> Any:
        """viewFrame(double) -> None
        viewFrame(MTime) -> None

        Sets the global time to the specified time.  This function is optimized
        for sequential time values that are monotonically increasing.  While
        one can set the time randomly with this function, a significant
        performance hit will be incurred.
        """


class MImage(object):
    """Manipulate color data."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(width, height, channels=4, type=kByte) -> self

        Create a new MImage object. Allocates memory for an RGBA array of pixels
        of the given size. If an object was already in memory, it is released first.

        * width (unsigned int) - the desired image's width in pixels.
        * height (unsigned int) - the desired image's height in pixels.
        * channels (unsigned int) - the desired number of channels per pixel.
        * type (int) - the desired pixel format (kByte or kFloat, see MImage.pixelType() description for details.)
        """

    def depth(self, *args: Any, **kwargs: Any) -> Any:
        """depth() -> int

        Get the color depth (in bytes) of the currently opened image.
        """

    def depthMap(self, *args: Any, **kwargs: Any) -> Any:
        """depthMap() -> long

        Returns a long containing a C++ 'float' pointer which points to the depth data.
        """

    def filter(self, *args: Any, **kwargs: Any) -> Any:
        """filter(sourceFormat, targetFormat, scale=1.0, offset=1.0) -> self

        Modify the content of the image by applying a filter.
        The dimension of the image remains the same; only the RGBA components get affected.

        * sourceFormat (MImageFilterFormat) - the format of the source image.
        * targetFormat (MImageFilterFormat) - the format of the resulting image.* scale (float) - vary depending on the source/target format.
        * offset (float) - vary depending on the source/target format.

        The scale argument for this filter can vary from -256.0 to 256.0, although typical values range from 1.0 to 10.0.
        The offset argument is currently ignored and should be left to the default value of 0.0.
        """

    def filterExists(self, *args: Any, **kwargs: Any) -> Any:
        """filterExists(sourceFormat, targetFormat) -> bool

        Return whether or not a given source format can be directly converted to a given target format.

        * sourceFormat (MImageFilterFormat) - the format of the source image.
        * targetFormat (MImageFilterFormat) - the format of the resulting image.
        """

    def floatPixels(self, *args: Any, **kwargs: Any) -> Any:
        """floatPixels() -> long

        Returns a long containing a C++ 'float' pointer which points to the pixel data.
        This data is uncompressed and tightly packed, of size (width * height * depth * sizeof( float)) bytes.
        """

    def getDepthMapRange(self, *args: Any, **kwargs: Any) -> Any:
        """getDepthMapRange() -> [minValue, maxValue]

        Compute the minimum and maximum depth values (range) for any stored depth buffer.
        """

    def getDepthMapSize(self, *args: Any, **kwargs: Any) -> Any:
        """getDepthMapSize() -> [width, height]

        Returns the size of the depth map buffer.
        """

    def getSize(self, *args: Any, **kwargs: Any) -> Any:
        """getSize() -> [width, height]

        Get the width and height of the currently opened image.
        """

    def haveDepth(self, *args: Any, **kwargs: Any) -> Any:
        """haveDepth() -> bool

        Returns True if this instance of MImage contains a depth map.
        """

    def isRGBA(self, *args: Any, **kwargs: Any) -> Any:
        """isRGBA() -> bool

        Query flag which indicates whether the pixel information is in RGBA sequence or BGRA sequence.
        If no pixel data exists, then False will be returned.
        """

    kByte: int = 1
    kFloat: int = 2
    kHeightFieldBumpFormat: int = 1
    kNoFormat: int = 0
    kNormalMapBumpFormat: int = 2
    kUnknown: int = 0
    kUnknownFormat: int = 3
    def pixelType(self, *args: Any, **kwargs: Any) -> Any:
        """pixelType() -> int

        Get the current pixel format of the image:  kUnknown    Format not known or invalid.
          kByte       One byte per channel, ranging from 0 to 255.
          kFloat      One float per channel, ranging from 0.0 to 1.0.
        """

    def pixels(self, *args: Any, **kwargs: Any) -> Any:
        """pixels() -> long

        Returns a long containing a C++ 'unsigned char' pointer which points to the pixel data.
        This data is uncompressed and tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.
        """

    def readDepthMap(self, *args: Any, **kwargs: Any) -> Any:
        """readDepthMap(pathname) -> self

        Reads the depth map from the specified file and place the result into the depth map array of this MImage instance.
        """

    def readFromFile(self, *args: Any, **kwargs: Any) -> Any:
        """readFromFile(pathname, type=kByte) -> self

        Attempt to identify and open the specified image file.

        * pathname (string) - the full path of the image file that should be opened.
        * type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type.
        """

    def readFromTextureNode(self, *args: Any, **kwargs: Any) -> Any:
        """readFromTextureNode(fileTextureObject, type=kByte) -> self

        Attempt to read the content of the given file texture node.


        * fileTextureObject (MObject) - an object that refers to the file texture node that should be read.
        * type (MPixelType) - the desired pixel format. kUnknown attempts to load the native pixel type.
        """

    def release(self, *args: Any, **kwargs: Any) -> Any:
        """release() -> self

        Release the current image. If there is no current image, the call is ignored.
        """

    def resize(self, *args: Any, **kwargs: Any) -> Any:
        """resize(width, height, preserveAspectRatio=True) -> self

        Resize the currently opened image to the specified dimension, or to the closest
        width/height that is preserves the original aspect ratio.* width (unsigned int) - the desired image's width in pixels.
        * height (unsigned int) - the desired image's height in pixels.
        * preserveAspectRatio (bool) - specifies whether the aspect ratio should be preserved or not.
                 If this flag is set, the given width and height are interpreted as the maximum dimensions allowable.
        """

    def setDepthMap(self, *args: Any, **kwargs: Any) -> Any:
        """setDepthMap(depth, width, heigth) -> self

        Specifies the depth map resolution and data.

        * depth (float*) - float buffer that contains depth values.
        * width (unsigned int) - the width of the depth buffer.
        * height (unsigned int) - the height of the depth buffer.

        * depth (MFloatArray) - float array that contains depth values.
        * width (unsigned int) - the width of the depth buffer.
        * height (unsigned int) - the height of the depth buffer.
        """

    def setFloatPixels(self, *args: Any, **kwargs: Any) -> Any:
        """setFloatPixels(pixels, width, height, channels=4) -> self

        Copy the uncompressed pixels array passed in into the MImage.
        This array is tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

        * pixels (float*) - the variable containing a block of pixels.
        * width (unsigned int) - the variable that will be set to the image's width in pixels.
        * height (unsigned int) - the variable that will be set to the image's height in pixels.
        * channels (unsigned int) - the number of channels per pixel.
        """

    def setPixels(self, *args: Any, **kwargs: Any) -> Any:
        """setPixels(pixels, width, height) -> self

        Copy the uncompressed pixels array passed in into the MImage.
        This array is tightly packed, of size (width * height * depth) bytes.
        For the moment, pixels are always stored in a RGBA (depth=4 bytes) pixel format.

        * pixels (unsigned char*) - the variable containing a block of pixels.
        * width (unsigned int) - the variable that will be set to the image's width in pixels.
        * height (unsigned int) - the variable that will be set to the image's height in pixels.
        """

    def setRGBA(self, *args: Any, **kwargs: Any) -> Any:
        """setRGBA(bool) -> self

        Sets a flag to indicate that pixel information is in RGBA sequence or BGRA sequence.
        Pixel data must have been allocated before this call is made.
        """

    def verticalFlip(self, *args: Any, **kwargs: Any) -> Any:
        """verticalFlip() -> bool

        Flips the image vertically.
        """

    def writeToFile(self, *args: Any, **kwargs: Any) -> Any:
        """writeToFile(pathname, outputFormat=iff) -> self

        Save the content of this image in a file. By default, the file is saved in IFF format.
        Optionally, the file can also be converted in a variety of image formats.
        """

    def writeToFileWithDepth(self, *args: Any, **kwargs: Any) -> Any:
        """writeToFileWithDepth(pathname, outputFormat=iff, writeDepth=False) -> self

        Save the content of this image in a file. By default, the file is saved in IFF format.
        Optionally, the file can also be converted in a variety of image formats.
        If the writeDepth parameter is True then any depth information stored in MImage will be written to file.
        """


class MInt64Array(object):
    """Array of MInt64 values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MInt64Array' objects>

class MIntArray(object):
    """Array of int values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MIntArray' objects>

class MItCurveCV(object):
    """An iterator for traversing a curve's CVs."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Returns the current CV in the iteration as an MObject.
        """

    def hasHistoryOnCreate(self, *args: Any, **kwargs: Any) -> Any:
        """hasHistoryOnCreate() -> bool

        This method determines if the shape was created with history.

        If the object that this iterator is attached to is not a shape then this method will fail.
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current edge in the iteration.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the edges have been traversed yet.
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next edge in the iteration.
        """

    def position(self, *args: Any, **kwargs: Any) -> Any:
        """position() -> MPoint

        Returns the position of the current CV.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def setPosition(self, *args: Any, **kwargs: Any) -> Any:
        """setPosition(point, space=kObject) -> self

        Sets the position of the current CV, in the given transformation

        space.

        * point       (MPoint) - The new position for the specified vertex
        * space (MSpace constant) - The transformation space
        """

    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """translateBy(vector, space=kObject) -> self

        Translate the current CV by the amount specified
        by the given vector.

        * vector (MVector) - The amount of translation
        * space (int) - The Transformation space
        """

    def updateCurve(self, *args: Any, **kwargs: Any) -> Any:
        """updateCurve() -> self

        This method is used to signal the curve that it has been changed and needs to redraw itself.

        When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified.
        """


class MItDag(object):
    """DAG Iterator.

    Use the DAG iterator to traverse the DAG either depth first or breadth
    first, visiting each node and, if desired, retrieving the node (as an
    MObject).  The DAG iterator provides a basic filtering capability, so
    that DAG node retrieval can be limited to a  specific type (MFn.Type)
    of node.  With filtering enabled the iterator checks to see if the node
    is compatible with the type of Function Set specified by the filter.
    See MFn.Type for a list of all valid Function set types.

    Since each object, if retrieved, is returned as an MObject, the
    MObject.hasFn() method can be used to further check for compatible
    function set types since an MObjects may be compatible with more than
    one function set).

    Any compatible Function Set can be attached to the retrieved object to
    query or or edit it.  Often you will want to use the DAG node Function
    Set (MFnDagNode), which is compatible with all DAG objects, to perform
    basic queries on each node as the iterator traverses the DAG.

    The iterator also provides the capability to reset the root of the
    iteration, the type of traversal, and the filter.

    Additionally, the iterator can be queried for the root, mode and type
    of traversal, and to determine if the the traversal has been completed.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Retrieves DAG node to which the iterator points.
        """

    def depth(self, *args: Any, **kwargs: Any) -> Any:
        """depth() -> integer

        Returns the height or depth of the current node in the DAG relative to the
        root node.  The root node has a depth of zero.
        """

    def fullPathName(self, *args: Any, **kwargs: Any) -> Any:
        """fullPathName() -> MString

        Return a string representing the full path from the root of the dag to this object.
        """

    def getAllPaths(self, *args: Any, **kwargs: Any) -> Any:
        """getAllPaths() -> MDagPathArray

        Determines all DAG Paths to current item in the iteration.
        """

    def getPath(self, *args: Any, **kwargs: Any) -> Any:
        """getPath() -> MDagPath

        Determines a DAG Path to the current item in the iteration.
        """

    def instanceCount(self, *args: Any, **kwargs: Any) -> Any:
        """instanceCount(total) -> Integer

        Determines the number of times the current item (DAG node) in the iteration
        is instanced.

        If total is False the number of direct instances is returned, which
        is the same as the node's parent count.

        If total is True the total number of instances is returned, including
        indirect instances resulting from instancing higher up the DAG hierarchy
        (i.e. one or more of the node's ancestors also has multiple instances).
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates end of iteration path.
        """

    def isInstanced(self, *args: Any, **kwargs: Any) -> Any:
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

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    kBreadthFirst: int = 2
    kDepthFirst: int = 1
    kInvalidType: int = 0
    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Moves to the next node matching the filter in the graph.
        """

    def partialPathName(self, *args: Any, **kwargs: Any) -> Any:
        """partialPathName() -> MString

        Return a string representing the partial path from the root of the
        dag to this object.

        The partial path is the minimum path that is still unique. This string
        may contain wildcards.
        """

    def prune(self, *args: Any, **kwargs: Any) -> Any:
        """prune() -> self

        Prunes iteration tree at current node.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def root(self, *args: Any, **kwargs: Any) -> Any:
        """root() -> MObject

        Returns the root (start node) of the current traversal.
        The constructor sets the root of traversal to the world node.
        The root can be changed by the reset() method.
        """

    def traversalType(self, *args: Any, **kwargs: Any) -> Any:
        """traversalType() -> MItDag.TraversalType

        Returns the direction of the traversal.
        """

    traverseUnderWorld: getset_descriptor = <attribute 'traverseUnderWorld' of 'OpenMaya.MItDag' objects>

class MItDependencyGraph(object):
    """Dependency Graph Iterator.

    Iterate over Dependency Graph (DG) Nodes or Plugs starting at a specified
    root Node or Plug.


    Set and query the root of the iteration.


    Set and query the direction (downstream or upstream), traversal priority
    (depth first or breadth first), level of detail (Node level or Plug
    level) and relationship (dependency, DG connection, eval graph) of the iteration.


    Set and disable a filter to iterate over only specific types (MFn.Type) of
    Nodes.


    Reset the root, filter, direction, traversal priority and level of detail
    of the iteration.


    Prune branches of the graph from iteration.


    In Maya, all geometry, animation and rendering information is implemented
    in nodes in the Dependency Graph (DG).  The DG includes the Directed Acyclic
    Graph (DAG).  Therefore, all DAG nodes are also DG nodes.  The data on nodes
    is associated with Attributes.  Attributes on nodes are connected to
    Attributes on other nodes via plugs on the Attributes.  Plugs are, in effect
    the external intefaces of Attributes.


    The DG Iterator Class (MItDependencyGraph) provides methods for iterating
    over either nodes or plugs, as well as methods for setting and querying the
    characteristics and behaviour of the iterator.


    This iterator will traverse all connected attributes upstream or
    downstream from the root node of the traversal. For non root nodes,
    only attributes that are affected by the incoming attribute to that
    node will be traversed.  Hence, only nodes to which data from the root
    node is flowing will be traversed. 


    By default, the iterator does not traverse world-space attribute
    dependencies (an example of a world-space dependency is that
    translateX affects worldMatrix). The
    setTraversalOverWorldSpaceDependents method can be used to enable such
    traversal. Note that even when world-space traversal is enabled, the
    iterator will only iterate to connected nodes. It does not iterate up
    and down through the dag hierarchy.


    The DG Iterator is used in conjunction with the Maya Object (MObject), plug
    (MPlug), Maya Object Array (MObjectArray) and plug Array (MPlugArray)
    classes.


    It is also useful to use Function Sets specific to the nodes returned by
    the iterator to query and modify the nodes in the DG.


    The DG itself can be modified using a DG Modifer (MDGModifier).


    Additionally, nodes can be added to and retrieved from selection lists using
    the Selection List (MSelectionList) class and Selection List Iterator
    (MItSelectionList).  This can be useful for obtaining the root node for an
    iteration.


    Attributes on the nodes can be manipulated using the Attribute Function Set
    (MFnAttribute) and its derivations.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    currentDirection: getset_descriptor = <attribute 'currentDirection' of 'OpenMaya.MItDependencyGraph' objects>
    currentFilter: getset_descriptor = <attribute 'currentFilter' of 'OpenMaya.MItDependencyGraph' objects>
    currentLevel: getset_descriptor = <attribute 'currentLevel' of 'OpenMaya.MItDependencyGraph' objects>
    def currentNode(self, *args: Any, **kwargs: Any) -> Any:
        """currentNode() -> MObject

        Retrieves the current node of the iteration.  Results in a null object on
        failure or if the node is of a unrecognized type.
        """

    def currentNodeHasUnknownType(self, *args: Any, **kwargs: Any) -> Any:
        """currentNodeHasUnknownType() -> Bool

        Indicates whether or not the current node has an unrecognised
        type.  This is useful if an unexpected failure is encountered
        in the next() or currentNode() methods.
        """

    def currentPlug(self, *args: Any, **kwargs: Any) -> Any:
        """currentPlug() -> MPlug

        Retrieves the current plug of the iteration.  Results in a null
        plug on failure.
        """

    currentRelationship: getset_descriptor = <attribute 'currentRelationship' of 'OpenMaya.MItDependencyGraph' objects>
    currentTraversal: getset_descriptor = <attribute 'currentTraversal' of 'OpenMaya.MItDependencyGraph' objects>
    def getNodePath(self, *args: Any, **kwargs: Any) -> Any:
        """getNodePath() -> MObjectArray

        Retrieves the direct path from the current node to the root
        node.  Path does not include the current node.
        State of the provided array is undefined if this method fails.
        """

    def getNodesVisited(self, *args: Any, **kwargs: Any) -> Any:
        """getNodesVisited() -> MObjectArray

        Retrieves all nodes visited during the iteration.
        State of the provided array is undefined if this method fails.
        """

    def getPlugPath(self, *args: Any, **kwargs: Any) -> Any:
        """getPlugPath() -> MPlugArray

        Retrieves the direct path from the current plug to the root
        plug, with the current plug in element 0 of the array and the root
        plug in the final element of the array.

        Once the iterator is done (i.e. isDone() returns True) there is no
        longer a current plug and this method will return an empty array.

        If this method fails the state of the returned array is undefined.
        """

    def getPlugsVisited(self, *args: Any, **kwargs: Any) -> Any:
        """getPlugsVisited() -> MPlugArray

        Retrieves all plugs visited during the iteration.
        State of the provided array is undefined if this method fails.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates whether or not all nodes or plugs have been iterated over
        in accordance with the direction, traversal, level, relationship and filter.
        If a valid filter is set, the iterator only visits those nodes that match
        the filter.
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    kBreadthFirst: int = 1
    kConnectedTo: int = 1
    kDependsOn: int = 0
    kDepthFirst: int = 0
    kDownstream: int = 0
    kEvaluationGraph: int = 2
    kNodeLevel: int = 0
    kPlugLevel: int = 1
    kUpstream: int = 1
    def next(self, *args: Any, **kwargs: Any) -> Any:
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

    nodeDepth: getset_descriptor = <attribute 'nodeDepth' of 'OpenMaya.MItDependencyGraph' objects>
    def previousPlug(self, *args: Any, **kwargs: Any) -> Any:
        """previousPlug() -> MPlug

        Retrieves the previous plug of the iteration.  Results in a
        null plug on failure.  Null plug may also indicate that the
        current plug is the root plug.
        """

    def prune(self, *args: Any, **kwargs: Any) -> Any:
        """prune() -> self

        Prunes the search path at the current plug.  Iterator will not
        visit any of the plugs connected to the pruned plug.
        """

    pruningOnFilter: getset_descriptor = <attribute 'pruningOnFilter' of 'OpenMaya.MItDependencyGraph' objects>
    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Clears iterator data and resets the iterator to the root node
        or plug.  If a valid filter is enabled, the iterator
        automatically advances to the next node after the root node
        that matches the filter.  If no matching node is found an
        exception is thrown.
        """

    def resetFilter(self, *args: Any, **kwargs: Any) -> Any:
        """resetFilter() -> self

        Resets the node or plug filter to default, MFn.kInvalid
        (filter disabled).  Disables pruning on the filter (default).
        Resets the iterator.
        """

    def resetTo(self, *args: Any, **kwargs: Any) -> Any:
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

    def rootNode(self, *args: Any, **kwargs: Any) -> Any:
        """rootNode() -> MObject

        Retrieves the root node of the iteration.
        """

    def rootPlug(self, *args: Any, **kwargs: Any) -> Any:
        """rootPlug() -> MPlug

        Retrieves the root plug of the iteration.
        """

    traversingOverWorldSpaceDependents: getset_descriptor = <attribute 'traversingOverWorldSpaceDependents' of 'OpenMaya.MItDependencyGraph' objects>

class MItDependencyNodes(object):
    """Dependency Node iterator.

    Use the dependency node iterator to traverse all the nodes in Maya's
    Dependency Graph.

    With filtering enabled, the iterator checks to see if the node is
    compatible with the type specified by the filter.  See MFn.Type for a
    list of all valid types.

    Since MObjects may be compatible with more than one type (nodes are
    organised in a hierarchy) the MObject.hasFn() method can be used to
    further check for compatible types.

    Any compatible Function Set can be attached to the retrieved object to
    query or or edit it.  Often you will want to use the dependency node
    function set (MFnDependencyNode), which is compatible with all
    dependency nodes, to perform queries on each node as the iterator
    traverses the Dependency Graph.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates end of the iteration.
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Moves to the next node matching the filter.  If the filter
        is set to kInvalid, this method advances to the next
        DG node without doing any filtering.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self
        reset(filterType = MFn.kInvalid) -> self
        reset(dagInfoObject) -> self


        Resets the iterator.


           dagInfoObject (MIteratorType) - Iterator object having info on filter or filterlist.
           filterType (MFn.Type) - Function set type, defaults to MFn.kInvalid.
        """

    def thisNode(self, *args: Any, **kwargs: Any) -> Any:
        """thisNode() -> MObject

        Retrieves the dependency node to which the iterator points.
        """


class MItGeometry(object):
    """Geometry iterator.

    This class is the iterator class for geometry data, and can be used to
    loop over the CVs of NURBS, the points of subds & lattices, and the
    vertices of polygonal meshes.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def allPositions(self, *args: Any, **kwargs: Any) -> Any:
        """allPositions() -> MStatus

        Return the position of all the points/CVs/vertices.  This
        operation is faster than using the iterator to get values one by
        one, but uses more memory as it requires an array to hold all the
        values to be returned.
        """

    def component(self, *args: Any, **kwargs: Any) -> Any:
        """component() -> MObject

            DEPRECATED in 2019, use currentItem instead.
        This method returns the current component in the iteration.
        """

    def count(self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int


        Return the number of items in this iteration. This number will
        always be at least as large as the number of items, however in
        some cases it may be larger. It is useful if allocating space in
        an array to hold the results, since it will always be of
        sufficient size. If the exact number of items is required, use the
        exactCount method instead. The exactCount method is however
        significantly slower than this method.
        """

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        This method returns the current component in the iteration.
        """

    def exactCount(self, *args: Any, **kwargs: Any) -> Any:
        """exactCount() -> int


        Return the exact number of items in this iteration. This method is
        significantly slower than the count() method, so use if only if
        the precise number is required.
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int


        This method returns the index of the current point/CV/vertex
        component in the iteration.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> Bool

        Indicates end of the iteration.
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next component in the iteration.
        If the iterator is already at the last component then this
        method has no effect. Use isDone to determine if the iterator
        is at the last component.
        """

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """normal() -> MVector

        Return the normal of the current point/CV/vertex component.
        """

    def position(self, *args: Any, **kwargs: Any) -> Any:
        """position() -> MPoint

        Return the position of the current point/CV/vertex component.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self


        Resets the iterator.
        """

    def setAllPositions(self, *args: Any, **kwargs: Any) -> Any:
        """setAllPositions() -> MStatus

        Set the position of all the points/CVs/vertices at once. This
        operation is faster than using the iterator to set values one by
        one, but uses more memory as it requires an array to hold all the
        values to be set.
        """

    def setPosition(self, *args: Any, **kwargs: Any) -> Any:
        """setPosition() -> MStatus

        Set the position of the current point/CV/vertex.
        """

    def weight(self, *args: Any, **kwargs: Any) -> Any:
        """weight() -> MWeight

        Return the weight of the current point/CV/vertex component.
        """


class MItMeshEdge(object):
    """An iterator for traversing a mesh's edges."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def center(self, *args: Any, **kwargs: Any) -> Any:
        """center(space=kObject) -> MPoint

        Returns the center point of the edge, in the given transformation space.

        * space (MSpace constant) - The  transformation space
        """

    def connectedToEdge(self, *args: Any, **kwargs: Any) -> Any:
        """connectedToEdge(index) -> bool

        Determines whether the given edge is connected to the current edge.

        * index (int) - Index of edge to check.
        """

    def connectedToFace(self, *args: Any, **kwargs: Any) -> Any:
        """connectedToFace(index) -> bool

        Determines whether the given face contains the current edge.

        * index (int) - Index of face to check.
        """

    def count(self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Return the number of edges in the iteration
        """

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Returns the current edge in the iteration as a component.

        Components are used to specify one or more edges and are useful in operating on groups of non-contiguous edges for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """

    def geomChanged(self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Resets the geom pointer in the MItMeshEdge. If you're using MFnMesh to
        update Normals or Color per vertex while iterating, you must call geomChanged
        on the iterator immediately after the MFnMesh call to make sure that your
        geometry is up to date. A crash may result if this method is not called.
        A similar approach must be taken for updating upstream vertex tweaks
        with an MPlug. After the update, call this method.
        """

    def getConnectedEdges(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedEdges() -> MIntArray

        Returns the indices of edges connected to the current edge.
        """

    def getConnectedFaces(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedFaces() -> MIntArray

        Returns the indices of the faces connected to the current edge.
        Normally a boundary edge will only have one face connected to it and
        an internal edge will have two, but if the mesh has manifold geometry
        then the edge may have three or more faces connected to it.
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current edge in the iteration.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the edges have been traversed yet.
        """

    isSmooth: getset_descriptor = <attribute 'isSmooth' of 'OpenMaya.MItMeshEdge' objects>
    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def length(self, *args: Any, **kwargs: Any) -> Any:
        """length(space=kObject) -> float

        Returns the length of the edge, in the given transformation space.

        * space (MSpace constant) - The  transformation space
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next edge in the iteration.
        """

    def numConnectedEdges(self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedEdges() -> int

        Returns the number of edges connected to the current edge.
        """

    def numConnectedFaces(self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedFaces() -> int

        Returns the number of faces connected to the current edge.
        """

    def onBoundary(self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary() -> bool

        Determines if the current edge is a border edge.
        """

    def point(self, *args: Any, **kwargs: Any) -> Any:
        """point(whichVertex, space=kObject) -> MPoint

        Returns the position of one of the current edge's vertices, int the
        given transformation space.

        * whichVertex    (0 or 1) - Which of the edge's two vertices to return
        * space (MSpace constant) - The transformation space
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def setIndex(self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(index) -> int

        Sets the index of the current edge to be accessed. The current edge
        will no longer be in sync with any previous iteration.

        Returns the index of the edge which was current before the change.


        * index (int) - The index of desired edge to access. 
        """

    def setPoint(self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(point, whichVertex, space=kObject) -> self

        Sets the position of one of the current edge's vertices, in the given
        transformation space.

        * point       (MPoint) - The new position for the specified vertex
        * whichVertex (0 or 1) - Which of the edge's 2 vertices to set.
        * space (MSpace constant) - The transformation space
        """

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Tells Maya that mesh has been changed and needs to redraw itself.
        """

    def vertexId(self, *args: Any, **kwargs: Any) -> Any:
        """vertexId(whichVertex) -> int

        Returns the global index (as opposed to face-relative index) of one of
        the edge's vertices.

        * whichVertex (0 or 1) - Which of the edge's 2 vertices to use.
        """


class MItMeshFaceVertex(object):
    """An iterator for traversing a mesh's face vertices."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Returns the current faceVertex as a double-indexed component.
        """

    def faceId(self, *args: Any, **kwargs: Any) -> Any:
        """faceId() -> int

        Returns the current face index.
        """

    def faceVertexId(self, *args: Any, **kwargs: Any) -> Any:
        """faceVertexId() -> int

        Returns the relative index of the vertex within the current face. This
        index together with the faceId can be used for a fast access to get
        various info stored per vertex (normals, uvs, colors).
        """

    def geomChanged(self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Resets the geom pointer in the MItMeshFaceVertex. If you're using
        MFnMesh to update Normals or Color per vertex while iterating, you
        must call geomChanged on the iterator immediately after the MFnMesh
        call to make sure that your geometry is up to date. A crash may result
        if this method is not called. A similar approach must be taken for
        updating upstream vertex tweaks with an MPlug. After the update, call
        this method.
        """

    def getBinormal(self, *args: Any, **kwargs: Any) -> Any:
        """getBinormal(space=MSpace.kObject, uvSet='') -> MVector

        Returns the face vertex binormal associated with the UV set.
        """

    def getColor(self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorSetName='') -> MColor

        Returns a color of the current face vertex.
        """

    def getColorIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndex(colorSetName='') -> int

        Return a color index of the current face vertex.
        """

    def getNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getNormal(space=MSpace.kObject) -> MVector

        Returns the face vertex normal.
        """

    def getTangent(self, *args: Any, **kwargs: Any) -> Any:
        """getTangent(space=MSpace.kObject, uvSet='') -> MVector

        Returns the face vertex tangent associated with the given UV set. The
        tangent is defined as the surface tangent of the polygon running in
        the U direction.
        """

    def getUV(self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvSet='') -> (float, float)

        Returns the texture coordinate for the current face vertex.
        """

    def getUVIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndex(uvSet='') -> int

        Returns the index of the texture coordinate for the current face
        vertex. This index refers to an element of the mesh's texture
        coordinate array as returned by MFnMesh::getUVs().
        """

    def hasColor(self, *args: Any, **kwargs: Any) -> Any:
        """hasColor() -> bool

        Returns whether the current face vertex has a color-per-vertex set.
        """

    def hasUVs(self, *args: Any, **kwargs: Any) -> Any:
        """hasUVs(uvSet='') -> bool

        Returns whether the current face vertex has UVs mapped in the given
        set.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the face vertices have been traversed.
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next face vertex in the iteration.
        """

    def normalId(self, *args: Any, **kwargs: Any) -> Any:
        """normalId() -> int

        Returns the normal index for the specified vertex. This index refers
        to an element in the normal array returned by MFnMesh::getNormals().
        These normals are per-face per-vertex normals.
        """

    def position(self, *args: Any, **kwargs: Any) -> Any:
        """position(space=MSpace.kObject) -> MPoint

        Returns the position of the current face vertex.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def setIndex(self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(faceId, faceVertexId) -> (oldFaceId, oldFaceVertexId)

        Sets the index of the current face vertex to be accessed. The current
        face vertex will no longer be in sync with any previous iteration.

        Returns the indices of the old face and vertex.


        * faceId (int) - Index of desired face to access.
        * faceVertexId (int) - Face-relative index of desired vertex to access.
        * oldFaceId (int) - Index of the face which was current before the change.
        * oldFaceVertexId (int) - Face-relative index of the vertex which was current before the change.
        """

    def tangentId(self, *args: Any, **kwargs: Any) -> Any:
        """tangentId() -> int

        Returns the tangent index for the current face vertex. This index
        refers to an element in the array returned by MFnMesh::getTangents.
        These tangents are per-face per-vertex.
        """

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Tells Maya that mesh has been changed and needs to redraw itself.
        """

    def vertexId(self, *args: Any, **kwargs: Any) -> Any:
        """vertexId() -> int

        Returns the global (as opposed to face-relative) index of the
        current vertex.
        """


class MItMeshPolygon(object):
    """This class is the iterator for polygonal surfaces (meshes)."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def center(self, *args: Any, **kwargs: Any) -> Any:
        """center(space=kObject) -> MPoint

        Return the position of the center of the current polygon

        * space (int) - The coordinate system for this operation
        """

    def count(self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Return the number of polygons in the iteration
        """

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Get the current polygon in the iteration as a component.

        Components are used to specify one or more polygons and are usefull in operating on groups of non-contiguous polygons for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """

    def geomChanged(self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Reset the geom pointer in the MItMeshPolygon. This is now being handled automatically inside the iterator, and users should no longer need to call this method directly to sync up the iterator to changes made by MFnMesh
        """

    def getArea(self, *args: Any, **kwargs: Any) -> Any:
        """getArea(space=kObject) -> float

        This method gets the area of the face

        * space (int) - World Space or Object Space
        """

    def getColor(self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorSetName=None) -> MColor
        getColor(vertexIndex) -> MColor

        This method gets the color of the specified vertex in this face

        * index (int) - The face-relative vertex index on this face

        Or the average color of the all the vertices in this face

        * colorSetName (string) - Name of the color set.
        """

    def getColorIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndex(vertexIndex, colorSetName=None) -> int

        This method returns the colorIndex for a vertex of the current face.

        * vertexIndex (int) - Face-relative index of vertex.
        * colorSetName (string) - Name of the color set.
        """

    def getColorIndices(self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndices(colorSetName=None) -> MIntArray

        This method returns the colorIndices for each vertex on the face.

        * colorSetName (string) - Name of the color set.
        """

    def getColors(self, *args: Any, **kwargs: Any) -> Any:
        """getColors(colorSetName=None) -> MColorArray

        This method gets the color of the each vertex in the current face.

        * colorSetName (string) - Name of the color set.
        """

    def getConnectedEdges(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedEdges() -> MIntArray

        This method gets the indices of the edges connected to the vertices of the current face, but DOES not include the edges contained in the current face
        """

    def getConnectedFaces(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedFaces() -> MIntArray

        This method gets the indices of the faces connected to the current face.
        """

    def getConnectedVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedVertices() -> MIntArray

        This method gets the object-relative indices of the vertices surrounding the vertices of the current face, but does not include the vertices of the current face
        """

    def getEdges(self, *args: Any, **kwargs: Any) -> Any:
        """getEdges() -> MIntArray

        This method gets the indices of the edges contained in the current face.
        """

    def getNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getNormal(space=kObject) -> MVector
        getNormal(vertexIndex, [space=]kObject) -> MVector

        Return the face normal of the current polygon.

        * space (int) - The transformation space. The keyword 'space' has to be explicitly stated. If not present, the argument will be identified as a 'vertexIndex' argument, and the second form of this function will be used instead.

        Returns the vertex-face normal for the vertex in the current polygon.

        * index (int) - face-relative vertex index of the vertex whose normal to retrieve
        * space (int) - The transformation space. Defaults to kObject, the keyword 'space' is optional as well.
        """

    def getNormals(self, *args: Any, **kwargs: Any) -> Any:
        """getNormals(space=kObject) -> MVectorArray

        Returns the normals for all vertices in the current face

        * space (int) - The transformation space
        """

    def getPointAtUV(self, *args: Any, **kwargs: Any) -> Any:
        """getPointAtUV(uvPoint, space=kObject, uvSet=None, tolerance=0) -> MPoint

        Return the position of the point at the given UV value in the current polygon.

        * uvPoint ([float, float]) - The UV value to try to locate
        * space (int) - The coordinate system for this operation
        * uvSet (string) - UV set to work with
        * tolerance (float) - tolerance value to compare float data type
        """

    def getPoints(self, *args: Any, **kwargs: Any) -> Any:
        """getPoints(space=kObject) -> MPointArray

        Retrieves the positions of the vertices on the current face/polygon that the iterator is pointing to. Vertex positions will be inserted into the given array and will be indexed using face-relative vertex IDs (ie. ordered from 0 to (vertexCount of the face) - 1), which should not be confused with the vertexIDs of each vertex in relation to the entire mesh object. 

        * space (int) - The coordinate system for this operation
        """

    def getTriangle(self, *args: Any, **kwargs: Any) -> Any:
        """getTriangle(localTriIndex, space=kObject) -> [MPointArray, MIntArray]

        Get the vertices and vertex positions of the given triangle in the current face's triangulation.

        * localTriIndex (int) - Local index of the desired triangle in this face
        * space (int) - World Space or Object Space
        """

    def getTriangles(self, *args: Any, **kwargs: Any) -> Any:
        """getTriangles(space=kObject) -> [MPointArray, MIntArray]

        Get the vertices and vertex positions of all the triangles in the current face's triangulation

        * space (int) - World Space or Object Space
        """

    def getUV(self, *args: Any, **kwargs: Any) -> Any:
        """getUV(vertexId, uvSet=None) -> [float, float]

        Return the texture coordinate for the given vertex.

        * vertex (int) - The face-relative vertex index to get UV for
        * uvSet (string) - UV set to work with
        """

    def getUVArea(self, *args: Any, **kwargs: Any) -> Any:
        """getUVArea(uvSet=None) -> float

        This method gets the UV area of the face

        * uvSet (string) - UV set to work with
        """

    def getUVAtPoint(self, *args: Any, **kwargs: Any) -> Any:
        """getUVAtPoint(pt, space=kObject, uvSet=None) -> [float, float]

        Find the point closest to the given point in the current polygon, and return the UV value at that point.

        * pt (MPoint) - The point to try to get UV for
        * space (int) - The coordinate system for this operation
        * uvSet (string) - UV set to work with
        """

    def getUVIndex(self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndex(vertex, uvSet=None) -> int

        Returns the index of the texture coordinate for the given vertex.
        This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

        * vertex (int) - The face-relative vertex index of the current polygon
        * uvSet (string) - UV set to work with
        """

    def getUVIndexAndValue(self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndexAndValue(vertex, uvSet=None) -> [int, float, float]

        Return the index and value of the texture coordinate for the given vertex. This index refers to an element of the texture coordinate array for the polygonal object returned by MFnMesh.getUVs.

        * vertex (int) - The face-relative vertex index of the current polygon
        * uvSet (string) - UV set to work with
        """

    def getUVSetNames(self, *args: Any, **kwargs: Any) -> Any:
        """getUVSetNames() -> list of strings

        This method is used to find the UV set names mapped to the current face
        """

    def getUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getUVs(uvSet=None) -> [MFloatArray, MFloatArray]

        Return the all the texture coordinates for the vertices of this face (in local vertex order).

        * uvSet (string) - UV set to work with
        """

    def getVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getVertices() -> MIntArray

        This method gets the indices of the vertices of the current face
        """

    def hasColor(self, *args: Any, **kwargs: Any) -> Any:
        """hasColor() -> bool
        hasColor(localVertexIndex) -> bool

        This method determines whether the current face has color-per-vertex set for any or the given vertex

        * localVertexIndex (int) - face-relative vertex index to check for color on
        """

    def hasUVs(self, *args: Any, **kwargs: Any) -> Any:
        """hasUVs(uvSet=None) -> bool

        Tests whether this face has UV's mapped or not (either all the vertices for a face should have UV's, or none of them do, so the UV count for a face is either 0, or equal to the number of vertices).

        * uvSet (string) - UV set to work with
        """

    def hasValidTriangulation(self, *args: Any, **kwargs: Any) -> Any:
        """hasValidTriangulation() -> bool

        This method checks if the face has a valid triangulation. If it doesn't, then the face was bad geometry: it may gave degenerate points or cross over itself.
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current polygon
        """

    def isConnectedToEdge(self, *args: Any, **kwargs: Any) -> Any:
        """isConnectedToEdge(index) -> bool

        This method determines whether the given face is adjacent to the current face

        * index (int) - Index of the face to be tested for
        """

    def isConnectedToFace(self, *args: Any, **kwargs: Any) -> Any:
        """isConnectedToFace(index) -> bool

        This method determines whether the given face is adjacent to the current face

        * index (int) - Index of the face to be tested for
        """

    def isConnectedToVertex(self, *args: Any, **kwargs: Any) -> Any:
        """isConnectedToVertex(index) -> bool

        This method determines whether the given vertex shares an edge with a vertex in the current face

        * index (int) - Index of the face to be tested for
        """

    def isConvex(self, *args: Any, **kwargs: Any) -> Any:
        """isConvex() -> bool

        This method checks if the face is convex.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the polygons have been traversed yet.
        """

    def isHoled(self, *args: Any, **kwargs: Any) -> Any:
        """isHoled() -> bool

        This method checks if the face has any holes.
        """

    def isLamina(self, *args: Any, **kwargs: Any) -> Any:
        """isLamina() -> bool

        This method checks if the face is a lamina (the face is folded over onto itself).
        """

    def isPlanar(self, *args: Any, **kwargs: Any) -> Any:
        """isPlanar() -> bool

        This method checks if the face is planar
        """

    def isStarlike(self, *args: Any, **kwargs: Any) -> Any:
        """isStarlike() -> bool

        This method checks if the face is starlike. That is, a line from the centre to any vertex lies entirely within the face.
        """

    def isUVReversed(self, *args: Any, **kwargs: Any) -> Any:
        """isUVReversed(faceId) -> bool

        Returns True if the texture coordinates (uv's) for the face are
        reversed (clockwise), False if they are not reversed (counter clockwise).
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next polygon in the iteration.
        """

    def normalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """normalIndex(vertex) -> int

        Returns the normal index for the specified vertex.
        This index refers to an element in the normal array returned by MFnMesh.getNormals.  These normals are per-polygon per-vertex normals. See the MFnMesh description for more information on normals.

        * localVertexIndex (int) - The face-relative index of the vertex to examine for the current polygon
        """

    def numColors(self, *args: Any, **kwargs: Any) -> Any:
        """numColors(colorSetName=None) -> int

        This method checks for the number of colors on vertices in this face

        * colorSetName (string) - Name of the color set.
        """

    def numConnectedEdges(self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedEdges() -> int

        This method checks for the number of connected edges on the vertices of this face
        """

    def numConnectedFaces(self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedFaces() -> int

        This method checks for the number of connected faces
        """

    def numTriangles(self, *args: Any, **kwargs: Any) -> Any:
        """numTriangles() -> int

        This Method checks for the number of triangles in this face in the current triangulation
        """

    def onBoundary(self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary() -> bool

        This method determines whether the current face is on a boundary
        """

    def point(self, *args: Any, **kwargs: Any) -> Any:
        """point(index, space=kObject) -> MPoint

        Return the position of the vertex at index in the current polygon.

        * index (int) - The face-relative index of the vertex in the current polygon
        * space (int) - The coordinate system for this operation
        """

    def polygonVertexCount(self, *args: Any, **kwargs: Any) -> Any:
        """polygonVertexCount() -> int

        Return the number of vertices for the current polygon
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def setIndex(self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(index) -> int

        This method sets the index of the current face to be accessed.
        The current face will no longer be in sync with any previous iteration.
        Returns the index of the current face in the iteration

        * index (int) - The index of desired face to access.
        """

    def setPoint(self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(point, index, space=kObject) -> self

        Set the vertex at the given index in the current polygon.

        * point (MPoint) - The new position for the vertex
        * index (int) - The face-relative index of the vertex in the current polygon
        * space (int) - The coordinate system for this operation
        """

    def setPoints(self, *args: Any, **kwargs: Any) -> Any:
        """setPoints(pointArray, space=kObject) -> self

        Sets new locations for vertices of the current polygon that the iterator is pointing to.

        * pointArray (MPointArray) - The new positions for the vertices.
        * space (int) - The coordinate system for this operation.
        """

    def setUV(self, *args: Any, **kwargs: Any) -> Any:
        """setUV(vertexId, uvPoint, uvSet=None) -> self

        Modify the UV value for the given vertex in the current face.
        If the face is not already mapped, this method will fail.

        * vertexId (int) - face-relative index of the vertex to set UV for.
        * uvPoint ([float, float]) - The UV values to set it to
        * uvSet (string) - UV set to work with
        """

    def setUVs(self, *args: Any, **kwargs: Any) -> Any:
        """setUVs(uArray, vArray, uvSet=None) -> self

        Modify the UV value for all vertices in the current face.
        If the face has not already been mapped, this method will fail.

        * uArray (MFloatArray) - All the U values - in local face order
        * vArray (MFloatArray) - The corresponding V values
        * uvSet (string) - UV set to work with
        """

    def tangentIndex(self, *args: Any, **kwargs: Any) -> Any:
        """tangentIndex(localVertexIndex) -> int

        Returns the tangent (or binormal) index for the specified vertex.
        This index refers to an element in the normal array returned by MFnMesh.getTangents. These tangent or binormals are per-polygon per-vertex.
        See the MFnMesh description for more information on tangents and binormals.

        * localVertexIndex(int) - The face-relative index of the vertex to examine for the current polygon
        """

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signal that this polygonal surface has changed and needs to redraw itself.
        """

    def vertexIndex(self, *args: Any, **kwargs: Any) -> Any:
        """vertexIndex(index) -> int

        Returns the object-relative index of the specified vertex of the current polygon.
        The index returned may be used to refer to an element in the vertex list returned by MFnMesh.getPoints. 

        * index (int) - The face-relative index of the vertex in the polygon
        """

    def zeroArea(self, *args: Any, **kwargs: Any) -> Any:
        """zeroArea() -> bool

        This method checks if its a zero area face
        """

    def zeroUVArea(self, *args: Any, **kwargs: Any) -> Any:
        """zeroUVArea(uvSet=None) -> bool

        This method checks if the UV area of the face is zero

        * uvSet (string) - UV set to work with
        """


class MItMeshVertex(object):
    """This class is the iterator for polygonal surfaces (meshes)."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def connectedToEdge(self, *args: Any, **kwargs: Any) -> Any:
        """connectedToEdge(index) -> bool

        This method determines whether the given edge contains the current vertex

        * index (int) - Index of edge to check.
        """

    def connectedToFace(self, *args: Any, **kwargs: Any) -> Any:
        """connectedToFace(index) -> bool

        This method determines whether the given face contains the current vertex

        * index (int) - Index of face to check.
        """

    def count(self, *args: Any, **kwargs: Any) -> Any:
        """count() -> int

        Return the number of vertices in the iteration
        """

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Get the current vertex in the iteration as a component.

        Components are used to specify one or more vertices and are usefull in operating on groups of non-contiguous vertices for a surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """

    def geomChanged(self, *args: Any, **kwargs: Any) -> Any:
        """geomChanged() -> self

        Reset the geom pointer in the MItMeshVertex. If you're using MFnMesh to
        update Normals or Color per vertex while iterating, you must call geomChanged
        on the iteratior immediately after the MFnMesh call to make sure that your
        geometry is up to date. A crash may result if this method is not called.
        A similar approach must be taken for updating upstream vertex tweaks
        with an MPlug. After the update, call this method.
        """

    def getColor(self, *args: Any, **kwargs: Any) -> Any:
        """getColor(colorSetName=None) -> MColor
        getColor(faceIndex, colorSetName=None) -> MColor

        This method gets the average color of the vertex

        * colorSetName (string) - Name of the color set.

        This method gets the color of the current vertex in the specified face

        * index (int) - The face to get the color for this vertex for* colorSetName (string) - Name of the color set.
        """

    def getColorIndices(self, *args: Any, **kwargs: Any) -> Any:
        """getColorIndices(colorSetName=None) -> MIntArray

        This method returns the colorIndices into the color array see MFnMesh::getColors()
        of the current vertex.

        * colorSetName (string) - Name of the color set.
        """

    def getColors(self, *args: Any, **kwargs: Any) -> Any:
        """getColors(colorSetName=None) -> MColorArray

        This method gets the colors of the current vertex for each face it
        belongs to. If no colors are assigned to the vertex at all, the
        return values will be (-1 -1 -1 1). If some but not all of the
        vertex/face colors have been explicitly set, the ones that have not
        been set will be (0, 0, 0, 1).

        * colorSetName (string) - Name of the color set.
        """

    def getConnectedEdges(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedEdges() -> MIntArray

        This method gets the indices of the edges contained in the current vertex.
        """

    def getConnectedFaces(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedFaces() -> MIntArray

        This method gets the indices of the faces connected to the current vertex.
        """

    def getConnectedVertices(self, *args: Any, **kwargs: Any) -> Any:
        """getConnectedVertices() -> MIntArray

        This method gets the indices of the vertices surrounding the current vertex.
        """

    def getNormal(self, *args: Any, **kwargs: Any) -> Any:
        """getNormal(space=kObject) -> MVector
        getNormal(faceIndex, space=kObject) -> MVector

        Return the normal or averaged normal if unshared of the current vertex.

        * space (int) - The transformation space

        Return the normal of the current vertex in the specified face.

        * faceIndex (int) - face index to get normal for
        * space (int) - The transformation space
        """

    def getNormalIndices(self, *args: Any, **kwargs: Any) -> Any:
        """getNormalIndices() -> MIntArray

        This method returns the normal indices of the face/vertex associated
        with the current vertex.
        """

    def getNormals(self, *args: Any, **kwargs: Any) -> Any:
        """getNormals(space=kObject) -> MVectorArray

        Return the normals of the current vertex for all faces

        * space (int) - The transformation space
        """

    def getOppositeVertex(self, *args: Any, **kwargs: Any) -> Any:
        """getOppositeVertex(edgeId) -> int

        This method gets the other vertex of the given edge

        * edgeId (int) - The edge to get the other vertex for
        """

    def getUV(self, *args: Any, **kwargs: Any) -> Any:
        """getUV(uvSet=None) -> [float, float]getUV(faceId, uvSet=None) -> [float, float]

        Get the shared UV value at this vertex.

        * uvSet (string) - Name of the uv set to work with.

        Get the UV value for the give facen at the current vertex.

        * faceId (int) - Index of the required face
        * uvSet (string) - Name of the uv set to work with
        """

    def getUVIndices(self, *args: Any, **kwargs: Any) -> Any:
        """getUVIndices(uvSet=None) -> MIntArray

        This method returns the uv indices into the normal array see MFnMesh::getUVs()
        of the current vertex.

        * uvSet (string) - Name of the uv set.
        """

    def getUVs(self, *args: Any, **kwargs: Any) -> Any:
        """getUVs(uvSet=None) -> [MFloatArray, MFloatArray, MIntArray]

        Get the UV values for all mapped faces at the current vertex.
        If at least one face was mapped the method will succeed.

        * uvSet (string) - Name of the uv set to work with
        """

    def hasColor(self, *args: Any, **kwargs: Any) -> Any:
        """hasColor() -> bool
        hasColor(index) -> bool

        This method determines whether the current Vertex has a color set
        for one or more faces.

        * index (int) - Index of face to check
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns the index of the current vertex in the vertex list for this
        polygonal object.
        Polygonal objects contain a list of vertices. Faces and edges are
        specified as indicies from this list, in this way vertices can
        be shared amoung faces and edges.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Indicates if all of the vertices have been traversed yet.
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next edge in the iteration.
        """

    def numConnectedEdges(self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedEdges() -> int

        This Method checks for the number of connected Edges on this vertex
        """

    def numConnectedFaces(self, *args: Any, **kwargs: Any) -> Any:
        """numConnectedFaces() -> int

        This Method checks for the number of Connected Faces
        """

    def numUVs(self, *args: Any, **kwargs: Any) -> Any:
        """numUVs(uvSet=None) -> int

        This method returns the number of unique UVs mapped on this vertex

        * uvSet (string) - Name of the uv set to work with
        """

    def onBoundary(self, *args: Any, **kwargs: Any) -> Any:
        """onBoundary() -> bool

        This method determines whether the current vertex is on a Boundary
        """

    def position(self, *args: Any, **kwargs: Any) -> Any:
        """position(space=kObject) -> MPoint

        Return the position of the current vertex in the specified space.
        Object space ignores all transformations for the polygon, world space
        includes all such transformations.

        * space (int) - The  transformation space
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def setIndex(self, *args: Any, **kwargs: Any) -> Any:
        """setIndex(index) -> int

        This method sets the index of the current vertex to be accessed.
        The current vertex will no longer be in sync with any previous iteration.

        * index (int) - The index of desired vertex to access.
        """

    def setPosition(self, *args: Any, **kwargs: Any) -> Any:
        """setPosition(point, space=kObject) -> self

        Set the position of the current vertex in the given space.

        * point (MPoint) - The new position for the current vertex
        * space (int) - The Transformation space
        """

    def setUV(self, *args: Any, **kwargs: Any) -> Any:
        """setUV(uvPoint, uvSet=None) -> selfsetUV(faceId, uvPoint, uvSet=None) -> self

        Set the shared UV value at this vertex

        * uvPoint ([float, float]) - The UV values to set
        * uvSet (string) - Name of the UV set to work with

        Set the UV value for the given face at the current vertex

        * faceId (int) - Index of required face
        * uvPoint ([float, float]) - The UV values to set
        * uvSet (string) - Name of the UV set to work with
        """

    def setUVs(self, *args: Any, **kwargs: Any) -> Any:
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

    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """translateBy(vector, space=kObject) -> self

        Translate the current vertex by the amount specified
        by the given vector.

        * vector (MVector) - The amount of translation
        * space (int) - The Transformation space
        """

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        Signal that this polygonal surface has changed and needs to redraw itself.
        """


class MItSelectionList(object):
    """Class for iterating over the items in an MSelection list."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def getComponent(self, *args: Any, **kwargs: Any) -> Any:
        """getComponent() -> (MDagPath, MObject)

        This method retrieves the dag path and the component of the current selection item.
        """

    def getDagPath(self, *args: Any, **kwargs: Any) -> Any:
        """getDagPath() -> MDagPath

        This method retrieves the dag path of the current selection item.
        """

    def getDependNode(self, *args: Any, **kwargs: Any) -> Any:
        """getDependNode() -> MObject

        This method retrieves the dependency node of the current selection itemRaises kFailure if there is no dependency node associated with the current item
        """

    def getPlug(self, *args: Any, **kwargs: Any) -> Any:
        """getPlug() -> MPlug

        This method retrieves the plug of the current selection item.
        """

    def getStrings(self, *args: Any, **kwargs: Any) -> Any:
        """getStrings() -> list of strings

        Get the string representation of the current item in the selection list.
        It is possible that it will require more than one string to represent the item (the item may contain groups of CVs for example)
        """

    def hasComponents(self, *args: Any, **kwargs: Any) -> Any:
        """hasComponents() -> bool

        Returns whether or not the current selection item has components.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Specifies whether or not there is anything more to iterator over.
        """

    def itemType(self, *args: Any, **kwargs: Any) -> Any:
        """itemType() -> int

        Returns the current selection item type.

          kDagSelectionItem    selection item is in the DAG
          kAnimSelectionItem   selection item is a keyset
          kDNselectionItem     selection item is a dependency node
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    kAnimSelectionItem: int = 1
    kDNselectionItem: int = 2
    kDagSelectionItem: int = 0
    kPlugSelectionItem: int = 3
    kUnknownItem: int = -1
    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next item. If components are selected then advance to next component.

        If a filter is specified then the next item will be one that matches the filter.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Reset the iterator.
        If a filter has been specified then the current item will be the first selected item that matches the filter.
        """

    def setFilter(self, *args: Any, **kwargs: Any) -> Any:
        """setFilter(filter) -> self

        Apply a filter to the iteration.
        Selection items not matching the filter type will be excluded from the iteration.
        """


class MItSurfaceCV(object):
    """NURBS surface CV iterator."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def currentItem(self, *args: Any, **kwargs: Any) -> Any:
        """currentItem() -> MObject

        Get the current CV in the iteration as a component.

        Components are used to specify one or more CVs and are useful in operating on groups of non-contiguous CVs for a curve or surface.
        Components do not contain any information about the surface that they refer to so an MDagPath must be specified when dealing with components.
        """

    def hasHistoryOnCreate(self, *args: Any, **kwargs: Any) -> Any:
        """hasHistoryOnCreate() -> bool

        This method determines if the shape was created with history.

        If the object that this iterator is attached to is not a shape then this method will raise.
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Get the index of the current CV as it appears in CV array for this surface.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Returns True if the iteration is finished, i.e. there are no more CVs to iterate on.
        """

    def isRowDone(self, *args: Any, **kwargs: Any) -> Any:
        """isRowDone() -> bool

        Returns True if the current row has no more CVs to iterate over.
        The row can be in the U or V direction depending on what value of useURows has been set in the constructor.
        """

    def iter(self, *args: Any, **kwargs: Any) -> Any:
        """iter() -> self

        Initializes the iterator object for pythonic iteration.
        """

    def iternext(self, *args: Any, **kwargs: Any) -> Any:
        """iternext() -> self

        Used in pythonic iteration to move the iterator
        """

    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advance to the next CV in the iteration.
        If the iterator is already at the last CV then this method has no effect. Use isDone() to determine if the iterator is at the last CV.
        """

    def nextRow(self, *args: Any, **kwargs: Any) -> Any:
        """nextRow() -> self

        Advance to the next row in the iteration.
        The row can be in the U or V direction depending on what value of useURows has been set in the constructor.
        """

    def position(self, *args: Any, **kwargs: Any) -> Any:
        """position(space=kObject) -> MPoint

        Returns the position of the current CV in the iteration in the specified space.

        * space (int) - The coordinate space in which the CV is set
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
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

    def setPosition(self, *args: Any, **kwargs: Any) -> Any:
        """setPosition(point, space=kObject) -> self

        Set the position of the current CV in the iteration to the specified point.

        * point (MPoint) - The new position for the current CV in the iteration
        * space (int) - The coordinate space in which the CV is set
        """

    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """translateBy(vector, space=kObject) -> self

        Move the current CV in the iteration by the sepcified vector.

        * vector (MVector) - The translation vector
        * space (int) - The coordinate space in which the CV is set
        """

    def updateSurface(self, *args: Any, **kwargs: Any) -> Any:
        """updateSurface() -> self

        This method is used to signal the surface that it has been changed and needs to redraw itself.

        When modifying a large number of CVs, it is most efficient to call this method after all of the CVs have been modified.
        """

    def uvIndices(self, *args: Any, **kwargs: Any) -> Any:
        """uvIndices() -> (indexU, indexV)

        Get the u and v index of the current CV.
        """


class MIteratorType(object):
    """The MIteratorType class is used on iterators where more than one type
    of filters can be specified. It also provides functionalities to set and
    get the filter list or individual types of filter. This class should be
    used in conjunction with DAG/DG/DependencyNodes iterators for using filter
    list (list of MFn::Type objects) on them, thus enabling faster traversal
    thro' iterators.

    Also, the class has functionalities for specifying the type of object the
    iterator will be reset to. This could be an MObject, an MPlug or an MDagPath.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    filterList: getset_descriptor = <attribute 'filterList' of 'OpenMaya.MIteratorType' objects>
    filterListEnabled: getset_descriptor = <attribute 'filterListEnabled' of 'OpenMaya.MIteratorType' objects>
    filterType: getset_descriptor = <attribute 'filterType' of 'OpenMaya.MIteratorType' objects>
    kMDagPathObject: int = 1
    kMObject: int = 0
    kMPlugObject: int = 2
    objectType: getset_descriptor = <attribute 'objectType' of 'OpenMaya.MIteratorType' objects>

class MLockMessage(MMessage):
    """Class used to register callbacks for model related messages."""
    kAddAttr: int = 5
    kChildReorder: int = 4
    kCreateChildInstance: int = 6
    kCreateNodeInstance: int = 5
    kCreateParentInstance: int = 7
    kLast: int = 10
    kLastDAG: int = 8
    kLastPlug: int = 8
    kLockAttr: int = 9
    kLockNode: int = 3
    kPlugAttrValChange: int = 3
    kPlugConnect: int = 6
    kPlugDisconnect: int = 7
    kPlugRemoveAttr: int = 4
    kPlugRenameAttr: int = 5
    kRemoveAttr: int = 6
    kRenameAttr: int = 7
    kReparent: int = 3
    kUnlockAttr: int = 8
    kUnlockNode: int = 4
    def setNodeLockDAGQueryCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def setNodeLockQueryCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def setPlugLockQueryCallback(self, *args: Any, **kwargs: Any) -> Any:
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


class MMatrix(object):
    """4x4 matrix with double-precision elements."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def adjoint(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's adjoint."""

    def det3x3(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the determinant of the 3x3 matrix formed by the first 3 elements of the first 3 rows of this matrix."""

    def det4x4(self, *args: Any, **kwargs: Any) -> Any:
        """Returns this matrix's determinant."""

    def getElement(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix element for the specified row and column."""

    def homogenize(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing the homogenized version of this matrix."""

    def inverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's inverse."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two matrices, within a tolerance."""

    def isSingular(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this matrix is singular."""

    kIdentity: MMatrix = (((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))
    kTolerance: float = 1e-10
    def setElement(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the matrix element for the specified row and column."""

    def setToIdentity(self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the identity."""

    def setToProduct(self, *args: Any, **kwargs: Any) -> Any:
        """Sets this matrix to the product of the two matrices passed in."""

    def transpose(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new matrix containing this matrix's transpose."""


class MMatrixArray(object):
    """Array of MMatrix values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MMatrixArray' objects>

class MMeshIntersector(object):
    """Provides methods for efficiently finding the closest point on
    the surface of a mesh. An octree algorithm is used to find the
    closest point.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """create(mesh, matrix) -> self

        Creates the internal data required by the intersector. It is a
        compute-heavy operation and should only be called when necessary.

        mesh (MObject)   - the mesh to be used
        matrix (MMatrix) - transformation to use to bring points into the
        mesh's object space.faceIds (list) - the faces of the mesh to be passed to the intersector
        """

    def getClosestPoint(self, *args: Any, **kwargs: Any) -> Any:
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

    isCreated: getset_descriptor = <attribute 'isCreated' of 'OpenMaya.MMeshIntersector' objects>

class MMeshIsectAccelParams(object):
    """Opaque class used to store parameters used by MFnMesh's
    intersection calculations for later re-use. Use MFnMesh's 
    uniformGridParams() or autoUniformGridParams() to create one
    of these to pass into the allIntersections(), 
    closestIntersection(), and anyIntersection() methods
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""


class MMeshSmoothOptions(object):
    """Options for control of smooth mesh generation."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    boundaryRule: getset_descriptor = <attribute 'boundaryRule' of 'OpenMaya.MMeshSmoothOptions' objects>
    divisions: getset_descriptor = <attribute 'divisions' of 'OpenMaya.MMeshSmoothOptions' objects>
    kCatmullClark: int = 0
    kCreaseAll: int = 1
    kCreaseEdge: int = 2
    kInvalid: int = -1
    kInvalidSubdivision: int = -1
    kLast: int = 3
    kLastSubdivision: int = 4
    kLegacy: int = 0
    kOpenSubdivCatmullClarkAdaptive: int = 3
    kOpenSubdivCatmullClarkUniform: int = 2
    keepBorderEdge: getset_descriptor = <attribute 'keepBorderEdge' of 'OpenMaya.MMeshSmoothOptions' objects>
    keepHardEdge: getset_descriptor = <attribute 'keepHardEdge' of 'OpenMaya.MMeshSmoothOptions' objects>
    propEdgeHardness: getset_descriptor = <attribute 'propEdgeHardness' of 'OpenMaya.MMeshSmoothOptions' objects>
    smoothUVs: getset_descriptor = <attribute 'smoothUVs' of 'OpenMaya.MMeshSmoothOptions' objects>
    smoothness: getset_descriptor = <attribute 'smoothness' of 'OpenMaya.MMeshSmoothOptions' objects>
    subdivisionType: getset_descriptor = <attribute 'subdivisionType' of 'OpenMaya.MMeshSmoothOptions' objects>

class MMessage(object):
    """Base class for message callbacks."""
    def currentCallbackId(self, *args: Any, **kwargs: Any) -> Any:
        """currentCallbackId() -> id

        Returns the callback ID of the currently executing callback. If called
        outside of a callback, an invalid MCallbackId and failed status will
        be returned.
        """

    kDefaultAction: int = 0
    kDoAction: int = 2
    kDoNotDoAction: int = 1
    def nodeCallbacks(self, *args: Any, **kwargs: Any) -> Any:
        """nodeCallbacks(node) -> ids

        Returns a list of callback IDs registered to a given node.

         * node (MObject) - Node to query for callbacks.
         * ids (MCallbackIdArray) - Array to store the list of callback IDs.
        """

    def removeCallback(self, *args: Any, **kwargs: Any) -> Any:
        """removeCallback(id) -> None

        Removes the specified callback from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.

         * id (MCallbackId) - identifier of callback to be removed
        """

    def removeCallbacks(self, *args: Any, **kwargs: Any) -> Any:
        """removeCallbacks(ids) -> None

        Removes all of the specified callbacks from Maya.
        This method must be called for all callbacks registered by a
        plug-in before that plug-in is unloaded.

         * idList (MCallbackIdArray) - list of callbacks to be removed.
        """


class MModelMessage(MMessage):
    """Class used to register callbacks for model related messages.The class also provides the following Message constants which
    describe the different types supported by the addCallback method:
      kActiveListModified           #active selection changes
    """
    def addAfterDuplicateCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addAfterDuplicateCallback(function, clientData=None) -> id

        This method registers a callback that is called after a duplicate
        command is made. The callback will be called after everything is
        duplicated.

         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addBeforeDuplicateCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addBeforeDuplicateCallback(function, clientData=None) -> id

        This method registers a callback that is called whenever a duplicate
        command is made. The callback will be called before anything is
        duplicated.

         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addCallback(message, function, clientData=None) -> id

        Adds a new callback for the specified model message.


         * message (Message constant, see class doc for a list) - the model
           message that will trigger the callback
         * function - callable which will be passed the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addNodeAddedToModelCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addNodeAddedToModelCallback(dagNode, function, clientData=None) -> id

        This method registers a callback that is called when a dag node is about
        to be added to the Maya model.

         * dagNode (MObject) - Node that should acquire the callback
         * function - callable which will be passed a MObject indicating
           the node being added to the model and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addNodeRemovedFromModelCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addNodeRemovedFromModelCallback(dagNode, function, clientData=None) -> id

        This method registers a callback that is called when the
        specified dag node is being removed from the Maya model.

         * dagNode (MObject) - Node that should acquire the callback
         * function - callable which will be passed a MObject indicating
           the node being removed to the model and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class MNamespace(object):
    """Access Maya namespace functionality."""
    def addNamespace(self, *args: Any, **kwargs: Any) -> Any:
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

    def currentNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """currentNamespace() -> MString

        Get the name of the current namespace. This name is returned 
        as an absolute namepath (i.e. fully qualfied from the root 
        namespace downwards, ':a:b:c').
        """

    def getNamespaceFromName(self, *args: Any, **kwargs: Any) -> Any:
        """getNamespaceFromName(MString fullName) -> MString

        Get namespace from a full name. 
        For example, given a full name: 'a:b:c:d:ball' this method 
        would return: 'a:b:c:d'. 
        """

    def getNamespaceObjects(self, *args: Any, **kwargs: Any) -> Any:
        """getNamespaceObjects(MString parentNamespace, bool recurse=False) -> MObjectArray

        Return an array of MObjects representing the object contained within 
        the specified namespace. To query the current namespace, call this 
        method in this way: 
        """

    def getNamespaces(self, *args: Any, **kwargs: Any) -> Any:
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

    def makeNamepathAbsolute(self, *args: Any, **kwargs: Any) -> Any:
        """makeNamepathAbsolute(MString fullName) -> MString

        Make a namepath which is relative to the root into an absolute 
        namepath. For example, given the namepath 'a:sphere' this method 
        returns ':a:sphere'. It also culls out duplicate and trailing 
        separators, e.g. 'a:b::c:' will return ':a:b:c'. 
        """

    def moveNamespace(self, *args: Any, **kwargs: Any) -> Any:
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

    def namespaceExists(self, *args: Any, **kwargs: Any) -> Any:
        """namespaceExists(MString name) -> bool

        Check if a given namespace exists.
        """

    def parentNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """parentNamespace() -> MString

        Get the name of the current namespace's parent. This name is returned 
        as an absolute namepath (i.e. fully qualfied from the root namespace 
        downwards, ':a:b'). If the root namespace is 
        current, this method returns an error. 
        """

    def relativeNames(self, *args: Any, **kwargs: Any) -> Any:
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

    def removeNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """removeNamespace(MString name, bool removeContents=False)

        Remove the specified namespace. 
        Note that removing a namespace changes the scene, so any code 
        that calls this method needs to handle undo. 
        """

    def renameNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """renameNamespace(MString oldName, MString newName, MString parent=None)

        Rename the specified namespace to a new name with optional parent name. 
        Note that removing a namespace changes the scene, so any code 
        that calls this method needs to handle undo. 
        """

    def rootNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """rootNamespace() -> MString

        Get the name of the root namespace. This name is an absolute
        namepath (i.e. prefixed by a ':'). 
        """

    def setCurrentNamespace(self, *args: Any, **kwargs: Any) -> Any:
        """setCurrentNamespace(MString name) -> MString

        Set the specified namespace to be the current namespace. The 'name' 
        parameter you specify is relative to whatever namespace is current, 
        but any namespace can be specified by passing an absolute name (e.g. :a:b:c).  
        Note that making a namespace current changes the scene, so any code 
        that calls this method needs to handle undo. 

        To make the root namespace become current, use:
            MNamespace.setCurrentNamespace(MNamespace.rootNamespace())
        """

    def setRelativeNames(self, *args: Any, **kwargs: Any) -> Any:
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

    def stripNamespaceFromName(self, *args: Any, **kwargs: Any) -> Any:
        """stripNamespaceFromName(MString fullName) -> MString

        Strips the namespace from a full name. 
        For example, given a full name: 'a:b:c:d:ball' this method  
        would return: 'ball'. 
        """

    def validateName(self, *args: Any, **kwargs: Any) -> Any:
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


class MNodeCacheDisablingInfo(object):
    """Defines additional info about why the node disables Cached Playback."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def getCacheDisabled(self, *args: Any, **kwargs: Any) -> Any:
        """getCacheDisabled() -> bool

        Return True if the cache should be disabled because of this node.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset()

        Resets the disabling info to an enabled state.
        """

    def setCacheDisabled(self, *args: Any, **kwargs: Any) -> Any:
        """setCacheDisabled(bool)

        Set if the cache should be disabled because of this node.
        """

    def setMitigation(self, *args: Any, **kwargs: Any) -> Any:
        """setMitigation(mitigation)

        Sets the mitigation to fix the reason for disabling Cached Playback.
        """

    def setReason(self, *args: Any, **kwargs: Any) -> Any:
        """setReason(reason)

        Sets the reason for disabling Cached Playback.
        """


class MNodeCacheSetupInfo(object):
    """Defines preferences and requirements the node has for Cached Playback."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def getPreference(self, *args: Any, **kwargs: Any) -> Any:
        """getPreference(PreferenceFlag) -> bool

        Get a preference flag for this node.
        """

    def getRequirement(self, *args: Any, **kwargs: Any) -> Any:
        """getRequirement(RequirementFlag) -> bool

        Get a requirement flag for this node.
        """

    kLastPreference: int = 1
    kLastRequirement: int = 1
    kSimulationSupport: int = 0
    kWantToCacheByDefault: int = 0
    def setPreference(self, *args: Any, **kwargs: Any) -> Any:
        """setPreference(PreferenceFlag, bool)

        Set a preference flag for this node.
        """

    def setRequirement(self, *args: Any, **kwargs: Any) -> Any:
        """setRequirement(RequirementFlag, bool)

        Set a requirement flag for this node.
        """


class MNodeClass(object):
    """A class for performing node class-level operations in the dependency graph."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def addExtensionAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Adds an extension attribute to the node class. An extension attribute is a class-level attribute which has been added dynamically to a node class. Because it is added at the class level, all nodes of that class will have the given attribute, and will only store the attribute's value if it differs from the default. Returns the type of the object at the end of the path."""

    def attribute(self, *args: Any, **kwargs: Any) -> Any:
        """If passed an int: Returns the node class's i'th attribute. Raises IndexError if index is out of bounds.  If passed a string, Returns the node class's attribute having the given name. Returns MObject.kNullObj if the class does not have an attribute with that name."""

    attributeCount: getset_descriptor = <attribute 'attributeCount' of 'OpenMaya.MNodeClass' objects>
    classification: getset_descriptor = <attribute 'classification' of 'OpenMaya.MNodeClass' objects>
    def getAttributes(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an MObjectArray array containing all of the node class's attributes."""

    def hasAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the node class has an attribute of the given name, False otherwise."""

    pluginName: getset_descriptor = <attribute 'pluginName' of 'OpenMaya.MNodeClass' objects>
    def removeExtensionAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Removes an extension attribute from the node class. Raises ValueError if attr is not an extension attribute of this node class."""

    def removeExtensionAttributeIfUnset(self, *args: Any, **kwargs: Any) -> Any:
        """Removes an extension attribute from the node class, but only if there are no nodes in the graph with non-default values for this attribute. Returns True if the attribute was removed, False otherwise. Raises ValueError if attr is not an extension attribute of this node class."""

    typeId: getset_descriptor = <attribute 'typeId' of 'OpenMaya.MNodeClass' objects>
    typeName: getset_descriptor = <attribute 'typeName' of 'OpenMaya.MNodeClass' objects>

class MNodeMessage(MMessage):
    """Class used to register callbacks for dependency node messages of specific dependency nodes.

    The class also provides the following AttributeMessage constants which describe
    the type of attribute changed/addedOrRemoved messages that has occurred:
      kConnectionMade               #a connection has been made to an attribute of this node
      kConnectionBroken     #a connection has been broken for an attribute of this node
      kAttributeEval                #an attribute of this node has been evaluated
      kAttributeSet         #an attribute value of this node has been set
      kAttributeLocked              #an attribute of this node has been locked
      kAttributeUnlocked    #an attribute of this node has been unlocked
      kAttributeAdded               #an attribute has been added to this node
      kAttributeRemoved     #an attribute has been removed from this node
      kAttributeRenamed     #an attribute of this node has been renamed
      kAttributeKeyable     #an attribute of this node has been marked keyable
      kAttributeUnkeyable   #an attribute of this node has been marked unkeyable
      kIncomingDirection    #the connection was coming into the node
      kAttributeArrayAdded  #an array attribute has been added to this node
      kAttributeArrayRemoved        #an array attribute has been removed from this node
      kOtherPlugSet         #the otherPlug data has been set


    The class also provides the following KeyableChangeMsg constants which
    allows user to prevent attributes from becoming (un)keyable:
      kKeyChangeInvalid
      kMakeKeyable
      kMakeUnkeyable
      kKeyChangeLast
    """
    def addAttributeAddedOrRemovedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addAttributeChangedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addKeyableChangeOverride(self, *args: Any, **kwargs: Any) -> Any:
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

    def addNameChangedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addNodeAboutToDeleteCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addNodeDestroyedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addNodeDestroyedCallback(node, function, clientData=None) -> id

        Registers a callback which will get called when a node's destructor is
        called.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed the clientData object
         * clientData - User defined data that will be passed to the callback
           function

         * return: Identifier used for removing the callback.
        """

    def addNodeDirtyCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addNodeDirtyCallback(node, function, clientData=None) -> id

        Registers a callback for node dirty messages.

         * node (MObject) - the node to register the callback for
         * function - callable which will be passed a MObject indicating the node
           that has  become dirty and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """

    def addNodeDirtyPlugCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addNodePreRemovalCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addUuidChangedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    kAttributeAdded: int = 64
    kAttributeArrayAdded: int = 4096
    kAttributeArrayRemoved: int = 8192
    kAttributeEval: int = 4
    kAttributeKeyable: int = 512
    kAttributeLocked: int = 16
    kAttributeRemoved: int = 128
    kAttributeRenamed: int = 256
    kAttributeSet: int = 8
    kAttributeUnkeyable: int = 1024
    kAttributeUnlocked: int = 32
    kIncomingDirection: int = 2048
    kKeyChangeLast: int = 3
    kLast: int = 32768
    kOtherPlugSet: int = 16384

class MObject(object):
    """Opaque wrapper for internal Maya objects."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def apiType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the function set type for the object."""

    apiTypeStr: getset_descriptor = <attribute 'apiTypeStr' of 'OpenMaya.MObject' objects>
    def hasFn(self, *args: Any, **kwargs: Any) -> Any:
        """Tests whether object is compatible with the specified function set."""

    def isNull(self, *args: Any, **kwargs: Any) -> Any:
        """Tests whether there is an internal Maya object."""

    kNullObj: MObject = <OpenMaya.MObject object at 0x00000218AAE21310>

class MObjectArray(object):
    """Array of MObject values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MObjectArray' objects>

class MObjectHandle(object):
    """Generic Class for validating MObjects."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def assign(self, *args: Any, **kwargs: Any) -> Any:
        """assign(source) -> self

        Assigns this MObjectHandle to an instance of another MObjectHandle, or to a MObject instance.

        * source (MObject/MObjectHandle) - other instance to assign from.
        """

    def hashCode(self, *args: Any, **kwargs: Any) -> Any:
        """hashCode() -> int

        Returns a hash code for the internal Maya object referenced by the MObject within this MObjectHandle. If the MObject is null or no longer alive then 0 will be returned, otherwise the hash code is guaranteed to be non-zero
        """

    def isAlive(self, *args: Any, **kwargs: Any) -> Any:
        """isAlive() -> bool

        Returns the live state of the associated MObject. An object can still be 'alive' but not 'valid' (eg. a deleted object that resides in the undo queue).
        """

    def isValid(self, *args: Any, **kwargs: Any) -> Any:
        """isValid() -> bool

        Returns the validity of the associated MObject.
        """

    def object(self, *args: Any, **kwargs: Any) -> Any:
        """object() -> MObject

        Returns the MObject associated with this handle. The returned MObject will be MObject.kNullObj if the object is invalid.
        """


class MObjectSetMessage(MMessage):
    """Class used to register callbacks for set modified related messages."""
    def addSetMembersModifiedCallback(self, *args: Any, **kwargs: Any) -> Any:
        """addSetMembersModifiedCallback(node, function, clientData=None) -> id

        Registers callbacks for set modified messages.

         * node (MObject) - the set that has triggered a setModified event
         * function (MMessage::MNodeFunction) - the callback function
         * function - callable which will be passed a MObject indicating the
           set that has triggered a setModified event and the clientData object
         * clientData - User defined data passed to the callback function

         * return: Identifier used for removing the callback.
        """


class MPlane(object):
    """This class describes a mathematical plane."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def distance(self, *args: Any, **kwargs: Any) -> Any:
        """distance() -> float

        Returns the distance of the plane along the normal.
        """

    def distanceToPoint(self, *args: Any, **kwargs: Any) -> Any:
        """distanceToPoint(point, signed=False) -> float

        Returns the distance from the plane to the specified point.

        * point (MVector) - The point from which to calculate the distance
        * signed (bool) - Whether to return a signed or unsigned distance
        """

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """normal() -> MVector

        Returns the normal of the plane.
        """

    def setPlane(self, *args: Any, **kwargs: Any) -> Any:
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


class MPlug(object):
    """Create and access dependency node plugs."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def array(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the array of plugs of which this plug is an element."""

    def asBool(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a boolean."""

    def asChar(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a single-byte integer."""

    def asDouble(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a double-precision float."""

    def asFloat(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a single-precision float."""

    def asInt(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a regular integer."""

    def asMAngle(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as an MAngle."""

    def asMDataHandle(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieve the current value of the attribute this plug references."""

    def asMDistance(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as an MDistance."""

    def asMObject(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as as an MObject containing a direct reference to the plug's data."""

    def asMTime(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as an MTime."""

    def asShort(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a short integer."""

    def asString(self, *args: Any, **kwargs: Any) -> Any:
        """Retrieves the plug's value, as a string."""

    def attribute(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the attribute currently referenced by this plug."""

    def child(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the specified child attribute of this plug."""

    def connectedTo(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an array of plugs which are connected to this one."""

    def connectionByPhysicalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the index'th connected element of this plug."""

    def constructHandle(self, *args: Any, **kwargs: Any) -> Any:
        """Constructs a data handle for the plug."""

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """Copies one plug to another."""

    def destinations(self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a source, return the destination plugs connected to it.
        If this plug is not a source, a null plug is returned.
        This method will produce the networked version of the connected plug.
        """

    def destinationsWithConversions(self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a source, return the destination plugs connected to it.
        This method is very similar to the destinations() method.  The only difference is that the destinations() method skips over any unit conversion node connected to this source, and returns the destination of the unit conversion node.
        destinationsWithConversionNode() does not skip over unit conversion nodes, and returns the destination plug on a unit conversion node, if present.
        Note that the behavior of connectedTo() is identical to destinationsWithConversions(), that is, do not skip over unit conversion nodes.
        """

    def destructHandle(self, *args: Any, **kwargs: Any) -> Any:
        """Destroys a data handle previously constructed using constructHandle()."""

    def elementByLogicalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the element of this plug array having the specified logical index."""

    def elementByPhysicalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the element of this plug array having the specified physical index. """

    def evaluateNumElements(self, *args: Any, **kwargs: Any) -> Any:
        """Like numElements() but evaluates all connected elements first to ensure that they are included in the count."""

    def getExistingArrayAttributeIndices(self, *args: Any, **kwargs: Any) -> Any:
        """Returns an array of all the plug's logical indices which are currently in use."""

    def getSetAttrCmds(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list of strings containing the setAttr commands (in MEL syntax) for this plug and all of its descendents."""

    info: getset_descriptor = <attribute 'info' of 'OpenMaya.MPlug' objects>
    isArray: getset_descriptor = <attribute 'isArray' of 'OpenMaya.MPlug' objects>
    isCaching: getset_descriptor = <attribute 'isCaching' of 'OpenMaya.MPlug' objects>
    isChannelBox: getset_descriptor = <attribute 'isChannelBox' of 'OpenMaya.MPlug' objects>
    isChild: getset_descriptor = <attribute 'isChild' of 'OpenMaya.MPlug' objects>
    isCompound: getset_descriptor = <attribute 'isCompound' of 'OpenMaya.MPlug' objects>
    isConnected: getset_descriptor = <attribute 'isConnected' of 'OpenMaya.MPlug' objects>
    def isDefaultValue(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a value indicating if the plug's value is equivalent to the plug's default value."""

    isDestination: getset_descriptor = <attribute 'isDestination' of 'OpenMaya.MPlug' objects>
    isDynamic: getset_descriptor = <attribute 'isDynamic' of 'OpenMaya.MPlug' objects>
    isElement: getset_descriptor = <attribute 'isElement' of 'OpenMaya.MPlug' objects>
    def isFreeToChange(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a value indicating if the plug's value can be changed, after taking into account the effects of locking and connections."""

    isFromReferencedFile: getset_descriptor = <attribute 'isFromReferencedFile' of 'OpenMaya.MPlug' objects>
    isIgnoredWhenRendering: getset_descriptor = <attribute 'isIgnoredWhenRendering' of 'OpenMaya.MPlug' objects>
    isKeyable: getset_descriptor = <attribute 'isKeyable' of 'OpenMaya.MPlug' objects>
    isLocked: getset_descriptor = <attribute 'isLocked' of 'OpenMaya.MPlug' objects>
    isNetworked: getset_descriptor = <attribute 'isNetworked' of 'OpenMaya.MPlug' objects>
    isNull: getset_descriptor = <attribute 'isNull' of 'OpenMaya.MPlug' objects>
    isProcedural: getset_descriptor = <attribute 'isProcedural' of 'OpenMaya.MPlug' objects>
    isProxy: getset_descriptor = <attribute 'isProxy' of 'OpenMaya.MPlug' objects>
    isSource: getset_descriptor = <attribute 'isSource' of 'OpenMaya.MPlug' objects>
    kAll: int = 0
    kChanged: int = 2
    kChildrenNotFreeToChange: int = 2
    kFreeToChange: int = 0
    kLastAttrSelector: int = 3
    kNonDefault: int = 1
    kNotFreeToChange: int = 1
    def logicalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Returns this plug's logical index within its parent array."""

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the name of the plug."""

    def node(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the node that this plug belongs to."""

    def numChildren(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of children this plug has."""

    def numConnectedChildren(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of this plug's children which have connections."""

    def numConnectedElements(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of this plug's elements which have connections."""

    def numElements(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of the plug's logical indices which are currently in use. Connected elements which have not yet been evaluated may not yet fully exist and may be excluded from the count."""

    def parent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a plug for the parent of this plug."""

    def partialName(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the name of the plug, formatted according to various criteria."""

    def proxied(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the proxied plug for this plug."""

    def selectAncestorLogicalIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Changes the logical index of the specified attribute in the plug's path."""

    def setAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """Switches the plug to reference the given attribute of the same node as the previously referenced attribute."""

    def setBool(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a boolean."""

    def setChar(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a single-byte integer."""

    def setDouble(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a double-precision float."""

    def setFloat(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a single-precision float."""

    def setInt(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a regular integer."""

    def setMAngle(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MAngle."""

    def setMDataHandle(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a data handle."""

    def setMDistance(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MDistance."""

    def setMObject(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MObject."""

    def setMPxData(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value using custom plug-in data."""

    def setMTime(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as an MTime."""

    def setNumElements(self, *args: Any, **kwargs: Any) -> Any:
        """Pre-allocates space for count elements in an array of plugs."""

    def setShort(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a short integer."""

    def setString(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the plug's value as a string."""

    def source(self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a destination, return the source plug connected to it.
        If this plug is not a destination, a null plug is returned.
        This method will produce the networked version of the connectedplug.
        """

    def sourceWithConversion(self, *args: Any, **kwargs: Any) -> Any:
        """If this plug is a destination, return the source plug connected to it.
        This method is very similar to the source() method.  The only difference is that the source() method skips over any unit conversionnode connected to this destination, and returns the source of the unit conversion node.
        sourceWithConversion() does not skip over unitconversion nodes, and returns the source plug on a unit conversionnode, if present.
        Note that the behavior of connectedTo() is identical to sourceWithConversion(), that is, do not skip over unit conversion nodes.
        """


class MPlugArray(object):
    """Array of MPlug values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MPlugArray' objects>

class MPoint(object):
    """3D point with double-precision coordinates."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __rtruediv__(self, value) -> Any:
        """Return value/self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def __truediv__(self, value) -> Any:
        """Return self/value."""

    def cartesianize(self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to cartesian form."""

    def distanceTo(self, *args: Any, **kwargs: Any) -> Any:
        """Return distance between this point and another."""

    def homogenize(self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to homogenous form."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Test for equivalence of two points, within a tolerance."""

    kOrigin: MPoint = (0, 0, 0, 1)
    kTolerance: float = 1e-10
    def rationalize(self, *args: Any, **kwargs: Any) -> Any:
        """Convert point to rational form."""

    w: getset_descriptor = <attribute 'w' of 'OpenMaya.MPoint' objects>
    x: getset_descriptor = <attribute 'x' of 'OpenMaya.MPoint' objects>
    y: getset_descriptor = <attribute 'y' of 'OpenMaya.MPoint' objects>
    z: getset_descriptor = <attribute 'z' of 'OpenMaya.MPoint' objects>

class MPointArray(object):
    """Array of MPoint values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MPointArray' objects>

class MPointOnMesh(object):
    """This class is used to return information about a point on the
    surface of a mesh: 3D position, normal, barycentric coordinates,
    etc. The point can be anywhere on the mesh, not just at its
    vertices.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    barycentricCoords: getset_descriptor = <attribute 'barycentricCoords' of 'OpenMaya.MPointOnMesh' objects>
    face: getset_descriptor = <attribute 'face' of 'OpenMaya.MPointOnMesh' objects>
    normal: getset_descriptor = <attribute 'normal' of 'OpenMaya.MPointOnMesh' objects>
    point: getset_descriptor = <attribute 'point' of 'OpenMaya.MPointOnMesh' objects>
    triangle: getset_descriptor = <attribute 'triangle' of 'OpenMaya.MPointOnMesh' objects>

class MPolyMessage(MMessage):
    """Class used to register callbacks for poly related messages."""
    def addPolyComponentIdChangedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addPolyTopologyChangedCallback(self, *args: Any, **kwargs: Any) -> Any:
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


class MPxAttributePatternFactory(object):
    """Base class for custom attribute pattern factories."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __str__(self) -> Any:
        """Return str(self)."""


class MPxCommand(object):
    """Base class for custom commands."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def appendToResult(self, *args: Any, **kwargs: Any) -> Any:
        """Append a value to the result to be returned by the command."""

    def clearResult(self, *args: Any, **kwargs: Any) -> Any:
        """Clears the command's result."""

    commandString: getset_descriptor = <attribute 'commandString' of 'OpenMaya.MPxCommand' objects>
    def currentResult(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the command's current result."""

    def currentResultType(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type of the current result."""

    def displayError(self, *args: Any, **kwargs: Any) -> Any:
        """Display an error message."""

    def displayInfo(self, *args: Any, **kwargs: Any) -> Any:
        """Display an informational message."""

    def displayWarning(self, *args: Any, **kwargs: Any) -> Any:
        """Display a warning message."""

    def doIt(self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to execute the command."""

    def hasSyntax(self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to determine if the command provides an MSyntax object describing its syntax."""

    historyOn: getset_descriptor = <attribute 'historyOn' of 'OpenMaya.MPxCommand' objects>
    def isCurrentResultArray(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if the command's current result is an array of values."""

    def isUndoable(self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to determine if the command supports undo."""

    kDouble: int = 1
    kLong: int = 0
    kNoArg: int = 3
    kString: int = 2
    def redoIt(self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to redo a previously undone command."""

    def setResult(self, *args: Any, **kwargs: Any) -> Any:
        """Set the value of the result to be returned by the command."""

    def syntax(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the command's MSyntax object, if it has one."""

    def undoIt(self, *args: Any, **kwargs: Any) -> Any:
        """Called by Maya to undo a previously executed command."""


class MPxData(object):
    """Base Class for User-defined Dependency Graph Data Types."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(src) -> self

        This method initializes an instance of an MPxData derived class from another existing instance.  This method can be thought of as the second half of a copy constructor for the class.  The default constructor has already been called for the instance, and this method is used to set the private data by copying the values from an existing instance.
        This method must be implemented by the derived class.

        * src (MPxData) - The object from which to copy the private data
        """

    kData: int = 0
    kGeometryData: int = 1
    kLast: int = 2
    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of the custom data type.
        This method must be implemented by the derived class.
        """

    def readASCII(self, *args: Any, **kwargs: Any) -> Any:
        """readASCII(argList, endOfTheLastParsedElement) -> int

        Creates Data in Data Block as specified by input from ASCII file record.
        Returns the new last argument parsed by this method.

        * argList (MArgList) - List of arguments read from ASCII record* endOfTheLastParsedElement (int) - points to last argument already parsed.
        """

    def readBinary(self, *args: Any, **kwargs: Any) -> Any:
        """readBinary(in, length) -> int

        Creates Data in Data Block as specified by binary data from the given stream.
        Returns the numbers of data bytes processed or -1 in case of error.

        * in (bytearray) - Input stream
        * length (int) - Length in bytes of binary data to be read.
        """

    def typeId(self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Determines the type id of the Data object.
        This method must be implemented by the derived class.
        """

    def writeASCII(self, *args: Any, **kwargs: Any) -> Any:
        """writeASCII() -> string

        Encodes Data in accordance with the ASCII file format and returns as string.
        """

    def writeBinary(self, *args: Any, **kwargs: Any) -> Any:
        """writeBinary() -> bytearray

        Encodes Data in accordance with the binary file format and returns as bytearray.
        """


class MPxGeometryData(MPxData):
    """Base Class for User-defined Dependency Graph Geometry Data Types."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def deleteComponent(self, *args: Any, **kwargs: Any) -> Any:
        """deleteComponent(compList) -> bool

        This method should be overridden if this data is to support component deletion. For user defined shapes (MPxSurfaceShape) which support components, this method must be overridden if component deletion is to be supported when the shape has history.

        Returns True if the deletion was successfull, False otherwise.

        * compList (MObjectArray) - a list of components that are to be deleted
        """

    def deleteComponentsFromGroups(self, *args: Any, **kwargs: Any) -> Any:
        """deleteComponentsFromGroups(compList, groupIdArray, groupComponentArray) -> bool

        This method should be overridden to modify the groups that flows along with the geometry, as part of the data, based on the components being deleted. It should intelligently update the groups based on what gets deleted. The class MFnGeometryData can be used to access and modify grouping information for data.

        Returns True if the deletion was successfull, False otherwise.

        The groupIdArray and groupComponentArray should contain the updated grouping information after the deletion has occurred.

        * compList (MObjectArray) - a list of components that are to be deleted
        * groupIdArray [OUT] (MIntArray) - array of group id's
        * groupComponentArray (MObjectArray) - array of updated components, one for each group id
        """

    def getMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """getMatrix(matrix) -> bool

        Gets the matrix associated to MPxGeometryData and retursn True if is identity

        * matrix [OUT] (MMatrix) - the returned matrix that takes a point from local object space to world space.
        """

    def iterator(self, *args: Any, **kwargs: Any) -> Any:
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

    matrix: getset_descriptor = <attribute 'matrix' of 'OpenMaya.MPxGeometryData' objects>
    def smartCopy(self, *args: Any, **kwargs: Any) -> Any:
        """smartCopy(srcGeom) -> self

        This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

        This method is used to prvoide maya with an efficient way to copy the source data into the memory of this data with as little memory allocation as possible.

        This method is not mandatory and only needs to be overridden to improve performance of deformations on shapes.

        * srcGeom (MPxGeometryData) - the data to be copied
        """

    def updateCompleteVertexGroup(self, *args: Any, **kwargs: Any) -> Any:
        """updateCompleteVertexGroup(component) -> bool

        This method is used in conjunction with MPxSurfaceShape classes which support maya's deformations.

        This method should make sure that complete vertex group data is up-to-date.
        If the given component is not complete (i.e. it represents all elements of your geometry) then you must mark is as complete using the methods of MFnComponent and return true if the component was updated, false if it was already complete.

        This method is used by deformers when deforming the "whole" object and not just selected components.

        Returns true if the component was updated, false if it was already complete.

        * component (MObject) - the component to test
        """


class MPxGeometryIterator(object):
    """Base class for user defined geometry iterators."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __iter__(self) -> Any:
        """Implement iter(self)."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __next__(self) -> Any:
        """Implement next(self)."""

    def component(self, *args: Any, **kwargs: Any) -> Any:
        """component() -> MObject

        Returns a component for the current item in the iteration.
        """

    currentPoint: getset_descriptor = <attribute 'currentPoint' of 'OpenMaya.MPxGeometryIterator' objects>
    def geometry(self, *args: Any, **kwargs: Any) -> Any:
        """geometry() -> long/object

        Returns the user geometry that this iterator is iterating over.
        """

    def hasNormals(self, *args: Any, **kwargs: Any) -> Any:
        """hasNormals() -> bool

        Returns whether the underlying geometry has normals.
        """

    def hasPoints(self, *args: Any, **kwargs: Any) -> Any:
        """hasPoints() -> bool

        Returns whether the underlying geometry has point data.
        """

    def index(self, *args: Any, **kwargs: Any) -> Any:
        """index() -> int

        Returns a unique index for the current item in the iteration.
        If the iteration is over the whole geometry then this index is the same as current point. If the iteration is over some elements of the geometry specified by a component then this index is the index in your geometry.
        """

    def indexUnsimplified(self, *args: Any, **kwargs: Any) -> Any:
        """indexUnsimplified() -> int

        Returns a unique index for the current item in the iteration.
        Rather than being the iterator index this is the index for the actual item when simplification is skipping items. This index will be equal to index() if no simplification, otherwise it will be larger.
        """

    def isDone(self, *args: Any, **kwargs: Any) -> Any:
        """isDone() -> bool

        Returns whether all the items have been traversed yet.
        """

    def iteratorCount(self, *args: Any, **kwargs: Any) -> Any:
        """iteratorCount() -> int

        Returns an estimate of how many items will be iterated over.
        """

    maxPoints: getset_descriptor = <attribute 'maxPoints' of 'OpenMaya.MPxGeometryIterator' objects>
    def next(self, *args: Any, **kwargs: Any) -> Any:
        """next() -> self

        Advances to the next component.
        """

    def point(self, *args: Any, **kwargs: Any) -> Any:
        """point() -> MPoint

        Returns the current component's positional data.
        """

    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """reset() -> self

        Resets the iterator to the start of the components so that another pass over them may be made.
        """

    def setObject(self, *args: Any, **kwargs: Any) -> Any:
        """setObject(shape) -> self

        Optional method to set a shape object to iterate over to allow tweaking of the shape's history (input geometry).

        * shape (MPxSurfaceShape) - a user defined shape object.
        """

    def setPoint(self, *args: Any, **kwargs: Any) -> Any:
        """setPoint(point) -> self

        Sets the current component's positional data.

        * point (MPoint) - the new positional value to set.
        """

    def setPointGetNext(self, *args: Any, **kwargs: Any) -> Any:
        """setPointGetNext(point) -> int

        Sets the current component's positional data, and returns the next index value.

        * point (MPoint) - the positional value to set.
        """


class MPxNode(object):
    """Base class for user defined dependency nodes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addAttribute(self, *args: Any, **kwargs: Any) -> Any:
        """addAttribute(attr) -> None

        This method adds a new attribute to a user defined node type during the type's initialization.

        This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into  MFnPlugin.registerNode(). The attributes must first be created using one of the MFnAttribute classes, and can then be added using this method.

        For compound attributes, the proper way to use this method is by calling it with the parent attribute. If a compound attribute is passed, this method will add all of its children.
        NOTE: A failure will occur if you attempt to call addAttribute() on the children of a compound attribute.

        * attr (MObject) - new attribute to add.
        """

    def addExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """addExternalContentForFileAttr(table, attr) -> bool

        This method is a helper for derived clases implementing getExternalContent().  It augments the external content info table passed in with an entry describing external content whose location is described by the specified attribute.

        The method will not overwrite existing items, i.e. items with the same key. (attribute name).  In this context, overwriting an item means the caller has called this function twice with the same attribute, or that two separate but identically named attributes were used.  If replacing an entry is the desired effect, it is the caller's responsibility to erase the previous item first.

        * table [OUT] (MExternalContentInfoTable) - table The table in which the new entry will be added.
        * attr (MObject) - The attribute for which the plug value will be queried for a location.

        Returns True if an item was sucessfully added to the table.  False if the attribute does not describe a non-empty location, or an item with the same key was already present in the table.
        """

    def attributeAffects(self, *args: Any, **kwargs: Any) -> Any:
        """attributeAffects(whenChanges, isAffected) -> None

        This method specifies that a particular input attribute affects a specific output attribute.  This is required to make evaluation efficient.  When an input changes, only the affected outputs will be computed. Output attributes cannot be keyable - if they are keyable, this method will fail.

        This method must be called for every attribute dependency when initializing the node's attributes.  The attributes must first be added using the MPxNode.addAttribute() method.  Failing to call this method will cause the node not to update when its inputs change. If there are no calls to this method in a node's initialization, then the compute method will never be called.

        This method will only work during the static initialization method of the user defined node class.  The initialization method is the one that is passed into MFnPlugin.registerNode().  As a result, it does not work with dynamic attributes. For an alternate solution which handles dynamic as well as non-dynamic attributes refer to MPxNode.setDependentsDirty.()

        * whenChanges (MObject) - input attribute - MObject that points to an input attribute that has already been added.
        * isAffected (MObject) - affected output attribute - MObject that points to an output attribute that has already been added.
        """

    def compute(self, *args: Any, **kwargs: Any) -> Any:
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

    def configCache(self, *args: Any, **kwargs: Any) -> Any:
        """configCache(evalNode, schema) -> None

        Defines the node's behavior when participating in Cached Playback.

        This method will be called at EM partitioning time, after rules evaluation.

        * evalNode (MEvaluationNode)  - This node's evaluation node, contains animated plug information
        * schema (MCacheSchema)       - Specification about what attributes to cache
        """

    def connectionBroken(self, *args: Any, **kwargs: Any) -> Any:
        """connectionBroken( plug, otherPlug, asSrc) -> self

        This method gets called when connections are broken with attributes of this node.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """

    def connectionMade(self, *args: Any, **kwargs: Any) -> Any:
        """connectionMade(plug, otherPlug, asSrc) -> self

        This method gets called when connections are made to attributes of this node.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """

    def copyInternalData(self, *args: Any, **kwargs: Any) -> Any:
        """copyInternalData(node) -> self

        This method is overriden by nodes that store attribute data in some internal format.

        On duplication this method is called on the duplicated node with the node being duplicated passed as the parameter.  Overriding this method gives your node a chance to duplicate any internal data you've been storing and manipulating outside of normal attribute data.

        * node (MPxNode) - the node that is being duplicated.
        """

    def dependsOn(self, *args: Any, **kwargs: Any) -> Any:
        """dependsOn( plug, otherPlug) -> bool/None

        This method may be overridden by the user defined node. It should only be required to override this on rare occasions.

        This method determines whether a specific attribute depends on another attribute.

        You should return None to specify that Maya should determines the dependency (default).

        This is mainly to define dependency of dynamic attributes, since attributeAffects does not work with dynamic attributes.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        """

    def doNotWrite(self, *args: Any, **kwargs: Any) -> Any:
        """doNotWrite() -> bool

        use this method to query the "do not write" state of this proxy node. True is returned if this node will not be saved when the maya model is written out. 
        """

    def existWithoutInConnections(self, *args: Any, **kwargs: Any) -> Any:
        """existWithoutInConnections() -> bool

        Determines whether or not this node can exist without input connections.

        If a node connected to this node is deleted resulting in no more input
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        Returns true if this node can exist without input connections, false otherwise
        """

    def existWithoutOutConnections(self, *args: Any, **kwargs: Any) -> Any:
        """existWithoutOutConnections() -> bool

        Determines whether or not this node can exist without output connections.

        If a node connected to this node is deleted resulting in no more output
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        Returns true if this node can exist without output connections, false otherwise
        """

    def forceCache(self, *args: Any, **kwargs: Any) -> Any:
        """forceCache(ctx=MDGContext::current()) -> MDataBlock

        Get the datablock for this node. If there is no datablock then one will be created.
        NOTE: This should be used only in places where fast access to the datablock outside of a compute is critical such as the transformUsing method of MPxSurfaceShape.

        * ctx (MDGContext) - The context in which the datablock will be retrieved.
        """

    def getCacheSetup(self, *args: Any, **kwargs: Any) -> Any:
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

    def getExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """getExternalContent(table) -> self

        The table populated by this method must include the location of all the content (files) used by this node, including those that do not exist.  See MExternalContentInfoTable for details.

        Keys used to add items to this table will be the same that get passed to setExternalContent through its MExternalContentLocationTable parameter to perform a batched change of content location.

        When implementing getExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also add their external content to the table.

        The default implementation does nothing.

        * table [OUT] (MExternalContentInfoTable) - Content information table that this method must populate.
        """

    def getFilesToArchive(self, *args: Any, **kwargs: Any) -> Any:
        """getFilesToArchive(shortName=False, unresolvedName=False, markCouldBeImageSequence=False) -> list of strings

        Use this method to return all external files used by this node. This file list will be used by the File > Archive zip feature, maya.exe -archive and the `file -q -list` mel command.

        Only include files that exist.

        If shortName is True, return just the filename portion of the path. Otherwise, return a full path.

        If unresolvedName is True, return the path before any resolution has been done (i.e leave it as a relative path, include unexpanded environment variables,  tildes, ".."s etc). Otherwise, resolve the file     path and return an absolute path (to resolve with standard Maya path resolution, use MFileObject.resolvedFullName()).

        * shortName (bool) - If True, only add the filename of the path.
        * unresolvedName (bool) - If True, add paths before any resolution, rather than absolute paths.
        * markCouldBeImageSequence (bool) - If True, append an asterisk after any file path that could be an image sequence (note: only used by maya.exe -archive).
        """

    def getInternalValue(self, *args: Any, **kwargs: Any) -> Any:
        """getInternalValue(plug, dataHandle) -> bool

        This method is overridden by nodes that store attribute data in some internal format.

        The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

        When internal attribute values are queried via getAttr or MPlug.getValue() this method is called.

        All internal data should respect the current context, which may be obtained from MDGContext::current()

        * plug (MPlug) - the attribute that is being queried.
        * dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
        """

    def getInternalValueInContext(self, *args: Any, **kwargs: Any) -> Any:
        """getInternalValueInContext(plug, dataHandle, ctx) -> bool [OBSOLETE]

        This method is obsolete. Override MPxNode.getInternalValue instead.

        * plug (MPlug) - the attribute that is being queried.
        * dataHandle [OUT] (MDataHandle) - the dataHandle to store the attribute value.
        * ctx (MDGContext) - the context the method is being evaluated in.
        """

    def hasInvalidationRangeTransformation(self, *args: Any, **kwargs: Any) -> Any:
        """hasInvalidationRangeTransformation() -> bool

        Checks if this MPxNode derived node overrides the MPxNode::transformInvalidationRange method
        """

    def inheritAttributesFrom(self, *args: Any, **kwargs: Any) -> Any:
        """inheritAttributesFrom(parentClassName) -> None

        This method allows a class of plugin node to inherit all of the attributes of a second class of plugin node.

        This method will only work during the static initialization method of the user defined node class and must be called before any other attributes have been added.  The initialization method is the one that is passed into  MFnPlugin.registerNode().

        A plugin node may only inherit attributes from one other class of plugin node. Attempting to call this method multiple times within a node's initialization method will result in an error.

        Both node classes must be registered using the same MPxNode type, listed in MPxNode.type().

        * parentClassName (string) - class of node to inherit attributes from.
        """

    def internalArrayCount(self, *args: Any, **kwargs: Any) -> Any:
        """internalArrayCount(plug) -> int
        internalArrayCount(plug, ctx) -> int  [OBSOLETE]

        This method is overridden by nodes that have internal array attributes which are not stored in Maya's datablock. This method is used by Maya to determine the non-sparse count of array elements during file IO. If the internal array is stored sparsely, you should return the maximum index of the array plus one. If the internal array is non-sparse then return the length of the array.

        This method does not need to be implemented for attributes that are stored in the datablock since Maya will use the datablock size.

        If this method is overridden, it should return -1 for attributes which it does not handle. Maya will use the datablock size to determine the array length when -1 is returned.

        All internal data should respect the current context, which may be obtained from MDGContext.current()

        * plug (MPlug) - the array plug.
        * ctx (MDGContext) - the context, default to MDGContext.current().
        """

    def isAbstractClass(self, *args: Any, **kwargs: Any) -> Any:
        """isAbstractClass() -> bool

        Override this class to return True if this node is an abstract node. An abstract node can only be used as a base class.  It cannot be created using the 'createNode' command.

        It is not necessary to override this method.
        """

    def isPassiveOutput(self, *args: Any, **kwargs: Any) -> Any:
        """isPassiveOutput(plug) -> bool

        This method may be overridden by the user defined node if it wants to provide output attributes which do not prevent value modifications to the destination attribute. For example, output plugs on animation curve nodes are passive. This allows the attributes driven by the animation curves to be set to new values by the user.

        * plug (MPlug) - plug representing output in question.
        """

    kAssembly: int = 22
    kBlendShape: int = 25
    kCameraSetNode: int = 16
    kClientDeviceNode: int = 20
    kConstraintNode: int = 17
    kDeformerNode: int = 2
    kDependNode: int = 0
    kEmitterNode: int = 6
    kEvaluatedDirectly: int = 1
    kEvaluatedIndirectly: int = 0
    kFieldNode: int = 5
    kFluidEmitterNode: int = 13
    kGeometryFilter: int = 24
    kHardwareShader: int = 9
    kHwShaderNode: int = 10
    kIkSolverNode: int = 8
    kImagePlaneNode: int = 14
    kLast: int = 26
    kLeaveDirty: int = 2
    kLocatorNode: int = 1
    kManipContainer: int = 3
    kManipulatorNode: int = 18
    kMotionPathNode: int = 19
    kObjectSet: int = 12
    kParticleAttributeMapperNode: int = 15
    kPostEvaluationTypeLast: int = 3
    kSkinCluster: int = 23
    kSpringNode: int = 7
    kSurfaceShape: int = 4
    kThreadedDeviceNode: int = 21
    kTransformNode: int = 11
    def legalConnection(self, *args: Any, **kwargs: Any) -> Any:
        """legalConnection(plug, otherPlug, asSrc) -> bool/None

        This method allows you to check for legal connections being made to attributes of this node.

        You should return None to specify that maya should handle this connection if you are unable to determine if it is legal.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (bool) - is this plug a source of the connection.
        """

    def legalDisconnection(self, *args: Any, **kwargs: Any) -> Any:
        """legalDisconnection(plug, otherPlug, arsSrc) -> bool/None

        This method allows you to check for legal disconnections being made to attributes of this node.

        You should return None to specify that maya should handle this disconnection if you are unable to determine if it is legal.

        * plug (MPlug) - attribute on this node.
        * otherPlug (MPlug) - attribute on other node.
        * asSrc (boool) - is this plug a source of the connection.
        """

    def name(self, *args: Any, **kwargs: Any) -> Any:
        """name() -> string

        Returns the name of this particular instance of this class.  Each objectin the dependency graph has a name.  This name will be used by the UIand by MEL.

        It is not necessary to override this method.

        Returns the name of the node
        """

    def passThroughToMany(self, *args: Any, **kwargs: Any) -> Any:
        """passThroughToMany(plug, plugArray) -> bool

        This method is overriden by nodes that want to control the traversal behavior of some Maya search algorithms which traverse the history/future of shape nodes looking for directly related nodes. In particular, the Artisan paint code uses this method when searching for paintable nodes, and the disk cache code uses this method when searching for upstream cacheFile nodes.

        If this method is not implemented or returns False, the base class Maya implementation of this method calls passThroughToOne and returns the results of that call.

        * plug (MPlug) - the plug.
        * plugArray (MPlugArray) - the corresponding plugs.
        """

    def passThroughToOne(self, *args: Any, **kwargs: Any) -> Any:
        """passThroughToOne(plug) -> plug

        This method may be overriden by nodes that have a one-to-one relationship between an input attribute and a corresponding output attribute. This method is used by Maya to perform the following capabilities:

        - When this node is deleted, the delete command will rewire the source of the input attribute to the destination of the output attribute if the source and destination are connected to nodes that are not deleted.
        - History traversal algorithms such as the bakePartialHistory command use this method to direct its traversal through a shape's construction history.
        - The base class Maya implementation of passThroughToAll will call this method if passThroughToAll returns False.

        * plug (MPlug) - the plug.
        """

    def postConstructor(self, *args: Any, **kwargs: Any) -> Any:
        """postConstructor() -> self

        Internally maya creates two objects when a user defined node is created, the internal MObject and the user derived object.
        The association between the these two objects is not made until after the MPxNode constructor is called. This implies that no MPxNode member function can be called from the MPxNode constructor.
        The postConstructor will get called immediately after the constructor when it is safe to call any MPxNode member function.
        """

    def postEvaluation(self, *args: Any, **kwargs: Any) -> Any:
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

    def preEvaluation(self, *args: Any, **kwargs: Any) -> Any:
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

    def setDependentsDirty(self, *args: Any, **kwargs: Any) -> Any:
        """setDependentsDirty(plug, plugArray) -> self

        This method can be overridden in user defined nodes to specify which plugs should be set dirty based upon an input plug which Maya is marking dirty. The list of plugs for Maya to mark dirty is returned by the plug array. This method handles both dynamic as well as non-dynamic plugs and is useful in the following ways:



        - Allows attributeAffects-style relationships to be handled for dynamically-added attributes. Since MPxNode.attributeAffects() can only be used with non-dynamic attributes, use of this method allows a way for all attributes of a node to affect one another, both dynamic and non-dynamic.

        - Provides more flexible relationships than what is available with MPxNode.attributeAffects(). For example, you may wish to not dirty plugs when the current frame is one. However, as the routine is called during dirty propagation, there are restrictions on what can be done within the routine, most importantly you must not cause any dependency graph computation. For details, see the IMPORTANT NOTE below.



        This method is designed to work harmoniously with MPxNode.attributeAffects() on the same node. Alternately, you can do all affects relationships within a yourNode.setDependentsDirty() implementation.

        The body of a user-implemented setDependentsDirty() implementation might look like the following example, which causes the plug called "B" to be set dirty whever plug "A" is changed, i.e. A affects B.

        * plug (MPlug) - plug which is being set dirty by Maya.
        * plugArray the programmer should add any plugs which they want to set dirty to this list.
        """

    def setDoNotWrite(self, *args: Any, **kwargs: Any) -> Any:
        """setDoNotWrite(bool) -> self

        Use this method to mark the "do not write" state of this proxy node.  If set, this node will not be saved when the Maya model is written out. 

        NOTES:
        1. Plug-in "requires" information will be written out with the model when saved.  But a subsequent reload and resave of the file will cause these to go away.
        2. If this node is a DAG and has a parent or children, the "do not write" flag of the parent or children will not be set. It is the developer's responsibility to ensure that the resulting scene file is capable of being read in without errors due to unwritten nodes. 
        """

    def setExistWithoutInConnections(self, *args: Any, **kwargs: Any) -> Any:
        """setExistWithoutInConnections(bool) -> bool

        This method specifies whether or not the node can exist without input
        connections.

        If a node connected to this node is deleted resulting in no more input
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        * flag (bool) true if this node can exist without input connections, false otherwise
        """

    def setExistWithoutOutConnections(self, *args: Any, **kwargs: Any) -> Any:
        """setExistWithoutOutConnections(bool) -> bool

        This method specifies whether or not the node can exist without
        output connections.

        If a node connected to this node is deleted resulting in no more output
        connections and if this flag is false, then this node will be deleted.

        Do not override this method.

        * flag (bool) true if this node can exist without output connections, false otherwise
        """

    def setExternalContent(self, *args: Any, **kwargs: Any) -> Any:
        """setExternalContent(table) -> self

        This is useful in the context of content relocation.  This will be called while the scene is being loaded to apply path changes performed externally. Consequently, interaction with the rest of the scene must be kept to a minimum.  It is however valid to call this method outside of scene loading contexts.

        The keys in the map must be the same as the ones provided by the node in getExternalContent.  The values are the new locations.

        When implementing setExternalContent, you are responsible for forwarding the call to the base class when it makes sense to do so, so that base classes  can also set their external content.

        The default implementation does nothing.

        * table Key->location table with new content locations.
        """

    def setExternalContentForFileAttr(self, *args: Any, **kwargs: Any) -> Any:
        """setExternalContentForFileAttr(attr, table) -> bool

        This method is a helper for derived clases implementing setExternalContent().  It assigns a value to a plug with the one from the table whose key is the same as the passed in attribute name.

        The method will not write to the plug if the attribute is not found in the  table.

        * attr (MObject) - The attribute of the plug we want to write to.
        * table (MExternalContentLocationTable) - A table which may hold or not the value for a given plug.

        Returns True if the plug was successfully written to. False if no entry in the table was named after the attribute or if no plug was found.
        """

    def setInternalValue(self, *args: Any, **kwargs: Any) -> Any:
        """setInternalValue(plug, dataHandle) -> bool


        This method is overriden by nodes that store attribute data in some internal format.

        The internal state of attributes can be set or queried using the setInternal and internal methods of MFnAttribute.

        When internal attribute values are set via setAttr or MPlug.setValue() this method is called.

        Another use for this method is to impose attribute limits.

        All internal data should respect the current context, which may be obtained from MDGContext::current()

        * plug (MPlug) - the attribute that is being set.
        * dataHandle (MDataHandle) - the dataHandle containing the value to set.
        """

    def setInternalValueInContext(self, *args: Any, **kwargs: Any) -> Any:
        """setInternalValueInContext(plug, dataHandle, ctx) -> bool  [OBSOLETE]

        This method is obsolete. Override MPxNode.setInternalValue instead.

        * plug (MPlug) - the attribute that is being set.
        * dataHandle (MDataHandle) - the dataHandle containing the value to set.
        * ctx (MDGContext) - the context the method is being evaluated in.
        """

    def setMPSafe(self, *args: Any, **kwargs: Any) -> Any:
        """setMPSafe(bool) -> self

        This method is obsolete. Override MPxNode.setSchedulingType instead.

        Set a flag to specify if a user defined shading node is safe for multi-processor rendering. For a shading node to be MP safe, it cannot access any shared global data and should only use attributes in the datablock to get input data and store output data. 

        NOTE: This should be called from the postConstructor() method for shading node plug-ins only. If a shading node is non-safe, then it will only be useful during single processor rendering.
        """

    def shouldSave(self, *args: Any, **kwargs: Any) -> Any:
        """shouldSave(plug) -> bool/None

        This method may be overridden by the user defined node.  It should only be required to override this on rare occasions.

        This method determines whether a specific attribute of this node should be written out during a file save.  The default behavior is to only write the value if it differs from the default and is not being supplied by a connection.  This behavior should be sufficient in most cases.
        This method is not called for ramp attributes since they should always be written.

        * plug (MPlug) - plug representing the attribute to be saved.
        """

    def thisMObject(self, *args: Any, **kwargs: Any) -> Any:
        """thisMObject() -> MObject

        Returns the MObject associated with this user defined node.  This makes it possible to use MFnDependencyNode or to construct plugs to this node's attributes.
        """

    def transformInvalidationRange(self, *args: Any, **kwargs: Any) -> Any:
        """transformInvalidationRange(plug, timeRange) -> timeRange

        Override this method to register this node as an Invalidation-Range-Transformation kernel (IRT kernel) An IRT kernel node will change the invalidation time range for its downstream nodes For example, Dynamics-solver will transform invalidation time range [a,b] to [a,+inf) And Clip-Time-Editor will send out the invalidation range for each of the clip [a,b] to ( [t0+a,t0+b] U [t1+a,t1+b] U [t2+a,t2+b] U ... ) 

        * source (MPlug)     - The source plug in this node where the dirty propagation comes from
        * input (MTimeRange) - The incoming invalidation range


        Returns The output invalidation range for all the dependents of plug 'source'

        WARNING: You cannot do any evaluation in this function, because it can be called in dirty-propagation
        WARNING: Do *not* call MPxNode::transformInvalidationRange from your override method
        NOTE: If a plugin node have invalidation-range-transformation *conditionally* Only transform the invalidation range when attribute 'enableIRT' is set The plugin should call MPxNode::transformInvalidationRange to signal it does not perform any IRT.
        """

    def type(self, *args: Any, **kwargs: Any) -> Any:
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
          kSkinCluster                                  Custom deformer derived from MPxSkinCluster
          kGeometryFilter                               Custom deformer derived from MPxGeometryFilter
                 kBlendShape                                    Custom deformer derived from MPxBlendShape
        """

    def typeId(self, *args: Any, **kwargs: Any) -> Any:
        """typeId() -> MTypeId

        Returns the TYPEID of this node.
        """

    def typeName(self, *args: Any, **kwargs: Any) -> Any:
        """typeName() -> string

        Returns the type name of this node.  The type name identifies the node type to the ASCII file format
        """


class MPxSurfaceShape(MPxNode):
    """Parent class of all user defined shapes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def acceptsGeometryIterator(self, *args: Any, **kwargs: Any) -> Any:
        """acceptsGeometryIterator(component, writeable=True, forReadOnly=False) -> bool
        acceptsGeometryIterator(writeable=True) -> boolboundingBox() -> MBoundingBox

        Returns True if the shape can supply a component iterator.
        This methods should be overridden to return True. The default is to return False.

        * component (MObject) - the component to test
        * writeable (bool) - is this component type writable by an iterator
        * forReadOnly (bool) - is this component type readable by an iterator
        """

    def activeComponents(self, *args: Any, **kwargs: Any) -> Any:
        """activeComponents() -> MObjectArray

        Returns a list of active (selected) components for the shape.
        """

    def boundingBox(self, *args: Any, **kwargs: Any) -> Any:
        """boundingBox() -> MBoundingBox

        This method should be overridden to return a bounding box for the shape.
        If this method is overridden, then MPxSurfaceShape.isBounded() should also be overridden to return True.
        """

    boundingBoxCenterX: MObject = <OpenMaya.MObject object at 0x00000218AAE21790>
    boundingBoxCenterY: MObject = <OpenMaya.MObject object at 0x00000218AAE217B0>
    boundingBoxCenterZ: MObject = <OpenMaya.MObject object at 0x00000218AAE217D0>
    def cachedShapeAttr(self, *args: Any, **kwargs: Any) -> Any:
        """cachedShapeAttr() -> MObject

        Returns the attribute containing the shape's cached geometry, if it has one.
        """

    def canMakeLive(self, *args: Any, **kwargs: Any) -> Any:
        """canMakeLive() -> bool

        This method is used by Maya to determine whether a surface can be made live. It can be overridden to return True if you wish to allow your surface to be made live. If you return True, you will also need to implement both closestPoint() overloads. The default is to return False.
        """

    center: MObject = <OpenMaya.MObject object at 0x00000218AAE21770>
    def childChanged(self, *args: Any, **kwargs: Any) -> Any:
        """childChanged(state=kObjectChanged) -> self

        This method can be used to trigger the shape to recalculate its bounding box.

        * state (int) - the type of change that has occurred

        Valid state:
          kObjectChanged         Object geometry changed. Internal caches need to be updated.
          kBoundingBoxChanged    Object geometry is unchanged but its bounding box has changed.
                                 This might happen if the object was moved or an offset changed.
        """

    def closestPoint(self, *args: Any, **kwargs: Any) -> Any:
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

        If no intersection is found and findClosestOnMiss is True, you should still provide a point on your surface closest to the ray defined by raySource and rayDirection. When used for live snapping, this allows the user to click and drag outside the bounds    of a live surface and still have it snap to the nearest point on it within the viewport. Note, performing a pure 3D closest point of approach test in this situation may not give the most natural result for live mesh snapping.
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

    def componentToPlugs(self, *args: Any, **kwargs: Any) -> Any:
        """componentToPlugs(component, selectionList) -> self

        Converts the given component into a selection list of plugs.
        This method is used to associate a shapes components into the corresponding attributes (plugs) within the shape. For example, it gets called by the translate manipulator to determine which attributes should be driven by the manipulator, and by the setKeyframe command to determine where to connect animCurves for components.

        This method should be overridden if the shape supports components that can be selected and moved in Maya.

        * component (MObject) - the component to be converted
        * list (MSelectionList) - a selection list where the plug should be added
        """

    def convertToTweakNodePlug(self, *args: Any, **kwargs: Any) -> Any:
        """convertToTweakNodePlug(plug) -> bool

        Check if a tweak node is connected to this node. If it is, then reset the supplied plug to contain the controlPoints attribute on the tweak node.
        Returns True if a tweak node was found, False if the plug was unchanged

        * plug (MPlug) - plug which will be set to point to the associated tweak node plug if a tweak node is connected
        """

    def createFullRenderGroup(self, *args: Any, **kwargs: Any) -> Any:
        """createFullRenderGroup() -> MObject

        Returns a component containing all of renderable elements in the shape.
        This method is used to create a component containing every renderable element in the object.

        This method is supposed to return non-null object only if the dag object contains renderable components. Type of the return component should is the same as the one returned by MPxSurfaceShape::renderGroupComponentType().
        """

    def createFullVertexGroup(self, *args: Any, **kwargs: Any) -> Any:
        """createFullVertexGroup() -> MObject

        Returns a component containing all of the vertices in the shape.
        This method is used to create a component containing every vertex/CV in the object.

        This method is supposed to return non-null object only if the dag object contains vertices/CVs (control points), so derived classes that do should override this method.
        """

    def deleteComponents(self, *args: Any, **kwargs: Any) -> Any:
        """deleteComponents(componentList, undoInfo) -> bool

        Returns True if this method was successful, False otherwise.
        This method should be overridden if the shape is to support deletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component can be stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.

        * componentList (MObjectArray) - List of components to be deleted
        * undoInfo (MDoubleArray) - Values used for undo purposes
        """

    def excludeAsPluginShape(self, *args: Any, **kwargs: Any) -> Any:
        """excludeAsPluginShape() -> bool

        A Maya viewport can be set to not display "Plugin Shapes", which means shapes derived from MPxSurfaceShape. By overriding excludeAsPluginShape() to return False, you can change that behaviour so that this shape is still displayed even when the display of "Plugin Shapes" is disabled.
        The default implementation returns True.
        Returns True to have this shape obey the "Plugin Shapes" settings in the viewport's "Show" menu; False to have it ignore that setting.
        """

    def geometryData(self, *args: Any, **kwargs: Any) -> Any:
        """geometryData() -> MObject

        Returns the geometry data of the shape. The geometry data must be derived from the MPxGeometryData class.

        The data is used by Maya to add, edit and query component grouping (set) information for the shape. This set information is stored and managed by Maya's shape base class, geometryShape.
        """

    def geometryIteratorSetup(self, *args: Any, **kwargs: Any) -> Any:
        """geometryIteratorSetup(componentList, components, forReadOnly=False) -> MPxGeometryIterator

        This method should be overridden by the user to return a geometry iterator compatible with the user's geometry.
        A geometry iterator is used for iterating over the components of a shape, such as the vertices of a mesh, in a generic manner.

        The components to be iterated over are passed to this function in on of two ways, as a list of components, or as a single component.
        Only one of these arguments is used at any particular time.

        * componentList (MObjectArray) - a list of components to be iterated over
        * components (MObject) - the components to be iterated over
        * forReadOnly (bool) - specifies whether the iterator is for read-only
        """

    def getComponentSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """getComponentSelectionMask() -> MSelectionMask

        Returns the selection mask of the shape.
        This routine must be overridden if the shape is to support interactive component selection in Viewport 2.0 and should provide information about the selection mask of the shape component.
        """

    def getShapeSelectionMask(self, *args: Any, **kwargs: Any) -> Any:
        """getShapeSelectionMask() -> MSelectionMask

        Returns the selection mask of the shape.
        This routine must be overridden if the shape is to support interactive object selection in Viewport 2.0 and should provide information about the selection mask of the shape.
        """

    def getWorldMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """getWorldMatrix(block, instanceGeom) -> MMatrix

        Returns MMatrix which takes a point from local object space to world space.

        * block (MDataBlock) - a MDataBlock
        * instanceGeom (int) - the instance this MPxSurfaceShape corresponds to
        """

    def hasActiveComponents(self, *args: Any, **kwargs: Any) -> Any:
        """hasActiveComponents() -> bool

        This method is used to determine whether or not the shape has active (selected) components.
        """

    instObjGroups: MObject = <OpenMaya.MObject object at 0x00000218AAE21910>
    intermediateObject: MObject = <OpenMaya.MObject object at 0x00000218AAE218D0>
    inverseMatrix: MObject = <OpenMaya.MObject object at 0x00000218AAE21810>
    def isBounded(self, *args: Any, **kwargs: Any) -> Any:
        """isBounded() -> bool

        This method should be overridden to return True if the user supplies a bounding box routine.  Supplying a bounding box routine makes refresh and selection more efficient.
        Returns a boolean value indicating whether a bounding box routine has been supplied
        """

    isRenderable: getset_descriptor = <attribute 'isRenderable' of 'OpenMaya.MPxSurfaceShape' objects>
    isTemplated: MObject = <OpenMaya.MObject object at 0x00000218AAE218F0>
    def localShapeInAttr(self, *args: Any, **kwargs: Any) -> Any:
        """localShapeInAttr() -> MObject

        Returns the attribute containing the shape's input geometry in local space.

        This method will be called by Maya to determine if the shape has construction history and must be overridden if the shape is to support deformers.
        """

    def localShapeOutAttr(self, *args: Any, **kwargs: Any) -> Any:
        """localShapeOutAttr() -> MObject

        Returns the attribute containing the shape's output geometry in local space.

        This method must be overridden if the shape is to support deformers.
        """

    mControlPoints: MObject = <OpenMaya.MObject object at 0x00000218AAE21570>
    mControlValueX: MObject = <OpenMaya.MObject object at 0x00000218AAE21590>
    mControlValueY: MObject = <OpenMaya.MObject object at 0x00000218AAE215B0>
    mControlValueZ: MObject = <OpenMaya.MObject object at 0x00000218AAE215D0>
    mHasHistoryOnCreate: MObject = <OpenMaya.MObject object at 0x00000218AAE21550>
    def match(self, *args: Any, **kwargs: Any) -> Any:
        """match(mask, componentList) -> bool

        This method is used to check for matches between a selection type (or mask) and a given component. If your shape has components representing attributes then this method is used to match up your components with selection masks.

        This is used by sets and deformers to make sure that the selected components fall into the "vertex only" category. This is useful when you want to make sure that only a particular component can be deformed.

        * mask (MSelectionMask) - the selection mask to test against
        * componentList (MObjectArray) - a list of components to be tested
        """

    def matchComponent(self, *args: Any, **kwargs: Any) -> Any:
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

    matrix: MObject = <OpenMaya.MObject object at 0x00000218AAE217F0>
    def newControlPointComponent(self, *args: Any, **kwargs: Any) -> Any:
        """newControlPointComponent() -> MObject

        The default action of this method is to return an MFnSingleIndexedComponent (of type MFn::kMeshVertComponent) in order to support rigid skinning binds.

        This method can be overridden to support other types of components such as MFnDoubleIndexedComponent and MFnTripleIndexedComponent      and should return a new component of that type.  The types allowed are those listed in the create() method docs for each MFn*IndexedComponent.
        """

    nodeBoundingBox: MObject = <OpenMaya.MObject object at 0x00000218AAE215F0>
    nodeBoundingBoxMax: MObject = <OpenMaya.MObject object at 0x00000218AAE21690>
    nodeBoundingBoxMaxX: MObject = <OpenMaya.MObject object at 0x00000218AAE216B0>
    nodeBoundingBoxMaxZ: MObject = <OpenMaya.MObject object at 0x00000218AAE216D0>
    nodeBoundingBoxMin: MObject = <OpenMaya.MObject object at 0x00000218AAE21610>
    nodeBoundingBoxMinX: MObject = <OpenMaya.MObject object at 0x00000218AAE21630>
    nodeBoundingBoxMinY: MObject = <OpenMaya.MObject object at 0x00000218AAE21650>
    nodeBoundingBoxMinZ: MObject = <OpenMaya.MObject object at 0x00000218AAE21670>
    nodeBoundingBoxSize: MObject = <OpenMaya.MObject object at 0x00000218AAE216F0>
    nodeBoundingBoxSizeX: MObject = <OpenMaya.MObject object at 0x00000218AAE21710>
    nodeBoundingBoxSizeY: MObject = <OpenMaya.MObject object at 0x00000218AAE21730>
    nodeBoundingBoxSizeZ: MObject = <OpenMaya.MObject object at 0x00000218AAE21750>
    objectColor: MObject = <OpenMaya.MObject object at 0x00000218AAE219D0>
    objectGroupColor: MObject = <OpenMaya.MObject object at 0x00000218AAE21990>
    objectGroupId: MObject = <OpenMaya.MObject object at 0x00000218AAE21970>
    objectGroups: MObject = <OpenMaya.MObject object at 0x00000218AAE21930>
    objectGrpCompList: MObject = <OpenMaya.MObject object at 0x00000218AAE21950>
    parentInverseMatrix: MObject = <OpenMaya.MObject object at 0x00000218AAE21890>
    parentMatrix: MObject = <OpenMaya.MObject object at 0x00000218AAE21870>
    def pointAtParm(self, *args: Any, **kwargs: Any) -> Any:
        """pointAtParm(atThisParm, evaluatedPoint) -> bool

        This method is used by Maya in functions (such as select) that require point at parameter values. This only makes sense for parametric surfaces such as NURBS.
        Returns True if a point was found, False otherwise

        * atThisParm (MPoint) - the parameter to check
        * evaluatedPoint [OUT] (MPoint) - the surface point
        """

    def renderGroupComponentType(self, *args: Any, **kwargs: Any) -> Any:
        """renderGroupComponentType() -> int

        This method is used to return the type of renderable components for this shape. It should return a type among MFn::kMeshPolygonComponent, MFn::kSubdivFaceComponent and MFn::kSurfaceFaceComponent, which is used in the creation of per-face/patch shader assignment.

        Returns the type of renderable components for this shape.
        See MFnSet.addMember()
        """

    def transformUsing(self, *args: Any, **kwargs: Any) -> Any:
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

    def tweakUsing(self, *args: Any, **kwargs: Any) -> Any:
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

    def undeleteComponents(self, *args: Any, **kwargs: Any) -> Any:
        """undeleteComponents(componentList, undoInfo) -> bool

        This method should be overridden if the shape is to support undeletion of components. A list of components to be deleted will be passed in as well as an array of doubles where information about each deleted component is stored for undo purposes. A typical use for this array is to store knot values or weights for control points that are deleted.
        Returns True if this method was successful, False otherwise

        * componentList (MObjectArray) - List of components that were deleted
        * undoInfo (MDoubleArray) - Values used for undo purposes
        """

    useObjectColor: MObject = <OpenMaya.MObject object at 0x00000218AAE219B0>
    def vertexOffsetDirection(self, *args: Any, **kwargs: Any) -> Any:
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

    visibility: MObject = <OpenMaya.MObject object at 0x00000218AAE218B0>
    def weightedTransformUsing(self, *args: Any, **kwargs: Any) -> Any:
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

    def weightedTweakUsing(self, *args: Any, **kwargs: Any) -> Any:
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

    worldInverseMatrix: MObject = <OpenMaya.MObject object at 0x00000218AAE21850>
    worldMatrix: MObject = <OpenMaya.MObject object at 0x00000218AAE21830>
    def worldShapeOutAttr(self, *args: Any, **kwargs: Any) -> Any:
        """worldShapeOutAttr() -> MObject

        Returns the attribute containing the shape's output geometry in world space.

        This method must be overridden if the shape is to support deformers.
        """


class MQuaternion(object):
    """Quaternion math."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __neg__(self) -> Any:
        """-self"""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def asAxisAngle(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as a tuple containing an axis vector and an angle in radians about that axis."""

    def asEulerRotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent MEulerRotation."""

    def asMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the rotation as an equivalent rotation matrix."""

    def conjugate(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the conjugate of this quaternion (i.e. x, y and z components negated)."""

    def conjugateIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place conjugation (i.e. negates the x, y and z components)."""

    def exp(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the exponent of this one."""

    def inverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the inverse of this one."""

    def invertIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place inversion."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if the distance between the two quaternions (in quaternion space) is less than or equal to the given tolerance."""

    kIdentity: MQuaternion = (0, 0, 0, 1)
    kTolerance: float = 1e-10
    def log(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the natural log of this one."""

    def negateIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place negation of the x, y, z and w components."""

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion containing the normalized version of this one (i.e. scaled to unit length)."""

    def normalizeIt(self, *args: Any, **kwargs: Any) -> Any:
        """In-place normalization (i.e. scales the quaternion to unit length)."""

    def setToXAxis(self, *args: Any, **kwargs: Any) -> Any:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the X-axis."""

    def setToYAxis(self, *args: Any, **kwargs: Any) -> Any:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Y-axis."""

    def setToZAxis(self, *args: Any, **kwargs: Any) -> Any:
        """Set this quaternion to be equivalent to a rotation of a given angle, in radians, about the Z-axis."""

    def setValue(self, *args: Any, **kwargs: Any) -> Any:
        """Set the value of this quaternion to that of the specified MQuaternion, MEulerRotation, MMatrix or MVector and angle."""

    def slerp(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the quaternion at a given interpolation value along the shortest path between two quaternions."""

    def squad(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the quaternion at a given interpolation value along a cubic curve segment in quaternion space."""

    def squadPt(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new quaternion representing an intermediate point which when used with squad() will produce a C1 continuous spline."""

    w: getset_descriptor = <attribute 'w' of 'OpenMaya.MQuaternion' objects>
    x: getset_descriptor = <attribute 'x' of 'OpenMaya.MQuaternion' objects>
    y: getset_descriptor = <attribute 'y' of 'OpenMaya.MQuaternion' objects>
    z: getset_descriptor = <attribute 'z' of 'OpenMaya.MQuaternion' objects>

class MRampAttribute(object):
    """Functionset for creating and working with ramp attributes."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addEntries(self, *args: Any, **kwargs: Any) -> Any:
        """Adds entries to the ramp."""

    def createColorRamp(self, *args: Any, **kwargs: Any) -> Any:
        """Creates and returns a new color ramp attribute."""

    def createCurveRamp(self, *args: Any, **kwargs: Any) -> Any:
        """Creates and returns a new curve ramp attribute."""

    def createRamp(self, *args: Any, **kwargs: Any) -> Any:
        """Creates and returns a new color or curve ramp attribute initialized with values."""

    def deleteEntries(self, *args: Any, **kwargs: Any) -> Any:
        """Removes from the ramp those entries with the specified indices."""

    def getEntries(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a tuple containing all of the entries in the ramp."""

    def getValueAtPosition(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the value of the entry at the given position."""

    def hasIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Return true if an entry is defined at this index."""

    isColorRamp: getset_descriptor = <attribute 'isColorRamp' of 'OpenMaya.MRampAttribute' objects>
    isCurveRamp: getset_descriptor = <attribute 'isCurveRamp' of 'OpenMaya.MRampAttribute' objects>
    kLinear: int = 1
    kNone: int = 0
    kSmooth: int = 2
    kSpline: int = 3
    def numEntries(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of entries in the ramp."""

    def pack(self, *args: Any, **kwargs: Any) -> Any:
        """Change the indices numbering by re-ordering them from 0."""

    def setInterpolationAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the interpolation of the entry at the given index."""

    def setPositionAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the position of the entry at the given index."""

    def setRamp(self, *args: Any, **kwargs: Any) -> Any:
        """Set this ramp with one or multiple entries. Current entries are removed before adding the new one(s)."""

    def setValueAtIndex(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the value of the entry at the given index."""

    def sort(self, *args: Any, **kwargs: Any) -> Any:
        """Sort the ramp by position. Indices are also re-ordered during sort."""


class MRichSelection(object):
    """A selection list supporting soft selection and symmetry.

    The rich selection is split into two halves: the 'normal' side,
    and an optional symmetric component. Components on both sides
    can include weight data which is used to specify both the amount
    of influence and the proximity to the centre of symmetry.

    In addition to the selected objects, the rich selection also
    includes information about the axis of symmetry so that
    operations can determine how to process any symmetric selection
    (e.g. reflect transformations).

    __init__()
    Initializes a new, empty MRichSelection object.

    __init__(MRichSelection other)
    Initializes a new MRichSelection object containing the same
    items as another rich selection.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self


        Empties the rich selection.
        """

    def getRawSymmetryMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """getRawSymmetryMatrix() -> (MMatrix, space)

        Returns a tuple containing the raw symmetry matrix to use for the
        symmetric components of the rich selection, and the transformation
        space used by the matrix (see MSpace). The caller is responsible for
        handling any necessary transformation space conversions.
        """

    def getSelection(self, *args: Any, **kwargs: Any) -> Any:
        """getSelection() -> MSelectionList

        Returns a copy of the non-symmetry component of the rich selection.
        """

    def getSymmetry(self, *args: Any, **kwargs: Any) -> Any:
        """getSymmetry() -> MSelectionList

        Returns a copy of the symmetry component of the rich selection.
        """

    def getSymmetryMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """getSymmetryMatrix(MDagPath, space) -> MMatrix

        Returns the symmetry matrix to use for the symmetric component of
        the specified DAG object. The matrix will already be converted to
        use the specified transformation space (see MSpace).
        """

    def getSymmetryPlane(self, *args: Any, **kwargs: Any) -> Any:
        """getSymmetryPlane(MDagPath, space) -> MPlane

        Returns the plane of symmetry, in the specified transformation space
        (see MSpace). This can be used to enforce seam weights in tools that
        support symmetry. Note that the direction of the plane carries no
        significance. Specifically, having a positive offset from the plane
        does not imply a point is part of the non-symmetric selection.
        """

    def setSelection(self, *args: Any, **kwargs: Any) -> Any:
        """setSelection(MSelectionList) -> self

        Sets the non-symmetry component of the rich selection.
        """


class MSceneMessage(MMessage):
    """Class used to register callbacks for scene related messages."""
    def addCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addCheckCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addCheckFileCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addCheckReferenceCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addConnectionFailedCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addReferenceCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def addStringArrayCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    kAfterCreateReference: int = 45
    kAfterCreateReferenceAndRecordEdits: int = 50
    kAfterExport: int = 11
    kAfterExportReference: int = 21
    kAfterFileRead: int = 8
    kAfterImport: int = 4
    kAfterImportReference: int = 19
    kAfterLoadReference: int = 37
    kAfterLoadReferenceAndRecordEdits: int = 48
    kAfterOpen: int = 6
    kAfterPluginLoad: int = 41
    kAfterPluginUnload: int = 43
    kAfterReference: int = 15
    kAfterRemoveReference: int = 17
    kAfterSave: int = 13
    kAfterSceneReadAndRecordEdits: int = 9
    kAfterSoftwareFrameRender: int = 27
    kAfterSoftwareRender: int = 25
    kAfterUnloadReference: int = 23
    kBeforeCreateReference: int = 44
    kBeforeCreateReferenceAndRecordEdits: int = 49
    kBeforeCreateReferenceCheck: int = 39
    kBeforeExport: int = 10
    kBeforeExportCheck: int = 35
    kBeforeExportReference: int = 20
    kBeforeFileRead: int = 7
    kBeforeImport: int = 3
    kBeforeImportCheck: int = 34
    kBeforeImportReference: int = 18
    kBeforeLoadReference: int = 36
    kBeforeLoadReferenceAndRecordEdits: int = 47
    kBeforeLoadReferenceCheck: int = 38
    kBeforeNewCheck: int = 31
    kBeforeOpen: int = 5
    kBeforeOpenCheck: int = 32
    kBeforePluginLoad: int = 40
    kBeforePluginUnload: int = 42
    kBeforeReference: int = 14
    kBeforeReferenceCheck: int = 39
    kBeforeRemoveReference: int = 16
    kBeforeSave: int = 12
    kBeforeSaveCheck: int = 33
    kBeforeSoftwareFrameRender: int = 26
    kBeforeSoftwareRender: int = 24
    kBeforeUnloadReference: int = 22
    kExportStarted: int = 46
    kLast: int = 51
    kMayaExiting: int = 30
    kMayaInitialized: int = 29
    kSoftwareRenderInterrupted: int = 28

class MSelectionList(object):
    """A heterogenous list of MObjects, MPlugs and MDagPaths.

    __init__()
    Initializes a new, empty MSelectionList object.

    __init__(MSelectionList other)
    Initializes a new MSelectionList object containing the same
    items as another list.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def add(self, *args: Any, **kwargs: Any) -> Any:
        """add(pattern, searchChildNamespaces=False) -> self
        add(item, mergeWithExisting=True) -> self


        The first version adds to the list any nodes, DAG paths, components
        or plugs which match the given the pattern string.

        The second version adds the specific item to the list, where the
        item can be a plug (MPlug), a node (MObject), a DAG path (MDagPath)
        or a component (tuple of (MDagPath, MObject) ).
        """

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Empties the selection list.
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(src) -> self

        Replaces the contents of the selection list with a copy of those from src (MSelectionList).
        """

    def getComponent(self, *args: Any, **kwargs: Any) -> Any:
        """getComponent(index) -> (MDagPath, MObject)

        Returns the index'th item of the list as a component, represented by
        a tuple containing an MDagPath and an MObject. If the item is just a
        DAG path without a component then MObject.kNullObj will be returned
        in the second element of the tuple. Raises TypeError if the item is
        neither a DAG path nor a component. Raises IndexError if index is
        out of range.
        """

    def getDagPath(self, *args: Any, **kwargs: Any) -> Any:
        """getDagPath(index) -> MDagPath

        Returns the DAG path associated with the index'th item of the list.
        Raises TypeError if the item is neither a DAG path nor a component.
        Raises IndexError if index is out of range.
        """

    def getDependNode(self, *args: Any, **kwargs: Any) -> Any:
        """getDependNode(index) -> MObject

        Returns the node associated with the index'th item, whether it be a
        dependency node, DAG path, component or plug.
        Raises kFailure if there is no dependency node associated with the current item.
        Raises IndexError if index is out of range.
        """

    def getPlug(self, *args: Any, **kwargs: Any) -> Any:
        """getPlug(index) -> MPluggetPlug(index, convertComponents) -> MPlug

        Returns the index'th item of the list as a plug. Raises TypeError if
        the item is not a plug. Raises IndexError if index is out of range.
        If convertComponents is True then components in the selection list that have a corresponding plug will return that instead.
        Note: This only works if the component selection can be converted into a single plug - single component or all components selected.
        """

    def getSelectionStrings(self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionStrings(index=None) -> (string, string, ...)

        Returns a tuple containing the string representation of the
        specified item. For nodes, DAG paths, plugs and contiguous
        components the tuple will only contain a single string, but for non-
        contiguous components there will be a separate string for each
        distinct block of contiguous elements. If index is not specified
        then the string representations of all the items in the selection
        list are returned. Raises IndexError if index is out of bounds.
        """

    def hasItem(self, *args: Any, **kwargs: Any) -> Any:
        """hasItem(item) -> bool

        Returns True if the given item is on the selection list. For a
        component this means that all of the elements of the component must
        be on the list. A component is passed as a tuple containing the
        MDagPath of the DAG node and an MObject containing the component.
        """

    def hasItemPartly(self, *args: Any, **kwargs: Any) -> Any:
        """hasItemPartly(dagPath, component) -> bool

        Returns True if at least one of the component's elements is on the
        selection list. Raises TypeError if dagPath is invalid or component
        does not contain a component.
        """

    def intersect(self, *args: Any, **kwargs: Any) -> Any:
        """intersect(other, expandToLeaves=False) -> self

        Modify this list to contain the intersection of itself and the given list.
        """

    def isEmpty(self, *args: Any, **kwargs: Any) -> Any:
        """isEmpty() -> bool

        Returns True if the selection list is empty.
        """

    kMergeNormal: int = 0
    kRemoveFromList: int = 2
    kXORWithList: int = 1
    def length(self, *args: Any, **kwargs: Any) -> Any:
        """length() -> int

        Returns the number of items on the selection list.
        """

    def merge(self, *args: Any, **kwargs: Any) -> Any:
        """merge(other, strategy=kMergeNormal) -> self
        merge(dagPath, component, strategy=kMergeNormal) -> self

        The first version merges the items from another selection list in
        with those already on the list, using the given strategy.

        The second version merges the specified component with those already
        on the list.
        """

    def remove(self, *args: Any, **kwargs: Any) -> Any:
        """remove(index) -> self

        Removes the index'th item from the list. Raises IndexError if the
        index is out of range.
        """

    def replace(self, *args: Any, **kwargs: Any) -> Any:
        """replace(index, newItem) -> self

        Replaces the index'th item on the list with a new item. A component
        is passed as a tuple containing the MDagPath of the DAG node and an
        MObject containing the component. Raises IndexError if the index is
        out of range.
        """

    def toggle(self, *args: Any, **kwargs: Any) -> Any:
        """toggle(dagPath, component) -> self

        Removes from the list those elements of the given component which
        are already on it and adds those which are not.
        """


class MSelectionMask(object):
    """Selection masks provide a way to control what is selectable in Maya."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addMask(self, *args: Any, **kwargs: Any) -> Any:
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

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy data from source selection mask.

        * source (MSelectionMask) - The source selection mask to copy from
        """

    def deregisterSelectionType(self, *args: Any, **kwargs: Any) -> Any:
        """deregisterSelectionType(selTypeName) -> bool

        Unregisters a previously registered selection type.

        * selTypeName (string) - Name of the selection type.
        """

    def getSelectionTypePriority(self, *args: Any, **kwargs: Any) -> Any:
        """getSelectionTypePriority(selTypeName) -> int

        Gets the selection priority corresponding to a given selection type.

        * selTypeName (string) - Name of the selection type.
        """

    def intersects(self, *args: Any, **kwargs: Any) -> Any:
        """intersects(mask) -> bool
        intersects(selType) -> bool

        Returns True if the specified selection mask or selection type is contained within this selection mask.

        * mask (MSelectionMask) - the selection mask to test.
        * selType (int) - the selection type to test.  See addMask() for a list of valid selection masks.
        """

    kSelectAnimAny: int = 68
    kSelectAnimCurves: int = 63
    kSelectAnimInTangents: int = 65
    kSelectAnimKeyframes: int = 64
    kSelectAnimMask: int = 67
    kSelectAnimOutTangents: int = 66
    kSelectCVs: int = 30
    kSelectCameras: int = 6
    kSelectClusters: int = 8
    kSelectCollisionModels: int = 21
    kSelectComponentsMask: int = 62
    kSelectCurveKnots: int = 47
    kSelectCurveParmPoints: int = 46
    kSelectCurves: int = 26
    kSelectCurvesOnSurfaces: int = 53
    kSelectDynamicConstraints: int = 82
    kSelectEdges: int = 42
    kSelectEditPoints: int = 32
    kSelectEmitters: int = 16
    kSelectFacets: int = 43
    kSelectFields: int = 17
    kSelectFluids: int = 77
    kSelectFollicles: int = 79
    kSelectGuideLines: int = 71
    kSelectHairSystems: int = 78
    kSelectHandles: int = 0
    kSelectHulls: int = 31
    kSelectIkEndEffectors: int = 3
    kSelectIkHandles: int = 2
    kSelectIsoparms: int = 52
    kSelectJointPivots: int = 57
    kSelectJoints: int = 4
    kSelectLatticePoints: int = 55
    kSelectLattices: int = 7
    kSelectLights: int = 5
    kSelectLocalAxis: int = 1
    kSelectLocators: int = 28
    kSelectManipulators: int = 70
    kSelectMeshComponents: int = 45
    kSelectMeshEdges: int = 34
    kSelectMeshFaces: int = 36
    kSelectMeshFreeEdges: int = 35
    kSelectMeshLines: int = 44
    kSelectMeshUVs: int = 40
    kSelectMeshVerts: int = 33
    kSelectMeshes: int = 12
    kSelectNCloths: int = 80
    kSelectNParticles: int = 83
    kSelectNRigids: int = 81
    kSelectNurbsCurves: int = 10
    kSelectNurbsSurfaces: int = 11
    kSelectObjectGroups: int = 75
    kSelectObjectsMask: int = 29
    kSelectOrientationLocators: int = 23
    kSelectPPStrokes: int = 54
    kSelectParticleShapes: int = 15
    kSelectParticles: int = 56
    kSelectPivots: int = 60
    kSelectPointsForGravity: int = 72
    kSelectPointsOnCurvesForGravity: int = 73
    kSelectPointsOnSurfacesForGravity: int = 74
    kSelectRigidBodies: int = 19
    kSelectRigidConstraints: int = 20
    kSelectRotatePivots: int = 59
    kSelectScalePivots: int = 58
    kSelectSculpts: int = 9
    kSelectSelectHandles: int = 61
    kSelectSketchPlanes: int = 14
    kSelectSprings: int = 18
    kSelectSubdiv: int = 13
    kSelectSubdivMeshEdges: int = 38
    kSelectSubdivMeshFaces: int = 39
    kSelectSubdivMeshMaps: int = 76
    kSelectSubdivMeshPoints: int = 37
    kSelectSurfaceEdge: int = 51
    kSelectSurfaceKnots: int = 49
    kSelectSurfaceParmPoints: int = 48
    kSelectSurfaceRange: int = 50
    kSelectSurfaces: int = 27
    kSelectTemplates: int = 69
    kSelectTextures: int = 25
    kSelectUVLocators: int = 24
    kSelectVertices: int = 41
    kSelectXYZLocators: int = 22
    def registerSelectionType(self, *args: Any, **kwargs: Any) -> Any:
        """registerSelectionType(selTypeName, priority=0) -> bool

        Registers a new selection type. It is perfectly legal for 2 plug-ins to register the same selection type.
        Currently we use the registration count. The selection type is deleted only when deregisterSelectionType() as been called the same number of times as this function - registerSelectionType().

        When registerSelectionType() is invoked and the selection type already exists, we neither enable it nor change its priority, just add its registration count by 1.
        The reason is the user might has modified these values after loading the plug-in that has register the selection type the first time.

        * selTypeName (string) - Name of the selection type.
        * priority (int) - Priority of the selection type.
        """

    def setMask(self, *args: Any, **kwargs: Any) -> Any:
        """setMask(mask) -> self
        setMask(selType) -> self

        Sets the selection mask to the specified selection mask or selection type.

        * mask (MSelectionMask) - the selection mask to be set.
        * selType (int) - the selection type to be set.  See addMask() for a list of valid selection masks.
        """


class MSpace(object):
    """Static class providing coordinate space constants."""
    kInvalid: int = 0
    kLast: int = 5
    kObject: int = 2
    kPostTransform: int = 3
    kPreTransform: int = 2
    kTransform: int = 1
    kWorld: int = 4

class MSyntax(object):
    """Syntax for commands."""
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def addArg(self, *args: Any, **kwargs: Any) -> Any:
        """Add a command argument."""

    def addFlag(self, *args: Any, **kwargs: Any) -> Any:
        """Add a flag and its arguments."""

    enableEdit: getset_descriptor = <attribute 'enableEdit' of 'OpenMaya.MSyntax' objects>
    enableQuery: getset_descriptor = <attribute 'enableQuery' of 'OpenMaya.MSyntax' objects>
    kAngle: int = 8
    kBoolean: int = 2
    kDistance: int = 7
    kDouble: int = 4
    kInvalidArgType: int = 0
    kInvalidObjectFormat: int = 0
    kLastArgType: int = 11
    kLastObjectFormat: int = 4
    kLong: int = 3
    kNoArg: int = 1
    kNone: int = 1
    kSelectionItem: int = 10
    kSelectionList: int = 3
    kString: int = 5
    kStringObjects: int = 2
    kTime: int = 9
    kUnsigned: int = 6
    def makeFlagMultiUse(self, *args: Any, **kwargs: Any) -> Any:
        """Set whether a flag may be used multiple times on the command line."""

    def makeFlagQueryWithFullArgs(self, *args: Any, **kwargs: Any) -> Any:
        """Set whether a flag requires its args when queried."""

    def maxObjects(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the maximum number of objects which can be passed to the command."""

    def minObjects(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the minimum number of objects which can be passed to the command."""

    def setMaxObjects(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the maximum number of objects which can be passed to the command."""

    def setMinObjects(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the minimum number of objects which can be passed to the command."""

    def setObjectType(self, *args: Any, **kwargs: Any) -> Any:
        """Set the type and number of objects to be passed to the command."""

    def useSelectionAsDefault(self, *args: Any, **kwargs: Any) -> Any:
        """If set to True then when no objects are provided on the command-line Maya will pass the current selection instead."""


class MTime(object):
    """Manipulate time data."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __itruediv__(self, value) -> Any:
        """Return self/=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __rtruediv__(self, value) -> Any:
        """Return value/self."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def __truediv__(self, value) -> Any:
        """Return self/value."""

    def asUnits(self, *args: Any, **kwargs: Any) -> Any:
        """Return the time value, converted to the specified units."""

    k100FPS: int = 25
    k10FPS: int = 18
    k1200FPS: int = 38
    k120FPS: int = 26
    k125FPS: int = 27
    k12FPS: int = 19
    k1500FPS: int = 39
    k150FPS: int = 28
    k15FPS: int = 5
    k16FPS: int = 20
    k2000FPS: int = 40
    k200FPS: int = 29
    k20FPS: int = 21
    k23_976FPS: int = 43
    k240FPS: int = 30
    k24FPS: int = 6
    k250FPS: int = 31
    k25FPS: int = 7
    k29_97DF: int = 45
    k29_97FPS: int = 44
    k2FPS: int = 12
    k3000FPS: int = 41
    k300FPS: int = 32
    k30FPS: int = 8
    k375FPS: int = 33
    k3FPS: int = 13
    k400FPS: int = 34
    k40FPS: int = 22
    k44100FPS: int = 48
    k47_952FPS: int = 46
    k48000FPS: int = 49
    k48FPS: int = 9
    k4FPS: int = 14
    k500FPS: int = 35
    k50FPS: int = 10
    k59_94FPS: int = 47
    k5FPS: int = 15
    k6000FPS: int = 42
    k600FPS: int = 36
    k60FPS: int = 11
    k6FPS: int = 16
    k750FPS: int = 37
    k75FPS: int = 23
    k80FPS: int = 24
    k8FPS: int = 17
    k90FPS: int = 50
    kFilm: int = 6
    kGames: int = 5
    kHours: int = 1
    kInvalid: int = 0
    kLast: int = 52
    kMilliseconds: int = 4
    kMinutes: int = 2
    kNTSCField: int = 11
    kNTSCFrame: int = 8
    kPALField: int = 10
    kPALFrame: int = 7
    kSeconds: int = 3
    kShowScan: int = 9
    kUserDef: int = 51
    def setUIUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Change the units used to display time in Maya's UI."""

    def ticksPerSecond(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the number of ticks per second, the smallest unit of time available."""

    def uiUnit(self, *args: Any, **kwargs: Any) -> Any:
        """Return the units used to display time in Maya's UI."""

    unit: getset_descriptor = <attribute 'unit' of 'OpenMaya.MTime' objects>
    value: getset_descriptor = <attribute 'value' of 'OpenMaya.MTime' objects>

class MTimeArray(object):
    """Array of MTime values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MTimeArray' objects>

class MTimeRange(object):
    """Mathematic type that represents a set of pseudo-real numbers (in units of time), such as [-1s, +1s] U [+2, +5s]"""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __or__(self, value) -> Any:
        """Return self|value."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __ror__(self, value) -> Any:
        """Return value|self."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def contains(self, *args: Any, **kwargs: Any) -> Any:
        """contains(MTime) -> boolcontains(MTime, MTime) -> bool

        Checks if the given time point or interval is contained in this time range.
        """

    def empty(self, *args: Any, **kwargs: Any) -> Any:
        """empty() -> bool

        Checks if this time range is an empty set
        """

    def intersects(self, *args: Any, **kwargs: Any) -> Any:
        """intersects(MTime, MTime) -> bool

        Checks if the given interval intersects with this time range.
        """


class MTimerMessage(MMessage):
    """Class used to register callbacks for timer related messages."""
    def addTimerCallback(self, *args: Any, **kwargs: Any) -> Any:
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


class MTransformationMatrix(object):
    """Manipulate the individual components of a transformation."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def asMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Interpolates between the identity transformation and that currently in the object, returning the result as an MMatrix."""

    def asMatrixInverse(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the inverse of the matrix representing the transformation."""

    def asRotateMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix which takes points from object space to the space immediately following the scale/shear/rotation transformations."""

    def asScaleMatrix(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the matrix which takes points from object space to the space immediately following scale and shear transformations."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns true if this transformation's matrix is within tolerance of another's matrix."""

    kIdentity: MTransformationMatrix = <OpenMaya.MTransformationMatrix object at 0x00000218AAE21B90>
    kInvalid: int = 0
    kLast: int = 7
    kTolerance: float = 1e-10
    kXYZ: int = 1
    kXZY: int = 4
    kYXZ: int = 5
    kYZX: int = 2
    kZXY: int = 3
    kZYX: int = 6
    def reorderRotation(self, *args: Any, **kwargs: Any) -> Any:
        """Reorders the transformation's rotate component to give the same overall rotation but using a new order or rotations."""

    def rotateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transformation's rotation component."""

    def rotateByComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Adds to the transformation's rotation component."""

    def rotatePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's rotate pivot component."""

    def rotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's rotate pivot translation component."""

    def rotation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's rotation component as either an Euler rotation or a quaternion."""

    def rotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the four components of the transformation's rotate component."""

    def rotationOrder(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the order of rotations when the transformation's rotate component is expressed as an euler rotation."""

    def rotationOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a quaternion which orients the local rotation space."""

    def scale(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transformation's scale components."""

    def scaleBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transformation's scale components by the three floats in the provided sequence."""

    def scalePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's scale pivot component."""

    def scalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's scale pivot translation component."""

    def setRotatePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate pivot component."""

    def setRotatePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate pivot translation component."""

    def setRotation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotation component."""

    def setRotationComponents(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate component from the four values in the provided sequence."""

    def setRotationOrientation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets a quaternion which orients the local rotation space."""

    def setScale(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's scale components to the three floats in the provided sequence."""

    def setScalePivot(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's scale pivot component."""

    def setScalePivotTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's scale pivot translation component."""

    def setShear(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's shear component."""

    def setToRotationAxis(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's rotate component to be a given axis vector and angle in radians."""

    def setTranslation(self, *args: Any, **kwargs: Any) -> Any:
        """Sets the transformation's translation component."""

    def shear(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a list containing the transformation's shear components."""

    def shearBy(self, *args: Any, **kwargs: Any) -> Any:
        """Multiplies the transformation's shear components by the three floats in the provided sequence."""

    def translateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Adds a vector to the transformation's translation component."""

    def translation(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the transformation's translation component as a vector."""


class MTypeId(object):
    """Stores a Maya object type identifier."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def id(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the type id as a long."""


class MURI(object):
    """Manipulate URIs."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def addQueryItem(self, *args: Any, **kwargs: Any) -> Any:
        """addQueryItem(key, value) -> self

        Add a key/value pair to the query string of the URI.
        """

    def asString(self, *args: Any, **kwargs: Any) -> Any:
        """asString() -> string

        Returns the string representation of the URI.
        """

    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear() -> self

        Clears the contents of the MURI object.
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy method. Assigns the value of one MURI to another.

        * source (MURI) - Existing MURI object to copy.
        """

    def getAllQueryItemKeys(self, *args: Any, **kwargs: Any) -> Any:
        """getAllQueryItemKeys() -> array

        Returns an array containing the keys from all query string pairs.
        """

    def getAllQueryItemValues(self, *args: Any, **kwargs: Any) -> Any:
        """getAllQueryItemValues(key) -> array

        Returns an array containing the values from all query string pairs which have a given key.
        """

    def getAuthority(self, *args: Any, **kwargs: Any) -> Any:
        """getAuthority() -> string

        Returns the authority component of the URI.
        """

    def getDirectory(self, *args: Any, **kwargs: Any) -> Any:
        """getDirectory() -> string

        Returns just the file directory portion of the URI, without the file name.
        """

    def getFileName(self, *args: Any, **kwargs: Any) -> Any:
        """getFileName(bool includeExtension=True) -> string

        Returns just the file name portion of the URI, with or without the extension.
        """

    def getFragment(self, *args: Any, **kwargs: Any) -> Any:
        """getFragment() -> string

        Returns the fragment component of the URI.
        """

    def getHost(self, *args: Any, **kwargs: Any) -> Any:
        """getHost() -> string

        Returns the host component of the URI.
        """

    def getPassword(self, *args: Any, **kwargs: Any) -> Any:
        """getPassword() -> string

        Returns the password component of the URI.
        """

    def getPath(self, *args: Any, **kwargs: Any) -> Any:
        """getPath() -> string

        Returns the path component of the URI.
        """

    def getPort(self, *args: Any, **kwargs: Any) -> Any:
        """getPort() -> int

        Returns the port component of the URI, or -1 if the port is not defined.
        """

    def getQueryItemValue(self, *args: Any, **kwargs: Any) -> Any:
        """getQueryItemValue(key) -> string

        Returns the value from the first query string pair in the URI which has a given key.
        """

    def getQueryPairDelimiter(self, *args: Any, **kwargs: Any) -> Any:
        """getQueryPairDelimiter() -> string

        Returns the character used to delimit between key-value pairs in the query string of the URI.
        """

    def getQueryValueDelimiter(self, *args: Any, **kwargs: Any) -> Any:
        """getQueryValueDelimiter() -> string

        Returns the character used to delimit keys and values in the query string of the URI.
        """

    def getScheme(self, *args: Any, **kwargs: Any) -> Any:
        """getScheme() -> string

        Returns the scheme of the URI.
        """

    def getUserInfo(self, *args: Any, **kwargs: Any) -> Any:
        """getUserInfo() -> string

        Returns the user info component of the URI.
        """

    def getUserName(self, *args: Any, **kwargs: Any) -> Any:
        """getUserName() -> string

        Returns the user name component of the URI.
        """

    def isEmpty(self, *args: Any, **kwargs: Any) -> Any:
        """isEmpty() -> bool

        Determines if the URI does not contain any data.
        """

    def isValid(self, *args: Any, **kwargs: Any) -> Any:
        """isValid() -> bool

        Determines if the URI is valid.
        """

    def isValidURI(self, *args: Any, **kwargs: Any) -> Any:
        """isValidURI(uri) -> bool

        Determines if a string value represents a valid URI.
        """

    def removeAllQueryItems(self, *args: Any, **kwargs: Any) -> Any:
        """removeAllQueryItems(int) -> self

        Removes all query string pairs having a given key from the URI.
        """

    def removeQueryItem(self, *args: Any, **kwargs: Any) -> Any:
        """removeQueryItem(int) -> self

        Removes the first query string pair with a given key from the URI.
        """

    def setAuthority(self, *args: Any, **kwargs: Any) -> Any:
        """setAuthority(string) -> self

        Set the authority portion of the URI.
        """

    def setDirectory(self, *args: Any, **kwargs: Any) -> Any:
        """setDirectory(string) -> self

        Sets just the directory portion of the URI (i.e. not including the filename).
        """

    def setFileName(self, *args: Any, **kwargs: Any) -> Any:
        """setFileName(string) -> self

        Sets just the filename portion of the URI (i.e. not including the directory).
        """

    def setFragment(self, *args: Any, **kwargs: Any) -> Any:
        """setFragment(string) -> self

        Sets the fragment component of the URI.
        """

    def setHost(self, *args: Any, **kwargs: Any) -> Any:
        """setHost(string) -> self

        Set the host component of the URI.
        """

    def setPassword(self, *args: Any, **kwargs: Any) -> Any:
        """setPassword(string) -> self

        Sets the password part of the user info component.
        """

    def setPath(self, *args: Any, **kwargs: Any) -> Any:
        """setPath(string) -> self

        Sets the path component of the URI.
        """

    def setPort(self, *args: Any, **kwargs: Any) -> Any:
        """setPort(int) -> self

        Set the port component of the URI.
        """

    def setQueryDelimiters(self, *args: Any, **kwargs: Any) -> Any:
        """setQueryDelimiters(valueDelimiter, pairDelimiter) -> self

        Sets the delimiter characters used in the query string of the URI.
        """

    def setScheme(self, *args: Any, **kwargs: Any) -> Any:
        """setScheme(string) -> self

        Sets the scheme component of the URI.
        """

    def setURI(self, *args: Any, **kwargs: Any) -> Any:
        """setURI(uri) -> self

        Initialize the MURI from a string value.
        """

    def setUserInfo(self, *args: Any, **kwargs: Any) -> Any:
        """setUserInfo(string) -> self

        Decomposes the userInfo string to fill out the userInfo-related component values.
        """

    def setUserName(self, *args: Any, **kwargs: Any) -> Any:
        """setUserName(string) -> self

        Sets the user name part of the user info component.
        """


class MUint64Array(object):
    """Array of MUint64 values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MUint64Array' objects>

class MUintArray(object):
    """Array of unsigned int values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MUintArray' objects>

class MUserData(object):
    """Virtual base class for user data caching.

    MUserData( deleteAfterUse=False, legacy=True )
    * deleteAfterUse (bool) - Enabled if user data should be deleted immediately after use. DEPRECATED in 2022. 
    * legacy (bool) - Enabled if legacy constructor arguments are used. DEPRECATED in 2022.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def deleteAfterUse(self, *args: Any, **kwargs: Any) -> Any:
        """deleteAfterUse() -> bool

        Returns whether or not this user data should be deleted immediately after use instead of being
        maintained until the internal owning object is deleted.

            DEPRECATED in 2022, deleteAfterUse is deprecated.
        """

    def setDeleteAfterUse(self, *args: Any, **kwargs: Any) -> Any:
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
    """Class used to register callbacks for user event messages."""
    def addUserEventCallback(self, *args: Any, **kwargs: Any) -> Any:
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

    def deregisterUserEvent(self, *args: Any, **kwargs: Any) -> Any:
        """deregisterUserEvent(eventName)

        Removes the event type with the given event name.  If callbacks have been
        registered with this event type, they will become invalid after a
        successful call to this method.

         * eventName (string) - the name of the new event to deregister.
        """

    def isUserEvent(self, *args: Any, **kwargs: Any) -> Any:
        """isUserEvent(eventName) -> bool

        Checks if an event type exists with the given event name.

         * eventName (string) - the name of the new event to check. 
        """

    def postUserEvent(self, *args: Any, **kwargs: Any) -> Any:
        """postUserEvent(eventName, clientData=None)

        Notifies all callbacks attached to the given event type of the occurence
        of the event.

        If clientData is specified, this data will be passed to all callbacks that
        receive the event.  If clientData is None (the default), the clientData
        registered with addUserEventCallback will be passed to the callbacks.


         * eventName (string) - the name of the new event.
         * clientData - User defined data.
        """

    def registerUserEvent(self, *args: Any, **kwargs: Any) -> Any:
        """registerUserEvent(eventName)

        Adds a new event type with the given string identifier.  The string
        identifier can then be used in all other MUserEventMessage methods to operate
        on the new event type.

         * eventName (string) - the name of the new event to register.  Any
           non-empty string may be used as an event name.
        """


class MUuid(object):
    """Manipulate UUID data."""
    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def asString(self, *args: Any, **kwargs: Any) -> Any:
        """asString() -> string

        Return the UUID as a string.
        """

    def copy(self, *args: Any, **kwargs: Any) -> Any:
        """copy(source) -> self

        Copy method. Assigns the value of one MUuid to another.

        * source (MUuid) - Existing MUuid object to copy.
        """

    def generate(self, *args: Any, **kwargs: Any) -> Any:
        """generate() -> self

        Generate a new UUID.
        """

    def valid(self, *args: Any, **kwargs: Any) -> Any:
        """valid() -> bool

        Return whether the UUID is valid.
        """


class MVector(object):
    """3D vector with double-precision coordinates."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __eq__(self, value) -> Any:
        """Return self==value."""

    def __ge__(self, value) -> Any:
        """Return self>=value."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __gt__(self, value) -> Any:
        """Return self>value."""

    def __iadd__(self, value) -> Any:
        """Return self+=value."""

    def __imul__(self, value) -> Any:
        """Return self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __isub__(self, value) -> Any:
        """Return self-=value."""

    def __itruediv__(self, value) -> Any:
        """Return self/=value."""

    def __le__(self, value) -> Any:
        """Return self<=value."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __lt__(self, value) -> Any:
        """Return self<value."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __ne__(self, value) -> Any:
        """Return self!=value."""

    def __neg__(self) -> Any:
        """-self"""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __radd__(self, value) -> Any:
        """Return value+self."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __rsub__(self, value) -> Any:
        """Return value-self."""

    def __rtruediv__(self, value) -> Any:
        """Return value/self."""

    def __rxor__(self, value) -> Any:
        """Return value^self."""

    def __setitem__(self, key, value) -> Any:
        """Set self[key] to value."""

    def __str__(self) -> Any:
        """Return str(self)."""

    def __sub__(self, value) -> Any:
        """Return self-value."""

    def __truediv__(self, value) -> Any:
        """Return self/value."""

    def __xor__(self, value) -> Any:
        """Return self^value."""

    def angle(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the angle, in radians, between this vector and another."""

    def isEquivalent(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within a given tolerance of being equal."""

    def isParallel(self, *args: Any, **kwargs: Any) -> Any:
        """Returns True if this vector and another are within the given tolerance of being parallel."""

    kOneVector: MVector = (1, 1, 1)
    kTolerance: float = 1e-10
    kWaxis: int = 3
    kXaxis: int = 0
    kXaxisVector: MVector = (1, 0, 0)
    kXnegAxisVector: MVector = (-1, 0, 0)
    kYaxis: int = 1
    kYaxisVector: MVector = (0, 1, 0)
    kYnegAxisVector: MVector = (0, -1, 0)
    kZaxis: int = 2
    kZaxisVector: MVector = (0, 0, 1)
    kZeroVector: MVector = (0, 0, 0)
    kZnegAxisVector: MVector = (0, 0, -1)
    def length(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the magnitude of this vector."""

    def normal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector containing the normalized version of this one."""

    def normalize(self, *args: Any, **kwargs: Any) -> Any:
        """Normalizes this vector in-place and returns a new reference to it."""

    def rotateBy(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the vector resulting from rotating this one by the given amount."""

    def rotateTo(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the quaternion which will rotate this vector into another."""

    def transformAsNormal(self, *args: Any, **kwargs: Any) -> Any:
        """Returns a new vector which is calculated by postmultiplying this vector by the transpose of the given matrix's inverse and then normalizing the result."""

    x: getset_descriptor = <attribute 'x' of 'OpenMaya.MVector' objects>
    y: getset_descriptor = <attribute 'y' of 'OpenMaya.MVector' objects>
    z: getset_descriptor = <attribute 'z' of 'OpenMaya.MVector' objects>

class MVectorArray(object):
    """Array of MVector values."""
    def __add__(self, value) -> Any:
        """Return self+value."""

    def __contains__(self, key) -> Any:
        """Return key in self."""

    def __delitem__(self, key) -> Any:
        """Delete self[key]."""

    def __getitem__(self, key) -> Any:
        """Return self[key]."""

    def __iadd__(self, value) -> Any:
        """Implement self+=value."""

    def __imul__(self, value) -> Any:
        """Implement self*=value."""

    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __len__(self) -> Any:
        """Return len(self)."""

    def __mul__(self, value) -> Any:
        """Return self*value."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    def __repr__(self) -> Any:
        """Return repr(self)."""

    def __rmul__(self, value) -> Any:
        """Return value*self."""

    def __setitem__(self, key, value) -> Any:
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

    sizeIncrement: getset_descriptor = <attribute 'sizeIncrement' of 'OpenMaya.MVectorArray' objects>

class MWeight(object):
    """Methods for accessing component weight data. This class is currently
    only used to access soft select and symmetry selection weights.
    Other weight data (e.g. deformer weights) does not use this class
    and can be accessed through the corresponding MFn class or directly
    from the node's attributes.

    __init__()
    Initializes a new MWeight object with influence weight of 1 and seam
    weight of 0.
    __init__(MWeight src)
    Initializes a new MWeight object with the same value as src.
    """
    def __init__(self, *args, **kwargs) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""

    def __new__(*args, **kwargs) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""

    influence: getset_descriptor = <attribute 'influence' of 'OpenMaya.MWeight' objects>
    seam: getset_descriptor = <attribute 'seam' of 'OpenMaya.MWeight' objects>

def getStringResource(*args: Any, **kwargs: Any) -> Any: ...
def registerStringResource(*args: Any, **kwargs: Any) -> Any: ...
def registerStringResources(*args: Any, **kwargs: Any) -> Any: ...
