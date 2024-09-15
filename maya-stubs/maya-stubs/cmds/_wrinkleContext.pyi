from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def wrinkleContext(*args: Any, edit: bool = ..., query: bool = ..., branchCount: Queryable[int] = ..., branchDepth: Queryable[int] = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., randomness: Queryable[float] = ..., style: Queryable[str] = ..., thickness: Queryable[float] = ..., wrinkleCount: Queryable[int] = ..., wrinkleIntensity: Queryable[float] = ...) -> Union[str, int, float]:
    """This command creates a context that creates wrinkles.
    Args:
        branchCount (Queryable[int]?): Set the number of branches spawned from a crease for radial wrinkles.  
                Default is 2.  
                Properties: create, query, edit
        branchDepth (Queryable[int]?): Set the depth of branching for radial wrinkles.  
                Defaults to 0.  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
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
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        randomness (Queryable[float]?): Set the deviation of the wrinkle creases from straight lines and  
                other elements of the wrinkle structure.  
                Defaults to 0.2.  
                Properties: create, query, edit
        style (Queryable[str]?): Set the wrinkle characteristic shape."lines"|"radial"|"custom.  
                Default is "radial".  
                Properties: create, query, edit
        thickness (Queryable[float]?): Set the thickness of wrinkle creases by setting the dropoff  
                distance on the underlying wires.  
                Properties: create, query, edit
        wrinkleCount (Queryable[int]?): Set the number of wrinkle creases.  
                Default is 3.  
                Properties: create, query, edit
        wrinkleIntensity (Queryable[float]?): Set the depth intensity of the wrinkle furrows.  
                Defaults to 0.5.  
                Properties: create, query, edit

    Returns:
        str: The name of the context created

    Example:
    """

