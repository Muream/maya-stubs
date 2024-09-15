from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def movieInfo(arg0: str = ..., /, *, counter: bool = ..., dropFrame: bool = ..., frameCount: bool = ..., frameDuration: bool = ..., height: bool = ..., movieTexture: bool = ..., negTimesOK: bool = ..., numFrames: bool = ..., quickTime: bool = ..., timeCode: bool = ..., timeCodeTrack: bool = ..., timeScale: bool = ..., twentyFourHourMax: bool = ..., width: bool = ...) -> bool:
    """movieInfo provides a mechanism for querying information about movie
    files.movie, imageplane, avi, quicktime
    Args:
        counter (bool?): Query the 'counter' flag of the movie's timecode format.  
                If this is true, the timecode returned by the -timeCode flag will be a simple counter.  
                If false, the returned timecode will be an array of integers (hours, minutes, seconds, frames).  
                Properties: create
        dropFrame (bool?): Query the 'drop frame' flag of the movie's timecode format.  
                Properties: create
        frameCount (bool?): Query the number of frames in the movie file  
                Properties: create
        frameDuration (bool?): Query the frame duration of the movie's timecode format.  
                Properties: create
        height (bool?): Query the height of the movie  
                Properties: create
        movieTexture (bool?): If set, the string argument is interpreted as the name of a movie texture node,  
                and the command then operates on the movie loaded by that node.  
                Properties: create
        negTimesOK (bool?): Query the 'neg times OK' flag of the movie's timecode format.  
                Properties: create
        numFrames (bool?): Query the whole number of frames per second of the movie's timecode format.  
                Properties: create
        quickTime (bool?): Query whether the movie is a QuickTime movie.  
                Properties: create
        timeCode (bool?): Query the timecode of the current movie frame.  
                Properties: create
        timeCodeTrack (bool?): Query whether the movie has a timecode track.  
                Properties: create
        timeScale (bool?): Query the timescale of the movie's timecode format.  
                Properties: create
        twentyFourHourMax (bool?): Query the '24 hour max' flag of the movie's timecode format.  
                Properties: create
        width (bool?): Query the width of the movie  
                Properties: create

    Returns:
        bool:

    Example:
    """

