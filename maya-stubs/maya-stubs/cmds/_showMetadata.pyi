from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def showMetadata(*args: str, query: bool = ..., auto: bool = ..., dataType: Queryable[str] = ..., interpolation: bool = ..., isActivated: bool = ..., listAllStreams: bool = ..., listMembers: bool = ..., listValidMethods: bool = ..., listVisibleStreams: bool = ..., member: Queryable[str] = ..., method: Queryable[str] = ..., off: bool = ..., range: Queryable[Tuple[float, float]] = ..., rayScale: Queryable[float] = ..., stream: Queryable[str] = ...) -> Union[str, bool, Tuple[float, float], float]:
    """This command is used to show metadata values which is in the
    specified channels "vertex", "edge", "face", and "vertexFace" in
    the viewport. You can view the data by three ways:For example, if the metadata of "shape.vtx[1]" is (1, 0, 0), you can turn on
    the visualization with all three modes.
    On "color" mode, you can see a red vertex which is on the position of "shape.vtx[1]".
    On "ray" mode, you can see a ray with the direction (1, 0, 0).
    On "string" mode, you can see strings "1 0 0" below the vertex in the viewport.To use "color" or "ray" mode, you should make the member of the data structure
    with three or less items, such as float[3]. The three items are mapped to "RGB" as a color, or "XYZ"
    as a vector. The structure with two items works similarly. The only difference
    is that the third value will always be zero.
    However, if the structure has only one item, the value is mapped to all three variables.
    That means if the structure is "int" and its value is 1, the color will be white(1, 1, 1)
    and the vector will be (1, 1, 1).You can get the current status of the flags on the query mode (using "-query").
    But you can query only the status of one flag in a single command and
    you cannot set values on the query mode.You can use the command on some specified objects, or run it with no arguments
    to make changes on all objects in the scene. The object must be a mesh shape.
    Components are not allowed as the command arguments.metadata, component, stream, channel, association
    Args:
        auto (bool?): Similar to the flag "-range", but uses the min/max value from the metadata in the same stream  
                and member instead of the specified input value.  
                In query mode, you can use the flag to query if "auto" is on.  
                Properties: create, query
        dataType (Queryable[str]?): In create mode, when used with the flags "stream" and "member",  
                specify a member to show.  
                If the flag "off" is used, specify the member to turn off.  
                In query mode, when used with the flags "stream" and "member", query  
                the visualization state of the specified member.  
                Only one member of each shape can be visualized at a time.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        interpolation (bool?): In create mode, enable/disable interpolation for "color" method.  
                When interpolation is on, the components will be displayed in the interpolated color,  
                which is computed by averaging their metadata values.  
                In query mode, query the current state of interpolation flag of  
                the selected objects.  
                Properties: create, query
        isActivated (bool?): Used to check if the given stream is activated.  
                If some shapes are selected, query their states.  
                If no shape is selected, query the states of all shapes  
                in the scene.  
                Properties: create, query
        listAllStreams (bool?): Used with object names to list all streams of the specified objects.  
                no matter if they are visible in the viewport.  
                Or you can use the flag individually to list all streams in the scene.  
                Due to the fact that different objects may have the same stream name,  
                the returned list will merge the duplicated stream names automatically.  
                Properties: create, query
        listMembers (bool?): Used with the flag 'stream' to get the  
                member list in the specified stream.  
                Properties: create, query
        listValidMethods (bool?): List the valid visual methods that can be set for the current stream and member. Some data type cannot be displayed  
                by some methods. For example, if the data type is "string", it cannot be displayed by "color" or by "ray".  
                In other words, only the method "string" will be returned when you list the methods.  
                Properties: create, query
        listVisibleStreams (bool?): Used with object names to list the name of the current visible streams of  
                the specified object. Or you can use the flag with no object name to list  
                all visible streams in the scene.  
                Properties: create, query
        member (Queryable[str]?): In create mode, when used with the flags "stream" and "dataType",  
                specify a member to show.  
                If the flag "off" is on, specify the member to turn off.  
                In query mode, when used with the flags "stream" and "dataType", query  
                the visualization state of the specified member.  
                Only one member of each shape can be visualized at a time.  
                			In query mode, this flag can accept a value.  
                Properties: create, query
        method (Queryable[str]?): Determine the method of visualization:  
                "color"         convert metadata to a color value and draw the components with the color  
                "ray"           convert metadata to a vector and draw this vector line which starts from the center of the component  
                "string"        display the metadata through 2d string beside the component in the viewport  
                The argument must be a string and must be one of the three words. The default method is "color".  
                If the data type is string, you can only show it with "string" method.  
                In query mode, you can use the flag with no arguments to query the method of a specified stream and member.  
                Properties: create, query
        off (bool?): In create mode, turn off the member which is specified  
                by the flags "stream", "member" and "dataType".  
                Properties: create, query
        range (Queryable[Tuple[float, float]]?): Specify the range of data to use. The value which is out of the range will be clamped to  
                the min/max value.  
                If the method of visualization is "color", the range will be mapped to the color. That means  
                the min value will be displayed in black while the max value will be in white.  
                In query mode, you can use the flag individually to query the current range.  
                Properties: create, query
        rayScale (Queryable[float]?): Specify the scale of the ray to display it with a proper length.  
                Properties: create, query
        stream (Queryable[str]?): In create mode, when used with the flags "member" and "dataType", specify a member to show.  
                If the flag "off" is used, specify the member to turn off.  
                In query mode, when used with the flags "member" and "dataType", query  
                the visualization state of the specified member.  
                When used with the flag "listMembers", query the members in the  
                specified stream.  
                Only one member of each shape can be visualized at a time.  
                			In query mode, this flag can accept a value.  
                Properties: create, query

    Returns:
        str: result of the operation or the queried status

    Example:
    """

