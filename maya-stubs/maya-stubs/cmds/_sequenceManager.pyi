from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def sequenceManager(*, edit: bool = ..., query: bool = ..., addSequencerAudio: str = ..., attachSequencerAudio: str = ..., currentShot: Queryable[str] = ..., currentTime: Queryable[int] = ..., listSequencerAudio: str = ..., listShots: bool = ..., modelPanel: Queryable[str] = ..., node: Queryable[str] = ..., writableSequencer: Queryable[str] = ...) -> Union[bool, str, int]:
    """The sequenceManager command manages sequences, shots, and their related scenes.shot, sequence
    Args:
        addSequencerAudio (str?): Add an audio clip to the sequencer by specifying a filename  
                Properties: create
        attachSequencerAudio (str?): Add an audio clip to the sequencer by specifying an audio node  
                Properties: create
        currentShot (Queryable[str]?): Returns the shot that is being used at the current sequence time.  
                Properties: query
        currentTime (Queryable[int]?): Set the current sequence time  
                Properties: create, query
        listSequencerAudio (str?): List the audio clips added to the sequencer  
                Properties: create
        listShots (bool?): List all the currently defined shots across all scene segments  
                Properties: create
        modelPanel (Queryable[str]?): Sets a dedicated modelPanel to be used as the panel that the sequencer will control.  
                Properties: create, query
        node (Queryable[str]?): Returns the SequenceManager node, of which there is only ever one.  
                Properties: query
        writableSequencer (Queryable[str]?): Get the writable sequencer node.  Create it if it doesn't exist.  
                Properties: query

    Returns:
        bool: In query mode, return type is based on queried flag.

    Example:
    """

