from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def wrinkle(*args: str, axis: Tuple[float, float, float] = ..., branchCount: int = ..., branchDepth: int = ..., center: Tuple[float, float, float] = ..., crease: Multiuse[str] = ..., dropoffDistance: float = ..., envelope: float = ..., randomness: float = ..., style: str = ..., thickness: float = ..., uvSpace: Tuple[float, float, float, float, float] = ..., wrinkleCount: int = ..., wrinkleIntensity: float = ...) -> List[str]:
    """The wrinkle command is used to create a network of wrinkles on a surface.
    It automatically creates a network of wrinkle curves that control a wire
    deformer. The wrinkle curves are attached to a cluster deformer.
    Args:
        axis (Tuple[float, float, float]?): Specifies the plane of the wrinkle.  
                Properties: create
        branchCount (int?): Specifies the number of branches per wrinkle. Default is 2.  
                Properties: create
        branchDepth (int?): Specifies the depth of the branching. Default is 0.  
                Properties: create
        center (Tuple[float, float, float]?): Specifies the center of the wrinkle.  
                Properties: create
        crease (Multiuse[str]?): Specifies an existing curve to serve as the wrinkle.  
                Properties: create, multiuse
        dropoffDistance (float?): Specifies the dropoff distance around the center.  
                Properties: create
        envelope (float?): The envelope globally attenuates the amount of deformation. Default is 1.0.  
                Properties: create
        randomness (float?): Amount of randomness. Default is 0.2.  
                Properties: create
        style (str?): Specifies the wrinkle style. Valid values are "radial" or "tangential"  
                Properties: create
        thickness (float?): Wrinkle thickness. Default is 1.0.  
                Properties: create
        uvSpace (Tuple[float, float, float, float, float]?): 1/2 length, 1/2 breadth, rotation angle, center u, v  
                definition of a patch in uv space where the wrinkle is  
                to be constructed.  
                Properties: create
        wrinkleCount (int?): Specifies the number of wrinkle lines to be generated.  
                Default is 3.  
                Properties: create
        wrinkleIntensity (float?): Increasing the intensity makes it more wrinkly. Default is 0.5.  
                Properties: create

    Returns:
        List[str]: List of clusters created followed by list of wire deformers created.

    Example:
    """

