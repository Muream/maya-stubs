from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def colorAtPoint(*args: str, coordU: Multiuse[float] = ..., coordV: Multiuse[float] = ..., maxU: float = ..., maxV: float = ..., minU: float = ..., minV: float = ..., output: str = ..., samplesU: int = ..., samplesV: int = ...) -> bool:
    """Thecommand is used to query textures or ocean
              shaders at passed in uv coordinates.
          (For ocean shaders uv is x and z in worldspace ).
              The return value is a floating point array whose size is
              determined by either the number of input uv arguments passed in and the
              the queried value.  One can query alpha only, rgb only, or rgba values.
              The returned array is only single indexed, so if rgb is specified then
              the index for red values would be index * 3. Blue is index * 3 + 1, and
              green is index * 3 + 2. For rgba use a multiple of 4 instead of 3.
              For alpha only one can simply use the index.
              There are two basic argument formats that may be used:
              colorAtPoint -u 0 -v 0   -u .2 -v .1  etc.. for all points
              or
              colorAtPoint -mu 0 -mv 0  -xu 1 -xv 1 -su 10 -sv 10 // samples 100 points
              If one is sampling several points and they are all in a regular grid
              formation it is more efficient to call this routine with the latter
              method, which uses a min/max uv and number of samples, rather than
              a long argument list of uv coords.texture, color, alpha, uv, ocean, outColor, paramUV
    Args:
        coordU (Multiuse[float]?): Input u coordinate to sample texture at.  
                Properties: create, multiuse
        coordV (Multiuse[float]?): Input v coordinate to sample texture at.  
                Properties: create, multiuse
        maxU (float?): DEFAULT 1.0  
                Maximum u bounds to sample.  
                Properties: create
        maxV (float?): DEFAULT 1.0  
                Maximum v bounds to sample.  
                Properties: create
        minU (float?): DEFAULT 0.0  
                Minimum u bounds to sample.  
                Properties: create
        minV (float?): DEFAULT 0.0  
                Minimum v bounds to sample.  
                Properties: create
        output (str?): Type of data to output:  
                        A        = alpha only  
                        RGB  = color only  
                        RGBA = color and alpha  
                Properties: create
        samplesU (int?): DEFAULT 1  
                The number of points to sample in the U dimension.  
                Properties: create
        samplesV (int?): DEFAULT 1  
                The number of points to sample in the V dimension.  
                Properties: create

    Returns:
        bool:

    Example:
    """

