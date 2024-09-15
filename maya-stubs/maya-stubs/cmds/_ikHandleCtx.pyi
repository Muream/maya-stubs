from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def ikHandleCtx(*args: Any, edit: bool = ..., query: bool = ..., autoPriorityH: bool = ..., createCurve: bool = ..., createRootAxis: bool = ..., exists: bool = ..., forceSolverH: bool = ..., history: bool = ..., image1: Queryable[str] = ..., image2: Queryable[str] = ..., image3: Queryable[str] = ..., name: str = ..., numSpans: int = ..., parentCurve: bool = ..., poWeightH: Queryable[float] = ..., priorityH: Queryable[int] = ..., rootOnCurve: bool = ..., rootTwistMode: bool = ..., simplifyCurve: bool = ..., snapCurve: bool = ..., snapHandleH: bool = ..., solverTypeH: Queryable[str] = ..., stickyH: Queryable[str] = ..., twistType: str = ..., weightH: Queryable[float] = ...) -> Union[str, bool, float, int]:
    """The ikHandle context command (ikHandleCtx) updates parameters of
    ikHandle tool.  The options for the tool will be set to the flags that
    the user specifies.
    Args:
        autoPriorityH (bool?): Specifies that this handle's priority is assigned  
                automatically.  
                C: The default is off.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        createCurve (bool?): Specifies if a curve should be automatically created  
                for the ikSplineHandle. The flag is ignored in the ikHandleCtx.  
                C: The default is on.   
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        createRootAxis (bool?): Specifies if a root transform should automatically  
                be created above the joints affected by the ikSplineHandle.  
                This option is used to prevent the  
                root flipping singularity on a motion path. This flag is ignored in  
                the ikHandleCtx.  
                C: The default is off.   
                Q: When queried, this flag returns an int.  
                Properties: edit
        exists (bool?): Returns true or false depending upon whether the  
                specified object exists. Other flags are ignored.  
                Properties: create
        forceSolverH (bool?): Specifies if the ikSolver is enabled for the ikHandle.  
                C: The default is on.   
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
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
        numSpans (int?): Specifies the number of spans in the automatically generated  
                curve of the ikSplineHandle. This flag is ignored in the  
                ikHandleCtx.  
                C: The default is 1.   
                Q: When queried, this flag returns an int.  
                Properties: edit
        parentCurve (bool?): Specifies if the curve should automatically be parented to the  
                parent of the first joint affected by the ikSplineHandle. The  
                flag is ignored in the ikHandleCtx.  
                C: The default is on.   
                Q: When queried, this flag returns an int.  
                Properties: edit
        poWeightH (Queryable[float]?): Specifies the position/orientation weight of the  
                ikHandle.  
                C: The default is 1.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit
        priorityH (Queryable[int]?): Specifies the priority of the ikHandle.  
                C: The default is 1.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        rootOnCurve (bool?): Specifies if the root is locked onto the curve  
                of the ikSplineHandle. This flag is ignored in the ikHandleCtx.   
                C: The default is on.   
                Q: When queried, this flag returns an int.  
                Properties: edit
        rootTwistMode (bool?): Specifies whether the start joint is allowed to twist or not.  
                If not, then the required twist is distributed over the  
                remaining joints. This applies to all the twist types.  
                This flag is ignored in the ikHandleCtx.   
                C: The default is off.   
                Q: When queried, this flag returns an int.  
                Properties: edit
        simplifyCurve (bool?): Specifies if the ikSplineHandle curve should be simplified.  
                This flag is ignored in the ikHandleCtx.  
                C: The default is on.   
                Q: When queried, this returns an int.  
                Properties: edit
        snapCurve (bool?): Specifies if the curve should automatically snap  
                to the first joint affected by the ikSplineHandle. This flag is  
                ignored in the ikHandleCtx.  
                C: The default is off.   
                Q: When queried, this flag returns an int.  
                Properties: edit
        snapHandleH (bool?): Specifies if the ikHandle snapping is on.  
                C: The default is on.  
                Q: When queried, this flag returns an int.  
                Properties: create, query, edit
        solverTypeH (Queryable[str]?): Lists what ikSolver is being used. The  
                ikSplineSolver may not be selected. To use an ikSplineSolver  
                use the ikSplineHandleCtx command.   
                C: The default solver is the default set by the user preferences.  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        stickyH (Queryable[str]?): Specifies if the ikHandle is sticky or not. Valid strings  
                are "sticky" and "off".  
                C: The default is "off".  
                Q: When queried, this flag returns a string.  
                Properties: create, query, edit
        twistType (str?): Specifies the type of interpolation to be used by the  
                ikSplineHandle. This flag is ignored in the ikHandleCtx.  
                The interpolation options are "linear", "easeIn", "easeOut", and  
                "easeInOut".   
                C: The default is "linear".   
                Q: When queried, this flag returns a string.  
                Properties: edit
        weightH (Queryable[float]?): Specifies the weight of the ikHandle.  
                C: The default is 1.  
                Q: When queried, this flag returns a float.  
                Properties: create, query, edit

    Returns:
        str: Context name

    Example:
    """

