from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def dollyCtx(arg0: str = ..., /, *, edit: bool = ..., query: bool = ..., alternateContext: bool = ..., boxDollyType: Queryable[str] = ..., centerOfInterestDolly: bool = ..., dollyTowardsCenter: bool = ..., exists: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., localDolly: bool = ..., name: str = ..., orthoZoom: bool = ..., scale: Queryable[float] = ..., toolName: Queryable[str] = ...) -> Union[str, bool, float]:
    """This command can be used to create, edit, or query a dolly
    context.
    Args:
        alternateContext (bool?): Set the ALT+MMB and ALT+SHIFT+MMB to refer to this context.  
                Properties: create, query
        boxDollyType (Queryable[str]?): Set the behavior of where the camera's center of interest is  
                set to after the box dolly. In surface mode, the center  
                of interest will be snapped to the surface point at the center  
                of the marquee. In bbox mode, the closest bounding box  
                to the camera will be used. Bounding box mode will use the  
                selection mask to determine which objects to include into the  
                calculation.  
                Properties: create, query, edit
        centerOfInterestDolly (bool?): Set the translate the camera's center of interest. Left and  
                right drag movements with the mouse will translate the center  
                of interest towards or away respectively from the camera. The  
                center of interest can be snapped to objects by using the left  
                mouse button for selection. The default select mask will be  
                used.  
                Properties: create, query, edit
        dollyTowardsCenter (bool?): Dolly towards center (if true), else dolly towards point where  
                user clicks in the view.  
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
        localDolly (bool?): Dolly with respect to the camera's center of interest. The  
                camera will not pass through the center of interest. Local  
                dolly only applies to perspective cameras.  
                Properties: create, query, edit
        name (str?): If this is a tool command, name the tool appropriately.  
                Properties: create
        orthoZoom (bool?): Zoom orthographic view (if true), else dolly orthographic camera.  
                Default value is true.  
                Properties: create, query, edit
        scale (Queryable[float]?): The sensitivity for dollying the camera.  
                Properties: create, query, edit
        toolName (Queryable[str]?): Name of the specific tool to which this command refers.  
                Properties: create, query

    Returns:
        str: The name of the context

    Example:
    """

