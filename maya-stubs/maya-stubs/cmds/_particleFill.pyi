from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def particleFill(*args: str, closePacking: bool = ..., doubleWalled: bool = ..., maxX: float = ..., maxY: float = ..., maxZ: float = ..., minX: float = ..., minY: float = ..., minZ: float = ..., particleDensity: float = ..., resolution: int = ...) -> bool:
    """This command generates an nParticle system that fills the selected object with a grid of particles.particle
    Args:
        closePacking (bool?): If this is on then the particles are positioned as closely as possible in a hexagonal close packing arrangement.  
                Otherwise particles are packed in a uniform grid lattice.  
                Properties: create
        doubleWalled (bool?): This flag should be used if the thickness of the object to fill has been modeled( for example a mug ).  
                Otherwise the particles will be created inside the wall. Note that doubleWalled will not  
                handle some cases very well. For example a double walled donut shape may get the center  
                region of the donut filled. In cases like this it may be better to make the internal wall a  
                separate mesh then fill that without using doubleWalled.  
                Properties: create
        maxX (float?): The fill max bounds of the particles in X relative to the X bounds of the object.  
                A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.  
                Properties: create
        maxY (float?): The fill max bounds of the particles in Y relative to the Y bounds of the object.  
                A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.  
                Properties: create
        maxZ (float?): The fill max bounds of the particles in Z relative to the Z bounds of the object.  
                A value of zero is totally empty and one is totally full. The default value is 1, or fully filled.  
                Properties: create
        minX (float?): The fill lower bounds of the particles in X relative to the X bounds of the object.  
                A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.  
                Properties: create
        minY (float?): The fill lower bounds of the particles in Y relative to the Y bounds of the object.  
                A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.  
                Properties: create
        minZ (float?): The fill lower bounds of the particles in Z relative to the Z bounds of the object.  
                A value of zero is totally full and one is totally empty. The default value is 0, or fully filled.  
                Properties: create
        particleDensity (float?): This controls the size of the particles. At a value of 1.0 the particle size will exactly match the  
                grid spacing determined by the resolution parameter and the object bounds. Particles which overlap  
                the surface will be rejected even if the center of the particle is inside.  
                Properties: create
        resolution (int?): This determines the total number of particles generated.  
                It represent the resolution along the largest axis of the object's bounding box.  
                For a cube shape the total potential particles will be the cube of the resolution.  
                For other shapes it will be less.  
                The default value for this flag is 10, so 1000 particles could be generated for a cube shape.  
                Properties: create

    Returns:
        bool:

    Example:
    """

