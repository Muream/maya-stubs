from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def defineDataServer(*args: Any, device: str = ..., server: str = ..., undefine: bool = ...) -> bool:
    """Connects to the specified data servername, creating a named device which
    then can be attached to device handlers.When the device is defined, it queries queries the server for data axis
    information.  The "CapChannels" present are represented as axis in form
    "channelName"."usage" for scalar channels and "channelName"."component"
    for compound channels. Seeto list axis names.Note that undoingdoes not break the connection with the data server until it cannot be
    redone.  Executing any other command (sphere for example) will cause
    this to occur.  Similarly, the commanddoes not break the connection with the data server until it cannot be
    undone.  Either flushUndo, or the 'defineDataServer' command falling"
    off the end of the undo queue causes this to occur, and the connection.
    to be broken.No return value.
    Args:
        device (str?): specified the device name to be given to the server connection.  
                device name must be unique or the command fails.  
                Properties: create
        server (str?): specifies the name of the server with which the define  
                device connects, and can be specifiied in two ways  
              
              
                name -- the name of the server socket  
                Server names of the form name connect to the  
                server socket on the localhost corresponding to  
                name.  If name does not begin with "/",  
                then /tmp/name is used. This is the default behavior  
                of most servers. If name begins with "/",  
                name denotes the full path to the socket.   
                host:service - a udp service  
                on the specified host.  
                The service can be any one of a "udp service name,"  
                a "port number," or a named service of "tcpmux," and they are  
                found in that order. If  
                host is omitted, the localhost is used.   
              
                In any case, if the server cannot be found, the device is not  
                defined (created) and the command fails.  
                Properties: create
        undefine (bool?): undefines (destroys) the dataServer device, closing the connection  
                with the server.  
                Properties: create

    Returns:
        bool:

    Example:
    """

