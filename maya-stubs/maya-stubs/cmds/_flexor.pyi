from __future__ import annotations

from typing import *


Unknown = Any

_T = TypeVar("_T")

Queryable = Union[bool, _T]
Multiuse = Union[_T, List[_T]]
Range = Union[Tuple[_T], Tuple[_T, _T]]
NullableRange = Range[Optional[_T]]

def flexor(*args: str, edit: bool = ..., query: bool = ..., atBones: bool = ..., atJoints: bool = ..., deformerCommand: str = ..., list: bool = ..., name: str = ..., noScale: bool = ..., toSkeleton: bool = ..., type: str = ...) -> Union[List[str], bool]:
    """This command creates a flexor. A flexor a deformer plus a set of
    driving    attributes. For example, a flexor might be a sculpt object
    that is driven by a joint's x rotation and a cube's y position.
    Args:
        atBones (bool?): Add a flexor at bones. Flexor will be added at each of the  
                selected bones, or at all bones in the selected skeleton if  
                the -ts flag is also specified.  
                Properties: create
        atJoints (bool?): Add a flexor at joints. Flexor will be added at each of the  
                selected joints, or at all joints in the selected skeleton if  
                the -ts flag is specified.  
                Properties: create
        deformerCommand (str?): String representing underlying deformer command string.  
                Properties: create
        list (bool?): List all possible types of flexors. Query mode only.  
                Properties: query
        name (str?): This flag is obsolete.  
                Properties: create
        noScale (bool?): Do not auto-scale the flexor to the size of the nearby geometry.  
                Properties: create
        toSkeleton (bool?): Specifies that flexors will be added to the entire skeleton  
                rather than just to the selected joints/bones.  
                This flag is used in conjunction with the -ab and -aj flags.  
                Properties: create
        type (str?): Specifies which type of flexor. To see list of valid types,  
                use the "flexor -query -list" command.  
                Properties: create

    Returns:
        List[str]: (the names of the new flexor nodes)

    Example:
    """

