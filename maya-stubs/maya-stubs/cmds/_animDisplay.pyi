from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def animDisplay(*, edit: bool = ..., query: bool = ..., modelUpdate: Queryable[str] = ..., refAnimCurvesEditable: bool = ..., timeCode: Queryable[str] = ..., timeCodeOffset: Queryable[str] = ...) -> Union[bool, str]:
    """This command changes certain display options used by
    animation windows.
    Args:
        modelUpdate (Queryable[str]?): Controls how changes to animCurves are propagated through the  
                dependency graph. Valid modes are "none", "interactive" or  
                "delayed". If modelUpdate is "none" then changing an  
                animCurve will not cause the model to be updated (change currentTime  
                in order to update the model).  If modelUpdate is "interactive" (which  
                is the default setting), then as interactive changes are being made  
                to the animCurve, the model will be updated.  If modelUpdate is  
                delayed, then the model is updated once the final change to an  
                animCurve has been made.  With modelUpdate set to  
                either "interactive" or "delayed", changes  
                to animCurves made via commands will also cause the  
                model to be updated.  
                Properties: create, query, edit
        refAnimCurvesEditable (bool?): Specify if animation curves from referenced files are  
                editable.  
                Properties: create, query, edit
        timeCode (Queryable[str]?): Controls how time value are display. Valid values are "frame", "timecode", "fulltimecode".  
                If the value is "frame" maya will display time in frame everywhere.  
                If the value is "timecode" maya will display time in timecode in time  
                slider, graph editor and dope sheet.  
                If the value is "fulltimecode" maya will display time in timecode everywhere.  
                Properties: create, query, edit
        timeCodeOffset (Queryable[str]?): This flag has now been deprecated.  It still exists to not break  
                legacy scripts, but it will now do nothing.  See the new timeCode  
                command to set and query timeCodes.  
                Properties: create, query, edit

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

