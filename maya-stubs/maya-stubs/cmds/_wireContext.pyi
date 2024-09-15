from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def wireContext(*args: Any, edit: bool = ..., query: bool = ..., crossingEffect: Queryable[float] = ..., deformationOrder: Queryable[str] = ..., dropoffDistance: Queryable[float] = ..., envelope: Queryable[float] = ..., exclusive: bool = ..., exclusivePartition: Queryable[str] = ..., exists: bool = ..., groupWithBase: bool = ..., history: bool = ..., holder: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., localInfluence: Queryable[float] = ..., name: str = ...) -> Union[str, float, bool]:
    """This command creates a tool that can be used to
    create a wire deformer.
    Args:
        crossingEffect (Queryable[float]?): Set the amount of convolution filter effect. Varies from fully  
                convolved at 0 to a simple additive effect at 1.  
                Default is 0.  
                Properties: create, query, edit
        deformationOrder (Queryable[str]?): Set the appropriate flag that determines the position in  
                in the deformation hierarchy.  
                Properties: create, query, edit
        dropoffDistance (Queryable[float]?): Set the dropoff Distance for the wires.  
                Properties: create, query, edit
        envelope (Queryable[float]?): Set the envelope value for the deformer. Default is 1.0  
                Properties: create, query, edit
        exclusive (bool?): Set exclusive mode on or off.  
                Properties: create, query, edit
        exclusivePartition (Queryable[str]?): Set the name of an exclusive partition.  
                Properties: create, query, edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        groupWithBase (bool?): Groups the wire with the base wire so that they can easily be moved  
                together to create a ripple effect.  
                Default is false.  
                Properties: create, query, edit
        history (bool?): If this is a tool command, turn the construction history on  
                for the tool in question.  
                Properties: create
        holder (bool?): Controls whether the user can specify holders for the wires  
                from the wire context. A holder is a curve that you can use to limit  
                the wire's deformation region. Default is false.  
                Properties: create, edit
        image1 (Queryable[str]?): First of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image2 (Queryable[str]?): Second of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        image3 (Queryable[str]?): Third of three possible icons representing the tool  
                associated with the context.  
                Properties: create, query, edit
        localInfluence (Queryable[float]?): Set the amount of local influence a wire has with respect  
                to other wires.  
                Default is 0.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create

    Returns:
        str: The name of the context created

    Example:
    """

