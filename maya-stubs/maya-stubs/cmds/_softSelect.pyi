from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def softSelect(*args: str, edit: bool = ..., query: bool = ..., compressUndo: Queryable[int] = ..., enableFalseColor: Queryable[int] = ..., softSelectColorCurve: Queryable[str] = ..., softSelectCurve: Queryable[str] = ..., softSelectDistance: Queryable[float] = ..., softSelectEnabled: Queryable[int] = ..., softSelectFalloff: Queryable[int] = ..., softSelectReset: bool = ..., softSelectUVDistance: Queryable[float] = ...) -> Union[bool, int, str, float]:
    """This command allows you to change the soft modelling options.Soft modelling is an option that allows for reflection of basic
    manipulator actions such as move, rotate, and scale.
    Args:
        compressUndo (Queryable[int]?): Controls how soft selection settings behave in undo:  
              
                0 means all changes undo individually  
                1 means all consecutive changes undo as a group  
                2 means only interactive changes undo as a group  
              
                When queried, returns an int indicating the current undo behaviour.  
                Properties: create, query, edit
        enableFalseColor (Queryable[int]?): Set soft select color feedback on or off.  
                When queried, returns an int indicating whether color feedback  
                is currently enabled.  
                Properties: create, query, edit
        softSelectColorCurve (Queryable[str]?): Sets the color ramp used to display false color feedback for soft selected  
                components in the viewport. The color curve is encoded as a string of comma  
                separated floating point values representing the falloff curve CVs. Each  
                CV is represented by 5 successive values: 3 RGB values (the color to use),  
                an input value (the selection weight), and a curve interpolation type.  
                When queried, returns a string containing the encoded CVs of the current  
                color feedback curve.  
                Properties: create, query, edit
        softSelectCurve (Queryable[str]?): Sets the falloff curve used to calculate selection weights for components  
                within the falloff distance. The curve is encoded as a string of comma  
                separated floating point values representing the falloff curve CVs. Each  
                CV is represented by 3 successive values: an output value (the selection  
                weight at this point), an input value (the normalised falloff distance)  
                and a curve interpolation type.  
                When queried, returns a string containing the encoded CVs of the current  
                falloff curve.  
                Properties: create, query, edit
        softSelectDistance (Queryable[float]?): Sets the falloff distance (radius) used for world and object space soft selection.  
                When queried, returns a float indicating the current falloff distance.  
                Properties: create, query, edit
        softSelectEnabled (Queryable[int]?): Sets soft selection based modeling on or off.  
                When queried, returns an int indicating the current state of the option.  
                Properties: create, query, edit
        softSelectFalloff (Queryable[int]?): Sets the falloff mode:  
              
                0 for volume based falloff  
                1 for surface based falloff  
                2 for global falloff  
              
                When queried, returns an int indicating the falloff mode.  
                Properties: create, query, edit
        softSelectReset (bool?): Resets soft selection to its default settings.  
                Properties: create, edit
        softSelectUVDistance (Queryable[float]?): Sets the falloff distance (radius) used for UV space soft selection.  
                When queried, returns a float indicating the current falloff distance.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

