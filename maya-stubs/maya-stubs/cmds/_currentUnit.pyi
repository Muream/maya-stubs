from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def currentUnit(*args: str, query: bool = ..., angle: Queryable[str] = ..., fullName: bool = ..., linear: Queryable[str] = ..., time: Queryable[str] = ..., updateAnimation: bool = ...) -> Union[str, bool]:
    """This command allows you to change the units in which you will work
    in Maya. There are three types of units: linear, angular and time.The current unit affects how all commands in Maya interpret their
    numeric values. For example, if the current linear unit is,
    then the command:will be interpreted as moving 5cm in X, -2cm in Y, 3cm in Z, and as
    creating a sphere with radius 4cm. Similarly, if the current time unit
    is Film (24 frames per second), then the command:will be interpreted as setting the current time to frame 6 in the Film
    unit, which is 6/24 or 0.25 seconds.You can always override the unit of a particular numeric value to a
    command be specifying it one the command. For example, using the above
    examples:would move the object 5 meters in X, -2 millimeters in Y, 3 centimeters
    in Z, create a sphere of radius 4 inches, and change the current time
    to 6 frames in the NTSC unit, which would be 0.2 seconds, or 4.8 frames
    in the current (Film) unit.
    Args:
        angle (Queryable[str]?): Set the current angular unit. Valid strings are:  
              
                [deg | degree | rad | radian]  
              
                When queried, returns a string which is the current angular unit  
                Properties: create, query
        fullName (bool?): A query only flag. When specified in conjunction with any of  
                the -linear/-angle/-time flags, will return the long form of the unit.  
                For example, mm and millimeter are the same unit, but  
                the former is the short form of the unit name, and the latter is the  
                long form of the unit name.  
                Properties: query
        linear (Queryable[str]?): Set the current linear unit. Valid strings are:  
              
                [mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]  
              
                When queried, returns a string which is the current linear unit  
                Properties: create, query
        time (Queryable[str]?): Set the current time unit. Valid strings are:  
              
                [hour | min | sec | millisec | game | film | pal | ntsc | show | palf | ntscf | 23.976fps | 29.97fps | 29.97df | 47.952fps | 59.94fps | 44100fps | 48000fps]  
              
                When queried, returns a string which is the current time unit  
              
                Note that there is no long form for any of the time units.  
                The non-seconds based time units are interpreted as the following  
                frames per second:  
              
                game: 15 fps  
                film: 24 fps  
                pal: 25 fps  
                ntsc: 30 fps  
                show: 48 fps  
                palf: 50 fps  
                ntscf: 60 fps  
                Properties: create, query
        updateAnimation (bool?): An edit only flag.  When specified in conjunction with the -time  
                flag indicates that times for keys are not updated.  By default when the  
                current time unit is changed, the times for keys are modified so that  
                playback timing is preserved.  For example a key set a frame 12film is  
                changed to frame 15ntsc when the current time unit is changed to ntsc,  
                since they both represent a key at a time of 0.5 seconds.  Specifying  
                -updateAnimation false would leave the key at frame 12ntsc.  
                Default is -updateAnimation true.  
                Properties: create

    Returns:
        str: The new current unit that has been set

    Example:
    """

