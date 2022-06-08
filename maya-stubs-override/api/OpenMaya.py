# fmt: off
from __future__ import annotations


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

class MFnBase:
    def hasObj(self: Self, type: int | MObject) -> bool:
        """Returns True if the function set is compatible with the specified Maya object."""
    def object(self: Self) -> MObject:
        """Returns a reference to the object to which the function set is currently attached, or MObject.kNullObj if none."""
    def setObject(self: Self, object: MObject) -> Self:
        """Attaches the function set to the specified Maya object."""
    def type(self: Self) -> int:
        """Returns the type of the function set."""


class MFnDependencyNode(MFnBase):
    pass


class MFnDagNode(MFnDependencyNode):
    def fullPathName(self: Self) -> str:
        """Returns the full path of the attached object, from the root of the DAG on down."""
