from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def bevelPlus(*args: str, edit: bool = ..., query: bool = ..., bevelInside: bool = ..., capSides: Queryable[int] = ..., constructionHistory: bool = ..., innerStyle: Queryable[int] = ..., joinSurfaces: bool = ..., name: str = ..., normalsOutwards: bool = ..., numberOfSides: Queryable[int] = ..., outerStyle: Queryable[int] = ..., polygon: int = ..., range: bool = ...) -> Union[List[str], bool, int]:
    """The bevelPlus command creates a new bevel surface for the specified
    curves using a given style curve. The first curve should be the
    "outside" curve, and the (optional) rest of them should be inside of
    the first one. For predictable results, the curves should be planar
    and all in the same plane.
    Args:
        bevelInside (bool?): If true, ensure surface always remains within the original profile curve  
                Default: false  
                Properties: create, query, edit
        capSides (Queryable[int]?): How to cap the bevel.  
              
                1. no caps  
                2. cap at start only  
                3. cap at end only  
                4. cap at start and end  
              
                Default:4  
                Properties: create, query
        constructionHistory (bool?): Turn the construction history on or off.  
                Properties: create
        innerStyle (Queryable[int]?): Similar to outerStyle, this style is applied to all  
                but the first (outer) curve specified.  
                Properties: create, query, edit
        joinSurfaces (bool?): Attach bevelled surfaces into one surface for each  
                input curve.  
                Default:true  
                Properties: create, query, edit
        name (str?): Sets the name of the newly-created node. If it contains  
                namespace path, the new node will be created under the  
                specified namespace; if the namespace does not exist, it  
                will be created.  
                Properties: create
        normalsOutwards (bool?): If enabled, the normals point outwards on the  
                resulting NURBS or poly surface.  
                Properties: create, query, edit
        numberOfSides (Queryable[int]?): How to apply the bevel.  
              
                1. no bevels  
                2. bevel at start only  
                3. bevel at end only  
                4. bevel at start and end  
              
                Default: 4  
                Properties: create, query, edit
        outerStyle (Queryable[int]?): Choose a style to use for the bevel of the first (outer)  
                curve.  There are 15 predefined styles (values 0 to 14 can be used  
                to select them). For those experienced with MEL, you can, after  
                the fact, specify a custom curve and use it for the style curve.  
                See the documentation for styleCurve node to see what requirements  
                a style curve must satisfy.  
                Properties: create, query, edit
        polygon (int?): The value of this argument controls the type of the object  
                created by this operation  
              
                 0. nurbs surface  
                 1. polygon (use nurbsToPolygonsPref to set the parameters for the conversion)  
                 2. subdivision surface (use nurbsToSubdivPref to set the parameters for the conversion)  
                 3. Bezier surface  
                 4. subdivision surface solid (use nurbsToSubdivPref to set the  
                parameters for the conversion)  
                Properties: create
        range (bool?): Force a curve range on complete input curve.  
                Properties: create

    Returns:
        List[str]: Object name(s) and node name

    Example:
    """

