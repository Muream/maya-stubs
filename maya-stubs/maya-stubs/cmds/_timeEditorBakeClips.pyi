from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def timeEditorBakeClips(*args: Any, edit: bool = ..., query: bool = ..., bakeToAnimSource: str = ..., bakeToClip: str = ..., clipId: Multiuse[int] = ..., combineLayers: bool = ..., forceSampling: bool = ..., keepOriginalClip: bool = ..., path: Multiuse[str] = ..., sampleBy: int = ..., targetTrackIndex: int = ..., targetTracksNode: str = ...) -> int:
    """This command is used to bake Time Editor clips and to blend them into a single clip.
    Args:
        bakeToAnimSource (str?): Bake/merge the selected clips into the animation source.  
                Properties: create
        bakeToClip (str?): Bake/merge the selected clips into a clip.  
                Properties: create
        clipId (Multiuse[int]?): Clip IDs of the clips to bake.  
                Properties: create, multiuse
        combineLayers (bool?): Combine the layers of the input clip.  
                Properties: create
        forceSampling (bool?): Force sampling on the whole time range when baking.  
                Properties: create
        keepOriginalClip (bool?): Keep the source clips after baking.  
                Properties: create
        path (Multiuse[str]?): Full path of clips on which to operate. For example: composition1|track1|group; composition1|track1|group|track2|clip1.  
                Properties: create, multiuse
        sampleBy (int?): Sampling interval when baking crossfades and timewarps.  
                Properties: create
        targetTrackIndex (int?): Specify the target track when baking containers.  
                If targetTrackIndex is specified, the track index within the specified node is used.  
                If targetTrackIndex is not specified or is the default value (-1), the track index within the current node is used.  
                If targetTrackIndex is -2, a new track will be created.  
                Properties: create
        targetTracksNode (str?): Target tracks node when baking containers.  
                Properties: create

    Returns:
        int: Command result

    Example:
    """

