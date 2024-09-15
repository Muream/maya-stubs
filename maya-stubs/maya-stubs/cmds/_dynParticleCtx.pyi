from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dynParticleCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., conserve: Queryable[float] = ..., cursorPlacement: bool = ..., exists: bool = ..., grid: bool = ..., gridSpacing: Queryable[float] = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., jitterRadius: Queryable[float] = ..., lowerLeftX: Queryable[float] = ..., lowerLeftY: Queryable[float] = ..., lowerLeftZ: Queryable[float] = ..., name: str = ..., nucleus: bool = ..., numJitters: Queryable[int] = ..., particleName: Queryable[str] = ..., sketch: bool = ..., sketchInterval: Queryable[int] = ..., textPlacement: bool = ..., upperRightX: Queryable[float] = ..., upperRightY: Queryable[float] = ..., upperZ: Queryable[float] = ...) -> Union[bool, float, str, int]:
    """The particle context command creates a particle context. The particle
    context provides an interactive means to create particle
    objects. The particle context command also provides an interactive
    means to set the option values, through the Tool Property Sheet, for
    the "particle" command that the context will issue.
    Args:
        conserve (Queryable[float]?): Conservation of momentum control (between 0 and 1). For smaller  
                values, the field will tend to erase any existing velocity the object  
                has (in other words, will not conserve momentum from frame to frame).  
                A value of 1 (the default) corresponds to the true physical law  
                of conservation of momentum.  
                Properties: query, edit
        cursorPlacement (bool?): Use the cursor to place the lower left and upper right of the grid.  
                Properties: query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        grid (bool?): Create a particle grid.  
                Properties: query, edit
        gridSpacing (Queryable[float]?): Spacing between particles in the grid.  
                Properties: query, edit
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
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
        jitterRadius (Queryable[float]?): Max radius from the center to place the particle instances.  
                Properties: query, edit
        lowerLeftX (Queryable[float]?): Lower left X position of the particle grid.  
                Properties: query, edit
        lowerLeftY (Queryable[float]?): Lower left Y position of the particle grid.  
                Properties: query, edit
        lowerLeftZ (Queryable[float]?): Lower left Z position of the particle grid.  
                Properties: query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        nucleus (bool?): If set true then an nParticle is generated with a nucleus node connection.  
                Otherwise a standard particle is created.  
                Properties: query, edit
        numJitters (Queryable[int]?): Number of jitters (instances) per particle.  
                Properties: query, edit
        particleName (Queryable[str]?): Particle name.  
                Properties: query, edit
        sketch (bool?): Create particles in sketch mode.  
                Properties: query, edit
        sketchInterval (Queryable[int]?): Interval between particles, when in sketch mode.  
                Properties: query, edit
        textPlacement (bool?): Use the textfields to specify the lower left and upper right of/  
                the grid.  
                Properties: query, edit
        upperRightX (Queryable[float]?): Upper right X position of the particle grid.  
                Properties: query, edit
        upperRightY (Queryable[float]?): Upper right Y position of the particle grid.  
                Properties: query, edit
        upperZ (Queryable[float]?): Upper right Z position of the particle grid.  
                Properties: query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

