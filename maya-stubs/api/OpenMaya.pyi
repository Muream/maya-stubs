# fmt: off
from typing_extensions import Self

from .OpenMaya_generated import *


class MDagPath:
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
    __hash__: NoneType = ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
    def __str__(self: Self) -> Any:
        """Return str(self)."""
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


class MFnBase:
    __doc__: str = ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def hasObj(self: Self, type: int) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    @overload
    def hasObj(self: Self, object: MObject) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""

    def object(self: Self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self: Self, object: MObject) -> Self:
        """Attaches the function set to the specified Maya object."""
    def type(self: Self) -> int:
        """Returns the type of the function set."""


class MFnDependencyNode(MFnBase):
    __doc__: str = ...
    @overload
    def __init__(self: Self) -> None: ...
    @overload
    def __init__(self: Self, node: MObject) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
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
    __doc__: str = ...
    @overload
    def __init__(self: Self, node: MObject) -> None: ...
    @overload
    def __init__(self: Self, path: MDagPath) -> None: ...
    @overload
    def __init__(self: Self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
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
