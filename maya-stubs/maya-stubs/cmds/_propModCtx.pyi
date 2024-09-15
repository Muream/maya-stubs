from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def propModCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., animCurve: Queryable[str] = ..., animCurveFalloff: Queryable[Tuple[float, float]] = ..., animCurveParam: Queryable[str] = ..., direction: Queryable[Tuple[float, float, float]] = ..., exists: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., linear: Queryable[float] = ..., linearParam: Queryable[Tuple[float, float]] = ..., nurbsCurve: Queryable[str] = ..., powerCutoff: Queryable[float] = ..., powerCutoffParam: Queryable[Tuple[float, float]] = ..., powerDegree: Queryable[float] = ..., powerDegreeParam: Queryable[float] = ..., script: Queryable[str] = ..., scriptParam: Queryable[str] = ..., type: Queryable[int] = ..., worldspace: bool = ...) -> Union[str, Tuple[float, float], Tuple[float, float, float], float, int, bool]:
    """Controls the proportional move context.
    Args:
        animCurve (Queryable[str]?): Name of the anim curve to use as a drop-off curve.  
                Only the 0. > side of the curve will be used and the distance  
                will be mapped to "seconds".  The profile of the curve will be  
                used as the profile for propmod function.  
                Properties: create, query, edit
        animCurveFalloff (Queryable[Tuple[float, float]]?): The profile of the curve will be used as the profile for propmod function in  
                both U and V. This will be scaled in U, V according to the paramters provided.  
                The ratio of the U, V scaling parameters will dictate the footprint of the fuction  
                while the curve itself provides the magnitudes.  
                Properties: create, query, edit
        animCurveParam (Queryable[str]?): Name of the anim curve to use as a drop-off curve.  
                Only the 0. > side of the curve will be used and the distance  
                will be mapped to "seconds", where 1 second maps to 0.01 units  
                in parametric space.  
                Properties: create, query, edit
        direction (Queryable[Tuple[float, float, float]]?): Direction along which to compute the distance for  
                the distance based drop-off functions.  The default is (1 1 1)  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        linear (Queryable[float]?): If using linear drop-off function, this is its  
                slope.  The default of -0.1 means the point at the locator  
                moves with it and the point 10 units away doesn't move at all.  
                Properties: create, query, edit
        linearParam (Queryable[Tuple[float, float]]?): If using parametric linear drop-off function, these specify  
                its limits along the U and V directions.  
                Properties: create, query, edit
        nurbsCurve (Queryable[str]?): Name of the nurbs curve to use as a drop-off curve.  
                The closest point distance would be used as the drop off percentage.  
                Properties: create, query, edit
        powerCutoff (Queryable[float]?): If using the power drop-off function, this is its  
                distance cutoff value.  The default is 10.0.  
                Properties: create, query, edit
        powerCutoffParam (Queryable[Tuple[float, float]]?): If using the power drop-off function, these specify  
                one of it's limits, 0 for U, and 1 and V.  The default cutoff is 10.0.  
                Properties: create, query, edit
        powerDegree (Queryable[float]?): If using the power drop-off function, this is its  
                degree.  The default is 3.  
                Properties: create, query, edit
        powerDegreeParam (Queryable[float]?): If using the power drop-off function, this is its  
                degree.  The default is 3.  
                Properties: create, query, edit
        script (Queryable[str]?): The name of the script to use to compute the drop-off.  
                The script takes 6 floats as input - first 3 are the position of  
                the move locator, the next 3 the position of the point to be  
                manipulated.  The script should return a drop-off coefficient  
                which could be negative or zero.  
                Properties: create, query, edit
        scriptParam (Queryable[str]?): The name of the script to use to compute the drop-off.  
                The script takes 4 floats as input - first 2 are the parametric  
                position of the move locator, the next 2 the parametric position of  
                the point to be manipulated.  The script should return a drop-off coefficient  
                which could be negative or zero.  
                Properties: create, query, edit
        type (Queryable[int]?): Choose the type for the drop-off function.  Legal  
                values are 1 for linear, 2 for power,  
                3 for script,  
                4 for anim curve.  
                The default is 1.  
                Properties: create, query, edit
        worldspace (bool?): Set the space in which the tool works. True for  
                world space, false for parametric space.  
                Properties: create, query, edit

    Returns:
        str: Name of the new context created

    Example:
    """

