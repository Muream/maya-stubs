from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def commandPort(arg0: str = ..., /, *, query: bool = ..., bufferSize: int = ..., close: bool = ..., echoOutput: bool = ..., listPorts: bool = ..., name: str = ..., noreturn: bool = ..., pickleOutput: bool = ..., prefix: str = ..., returnNumCommands: bool = ..., securityWarning: bool = ..., sourceType: str = ...) -> bool:
    """Opens or closes the Maya command port. The command port comprises a socket
    to which a client program may connect. An example command port client
    "mcp" is included in the Motion Capture developers kit.It supports multi-byte commands and uses utf-8 as its transform
    format. It will receive utf8 command string and decode it to Maya native
    coding. The result will also be encoded to utf-8 before sending back.Care should be taken regarding INET domain sockets as no user
    identification, or authorization is required to connect to a given
    socket, and all commands (including "system(...)") are allowed and
    executed with the user id and permissions of the Maya user. The prefix
    flag can be used to reduce this security risk, as only the prefix
    command is executed.The query flag can be used to determine if a given command port exists.
    See examples below.
    Args:
        bufferSize (int?): Commands and results are each subject to size limits. This option allows  
                the user to specify the size of the buffer used to communicate with Maya. If  
                unspecified the default buffer size is 4096 characters.  
                Commands longer than bufferSize characters will cause the client connection to close.  
                Results longer that bufferSize characters are replaced with an error message.  
                Properties: create
        close (bool?): Closes the commandPort, deletes the pipes  
                Properties: create
        echoOutput (bool?): Sends a copy of all command output to the command port. Typically  
                only the result is transmitted. This option provides a copy of  
                all output.  
                Properties: create
        listPorts (bool?): Returns the available ports  
                Properties: create
        name (str?): Specifies the name of the command port which this command  
                creates. CommandPort names of the form name create a  
                UNIX domain socket on the localhost corresponding to  
                name. If name does not begin with "/",  
                then /tmp/name is used. If name begins  
                with "/", name denotes the full path to the socket.   
                Names of the form :port number create an INET domain  
                on the local host at the given port.  
                Properties: create
        noreturn (bool?): Do not write the results from executed commands back to the  
                command port socket. Instead, the results from executed  
                commands are written to the script editor window. As no information  
                passes back to the command port client regarding the execution  
                of the submitted commands, care must be taken not to overflow  
                the command buffer, which would cause the connection to close.  
                Properties: create
        pickleOutput (bool?): Python output will be pickled.  
                Properties: create
        prefix (str?): The string argument is the name of a Maya command taking one string  
                argument. This command is called each time data is sent to the command  
                port. The data written to the command port is passed as the argument to  
                the prefix command. The data from the command port is encoded as with  
                enocodeString and enclosed in quotes.   
                If newline characters are embedded in the command port data,  
                the input is split into individual lines.  
                These lines are treated as if they were separate  
                writes to the command port. Only the result to the last  
                prefix command is returned.  
                Properties: create
        returnNumCommands (bool?): Ignore the result of the command, but return the number of  
                commands that have been read and executed in this call. This  
                is a simple way to track buffer overflow. This flag is ignored  
                when the noreturn flag is specified.  
                Properties: create
        securityWarning (bool?): Enables security warning on command port input.  
                Properties: create
        sourceType (str?): The string argument is used to indicate which source type  
                would be passed to the commandPort, like "mel", "python".  
                The default source type is "mel".  
                Properties: create

    Returns:
        bool: - in query mode

    Example:
    """

