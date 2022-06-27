# pylint: skip-file
from typing import *

from maya.api.OpenMaya import (
    MDAGDrawOverrideInfo,
    MDagPath,
    MDagPathArray,
    MEulerRotation,
    MFnDependencyNode,
    MMatrix,
    MObject,
    MQuaternion,
    MSpace,
    MVector,
)
from typing_extensions import Self

class MObject:
    def __eq__(self, value: object) -> bool:
        """Return self==value."""
    def __ge__(self, value: object) -> bool:
        """Return self>=value."""
    def __gt__(self, value: object) -> bool:
        """Return self>value."""
    def __le__(self, value: object) -> bool:
        """Return self<=value."""
    def __lt__(self, value: object) -> bool:
        """Return self<value."""
    def __ne__(self, value: object) -> bool:
        """Return self!=value."""
    def __new__(cls: type[Self]) -> Self:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, src: MObject) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def apiType(self) -> int:
        """Returns the function set type for the object.

        Returns:
            MFn type constant.
            Returns a constant indicating the type of the internal Maya object.
            If the MObject is null MFn.kInvalid will be returned.
        """
    @property
    def apiTypeStr(self) -> Any:
        """(readonly) String containing the object's type name."""
    @apiTypeStr.setter
    def apiTypeStr(self, value) -> Any:
        """(readonly) String containing the object's type name."""
    def hasFn(self, fn: int) -> bool:
        """Tests whether object is compatible with the specified function set.

        Args:
            fn: MFn type constant

        Returns:
            Returns True if the internal Maya object supports the specified function set specified by fn.
        """
    def isNull(self) -> bool:
        """Tests whether there is an internal Maya object.

        Returns:
            Returns True if the MObject is not referring to any Maya internal object
            (i.e. it is equivalent to kNullObj).
        """
    kNullObj: MObject = ...

class MDagPath:
    def apiType(self) -> int:
        """Returns the type of the object at the end of the path."""
    def child(self, childNum: int) -> MObject:
        """Returns the specified child of the object at the end of the path."""
    def childCount(self) -> int:
        """Returns the number of objects parented directly beneath the object at the end of the path."""
    def exclusiveMatrix(self) -> MMatrix:
        """Returns the matrix for all transforms in the path, excluding the end object."""
    def exclusiveMatrixInverse(self) -> MMatrix:
        """Returns the inverse of exclusiveMatrix()."""
    def extendToShape(self, shapeNum: int = ...) -> str:
        """Extends the path to the specified shape node parented directly beneath the transform at the current end of the path."""
    def fullPathName(self) -> str:
        """Returns a string representation of the path from the DAG root to the path's last node."""
    def getAPathTo(self, node: MObject) -> MDagPath:
        """Returns the first path found to the given node."""
    def getAllPathsTo(self, node: MObject) -> MDagPathArray:
        """Returns all paths to the given node."""
    def getDisplayStatus(self) -> int:
        """Returns the display status for this path."""
    def getDrawOverrideInfo(self) -> MDAGDrawOverrideInfo:
        """Returns the draw override information for this path."""
    def getPath(self, pathNum: int = ...) -> MDagPath:
        """Returns the specified sub-path of this path."""
    def hasFn(self, type: int) -> bool:
        """Returns True if the object at the end of the path supports the given function set."""
    def inclusiveMatrix(self) -> MMatrix:
        """Returns the matrix for all transforms in the path, including the end object, if it is a transform."""
    def inclusiveMatrixInverse(self) -> MMatrix:
        """Returns the inverse of inclusiveMatrix()."""
    def instanceNumber(self) -> int:
        """Returns the instance number of this path to the object at the end."""
    def isInstanced(self) -> bool:
        """Returns True if the object at the end of the path can be reached by more than one path."""
    def isTemplated(self) -> bool:
        """Returns true if the DAG Node at the end of the path is templated."""
    def isValid(self) -> bool:
        """Returns True if this is a valid path."""
    def isVisible(self) -> bool:
        """Returns true if the DAG Node at the end of the path is visible."""
    def length(self) -> int:
        """Returns the number of nodes on the path, not including the DAG's root node."""
    def node(self) -> MObject:
        """Returns the DAG node at the end of the path."""
    def numberOfShapesDirectlyBelow(self) -> int:
        """Returns the number of shape nodes parented directly beneath the transform at the end of the path."""
    def partialPathName(self) -> str:
        """Returns the minimum string representation which will uniquely identify the path."""
    def pathCount(self) -> int:
        """Returns the number of sub-paths which make up this path."""
    def pop(self, nom: int = ...) -> Self:
        """Removes objects from the end of the path."""
    def push(self, child: MObject) -> Self:
        """Extends the path to the specified child object, which must be parented directly beneath the object currently at the end of the path."""
    def set(self, path: MDagPath) -> Self:
        """Replaces the current path held by this object with another."""
    def transform(self) -> MObject:
        """Returns the last transform node on the path."""

class MFnBase:
    def hasObj(self, type: int | MObject) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self, object: MObject) -> Self:
        """Attaches the function set to the specified Maya object."""
    def type(self) -> int:
        """Returns the type of the function set."""

class MFnDagNode(MFnDependencyNode):
    def fullPathName(self) -> str:
        """Returns the full path of the attached object, from the root of the DAG on down."""
    def transformationMatrix(self) -> MMatrix: ...

class MTransformationMatrix:
    @overload
    def rotation(self, asQuaternion: Literal[True]) -> MQuaternion: ...
    @overload
    def rotation(self, asQuaternion: Literal[False] = ...) -> MEulerRotation:
        """Returns the transform's rotation as an MEulerRotation or MQuaternion."""
    def translation(self, space: MSpace) -> MVector:
        """Returns the transformation's translation component as a vector."""

class MFnTransform(MFnDagNode):
    def translation(self, space: MSpace) -> MVector: ...
    def setTranslation(self, trans: MVector, space: MSpace) -> Self: ...
    @overload
    def rotation(
        self,
        space: MSpace = ...,
        asQuaternion: Literal[True] = ...,
    ) -> MQuaternion: ...
    @overload
    def rotation(
        self,
        space: MSpace = ...,
        asQuaternion: Literal[False] = ...,
    ) -> MEulerRotation: ...
    def setRotation(self, rot: MEulerRotation | MQuaternion, space: MSpace) -> Self: ...
