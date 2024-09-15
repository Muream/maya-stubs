from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditor(*args: Any, query: bool = ..., allClips: str = ..., clipId: Multiuse[int] = ..., commonParentTrack: bool = ..., composition: str = ..., drivingClipsForAttr: str = ..., drivingClipsForObj: Tuple[str, int] = ..., includeParent: bool = ..., mute: bool = ..., selectedClips: str = ..., topLevelClips: str = ...) -> Union[str, bool]:
    """General Time Editor commandstimeEditor, nle
    Args:
        allClips (str?): Return an exhaustive (recursive) list of all clip IDs from the active composition.  
                Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:  
              
                 roster   
                 container   
                 group  
                Properties: create
        clipId (Multiuse[int]?): ID of the clip to be edited.  
                Properties: create, multiuse
        commonParentTrack (bool?): Locate the common parent track node and track index of the given clip IDs.  
                Requires a list of clip IDs to be specified using the clipId flag.  
                The format of the returned string is "track_node:track_index". If the clips specified  
                are on the same track node but in different track indexes, only the track node  
                will be returned.  
                Properties: create
        composition (str?): A flag to use in conjunction with -dca/drivingClipsForObj to indicate the name of composition to use.  
                By default if this flag is not provided, current active composition will be used.  
                Properties: create
        drivingClipsForAttr (str?): Return a list of clips driving the specified attribute(s).  
                If the composition is not specified, current active composition will be used.  
                Properties: create
        drivingClipsForObj (Tuple[str, int]?): Return a list of clips driving the specified object(s) with an integer value indicating the matching mode.  
                If no object is specified explicitly, the selected object(s) will be used.  
                Objects that cannot be driven by clips are ignored.  
                If the composition is not specified, current active composition will be used.  
                Default match mode is 0.  
              
                0. Include only the clip that has an exact match  
                1. Include any clip that contains all of the specified objects  
                2. Include any clip that contains any of the specified objects  
                3. Include all clips that do not include any of the specified objects  
                Properties: create
        includeParent (bool?): A toggle flag to use in conjunction with -dca/drivingClipsForObj.  
                When toggled, parent clip is included in selection (the entire hierarchy will be selected).  
                Properties: create
        mute (bool?): Mute/unmute Time Editor.  
                Properties: create, query
        selectedClips (str?): Return a list of clip IDs of currently selected Time Editor clips.  
                Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:  
              
                 roster   
                 container   
                 group  
                Properties: create
        topLevelClips (str?): Return a list of all top-level clip IDs from the active composition.  
                Arguments may be used to filter the returning result. An empty string will return clip IDs for all clip types:  
              
                 roster   
                 container   
                 group  
                Properties: create

    Returns:
        str: Command result

    Example:
    """

