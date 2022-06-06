# fmt: off
from typing_extensions import Self

from .OpenMaya_generated import *


class MDagPath(object):
    def __delattr__(self: Self, name: Any) -> Any:
        """Implement delattr(self, name)."""
    def __dir__(self: Self) -> Any:
        """Default dir() implementation."""
    __doc__: str = ...
    def __eq__(self: Self, value: Any) -> Any:
        """Return self==value."""
    def __format__(self: Self, format_spec: Any) -> Any:
        """Default object formatter."""
    def __ge__(self: Self, value: Any) -> Any:
        """Return self>=value."""
    def __getattribute__(self: Self, name: Any) -> Any:
        """Return getattr(self, name)."""
    def __gt__(self: Self, value: Any) -> Any:
        """Return self>value."""
    __hash__: NoneType = ...
    def __init__(self: Self, args: Any, kwargs: Any) -> Any:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __init_subclass__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
    def __le__(self: Self, value: Any) -> Any:
        """Return self<=value."""
    def __lt__(self: Self, value: Any) -> Any:
        """Return self<value."""
    def __ne__(self: Self, value: Any) -> Any:
        """Return self!=value."""
    def __new__(self: Self, args: Any, kwargs: Any) -> Any:
        """Create and return a new object.  See help(type) for accurate signature."""
    def __reduce__(self: Self) -> Any:
        """Helper for pickle."""
    def __reduce_ex__(self: Self, protocol: Any) -> Any:
        """Helper for pickle."""
    def __repr__(self: Self) -> Any:
        """Return repr(self)."""
    def __setattr__(self: Self, name: Any, value: Any) -> Any:
        """Implement setattr(self, name, value)."""
    def __sizeof__(self: Self) -> Any:
        """Size of object in memory, in bytes."""
    def __str__(self: Self) -> Any:
        """Return str(self)."""
    def __subclasshook__(self: Self, *args: Any, **kwargs: Any) -> Any:
        """Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
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

