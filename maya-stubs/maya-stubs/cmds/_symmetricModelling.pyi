from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def symmetricModelling(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., about: Queryable[str] = ..., allowPartial: bool = ..., axis: Queryable[str] = ..., preserveSeam: Queryable[int] = ..., reset: bool = ..., seamFalloffCurve: Queryable[str] = ..., seamTolerance: Queryable[float] = ..., symmetry: Queryable[int] = ..., tolerance: Queryable[float] = ..., topoSymmetry: bool = ...) -> Union[bool, str, int, float]:
    """This command allows you to change the symmetric modelling options.Symmetric modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.
    Args:
        about (Queryable[str]?): Set the space in which symmetry should be calculated (object or world or topo).  
                When queried, returns a string which is the current space being used.  
                Properties: create, query, edit
        allowPartial (bool?): Specifies whether partial symmetry should be allowed when enabling topological symmetry.  
                Properties: create, query, edit
        axis (Queryable[str]?): Set the current axis to be reflected over.  
                When queried, returns a string which is the current axis.  
                Properties: create, query, edit
        preserveSeam (Queryable[int]?): Controls whether selection or symmetry should take priority on the plane  
                of symmetry.  
                When queried, returns an int for the option.  
                Properties: create, query, edit
        reset (bool?): Reset the redo information before starting.  
                Properties: create, edit
        seamFalloffCurve (Queryable[str]?): Set the seam's falloff curve, used to control the seam strength within the  
                seam tolerance. The string is a comma separated list of sets of 3 values  
                for each curve point.  
                When queried, returns a string which is the current space being used.  
                Properties: create, query, edit
        seamTolerance (Queryable[float]?): Set the seam tolerance used for reflection. When preserveSeam is enabled, this  
                tolerance controls the width of the enforced seam.  
                When queried, returns a float of the seamTolerance.  
                Properties: create, query, edit
        symmetry (Queryable[int]?): Set the symmetry option on or off.  
                When queried, returns an int for the option.  
                Properties: create, query, edit
        tolerance (Queryable[float]?): Set the tolerance of reflection.  
                When queried, returns a float of the tolerance.  
                Properties: create, query, edit
        topoSymmetry (bool?): Enable/disable topological symmetry.  
                When enabled, the supplied component/active list will be used to define the topological symmetry seam.  
                When queried, returns the name of the active topological symmetry object.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

